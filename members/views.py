from sqlite3 import IntegrityError
from django.shortcuts import redirect, render
from django.http import Http404, HttpResponseNotAllowed
from django.views.decorators.http import require_http_methods
from .models import Member
from .forms import AddMemberForm, DeleteMemberForm, EditMemberForm

# Create your views here.

@require_http_methods(["GET"])
def home(response):
    members = Member.objects.all()
    size = len(members)
    return render(response, "main/list.html", {"members": members, "size": size})

@require_http_methods(["POST"])
def delete_member(request):
    if request.method == 'POST':
        form = DeleteMemberForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']

            try:
                member = Member.objects.get(first_name=first_name, last_name=last_name)
                member.delete()
            except Member.DoesNotExist:
                raise Http404("Member does not exist.")
            
        return redirect('home')
    else:
        return HttpResponseNotAllowed(['POST'])

@require_http_methods(["POST"])
def edit_member(request):
    if request.method == "POST":
        form = EditMemberForm(request.POST)  
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            is_admin = form.cleaned_data['is_admin']

            try:
                member = Member.objects.get(first_name=first_name, last_name=last_name)
                member.phone = phone
                member.email = email
                member.is_admin = is_admin
                member.save()
            except Member.DoesNotExist:
                raise Http404("Member does not exist.")
            
        return redirect('home')
    else:
        return HttpResponseNotAllowed(['POST'])

@require_http_methods(["POST"])
def add_member(request):
    if request.method == "POST":
        form = AddMemberForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            is_admin = form.cleaned_data['is_admin']

            try:
                member = Member(last_name=last_name, first_name=first_name, phone=phone, email=email, is_admin=is_admin)
                member.save()
            except IntegrityError:
                form.add_error(None, "Member already exists in the database.")
                
        return redirect('home')           
    else:
        return HttpResponseNotAllowed(['POST'])

