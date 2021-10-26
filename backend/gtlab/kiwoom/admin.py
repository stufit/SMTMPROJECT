from django.contrib import admin
from .models import textboard, MemberInfo
# Register your models here.

admin.site.register(textboard)
class MemberInfoAdmin(admin.ModelAdmin):
    list_display = ('username','email','password','created_at','updated_at')
admin.site.register(MemberInfo,MemberInfoAdmin)
