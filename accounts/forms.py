from django.contrib.auth.forms import UserCreationForm
from accounts.models import User

class SignupForm(UserCreationForm):
   class Meta(UserCreationForm.Meta):
       model = User
       fields = ['username', 'email', 'first_name', 'last_name']