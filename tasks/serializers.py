# from django.forms import BooleanField, CharField, DateField, DateTimeField, IntegerField
from rest_framework import serializers
from tasks.models import *

# Usando Metodo Automatico


class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'

# Usando Metodo Manual
# class TasksSerializer(serializers.ModelSerializer):
# # TasksSerializer():
#     id = IntegerField(label='ID', read_only=True)
#     title = CharField(allow_blank=True, allow_null=True, required=False, style={'base_template': 'textarea.html'})
#     description = CharField(allow_blank=True, allow_null=True, required=False, style={'base_template': 'textarea.html'})
#     nlevel = CharField(allow_blank=True, allow_null=True, max_length=1, required=False)
#     review = BooleanField(allow_null=True, required=False)
#     pricebook = CharField(allow_blank=True, allow_null=True, required=False, style={'base_template': 'textarea.html'})
#     datepublic = DateField(allow_null=True, required=False)
#     datesell = DateTimeField(allow_null=True, required=False)


"""

- Apuntes:

Se puede generar un modelo Serializador a travez de estos comandos:
    python manage.py shell
    from tasks.serializers import TasksSerializer
    serializer = TasksSerializer()
    print(repr(serializer))

- Bibliografia:

https://www.django-rest-framework.org/api-guide/serializers/#inspecting-a-modelserializer

"""
