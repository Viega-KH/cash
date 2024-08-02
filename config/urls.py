from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.views.static import serve
from django.urls import path, include, re_path

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path('site/', include('uisoff.urls')),
    path('', include('account.urls')),
] 

urlpatterns += [
   re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
   static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
]

