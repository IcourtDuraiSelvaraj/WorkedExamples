from signIn.signup_form import Signup_Form
from django.shortcuts import render
from django.http import HttpResponse
import datetime


def home(request):
    now = datetime.datetime.now()
    signup = Signup_Form()
    return render(request, "Home.html", {'form': signup,
                                         'curr_date': now,
                                         })

def signup(request):
    signup = Signup_Form()
    return render(request, "signup.html", {'form': signup,

                                           })
