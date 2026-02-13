from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import User, Team, Activity, Leaderboard, Workout
from datetime import date


class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            name='Test User',
            email='test@example.com',
            password='password123'
        )

    def test_user_creation(self):
        self.assertEqual(self.user.name, 'Test User')
        self.assertEqual(self.user.email, 'test@example.com')

    def test_user_str(self):
        self.assertEqual(str(self.user), 'Test User')


class TeamModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(
            name='Test Team',
            description='A test team'
        )

    def test_team_creation(self):
        self.assertEqual(self.team.name, 'Test Team')
        self.assertEqual(self.team.description, 'A test team')

    def test_team_str(self):
        self.assertEqual(str(self.team), 'Test Team')


class ActivityModelTest(TestCase):
    def setUp(self):
        self.activity = Activity.objects.create(
            user_id='123456',
            activity_type='Running',
            duration=30,
            distance=5.0,
            calories=300,
            date=date.today()
        )

    def test_activity_creation(self):
        self.assertEqual(self.activity.activity_type, 'Running')
        self.assertEqual(self.activity.duration, 30)
        self.assertEqual(self.activity.calories, 300)


class LeaderboardModelTest(TestCase):
    def setUp(self):
        self.leaderboard = Leaderboard.objects.create(
            user_id='123456',
            user_name='Test User',
            team_id='654321',
            team_name='Test Team',
            total_points=100,
            total_activities=5,
            total_calories=1500
        )

    def test_leaderboard_creation(self):
        self.assertEqual(self.leaderboard.user_name, 'Test User')
        self.assertEqual(self.leaderboard.total_points, 100)


class WorkoutModelTest(TestCase):
    def setUp(self):
        self.workout = Workout.objects.create(
            name='Morning Run',
            description='A refreshing morning run',
            difficulty='medium',
            duration=30,
            calories_estimate=300,
            activity_type='Running'
        )

    def test_workout_creation(self):
        self.assertEqual(self.workout.name, 'Morning Run')
        self.assertEqual(self.workout.difficulty, 'medium')
        self.assertEqual(str(self.workout), 'Morning Run')


class UserAPITest(APITestCase):
    def test_create_user(self):
        url = '/api/users/'
        data = {
            'name': 'API Test User',
            'email': 'apitest@example.com',
            'password': 'testpass123'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TeamAPITest(APITestCase):
    def test_create_team(self):
        url = '/api/teams/'
        data = {
            'name': 'API Test Team',
            'description': 'Team created via API'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class WorkoutAPITest(APITestCase):
    def test_create_workout(self):
        url = '/api/workouts/'
        data = {
            'name': 'Test Workout',
            'description': 'A test workout',
            'difficulty': 'easy',
            'duration': 20,
            'calories_estimate': 200,
            'activity_type': 'Yoga'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
