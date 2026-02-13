from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['_id', 'name', 'email', 'password', 'team_id', 'created_at']
        extra_kwargs = {
            'password': {'write_only': True}
        }


class TeamSerializer(serializers.ModelSerializer):
    member_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Team
        fields = ['_id', 'name', 'description', 'created_at', 'member_count']
    
    def get_member_count(self, obj):
        """Calculate the number of members in this team"""
        return User.objects.filter(team_id=str(obj._id)).count()


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['_id', 'user_id', 'activity_type', 'duration', 'distance', 'calories', 'date', 'created_at']


class LeaderboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leaderboard
        fields = ['_id', 'user_id', 'user_name', 'team_id', 'team_name', 'total_points', 'total_activities', 'total_calories', 'last_updated']


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['_id', 'name', 'description', 'difficulty', 'duration', 'calories_estimate', 'activity_type', 'created_at']
