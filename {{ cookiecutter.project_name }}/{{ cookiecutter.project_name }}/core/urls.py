from django.urls import path

from . import views

urlpatterns = [
    path(".well-known/security.txt", views.security_txt),
    path("robots.txt", views.robots_txt),
    path("android-chrome-192x192.png", views.favicon),
    path("android-chrome-512x512.png", views.favicon),
    path("apple-touch-icon.png", views.favicon),
    path("browserconfig.xml", views.favicon),
    path("favicon-16x16.png", views.favicon),
    path("favicon-32x32.png", views.favicon),
    path("favicon.ico", views.favicon),
    path("mstile-150x150.png", views.favicon),
    path("safari-pinned-tab.svg", views.favicon),
]
