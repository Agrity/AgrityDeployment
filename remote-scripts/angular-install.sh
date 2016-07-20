#!/bin/bash


# Use Example
# sh angular-install.sh <zip-file> <dist-folder>

SCREEN_LOG="screenlog.0"

ZIP_FILE="$1"
if [[ -z "$ZIP_FILE" ]]; then
  echo 'Error: Missing Zip File Argument'
  exit
fi

DIST_FOLDER="$2"
if [[ -z "$DIST_FOLDER" ]]; then
  echo 'Error: Missing Dist Folder Argument'
  exit
fi

# Unzip Server
echo 'Unzipping Server...'
tar -xzf $ZIP_FILE

# Kill currently running server
echo 'Shutting Down Previous Play Servers...'
killall screen
sudo kill -9 $(sudo lsof -ti tcp:80)

# Reset screenlog
rm $SCREEN_LOG

echo 'Starting Server...'
screen -dmSL agrity-app \
    sudo env "PATH=$PATH" serve $DIST_FOLDER -p 80

echo 'Runnning Screens...'
screen -ls

# Print Screenlog
echo 'Printing Screenlog...'
tail -f $SCREEN_LOG
