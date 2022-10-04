from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Ticket

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'
    #sub, msg, tkt_type, tkt_status, updated
    #def create(self, id, sub, msg, tkt_type, tkt_status, updated):
    #    ticket = Ticket.objects.create(id, sub, msg, tkt_type, tkt_status, updated)
        #Profile.objects.create(user=user, **profile_data)
    #    return ticket
"""
class TicketCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('id', 'subject', 'message', 'ticket_type', 'ticket_status', 'updated')

    def create(self, id, sub, msg, tkt_type, tkt_status, updated):
        ticket = Ticket.objects.create(id, sub, msg, tkt_type, tkt_status, updated)
        #Profile.objects.create(user=user, **profile_data)
        return ticket

class TicketCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id', 'subject', 'message', 'ticket_type', 'ticket_status', 'updated']

    def create(self, id, sub, msg, tkt_type, tkt_status, updated):
        ticket = Ticket.objects.create(id, sub, msg, tkt_type, tkt_status, updated)
        #Profile.objects.create(user=user, **profile_data)
        return ticket

class TicketListSerializer(serializers.ModelSerializer):
    #queryset = Ticket.objects.all()
    #serializer_class = TicketListSerializer
    class Meta:
        model = Ticket
        fields = '__all__'

class TicketDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id', 'subject', 'message', 'ticket_type', 'ticket_status', 'updated']

    def retrieve(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.subject = validated_data.get('subject', instance.subject)
        instance.message = validated_data.get('message', instance.message)
        instance.ticket_type = validated_data.get('ticket_type', instance.ticket_type)
        instance.ticket_status = validated_data.get('ticket_status', instance.ticket_status)
        instance.updated = validated_data.get('updated', instance.updated)
        return instance

class TicketUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id', 'subject', 'message', 'ticket_type', 'ticket_status', 'updated']

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.subject = validated_data.get('subject', instance.subject)
        instance.message = validated_data.get('message', instance.message)
        instance.ticket_type = validated_data.get('ticket_type', instance.ticket_type)
        instance.ticket_status = validated_data.get('ticket_status', instance.ticket_status)
        instance.updated = validated_data.get('updated', instance.updated)
        return instance

class TicketDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id', 'subject', 'message', 'ticket_type', 'ticket_status', 'updated']
"""
