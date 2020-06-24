from rest_framework import serializers


class CreateUserSerializer(serializers.ModelSerializer):
    token = serializers.CharField(label='登录状态token', read_only=True)
    class Meta:
        fields = ('id', 'username', 'token')