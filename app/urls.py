from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("detail/<int:shop_id>", detailShop, name="detail"),
]
