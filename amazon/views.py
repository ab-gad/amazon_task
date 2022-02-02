from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import myUsers, Track, Trainee, Intake
from django.contrib.auth.models import User #auth user table in DB
from django.contrib.auth import authenticate, login as authlogin, logout as authlogout
from .forms import CreateTrackForm, CreateTraineeModelform, CreateIntakeModelform
from django.views import View #to use class based Views
from django.views.generic import ListView

# Using Generic class based Views for listing
# When using generic classes > REMEBER  (template name ,tempelate path & context) are Crucial 
# .. and there all are class type dependant
# >> Type here is ListView which mean : template(model_list.html), template Must be in a folder with the same of the app (app/model_list), context(object_list)
# NOTICE > in  
class TrackList(ListView):
    model = Track

# Using Class based views
class CreateIntake(View):
    context = {}
    intakeForm = CreateIntakeModelform()
    def get(self, request):
        self.context['intakeForm'] = self.intakeForm
        return render(request, 'createIntake.html', self.context)

    def post(self, request):
        self.context['intakeForm'] = self.intakeForm
        filledForm = CreateIntakeModelform(request.POST)
        filledForm.save()
        self.context['msg'] = 'Intake Created Successfully'
        return render(request, 'createIntake.html', self.context)

#Inserting Trainee date once more using forms.ModelForm
def createTrainee(request):
    context = {}
    traineeForm =  CreateTraineeModelform()
    if (request.method == 'GET'):
        context['traineeForm'] = traineeForm
        return render(request, 'createTrainee.html', context)
    else:
        filledForm = CreateTraineeModelform(request.POST)
        filledForm.save()
        context['msg'] = 'Trainee Created Successfully'
        return render(request, 'createTrainee.html', context)


#Inserting Track Data using forms.Form 
def createTrack (request):
    context = {}
    trackForm = CreateTrackForm()
    if (request.method == 'GET'):
        context['trackForm'] = trackForm
        return render(request, 'createTrack.html', context)
    else:
        data = {'name' : request.POST['name']}
        f = CreateTrackForm(data)
        if (f.is_valid()):
            print("VALID", request.POST['name'])
            Track.objects.create(name=request.POST['name'])
            context = {}
            context['msg'] = 'Track Created Successfully'
            return render(request, 'createTrack.html', context)
        else:
            context = {}
            context['msg'] = 'err'
            return render(request, 'createTrack.html', context)

def register(request):
    context = {}
    if (request.method == 'GET'):
        return render(request, 'register.html', context)
    else:
        myUsers.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=request.POST['password'])

        # NOTICE using create_user or create_superuser when dealing with User model
        User.objects.create_user(username=request.POST['first_name'], password=request.POST['password'], is_staff=True)
        return redirect(login) 

def login(request):
    if (request.method == 'GET'):
        return render(request,'login.html')
    else:
        try:
            user = myUsers.objects.all().filter(email=request.POST['email'], password=request.POST['password'])
            # user = myUsers.objects.all().filter(email<colName>=request.POST['email'<inputName>], password=request.POST['password'])
            authuser = authenticate(username = user[0].first_name, password=request.POST['password'])
            
            print(authuser, user[0].first_name)
            #username = user[0].first_name
            if (len(user) > 0 and authuser is not None):
                
                context = {}
                context['first_name'] = user[0].first_name
                context['last_name'] = user[0].last_name
                print(context)
                print(authuser)
                request.session['user'] = context
                
                authlogin(request, authuser)
                
                return redirect('/amazon/home/')
        except:
            context = {}
            context ['errmsg'] = 'inValid cred'
            return render(request, 'login.html', context)

# def checklogin(request):
#     if (request.method == 'POST'):
#         return redirect(home)

def home(request):
    try: 
        if(request.session['user'] is not None):
            return render(request,'home.html')
    except:
        return redirect(login)


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def nav(request):
    return render(request, 'nav.html')

def create(request):
    # myForm = CreateUserForm()
    context ={}
    # context['form'] = myForm
    if (request.method == 'GET'):
        return render(request, 'create.html')
    else:
        intakInstance = Intake.objects.get(id = request.POST['intake_id'])
        trackInstance = Track.objects.get(id = request.POST['intake_id'])

        Trainee.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], intake_id = intakInstance, track_id=trackInstance)
        context = {}
        context['msg'] = 'Trainee has been Created Successfully'
        return render(request, 'create.html', context)

def read(request):
    if (request.method == 'GET'):
        return render(request, 'read.html')
    else:
        id = request.POST['id']
        if (id == '*'):
            alltrainees = Trainee.objects.all()
            context = {}
            context['alltrainees'] = alltrainees
            return render(request, 'read.html', context)
        else:
            try:
                selectedtrainee = Trainee.objects.get(id = request.POST['id'])
                print(selectedtrainee.first_name)
                context = {}
                context['selectedtrainee'] = selectedtrainee
                return render(request, 'read.html', context)
            except:
                context = {}
                context['msg'] = 'Trainee You Try To Get Is Not Found'
                return render(request, 'read.html', context)

def update(request, id):
    if (request.method == 'GET'):
        selectedtrainee = Trainee.objects.get(id = id)
        context = {}
        print(selectedtrainee.first_name)
        context['selectedtrainee'] = selectedtrainee
        return render(request, 'update.html', context)
    else:
        intakInstance = Intake.objects.get(id = request.POST['intake_id'])
        trackInstance = Track.objects.get(id = request.POST['intake_id'])

        Trainee.objects.filter(id = id).update(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], intake_id = intakInstance, track_id=trackInstance)
        context = {}
        context['msg'] = "Trainee has been updated successfull"
        return render(request, 'update.html', context)

        
def delete(request, id):
    Trainee.objects.filter(id=id).delete()
    return redirect('/amazon/read/')

def logout(request):
    request.session.clear()
    return redirect(login)
