from django.conf.urls import url
from . import views

urlpatterns=[
  url(r'^index/$',views.index),
  url(r'^Register/$',views.Registration),
  url(r'^saveData/', views.saveData),
  url(r'^Rooms/', views.Rooms),
  url(r'^Room_Save/', views.Room_Save),
  url(r'^EmptyRoom/', views.EmptyRoom),
  url(r'^EnterTzId/', views.EnterTzId),
]