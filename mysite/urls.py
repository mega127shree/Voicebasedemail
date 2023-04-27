from django.contrib import admin
from django.conf.urls import url, include
admin.autodiscover()
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include('homepage.urls')),
    
]
