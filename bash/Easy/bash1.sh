#!/bin/bash
echo "Please enter first number"
read NUM1
echo "Please enter second number"
read NUM2
function operations {
	echo "sum : `expr $1 + $2`"
	echo "Diffrence : `expr $1 - $2`"
	echo "Product : `expr $1 \* $2`"
	echo "Division : `expr $1 + $2`"
}

operations $NUM1 $NUM2
