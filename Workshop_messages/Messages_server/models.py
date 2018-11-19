from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=160)
    surname = models.CharField(max_length=160)
    description = models.TextField()
    adress = models.ForeignKey('Adress', null=True, on_delete=models.SET(None))
    group = models.ManyToManyField('Groups')

    class Meta:
        get_latest_by = ['id']

    def __str__(self):
        return f"{self.name} {self.surname}"


class Adress(models.Model):
    city = models.CharField(max_length=160)
    street = models.CharField(max_length=160)
    house = models.IntegerField()
    flat = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.city}, ul. {self.street} {self.house} m. {self.flat}"


class Telephone(models.Model):
    phone_number = models.IntegerField()
    phone_description = models.CharField(max_length=160)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.phone_number} ({self.phone_description})"


class Email(models.Model):
    email_adress = models.EmailField()
    email_description = models.CharField(max_length=160)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.email_adress} ({self.email_description})"


class Groups(models.Model):
    group_name = models.CharField(max_length=160)

    def __str__(self):
        return f"{self.group_name}"



