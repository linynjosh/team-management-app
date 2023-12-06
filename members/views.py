from sqlite3 import IntegrityError
from django.http import Http404
from .models import Member
from .forms import AddMemberForm, EditMemberForm
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView, FormView
from django.views.generic import ListView

# Create your views here.

class MemberDeleteView(DeleteView):
    template_name = ''
    model = Member
    success_url = reverse_lazy('home')  

    def get_object(self, queryset=None):
        first_name = self.request.POST.get('first_name', None)
        last_name = self.request.POST.get('last_name', None)
        return Member.objects.get(first_name=first_name, last_name=last_name)

class MemberListView(ListView):
    template_name = 'main/list.html'
    model = Member
    context_object_name = 'members'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['size'] = len(context['members'])
        return context

class EditMemberView(FormView):
    template_name = '' 
    form_class = EditMemberForm
    success_url = reverse_lazy('home') 

    def form_valid(self, form):
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

        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

    def get_initial(self):
        first_name = self.kwargs.get('first_name')
        last_name = self.kwargs.get('last_name')
        return {'first_name': first_name, 'last_name': last_name}

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class AddMemberView(FormView):
    template_name = ''
    form_class = AddMemberForm
    success_url = reverse_lazy('home')  

    def form_valid(self, form):
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        phone = form.cleaned_data['phone_number']
        email = form.cleaned_data['email']
        is_admin = form.cleaned_data['is_admin']

        try:
            member = Member.objects.create(last_name=last_name, first_name=first_name, phone=phone, email=email, is_admin=is_admin)
        except IntegrityError:
            form.add_error(None, "Member already exists in the database.")
            return self.form_invalid(form)

        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)