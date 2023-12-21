from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django_resized import ResizedImageField
from apps.common.models import BaseModel, Tag
from apps.module.utils import randomize_certificate_number


class Speaker(BaseModel):
    first_name = models.CharField(_("First name"), max_length=255)
    last_name = models.CharField(_("Last name"), max_length=255)
    family_name = models.CharField(_("Family name"), max_length=255)
    position = models.CharField(_("Position"), max_length=255)
    avatar = ResizedImageField(_("Avatar"), upload_to="speaker/avatar/")

    class Meta:
        verbose_name = _("Speaker")
        verbose_name_plural = _("Speakers")
        db_table = "speaker"
        ordering = ("-id",)

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"


class Drug(BaseModel):
    title = models.CharField(verbose_name=_("Title"), max_length=255)

    class Meta:
        verbose_name = _("Drug")
        verbose_name_plural = _("Drugs")
        db_table = "drug"
        ordering = ("-id",)

    def __str__(self):
        return f"{self.id} - {self.title}"


class PharmacistCompany(BaseModel):
    title = models.CharField(verbose_name=_("Title"), max_length=255)

    class Meta:
        verbose_name = _("Pharmacist Company")
        verbose_name_plural = _("Pharmacist Companies")
        db_table = "pharmacist_company"
        ordering = ("-id",)

    def __str__(self):
        return f"{self.id} - {self.title}"


class CourseFiles(BaseModel):
    file = models.FileField(upload_to="education_files", verbose_name=_("File"))
    title = models.CharField(max_length=255, verbose_name=_("Title"))

    class Meta:
        verbose_name = _("Course File")
        verbose_name_plural = _("Course Files")

    def __str__(self):
        return self.title


class Course(BaseModel):
    title = models.CharField(verbose_name=_("Title"), max_length=255)
    description = models.CharField(verbose_name=_("Description"), max_length=255)
    image = ResizedImageField(_("Image"), upload_to="course.py/cover_image/%Y/%m/%d", null=True, blank=True)
    speaker = models.ManyToManyField(to=Speaker, verbose_name=_("Speaker"), blank=True)
    drugs = models.ManyToManyField(to=Drug, verbose_name=_("Drugs"), blank=True)
    pharmacist_company = models.ManyToManyField(to=PharmacistCompany, verbose_name=_("Pharmacist Company"), blank=True)
    disclaimer = models.TextField(verbose_name=_("Disclaimer"))
    course_files = models.ManyToManyField(to=CourseFiles, verbose_name=_("Course Files"), blank=True)
    certificate_html_template = models.FileField(
        verbose_name=_("Certificate HTML Template"),
        upload_to="course_certificate_html_templates",
        null=True,
        help_text=_(
            """Use {{ full_name }} to show user full name.
            Use {{ course_title }} to show course.py title.
            Use {{ qrcode_url }} to show QR code url.
            Use {{ absolute_path }} to show absolute path."""
        ),
    )

    class Meta:
        verbose_name = _("Course")
        verbose_name_plural = _("Courses")
        db_table = "course"
        ordering = ("-id",)

    def __str__(self):
        return f"{self.id} - {self.title}"

    @property
    def number_of_modules(self):
        return self.modules.count()

    def can_course_certificate_be_issued(self, user):
        """Check if all modules of the course.py are completed by the user using aggregation."""
        total_modules_count = self.modules.count()

        # Count the number of modules completed by the user
        completed_modules_count = UserModuleCompletionRequirements.objects.filter(
            module__course=self,  # Modules in this course.py
            user=user,  # For the given user
            is_video_played=True,
            is_files_downloaded=True,
            is_test_passed=True
        ).count()

        # Compare the count of completed modules with the total number of modules
        return completed_modules_count == total_modules_count


class Certificate(BaseModel):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="certificates", verbose_name=_("User")
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="certificates", verbose_name=_("Course"))
    cid = models.CharField(max_length=255, verbose_name=_("CID"), default=randomize_certificate_number)
    file = models.FileField(upload_to="certificates", verbose_name=_("File"), null=True, blank=True)

    class Meta:
        verbose_name = _("Certificate")
        verbose_name_plural = _("Certificates")
        unique_together = ["user", "course"]

    def __str__(self):
        return f"{self.user} - {self.course} - {self.cid}"

    def clean(self):
        # Check if the certificate already exists for the user and course.py
        if Certificate.objects.filter(user=self.user, course=self.course).exists():
            raise ValidationError("Certificate already issued for this course.py.")

        # Check if all course.py modules have been completed by the user
        if not self.course.can_course_certificate_be_issued(self.user):
            raise ValidationError("All course.py requirements have not been met.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


class Module(BaseModel):
    title = models.CharField(verbose_name=_("Title"), max_length=255)
    video = models.FileField(_("Video"), upload_to="module/video")
    cover_image = ResizedImageField(_("Cover Image"), upload_to="module/cover_image/%Y/%m/%d")
    tags = models.ManyToManyField(to=Tag, verbose_name=_("Tags"), blank=True)
    speaker = models.ManyToManyField(to=Speaker, verbose_name=_("Speaker"), blank=True)
    drugs = models.ManyToManyField(to=Drug, verbose_name=_("Drugs"), blank=True)
    pharmacist_company = models.ManyToManyField(to=PharmacistCompany, verbose_name=_("Pharmacist Company"), blank=True)
    module_files = models.ManyToManyField(to=CourseFiles, verbose_name=_("Module Files"), blank=True)
    disclaimer = models.TextField(verbose_name=_("Disclaimer"))
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE, related_name="modules", null=True, blank=True)

    class Meta:
        verbose_name = _("Module")
        verbose_name_plural = _("Modules")
        db_table = "module"
        ordering = ("-id",)

    def __str__(self):
        return f"{self.id} - {self.title}"


class UserModuleCompletionRequirements(BaseModel):
    module = models.ForeignKey(to=Module, on_delete=models.CASCADE, verbose_name=_("Module"))
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("User"))
    is_video_played = models.BooleanField(verbose_name=_("Is Video Played"), default=False)
    is_files_downloaded = models.BooleanField(verbose_name=_("Is Files Downloaded"), default=False)
    is_test_passed = models.BooleanField(verbose_name=_("Is Tests Passed"), default=False)

    class Meta:
        verbose_name = _("UserModuleCompletionRequirement")
        verbose_name_plural = _("UserModuleCompletionRequirements")
        db_table = "user_module_completion_requirements"
        ordering = ("-id",)
        unique_together = ('user', 'module')  # user should have separate one related requirement to each module

    def __str__(self):
        return f"{self.id} - {self.user.first_name}"

    @property
    def can_certificate_be_issued(self):
        """Check if all conditions for issuing a certificate are met."""
        return self.is_video_played and self.is_files_downloaded and self.is_test_passed and self.module.course is None


class TimeCode(BaseModel):
    title = models.CharField(verbose_name=_("Title"), max_length=255)
    order = models.IntegerField(verbose_name=_("Order"))
    start_time = models.DurationField(verbose_name=_("Start Time"))
    end_time = models.DurationField(verbose_name=_("End Time"))
    module = models.ForeignKey(Module, verbose_name=_("Module"), on_delete=models.CASCADE, related_name='timecodes')

    class Meta:
        verbose_name = _("TimeCode")
        verbose_name_plural = _("TimeCodes")
        db_table = "time_code"
        ordering = ("-id",)

    def __str__(self):
        return f"{self.id} - {self.module.title}"
