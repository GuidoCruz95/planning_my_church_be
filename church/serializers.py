from rest_framework import serializers
from church.models import Person, Macro, Cell, Event


class MacroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Macro
        fields = ['macro_id', 'name', 'creation_date', 'closing_date']


class CellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cell
        fields = ['cell_id', 'name', 'description', 'macro']


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['ci', 'email', 'name', 'lastname', 'birthdate', 'cell']


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['name', 'start_date', 'end_date', 'location', 'cost', 'requirements']
