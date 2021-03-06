from django.contrib.auth.models import User

from rest_framework import serializers

from todo.models import Todo


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Todo
        fields = ['url', 'id', 'todo_name', 'is_completed', 'priority', 'created_date', 'owner']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    todos = serializers.HyperlinkedRelatedField(many=True, view_name='todo-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'todos']