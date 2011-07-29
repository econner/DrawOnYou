from django.db import models

class FacebookProfile(models.Model):
    """
    There will be one facebook profile for each user.
    """
    fbid = models.IntegerField()		# id as assigned by facebook (e.g. 1674638376)
    name = models.CharField(max_length=64)	# full name (e.g. "Eric Conner")
    email = models.EmailField(blank=True)
    gender = models.CharField(max_length=6,blank=True)
    birthday = models.DateField(blank=True,null=True)
    
    def __unicode__(self):
        return self.name

class DrawSession(models.Model):
    """
    We'll track when a user begins using the app, for how long,
    and if he / she is successfull.
    """
    profile = models.ForeignKey(FacebookProfile)
    date_began = models.DateTimeField(auto_now = True)
    date_finished = models.DateTimeField()
    finished = models.BooleanField()
    drawee_id = models.IntegerField()
    filename = models.CharField(max_length=50)
    last_page_viewed =models.CharField(max_length=50)
    
    
    
    
    
    
