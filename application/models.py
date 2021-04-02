from django.db import models
import os
from django.core.exceptions import ValidationError


def validate_file_extension(value):
	ext = os.path.splitext(value.name)[1]
	print((value.name)[1])
	valid_extensions = ['.png']
	if not ext.lower() in valid_extensions:
		raise ValidationError('Unsupported file type')


class UserProfile(models.Model):
	prof_img = models.ImageField(upload_to='images/', validators=[validate_file_extension])