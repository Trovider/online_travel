from django.contrib import admin

from .models import Member
from .models import Spot
from .models import Video
from .models import Livechat
from .models import Bookmark, Photo


admin.site.register(Member)

admin.site.register(Video)
admin.site.register(Livechat)
admin.site.register(Bookmark)
class PhotoInline(admin.TabularInline):
    model = Photo
class SpotAdmin(admin.ModelAdmin):
    inlines = [PhotoInline, ]
admin.site.register(Spot, SpotAdmin)
