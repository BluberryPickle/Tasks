#! /bin/bash

echo "Enter text : "
read TEXT
palindrom() {

pal=`rev <<< $1`
echo $pal
echo $1
if [ "$1" == "$pal" ]
then
	echo "Palindrome"

else
	echo "Not a palindrome"

fi

}

palindrom $TEXT