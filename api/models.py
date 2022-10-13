from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class PostModel(models.Model):
    post_id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='posts/%Y%M%d', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    reason = models.TextField(null=True, blank=True, verbose_name='Reject Reason')
    status = models.CharField(max_length= 50, null=True, blank=True, verbose_name='Approved')

    def __str__(self):
        return self.post_name



