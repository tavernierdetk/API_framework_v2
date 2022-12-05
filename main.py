import falcon
import requests
import os
from datetime import datetime as dt
import json

from Api.middleware.cors import *


import re

app = falcon.API(
    middleware=[CorsMiddleware()]
)

from Api.routes import *

print('['+ dt.now().strftime('%Y-%m-%d %H:%M:%S') +']' + ' Routes loaded ! ✅')
print('['+ dt.now().strftime('%Y-%m-%d %H:%M:%S') +']' + ' This server is ready !')
