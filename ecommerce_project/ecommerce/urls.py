from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

#  настройки деплоя на хостинг для того, что бы MEDIA и SATAIC файлы искались в корне проекта а не в папке piblic
# from django.views.static import serve as mediaserve
# from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),
    # path('__debug__/', include('debug_toolbar.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#  настройки деплоя на хостинг для того, что бы MEDIA и SATAIC файлы искались в корне проекта а не в папке piblic
# else:
#     urlpatterns += [
#         url(f'^{settings.MEDIA_URL.lstrip("/")}(?P<path>.*)$',
#             mediaserve, {'document_root': settings.MEDIA_ROOT}),
#         url(f'^{settings.STATIC_URL.lstrip("/")}(?P<path>.*)$',
#             mediaserve, {'document_root': settings.STATIC_ROOT}),
#     ]