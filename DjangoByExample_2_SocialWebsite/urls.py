"""
Definition of urls for DjangoByExample_2_SocialWebsite.
"""

from django.conf.urls import include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include('account.urls')),
]
