from django.urls import path
from professor.views import professors_list_view,professor_create_view
"""
URLs ~
/(list of all professors)
/q-{query} (for searching profesor)
​
"""

#TODO make URL pattern for this app

app_name = 'professors'
urlpatterns = [
    path('', professors_list_view, name='professors-list'),
    path('create/', professor_create_view),
    ]
