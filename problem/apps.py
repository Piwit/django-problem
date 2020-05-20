from django.apps import AppConfig


class ProblemConfig(AppConfig):
    name = 'problem'
    verbose_name = 'Problems'

    def ready(self):
        import problem.signals
