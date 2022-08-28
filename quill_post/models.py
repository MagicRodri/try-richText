from django.db import models
from django_quill.fields import QuillField
# Create your models here.

class QPost(models.Model):
    content = QuillField()