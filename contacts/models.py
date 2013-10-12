from django.db import models
from django.core.urlresolvers import reverse

class Contact(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField()

    def __unicode__(self):
        return u' '.join([self.first_name, self.last_name])
    def get_absolute_url(self):
        return reverse('contacts-view', kwargs={'pk': self.id})


