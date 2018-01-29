import logging

from django.db.models.signals import post_save
from django.dispatch import receiver

from pulsemanager.surveys   import models as survey_models
from pulsemanager.users     import models as user_models



#CASE1: first survey for a new church
#CASE2: toggle survey from on to off
#CASE3: toggle survey from off to on
#CASE4: on with changes only to other fields
#CASE5: off with changes only to other fields

#REFERENCE: https://stackoverflow.com/questions/23926385/difference-between-objects-create-and-object-save-in-django-orm

def _create_new_survey(instance):
    thesurvey = survey_models.Survey(user=instance)
    thesurvey.copy_limesurvey()
    thesurvey.save(force_insert=True)



def post_save_User_receiver(sender, instance, *args, **kwargs):

    logger = logging.getLogger()
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
            '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

    logger.debug('*** start post_save_User_receiver ***')

    activestatuschanged = instance.tracker.has_changed("acitvesurvey")
    previousstatus      = instance.tracker.previous("acitvesurvey")

    logger.debug('activestatuschanged %s', activestatuschanged)
    logger.debug('previousstatus %s', previousstatus)

    try:
        #CASE2 on to off
        thesurvey       = instance.surveys.get(issurveyactive = True)
        logger.debug('thesurvey %s', thesurvey.surveyid)
        if activestatuschanged and previousstatus:
            #if status changed from active to inactive
            #set the current survey to inactive
            thesurvey.issurveyactive = False
            # set expired in lime survey, remember i keep a separate (in)active status
            #                             and I can't actually deactivate in LS
            thesurvey.save()
            thesurvey.expire()

    except Exception as e:
        logger.debug(e)
        #CASE 1 & CASE 3 off/new to on
        #TODO handle multple result exception
        if activestatuschanged and not previousstatus:
            logger.debug('*** call _create_new_survey ***')
            _create_new_survey(instance)
    
    logger.debug('*** end post_save_User_receiver ***')
