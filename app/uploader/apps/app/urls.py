from django.conf.urls import url, include
from . import views


urlpatterns = [
	url('^favs/', 
		views.FavoriteListView.as_view(), 
		name='favs'),

	url('^ticket/(?P<pk>[0-9]+)/', 
		views.TicketDetailView.as_view(), 
		name='ticket')

]
