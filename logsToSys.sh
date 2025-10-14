#!/bin/bash


TMP_EXTRACT_DIR="./extracted_logs"



# first, check if the file passed is of type .tz
echo "Checking for valid tar"
echo "$1" # print the first arg

LOGSFILE=$1

if [[ "$LOGSFILE" == *".tz" ]] 
then
	echo "File is of type .tz"
else
	echo "File is not of type .tz, invalid argument passed"
	exit 1 # exit the script with an error
fi


# second, check if there's a virtualun directory in the logs 
echo "Untaring the logs"

#remove the last run
rm -rf $TMP_EXTRACT_DIR
#make the new dir
mkdir $TMP_EXTRACT_DIR

echo "Made new dir for extracted logs at : '$TMP_EXTRACT_DIR'"

# extract the logs
tar -xvf $1 -C $TMP_EXTRACT_DIR

# checking for an error 
tarError=$?
if [[ $tarError == "0" ]] 
then
	echo ".tz files extracted successfully to $TMP_EXTRACT_DIR"
else 
	echo "Exit ($tarError) occurred during extraction, please check and re-run"
	exit 1
fi



# third, checkign if the virtualun exists on this current system...
VIRTUALUN_DIR="/virtualun/"

if [ -d "$VIRTUALUN_DIR" ]; then
  echo "Directory '$DIRECTORY' exists."
else
  echo "Directory '$DIRECTORY' does not exist."
  # Optional: Create the directory if it doesn't exist
  # mkdir -p "$DIRECTORY"
fi

