from django.conf.urls import url, include
from application import views

urlpatterns = [
    url(r'^index', views.HomeView.as_view(), name="index"),
    url(r'^api/chart/$', views.DispalyGraph.as_view(), name="graph"),
]

