from rest_framework import serializers
from users.models import User


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class UserRegiserSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
    confirm_password = serializers.CharField()

    def validate_email(self, email):
        existing = User.objects.filter(email=email).first()
        if existing:
            raise serializers.ValidationError("Someone with that email address has already registered")
        return email

    def validate_password(self, password):
        if(len(password) < 8):
            raise serializers.ValidationError("Password should have at least 8 characters.")
        
        l, u, c = 0, 0, 0
        for letter in password:
            if letter == " ":
                raise serializers.ValidationError("Password shouldn't have any spaces.")
            if letter.islower(): 
                l += 1
            elif letter.isupper():
                u += 1
            elif not letter.isdigit():
                c += 1
        
        if l < 1 :
            raise serializers.ValidationError("Password should have at least 1 lowercase character.")
        if u < 1:
            raise serializers.ValidationError("Password should have at least 1 uppercase character.")
        if c < 1:
            raise serializers.ValidationError("Password should have at least 1 special character.")
        
        return password

    def validate(self, data):
        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError("Those passwords don't match.")
        return data
