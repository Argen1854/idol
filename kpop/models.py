from django.db import models


class Kpop(models.Model):
    name = models.CharField(max_length=100)
    group = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')
    description = models.TextField()
    date_birth = models.DateField()
    rating = models.ForeignKey('Rating', on_delete=models.CASCADE, )


class Rating(models.Model):
    RATING_IDOL = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    ]
    rating = models.CharField(max_length=2, choices=RATING_IDOL)

