from django.contrib.auth.models import User
from django.db import models


class SalesOrders(models.Model):
    amount = models.IntegerField()
    description = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Заказ на продажу'
        verbose_name_plural = 'Заказы на продажу'
