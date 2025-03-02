#!/bin/bash

# Get the current user
USER=$(whoami)

# Change ownership of all files and directories in the current directory
sudo chown -R "$USER":"$USER" *

echo "Ownership changed to $USER for all files in $(pwd)"

