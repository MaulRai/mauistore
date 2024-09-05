from django.db import models

class MoodEntry(models.Model):
    mood = models.CharField(max_length=255)
    time = models.DateField(auto_now_add=True)
    feelings = models.TextField()
    mood_intensity = models.IntegerField()

    @property
    def is_mood_strong(self):
        return self.mood_intensity > 5
    
    
class Product(models.Model):
    name = models.CharField(max_length=63)
    price = models.IntegerField()
    desc = models.CharField(max_length=255)
    
    @property
    def get_formatted_price(self):
        return f"Rp{self.price:,.0f}".replace(",", ".")