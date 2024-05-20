from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_added']
        verbose_name_plural = 'categories'
        verbose_name = 'category'
    
    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(Category, related_name=('categorie'), on_delete=models.CASCADE)
    image = models.CharField(max_length=5000)
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_added']
    
    def __str__(self):
        return self.title