from django.contrib import admin
from django.urls import path
from tax_app import views

urlpatterns = [
    path('', views.default_view),
    path('<int:number>/', views.calculate_tax),
    path('taxrate/', views.tax_rate_view),
    path('admin/', admin.site.urls),
]
