from __future__ import unicode_literals
from django.core.exceptions import ObjectDoesNotExist
from django.utils.datastructures import MultiValueDictKeyError
from django.db import models
import bcrypt, re

# Create your models here.

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def validateReg(self, request):
        print request.POST
        errors = self.validate_inputs(request)

        if len(errors) > 0:
            return (False, errors)

        #if no errors, hash the password
        print request.POST['password'],"current password here"
        pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())

        #password is hashed, create the User
        curr_user = {'request.POST' :
         ['first_name','last_name','email']
         }

        print curr_user


        user = self.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'],email=request.POST['email'],pw_hash=pw_hash)


        return (True, user)

    def validate_inputs(self,request):
        errors=[]
        if len(request.POST['first_name']) < 2 or len(request.POST['last_name']) < 2:
            errors.append("Incomplete Name, minimum characters not met")
        if not EMAIL_REGEX.match(request.POST['email']):
            errors.append("email address problem")
        if len(request.POST['password']) < 8 or request.POST['password'] != request.POST['cpassword']:
            errors.append("Passwords must match and be at least 8 characters long")
        if self.user_exists(request):
            errors.append("You already have a login")
        return errors

    def user_exists(self, request):
        email = request.POST['email']
        if User.objects.filter(email=email):
            return (True)

    def validate_login(self,request):
        try:
            user=User.objects.get(email=request.POST['email'])
            password=request.POST['password'].encode()
            print password
            if bcrypt.hashpw(password, user.pw_hash.encode()) == user.pw_hash:
                print password,"provided password"
                print user.pw_hash.encode(),"hashed db pw"
                return(True, user)
            # if not request.GET['email']:
            #     errors.append('email field is empty')
            # return (False, errors)
        except ObjectDoesNotExist:
            pass
        return (False, ["Email/password doesnt match"])


class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    pw_hash = models.CharField(max_length=255)
    dob = models.DateField(max_length=8)

    objects = UserManager()


    #Initial generation
# hashed = bcrypt.hashpw(password, bcrypt.gensalt())
#Store hashed in your db

#Load hashed from the db and check the provided password
# if bcrypt.hashpw(password, hashed) == hashed:
#     print "It matches"
# else:
#     print "It does not match"
