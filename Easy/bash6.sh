#! /bin/bash

echo enter a number
read NUM

function numchek {

if [ `expr $NUM % 2` == 0 ]
then
	echo even number
else
	echo odd number
fi
}

numchek