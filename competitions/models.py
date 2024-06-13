from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name

class Competition(models.Model):
    category = models.ForeignKey(Category, related_name='competitions', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank = True, null = True)
    image = models.ImageField(upload_to='competition_images', blank=True, null=True)
    deadline = models.DateTimeField(blank = True, null = True)
    has_passed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('auth.User', related_name='competitions', on_delete=models.CASCADE)
    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Competitions"
    
    def __str__(self):
        return self.name
