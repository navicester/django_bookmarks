from django.contrib import admin
from bookmarks.models import Link, Tag, Bookmark


class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'user')
    

class LinkAdmin(admin.ModelAdmin):
    pass

class TagAdmin(admin.ModelAdmin):
    pass


admin.site.register(Link, LinkAdmin)
admin.site.register(Bookmark, BookmarkAdmin)
admin.site.register(Tag, TagAdmin)


