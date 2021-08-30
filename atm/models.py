from django.db import models


class Session(models.Model):
    D_HUNDRED = models.IntegerField(null=True, default=0)
    D_FIFTY = models.IntegerField(null=True, default=0)
    D_TWENTY = models.IntegerField(null=True, default=0)
    D_TEN = models.IntegerField(null=True, default=0)
    C_FIFTY = models.IntegerField(null=True, default=0)
    C_TWENTY = models.IntegerField(null=True, default=0)
    C_TEN = models.IntegerField(null=True, default=0)
    C_FIVE = models.IntegerField(null=True, default=0)
