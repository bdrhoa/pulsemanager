from django.apps import AppConfig


class SurveysConfig(AppConfig):
    name = 'pulsemanager.surveys'
    verbose_name = "Surveys"

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        pass
