from django.contrib import admin
from django.urls import path
from django.contrib.sitemaps.views import sitemap
from main import views
from main.sitemaps import StaticViewSitemap


sitemaps = {
    "static": StaticViewSitemap,
}


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name="home"),
    path('order/', views.order, name="order"),
    path('founderrayhan/', views.founderrayhan, name="founderrayhan"),
    path('founderarafat/', views.founderarafat, name="founderarafat"),

    # Sitemap
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
]