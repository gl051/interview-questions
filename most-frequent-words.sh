#!/usr/bin/env bash

# -----------------------------------
# Check parameters and set variables
# -----------------------------------

if [ $# -lt 2 ]
then
    echo ''
    echo 'Description: read a text file and return the most N frequent words.'
    echo 'You can filter out a list of words by providing them as parameter'.
    echo ''
    echo 'find_most_frequent file n [''word1''|''word2'']'
    echo
    exit -1
elif [ $# == 3 ]
then
    filter=$3
    filename=$1
    quantity=$2
else
    filter=''
    filename=$1
    quantity=$2
fi

# Check if file exists
if [ ! -f $filename ];
then
   echo 'File' $filename 'does not exist'
   exit -1
fi

# -------------------------------------
# Execution
# -------------------------------------

echo 'Find the most' $quantity 'frequent words in the file' $filename

# Check file size
filesize=$(du -h "$filename" | cut -f 1)
echo 'File size ' $filesize

# For sake of explanation two temporary files are used, but you could
# eventually pipe all the commands
tmp1='__tmp1__.txt'
tmp2='__tmp2__.txt'

echo 'Start' $(date +"%r")
echo 'Start Processing file' $filename

echo 'Convert DOS (ending \r\n) to Unix format (ending \n)'
tr -d '\r' < $filename > $tmp1

echo 'Generate one line per each word'
tr -c '[:alnum:]' '\n' < $tmp1 > $tmp2

if [ $filter ]
then
    echo 'Removing blank lines and the following words:' $filter
    echo 'Filtering out ' $filter
    grep -Ev "^\s*$|$filter" < $tmp2 > $tmp1
else
    echo 'Removing blank lines'
    grep -v "^\s*$" < $tmp2 > $tmp1
fi

echo 'Sorting lines and looking for duplicates count'
cat $tmp1 | sort | uniq -c > $tmp2

echo 'Getting the first' $quantity 'most frequent words by ordering the lines on frequency count'
sort -nr < $tmp2 | head -$quantity

echo  'End' $(date +"%r") '---'

rm $tmp1
rm $tmp2
