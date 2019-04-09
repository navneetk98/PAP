#TODO make URL pattern for this app

"""
URLs ~
/(page with list of all batch and data)
/edit-{batchName}
/create
​
"""
from django.conf.urls import url
from . views import upload_students as student_upload_view
from . views import upload_professor as professor_upload_view

urlpatterns = [
    url(r'^upload/students$', student_upload_view, name='student_upload'),
    url(r'^upload/professor$', professor_upload_view, name='professor_upload'),
]