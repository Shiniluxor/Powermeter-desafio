from django.db import models
from django.urls import reverse


class Medidores(models.Model):

    # Fields
    nombre = models.CharField(max_length=100, null=False, blank=False, unique=True)
    llave_id = models.CharField(max_length=50, null=False, blank=False, unique=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    Id = models.AutoField(primary_key=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("Medidores_detail", args=(self.Id,))

    def get_update_url(self):
        return reverse("Medidores_update", args=(self.Id,))



class Mediciones(models.Model):

    # Relationships
    medidor_id = models.ForeignKey("medidores.Medidores", on_delete=models.CASCADE)

    # Fields
    id = models.AutoField(primary_key=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    consumo_reg = models.CharField(max_length=100, null=False, blank=False,)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("Mediciones_detail", args=(self.id,))

    def get_update_url(self):
        return reverse("Mediciones_update", args=(self.id,))

