# Django settings for cape project.
import os

ROOT_PROJECT_FOLDER = os.path.dirname(__file__)

MEDIA_ROOT = os.path.join(ROOT_PROJECT_FOLDER,'media')



DEBUG = True
#DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Aaron Racicot', 'aaronr@z-pulley.com'),
)

ACCOUNT_ACTIVATION_DAYS = 5
DEFAULT_FROM_EMAIL = 'donotreply@z-pulley.com'
EMAIL_MANAGERS = False

MANAGERS = ADMINS

AUTH_PROFILE_MODULE = 'profiles.UserProfile'

GOOGLE_ANALYTICS_CODE = ''
# this key does not need to be filled in when running locally.
GMAP_API_KEY = 'ABQIAAAAqm4SKuQITs2FoZu5Mz_ubhSAa4PBXeYnuhvAORHTrPcbaRaLShSQ_shhca1jNL9SBLkEG3k64ecDxw'
ENABLE_GMAPS = False

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'cugos',
        'USER': 'aaronr',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
        },
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Los_Angeles'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"


# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

ADMIN_MEDIA_ROOT = os.path.join(ROOT_PROJECT_FOLDER, 'admin_media')
ADMIN_MEDIA_PREFIX = '/admin_media/'
# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
#ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'vfnlvw6rlpevp)$w)8%5hgy67_aucgm9q)3coqqo-#3w$%gyxo'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'cugos_org.urls'

TEMPLATE_DIRS = (
    os.path.join(ROOT_PROJECT_FOLDER, 'templates'),
    '/usr/lib/pymodules/python2.6/django/contrib/databrowse/templates',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.gis',
    'django.contrib.flatpages',
    'django.contrib.humanize',
    'django.contrib.databrowse',
    'cugos_org.batchadmin',
    'cugos_org.registration',
    'cugos_org.profiles',
    'cugos_org.cugos_main',
    'cugos_org.voting',
    'cugos_org.modelviz',
    'cugos_org.shapes',
    'cugos_org.tagging',
    'django_extensions',
    'south'
)

# add a file next to this settings.py file called 'local_settings.py' that overrides any database settings or other 
# settings in this 'master' settings file. This allows you to make local changes to get the
# project running on your system without editing this file. When we get to the point
# that edits need to be made to this file to load more say, INSTALLED_APPS, then changes
# can be made to this 'settings.py' file and committed to the repository so everyone can see
# what additional installations they need. IE, we'll need the app called 'django-registration' soon.
try:
    from local_settings import *
except ImportError, exp:
    pass
