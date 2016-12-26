from __future__ import unicode_literals
from django.core.exceptions import ObjectDoesNotExist
from django.utils.datastructures import MultiValueDictKeyError
from django.db import models
import bcrypt, re
from ..login_registration.models import User

class QuotesManager(models.Manager):
    def add_quote(self,data,user):
        print "this is the data >",data
        id = int(user['id'])
        dbUser = User.objects.get(id=id)
        print dbUser


        quote = Quotes(
        quote = data['quote'],
        posted_by = dbUser,
        quoted_by = data['quoted_by'],
        )

        quote.save()
        print "running add_quote",quote
        print quote.quote,quote.posted_by

        return (True)


# Create your models here.
class Quotes(models.Model):
    quote = models.CharField(max_length=255)
    posted_by = models.ForeignKey(User)
    quoted_by = models.CharField(max_length=45)
    objects = QuotesManager()
