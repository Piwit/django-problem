from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView

from .serializers import ProblemSerializer
from .models import Problem


class CreateProblemAPI(CreateAPIView):
    serializer_class = ProblemSerializer


class RetrieveProblemAPI(RetrieveAPIView):
    serializer_class = ProblemSerializer
    queryset = Problem.objects.all()


class ListProblemAPI(ListAPIView):
    serializer_class = ProblemSerializer
    queryset = Problem.objects.all()
