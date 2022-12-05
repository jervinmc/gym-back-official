from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid


from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid
from django.utils import timezone
# Create your models here.

def nameFile(instance, filename):
    """
    Custom function for naming image before saving.
    """
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)

    return 'uploads/{filename}'.format(filename=filename)


class Transaction(models.Model):
    user_id = models.IntegerField(_('user_id'),default=0.0)
    product_id = models.IntegerField(_('product_id'),default=0.0)
    quantity = models.IntegerField(_('quantity'),default=0.0)
    created_date=models.DateTimeField(_('created_date'), null=False,blank=False,default=timezone.now)
    class Meta:
        ordering = ["-id"]
