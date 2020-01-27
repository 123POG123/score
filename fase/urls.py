
from django.urls import path, include
from fase.views import *
from django.conf.urls.static import static



urlpatterns = [


    path('bathtubs/', mixer, name='mixer'),
    path('shower/', shower, name='shower'),
    path('bidet/', bidet, name='bidet'),
    path('sink/', sink, name='sink'),
    path('about_mixer/<int:mix_id>', about_mixer, name='about_mixer'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)

