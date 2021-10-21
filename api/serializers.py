from rest_framework import serializers
from .models import *
class  AboutSerializer (serializers.ModelSerializer):
    class Meta:
        model = About
        exclude = ['title_en', 'body_en', 'title_ar','body_ar']
class AboutArSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='title_ar')
    content = serializers.CharField(source='body_ar')

    class Meta(AboutSerializer.Meta):
        pass

class AboutEnSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='title_en')
    content = serializers.CharField(source='body_en')

    class Meta(AboutSerializer.Meta):
        pass
    
class  HeaderSerializer (serializers.ModelSerializer):
    class Meta:
        model = Header
        exclude = ['title_en', 'slider_text_en','slider_header_en','title_ar', 'slider_text_ar','slider_header_ar']
class HeaderArSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='title_ar')
    slider_text = serializers.CharField(source='slider_text_ar')
    slider_header = serializers.CharField(source='slider_header_ar')

    class Meta(HeaderSerializer.Meta):
        pass

class HeaderEnSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='title_en')
    slider_text = serializers.CharField(source='slider_text_en')
    slider_header = serializers.CharField(source='slider_header_en')


    class Meta(HeaderSerializer.Meta):
        pass
    
class  mision_visionSerializer (serializers.ModelSerializer):
    class Meta:
        model = mision_vision
        exclude = ['title_en', 'body_en', 'title_ar','body_ar']
class mision_visionArSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='title_ar')
    content = serializers.CharField(source='body_ar')

    class Meta(mision_visionSerializer.Meta):
        pass

class mision_visionEnSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='title_en')
    content = serializers.CharField(source='body_en')
    class Meta(mision_visionSerializer.Meta):
        pass
    
class  why_homeSerializer (serializers.ModelSerializer):
    class Meta:
        model = why_home
        exclude = ['title_en','title_ar']
class why_homeArSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='title_ar')
   

    class Meta(why_homeSerializer.Meta):
        pass

class why_homeEnSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='title_en')
 
    class Meta(why_homeSerializer.Meta):
        pass
   
class  ServiceSerializer (serializers.ModelSerializer):
    class Meta:
        model = Service
        exclude = ['title_en', 'body_en', 'title_ar','body_ar']
class ServiceArSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='title_ar')
    content = serializers.CharField(source='body_ar')

    class Meta(ServiceSerializer.Meta):
        pass

class ServiceEnSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='title_en')
    content = serializers.CharField(source='body_en')
    class Meta(ServiceSerializer.Meta):
        pass

class  ClientSerializer (serializers.ModelSerializer):
    class Meta:
        model = Client
        exclude = ['client_name_en', 'client_name_ar', 'review_message_en','review_message_ar']
class ClientArSerializer(serializers.ModelSerializer):
    client = serializers.CharField(source='client_name_ar')
    review = serializers.CharField(source='review_message_ar')

    class Meta(ClientSerializer.Meta):
        pass

class ClientEnSerializer(serializers.ModelSerializer):
    client = serializers.CharField(source='client_name_en')
    review = serializers.CharField(source='review_message_en')

    class Meta(ClientSerializer.Meta):
        pass
    

class ProductHdlSerializer (serializers.ModelSerializer):
    class Meta:
        model = ProductHdl
        exclude = ['name_en', 'name_ar', 'description_ar','description_en']
        
class ProductHdlArSerializer(serializers.ModelSerializer):
    Name = serializers.CharField(source='name_ar')
    description= serializers.CharField(source='description_ar')
    SubCategory = serializers.CharField(source='SubCategory.name_ar')

    class Meta(ProductHdlSerializer.Meta):
        pass
class ProductHdlEnSerializer(serializers.ModelSerializer):
    Name = serializers.CharField(source='name_en')
    description = serializers.CharField(source='description_en')
    SubCategory = serializers.CharField(source='SubCategory.name_en')


    class Meta(ProductHdlSerializer.Meta):
        pass
    



class  ProductTuyaSerializer (serializers.ModelSerializer):
    class Meta:
        model = ProductTuya
        exclude = ['name_en', 'name_ar', 'description_ar','description_en']
        
class ProductTuyaArSerializer(serializers.ModelSerializer):
    Name = serializers.CharField(source='name_ar')
    description= serializers.CharField(source='description_ar')
    tag = serializers.CharField(source='tag.name_ar')
    class Meta(ProductTuyaSerializer.Meta):
        pass
class ProductTuyaEnSerializer(serializers.ModelSerializer):
    Name = serializers.CharField(source='name_en')
    description = serializers.CharField(source='description_en')
    tag = serializers.CharField(source='tag.name_en')



    class Meta(ProductTuyaSerializer.Meta):
        pass
    

class  TagSerializer (serializers.ModelSerializer):
    class Meta:
        model = Tag
        exclude = ['name_en', 'name_ar', 'description_ar','description_en']
        
class TagArSerializer(serializers.ModelSerializer):
    Name = serializers.CharField(source='name_ar')
    description= serializers.CharField(source='description_ar')
    class Meta(TagSerializer.Meta):
        pass
class TagEnSerializer(serializers.ModelSerializer):
    Name = serializers.CharField(source='name_en')
    description = serializers.CharField(source='description_en')


    class Meta(TagSerializer.Meta):
        pass
    
class  SubCategorySerializer (serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        exclude = ['name_en', 'name_ar']
        
class SubCategoryArSerializer(serializers.ModelSerializer):
    Name = serializers.CharField(source='name_ar')
    class Meta(SubCategorySerializer.Meta):
        pass
class SubCategoryEnSerializer(serializers.ModelSerializer):
    Name = serializers.CharField(source='name_en')


    class Meta(SubCategorySerializer.Meta):
        pass
    

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = project
        fields ='__all__'

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields ='__all__'

class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields ='__all__'


