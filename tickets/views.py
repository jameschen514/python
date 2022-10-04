from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.contrib.auth.models import User, Group
from django.contrib import auth
"""
from rest_framework.generics import (
    CreateAPIView, RetrieveAPIView,
    UpdateAPIView, DestroyAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView, ListCreateAPIView
)
"""
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from .models import Ticket
from .forms import TicketForm, Textarea, TextareaWidget, UserForm
#from .serializers import TicketSerializer
from .serializers import TicketSerializer#, TicketCreateSerializer, TicketListSerializer, TicketDetailSerializer, TicketUpdateSerializer, TicketDeleteSerializer
from datetime import datetime
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.http import HttpResponse, HttpResponseRedirect, QueryDict
from django.views.decorators.csrf import csrf_exempt

from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
from http.client import HTTPConnection


#class TicketViewSet(viewsets.ReadOnlyModelViewSet):

"""
class TicketViewSet(viewsets.ModelViewSet):
    # API endpoint that allows users to be viewed or edited.
    queryset = Ticket.objects.all().order_by('-id')
    serializer_class = TicketSerializer

class UserViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
"""
class TicketViewSet(viewsets.GenericViewSet):

    def list(self, request):
        queryset = Ticket.objects.all().order_by('-id')
        serializer_class = TicketSerializer(queryset, many=True)
        return Response(serializer_class.data)

    def create(self, request):
        queryset = Ticket.objects.all()
        ticket = request.get('ticket', None)
        serializer_class = TicketSerializer(ticket)
        new_ticket = Ticket.objects.create(ticket=ticket, **request)
        new_ticket.save()
        return Response(serializer_class.data)

    def retrieve(self, request, pk=None):
        queryset = Ticket.objects.all()
        ticket = get_object_or_404(queryset, pk=pk)
        serializer_class = TicketSerializer(ticket)
        return Response(serializer_class.data)

    def update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        # def destroy(self, request, *args, **kwargs):
        #
        queryset = Ticket.objects.all()
        instance = self.get_object_or_404()
        instance.delete()  # perform_destroy(instance)
        # except Http404:
        #    pass
        return Response(status=status.HTTP_204_NO_CONTENT)

class TicketListView(ListCreateAPIView):
    queryset = Ticket.objects.all().order_by('-id')
    serializer_class = TicketSerializer

