from django.urls import path
from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [
    path('', views.index, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('product/', views.product, name='shop'),
    path('orders/', OrdersView.as_view(), name = 'orders')
]  + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)