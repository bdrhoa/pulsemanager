import datetime
import requests

from django.urls import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView, TemplateView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from .models import User


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})


class UserUpdateView(LoginRequiredMixin, UpdateView):

    fields = ['name', 'churchname', 'acitvesurvey']

    # we already imported User in the view code above, remember?
    model = User

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})

    def get_object(self):
        # Only get the User record for the user making the request
        return User.objects.get(username=self.request.user.username)


class UserListView(LoginRequiredMixin, ListView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'

class UserReportView(LoginRequiredMixin, TemplateView):
    model = User
    template_name = 'users/reports/rptemplate/report.html'
    def get_context_data(self, **kwargs):
        #context = super(DisplayTaskView, self).get_context_data(kwargs)
            #TODO: retrieve the actual data
        theuser = self.request.user
        thesurvey = theuser.get_survey().surveyid
        reportdata = theuser.get_survey().createreport()
        
        context = {'sid': thesurvey,
        'church_name': 'Lakeview Bible',
        'report_date': str(datetime.date.today()),
        'responses': int(reportdata['responses']),
        'img_vision': 'image1.png',
        'img_leadership': 'image1.png',
        'img_mobilization': 'image1.png',
        'img_stewardship': 'image1.png',
        'img_context': 'image1.png',
        'img_evangelism': 'image1.png',
        'img_disipleship': 'image1.png',
        'img_service': 'image1.png',
        'img_fellowship': 'image1.png',
        'img_worship': 'image1.png',
        'img_category': 'image1.png',
        'img_radar': "{surveyid}_radar.png".format(surveyid = thesurvey)
        }  
        return context