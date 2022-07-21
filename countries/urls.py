from django.urls.conf import path
from countries import views

urlpatterns = [
    path(r'^api/countries$', views.countries_list),
    path(r'^api/countries/(?P<pk>[0-9]+)$', views.countries_detail)

]
