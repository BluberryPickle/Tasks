#! /bin/bash

function fileSort () {

ls ~/Downloads | while read -r i
do
	if [ -f ~/Downloads/$i ]
	then
		fy=$(date -r ~/Downloads/$i +%Y)
		fmonth=$(date -r ~/Downloads/$i +%b)
		fday=$(date -r ~/Downloads/$i +%d)
		fname=${fmonth}_${fday}
		if [ ! -d ~/Downloads/$fy ]
		then
			`mkdir ~/Downloads/$fy`
		fi

		if [ -d ~/Downloads/$fy/$fname ]
		then
			`mv ~/Downloads/$i ~/Downloads/$fy/$fname/`

		else
			`mkdir ~/Downloads/$fy/$fname`
			`mv ~/Downloads/$i ~/Downloads/$fy/$fname/`
		fi

	fi

done
}

fileSort