from rest_framework import serializers
from .models import Patient
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = Patient
        fields = ('username', 'email', 'first_name', 'last_name', 'password', 'password_confirm')

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError("Пароли не совпадают")
        return attrs

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        user = Patient.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
from .models import MedicalCard


class MedicalCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalCard
        fields = '__all__'
        read_only_fields = ('patient',)
# class PatientSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Patient
#         fields = ('id', 'username', 'email', 'first_name', 'last_name')
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'date_joined',
        ]
from .models import MedicalDocument
class MedicalDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalDocument
        fields = [
            'id',
            'title',
            'guid',
            'created_at',
            'card_prefix',
            'card_number',
            'medical_card',
        ]
        read_only_fields = (
            'guid',
            'created_at',
            'card_prefix',
            'card_number',
            'medical_card',
        )