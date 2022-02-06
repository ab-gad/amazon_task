from rest_framework import serializers
from amazon.models import Intake, Trainee

class IntakeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Intake
        fields = ['id', 'number']

# class TraineeSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Trainee
#         fields = ('__all__')
        # fields = ['id', 'first_name']

# Notice >> using ModelSerializer instead of HyperlinkedModelSerializer give me the abiliy to use '__all__'
class TraineeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainee
        fields = ('__all__')