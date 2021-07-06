from django.contrib import admin
from twitteruser.models import TwitterUser
from twitteruser.forms import TwitterUserCreationForm
from django.contrib.auth.admin import UserAdmin

# Register your models here.


class TwitterUserAdmin(UserAdmin):
    model = TwitterUser
    add_form = TwitterUserCreationForm

    fieldsets = (
        *UserAdmin.fieldsets, (
            'User Information', {
                'fields': (
                    'display_name',
                    'bio',
                    'following'
                )
            }
        )
    )


admin.site.register(TwitterUser, TwitterUserAdmin)