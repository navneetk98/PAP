#TODO make URL pattern for this app

"""
URLs ~
/(page with list of all batch and data)
/edit-{batchName}
/create
​
"""
from django.conf.urls import url
from django.urls import path

from . views import upload_professor as professor_upload_view
from . views import admin_home, add_batch, prof_details, view_allotted_groups

urlpatterns = [
    url(r'^upload/professor$', professor_upload_view, name='professor_upload'),
    url(r'^$', admin_home, name='admin_home'),
    url(r'^add-batch$', add_batch, name='add-batch'),
    path('<int:batch_id>/professor-<int:prof_id>', prof_details, name='prof_details'),
    path('<int:batch_id>', view_allotted_groups, name='groups-details'),
]
