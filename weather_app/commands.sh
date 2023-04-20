#!/bin/bash
if ping -c 3 $DATABASE_IP; then
    echo "$DATABASE_IP reachable"
    python3 weather_app.py
else
    echo "Cannot reach $DATABASE_IP , please check your connectivity "
fi