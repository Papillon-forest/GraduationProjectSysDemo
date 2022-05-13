import pickle

import numpy as np
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
class Topic(models.Model):
    """用户学习的主题"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Entry(models.Model):
    """学到的有关某个主题的具体知识"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    # rules = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('14', '14'), ('30', '30')]  # Default management rule
    # key_days = models.CharField(max_length=5, choices=rules, default=1)
    key_days = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(30)])
    rating_5 = models.DecimalField(max_digits=11, decimal_places=10,
                                   validators=[MinValueValidator(0), MaxValueValidator(1)])
    rating_4 = models.DecimalField(max_digits=11, decimal_places=10,
                                   validators=[MinValueValidator(0), MaxValueValidator(1)])
    rating_3 = models.DecimalField(max_digits=11, decimal_places=10,
                                   validators=[MinValueValidator(0), MaxValueValidator(1)])
    rating_2 = models.DecimalField(max_digits=11, decimal_places=10,
                                   validators=[MinValueValidator(0), MaxValueValidator(1)])
    rating_1 = models.DecimalField(max_digits=11, decimal_places=10,
                                   validators=[MinValueValidator(0), MaxValueValidator(1)])
    rating_average = models.DecimalField(max_digits=11, decimal_places=10,
                                         validators=[MinValueValidator(0), MaxValueValidator(5)])
    positive_percent = models.DecimalField(max_digits=11, decimal_places=10,
                                           validators=[MinValueValidator(0), MaxValueValidator(1)])

    def user_retention(self):
        with open('/Users/xiayi/PycharmProjects/GraduationProject/saved_model.pkl', 'rb') as f:
            model_linregr = pickle.load(f)

        x_test = np.array(
            [[self.key_days], [self.rating_5], [self.rating_4], [self.rating_3], [self.rating_2], [self.rating_1],
             [self.rating_average], [self.positive_percent]]).reshape(-1, 8)

        y_test_pred = model_linregr.predict(x_test)

        return y_test_pred

    user_retention.short_decsription = '未知'

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return f"{self.text[:10]}..."
