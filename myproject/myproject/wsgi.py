"""
WSGI 配置文件，用於 myproject 項目。

它將 WSGI 可調用對象作為模塊級變量名為 ``application``。

有關此文件的更多信息，請參見
https://docs.djangoproject.com/zh-hans/4.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

application = get_wsgi_application()
