from rest_framework import serializers
from .models import Person


# queryset과 같은 복잡한 데이터를 json, xml 과 같은 유형으로 변환
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person  # 모델 설정
        fields = ('name', 'id', 'age')  # 필드 설정
