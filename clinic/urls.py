from django.urls import path
from .views import RegisterView, SearchPatientsView, PatientDetailView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import PatientMedicalCardsView
from .views import MedicalCardDocumentsView
from .views import MedicalDocumentDetailView

from .views import DocumentFormSchemaView
urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('patients/search/', SearchPatientsView.as_view()),
    path('patients/<int:pk>/', PatientDetailView.as_view()),
    path(
        'patients/<int:patient_id>/medical-cards/',
        PatientMedicalCardsView.as_view()
    ),
    path(
        'medical-cards/<int:card_id>/documents/',
        MedicalCardDocumentsView.as_view(),
        name='medical-card-documents'
    ),
    path(
      'documents/form-schema/<str:doc_type>/',
      DocumentFormSchemaView.as_view()
    ),
    path(
        'documents/<int:doc_id>/',
        MedicalDocumentDetailView.as_view()
    ),
    
]
