#!/bin/bash

# Variables
filename_excel="daily_market_price.xlsx"
source_dir="/local/data/market"
target_dir="/path/to/target"

# Check if directory exists inside the target path
if [ -d "$target_dir" ]; then
  # Copy the file from the source directory to the target directory
  cp "$source_dir/$filename_excel" "$target_dir/$filename_excel"

  # Create a log file with "File Moved Successfully" content
  echo "File Moved Successfully" > "$target_dir/log.txt"
else
  echo "Target directory does not exist."
fi
