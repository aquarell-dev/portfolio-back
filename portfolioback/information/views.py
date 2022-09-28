from rest_framework import generics

from .models import Skill
from .serializers import InfoSerializer


class InfoListView(generics.ListAPIView):
    queryset = Skill.objects.all()
    serializer_class = InfoSerializer
