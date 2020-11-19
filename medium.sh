#! /bin/bash

month=$(date +%b)
day=$(date +%d)
folder=${month}_${day}
list="$(ls ~/Downloads)"
echo $list | while read -r i
do
	if [ -f "$i" ]
	then 
		fmonth=$(date -r "$i" +%b)
		fday=$(date -r "$i" +$d)
		fname=${fmonth}_${fday}
		if [ -d "$fname" ]
		then
			`mv "$i" ./$fname`
		else
			`mkdir ~/Downloads/$fname`
			`mv "$i" ./$fname`

	fi
done

##tofix file path ,mkdir
##toadd trigger,newyear