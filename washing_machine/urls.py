from django.urls import path
from . import views

urlpatterns = [
    # path("test",views.test),
    path("",views.WashingMachineListView.as_view()),
    path("book/<int:pk>/",views.WashingMachineUpdateView.as_view())]