from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from . models import Author, Poem, UserProfile, Line
from random import randint
from poetry.forms import UserForm, UserProfileForm
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.core import serializers
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
import json
# Create your views here.

def index(request):
    all_authors = Author.objects.all()
    featured_poem = Poem.objects.all()[2]
    context = {'all_authors' : all_authors, 'featured_poem' : featured_poem}
    return render(request, 'poetry/index.html', context)
def poemdetail(request, poem_id):
    thepoem = Poem.objects.get(pk = poem_id)
    if request.user.is_authenticated:
        if request.user.profile.poemfavorites.filter(pk = poem_id).exists():
            isfavorite = True;
        else:
            isfavorite = False;
    context = {'thepoem' : thepoem, 'isfavorite' : isfavorite}
    return render(request, 'poetry/poem.html', context)
def authordetail(request, author_id):
    author = Author.objects.get(pk = author_id)
    context = {"author" : author}
    return render(request, 'poetry/author.html', context)
def explore(request):
    num = randint(1,5)
    origPoem =Poem.objects.get(pk = num)
    theauthor = origPoem.writer.name
    thepoem = serializers.serialize("json", [origPoem], indent=2, use_natural_foreign_keys=True, use_natural_primary_keys=True)
    context ={'thepoem': thepoem}
    if request.is_ajax():
        return HttpResponse(thepoem, content_type ='application/json')
    else:
        return render(request, 'poetry/explore.html', {"origPoem" : origPoem})

@csrf_protect
def register(request):

    registered = False
    if request.method == 'POST':
        user_form = UserForm(data = request.POST)
        profile_form = UserProfileForm(data = request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit = False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
        else:
            print (user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request, 'poetry/register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username, password = password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/poetry/')
            else:
                return HttpResponse("Account Disactivated")
        else:
            print ("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details")
    else:
        return render(request, 'poetry/login.html', {})
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/poetry/')

@login_required
def account_page(request):
    return render(request, 'poetry/account.html', {})

@login_required
@csrf_exempt
def favorite(request):
        if request.method == 'POST':
            if request.user.is_authenticated():
                selectedpoem =  Poem.objects.get(pk = request.POST['poemNum'])
                if request.user.profile.poemfavorites.filter(pk = request.POST['poemNum']).exists():
                    request.user.profile.poemfavorites.remove(selectedpoem)
                else:
                    request.user.profile.poemfavorites.add(selectedpoem)
                return HttpResponse("Success")
            else:
                return HttpResponse("you aint authenticated my dude")
        else:
            return HttpResponse("Bruh what?")


@csrf_exempt
def favoriteline(request):
    if request.method == 'POST':
        selectedpoem = Poem.objects.get(pk = request.POST['poemNum'])
        newline = Line(poem = selectedpoem, thewords = request.POST['theselected'])
        newline.save()
        if request.user.is_authenticated():
            request.user.profile.linefavorite.add(newline)
        return HttpResponse(newline.thewords)
    else:
        return HttpResponse("Nope")
