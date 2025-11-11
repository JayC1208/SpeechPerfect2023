#!/bin/bash
#title           :gget.sh
#description     :Download Google drive file via wget for large size file(>100MB)
#author          :m2b3k3
#date            :20220224
#version         :0.1
#usage           :sh gget.sh <FILE ID> <FILE NAME>
#==============================================================================

if [ $# -ne 2 ]; then
 echo "require id and name"
 echo "exit"
 exit 1
fi

file_id=$1
file_name=$2

url="https://docs.google.com/uc?export=download&id=${file_id}"
my_wget="(wget --quiet --save-cookies /tmp/gd-cookie --keep-session-cookies --no-check-certificate '${url}' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')"
confirm_url="https://docs.google.com/uc?export=download&confirm=\$${my_wget}&id=${file_id}"
cmd="wget --load-cookies /tmp/gd-cookie \"$confirm_url\" -O $file_name"
eval $cmd
rm -rf /tmp/gd-cookie
