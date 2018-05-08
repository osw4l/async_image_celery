from django.conf.urls import url, include
from rest_framework import routers
from . import views, viewsets

router = routers.DefaultRouter()
router.register(r'images', viewsets.ImageTicketViewSet)
router.register(r'tickets-images', viewsets.TicketViewSet)

urlpatterns = [
    url(r'^viewsets/', include(router.urls)),

    url(r'^tickets/', views.TicketListApiView.as_view()),

]
