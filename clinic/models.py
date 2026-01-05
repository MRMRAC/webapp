from django.contrib.auth.models import AbstractUser

class Patient(AbstractUser):
    class Meta:
        verbose_name = "Пациент"
        verbose_name_plural = "Пациенты"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"