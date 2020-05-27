from django.contrib import admin
from django.urls import path, re_path
from django.urls.conf import include


urlpatterns = [
    path('admin/', admin.site.urls),

    re_path(r'^accounts/', include('accounts.urls')),
    re_path(r'^', include('customer.urls')),
    #re_path(r'^seller/', include('seller.urls')),

]
