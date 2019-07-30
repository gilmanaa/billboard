from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout

app_name = 'socialboard'
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, kwargs={'next_page':'/social'},name='logout'),
    url(r'^register$',views.register,name="register")
]