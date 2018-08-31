from django.db.utils import IntegrityError
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from .models import Group, User_Groups, Pictures
from .forms import Register_form, Login_form, Group_form, Post_form, Post_form_within_group, Pictures_form
from django.core.exceptions import ObjectDoesNotExist
from methods import login_redirect
from django.utils.text import slugify

# Create your views here.

def index(request):
    return render(request, 'stars/index.html', {'groups': Group.objects.all()})


def register(request):
    form = Register_form()
    if request.method == 'POST':
        form = Register_form(request.POST)
        if form.is_valid(): # Proverava da li je validna forma koristeci validatore i proverava da li moze elemente forme da upise u bazu
            user = form.save(commit=False)
            user.set_password(request.POST['password'])
            user.save()
            login(request, user)
            return HttpResponseRedirect(reverse('stars:index'))
    return render(request, 'stars/register.html', {'form': form})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('stars:index'))


def user_login(request):
    form = Login_form()
    if request.method == 'POST':
        form = Login_form(request.POST)
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user:
            if user.is_active:
                login(request, user)
                # return HttpResponseRedirect(reverse('stars:index'))
                return HttpResponseRedirect(login_redirect(request.get_raw_uri()))
            else:
                return HttpResponse('User is not active!')
        else:
            return render(request, 'stars/login.html', {'form': form, 'error': 'Invalid username or password'})
    return render(request, 'stars/login.html', {'form': form})


@login_required
def new_group(request):
    form = Group_form()
    if request.method == 'POST':
        form = Group_form(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.slug = slugify(form.title)
            try:
                form.save()
            except IntegrityError:
                form = Group_form(request.POST)
                return render(request, 'stars/new_group.html', {'form': form, 'error': 'Group with this Title already exists.'})
            else:
                return HttpResponseRedirect(reverse('stars:group_details', args=(form.slug,)))
    return render(request, 'stars/new_group.html', {'form': form})


@login_required
def group_details(request, slug):
    grp = Group.objects.get(slug=slug)
    try:
        grp.user_groups_set.get(user=request.user)
    except ObjectDoesNotExist:
        member = False
    else:
        member = True

    form = Post_form_within_group()
    if request.method == 'POST':
        if 'delete' in request.POST:
            grp.delete()
            return HttpResponseRedirect(reverse('stars:index'))
        elif 'join' in request.POST:
            User_Groups.objects.create(user=request.user, group=grp)
            member = True
        elif 'leave' in request.POST:
            User_Groups.objects.get(user=request.user, group=grp).delete()
            member = False
        elif 'add' in request.POST:
            form = Post_form_within_group(request.POST)
            form = form.save(commit=False)
            form.user = request.user
            form.group = grp
            form.save()
            form = Post_form_within_group()
    return render(request, 'stars/group_details.html', {'group': grp, 'member': member, 'form': form})


@login_required
def post(request):
    form = Post_form()
    if request.method == 'POST':
        form = Post_form(request.POST)
        form = form.save(commit=False)
        form.user = request.user
        form.group = Group.objects.get(id=int(request.POST['choose_group']))
        form.save()
        return HttpResponseRedirect(reverse('stars:group_details', args=(form.group.slug,)))
    return render(request, 'stars/new_post.html', {'form': form})


@login_required
def my_groups(request):
    return render(request, 'stars/my_groups.html', {'groups': request.user.group_set.all()})


@login_required
def upload(request):
    form = Pictures_form()
    if request.method == 'POST':
        picture = request.FILES['picture'].name
        if picture.endswith('.tif') or picture.endswith('.jpg') or picture.endswith('.png'): # Provra da li je odgovarajuci format
            form = form.save(commit=False)
            form.user = request.user
            form.picture = request.FILES['picture']
            form.save()
            return HttpResponseRedirect(reverse('stars:space_uploads'))
        else:
            return render(request, 'stars/upload.html', {'form': form, 'error': 'Select an image file'})
    return render(request, 'stars/upload.html', {'form': form})


@login_required
def space_uploads(request):
    pictures = Pictures.objects.all()
    return render(request, 'stars/space_uploads.html', {'pictures': pictures})