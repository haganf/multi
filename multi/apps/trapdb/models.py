from django.db import models
from django.utils.translation import ugettext_lazy as _

from mezzanine.core.models import Displayable, Ownable, Slugged
from mezzanine.generic.fields import CommentsField
from mezzanine.conf import settings


class MultiDatabase(Displayable, Ownable):
    """
    A database entry!
    """
    engine = models.CharField(max_length=64)
    dbname = models.CharField(max_length=64)
    dbuser = models.CharField(max_length=64)
    dbpass = models.CharField(max_length=64)
    dbhost = models.CharField(max_length=64)
    dbport = models.CharField(max_length=64)

    class Meta:
        verbose_name = _("Multi Database")
        verbose_name_plural = _("Multi Databases")
        ordering = ("-dbhost",)




