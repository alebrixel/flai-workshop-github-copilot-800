#!/bin/bash

# OctoFit Tracker API Test Script
# This script tests all API endpoints

# Determine the base URL (Codespace or localhost)
if [ -n "$CODESPACE_NAME" ]; then
    BASE_URL="https://$CODESPACE_NAME-8000.app.github.dev"
    echo "Testing Codespace URL: $BASE_URL"
else
    BASE_URL="http://localhost:8000"
    echo "Testing localhost URL: $BASE_URL"
fi

echo "========================================"
echo "Testing OctoFit Tracker API Endpoints"
echo "========================================"

echo -e "\n1. Testing API Root:"
curl -s "$BASE_URL/" | python3 -m json.tool

echo -e "\n2. Testing Users endpoint:"
curl -s "$BASE_URL/api/users/" | python3 -m json.tool

echo -e "\n3. Testing Teams endpoint:"
curl -s "$BASE_URL/api/teams/" | python3 -m json.tool

echo -e "\n4. Testing Activities endpoint:"
curl -s "$BASE_URL/api/activities/" | python3 -m json.tool

echo -e "\n5. Testing Leaderboard endpoint:"
curl -s "$BASE_URL/api/leaderboard/" | python3 -m json.tool

echo -e "\n6. Testing Workouts endpoint:"
curl -s "$BASE_URL/api/workouts/" | python3 -m json.tool

echo -e "\n========================================"
echo "API Testing Complete"
echo "========================================"
