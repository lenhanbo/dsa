from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
# from django.contrib.auth 
urlpatterns = [
    # path('', include('members.urls')),
    # path('shop/', include('shopping.urls')),
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [

    path('accounts/', include('django.contrib.auth.urls')),
]