from django import forms
from django.core.exceptions import ValidationError
from .models import Visitor


class Sign_in_Form(forms.ModelForm):
    # Visitor roles
    role_choices = (('staff', 'BSrE Staff'),
                    ('other_staff', 'BSSN staff'),
                    ('contractor', 'Contractor'),
                    ('other', 'Other'))
    role_dropdown = forms.CharField(label='Select Role', initial=('staff', 'BSrE Staff'), widget=forms.Select(choices=role_choices, attrs={'class': 'form-control'}))
    # Visitor reason
    reason_choices = (('audit', 'Audit'),
                    ('dismantle', 'Dismantle'),
                    ('installation', 'Installation'),
                    ('maintenance', 'Maintenance'),
                    ('replace', 'Replace'),
                    ('troubleshoot', 'Troubleshoot'),
                    ('visit', 'Visit'),
                    ('other', 'Other Reason'))
    reason_dropdown = forms.CharField(label='Select Reason', initial=('audit', 'Audit'), widget=forms.Select(choices=reason_choices, attrs={'class': 'form-control'}))
    # Custom cleaning function that is called during 'sign_in_form.is_valid()' in views.py
    def clean(self):
        cleaned_data = super(Sign_in_Form, self).clean()
        this_email = cleaned_data.get('email')
        this_visitor = Visitor.objects.filter(email=this_email).first()
        if this_visitor:
            checked_out = this_visitor.checkout
            if not checked_out:
                raise ValidationError("You are already checked in. Please check out to continue.")

        return cleaned_data

    class Meta:
        model = Visitor

        fields = [
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'role',
            'reason',
        ]

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.TextInput(attrs={'class': 'form-control'}),
            'reason': forms.TextInput(attrs={'class': 'form-control'})
        }

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'phone_number': 'Phone Number',
            'role': '',
            'reason': '',
        }

    def __init__(self, exclude, *args, **kwargs):
        super(Sign_in_Form, self).__init__(*args, **kwargs)
        self.order_fields(['first_name',
                       'last_name',
                       'email',
                       'phone_number',
                       'role_dropdown',
                       'role',
                       'reason_dropdown',
                       'reason'])

class Sign_out_Form(forms.Form):
    email = forms.EmailField(label='Email')
    email.widget.attrs.update({'class': 'form-control'})

    # custom cleaning function that is called during 'sign_out_form.is_valid()' in views.py
    def clean(self):
        cleaned_data = super(Sign_out_Form, self).clean()
        this_email = cleaned_data.get('email')

        visitor = Visitor.objects.filter(email=this_email).first()
        if not visitor:
            raise ValidationError("Please enter the correct credentials.")
        else:
            checked_out = visitor.checkout
            if checked_out:
                raise ValidationError("You are already checked out.")

        return cleaned_data
