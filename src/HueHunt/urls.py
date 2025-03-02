from .views import Index
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required


urlpatterns = [
    # Custom views
    path('', login_required(Index.as_view()), name='home'),

    # app urls
    path('account/', include('account.urls')),
    path('payments/', include('payment.urls')),
    path('live_game/', include('live_game.urls')),

    # Django admin
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Custom 404 page handler
handler404 = 'HueHunt.views.custom_404'
