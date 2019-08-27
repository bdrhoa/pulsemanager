import sys

from django.test import RequestFactory

from test_plus.test import TestCase

from unittest import mock
from unittest.mock import patch
from contextlib import contextmanager

import factory
from django.db.models import signals

from pulsemanager.users.views import UserRedirectView
from pulsemanager.users.views import UserUpdateView
from pulsemanager.users.views import UserReportView


from pulsemanager.surveys   import models as Survey
from pulsemanager.users     import models as user_models

class BaseUserTestCase(TestCase):

    def setUp(self):
        self.user = self.make_user()
        self.factory = RequestFactory()


# class TestUserRedirectView(BaseUserTestCase):
#
#     def test_get_redirect_url(self):
#         # Instantiate the view directly. Never do this outside a test!
#         view = UserRedirectView()
#         # Generate a fake request
#         request = self.factory.get('/fake-url')
#         # Attach the user to the request
#         request.user = self.user
#         # Attach the request to the view
#         view.request = request
#         # Expect: '/users/testuser/', as that is the default username for
#         #   self.make_user()
#         self.assertEqual(
#             view.get_redirect_url(),
#             '/users/testuser/'
#         )


# class TestUserUpdateView(BaseUserTestCase):
#
#     def setUp(self):
#         # call BaseUserTestCase.setUp()
#         super(TestUserUpdateView, self).setUp()
#         # Instantiate the view directly. Never do this outside a test!
#         self.view = UserUpdateView()
#         # Generate a fake request
#         request = self.factory.get('/fake-url')
#         # Attach the user to the request
#         request.user = self.user
#         # Attach the request to the view
#         self.view.request = request
#
#     def test_get_success_url(self):
#         # Expect: '/users/testuser/', as that is the default username for
#         #   self.make_user()
#         self.assertEqual(
#             self.view.get_success_url(),
#             '/users/testuser/'
#         )
#
#     def test_get_object(self):
#         # Expect: self.user, as that is the request's user object
#         self.assertEqual(
#             self.view.get_object(),
#             self.user
#         )

#@contextmanager
def mock_user_get_survey(self):
    survey = mock.Mock(autospec=Survey)
    survey.surveyid = 1
    return survey
    #theuser.get_survey().createreport()

# def mock_user_get_surveyid():
#     return 1

def mock_get_ls_data_empty(self):

    print("****mock_get_ls_data_empty*****")

    data = ({'status': 'No Data, could not get max id.'}, None) #empty

    return data

