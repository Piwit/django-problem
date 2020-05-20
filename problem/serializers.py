from rest_framework.serializers import ModelSerializer

from .models import Problem


class ProblemSerializer(ModelSerializer):
    class Meta:
        model = Problem
        exclude = ['resolved', 'resolved_at']
