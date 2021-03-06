from rest_framework import serializers
from professors.models import *

class CaptchaSerializer(serializers.Serializer):
    success = serializers.BooleanField()
    challenge_ts = serializers.DateTimeField()
    hostname = serializers.CharField(max_length=None)

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
    professor = serializers.PrimaryKeyRelatedField(required=False, read_only=True)

    def create(self, validated_data):
        for key in list(validated_data.keys()):
            if 'professor' == key:
                professor_id = validated_data.pop('professor')
                professor = Professor.objects.get(id=professor_id)
            if 'major' == key:
                major_id = validated_data.pop('major')
                major = Major.objects.get(id=major_id)
        if major and professor:
            return Review.objects.create(professor=professor, major=major, **validated_data)
        else:
            return Review.objects.create(**validated_data)            

    def update(self, instance, validated_data):
        pass

    class Meta:
        model = Review
        fields = ('id', 'rating', 'class_grade', 'difficulty', 'class_num', 'major', 'created',
        'user', 'review', 'quarter', 'professor')
        
class ProfessorSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(source='professors', many=True, required=False)
    major = serializers.PrimaryKeyRelatedField(required=False, read_only=True)
    # gpa = serializers.SerializerMethodField()

    def create(self, validated_data):
        if type(validated_data) is not dict:
            print('data is not a dict.')
            validated_data = validated_data.dict()
        print('validated data', validated_data)
        if 'major' in validated_data.keys():
            major_id = validated_data.pop('major')
            major = Major.objects.get(id=major_id)
            p = Professor.objects.create(major=major, **validated_data)
            return p
        else:
            p = Professor.objects.create(**validated_data)
            return p

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.major = validated_data.get('major', instance.major)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance

    class Meta:
        model = Professor
        fields = ('id', 'first_name', 'last_name', 'slug','email', 'major', 'reviews')

class GetProfessorSerializer(serializers.ModelSerializer):
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
        queryset = Review.objects.filter(professor__id=obj.id)
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