#TODO make URL pattern for this app

"""
URLs ~
/(page with list of all batch and data)
/edit-{batchName}
/create
​
"""
from django.conf.urls import url
from . views import upload_professor as professor_upload_view
from . views import admin_home, add_batch

urlpatterns = [
    url(r'^upload/professor$', professor_upload_view, name='professor_upload'),
    url(r'^$', admin_home, name='admin_home'),
    url(r'^add-batch$', add_batch, name='add-batch'),
]
