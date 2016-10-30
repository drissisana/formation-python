from django.db import models

# Create your models here.

class Post(models.Model):#creation class de type model
    title =models.CharField(max_length=80) # chaine de caractere max80
    contenu =models.TextField() # contenu texte

    def __str__(self):
        return self.title #pour specifier les postes