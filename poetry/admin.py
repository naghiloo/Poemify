from django.contrib import admin
from poetry.models import (
    Category,
    Status,
    Poem
)


@admin.register(Category)
class FacilityAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'symbol',
        'description',
    )

@admin.register(Status)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'code',
        'description',
        'category',
    )


@admin.register(Poem)
class FacilityAdmin(admin.ModelAdmin):
    list_display = (
        'parts',
        'status',
    )



# @admin.register(Benefit)
# class BenefitAdmin(admin.ModelAdmin):
#     list_display = (
#         'id',
#         'title'
#     )


# class BenefitInline(admin.TabularInline):
#     model = CompanyBenefit
#     extra = 0


# @admin.register(Company)
# class CompanyAdmin(admin.ModelAdmin):
#     list_display = (
#         'id',
#         'name'
#     )
#     search_fields = ('name', 'website')
#     inlines = (BenefitInline,)
