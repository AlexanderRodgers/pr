from professors.models import Professor, Review, Major
from professors.serializers import GetProfessorSerializer, ReviewSerializer, MajorSerializer
from rest_framework import generics

class ProfessorQuery(generics.ListAPIView):
    queryset = Professor.objects.all()
    serializer_class = GetProfessorSerializer

    def get_queryset(self):
        return super().get_queryset()