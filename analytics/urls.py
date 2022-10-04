from django.urls import path, include
from django.conf.urls import url
from . import views
#from .views import (
    #TicketCreateAPIView,
    #TicketDeleteAPIView,
    #TicketDetailAPIView,
    #TicketListAPIView,
    #TicketUpdateAPIView,
#    )
#from rest_framework import routers

"""
router = routers.DefaultRouter()
router.register('tickets', views.TicketViewSet, basename='tickets-list')
#router.register(r'my-model/', MyModelView, basename='MyModel')

urlpatterns = [
    path('', include(router.urls)),

    #path('tickets/list/', TicketListAPIView, name='List'),
    #path('tickets/<int:id>/', TicketDetailAPIView, name='Detail'),
    #path('tickets/update/<int:id>/', TicketUpdateAPIView, name='Update'),
    #path('tickets/delete/<int:id>/', TicketDeleteAPIView, name='Delete'),
]
"""

app_name = 'tickets'

urlpatterns = [
    #path('', views.TicketListView.as_view(), name="list"),
    #path('<int:id>/', views.TicketDetailView.as_view(), name="detail"),
    #path('<int:id>/update/', views.TicketUpdateView.as_view(), name="update"),
    #path('<int:id>/delete/', views.TicketDeleteView.as_view(), name="delete"),

    #url(r'^$', views.list_tickets, name="listsss"),
    url(r'^list/$|^$', views.list_tickets, name="listss"),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.ticket_detail, name="detailss"),
    url(r'^action/(?P<pk>[0-9]+)/update/$', views.ticket_detail, name="updatess"),
    url(r'^action/(?P<pk>[0-9]+)/delete/$', views.ticket_detail, name="deletess"),

    #path('action/<int:id>/updatess/', views.update_ticket, name="updatess"),
    #path('action/<int:id>/deletess/', views.delete_ticket, name="deletess"),
]
