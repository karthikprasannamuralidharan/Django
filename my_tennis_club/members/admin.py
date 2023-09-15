from django.contrib import admin
from .models import Members

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "dob")
    prepopulated_fields = {"slug": ("firstname", "lastname")}

admin.site.register(Members,MemberAdmin)