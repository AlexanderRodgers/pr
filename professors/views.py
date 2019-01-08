from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from professors.models import *
from professors.serializers import *

@api_view(['GET', 'POST', 'DELETE'])
def professor_list(request):

    if (request.method == 'GET'):
        professors = Professor.objects.all()
        serializer = ProfessorSerializer(professors, many=True)
        return Response(serializer.data)

    elif (request.method == 'POST'):
        serializer = ProfessorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif (request.method == 'DELETE'):
        for professor in Professor.objects.all():
            professor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

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
        return Resposne(serializer.erros, status=status.HTTP_400_BAD_REQUEST)
