from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.serializers import QuestionSerializer, ResponseUpsertSerializer
from api.models import Question, Option
from web_app.models import Job_postings


class QuestionView(ListAPIView):

    def get_queryset(self):
        job_id = self.request.query_params.get('job_id', None)
        queryset = Question.objects.filter(job=job_id)
        return queryset

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(self):
            self.evaluate_answers(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return QuestionSerializer
        if self.request.method == 'POST':
            return ResponseUpsertSerializer

    def evaluate_answers(self, serializer):
        data = serializer.data.get('response')
        job_id = serializer.data.get('job_id')
        que_opt_list = [tuple(response.values()) for response in data]
        question_ids, option_ids = map(list, zip(*que_opt_list))

        question_answer_map = Option.objects.filter(
            question_id__in=question_ids).filter(
            is_correct=True).values_list(
            'question',
            'id')

        score = len(set(que_opt_list).intersection(set(question_answer_map)))
        job_application = Job_postings.objects.get(
            id=job_id).applicants.get(
            applicant=self.request.user)
        job_application.evaluated_score = score
        job_application.save()
