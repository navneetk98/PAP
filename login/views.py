from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from . forms import SignUpForm
from tf.models import TeamFormation
from django.contrib.auth.models import User

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.cpi = form.cleaned_data.get('cpi')
            user.profile.tier = form.cleaned_data.get('tier')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)

            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def home(request):
    if not request.user.teamformation.slot_no:
        stri=request.user.teamformation.requests
        stri2 = stri.split(',')
        print(stri2)
        # g=stri2.len()
        users = User.objects.filter(teamformation__slot_no__exact=1)
        context = {
            "string": stri2,
            "all": users
            # "length": g
        }
        return render(request,'normal_login.html', context)
    else:

        users = User.objects.filter(teamformation__slot_no__exact=-1)
        for u in users:
            print(u.id)
            if request.POST.get(str(u.id)):
                std = User.objects.filter(id=u.id)
                std = std[0]
                print(std.teamformation.requests)
                std.teamformation.requests = std.teamformation.requests + ',' + str(request.user.teamformation.group_id)
                std.teamformation.save()
        context = {
            "all":users
        }
        return render(request,'leader_login.html', context)
    return render(request, 'home.html')

def site_home(request):
    return render(request,'site_home.html')

def update_group(request ,idd):
    request.user.teamformation.group_id = idd
    return redirect('home')

def leader_send(request ,usrname):
    sel_user=User.objects.filter(username__exact= usrname)
    sel_user.teamformation.requests.append(request.user.teamformation.group_id)
    return redirect('home')