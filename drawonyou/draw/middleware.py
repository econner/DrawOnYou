import facebook, urllib, cgi, re
from django.conf import settings

class Facebook(object):
    def __init__(self, user=None):
        if user is None:
            self.uid = None
        else:
            self.uid = user['uid']
            self.user = user
            self.graph = facebook.GraphAPI(user['access_token'])


class FacebookMiddleware(object):
    def process_request(self, request):
        """
        Enables ``request.facebook`` and ``request.facebook.graph`` in your views 
        once the user authenticated the  application and connected with facebook. 
        You might want to use this if you don't feel confortable with the 
        javascript library.
        """
        #print "COOKIES: %s" % str(request.COOKIES) 
        fb_user = facebook.get_user_from_cookie(request.COOKIES,
            settings.FACEBOOK_API_KEY, settings.FACEBOOK_SECRET_KEY)
        #print "FB USER: %s" % str(fb_user)
        request.facebook = Facebook(fb_user)
        
        return None

class FakeSessionCookieMiddleware(object):
    
    def process_request(self, request):
        if not request.COOKIES.has_key("fbs_%s" % settings.FACEBOOK_API_KEY) \
            and request.GET.has_key("fs_%s" % settings.FACEBOOK_API_KEY):
            #print request.GET["fs_%s" % settings.FACEBOOK_API_KEY]
            request.COOKIES["fbs_%s" % settings.FACEBOOK_API_KEY] = urllib.unquote(request.GET["fs_%s" % settings.FACEBOOK_API_KEY]).decode("utf-8")
        elif not request.COOKIES.has_key("fbs_%s" % settings.FACEBOOK_API_KEY) \
            and request.method == "POST" \
            and request.META.has_key("HTTP_REFERER"):
            # try to get the fbs session data from the referer.. this will only happen on uploading a photo
            print request.META['HTTP_REFERER']
            m = re.search("fs_%s=(.*?)&" % settings.FACEBOOK_API_KEY, request.META['HTTP_REFERER'])
            if m:
                request.COOKIES["fbs_%s" % settings.FACEBOOK_API_KEY] = urllib.unquote(m.group(1)).decode("utf-8")
            
		