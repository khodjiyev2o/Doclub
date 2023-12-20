from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.common.models import BaseModel, Tag
from django_resized import ResizedImageField


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
    image = ResizedImageField(_("Image"), upload_to="course/cover_image/%Y/%m/%d")
    speaker = models.ManyToManyField(to=Speaker, verbose_name=_("Speaker"))
    drugs = models.ManyToManyField(to=Drug, verbose_name=_("Drugs"))
    pharmacist_company = models.ManyToManyField(to=PharmacistCompany, verbose_name=_("Pharmacist Company"))
    disclaimer = models.TextField(verbose_name=_("Disclaimer"))

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


class Module(BaseModel):
    title = models.CharField(verbose_name=_("Title"), max_length=255)
    video = models.FileField(_("Video"), upload_to="module/video")
    cover_image = ResizedImageField(_("Cover Image"), upload_to="module/cover_image/%Y/%m/%d")
    tags = models.ManyToManyField(to=Tag, verbose_name=_("Tags"))
    speaker = models.ManyToManyField(to=Speaker, verbose_name=_("Speaker"))
    drugs = models.ManyToManyField(to=Drug, verbose_name=_("Drugs"))
    pharmacist_company = models.ManyToManyField(to=PharmacistCompany, verbose_name=_("Pharmacist Company"))
    module_files = models.ManyToManyField(to=CourseFiles, verbose_name=_("Module Files"))
    disclaimer = models.TextField(verbose_name=_("Disclaimer"))
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE, related_name="modules", null=True, blank=True)

    class Meta:
        verbose_name = _("Module")
        verbose_name_plural = _("Modules")
        db_table = "module"
        ordering = ("-id",)

    def __str__(self):
        return f"{self.id} - {self.title}"


class TimeCode(BaseModel):
    order = models.IntegerField(verbose_name=_("Order"))
    start_time = models.DurationField(verbose_name=_("Start Time"))
    end_time = models.DurationField(verbose_name=_("End Time"))
    module = models.ForeignKey(Module, verbose_name=_("Module"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("TimeCode")
        verbose_name_plural = _("TimeCodes")
        db_table = "time_code"
        ordering = ("-id",)

    def __str__(self):
        return f"{self.id} - {self.module.title}"
