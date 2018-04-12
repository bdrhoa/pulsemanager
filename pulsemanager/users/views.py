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
        thechurch = theuser.churchname
        
        context = {'sid': thesurvey,
        'church_name': thechurch,
        'report_date': str(datetime.date.today()),
        'responses': int(reportdata['responses']),
        'img_vision': "{surveyid}_vision.png".format(surveyid = thesurvey),
        'img_leadership': "{surveyid}_leadership.png".format(surveyid = thesurvey),
        'img_mobilization': "{surveyid}_mobilization.png".format(surveyid = thesurvey),
        'img_stewardship': "{surveyid}_stewardship.png".format(surveyid = thesurvey),
        'img_context': "{surveyid}_context.png".format(surveyid = thesurvey),
        'img_evangelism': "{surveyid}_evangelism.png".format(surveyid = thesurvey),
        'img_disipleship': "{surveyid}_disipleship.png".format(surveyid = thesurvey),
        'img_service': "{surveyid}_service.png".format(surveyid = thesurvey),
        'img_fellowship': "{surveyid}_fellowship.png".format(surveyid = thesurvey),
        'img_worship': "{surveyid}_worship.png".format(surveyid = thesurvey),
        'img_category': "{surveyid}_category.png".format(surveyid = thesurvey),
        'img_radar': "{surveyid}_radar.png".format(surveyid = thesurvey)
        }  
        return context