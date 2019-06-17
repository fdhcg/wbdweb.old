from django.conf.urls import url, include
from myapp import views

urlpatterns = [url(r'add_label$', views.add_label, ),url(r'show_label$', views.show_label, ),url(r'pull_data$', views.pull_data,)]
