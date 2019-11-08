from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView
from .models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User as u
#for forms
from .models import Activity
from .form import Activityforms

#for crud
from django.views.generic.edit import CreateView

#for SignUpView
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
# Create your views here.

@login_required

def home(request):
    c = ["aman","Niranjan","Justin"]
    d = str(request.user)
    if d in c:
        a = "aman"
    else:
        a = "other"
    return render(request,'home.html',{"a":a})

class EnterWorking(CreateView):
    model = User
    template_name = 'Working_in.html'
    fields = '__all__'

class ActivityReport(ListView):
    model = Activity
    template_name = 'ActivityReport.html'
    context_name = 'activityreport'


def WorkingDetail(request):
    a = request.user
    print(a)
    if u.objects.get(username = "aman"):
        employ = User.objects.all()
        return render(request,'workingdetail.html',{'employ' : employ})
    else:
        return render(request,'a.html')

def ActivityF(request):
    if request.method == 'POST':
        form = Activityforms(request.POST)

        if form.is_valid():
            new_req = Activity(ActivityName=request.POST['ActivityName'],
            FromDate=request.POST['FromDate'],
            ToDate=request.POST['ToDate'],
            Venue=request.POST['Venue'],
            Country=request.POST['Country'],
            State=request.POST['State'],
            District=request.POST['District'],
            Village_Panchayat=request.POST['Village_Panchayat'],
            ActivityDescription=request.POST['ActivityDescription']
            )
            new_req.save()
            return redirect('home')

    else:
        form = Activityforms()

    context = {'form': form}
    return render(request,'form.html',context)



'''for logout'''
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('login')
