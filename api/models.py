from django.db import models
from django.utils import timezone
from django.db import models
from datetime import datetime

class Header(models.Model):
    title_en = models.CharField(max_length=255, null=True, blank=True)
    title_ar = models.CharField(max_length=255, null=True, blank=True)
    videofile= models.FileField(upload_to = 'videos/', null=True, verbose_name="")
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    linkedin_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    slider_img1 = models.ImageField(null=True, blank=True)
    slider_img2 = models.ImageField(null=True, blank=True)
    slider_img3 = models.ImageField(null=True, blank=True)
    slider_text_en = models.CharField(max_length=255, null=True, blank=True)
    slider_text_ar = models.CharField(max_length=255, null=True, blank=True)
    slider_header_en = models.CharField(max_length=255, null=True, blank=True)
    slider_header_ar = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return self.title_en or ''
  

class About(models.Model):
    title_en = models.CharField(max_length=255, null=True, blank=True)
    body_en= models.Tbody_ar= models.TextField(null=True, blank=True)
    title_ar = models.CharField(max_length=255, null=True, blank=True)
    body_ar= models.TextField(null=True, blank=True)
    number_of_project = models.IntegerField(null=True , blank=True)
    number_of_Awards=models.IntegerField(null=True , blank=True)
    Years_of_experience=models.IntegerField(null=True , blank=True)
    number_of_client= models.IntegerField(null=True , blank=True)
    about_image = models.ImageField(upload_to= 'Home/', max_length=254,null=True, blank=True)
    def __str__(self):
        return self.title_en or ''


class Client(models.Model):
    client_name_en = models.CharField(max_length=255)
    client_name_ar =models.CharField(max_length=255)
    review_message_en = models.TextField(null=True, blank=True)
    review_message_ar = models.TextField(null=True, blank=True)
    img = models.ImageField(upload_to='Home/', max_length=254,null=True, blank=True)
    def __str__(self):
        return self.client_name_en or ''    
class mision_vision(models.Model):
    title_en = models.CharField(max_length=255)
    title_ar = models.CharField(max_length=255)
    body_en =  models.TextField(null=True, blank=True)
    body_ar =  models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title_en or ''
class why_home(models.Model):
    title_en = models.CharField(max_length=255)
    title_ar = models.CharField(max_length=255)

    def __str__(self):
        return self.title_en or ''
class Service(models.Model):
    title_en = models.CharField(max_length=255)
    title_ar = models.CharField(max_length=255)
    body_en =  models.TextField(null=True, blank=True)
    body_ar =  models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title_en or ''
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    subject = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.email


class project(models.Model):
    img = models.ImageField(upload_to='Home/', max_length=254,null=True, blank=True)
class SubCategory(models.Model):
    name_en = models.CharField(max_length=150)
    name_ar = models.CharField(max_length=150)
    img = models.ImageField(upload_to='product/')
    def __str__(self):
        return self.name_en or ''
class Tag(models.Model):
    name_en = models.CharField(max_length=150)
    name_ar = models.CharField(max_length=150)
    description_en = models.TextField(blank=True)
    description_ar = models.TextField(blank=True)
    img_slider = models.ImageField(upload_to='product/' ,null=True, blank=True)
    img_description = models.ImageField(upload_to='product/' ,null=True, blank=True)
    def __str__(self):
        return self.name_en or ''
class ProductHdl (models.Model):
    SubCategory = models.ForeignKey(SubCategory ,on_delete=models.CASCADE)
    name_en = models.CharField(max_length=300)
    name_ar = models.CharField(max_length=300)
    description_en = models.TextField(null=True , blank=True)
    description_ar = models.TextField(null=True , blank=True)
    slug = models.SlugField(max_length=150)
    image_1 = models.ImageField(upload_to='product/',null=True, blank=True)
    image_2 = models.ImageField(upload_to='product/',null=True, blank=True)
    image_3 = models.ImageField(upload_to='product/',null=True, blank=True)
    image_4 = models.ImageField(upload_to='product/',null=True, blank=True)
    image_5 = models.ImageField(upload_to='product/',null=True, blank=True)
    videofile= models.FileField(upload_to='videos/', null=True,blank=True)

    def __str__(self):
        return self.name_en
class ProductTuya(models.Model):
    SubCategory = models.ForeignKey(SubCategory ,on_delete=models.CASCADE)
    name_en = models.CharField(max_length=300)
    name_ar = models.CharField(max_length=300)
    tag = models.ForeignKey(Tag ,on_delete=models.CASCADE )
    description_en = models.TextField(null=True , blank=True)
    description_ar = models.TextField(null=True , blank=True)
    slug = models.SlugField(max_length=300)
    image_1 = models.ImageField(upload_to='product/',null=True, blank=True)
    image_2 = models.ImageField(upload_to='product/',null=True, blank=True)
    image_3 = models.ImageField(upload_to='product/',null=True, blank=True)
    image_4 = models.ImageField(upload_to='product/',null=True, blank=True)
    image_5 = models.ImageField(upload_to='product/',null=True, blank=True)
    videofile= models.FileField(upload_to='videos/', null=True, blank=True)
    def __str__(self):
        return self.name_en


class Video(models.Model):
    videofile_1= models.FileField(upload_to='videos/', null=True, blank=True)
    videofile_2= models.FileField(upload_to='videos/', null=True, blank=True)
    videofile_3= models.FileField(upload_to='videos/', null=True, blank=True)
    videofile_4= models.FileField(upload_to='videos/', null=True, blank=True)
    videofile_5= models.FileField(upload_to='videos/', null=True, blank=True)

