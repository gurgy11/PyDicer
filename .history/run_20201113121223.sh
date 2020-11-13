#!/bin/bash

echo "Enter the Flask app's name: "
read flask_app

echo "Exporting Flask app..."
export FLASK_APP=$flask_app

echo "Exporting Flask environment as development..."
export FLASK_ENV=development

echo "Setting current Flask app as $flask_app..."
FLASK_APP=$flask_app

echo "Exports done. Flask app set as $flask_app. Running Flask app..."
flask run

echo "Either the app processes ended on its own or the user stopped the process with CTRL+C."
