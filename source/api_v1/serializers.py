from rest_framework import serializers
from webapp.models import Issue, Project


class IssueSerializer(serializers.ModelSerializer):
    status = serializers.StringRelatedField()
    type = serializers.StringRelatedField()
    created_by = serializers.CharField(read_only=True)
    assigned_to = serializers.CharField()

    class Meta:
        model = Issue
        fields = ('id', 'summary', 'description', 'status', 'type', 'created_at', 'project', 'created_by', 'assigned_to')


class ProjectSerializer(serializers.ModelSerializer):
    issues = IssueSerializer(many=True, read_only=True)
    status = serializers.CharField(read_only=True)
    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'created_at', 'updated_at', 'status', 'issues')
