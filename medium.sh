#! /bin/bash

function year () {
	y=$(date +%Y)
	
	if [ ! -d ~/Downloads/$y ]
	then
		`mkdir ~/Downloads/$y`
	fi
}

function fileSort () {

ls ~/Downloads | while read -r i
do
	if [ -f ~/Downloads/$i ]
	then
		fy=$(date +%Y)
		fmonth=$(date -r ~/Downloads/$i +%b)
		fday=$(date -r ~/Downloads/$i +%d)
		fname=${fmonth}_${fday}
		echo "fname is $fname"
		if [ -d ~/Downloads/$fname ]
		then
			`mv ~/Downloads/$i ~/Downloads/$fname/`

		else
			`mkdir ~/Downloads/$fname`
			`mv ~/Downloads/$i ~/Downloads/$fname/`
		fi

	fi
	`mv ~/Downloads/$fname ~/Downloads/$fy`

done
}

year
fileSort


#todo fix subdir issue
#add cron