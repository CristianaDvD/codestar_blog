from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import About


@admin.register(About)
# Register your models here.
class AboutAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)