class TicketDetailView(RetrieveAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    lookup_field = 'id'

class TicketUpdateView(RetrieveUpdateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    lookup_field = 'id'

class TicketDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    lookup_field = 'id'

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

def list_tickets(request):
    if request.method == 'GET':
        tickets = Ticket.objects.all().order_by('-id')
        ticket_serializer = TicketSerializer(tickets, many=True)

        # if request.user.is_authenticated:
        form = TicketForm({'id': Ticket.objects.count() + 1})

        #return Response({'serializer': ticket_serializer })
        #return JSONResponse(ticket_serializer.data)
        #ticket_form = TicketForm(request.POST)
        return render(request, "tickets/list_tickets.html", { "tickets":ticket_serializer.data, 'form':form })

    elif request.method == 'POST':
        if request.user.is_authenticated:

            # form = TicketForm(request.POST)
            # tickets = Ticket.objects.all().order_by('-id')
            # ticket = get_object_or_404(Ticket, pk=request.POST['id'])
            # ticket_serializer = TicketSerializer(ticket, many=False)

            # form = TicketForm(initial=ticket_serializer.data)
            """
            form = TicketForm(initial={'id':2,
                'subject':'subject goes here',
                'message':'message goes here',
                'ticket_status':'N',
                'ticket_type': 'D',
                'updated':'2019-08-15 13:25:00',
                'owner':'system'})
            """

            # data = {'id':15, 'subject':'subject goes here', 'message':'message goes here','ticket_status':'N','ticket_type': 'D','updated':'2019-08-15 13:25:00','owner':'system'}
            # data = {'id':request.POST['id'], 'subject':request.POST['subject'], 'message':request.POST['message'],'ticket_status':request.POST['ticket_status'],'ticket_type':request.POST['ticket_type'],'updated':request.POST['updated'],'owner':request.POST['owner'] }
            data = QueryDict.dict(request.POST)
            form = TicketForm()

            if not form.is_valid():
                #cd = form.cleaned_data

                form = TicketForm(data)
                #data = form.cleaned_data
                bound = form.is_bound
                valid = form.is_valid()
                form.save()
                tickets = Ticket.objects.all().order_by("-id")
                size = Ticket.objects.count() + 1
                blank = TicketForm({'id': Ticket.objects.count() + 1})
                return render(request, "tickets/list_tickets.html", {"tickets": tickets, "size": size, "form":blank })    
            else:
                #return HttpResponse(request.POST + "hello" form['id'] + " " + form['subject'] + " " + form['message'] + " " + form['ticket_status'] + " " + form['ticket_type'] + " " + form['updated'] + " " + form['owner'])
                #return HttpResponse(form['id'])
                tickets = Ticket.objects.all()
                size = Ticket.objects.count() + 1
                return render(request, "tickets/list_tickets.html", {'form': form, "size":size })

            

            """
            ticket_data = JSONParser().parse(request)
            ticket_serializer = TicketSerializer(data=ticket_data)
            if ticket_serializer.is_valid():
                ticket_serializer.save()
                #return JSONResponse(ticket_serializer.data, status=status.HTTP_201_CREATED )
                return render(request, "tickets/list_tickets.html", { "tickets": ticket_serializer.data })
            return JSONResponse(ticket_serializer.errors, status=status.HTTP_400_BAD_REQUEST )
            """
        else:
            return redirect("tickets:loginsss")
    else:
        form = TicketForm()
        return render(request, "tickets/list_tickets.html", { 'form':form })

def ticket_detail(request, pk):
    # http_method_names = ["GET", "PUT", "DELETE"]

    try:
        ticket = Ticket.objects.get(pk=pk)
    except Ticket.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        ticket_serializer = TicketSerializer(ticket)
        form = TicketForm(initial=ticket_serializer.data)

        # return JSONResponse(ticket_serializer.data)
        return render(request, "tickets/ticket_detail.html", {'ticket': ticket_serializer.data, 'current_user':request.user, 'form':form })
        # return HttpResponse("GET Method")
    elif request.method == 'POST':

        data = QueryDict.dict(request.POST)
        if request.user.is_authenticated:

            # check if forms has values stored previously
            t = Ticket.objects.get(id=data['id'])
            # form = TicketForm(auto_id=True)

            Ticket.objects.filter(id=data['id']).update(subject=data['subject'], message=data['message'], ticket_type=data['ticket_type'], ticket_status=data['ticket_status'], updated=data['updated'], owner=data['owner'])
            # the **kwargs, states that it accepts dictionary as parameter
            # Ticket.objects.update_or_create(id=data['id'], subject=data['subject'], message=data['message'], ticket_type=data['ticket_type'], ticket_status=data['ticket_status'], updated=data['updated'], owner=data['owner'])


            #Ticket.objects.update(id=data['id'], subject=data['subject'], message=data['message'], ticket_type=data['ticket_type'], ticket_status=data['ticket_status'], updated=data['updated'], owner=data['owner'])
            #t.save()


            """
            if not form.is_valid():
                #cd = form.cleaned_data
                form = TicketForm(data)
                #data = form.cleaned_data
                bound = form.is_bound
                valid = form.is_valid()
                form.save()
                return redirect("tickets:updatess")
                #ticket = Ticket.objects.get(pk=pk)
                #return HttpResponse("Form is saved block")
                #return redirect("/tickets/api/list/", { "ticket": ticket, "current_user":request.user, "form":form })
                #return redirect("tickets:listsss")
                #return render(request, "tickets/ticket_detail.html", { "ticket": ticket, "current_user":request.user, "form":form })
            else:
                #return HttpResponse(request.POST + "hello" form['id'] + " " + form['subject'] + " " + form['message'] + " " + form['ticket_status'] + " " + form['ticket_type'] + " " + form['updated'] + " " + form['owner'])
                return HttpResponse("Is valid end")
            """
            return redirect("tickets:listsss")
            # render(request, "tickets/ticket_detail.html", { "ticket":ticket })
        else:
            return HttpResponse("Detail post not logged in")

    elif request.method == 'PUT':
        if request.user.is_authenticated:
            ticket_data = JSONParser().parse(request)
            # legacy ticket_serializer = TicketSerializer(ticket_data, data=ticket_data)
            ticket_serializer = TicketSerializer(ticket_data)
            if ticket_serializer.is_valid():
                ticket_serializer.save()
                return HttpResponse("Serializer complete")
                #return JSONResponse(ticket_serializer.data)
            #return JSONResponse(ticket_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return HttpResponse("PUT block")
        else:
            return HttpResponse("PUT check user block")
    elif request.method == 'DELETE':
        if request.user.is_authenticated:
            ticket.delete()
            return HttpResponse("Delete block")
            # return HttpResponse(status=status.HTTP_204_NO_CONTENT)
        else:
            return HttpResponse("DELETE check user")

def delete_ticket(request, pk):
	tkt = get_object_or_404(Ticket, id = pk)
	
	if request.method == "POST":
		tkt.delete()
		return HttpResponseRedirect("/tickets/api/list/")
	return render(request, "tickets/delete_ticket.html", {})
	
def new_ticket(request):
    #if user is not None and user.is_active
    if request.user.is_authenticated:


        if request.method == "GET":
            form = TicketForm({"id": Ticket.objects.all().order_by("-id")[0].id + 1})
			#form.id = Ticket.objects.all().order_by("-id")[0].id + 1
			
			
			
			#if form.is_valid():
            #    form.user = request.user
            #    form.save()
            #    tickets = Ticket.objects.all().order_by("-id")
	
        elif request.method == "POST":
            #form = TicketForm({'id':3, 'subject': '1st subject', 'message':'2nd message', 'ticket_type':'D', 'ticket_status':'N', 'updated':'2019-08-13 00:00:00'})
            form = TicketForm(request.POST)

            if form.is_valid():
                form.user = request.user
                form.save()
                tickets = Ticket.objects.all().order_by("-id")

            return redirect("tickets:listsss")
            #return render(request, "tickets/list_tickets.html", { "tickets": tickets, "form":form })
            #return render(request, "tickets/new_ticket.html", {"form":form,"tickets": tickets })
            #return HttpResponse("not saved")
        else:
            return HttpResponse("is not get or post")

        #return render(request, 'tickets/login.html', { "form": form })
        #return redirect("")


        """
        if request.method == 'POST':
            ticket_data = JSONParser().parse(request)
            ticket_serializer = TicketSerializer(ticket_data)

            if ticket_serializer.is_valid():
                ticket_serializer.save()
                #return JSONResponse(ticket_serializer.data, status=status.HTTP_201_CREATED )
                return render(request, "tickets/new_ticket.html", { "tickets": ticket_serializer.data, "ticket_data":ticket_data })

            #return JSONResponse(ticket_serializer.errors, status=status.HTTP_400_BAD_REQUEST )
        elif request.method == 'GET':
            form = TicketForm()
        else:
            form = TicketForm()
        """

        return render(request, "tickets/new_ticket.html", { "form": form })
    else:
        return HttpResponseRedirect('/tickets/api/action/login/')

def account_login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        #auth.login(request, user)

        if user is not None and user.is_active: # and user.is_superuser
            auth.login(request, user)
            return redirect("tickets:listsss")
        else:
            #return HttpResponseRedirect("/accounts/invalid/")
            return redirect("tickets:loginsss")
    elif request.method == "GET":
        userform = UserForm()
        return render(request, "tickets/login.html", { "user_form": userform })
    else:
        return HttpResponse("It's not GET or POST")

    return render(request, "tickets/login.html")
    #return render(request, "tickets/login.html", { "user":user, "username":username, "form":form })

def account_logout(request):
    auth.logout(request)
    #return render(request, "tickets/logout.html", {})
    return redirect("tickets:loginss")

class TicketList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'tickets/ticket_list.html'

    def get(self, request):
        tickets = Ticket.objects.all().order_by("-id")
        serializer = TicketSerializer(tickets, many=True)
        return render(request, "tickets/list_tickets.html", { "tickets": serializer.data})

    def post(self):
        pass

class TicketDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'tickets/ticket_detail.html'

    def get(self, request, pk):
        ticket = get_object_or_404(Ticket, pk=pk)
        serializer = TicketSerializer(ticket)
        return render(request, template_name, {'serializer':serializer.data, 'ticket':ticket })

    def post(self, request, pk):
        ticket = get_object_or_404(Ticket, pk=pk)
        serializer = TicketSerializer(Ticket, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer':serilizer, 'ticket':ticket })
        serializer.save()
        return redirect('ticket/api/listss')
"""
class TicketCreateAPIView(CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketCreateSerializer

class TicketListAPIView(ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketListSerializer

    def get_extra_actions(self):
        pass
        return null
    #queryset = get_queryset(
    #permission_classes = [IsAdminUser]


class TicketDetailAPIView(RetrieveAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketDetailSerializer
    lookup_field = 'id'

class TicketUpdateAPIView(UpdateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketDetailSerializer

class TicketDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketDetailSerializer

    def delete(self, request, id):
        ticket = get_object_or_404(Ticket, pk=kwargs['id'])
        ticket.delete()
        return Response("Question deleted", status=status.HTTP_204_NO_CONTENT)
"""
