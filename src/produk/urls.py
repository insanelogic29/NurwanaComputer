from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('detail_produk/<id>', views.detail_produk, name="detail_produk"),
		path('beli_produk/<id>', views.beli_produk, name="beli_produk"),
		path('invoice/<id>', views.invoice, name="invoice"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('beli_produk', views.contact, name="contact"),
    path('keranjang', views.keranjang, name="keranjang"),

]