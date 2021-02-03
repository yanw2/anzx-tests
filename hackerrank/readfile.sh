#!/bin/bash - 
#===============================================================================
#
#          FILE: readfile.sh
# 
#         USAGE: ./readfile.sh 
# 
#   DESCRIPTION: 
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: YOUR NAME (), 
#  ORGANIZATION: 
#       CREATED: 03/02/2021 10:36
#      REVISION:  ---
#===============================================================================

set -o nounset                              # Treat unset variables as an error

counter=0
sum=0

byte_array=($(awk '{ print $NF }' hosts.txt))
for byte in "${byte_array[@]}"; do
  echo ">>> $byte"
done

#while IFS= read -r line; do
#  byte_size=$(echo $line | awk '{print $NF}')
#  if [ "$byte_size" -gt '5000' ]; then
#    ((counter++)) 
#    sum=$((sum + byte_size))
#  fi
#  done < "hosts.txt"

echo "$counter" > "bytes_hosts.txt"
echo "$sum" >> "bytes_hosts.txt"

