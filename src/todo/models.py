from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)  # otomatik tarih kaydediyor
    completed = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_date']  # eksi olunca güncel olan en üstte/önde oluyor
        # verbose_name = "pizza"
    
    def __str__(self):
        return self.title