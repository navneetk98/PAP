from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .create_database import student_database, professor_database
import os
from . forms import AddBatchForm
from PAP.AdminPass import staff_user_required


@staff_user_required
def upload_students(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        # fileCSV = open('../'+filename)
        # print(fileCSV)
        student_database('../' + filename)
        os.remove('../'+filename)
        uploaded_file_url = fs.url(filename)
        return render(request, 'simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'simple_upload.html')


@staff_user_required
def upload_professor(request):
        if request.method == 'POST' and request.FILES['myfile']:
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            # fileCSV = open('../'+filename)
            # print(fileCSV)
            professor_database('../' + filename)
            os.remove('../'+filename)
            uploaded_file_url = fs.url(filename)
            return render(request, 'simple_upload.html', {
                'uploaded_file_url': uploaded_file_url
            })
        return render(request, 'simple_upload.html')


@staff_user_required
def add_batch(request):
        if request.method == 'POST':
            form = AddBatchForm(request.POST)
            if form.is_valid():
                form.save()
