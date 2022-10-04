from django.urls import path, include
from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
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
    #url(r'^listss/$|^$', views.TicketList.as_view()),
    url(r'^list/$|^$', views.list_tickets, name="listss"),
    url(r'^tickets/api/list/$|^tickets/api/$', views.list_tickets, name="listsss"),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.ticket_detail, name="detailss"),
    url(r'^tickets/api/detail/(?P<pk>[0-9]+)/$', views.ticket_detail, name="detailsss"),
    #url(r'^details/(?P<pk>[0-9]+)/$', views.TicketList.as_view(), name="detailsss"),
    url(r'^tickets/api/detail/(?P<pk>[0-9]+)/update/$', views.ticket_detail, name="updatess"),
    url(r'^tickets/api/detail/(?P<pk>[0-9]+)/update/$', views.ticket_detail, name="updatesss"),
    #url(r'^tickets/api/detail/(?P<pk>[0-9]+)/delete/$', views.ticket_detail, name="deletess"),
    url(r'^action/newticket/$', views.new_ticket, name="newss"),
    url(r'^tickets/api/action/newticket/$', views.new_ticket, name="newsss"),
	url(r'^tickets/api/action/(?P<pk>[0-9]+)/delete/$', views.delete_ticket, name="deletesss"),
	#url(r'^action/deleteticket/$', views.delete_ticket, name="deletesss"),
    url(r'^action/login/$', views.account_login, name="loginss"),
    url(r'^action/logout/$', views.account_logout, name="logoutss"),
    url(r'^tickets/api/action/login/$', views.account_login, name="loginsss"),
    url(r'^tickets/api/action/logout/$', views.account_logout, name="logoutsss"),
    #path('action/<int:id>/updatess/', views.update_ticket, name="updatess"),
    #path('action/<int:id>/deletess/', views.delete_ticket, name="deletess"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
