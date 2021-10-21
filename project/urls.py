from rest_framework.routers import DefaultRouter
from api import views
from django.conf.urls.static import static
from rest_framework.response import Response
from django.contrib import admin
from django.urls import path,include               
from rest_framework import routers                 
from django.conf.urls.static import  static
from django.conf import settings
router = DefaultRouter()
router.register(r'Header', views.HeaderViewSet)
router.register(r'About', views.AboutViewSet)
router.register(r'Service', views.ServiceViewSet)
router.register(r'Client', views.ClientViewSet)
router.register(r'SubCategory', views.SubCategoryViewSet)
router.register(r'Tag', views.TagViewSet)
router.register(r'ProductTuya', views.ProductTuyaViewSet)
router.register(r'ProductHdl', views.ProductHdlViewSet)
router.register(r'mision_vision', views.mision_visionViewSet)
router.register(r'why_home', views.why_homeViewSet)
router.register(r'project', views.projectViewSet)
router.register(r'Video', views.VideoViewSet)


admin.site.site_header ='Home automation website admin interface'
admin.site.site_title ='Home automation website admin'
admin.site.index_title = 'Home automation adminstrations'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/Contactus/',views.ContactCreateView.as_view(),name='contactus'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
