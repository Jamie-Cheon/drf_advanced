from django.contrib import admin
from cards.models import Card


def report(ModelAdmin, request, queryset):       # queryset : return checked items
    queryset.update(is_reported=True)

    # ids = [x.id for x in queryset.all()]
    # count = queryset.update(is_reported=True)
    # print('id:', ids, 'count:', count)


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    search_fields = ('name', 'context', 'owner__username')
    date_hierarchy = 'created'
    list_display = ('id', 'name', 'context', 'is_reported', '_owner')
    list_filter = ('name', 'is_reported')
    autocomplete_fields = ('owner',)
    actions = (report,)

    def _owner(self, obj):
        return f'{obj.owner.id} {obj.owner.username}'

