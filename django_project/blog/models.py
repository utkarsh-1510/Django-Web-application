from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# class Post(models.Model):
#     title = models.CharField(max_length=100)
#     content = models.TextField()
#     date_posted = models.DateTimeField(default=timezone.now)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.title

class FypaperPdf(models.Model):
    Caption = models.CharField(max_length=100)
    pdf=models.FileField(upload_to="pdf/%y")

    def __str__(self):
        return self.Caption

class FybookPdf(models.Model):
    Caption = models.CharField(max_length=100)
    pdf1=models.FileField(upload_to="pdf1/%y")

    def __str__(self):
        return self.Caption

class SypaperPdf(models.Model):
    Caption = models.CharField(max_length=100)
    pdf=models.FileField(upload_to="pdf/%y")

    def __str__(self):
        return self.Caption

class SybookPdf(models.Model):
    Caption = models.CharField(max_length=100)
    pdf1=models.FileField(upload_to="pdf1/%y")

    def __str__(self):
        return self.Caption

class TypaperPdf(models.Model):
    Caption = models.CharField(max_length=100)
    pdf=models.FileField(upload_to="pdf/%y")

    def __str__(self):
        return self.Caption

class TybookPdf(models.Model):
    Caption = models.CharField(max_length=100)
    pdf1=models.FileField(upload_to="pdf1/%y")

    def __str__(self):
        return self.Caption