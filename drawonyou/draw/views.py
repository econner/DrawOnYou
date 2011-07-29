from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.conf import settings
from json import loads
import urllib2, urllib, cgi
from drawonyou.draw.utils import MultiPartForm
from drawonyou.draw.models import FacebookProfile
import os, uuid, time, datetime
from django.http import HttpResponse

def get_user(request):
    """
    Utility function that gets the logged in user if there is one.
    """
    user = None
    if(request.facebook.uid is not None):
        user = request.facebook.user
        # store this user in db if this is our first encounter
        fbuser = FacebookProfile.objects.filter(fbid = request.facebook.uid)
        if not fbuser:
            fbprofile = request.facebook.graph.get_object(request.facebook.uid)
            namestr = "%s %s" % (fbprofile['first_name'], fbprofile['last_name'])

            bday = None
            emailstr = ''
            genderstr = ''
            
            if "birthday" in fbprofile and fbprofile['birthday']:
                bday = datetime.datetime(*time.strptime(fbprofile['birthday'], "%m/%d/%Y")[:6])
    
            if "email" in fbprofile and fbprofile['email']:
                emailstr = fbprofile['email']
            
            if "gender" in fbprofile and fbprofile['gender']:
                genderstr = fbprofile['gender']
            
            
            localprofile = FacebookProfile(name = namestr,
                                           email = emailstr,
                                           fbid = request.facebook.uid,
                                           birthday = bday,
                                           gender = genderstr)
            localprofile.save()
    return user

def upload_photo(request):
    """
    View called to upload a photo back to facebook after
    the user has finished with our app.
    """
    #print request.session['fbs']
    error = ""
    if request.session['friend_id']:
        # create the unique path to this file
        userdir = "%s%s/%s" % (settings.FINISHED_PATH,
                               request.facebook.uid.encode("ascii"),
                               request.session['friend_id'].encode("ascii"))
        if not os.path.exists(userdir):
            os.makedirs(userdir)
        
        filestr = str(uuid.uuid4()) # generate a random unique uuid for this filename
        filename = "%s/%s.jpg" % (userdir, filestr)
        
        if(request.raw_post_data is not None):
            # save the data to file
            fout = open(filename, "wb")
            fout.write(request.raw_post_data)
            fout.close()

            # setup the form to post the photo
            form = MultiPartForm()
            form.addField('message', settings.PHOTO_CAPTION)

            fp = open(filename)
            form.addFile('source', filename, fp)
            body = str(form)
            
            req = urllib2.Request('https://graph.facebook.com/' + request.facebook.uid.encode("ascii") + "/photos?access_token=" + request.facebook.user['access_token'].encode("ascii"))
            req.add_header('Content-type', form.getContentType())
            req.add_data(body)

            #POST-away!
            photo = urllib2.urlopen(req)
            
        else:
            # TODO log error / error output
            # TODO make this error message nicer
            error = "File could not be saved!"
            print "ERROR: no post data at upload_photo"
    else:
        error = "No friend selected!"
        
    return render_to_response(
        "upload_photo.html",
        { "error": error,
          "facebook_canvas_url" : settings.FACEBOOK_CANVAS_URL,
          "finished_url" : settings.FINISHED_URL,
          "friend_id" : request.session['friend_id'],
          "filename" : filestr,
          "user" : get_user(request),
        },
        context_instance = RequestContext(request)
    )
	
def retrieve_photo(request):
    """
    View that grabs a selected photo from facebook and loads the image editor
    """
    if request.session['friend_id'] or request.GET['friend_id']:
        
        filename = "%s%s%s" % (settings.UPLOAD_PATH,
                                request.facebook.uid,
                                request.GET['photo_url'][-4:])
								
        page = urllib2.urlopen(request.GET['photo_url'])
        ret_picture = page.read()
        
        if(ret_picture is not None):
            fout = open(filename, "wb")
            fout.write(ret_picture)
            fout.close()
        else:
            # TODO log error / error output
            print "ERROR: no return picture information at retrieve_photo"
    else:
        # TODO error logging
        print "ERROR: no friend selected"
    
    return render_to_response(
        "image_editor.html",
        { "user" : get_user(request),
          "editor_url" : settings.EDITOR_URL,
          "upload_url" : settings.UPLOAD_URL,
          "images_url" : settings.IMAGES_URL},
        context_instance = RequestContext(request)
    )

def friend_photo(request):
    """
    Gets a friend's photos and displays them for the user to select one from.
    """
    # friend_id = request.GET['user_id']
    # photos = request.facebook.graph.get_connections(friend_id, "photos")
    # print photos
    # print photos['data'][0]['picture']
    
    # pass the url to the template and load via ajax
    if not ("user_id" in request.GET and request.GET["user_id"]):
        return HttpResponseRedirect("/")
    
    photos_url = "/%s/photos" % (request.GET['user_id'])
    request.session['friend_id'] = request.GET['user_id']
    
    args = dict((k, v[-1]) for k, v in cgi.parse_qs(request.COOKIES['fbs_%s' % settings.FACEBOOK_API_KEY].strip('"')).items())
    #print _get_fbs(request)
    return render_to_response(
        "friend_photos.html",
        {
          "photos_url" : photos_url,
          "facebook_canvas_url" : settings.FACEBOOK_CANVAS_URL,
          "facebook_api_key" : settings.FACEBOOK_API_KEY,
          "access_token" : args['access_token'],
          "fbs" : _get_fbs(request),
          "friend_id" : request.GET['user_id'],
		},
        context_instance = RequestContext(request)
    )

def _get_fbs(request):
    fbs = None;
    if 'fs_%s' % settings.FACEBOOK_API_KEY in request.GET and request.GET['fs_%s' % settings.FACEBOOK_API_KEY]:
        fbs = request.GET['fs_%s' % settings.FACEBOOK_API_KEY]
    return fbs

def index(request):
    """
    Shows either the login button or the select a friend form.
    """
    #friends = request.facebook.graph.get_connections(request.facebook.uid, "friends")
    #print friends
    # we encoded 

    #fbs = urllib.quote(_get_fbs(request))
    fbs = _get_fbs(request)
    if fbs is not None:
        fbs = urllib.quote(fbs)
        
    return render_to_response(
        "index.html",
        { "user" : get_user(request),
          "base_url": settings.BASE_URL,
          "facebook_canvas_url": settings.FACEBOOK_CANVAS_URL,
          "facebook_api_key" : settings.FACEBOOK_API_KEY,
          "fbs" : fbs},
        context_instance = RequestContext(request)
    )
