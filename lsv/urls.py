from django.urls import path

from . import views

app_name = "lsv"
urlpatterns = [
    # ex: /lsv/
    path("", views.IndexView.as_view(), name="index"),  # Muestra todos
    # ex: /lsv/5/
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),  # Muestra uno
]