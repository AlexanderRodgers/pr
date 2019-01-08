from rest_framework import serializers
from professors.models import *

class MajorSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Major.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.major = validated_data.get('major', instance.major)
        instance.abbreviation = validated_data.get('abbreviation', instance.abbreviation)

    class Meta:
        model = Major
        fields = ('__all__')

class ReviewSerializer(serializers.ModelSerializer):
    gpa = serializers.SerializerMethodField(method_name='gpa')
    major = MajorSerializer(source='majors', many=True, required=False)

    def create(self, validated_data):
        return Review.objects.create(**validated_data)

    # DO THIS NEXT
    def update(self, instance, validated_data):
        pass

    class Meta:
        model = Review
        fields = ('id', 'rating', 'class_grade', 'difficulty', 'class_num', 'major', 'created',
        'user', 'review', 'year_taken', 'quarter', 'gpa')

    def get_gpa(self, obj):
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

class ProfessorSerializer(serializers.ModelSerializer):
    # Review serializer would be read only. If writing is needed
    # create() and update() methods are required.
    reviews = ReviewSerializer(source='professors', many=True, required=False)
    major = MajorSerializer(source='majors', many=True, required=False)

    def create(self, validated_data):
        return Professor.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.major = validated_data.get('major', instance.major)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance

    class Meta:
        model = Professor
        fields = ('id', 'first_name', 'last_name', 'email', 'major','reviews')