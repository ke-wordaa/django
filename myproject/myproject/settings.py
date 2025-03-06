from django.utils.translation import gettext_lazy as _
import pymysql
pymysql.install_as_MySQLdb()
from pathlib import Path
# 在項目內部構建路徑，如： BASE_DIR / 'subdir'。
BASE_DIR = Path(__file__).resolve().parent.parent


# 快速啟動開發設置 - 不適用於生產環境
# 請參見 https://docs.djangoproject.com/zh-hans/4.2/howto/deployment/checklist/

# 安全警告：請保密生產環境中使用的密鑰！
SECRET_KEY = 'django-insecure-i#&04+m)mc2+l%^96q=uftj9!c8$^elv^y@!0ax^oz_i522@h#'

# 安全警告：不要在生產環境中打開調試模式！
DEBUG = True

ALLOWED_HOSTS = ['*']



# 應用程序定義

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'web_page',
    # 'myapp',
    'accounts',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'myproject.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # 建立 templates 目錄
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'myproject.wsgi.application'


# 數據庫
# https://docs.djangoproject.com/zh-hans/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_db',
        'USER': 'jj',
        'PASSWORD': 'P@ssword888',
        'HOST': '192.168.118.128',
        'PORT': '3306',
    }
}


# 密碼驗證
# https://docs.djangoproject.com/zh-hans/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# 國際化
# https://docs.djangoproject.com/zh-hans/4.2/topics/i18n/

LANGUAGE_CODE = 'zh-Hant' # default=en-us

TIME_ZONE = 'Asia/Taipei'

USE_I18N = True

USE_TZ = True
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'


# 靜態文件（CSS、JavaScript、圖片）
# https://docs.djangoproject.com/zh-hans/4.2/howto/static-files/

STATIC_URL = 'static/'

# 默認主鍵字段類型
# https://docs.djangoproject.com/zh-hans/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
