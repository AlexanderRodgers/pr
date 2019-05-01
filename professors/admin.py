from django.contrib import admin
from .models import Professor, Review, Major

# Register your models here.
admin.site.register(Professor)
admin.site.register(Review)
admin.site.register(Major)