#!/bin/bash

# Define target directories
dirs=(
  "Resources/CAR_constructs/Sequences"
  "Resources/CAR_constructs/Annotations"
  "Resources/Vector_systems/Sequences"
  "Resources/Vector_systems/Annotations"
)

# Output file for hashes
output_file="file_hashes.txt"

# Clear or create the output file
> "$output_file"

# Loop through each directory and hash the files
for dir in "${dirs[@]}"; do
  if [ -d "$dir" ]; then
    find "$dir" -type f | while read -r file; do
      sha256sum "$file" >> "$output_file"
    done
  else
    echo "Directory not found: $dir" >&2
  fi
done

# Sort the output file
sort "$output_file" -o "$output_file"

echo "Hashing complete. Results saved to $output_file"

