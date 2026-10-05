"""
title       : User account view
description : User accounts views
created at  : 04 Oct, 2026
author      : Joel
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Div, HTML, Button, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from django.contrib.auth.models import User
from accounts.models import Profile

# User Registration ******************************************************************
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("username", "email", 'password1', 'password2', "first_name", "last_name")
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            Field('username', css_class='bg-body-secondary'),
            Field('email', css_class='bg-body-secondary'),
            Row(
                Column(
                    Field('first_name', css_class='bg-body-secondary'), 
                    css_class='form-group col-md-6'),
                Column(
                    Field('last_name', css_class='bg-body-secondary'), 
                    css_class='form-group col-md-6'),
                css_class='form-row'
            ),
            Field('password1', css_class='bg-body-secondary'),
            Field('password2', css_class='bg-body-secondary'),
            HTML("<hr/>"),
            FormActions(
                Div(
                    Submit('submit', 'Create User', css_class='btn btn-primary'),
                    HTML("<a href='/' class='btn btn-outline-dark'>Go Back</a>"),
                    css_class="d-flex justify-content-between"   
                )
            )
        )
        
        
# Profile Form ******************************************************************
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("role", "phone", "address", "city", "avatar")
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            Row(
                Column(
                    Field('role', css_class='bg-body-secondary'), 
                    css_class='form-group col-md-4'),
                Column(
                    Field('phone', css_class='bg-body-secondary'),
                    css_class='form-group col-md-4'),
                Column(
                    Field('city', css_class='bg-body-secondary'),
                    css_class='form-group col-md-4'),
                css_class='form-row'
            ),
            Field('avatar', css_class='bg-body-secondary'),
            Field('address', rows="3", css_class='bg-body-secondary'),
            Submit('submit', 'Save', css_class='btn btn-primary')
        )
        
        

