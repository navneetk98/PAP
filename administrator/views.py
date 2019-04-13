from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .create_database import student_database, professor_database
import os
from .forms import AddBatchForm
from PAP.AdminPass import staff_user_required
from .slot_allotment import slot_allotment
from allotment.algo import allot_mentor


@staff_user_required
def admin_home(request):
    # print(request.POST)
    # print(request.GET)
    all_batches = request.user.admin.batch_set.all()
    batch = {
        "batch": all_batches
    }
    if request.method == 'POST' and request.FILES['prof-data']:
        prof_data = request.FILES['prof-data']
        fs = FileSystemStorage()
        filename = fs.save(prof_data.name, prof_data)
        # fileCSV = open('../'+filename)
        # print(fileCSV)
        current_batch = (request.user.admin.batch_set.all())[0]
        # current_batch = Batch()
        for b in all_batches:
            print(request.POST.get(b.ID), b.ID)
            if request.POST.get(str(b.ID)):
                current_batch = b
                # professor_database(filename, b)
                # b.save()
            # print(b.batch_name)
        professor_database(filename, current_batch)
        print(current_batch.professor_data_uploaded, current_batch.ID)
        current_batch.save()
        os.remove(filename)

    elif request.method == 'GET':
        for b in all_batches:

            if request.GET.get(str(b.ID) + "_team_formation"):
                b.is_team_formation_allowed = not b.is_team_formation_allowed
                b.save()
                print(b.is_team_formation_allowed)

            if request.GET.get(str(b.ID) + "_preference_filling"):
                b.is_preference_filling_allowed = not b.is_preference_filling_allowed
                b.save()
                print(b.is_preference_filling_allowed)

            if request.GET.get(str(b.ID)+"_allotment"):
                allot_mentor(b)
                b.is_mentor_allotted=True
                b.save()

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
        professor_database(filename,)
        os.remove('../' + filename)
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
            b = form.save()
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


@staff_user_required
def prof_details(request, batch_id, prof_id):
    admin = request.user
    admin = admin.admin
    batch = admin.batch_set.filter(ID=batch_id)
    if batch.count() > 0:
        batch = batch[0]
        prof = batch.professor.filter(ID=prof_id)
        if prof.count() > 0:
            prof = prof[0]
            data = {
                "prof": prof
            }
            return render(request, "prof_details.html", data)
    return redirect("/")


@staff_user_required
def view_allotted_groups(request, batch_id):
    batch = request.user.admin.batch_set.filter(ID=batch_id)
    if batch.count() > 0:
        batch = batch[0]
        groups = batch.group_set.all()
        return render(request,"view_groups.html", {"groups": groups})

    return redirect('/administrator')
