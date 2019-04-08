from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from .create_batch import create_database
import os


def simple_upload(request):
    user = request.user
    # print(user.is_staff)
    if user.is_staff:
        if request.method == 'POST' and request.FILES['myfile']:
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            # fileCSV = open('../'+filename)
            # print(fileCSV)
            create_database('../'+filename)
            os.remove('../'+filename)
            uploaded_file_url = fs.url(filename)
            return render(request, 'simple_upload.html', {
                'uploaded_file_url': uploaded_file_url
            })
        return render(request, 'simple_upload.html')
    else:
        return HttpResponse("<h1>You are not allowed here</h1>")
