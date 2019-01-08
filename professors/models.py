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

    @classmethod
    def gpa(cls):
        #this is a bad thing to do.
        grade_points = {
            'A+': 4.1,
            'A': 4.0,
            'A-': 3.7,
            'B+': 3.33,
            'B': 3,
            'B-': 2.7,
            'C+': 2.3,
            'C': 2.0,
            'C-': 1.7,
            'D+': 1.3,
            'D': 1.0,
            'D-': 0.7,
            'F': 0,
        }
        weightings = []
        for grade in Review.objects.values('rating'):
            weightings.push(grade_points[grade])
        overall_rating = sum(weightings) / (len(weightings) - 1)
        return overall_rating

    class Meta: 
        ordering = ('class_grade',)
    