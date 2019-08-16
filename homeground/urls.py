from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.welcome, name= 'welcome'),
    url(r'^new/business$', views.new_business, name='new-business'),
    url(r'^new/community$', views.new_community, name='new-community'),
    url(r'^new/comment$',views.new_comment, name='new-comment'),
    url(r'community/business/all/(\d+)/', views.businesses, name="businesses"),
    url(r'community/resident/all',views.residents, name="residents"),
    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)