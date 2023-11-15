from django.contrib import admin
from .models import Department,Purpose
from .models import Collegepart,CollegepartImage

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Department, DepartmentAdmin)


class PurposeAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Purpose,PurposeAdmin)

class CollegepartAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Collegepart,CollegepartAdmin)

admin.site.register(CollegepartImage)




