#!/bin/bash

# Function to print strings from all files in a directory
print_strings() {
  local dir="$1"
  
  # Find all files and run the strings command on them
  find "$dir" -type f -exec strings {} \;
}

# Check if a directory argument is provided
if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <directory>"
  exit 1
fi

# Call the function with the specified directory
print_strings "$1"
