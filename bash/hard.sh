#! /bin/bash

printf "Enter the message you want to send."
read -r msg
echo $msg
telegram-cli -W -e "msg Bi0s_Pentest_Freshers_2020 'Nama shivaya \n Name : Milind \n $msg'"	