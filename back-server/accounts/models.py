from django.db import models
from django.contrib.auth.models import AbstractUser
from products.models import DepositProducts, SavingProducts

# Create your models here.
class User(AbstractUser):
    fin_prdt_cd = models.ForeignKey(
        DepositProducts,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='users_deposit',
    )  # DepositProducts 모델과의 ForeignKey

    fin_prdt_cd_saving = models.ForeignKey(
        SavingProducts,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='users_saving',
    )  # SavingProducts 모델과의 ForeignKey