from __future__ import unicode_literals
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
import bcrypt, re
from ..login_registration.models import User

# Create your models here.



class TravelsManager(models.Manager):
    def add_travel(self,data,user):

        print data,"this is the user -->",user,user['id']


        id = int(user['id'])
        dbUser = User.objects.get(id=id)

        # try:
        #     book_author = data['author2']
        # except:
        #     book_author = data['author']

        new_travel = Travels(
        destination=data['destination'],
        traveler=dbUser,
        description=data['description'],
        travel_from=data['travel_from'],
        travel_to=data['travel_to']
        )

        new_travel.save()

        print new_travel
        # record = self.create(author=request.POST['author'])

        # print review,"this is the dictionary"
        return (True)








# Create your models here.
class Travels(models.Model):
    destination = models.CharField(max_length=255)
    traveler = models.ForeignKey(User)
    travel_from = models.DateTimeField(null=True)
    travel_to = models.DateTimeField(null=True)
    description = models.CharField(max_length=255)
    objects = TravelsManager()
