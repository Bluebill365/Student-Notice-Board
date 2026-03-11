from django.contrib import admin
from .models import Notice

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin): # type: ignore
    list_display = ('title', 'notice_type', 'target_level', 'created_at')
    search_fields = ('title', 'message', 'notice_type')
    filter_horizontal = ('target_students',)