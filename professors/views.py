from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
import json
from professors.models import *
from professors.serializers import *
from decouple import config
from unipath import Path
BASE_DIR = Path(__file__).parent
DEBUG = config('DEBUG', default=False, cast=bool)
TEMPLATE_DEBUG = DEBUG

# TODO: Refactor to better use the ViewList library

@api_view(['GET', 'POST'])
def captcha_verificatiton(request):
    if request.method == 'POST':
        print(request.data['response'])
        data = { 
            'secret': config('CAPTCHA_SECRET_KEY'),
            'response': request.data['response']
        }
        response = requests.post('https://www.google.com/recaptcha/api/siteverify', data)
        print('response type', type(response.json()))
        serializer = CaptchaSerializer(data=response.json())
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        print(serializer.errors)    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def professor_list(request):

    if (request.method == 'GET'):
        professors = Professor.objects.all()
        serializer = GetProfessorSerializer(professors, many=True)
        return Response(serializer.data)

    elif (request.method == 'POST'):
        serializer = ProfessorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.create(request.data.copy())
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print('data invalid?')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # elif (request.method == 'DELETE'):
    #     for professor in Professor.objects.all():
    #         professor.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def major_list(request):

    if (request.method == 'GET'):
        majors = Major.objects.all()
        serializer = MajorSerializer(majors, many=True)
        return  Response(serializer.data)

    elif (request.method == 'POST'):
        serializer = MajorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)

    # elif (request.method == 'DELETE'):
    #     for majors in Major.objects.all():
    #         majors.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def major_detail(request, slug):
    try:
        major = Major.objects.get(slug=slug)
    except Major.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if (request.method == 'GET'):
        serializer = MajorSerializer(major)
        return Response(serializer.data)

    elif (request.method == 'POST'):
        serializer = MajorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def major_detail_pk(request, pk):
    try:
        major = Major.objects.get(pk=pk)
    except Major.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if (request.method == 'GET'):
        serializer = MajorSerializer(major)
        return Response(serializer.data)

    elif (request.method == 'POST'):
        serializer = MajorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def professor_detail(request, slug):
    try:
        professor = Professor.objects.get(slug=slug)
    except Professor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if (request.method == 'GET'):
        serializer = ProfessorSerializer(professor)
        return Response(serializer.data)

    elif (request.method == 'POST'):
        serializer = ProfessorSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def professor_detail_id(request, pk):
    try:
        professor = Professor.objects.get(pk=pk)
    except Professor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if (request.method == 'GET'):
        serializer = GetProfessorSerializer(professor)
        return Response(serializer.data)

    elif (request.method == 'POST'):
        serializer = ProfessorSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def latest_professor_list(request):
    if (request.method == 'GET'):
        reviews = Review.objects.order_by('-created', 'difficulty')
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def review_list(request):

    if (request.method == 'GET'):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def professor_review(request, pk):
    try:
        reviews = Review.objects.filter(professor__pk=pk)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if (request.method == 'GET'):
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    elif (request.method == 'POST'):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.create(request.data.copy())
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
