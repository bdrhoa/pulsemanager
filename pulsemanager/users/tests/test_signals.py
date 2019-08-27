from test_plus.test import TestCase
from unittest import mock
from unittest.mock import patch
from contextlib import contextmanager

import django.db.models.signals
from django.db.models.signals import post_save

from pulsemanager.users.signals import post_save_User_receiver

@contextmanager
def catch_signal(signal):
    """Catch django signal and return the mocked call."""
    handler = mock.Mock()
    signal.connect(handler)
    yield handler
    signal.disconnect(handler)



def mock_copy_limesurvey(self):

    self.surveyname = "testsurvey"
    self.surveyid = 1
    self.issurveyactive = True

@patch('pulsemanager.surveys.models.Survey.copy_limesurvey', side_effect=mock_copy_limesurvey)
class TestSignals(TestCase):
    """docstring for TestSignals."""

#CASE1: first survey for a new church
    def test_first_survey_for_new_church(self, mock_copy_limesurvey):
        with catch_signal(post_save_User_receiver) as handler:
            self.user = self.make_user()
            self.user.save()
        handler.assert_called_once_with(
            sender=mock.ANY,
            signal=post_save_User_receiver,
        )


#CASE2: toggle survey from on to off
#CASE3: toggle survey from off to on
#CASE4: on with changes only to other fields
#CASE5: off with changes only to other fields
