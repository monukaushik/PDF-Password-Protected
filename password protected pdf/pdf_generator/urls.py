from django.contrib import admin
from django.urls import path
from pdf_generator_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.getpdf),
]
