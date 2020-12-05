#!/bin/bash

echo "Enter your number : "
read NUM
factorial () {
fact=1
for((i=1;i<=$NUM;i++))
{
	fact=$((fact * i))
}
echo $fact
}

factorial $NUM
