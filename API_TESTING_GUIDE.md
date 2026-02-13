# OctoFit Tracker API Testing Guide

## Your Codespace URL
```
https://symmetrical-invention-vr7j54r95gvc6qxg-8000.app.github.dev
```

## Starting the Django Server

### Option 1: Using VS Code (Recommended)
1. Press `F5` or click **Run and Debug** icon (Ctrl+Shift+D)
2. Select **"Launch Django Backend"** from the dropdown
3. Click the green play button

### Option 2: Using Terminal
```bash
cd /workspaces/flai-workshop-github-copilot-800/octofit-tracker/backend
source venv/bin/activate
python manage.py runserver 0.0.0.0:8000
```

## Testing API Endpoints

### Quick Test All Endpoints
Run the automated test script:
```bash
./test-api.sh
```

### Manual Testing with curl

#### 1. API Root (shows all available endpoints)
```bash
curl https://symmetrical-invention-vr7j54r95gvc6qxg-8000.app.github.dev/
```

#### 2. Users Endpoint
```bash
curl https://symmetrical-invention-vr7j54r95gvc6qxg-8000.app.github.dev/api/users/
```

#### 3. Teams Endpoint
```bash
curl https://symmetrical-invention-vr7j54r95gvc6qxg-8000.app.github.dev/api/teams/
```

#### 4. Activities Endpoint
```bash
curl https://symmetrical-invention-vr7j54r95gvc6qxg-8000.app.github.dev/api/activities/
```

#### 5. Leaderboard Endpoint
```bash
curl https://symmetrical-invention-vr7j54r95gvc6qxg-8000.app.github.dev/api/leaderboard/
```

#### 6. Workouts Endpoint
```bash
curl https://symmetrical-invention-vr7j54r95gvc6qxg-8000.app.github.dev/api/workouts/
```

## Configuration Summary

### Files Updated
- **settings.py**: Updated `ALLOWED_HOSTS` to include Codespace URL and localhost
  ```python
  CODESPACE_NAME = os.getenv('CODESPACE_NAME')
  ALLOWED_HOSTS = ['localhost', '127.0.0.1']
  if CODESPACE_NAME:
      ALLOWED_HOSTS.append(f'{CODESPACE_NAME}-8000.app.github.dev')
  ```

### Current ALLOWED_HOSTS
```
['localhost', '127.0.0.1', 'symmetrical-invention-vr7j54r95gvc6qxg-8000.app.github.dev']
```

## Notes
- The `$CODESPACE_NAME` environment variable is automatically used (not hardcoded)
- MongoDB is already running on port 27017
- Port 8000 is configured as public in the Codespace
- All API endpoints use the `/api/` prefix
- Django REST Framework automatically handles request host resolution
