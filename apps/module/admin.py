from django.contrib import admin
from apps.module.models import (Speaker, Drug, PharmacistCompany, CourseFiles, Course, Module, TimeCode,
                                Certificate, UserModuleCompletionRequirements)

admin.site.register(Drug)
admin.site.register(PharmacistCompany)
admin.site.register(CourseFiles)
admin.site.register(TimeCode)
admin.site.register(UserModuleCompletionRequirements)


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ("id", "title",  "created_at")
    list_display_links = ("id", "title")
    search_fields = ("title",)
    list_filter = ("created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at")


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ("id", "cid", "user",  "course")
    list_display_links = ("id", "cid")
    search_fields = ("cid",)
    list_filter = ("created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at")


@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name",  "position")
    list_display_links = ("id", "first_name")
    search_fields = ("first_name", "last_name")
    list_filter = ("created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at")


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "title",)
    list_display_links = ("id", "title")
    search_fields = ("title",)
    list_filter = ("created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at")
