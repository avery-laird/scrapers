import os

from pysec.models import *
settings.configure()
filing = Index.objects.filter(form='10-K',cik=1057758).order_by('-date')[0]
x = filing.xbrl()
x.fields
