from django import template
register = template.Library()

@register.filter
def user_display(user):
    user_display = "ログアウト中"
    if user.is_authenticated:
        user_display = user.profile.username
    return user_display
