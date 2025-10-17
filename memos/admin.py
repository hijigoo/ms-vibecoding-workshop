from django.contrib import admin
from .models import Memo


@admin.register(Memo)
class MemoAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'is_public', 'created_at')
    search_fields = ('title', 'body', 'author__username')
    list_filter = ('is_public', 'created_at')
