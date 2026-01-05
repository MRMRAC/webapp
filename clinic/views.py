from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Patient
from .serializers import RegisterSerializer, PatientSerializer
from django.db.models import Q
from rest_framework_simplejwt.views import TokenObtainPairView

class RegisterView(generics.CreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = RegisterSerializer

class SearchPatientsView(generics.ListAPIView):
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        return Patient.objects.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query)
        )