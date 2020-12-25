#! /bin/bash

printf "Enter the message you want to send."
read -r msg
$(telegram-cli -W -e "msg Bi0s_Pentest_Freshers_2020 '$msg'")