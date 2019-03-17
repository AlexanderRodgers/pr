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
    major = serializers.PrimaryKeyRelatedField(required=False, read_only=True)

    def create(self, validated_data):
        return Review.objects.create(**validated_data)

    # DO THIS NEXT
    def update(self, instance, validated_data):
        pass

    class Meta:
        model = Review
        fields = ('id', 'rating', 'class_grade', 'difficulty', 'class_num', 'major', 'created',
        'user', 'review', 'quarter',)

class ProfessorSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(source='professors', many=True, required=False)
    major = serializers.PrimaryKeyRelatedField(required=False, read_only=True)
    gpa = serializers.SerializerMethodField()

    def create(self, validated_data):
        major_id = validated_data.pop('major')
        print(major_id)
        major = Major.objects.get(id=major_id)
        print(major)
        p = Professor.objects.create(major=major, **validated_data)
        return p

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.major = validated_data.get('major', instance.major)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance

    def get_gpa(self, obj):
        print(obj)
        queryset = Review.objects.filter(professor__first_name=obj.first_name)
        grade_points = { 
            'A+': 4.1, 'A': 4.0, 'A-': 3.7,
            'B+': 3.33, 'B': 3, 'B-': 2.7,
            'C+': 2.3, 'C': 2.0, 'C-': 1.7,
            'D+': 1.3, 'D': 1.0, 'D-': 0.7,
            'F': 0,
        }
        weightings = []
        for review in queryset.values('rating'):
            weightings.append(grade_points[review['rating']])
        if len(weightings) != 0:
            return sum(weightings) / len(weightings)
        return -1

    class Meta:
        model = Professor
        fields = ('id', 'first_name', 'last_name', 'slug','email', 'major', 'reviews', 'gpa')

    
