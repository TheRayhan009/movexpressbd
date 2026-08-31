from django.contrib import admin
from django.urls import path
from django.contrib.sitemaps.views import sitemap

from main import views
from main.sitemaps import StaticViewSitemap


# Sitemap configuration
sitemaps = {
    "static": StaticViewSitemap,
}


urlpatterns = [

    # Admin
    path('admin/', admin.site.urls),

    # Website pages
    path('', views.home, name="home"),
    path('order/', views.order, name="order"),
    path('founderrayhan/', views.founderrayhan, name="founderrayhan"),
    path('founderarafat/', views.founderarafat, name="founderarafat"),

    # XML Sitemap
    path(
        'sitemap.xml',
        sitemap,
        {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'
    ),
]