#!/bin/bash

# Load messages.sh
source ./messages.sh

file_name="$1"

# Check if file exists
if [ ! -f "$file_name" ]; then
    echo "Error: File does not exist."
    exit 1
fi

# Extract Magic Number (first 4 bytes)
magic_number=$(xxd -p -l 4 "$file_name" | sed 's/../& /g')
magic_number="${magic_number%" "}"  # remove trailing space

# Extract Class and trim spaces
class=$(readelf -h "$file_name" | awk -F: '/Class:/ {print $2}')
class="${class#"${class%%[![:space:]]*}"}"  # ltrim
class="${class%"${class##*[![:space:]]}"}"  # rtrim

# Normalize class to ELF32 or ELF64
if echo "$class" | grep -q "64"; then
    class="ELF64"
else
    class="ELF32"
fi

# Extract Byte Order and trim spaces
byte_order=$(readelf -h "$file_name" | grep 'Data:' | awk '{print $5, $6}')
byte_order="${byte_order#"${byte_order%%[![:space:]]*}"}"
byte_order="${byte_order%"${byte_order##*[![:space:]]}"}"

# Extract Entry Point Address and trim spaces
entry_point_address=$(readelf -h "$file_name" | awk -F: '/Entry point address:/ {print $2}')
entry_point_address="${entry_point_address#"${entry_point_address%%[![:space:]]*}"}"
entry_point_address="${entry_point_address%"${entry_point_address##*[![:space:]]}"}"

# Export variables for messages.sh
export file_name magic_number class byte_order entry_point_address

# Display formatted output
display_elf_header_info
