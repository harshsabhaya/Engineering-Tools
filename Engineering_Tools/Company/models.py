from django.db import models
import os
import random
# Create your models here.


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    new_filename = instance.c_name + "_" + str(random.randint(1,1000))
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "Company/{final_filename}".format(final_filename=final_filename)


class Register(models.Model):
    c_name = models.CharField(max_length = 50, unique = True)
    c_email = models.EmailField()
    c_password = models.CharField(max_length = 16)
    c_r_password = models.CharField(max_length = 16)

    def __str__(self):
        return self.c_name


class Company_Profile(models.Model):
    c_name = models.CharField(max_length = 50)
    c_phone = models.CharField(max_length = 10)
    c_street = models.TextField()
    c_area = models.TextField()
    c_city = models.TextField()
    c_state = models.TextField()
    c_country = models.TextField()
    c_pincode = models.CharField(max_length = 6)
    c_logo = models.ImageField(upload_to = upload_image_path)
    c_website = models.URLField(max_length = 200)
    c_linkedin = models.URLField(max_length = 200)


    def __str__(self):
        return self.c_name



