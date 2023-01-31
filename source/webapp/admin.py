from django.contrib import admin
from webapp.models import Article, Tag


class ArticleTagInlines(admin.TabularInline):
    model = Article.tags.through


# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']
    list_display_links = ['title']
    search_fields = ['title', 'content']
    exclude = ['tags']
    readonly_fields = ['created_at', 'updated_at']
    inlines = (ArticleTagInlines,)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag)
