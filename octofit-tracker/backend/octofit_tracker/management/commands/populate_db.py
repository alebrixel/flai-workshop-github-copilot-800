from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import date, timedelta
import random


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting database population...'))

        # Clear existing data
        self.stdout.write('Clearing existing data...')
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        self.stdout.write('Creating teams...')
        team_marvel = Team.objects.create(
            name='Team Marvel',
            description='Earth\'s Mightiest Heroes - Dedicated to protecting the world through strength and teamwork'
        )
        team_dc = Team.objects.create(
            name='Team DC',
            description='Justice League - United for truth, justice, and ultimate fitness'
        )

        # Create Users (Superheroes)
        self.stdout.write('Creating users...')
        marvel_heroes = [
            {'name': 'Tony Stark', 'email': 'ironman@marvel.com', 'password': 'arc_reactor_3000'},
            {'name': 'Steve Rogers', 'email': 'captainamerica@marvel.com', 'password': 'vibranium_shield'},
            {'name': 'Thor Odinson', 'email': 'thor@asgard.com', 'password': 'mjolnir_worthy'},
            {'name': 'Natasha Romanoff', 'email': 'blackwidow@marvel.com', 'password': 'red_room_elite'},
            {'name': 'Bruce Banner', 'email': 'hulk@marvel.com', 'password': 'gamma_smash'},
        ]

        dc_heroes = [
            {'name': 'Clark Kent', 'email': 'superman@dc.com', 'password': 'krypton_last_son'},
            {'name': 'Bruce Wayne', 'email': 'batman@dc.com', 'password': 'gotham_knight'},
            {'name': 'Diana Prince', 'email': 'wonderwoman@dc.com', 'password': 'amazonian_warrior'},
            {'name': 'Barry Allen', 'email': 'flash@dc.com', 'password': 'speed_force'},
            {'name': 'Arthur Curry', 'email': 'aquaman@dc.com', 'password': 'atlantis_king'},
        ]

        marvel_users = []
        for hero in marvel_heroes:
            user = User.objects.create(
                name=hero['name'],
                email=hero['email'],
                password=hero['password'],
                team_id=str(team_marvel._id)
            )
            marvel_users.append(user)

        dc_users = []
        for hero in dc_heroes:
            user = User.objects.create(
                name=hero['name'],
                email=hero['email'],
                password=hero['password'],
                team_id=str(team_dc._id)
            )
            dc_users.append(user)

        all_users = marvel_users + dc_users

        # Create Activities
        self.stdout.write('Creating activities...')
        activity_types = ['Running', 'Swimming', 'Cycling', 'Strength Training', 'Yoga', 'Boxing', 'Jump Rope']
        
        for user in all_users:
            # Each user gets 5-10 activities
            num_activities = random.randint(5, 10)
            for i in range(num_activities):
                activity_type = random.choice(activity_types)
                duration = random.randint(20, 120)  # 20-120 minutes
                distance = round(random.uniform(2, 25), 2) if activity_type in ['Running', 'Swimming', 'Cycling'] else None
                calories = duration * random.randint(5, 12)  # Approximate calories per minute
                activity_date = date.today() - timedelta(days=random.randint(0, 30))
                
                Activity.objects.create(
                    user_id=str(user._id),
                    activity_type=activity_type,
                    duration=duration,
                    distance=distance,
                    calories=calories,
                    date=activity_date
                )

        # Create Leaderboard entries
        self.stdout.write('Creating leaderboard entries...')
        for user in all_users:
            user_activities = Activity.objects.filter(user_id=str(user._id))
            total_activities = user_activities.count()
            total_calories = sum(activity.calories for activity in user_activities)
            total_points = total_calories + (total_activities * 50)  # 50 points per activity + calories
            
            team_name = 'Team Marvel' if user.team_id == str(team_marvel._id) else 'Team DC'
            
            Leaderboard.objects.create(
                user_id=str(user._id),
                user_name=user.name,
                team_id=user.team_id,
                team_name=team_name,
                total_points=total_points,
                total_activities=total_activities,
                total_calories=total_calories
            )

        # Create Workouts
        self.stdout.write('Creating workouts...')
        workouts_data = [
            {
                'name': 'Super Soldier Training',
                'description': 'Captain America\'s legendary workout routine for peak human performance',
                'difficulty': 'hard',
                'duration': 60,
                'calories_estimate': 600,
                'activity_type': 'Strength Training'
            },
            {
                'name': 'Asgardian Warrior Circuit',
                'description': 'Thor\'s intense full-body circuit worthy of a god',
                'difficulty': 'hard',
                'duration': 45,
                'calories_estimate': 550,
                'activity_type': 'Strength Training'
            },
            {
                'name': 'Speed Force Sprint',
                'description': 'Flash-inspired high-intensity interval running',
                'difficulty': 'medium',
                'duration': 30,
                'calories_estimate': 400,
                'activity_type': 'Running'
            },
            {
                'name': 'Bat Cave HIIT',
                'description': 'Batman\'s stealth and agility training session',
                'difficulty': 'hard',
                'duration': 50,
                'calories_estimate': 520,
                'activity_type': 'Boxing'
            },
            {
                'name': 'Amazonian Yoga Flow',
                'description': 'Wonder Woman\'s flexibility and balance routine',
                'difficulty': 'medium',
                'duration': 40,
                'calories_estimate': 250,
                'activity_type': 'Yoga'
            },
            {
                'name': 'Atlantean Swim',
                'description': 'Aquaman\'s underwater endurance training',
                'difficulty': 'medium',
                'duration': 35,
                'calories_estimate': 380,
                'activity_type': 'Swimming'
            },
            {
                'name': 'Arc Reactor Core',
                'description': 'Iron Man\'s tech-enhanced core strengthening workout',
                'difficulty': 'easy',
                'duration': 25,
                'calories_estimate': 200,
                'activity_type': 'Strength Training'
            },
            {
                'name': 'Widow\'s Combat Cardio',
                'description': 'Black Widow\'s martial arts cardio session',
                'difficulty': 'medium',
                'duration': 40,
                'calories_estimate': 450,
                'activity_type': 'Boxing'
            },
            {
                'name': 'Kryptonian Strength',
                'description': 'Superman\'s ultimate power training',
                'difficulty': 'hard',
                'duration': 55,
                'calories_estimate': 580,
                'activity_type': 'Strength Training'
            },
            {
                'name': 'Hulk Smash Circuit',
                'description': 'Hulk-inspired explosive power training',
                'difficulty': 'hard',
                'duration': 30,
                'calories_estimate': 500,
                'activity_type': 'Strength Training'
            },
        ]

        for workout_data in workouts_data:
            Workout.objects.create(**workout_data)

        # Create unique index on email field using MongoDB
        from pymongo import MongoClient
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']
        db.users.create_index('email', unique=True)
        client.close()

        self.stdout.write(self.style.SUCCESS(f'Successfully populated database with:'))
        self.stdout.write(f'  - {Team.objects.count()} teams')
        self.stdout.write(f'  - {User.objects.count()} users')
        self.stdout.write(f'  - {Activity.objects.count()} activities')
        self.stdout.write(f'  - {Leaderboard.objects.count()} leaderboard entries')
        self.stdout.write(f'  - {Workout.objects.count()} workouts')
        self.stdout.write(self.style.SUCCESS('Database population complete!'))
