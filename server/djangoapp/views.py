from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
# from .models import related models

# from .restapis import related methods
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.
def Home(request):
    return render(request,'djangoapp/index.html',{})

# Create an `about` view to render a static about page
# def about(request):
# ...
def about(request):
   return render(request,'djangoapp/about.html',{})
    

# Create a `contact` view to return a static contact page
def contact(request):
    return render(request,'djangoapp/contact.html',{})

# Create a `login_request` view to handle sign in request
# def login_request(request):
# ...
def login_request(request):
    if request.method== "POST":
        username=request.POST['username']
        password=request.POST['psw']
        user=authenticate(username=username,password=password)
        login(request,user)
        return redirect('djangoapp:home')
       
    else:
        return render(request, 'djangoapp/registration.html', {})
    
def logout_request(request):
    
    # Get the user object based on session id in request
    print("Log out the user `{}`".format(request.user.username))
    # Logout user in the request
    logout(request)
    return redirect('djangoapp:home')
    # Redirect user back to course list view
def registration_request(request):
    if request.method=="GET":
        return render(request,'djangoapp/registration.html',{})
    elif request.method=="POST":
            username = request.POST['username']
            password = request.POST['psw']
            first_name = request.POST['firstname']
            last_name = request.POST['lastname']
            user_exist = False
            try:
                User.objects.get(username=username)
                user_exist=true
            except :
                  logger.debug("{} is new user".format(username))
            if not user_exist:

            # Create user in auth_user table
                    user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                            password=password)
 
                    login(request, user)
                    return redirect('djangoapp:home')
            else:

                 return render(request, 'djangoapp/registration.html', {})



           


# Create a `registration_request` view to handle sign up request
# def registration_request(request):
# ...

# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
    context = {get_dealers_from_cf}
    if request.method == "GET":
        return render(request, 'djangoapp/index.html', context)


# Create a `get_dealer_details` view to render the reviews of a dealer
# def get_dealer_details(request, dealer_id):
# ...

# Create a `add_review` view to submit a review
# def add_review(request, dealer_id):
# ...
def get_dealerships(request):
    if request.method == "GET":
        url = "your-cloud-function-domain/dealerships/dealer-get"
        # Get dealers from the URL
        dealerships = get_dealers_from_cf(url)
        # Concat all dealer's short name
        dealer_names = ' '.join([dealer.short_name for dealer in dealerships])
        # Return a list of dealer short name
        return HttpResponse(dealer_names)
