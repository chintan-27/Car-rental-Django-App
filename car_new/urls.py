from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.indexView, name="home"),
    path('registercar/',views.registerCar,name="carregister"),
    path('dashboard/', views.dashboardView,name="dashboard"),
    path('login/',LoginView.as_view(),name="login_url"),
    path('register/',views.registerView,name="register_url"),
    path('logout/',LogoutView.as_view(next_page='home'),name="logout"),
    path('rent/',views.rentNow,name="rent"),
    path('loc/',views.loc,name="loc"),
    path('carrented/<int:id>/<str:date>/',views.carRented,name="carrented"),
    path('bill/<int:id>/',views.locs,name="locs"),
    path('rented/<str:car_num>/<str:date>/',views.rented,name="rented"),
    path('booked/',views.booked,name="booked"),
]
urlpatterns+= staticfiles_urlpatterns()
urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
