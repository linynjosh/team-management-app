from django import forms
from .models import Member
from .constants import MAX_FIRST_NAME_LENGTH, MAX_LAST_NAME_LENGTH, PHONE_LENGTH


class BaseMemberForm(forms.Form):
    first_name = forms.CharField(max_length=MAX_FIRST_NAME_LENGTH)
    last_name = forms.CharField(max_length=MAX_LAST_NAME_LENGTH)

    def clean(self):
        cleaned_data = super().clean()

        return cleaned_data

class DeleteMemberForm(BaseMemberForm):
    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if not Member.objects.filter(first_name=first_name, last_name=last_name).exists():
            raise forms.ValidationError("Member does not exist.")

        return cleaned_data

class EditMemberForm(BaseMemberForm):
    phone_number = forms.CharField(max_length=PHONE_LENGTH)
    email = forms.EmailField()
    is_admin = forms.BooleanField(required=False)

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if not Member.objects.filter(first_name=first_name, last_name=last_name).exists():
            raise forms.ValidationError("Member does not exist.")

        return cleaned_data

class AddMemberForm(BaseMemberForm):
    phone_number = forms.CharField(max_length=PHONE_LENGTH)
    email = forms.EmailField()
    is_admin = forms.BooleanField(required=False)

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if Member.objects.filter(first_name=first_name, last_name=last_name).exists():
            raise forms.ValidationError("Member already exists in the database.")

        return cleaned_data