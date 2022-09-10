from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import Customer, User
from .customer_serializer import CustomerSerializer
from django.http import HttpResponse


class CustomerViewSet(viewsets.ModelViewSet):

    serializer_class = CustomerSerializer

    def get_queryset(self):
        customer = Customer.objects.all()
        return customer

    def create(self, request, *args, **kwargs):
        customer_data = request.data
        new_user = User.objects.create(
            first_name=customer_data["user"]["first_name"],
            last_name=customer_data["user"]["last_name"],
            email=customer_data["user"]["email"],
            phone_number=customer_data["user"]["phone_number"])

        new_user.save()

        new_customer = Customer.objects.create(profile_number=customer_data["profile_number"], user=new_user)
        new_customer.save()

        serializer = CustomerSerializer(new_customer)
        return Response(serializer.data)
        