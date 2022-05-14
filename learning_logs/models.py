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

    rules = [('0', '0'), ('1', '月初第1天后'), ('2', '月初第2天后'), ('3', '月初第3天后'), ('4', '月初第4天后'), ('5', '月初第5天后'), ('6', '月初第6天后'),
             ('7', '月初第7天后')]  # Default management rule
    key_days = models.CharField(max_length=10, choices=rules, default='0')
    # key_days = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(30)])
    last_retention = models.DecimalField(default=0, max_digits=11, decimal_places=10,
                                         validators=[MinValueValidator(0), MaxValueValidator(1)])
    rating_5 = models.DecimalField(default=0, max_digits=11, decimal_places=10,
                                   validators=[MinValueValidator(0), MaxValueValidator(1)])
    rating_4 = models.DecimalField(default=0, max_digits=11, decimal_places=10,
                                   validators=[MinValueValidator(0), MaxValueValidator(1)])
    rating_3 = models.DecimalField(default=0, max_digits=11, decimal_places=10,
                                   validators=[MinValueValidator(0), MaxValueValidator(1)])
    rating_2 = models.DecimalField(default=0, max_digits=11, decimal_places=10,
                                   validators=[MinValueValidator(0), MaxValueValidator(1)])
    rating_1 = models.DecimalField(default=0, max_digits=11, decimal_places=10,
                                   validators=[MinValueValidator(0), MaxValueValidator(1)])
    rating_average = models.DecimalField(default=0, max_digits=11, decimal_places=10,
                                         validators=[MinValueValidator(0), MaxValueValidator(5)])
    positive_percent = models.DecimalField(default=0, max_digits=11, decimal_places=10,
                                           validators=[MinValueValidator(0), MaxValueValidator(1)])

    def user_retention(self):
        with open('/Users/xiayi/PycharmProjects/GraduationProject/saved_model.pkl', 'rb') as f:
            model_linregr = pickle.load(f)

        x_test = np.array(
            [[self.key_days], [self.last_retention], [self.rating_5], [self.rating_4], [self.rating_3], [self.rating_2],
             [self.rating_1],
             [self.rating_average], [self.positive_percent]]).reshape(-1, 9)

        y_test_pred = model_linregr.predict(x_test)

        return y_test_pred

    user_retention.short_decsription = '未知'

    rules_middle = [('0', '0'), ('Middle', '月中旬（第14天）')]  # Default management rule
    key_days_middle = models.CharField(max_length=10, choices=rules_middle, default='0')
    # key_days = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(30)])
    retention_1_middle = models.DecimalField(default=0, max_digits=20, decimal_places=19,
                                             validators=[MinValueValidator(0), MaxValueValidator(1)])
    retention_2_middle = models.DecimalField(default=0, max_digits=20, decimal_places=19,
                                             validators=[MinValueValidator(0), MaxValueValidator(1)])
    retention_3_middle = models.DecimalField(default=0, max_digits=20, decimal_places=19,
                                             validators=[MinValueValidator(0), MaxValueValidator(1)])
    retention_4_middle = models.DecimalField(default=0, max_digits=20, decimal_places=19,
                                             validators=[MinValueValidator(0), MaxValueValidator(1)])
    retention_5_middle = models.DecimalField(default=0, max_digits=20, decimal_places=19,
                                             validators=[MinValueValidator(0), MaxValueValidator(1)])
    retention_6_middle = models.DecimalField(default=0, max_digits=20, decimal_places=19,
                                             validators=[MinValueValidator(0), MaxValueValidator(1)])
    retention_7_middle = models.DecimalField(default=0, max_digits=20, decimal_places=19,
                                             validators=[MinValueValidator(0), MaxValueValidator(1)])

    def user_retention_middle(self):
        with open('/Users/xiayi/PycharmProjects/GraduationProject/saved_model_middle.pkl', 'rb') as f:
            model_linregr = pickle.load(f)

        x_test_middle = np.array(
            [[self.retention_1_middle], [self.retention_2_middle], [self.retention_3_middle], [self.retention_4_middle],
             [self.retention_5_middle], [self.retention_6_middle], [self.retention_7_middle]
             ]).reshape(-1, 7)

        y_test_pred_middle = model_linregr.predict(x_test_middle)

        return y_test_pred_middle

    user_retention_middle.short_decsription = '未知'

    rules_end = [('0', '0'), ('End', '月末（第30天）')]  # Default management rule
    key_days_end = models.CharField(max_length=10, choices=rules_end, default='0')
    # key_days = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(30)])
    retention_1_end = models.DecimalField(default=0, max_digits=20, decimal_places=19,
                                          validators=[MinValueValidator(0), MaxValueValidator(1)])
    retention_2_end = models.DecimalField(default=0, max_digits=20, decimal_places=19,
                                          validators=[MinValueValidator(0), MaxValueValidator(1)])
    retention_3_end = models.DecimalField(default=0, max_digits=20, decimal_places=19,
                                          validators=[MinValueValidator(0), MaxValueValidator(1)])
    retention_4_end = models.DecimalField(default=0, max_digits=20, decimal_places=19,
                                          validators=[MinValueValidator(0), MaxValueValidator(1)])
    retention_5_end = models.DecimalField(default=0, max_digits=20, decimal_places=19,
                                          validators=[MinValueValidator(0), MaxValueValidator(1)])
    retention_6_end = models.DecimalField(default=0, max_digits=20, decimal_places=19,
                                          validators=[MinValueValidator(0), MaxValueValidator(1)])
    retention_7_end = models.DecimalField(default=0, max_digits=20, decimal_places=19,
                                          validators=[MinValueValidator(0), MaxValueValidator(1)])
    retention_8_end = models.DecimalField(default=0, max_digits=20, decimal_places=19,
                                          validators=[MinValueValidator(0), MaxValueValidator(1)])

    def user_retention_end(self):
        with open('/Users/xiayi/PycharmProjects/GraduationProject/saved_model_end.pkl', 'rb') as f:
            model_linregr = pickle.load(f)

        x_test_end = np.array(
            [[self.retention_1_end], [self.retention_2_end], [self.retention_3_end], [self.retention_4_end],
             [self.retention_5_end], [self.retention_6_end], [self.retention_7_end], [self.retention_8_end]
             ]).reshape(-1, 8)

        y_test_pred_end = model_linregr.predict(x_test_end)

        return y_test_pred_end

    user_retention_middle.short_decsription = '未知'

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return f"{self.text[:10]}..."
