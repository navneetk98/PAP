#TODO make URL pattern for this app

"""
URLs ~
/(page with list of all batch and data)
/edit-{batchName}
/create
​
"""
from django.conf.urls import url
from . views import simple_upload as upload_view

urlpatterns = [
    url(r'^upload/$', upload_view, name='upload'),
]