def mock_get_ls_data(self):

    print("*****mock_get_ls_data*****")

    data = ('77u/ImlkIjsic3VibWl0ZGF0ZSI7Imxhc3RwYWdlIjsic3RhcnRsYW5ndWFnZSI7InNlZWQiOyJBZ2VHcm91cCI7IkdlbmRlciI7IlJhY2UiOyJNaW5pc3RyeVJvbGUiOyJxMVt2aXMxXSI7InExW3ZpczJdIjsicTFbdmlzM10iOyJxMVt2aXM0XSI7InExW3ZpczVdIjsicTFbdmlzNl0iOyJxMVt2aXM3XSI7InEyW2xlYTFdIjsicTJbbGVhMl0iOyJxMltsZWEzXSI7InEyW2xlYTRdIjsicTJbbGVhNV0iOyJxMltsZWE2XSI7InEyW2xlYTddIjsicTNbYm9kMV0iOyJxM1tib2QyXSI7InEzW2JvZDNdIjsicTNbYm9kNF0iOyJxM1tib2Q1XSI7InEzW2JvZDZdIjsicTNbYm9kN10iOyJxNFtyZXMxXSI7InE0W3JlczJdIjsicTRbcmVzM10iOyJxNFtyZXM0XSI7InE0W3JlczVdIjsicTRbcmVzNl0iOyJxNFtyZXM3XSI7InE1W2NvbjFdIjsicTVbY29uMl0iOyJxNVtjb24zXSI7InE1W2NvbjRdIjsicTVbY29uNV0iOyJxNVtjb242XSI7InE1W2NvbjddIjsicTZbZXZhMV0iOyJxNltldmEyXSI7InE2W2V2YTNdIjsicTZbZXZhNF0iOyJxNltldmE1XSI7InE2W2V2YTZdIjsicTZbZXZhN10iOyJxN1tlZHUxXSI7InE3W2VkdTJdIjsicTdbZWR1M10iOyJxN1tlZHU0XSI7InE3W2VkdTVdIjsicTdbZWR1Nl0iOyJxN1tlZHU3XSI7InE4W3NlcjFdIjsicThbc2VyMl0iOyJxOFtzZXIzXSI7InE4W3NlcjRdIjsicThbc2VyNV0iOyJxOFtzZXI2XSI7InE4W3NlcjddIjsicTlbZmVsMV0iOyJxOVtmZWwyXSI7InE5W2ZlbDNdIjsicTlbZmVsNF0iOyJxOVtmZWw1XSI7InE5W2ZlbDZdIjsicTlbZmVsN10iOyJxMTBbd29yMV0iOyJxMTBbd29yMl0iOyJxMTBbd29yM10iOyJxMTBbd29yNF0iOyJxMTBbd29yNV0iOyJxMTBbd29yNl0iOyJxMTBbd29yN10iDQoiMjU0MyI7IjE5ODAtMDEtMDEgMDA6MDA6MDAiOyIxMSI7ImVuIjsiMTQxNzgyMDExNCI7IjQiOyIyIjsiNyI7IjIiOyIxIjsiMSI7IjEiOyIxIjsiMSI7IjEiOyIxIjsiMSI7IjEiOyIxIjsiMSI7IjEiOyIxIjsiMSI7IjEiOyIxIjsiMSI7IjEiOyIxIjsiMSI7IjEiOyIxIjsiMSI7IjEiOyIxIjsiMSI7IjEiOyIxIjsiMSI7IjEiOyIxIjsiMSI7IjEiOyIxIjsiMSI7IjEiOyIxIjsiMSI7IjEiOyIxIjsiMSI7IjEiOyIxIjsiMSI7IjEiOyIxIjsiMSI7IjEiOyIxIjsiMSI7IjEiOyIxIjsiMSI7IjEiOyIxIjsiMSI7IjEiOyIxIjsiMSI7IjEiOyIxIjsiMSI7IjEiOyIxIjsiMSI7IjEiOyIxIjsiMSI7IjEiOyIxIg0KDQo=', None)

    return data

# ******************S-DATA********************
# b'\xef\xbb\xbf"id";"submitdate";"lastpage";"startlanguage";"seed";"AgeGroup";"Gender";"Race";"MinistryRole";"q1[vis1]";"q1[vis2]";"q1[vis3]";"q1[vis4]";"q1[vis5]";"q1[vis6]";"q1[vis7]";"q2[lea1]";"q2[lea2]";"q2[lea3]";"q2[lea4]";"q2[lea5]";"q2[lea6]";"q2[lea7]";"q3[bod1]";"q3[bod2]";"q3[bod3]";"q3[bod4]";"q3[bod5]";"q3[bod6]";"q3[bod7]";"q4[res1]";"q4[res2]";"q4[res3]";"q4[res4]";"q4[res5]";"q4[res6]";"q4[res7]";"q5[con1]";"q5[con2]";"q5[con3]";"q5[con4]";"q5[con5]";"q5[con6]";"q5[con7]";"q6[eva1]";"q6[eva2]";"q6[eva3]";"q6[eva4]";"q6[eva5]";"q6[eva6]";"q6[eva7]";"q7[edu1]";"q7[edu2]";"q7[edu3]";"q7[edu4]";"q7[edu5]";"q7[edu6]";"q7[edu7]";"q8[ser1]";"q8[ser2]";"q8[ser3]";"q8[ser4]";"q8[ser5]";"q8[ser6]";"q8[ser7]";"q9[fel1]";"q9[fel2]";"q9[fel3]";"q9[fel4]";"q9[fel5]";"q9[fel6]";"q9[fel7]";"q10[wor1]";"q10[wor2]";"q10[wor3]";"q10[wor4]";"q10[wor5]";"q10[wor6]";"q10[wor7]"\r\n"2543";"1980-01-01 00:00:00";"11";"en";"1417820114";"4";"2";"7";"2";"1";"1";"1";"1";"1";"1";"1";"1";"1";"1";"1";"1";"1";"1";"1";"1";"1";"1";"1";"1";"1";"1";"1";"1";"1";"1";"1";"1";"1";"1";"1";"1";"1";"1";"1";"1";"1";"1";"1";"1";"1";"1";"1";"1";"1";"1";"1";"1";"1";"1";"1";"1";"1";"1";"1";"1";"1";"1";"1";"1";"1";"1";"1";"1";"1";"1";"1";"1";"1";"1"\r\n\r\n'
# **************************************



