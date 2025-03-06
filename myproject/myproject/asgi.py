"""
ASGI 配置文件，用於 myproject 項目。

它將 ASGI 可調用對象作為模塊級變量名為 ``application``。

有關此文件的更多信息，請參見
https://docs.djangoproject.com/zh-hans/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

application = get_asgi_application()
