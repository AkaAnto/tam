from django.db import models
from TAM import settings
from TAM.custom_storage import MediaStorage


class Customer(models.Model):
  name = models.CharField(max_length=255, )
  last_name = models.CharField(max_length=255)
  photo = models.ImageField(upload_to='uploads/images', storage=MediaStorage, null=True, blank=True)
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name="customers")
  editor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name="edited_customers", null=True, blank=True, default=None)
  created_on = models.DateTimeField(auto_now=True)
  updated_on = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"Customer: {self.name} {self.last_name}"
