from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('<int:user_id>/', include('JET.urls')),
    path('admin/', admin.site.urls),
]

#site authentication urls
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
