from .models import Register, Version, Field, FieldChoice, Project
from rest_framework import serializers

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('name', 'description', 'address_size', 'word_size')


class FieldChoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FieldChoice
        fields = ('id','name', 'desc', 'value', 'field_id')


class FieldSerializer(serializers.HyperlinkedModelSerializer):
    choices = FieldChoiceSerializer(many=True, read_only=True)
    class Meta:
        model = Field
        fields = ('id','name','range_upper','range_lower', 'type','unit_scale','unit_type','choices', 'value_min', 'value_max', 'description', 'register_id')


class RegisterSerializer(serializers.ModelSerializer):
    fields = FieldSerializer(many=True, read_only=True)
    address_to_hex = serializers.CharField()
    class Meta:
        model = Register
        fields = ('id','name', 'address', 'size', 'description', 'fields', "address_to_hex", "access", "default", "version")
        depth = 2


class VersionSerializer(serializers.ModelSerializer):
    registers = RegisterSerializer(many=True)
    class Meta:
        model = Version
        fields = ('id', 'name', 'registers')

