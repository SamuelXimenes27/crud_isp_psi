from django.forms import ModelForm, TextInput
from app.models import Animals, ServiceOrders


class AnimalsForm(ModelForm):
    class Meta:
        model = Animals
        fields = ['nome', 'birthDate', 'cpf', 'address', 'contact']


class ServiceOrdersForm(ModelForm):
    class Meta:
        model = ServiceOrders
        fields = ['cpf_client', 'visit_date', 'visit_hour',
                  'visit_reason', 'technician_name']
