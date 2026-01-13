from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models

class Patient(AbstractUser):
    class Meta:
        verbose_name = "Пациент"
        verbose_name_plural = "Пациенты"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

import uuid
class MedicalCard(models.Model):
    patient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='medical_cards'
    )

    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    card_type = models.CharField(max_length=100)
    prefix = models.CharField(max_length=10)
    number = models.CharField(max_length=50)

    note = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.prefix}-{self.number}'

class DocumentType(models.TextChoices):
    PRIMARY_VISIT = 'PRIMARY_VISIT', 'Первичный приём'
    HEAD_DOCTOR_REVIEW = 'HEAD_DOCTOR_REVIEW', 'Осмотр с заведующим'
    PREOPERATIVE_EPICRISIS = 'PREOPERATIVE_EPICRISIS', 'Предоперационный эпикриз'
    OPERATION = 'OPERATION', 'Протокол операции'
    DISCHARGE_EPICRISIS = 'DISCHARGE_EPICRISIS', 'Выписной эпикриз'
    UNKNWOWN = 'UNKNWOWN', 'ПУТСЫШКК'
    
class MedicalDocument(models.Model):
    medical_card = models.ForeignKey(
        'MedicalCard',
        on_delete=models.CASCADE,
        related_name='documents'
    )

    document_type = models.CharField(
        max_length=50,
        choices=DocumentType.choices,
        default=DocumentType.UNKNWOWN 
    )

    title = models.CharField(max_length=255)
    guid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)

    created_at = models.DateTimeField(auto_now_add=True)

    STATUS_CHOICES = (
        ('DRAFT', 'Черновик'),
        ('SIGNED', 'Подписан'),
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='DRAFT'
    )

    def __str__(self):
        return f'{self.title} ({self.get_document_type_display()})'
    





class MedicalDocumentFieldValue(models.Model):
    document = models.ForeignKey(
        MedicalDocument,
        on_delete=models.CASCADE,
        related_name='fields'
    )

    field_code = models.CharField(
        max_length=100,
        verbose_name='Код поля'
    )

    field_name = models.CharField(
        max_length=255,
        verbose_name='Наименование поля'
    )

    value = models.TextField(
        verbose_name='Значение'
    )

    guid = models.UUIDField(
        default=uuid.uuid4,
        editable=False
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('document', 'field_code')