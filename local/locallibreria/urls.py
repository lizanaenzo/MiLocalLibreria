from django.contrib import admin
from django.conf.urls import include, url

urlpatterns = [
    url(r'^admin/',admin.site.urls),
    url(r'^catalog/',include ('catalog.urls')),
]

admin.site.site_header = "Administración de Mundo Películas"
admin.site.index_title = "Mundo Películas"
admin.site.site_title = "mundo películas"
