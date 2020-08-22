from functools import wraps
from time import time
from .sprite_cutter import find_sprites

def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print ('func:%r took: %2.4f sec' % \
          (f.__name__, te-ts))
        return result
    return wrap

find_sprites_t = timing(find_sprites)