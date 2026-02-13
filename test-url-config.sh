#!/bin/bash
# Quick test to verify Codespace URL configuration

echo "================================"
echo "OctoFit Tracker URL Configuration Test"
echo "================================"

cd /workspaces/flai-workshop-github-copilot-800/octofit-tracker/backend
source venv/bin/activate

echo -e "\n1. Codespace Name:"
echo "   $CODESPACE_NAME"

echo -e "\n2. API Base URL (from urls.py):"
python -c "import os; os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings'); import django; django.setup(); from octofit_tracker.urls import API_BASE_URL; print('   ' + API_BASE_URL)"

echo -e "\n3. Allowed Hosts (from settings.py):"
python -c "import os; os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings'); import django; django.setup(); from django.conf import settings; print('   ' + str(settings.ALLOWED_HOSTS))"

echo -e "\n4. Proxy Headers Configuration:"
python -c "import os; os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings'); import django; django.setup(); from django.conf import settings; print('   USE_X_FORWARDED_HOST:', settings.USE_X_FORWARDED_HOST); print('   SECURE_PROXY_SSL_HEADER:', settings.SECURE_PROXY_SSL_HEADER)"

echo -e "\n================================"
echo "✅ Configuration Complete!"
echo "================================"
