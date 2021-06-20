from django.contrib import admin

# Register your models here.
from .models import Answer, Question

admin.site.register(Question)
admin.site.register(Answer)