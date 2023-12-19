from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path , include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', TemplateView.as_view(template_name ='home.html'), name='home'),
    path('registration/', include('registration.urls')),
    path('', include('profile_page.urls')),
    path('', include('search.urls')),
    path('', include('chat.urls')),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
