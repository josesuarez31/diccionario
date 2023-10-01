from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    # ex: /polls/
    path("", views.IndexView.as_view(), name="index"),  # Muestra todos
    # ex: /polls/5/
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),  # Muestra uno
    # ex: /polls/5/results/
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),  # Muestra el resultado despues de votar
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"), # Este lo usamos para guardar el voto
]