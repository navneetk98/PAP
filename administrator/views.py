from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .create_database import student_database, professor_database
import os
from . forms import AddBatchForm
from PAP.AdminPass import staff_user_required
from . slot_allotment import slot_allotment


@staff_user_required
def admin_home(request):
    all_batches = request.user.admin.batch_set.all()
    batch = {
        "batch" : all_batches
    }
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        # fileCSV = open('../'+filename)
        # print(fileCSV)
        current_batch=(request.user.admin.batch_set.all())[0]
        #current_batch = Batch()
        for b in all_batches:
            print(request.POST.get(b.ID), b.ID)
            if request.POST.get(str(b.ID)):
                current_batch=b
                #professor_database(filename, b)
                #b.save()
            #print(b.batch_name)
        professor_database(filename, current_batch)
        print(current_batch.professor_data_uploaded, current_batch.ID)
        current_batch.save()
        os.remove(filename)
        return render(request, 'admin_home.html', batch)
    return render(request, 'admin_home.html', batch)


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
        if request.method == 'POST' and request.FILES['myfile']:
            form = AddBatchForm(request.POST)
            if form.is_valid():
                b=form.save()
                b.admin = request.user.admin
                b.save()
                myfile = request.FILES['myfile']
                fs = FileSystemStorage()
                filename = fs.save(myfile.name, myfile)
                # fileCSV = open('../'+filename)
                # print(fileCSV)
                student_database(filename, b)
                os.remove(filename)
                slot_allotment(b)
                return redirect("/administrator/")
        else:
            form = AddBatchForm()
        return render(request, 'add_batch.html', {'form': form})

