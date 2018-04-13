import os
import contentful
#from django.db import models

# Create your models here.

client = contentful.Client(
    os.environ.get('CTF_SPACE_ID', '1v7zodclvrzr'),
    os.environ.get('CTF_DELIVERY_KEY', 'f51a25a16c7279d7803228071218b1250c33d2fef1fb5a5e000e4160648875f6')
)
