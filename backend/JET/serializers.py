from rest_framework import serializers
from user.models import Questionnaire

class QuestionnaireSerializer(serializers.Serializer):
    questionnaireID = serializers.IntegerField(required=True)
    questionnaireName = serializers.CharField(max_length=200)

    def create(self, validated_data):
        # create and return a new questionnaire
        return Questionnaire.objects.create(**validated_data)