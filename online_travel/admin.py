from django.contrib import admin

from .models import Member
from .models import Spot
from .models import Video
from .models import Livechat
from .models import Bookmark


admin.site.register(Member)
admin.site.register(Spot)
admin.site.register(Video)
admin.site.register(Livechat)
admin.site.register(Bookmark)

