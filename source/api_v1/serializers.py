from django.contrib.auth.models import User
from rest_framework import serializers
from webapp.models import Issue, Project


class UserSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField()
    class Meta:
        model = User
        fields = ("username", "password", "password_confirm", "email")



    def validate_username(self, value):
        username = value
        try:
            User.objects.get(username=username)
            raise serializers.ValidationError("Такой пользователь уже есть", code='username_taken')
        except User.DoesNotExist:
            return value

    def validate_email(self,value):
        try:
            User.objects.get(email=value)
            raise serializers.ValidationError("Эта почта уже используется", code='email_taken')
        except User.DoesNotExist:
            return value

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError("Пароли должны совпадать!")
        return attrs

class IssueSerializer(serializers.ModelSerializer):
    status = serializers.StringRelatedField()
    type = serializers.StringRelatedField()

    class Meta:
        model = Issue
        fields = ('id', 'summary', 'description', 'status', 'type', 'created_at', 'project', 'created_by', 'assigned_to')


class ProjectSerializer(serializers.ModelSerializer):
    issues = IssueSerializer(many=True, read_only=True)
    status = serializers.CharField(read_only=True)
    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'created_at', 'updated_at', 'status', 'issues')
