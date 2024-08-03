#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 0 ]; then
    echo "Usage: translate"
    exit 1
fi

# Get the current working directory
current_dir=$(pwd)

# Run the translation script with the current directory as input and output
translate-subtitles "$current_dir" "$current_dir"