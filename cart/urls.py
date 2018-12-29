from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from allauth.account import views as allauthviews

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^profiles/', include('accounts.urls', namespace='accounts')),
    url(r'^products/', include('products.urls', namespace='products')),
    url(r'^cart/', include('shopping_cart.urls', namespace='shopping_cart')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^$', allauthviews.login),
    url(r'/logout', allauthviews.logout)
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
