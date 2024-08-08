Database structure and models
=============================

**The project has 4 models**

* **User** ::

    In this project we use the abstract user provide by Django
    from django.contrib.auth.models import User

* **Profile** ::

    class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

* **Lettings** ::

    class Letting(models.Model):
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

* **Address** ::

    class Address(models.Model):
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(
        max_length=3, validators=[MinLengthValidator(3)]
    )

