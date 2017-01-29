from django.contrib import admin
from .models import Book
from .models import Author

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Book Details", {"fields": ["title", "author"]}),
        ("Review", {"fields": ["is_favorite", "review", "reviewed_by", "date_reviewed"]})
    ]
    
    readonly_fields = ["date_reviewed"]

    def book_authors(self, obj):
        return obj.list_authors()

    book_authors.short_description = "Author(s)"

    list_display = ["title", "book_authors", "date_reviewed", "is_favorite"]
    list_editable = ["is_favorite"]
    list_display_links = ["title", "date_reviewed"]
    list_filter = ["is_favorite"]
    search_fields = ["title", "author__name"]


admin.site.register(Author)