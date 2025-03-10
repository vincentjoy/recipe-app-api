"""Serializers for the user API view"""

from django.contrib.auth import (
    get_user_model,
    authenticate,
)
from django.utils.translation import gettext as _

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer): # same serializer is used for registering/creating a user and updating the user
    """Serializer for the user object."""

    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'name']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data): # create method will only get called after the validation of the iput data, for example min_length check in line 18
        """Create and return a user with encrypted password."""
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Update and return user."""
        password = validated_data.pop('password', None) # defaulting to none, because user may not be updating the password and hence it can be empty
        user = super().update(instance, validated_data)

        if password:
            # here we takes the retrieved password from the validated data in the above step
            # if not, in the update process, the new password will get saved as it is, in human readable form
            # so to avoid that, we use the set_password method to hash it before storing it
            user.set_password(password)
            user.save()

        return user


class AuthTokenSerializer(serializers.Serializer): # we are using a normal serializer subclassing instead of ModelSerializer (like in UserSerializer), because we are not basing this serializer on any model
    """Serializer for the user auth token."""
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False,
    )

    def validate(self, attrs): # this validate method will get called at the validation stage by the view
        """Validate and authenticate the user."""
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password,
        ) # at this step, DRF will check for existing users with the email and password and returns the user if the inputs are valid
        if not user:
            msg = _('Unable to authenticate with provided credentials.')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
