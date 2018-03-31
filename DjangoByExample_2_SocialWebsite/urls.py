"""
Definition of urls for DjangoByExample_2_SocialWebsite.
"""

from django.conf.urls import include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include('account.urls')),
]

if settings.DEBUG:
    # 在调试模式下django负责服务静态文件
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)