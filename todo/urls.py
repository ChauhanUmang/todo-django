from django.urls import path
from todo import views

urlpatterns = [
    path('addTask/', views.addTask, name="addTask"),
    # in the url, whatever name we have given after int:<variable name>
    # should be same as the name in the function in the view
    # here, we have named it task_id, so we should have a task_id parameter
    # in the function
    # if named it pk, like we usually do, we should have a parameter named pk
    # in the function
    path('mark_as_done/<int:task_id>/', views.mark_as_done, name="mark_as_done"),
]
