from .models import Question,QuestionPapers
from rest_framework import serializers

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class QuestionPapersSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionPapers
        fields = "__all__"

