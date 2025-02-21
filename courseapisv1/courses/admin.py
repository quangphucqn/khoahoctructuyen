from django.contrib import admin
from courses.models import Category ,Course
from django.utils.html import mark_safe

class MyCourseAdmin(admin.ModelAdmin):
    list_display = ['id','subject','active','created_date','category']
    search_fields = ['subject']
    list_filter = ['id','created_date']
    list_editable = ['subject']
    readonly_fields = ['image_view']

    def image_view(self,course):
        return mark_safe(f"<img src='/static/{course.image.name}' width='120'/>")

admin.site.register(Category)
admin.site.register(Course,MyCourseAdmin)




