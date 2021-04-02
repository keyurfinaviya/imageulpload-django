from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import UploadSerializer
from .models import UserProfile


class UploadViewSet(ModelViewSet):
	serializer_class = UploadSerializer
	queryset = UserProfile.objects.all()
	