from datetime import datetime


from django.db import models, IntegrityError


# Create your models here.



class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    client_first_name = models.CharField('Prénom', max_length=80)
    client_last_name = models.CharField('Nom', max_length=80)
    client_birthdate = models.DateField('Date de naissance', null=True, blank=True)#, help_text="Format : jj.mm.aaaa (Exemple : 24.02.1980)")
    client_address = models.CharField('Adressse', null=True, blank=True, max_length=80)
    client_additional_address = models.CharField('Complément d\'adresse', null=True, blank=True, max_length=80)
    client_zip_code = models.PositiveSmallIntegerField('NPA', null=True, blank=True)
    client_city = models.CharField('Localité', null=True, blank=True, max_length=80)
    client_phone_number_1 = models.CharField('Téléphone 1', max_length=30, blank=True, help_text="Format : +xx xx xxx xx xx (Exemple : +41 79 123 45 67)")
    client_phone_number_2 = models.CharField('Téléphone 2', max_length=30, blank=True, help_text="Format : +xx xx xxx xx xx (Exemple : +41 79 123 45 67)")
    client_email_address = models.EmailField('E-mail', null=True, blank=True)
    client_comment = models.TextField('Commentaire', null=True, blank=True)

    def __str__(self):
        return self.client_last_name + " " + self.client_first_name  #+ " (" + str(self.client_birthdate.strftime("%d.%m.%Y")) + ")"

    def save(self, *args, **kwargs):
        print("Save 'Client'")
        super(Client, self).save(*args, **kwargs)


    # class Meta:
    #     ordering = ["client_last_name", "client_first_name"]


class Massage(models.Model):
    massage_id = models.AutoField(primary_key=True)
    massage_name = models.CharField('Nom du massage', max_length=80)
    # massage_description = models.TextField('Description')
    massage_duration = models.PositiveSmallIntegerField('Durée (minutes)')
    massage_price = models.FloatField('Prix par heure')

    def __str__(self):
        return self.massage_name + " - " + str(self.massage_duration) + " min."


class Service(models.Model):
    service_id = models.AutoField(primary_key=True)
    service_client_id = models.ForeignKey(Client, null=True, on_delete=models.DO_NOTHING, verbose_name="Client")
    service_massage_id = models.ForeignKey(Massage, null=True, on_delete=models.DO_NOTHING, verbose_name="Massage")
    service_date = models.DateTimeField('Date du massage')
    service_duration = models.PositiveSmallIntegerField('Durée du massage (en minutes)')
    service_comment = models.TextField('Remarque', blank=True)
    service_cashed_price = models.FloatField('Montant encaissé')
    # service_cashed_price = computed_property.ComputedFloatField( compute_from='service_theorical_price')

    def __str__(self):
        return str(self.service_date.strftime("%d.%m.%Y, %H:%M")) + " : " + str(self.service_massage_id) + " => " + str(self.service_client_id)

    def save(self, *args, **kwargs):
        print("Save 'Service': " + str(self.service_client_id) + ", " + str(self.service_massage_id))
        super(Service, self).save(*args, **kwargs)

    # class Meta:
    #     ordering = ["service_date"]

    # @property
    # def service_theorical_price(self):
    #     # print(self.service_duration)
    #     # print(self.service_massage_id)
    #     return float(self.service_duration) # * self.service_massage_id.massage_price
