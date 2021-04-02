from rest_framework.serializers import ModelSerializer
from .models import UserProfile



class UploadSerializer(ModelSerializer):
	class Meta:
		model = UserProfile
		fields = ['prof_img']
	# file_uploaded = ImageField(upload_to='images/')
	# class Meta:
	# 	fields = ['file_uploaded']