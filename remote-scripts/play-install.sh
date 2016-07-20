#!/bin/bash


# Use Example
# sh play-install.sh <zip-file> <app-name> <config-resource> <additional-config>

SCREEN_LOG="screenlog.0"

ZIP_FILE="$1"
if [[ -z "$ZIP_FILE" ]]; then
  echo 'Error: Missing Zip File Argument'
fi

APP_NAME="$2"
if [[ -z "$APP_NAME" ]]; then
  echo 'Error: Missing App Name Argument'
fi

CONFIG_RESOURCE="$3"
if [[ -z "$CONFIG_RESOURCE" ]]; then
  echo 'Error: Missing Config Resource Argument'
fi

echo "Config Resource: $CONFIG_RESOURCE"

# Optional Additional Arguements
ADDITIONAL_CONFIG="${@:4}"

echo "Aditional Config: $ADDITIONAL_CONFIG"



# Remove ZIP (.tgz) extension
BASENAME=${ZIP_FILE:0:-4}

# Unzip Server
echo 'Unzipping Server...'
tar -xzf $ZIP_FILE

# Kill currently running server
echo 'Shutting Down Previous Play Servers...'
killall screen
sudo kill -9 $(sudo lsof -ti tcp:80)

# Remove current RUNNING_PID
find . -name "RUNNING_PID" -delete

# Reset screenlog
rm $SCREEN_LOG


echo 'Starting Server...'
screen -dmSL agrity-server \
    sudo ./$BASENAME/bin/$APP_NAME $CONFIG_RESOURCE $ADDITIONAL_CONFIG


echo 'Runnning Screens...'
screen -ls

# Print Screenlog
echo 'Printing Screenlog...'
tail -f $SCREEN_LOG
