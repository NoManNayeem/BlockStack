from django.contrib import admin
from core.models.profile import Profile
from core.models.post import Post
from core.models.connection import Connection
from core.models.like import Like
from core.models.comment import Comment
from core.models.share import Share
from core.models.search import SearchHistory




import csv
from django.http import HttpResponse

def export_to_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="export.csv"'

    writer = csv.writer(response)
    writer.writerow([field.name for field in modeladmin.model._meta.fields])

    for obj in queryset:
        writer.writerow([getattr(obj, field.name) for field in modeladmin.model._meta.fields])

    return response

export_to_csv.short_description = 'Download as CSV'



@admin.register(Profile)
class DeviceInfoAdmin(admin.ModelAdmin):
    list_display = ("user","bio",)
    list_filter = ("user","bio",)
    actions = [export_to_csv]



admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Share)
admin.site.register(SearchHistory)
admin.site.register(Comment)
admin.site.register(Connection)
