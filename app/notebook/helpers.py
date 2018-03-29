from notebook.models import *

def tags(user):
    return user.tag_set.distinct('category_id')
