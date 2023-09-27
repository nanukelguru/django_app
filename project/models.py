from django.db import models

# Create your models here.
#from rest_framework.authentication import JWTAuthentication


#@authentication_classes([JWTAuthentication])

class Articulo(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)
