from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Patient
from .serializers import RegisterSerializer, PatientSerializer
from django.db.models import Q
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from .models import Patient
from .serializers import PatientSerializer

class RegisterView(generics.CreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = RegisterSerializer

# class SearchPatientsView(generics.ListAPIView):
#     serializer_class = PatientSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def get_queryset(self):
#         query = self.request.query_params.get('q', '')
#         return Patient.objects.filter(
#             Q(first_name__icontains=query) | Q(last_name__icontains=query)
#         )

from rest_framework.generics import RetrieveAPIView

class PatientDetailView(RetrieveAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]

class SearchPatientsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        query = request.GET.get('q', '').strip()

        qs = Patient.objects.all()

        if query:
            qs = qs.filter(
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query) |
                Q(username__icontains=query) |
                Q(email__icontains=query)
            )

        qs = qs.order_by('last_name', 'first_name')

        return Response(PatientSerializer(qs, many=True).data)


from rest_framework.generics import ListCreateAPIView
from .models import MedicalCard
from .serializers import MedicalCardSerializer

class PatientMedicalCardsView(ListCreateAPIView):
    serializer_class = MedicalCardSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return MedicalCard.objects.filter(
            patient_id=self.kwargs['patient_id']
        )

    def perform_create(self, serializer):
        serializer.save(patient_id=self.kwargs['patient_id'])

from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import MedicalCard, MedicalDocument
from .serializers import MedicalDocumentSerializer


class MedicalCardDocumentsView(ListCreateAPIView):
    serializer_class = MedicalDocumentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return MedicalDocument.objects.filter(
            medical_card_id=self.kwargs['card_id']
        )

    def perform_create(self, serializer):
        medical_card = MedicalCard.objects.get(
            id=self.kwargs['card_id']
        )
        serializer.save(medical_card=medical_card)


from rest_framework.views import APIView
from rest_framework.response import Response
from .document_forms import FORMS_MAP


class DocumentFormSchemaView(APIView):
    def get(self, request, doc_type):
        return Response(FORMS_MAP.get(doc_type, []))
    

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import MedicalCard, MedicalDocument, MedicalDocumentFieldValue
from .document_forms import FORMS_MAP

class MedicalDocumentDetailView(APIView):

    # ПРОСМОТР ДОКУМЕНТА
    def get(self, request, doc_id):
        doc = get_object_or_404(MedicalDocument, id=doc_id)

        fields = MedicalDocumentFieldValue.objects.filter(document=doc)

        return Response({
            'id': doc.id,
            'type': doc.document_type,
            'title': doc.title,
            'created_at': doc.created_at,
            'fields': [
                {
                    'code': f.field_code,
                    'label': f.field_name,
                    'value': f.value
                }
                for f in fields
            ]
        })

    # РЕДАКТИРОВАНИЕ ДОКУМЕНТА
    def put(self, request, doc_id):
        doc = get_object_or_404(MedicalDocument, id=doc_id)

        for code, value in request.data.get('fields', {}).items():
            MedicalDocumentFieldValue.objects.update_or_create(
                document=doc,
                field_code=code,
                defaults={'value': value}
            )

        return Response({'status': 'updated'})

class MedicalCardDocumentsView(APIView):

    def get(self, request, card_id):
        card = get_object_or_404(MedicalCard, id=card_id)

        documents = MedicalDocument.objects.filter(
            medical_card=card
        ).order_by('-created_at')

        result = []
        for doc in documents:
            if doc.document_type == 'PRIMARY_VISIT':
              type_display = 'Первичный приём'
            elif doc.document_type == 'HEAD_DOCTOR_REVIEW':
              type_display = 'Осмотр с заведующим'
            elif doc.document_type == 'PREOPERATIVE_EPICRISIS':
              type_display = 'Предоперационный эпикриз'
            elif doc.document_type == 'OPERATION':
              type_display = 'Протокол операции'
            elif doc.document_type == 'DISCHARGE_EPICRISIS':
              type_display = 'Выписной эпикриз'
            elif doc.document_type == 'UNKNOWN':
              type_display = 'Неизвестный'
            else:
              type_display = doc.document_type

            result.append({
                'id': doc.id,
                'guid': str(doc.guid),
                'type': doc.document_type,
                'title': type_display,
                'created_at': doc.created_at
            })

        return Response(result)



    def post(self, request, card_id):
        data = request.data

        card = get_object_or_404(MedicalCard, id=card_id)

        doc = MedicalDocument.objects.create(
            medical_card=card,
            document_type=data['document_type'],
            title=data['document_type']
        )

        schema = FORMS_MAP.get(data['document_type'], [])

        schema_map = {f['code']: f['label'] for f in schema}

        for code, value in data.get('fields', {}).items():
            MedicalDocumentFieldValue.objects.create(
                document=doc,
                field_code=code,
                field_name=schema_map.get(code, code),
                value=value
            )

        return Response(
            {'id': doc.id, 'guid': str(doc.guid)},
            status=status.HTTP_201_CREATED
        )


