from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('sponsors', views.SponsorPage().as_view()),
    path('<int:id>', views.sponsor_update, name='sponsor_update'),
    path('sponsorsdelete/<int:id>/', views.sponsorsdelete, name='sponsorsdelete'),
    path('<int:id>/', views.details, name='details'),
    path('create', views.create_sponsor, name='create_sponsor'),
    path('add', views.add_sponsor, name='add_sponsor'),
    path('sponsordata', views.sponsor_data_update, name='sponsor_data_update')
]
