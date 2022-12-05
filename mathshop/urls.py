"""mathshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from market import views
from . import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="home"),
    path('market-place/', views.marketPlace, name="market-place"),
    path('transaction/', views.transaction, name="transaction"),
    path('add-product/', views.addProduct, name="add-product"),
    path('add-product/add/', views.addProductRecord, name="add"),
    path('update-product/<int:id>', views.updateProduct, name="update"),
    path('update-product/record/<int:id>', views.updateProductRecord, name="update record"),
    path('delete-product/<int:id>', views.deleteProduct, name="delete"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

