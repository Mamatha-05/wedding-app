from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('vendor',views.login_view,name='login'),
    path('logout',views.logout_view,name='logout'),
    path('login',views.admin_login_view,name='Admin'),
    path('Register',views.Register_view,name='register'),
    path('add-wedding',views.add_wedding,name='wedding_add'),
    path('create-vendor',views.vendor_details,name='vendor_details'),
    path('services',views.service_list,name='services'),
    path('Weddings-view',views.weddings_view,name='weddings_view'),
    path('wedding-vendor',views.wedding_vendor,name='wedding_vendor'),
    path('add-vendors/<int:pk>/',views.add_vendors,name='add_vendors'),
    path('delete-vendor/<int:pk>/',views.delete_vendor,name='delete_vendor'),
    path('check-vendor-list',views.wedding_vendor_list,name='check_vendor_list'),
    path('wedding-vendor-list/<int:pk>/',views.wedding_vendors_check,name='wedding_vendor_list'),
    path('my-vendor-list/<int:pk>/',views.vendor_wedding_requests,name="vendor_wedding_requests"),
    path('my-vendor-list',views.my_vendor_list,name="my_vendor_list"),
    path('confirmation/<int:pk>/',views.vendor_confirmation,name="vendor_confirmation"),
    path('check-confirmed',views.check_confirmed,name="check_confirmed"),
    path('check-confirm/<int:pk>/',views.confirmed_data,name="check_confirm_list")
]
