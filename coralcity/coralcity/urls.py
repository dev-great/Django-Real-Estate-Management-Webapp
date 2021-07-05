from django.contrib import admin
from django.urls import path, include


from django.conf import settings
from django.conf.urls.static import static

from appartments import views
from howitworks import views
from about import views
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('listings/', include('listings.urls')),
    path('', include('accounts.urls')),
    path('', include('appartments.urls')),
    path('', include('about.urls')),
    path('', include('howitworks.urls')),
]


urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



admin.site.site_header ="Coralcity control panel"
admin.site.index_title ="Administrators dashboard"
admin.site.site_title ="Control panel"