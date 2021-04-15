from django.contrib import admin
from photo.models import Album, Photo

class PhotoInline(admin.StackedInline): # 1:N 관계 성립, 앨범 객체를 보여줄 때 객체에 연결된 사진 객체들을 같이
    model = Photo                       # 보여줄 수 있는데, 같이 보여주는 형식은 StakedInline(세로로 나열)과 TabularInline(가로로 나열) 두 가지가 있다.
    extra = 2


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    inlines = (PhotoInline,)
    list_display = ('id', 'name', 'description')

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'upload_dt')
