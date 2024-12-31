from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from .views import CustomLoginView, home_view, forgot_password
from account.views import account_view, payment_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/',
         CustomLoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/',
         auth_views.LogoutView.as_view(next_page='/accounts/login/'), name='logout'),
    path('account/', login_required(account_view), name='account'),
    path('payments/', login_required(payment_view), name='payment'),
    path('', login_required(home_view), name='home'),
    path('forgot-password/', forgot_password, name='forgot_password'),
    path('live_game/', include('live_game.urls')),
]

handler404 = 'HueHunt.views.custom_404'

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
