from django import forms
from django.forms import ModelForm
from .models import Ticket
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

class TextareaWidget(forms.Textarea):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('attrs', {}).update({'rows': 20, 'cols': 100})
        super(TextareaWidget, self).__init__(*args, **kwargs)

class Textarea(forms.Field):
    widget = TextareaWidget()

"""
class TicketForm(forms.Form):
    class Meta:
        model = Ticket
        fields = '__all__'
        #fields = ['id', 'subject', 'message', 'ticket_type', 'ticket_status', 'updated']

    def save(requestobj, self):
        # By James Chen
        # Extend form class to have the save attribute
        # check paramters
        #data = self.cleaned_data
        #scope

        #if user.is_authenticated:

        data = request.POST
        id = data['id']
        subject = data['subject']
        message = data['message']
        type = data['ticket_type']
        status = data['ticket_status']
        update = data['updated']

        #name_map = {"id": request.POST['id'],"subject": request.POST['subject'],"message": request.POST['message'],"ticket_status": request.POST['ticket_status'],"ticket_type": request.POST['ticket_type'],"updated": request.POST['updated']}
        name_map = {"id": requestobj['id'],"subject": requestobj['subject'],"message": requestobj['message'],"ticket_status": requestobj['ticket_status'],"ticket_type": requestobj['ticket_type'],"updated": requestobj['updated']}
        Ticket.objects.raw("insert into tickets_ticket ('id', 'subject', 'message', 'ticket_status', 'ticket_type', 'updated') values (requestobj['id'], requestobj['subject'], requestobj['message'], requestobj['ticket_status'], requestobj['ticket_type'], requestobj['updated'])", translations=name_map)
        #ticket = Ticket({'id':requestobj['id'], 'subject':requestobj['subject'],'message':requestobj['message'],'ticket_type':requestobj['ticket_type'],'ticket_status':requestobj['ticket_status'],'updated':requestobj['updated']})



        #return redirect("tickets:listsss")
        # open connection
        # execute


"""

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'
        #fields = ['id', 'subject', 'message', 'ticket_type', 'ticket_status', 'updated']

    id = forms.IntegerField(label="Bug id")
	
    subject = forms.CharField(label="Subject")
    #message = forms.CharField(label="Message", widget=forms.Textarea)
    message = Textarea()

    DEFECT = 'D'
    FEATURE = 'F'
    PATCH = 'P'

    #TICKET_TYPE = (
    #    (DEFECT, 'Defect'),
    #    (FEATURE, 'Feature'),
    #    (PATCH, 'Patch'),
    #)

    ticket_type = forms.ChoiceField(choices=[(DEFECT, 'Defect'), (FEATURE, 'Feature'), (PATCH, 'Patch'),])

    NEW = 'N'
    READ = 'RD'
    WAITING = 'W'
    REOPENED = 'RO'
    RESOLVED = 'R'


    #TICKET_STATUS = (
    #    (NEW, 'New'),
    #    (READ, 'Read'),
    #    (WAITING, 'Waiting'),
    #    (REOPENED, 'Reopened'),
    #    (RESOLVED, 'Resolved'),
    #)

    #ticket_type = forms.ModelChoiceField(queryset=TICKET_TYPE, empty_label="Select Ticket Type")
    ticket_status = forms.ChoiceField(choices=[(NEW, 'New'),(READ, 'Read'),(WAITING, 'Waiting'),(REOPENED, 'Reopened'),(RESOLVED, 'Resolved')])
    #updated = forms.DateField(input_formats=['%Y-%m-%d %H:%M:%S'])
    #updated = forms.DateField(input_formats=['%Y-%m-%d %H:%M:%S'])
    updated = forms.DateField(input_formats=['%Y-%m-%d'])
    owner = forms.CharField(label='Owner', max_length=18)
    # attachment = forms.ImageField()
	
class UserForm(forms.Form):
    class Meta:
        model = User
        fields = '__all__'
