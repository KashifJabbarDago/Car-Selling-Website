from dataclasses import fields
from django import forms 
from django.db import models
from django.forms import ModelForm
#from uploads.core.models import Document
'''
class DocumentForm(forms.ModelForm):
    pass 
    
         form = DocumentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    class Meta:
        # model = Document
        fields = ('description','document',)
        '''