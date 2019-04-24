from django.db import models
from datetime import date
from django.utils.text import slugify
from django.db.models.signals import pre_save
from professors.utils import slug_generator
from professors.validators import difficulty, class_num, quarter, grade_system

class Major(models.Model):
    major = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=15)
    slug = models.SlugField(max_length=100, default='')

    def __str__(self):
        return "%s" % (self.major)

def slug_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slug_generator(instance, instance.major, instance.slug)
pre_save.connect(slug_save, sender=Major)

class Professor(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(null=True)
    created = models.DateField(auto_now_add=True)
    major = models.ForeignKey(Major, null=True, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, default='')

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

def slug_professor(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slug_generator(instance, 
        instance.first_name + " " + instance.last_name, instance.slug)
pre_save.connect(slug_professor, sender=Professor)

class Review(models.Model):
    rating = models.CharField(max_length=2, validators=[grade_system])
    class_grade = models.CharField(max_length=2, null=True, validators=[grade_system])
    difficulty = models.IntegerField(validators=[difficulty])
    class_num = models.IntegerField(validators=[class_num])
    # major = models.CharField(max_length=50)
    created = models.DateField(auto_now_add=True)
    user = models.CharField(max_length=200, default="Anonymous")
    review = models.CharField(max_length=10000)
    quarter = models.IntegerField(validators=[quarter])
    professor = models.ForeignKey(Professor, related_name="professors", on_delete=models.CASCADE, null=True)
    major = models.ForeignKey(Major, on_delete=models.CASCADE, null=True)

    class Meta: 
        ordering = ('class_grade',)
    