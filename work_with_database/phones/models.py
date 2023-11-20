from django.db import models


class Phone(models.Model):
    name=models.CharField(max_length=25)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    image=models.ImageField()
    release_date=models.DateField()
    lte_existing=models.BooleanField()
    slug=models.SlugField(max_length=25,primary_key=True ,unique=True, db_index=True,verbose_name="slug")


    def __str__(self):
        return f'{self.name}'