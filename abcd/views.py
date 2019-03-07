from django.shortcuts import render,redirect
from abcd.forms import Todoform
from abcd.models import Todo
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from abcd.forms import UserRegistrationForm
from django.conf import settings
import requests
from django_cron import CronJobBase, Schedule
from django.contrib.auth.decorators import login_required
from abcde.tasks import Alert

# Create your views here.

def register_view(request):
    if request.user.is_authenticated:
        return redirect("show")
    else:
        title = "Create an Account"
        form = UserRegistrationForm(
            request.POST or None,
            request.FILES or None
            )

        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get("password1")
            user.set_password(password)
            user.save()
            new_user = authenticate(email=user.email, password=password)
            login(request, new_user)

            return HttpResponseRedirect(reverse('show'))

        context = {"title": title, "form": form}

        return render(request, "todo/form.html", context)



def user_login(request):
    context = {}
    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']


        ''' Begin reCAPTCHA validation '''
        recaptcha_response = request.POST.get('g-recaptcha-response')
        data = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()
        ''' End reCAPTCHA validation '''

        if result['success']:
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('show'))
            else:
                context["error"] = "Provide valid credentials !!"
                return render(request, "todo/login.html", context)
        else:
            context["error"] = "Please fill the captcha"
            return render(request, "todo/login.html", context)

    else:
        return render(request, "todo/login.html", context)



def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('user_login'))



def add_task(request):
    if request.method == "POST":
        form = Todoform(request.POST)
        if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('show'))
    else:
        form = Todoform()
    return render(request,'todo/index.html',{'form':form})


def show(request):
    todotask = Todo.objects.all()
    return render(request,"todo/show.html",{'todotask':todotask})

def destroy(request, id):
    todotask = Todo.objects.get(id=id)
    todotask.delete()
    return HttpResponseRedirect(reverse('show'))


def crossoff(request, id):
    item = Todo.objects.get(id=id)
    item.task_completed = True
    item.save()
    return HttpResponseRedirect(reverse('show'))

def uncross(request, id):
    item = Todo.objects.get(id=id)
    item.task_completed = False
    item.save()
    return HttpResponseRedirect(reverse('show'))


def mail(request):
    if request.user.is_authenticated:
        user = request.user
        email = user.email
        if datetime.datetime.now() == Todo.time:
            gmail
            smtp
            subject = 'ALARM'
            from_email = settings.EMAIL_HOST_USER
            to_email = ['email':email]
            contact_message = "Your Task is Pending"
            send_mail(subject, contact_message, from_email, [to_email], fail_silently=True)

        else:
            Alert.delay()
    else:
        return HttpResponseRedirect(reverse('login'))







# class MyCronJob(CronJobBase):
#     RUN_EVERY_MINS = 120 # every 2 hours
#
#     schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
#     code = 'my_app.my_cron_job'    # a unique code
#
#     def do(self):
#         pass    # do your thing here
#

