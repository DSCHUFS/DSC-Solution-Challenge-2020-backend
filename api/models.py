from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=20)  # 이름
    id = models.AutoField(primary_key=True)  # 주민등록번호 Primary_Key
    age = models.IntegerField()  # 나이
    # heart_rate = models.IntegerField()  # 심박수

    def __str__(self):
        return self.name
