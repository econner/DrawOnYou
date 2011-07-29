# Django settings for drawonyou project.
import os, platform

# Learned this one from djangoproject.com .. awesome!
DEVELOPMENT_MODE = (platform.node() != "web149.webfaction.com") 

# setup python path for this instance
PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))

if DEVELOPMENT_MODE:
    DEBUG = True
else:
    DEBUG = False
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '%s/drawonyou' % PROJECT_ROOT, # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = '/home/dangd/webapps/user_media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = 'http://dangd.webfactional.com/user_media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = 'http://dangd.webfactional.com/admin_media/'
 
# Make this unique, and don't share it with anybody.
SECRET_KEY = 'iw6sybcur(c%z1h6@llxon$!a4(dtremks_@+c-(8t=5+tcr^a'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'drawonyou.draw.middleware.FakeSessionCookieMiddleware',
    # TODO add csrf
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'drawonyou.draw.middleware.FacebookMiddleware',
)

ROOT_URLCONF = 'drawonyou.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    'drawonyou.draw',
)

if not DEVELOPMENT_MODE:
    FACEBOOK_API_KEY = '72f573ed36507f7fc9c1e0a8f0c20974'
    FACEBOOK_SECRET_KEY = 'afe038aef0ba2c94e63bc130ce078fb0'
    FACEBOOK_CANVAS_URL = 'http://apps.facebook.com/drawonyou/'
else:
    FACEBOOK_API_KEY = 'e5e09d3e029341b92864ca3484ba33fb'
    FACEBOOK_SECRET_KEY = '82d6b9469dbf0be6457559b1d98ae8fb'
    FACEBOOK_CANVAS_URL = 'http://apps.facebook.com/drawonyou_local/'
    
FACEBOOK_EXTENDED_PERMISSIONS = 'friends_photos,user_photos,user_photo_video_tags,friends_photo_video_tags,friends_videos,user_videos'

if not DEVELOPMENT_MODE:
    BASE_URL = "http://dangd.webfactional.com"
    BASE_PATH = "/home/dangd/webapps"
else:
    BASE_URL = 'http://127.0.0.1:8000'
    BASE_PATH = "/Users/ericconner/Documents/draw"

UPLOAD_URL = "/user_media/uploads/"
FINISHED_URL = "/user_media/finished/"
IMAGES_URL = "/user_media/images/"
EDITOR_URL = "/user_media/Smiles.swf"

UPLOAD_PATH = "%s%s" % (BASE_PATH, UPLOAD_URL)
FINISHED_PATH = "%s%s" % (BASE_PATH, FINISHED_URL)

PHOTO_CAPTION = """ Created with the DrawOnYou Facebook application.
                Draw On Your friends at http://apps.facebook.com/drawonyou """
