from django import forms
from .models import Trainee, Intake

#1 Using forms.Form
class CreateTrackForm(forms.Form):
    name = forms.CharField(label = 'Track Name', max_length=20)

#2 Using forms.ModelForm
class CreateTraineeModelform(forms.ModelForm):
    class Meta:
        fields  = '__all__'
        model   = Trainee
        
class CreateIntakeModelform(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model  = Intake
        
# class CreateTrackForm(forms.form):
#     #list of tuples [(id, value),()]
#     id = forms.ChoiceField(choices=[(user.id, user.first_name) for user in myUsers.objects.all()])
#     first_name = forms.CharField(label = 'First Name', max_length=20)
#     last_name = forms.CharField(max_length=20)
#     email = forms.EmailInput(max_length=50)
#     password = forms.PasswordInput(max_length=20)

# class CreateUserForm2(forms.ModelForm):
#     class Meta:
#         fields = '__all__'
#         model = myUsers