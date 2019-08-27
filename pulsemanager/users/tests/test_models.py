from test_plus.test import TestCase

from pulsemanager.surveys   import models as survey_models
from pulsemanager.users     import models as user_models

class TestUser(TestCase):

    def setUp(self):
        self.user = self.make_user()


    def test__str__(self):
        self.assertEqual(
            self.user.__str__(),
            'testuser'  # This is the default username for self.make_user()
        )

    def test_get_absolute_url(self):
        self.assertEqual(
            self.user.get_absolute_url(),
            '/users/testuser/'
        )

    def test_get_surveyid(self):
        self.survey = survey_models.Survey(
            user = self.user
        )
        self.survey.save()
        self.assertEqual(self.user.get_surveyid(),
            0 # This is the default surveyid
        )
