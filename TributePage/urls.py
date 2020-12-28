from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/',include('core.urls')),
    path("user/", include("users.urls.users_urls")),
    path("account/", include("users.urls.account_urls")),
]
media_url = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
static_url = static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += media_url
urlpatterns += static_url
