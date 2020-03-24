import os
import contentful
#from django.db import models

# Create your models here.

client = contentful.Client(
    space_id=os.environ.get('CTF_SPACE_ID'),
    access_token=os.environ.get('CTF_DELIVERY_KEY'),
    environment=os.environ.get('CTF_ENVIRONMENT')
    )
