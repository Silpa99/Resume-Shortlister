from rest_framework import serializers
from api.models import Question, Option


class OptionSerializer(serializers.ModelSerializer):
    """Serialize options."""

    class Meta:
        model = Option
        fields = ('id', 'option')


class QuestionSerializer(serializers.ModelSerializer):

    options = OptionSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = ('id','question','options')


class AnswerSerializer(serializers.Serializer):
    question_id = serializers.IntegerField()
    option_id = serializers.IntegerField()


class ResponseUpsertSerializer(serializers.Serializer):
    job_id = serializers.IntegerField()
    response = AnswerSerializer(many=True)