# ***********CONTEXT***********
# {'sid': 251489, 'church_name': '', 'report_date': '2018-07-06', 'responses': 0, 'img_vision': 'nodata.jpeg', 'img_leadership': 'nodata.jpeg', 'img_mobilization': 'nodata.jpeg', 'img_stewardship': 'nodata.jpeg', 'img_context': 'nodata.jpeg', 'img_evangelism': 'nodata.jpeg', 'img_discipleship': 'nodata.jpeg', 'img_service': 'nodata.jpeg', 'img_fellowship': 'nodata.jpeg', 'img_worship': 'nodata.jpeg', 'img_category': 'nodata.jpeg', 'img_radar': 'nodata.jpeg'}
# ***********CONTEXT***********


# ***********CONTEXT***********
# {'sid': 113242, 'church_name': 'The Chuch', 'report_date': '2018-07-06', 'responses': 1, 'img_vision': '113242_vision.png', 'img_leadership': '113242_leadership.png', 'img_mobilization': '113242_mobilization.png', 'img_stewardship': '113242_stewardship.png', 'img_context': '113242_context.png', 'img_evangelism': '113242_evangelism.png', 'img_discipleship': '113242_discipleship.png', 'img_service': '113242_service.png', 'img_fellowship': '113242_fellowship.png', 'img_worship': '113242_worship.png', 'img_category': '113242_category.png', 'img_radar': '113242_radar.png'}
# ***********CONTEXT***********


# def trace_calls_and_returns(frame, event, arg):
#     co = frame.f_code
#     func_name = co.co_name
#     if func_name == 'write':
#         # Ignore write() calls from print statements
#         return
#     line_no = frame.f_lineno
#     filename = co.co_filename
#     if event == 'call':
#         print("Call to {1} on line {2} of {3}".format(func_name, line_no, filename))
#         return trace_calls_and_returns
#     elif event == 'return':
#         print("{1} => {2}".format(func_name, arg))
#     return

@patch('pulsemanager.surveys.models.Survey._get_ls_data', side_effect = ['mock_get_ls_data','mock_get_ls_data_empty'])
@patch('pulsemanager.users.views.User.get_survey', new = mock_user_get_survey)
class TestUserReportView(TestCase):
    @factory.django.mute_signals(signals.post_save) #don't call the after save signal
    def setUp(self):

        # call BaseUserTestCase.setUp()
        #super(TestUserReportView, self).setUp()
        # Instantiate the view directly. Never do this outside a test!
        self.user = user_models.User()
        self.user.username = 'testuser'
        self.user.save()

        self.view = UserReportView()
        # Generate a fake request
        self.factory = RequestFactory()
        request = self.factory.get('/fake-url')
        # Attach the user to the request
        request.user = self.user
        # Attach the request to the view
        self.view.request = request


    def test_get_context_data_empty(self, mock_get_ls_data_empty):
        print("test get context data - empty")

        theContext = self.view.get_context_data()
        print(theContext)
        survey_id = theContext['sid']
        self.assertEqual(survey_id, 1)
        total_responses = theContext['responses']
        self.assertEqual(total_responses, 0)

    def test_get_context_data(self, mock_get_ls_data):
        print("test get context data")
        theContext = self.view.get_context_data()
        print(theContext)
        survey_id = theContext['sid']
        self.assertEqual(survey_id, 1)
        total_responses = theContext['responses']
        self.assertEqual(total_responses, 1)
