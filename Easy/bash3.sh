#!/bin/bash

function check() {
echo 'Please wait...'
for x in $(find / -name persistence 2>/dev/null)
do
	if [ -f "$x" ]
	then
		s=1

	else 
		s=2
	fi

done

if [ $s==1 ]
then
	echo "File exists"

else
	echo "File does not exist"
fi
}

check 
