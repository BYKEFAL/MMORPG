from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group


class BasicSignupForm(SignupForm):

    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        common = Group.objects.get_or_create(name='common_group')[0]
        common.user_set.add(user)
        return user
