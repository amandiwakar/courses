from __future__ import unicode_literals
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
import bcrypt, re
from ..login_registration.models import User

# Create your models here.

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class ReviewsManager(models.Manager):
    def add_book_review(self,data,user):

        print data,"this is the user -->",user,user['id']


        id = int(user['id'])
        dbUser = User.objects.get(id=id)
        rating = int(data['rating'])

        try:
            book_author = data['author2']
        except:
            book_author = data['author']

        new_review = Reviews(
        title=data['title'],
        author=book_author,
        review=data['review'],
        rating=rating,
        reviewer=dbUser,
        )

        new_review.save()

        print new_review
        # record = self.create(author=request.POST['author'])

        # print review,"this is the dictionary"
        return (True)


class UserManager(models.Manager):
    pass


class Reviews(models.Model):
    title = models.CharField(max_length=45)
    author = models.CharField(max_length=45)
    rating = models.CharField(max_length=5)
    review = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    reviewer = models.ForeignKey(User)

    objects = ReviewsManager()
