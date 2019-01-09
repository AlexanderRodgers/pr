from django.db import models
from datetime import date
# Create your models here.

class Major(models.Model):
    major = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=15)

class Professor(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(null=True)
    major = models.ForeignKey(Major, related_name="majors", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class Review(models.Model):
    # Needs Min/Max validation
    rating = models.CharField(max_length=2)
    class_grade = models.CharField(max_length=2, null=True)
    difficulty = models.IntegerField()
    class_num = models.IntegerField()
    major = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=200)
    review = models.CharField(max_length=10000)
    year_taken = models.DateField(null=True)
    quarter = models.IntegerField()
    professor = models.ForeignKey(Professor, related_name="professors", on_delete=models.CASCADE,
    null=True)
    major = models.ForeignKey(Major, related_name="review_major", on_delete=models.CASCADE, null=True)

    class Meta: 
        ordering = ('class_grade',)
    