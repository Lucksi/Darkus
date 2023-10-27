#!/bin/bash
# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2023 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

ARCHITECTURE="$(arch)"
YELLOW=$(tput setaf 11)
RED=$(tput setaf 1)
WHITE=$(tput setaf 15)

function Banner {
	banner=$(<"Banner/Banner2.txt")
	printf "${RED}$banner"
}

function Packet-Installer {
	sudo apt-get install tor -y &> /dev/null | printf "${WHITE}\n\nINSTALLING TOR\n"
	sudo apt-get install git -y &> /dev/null | printf "${WHITE}\nINSTALLING GIT\n"
	sudo apt-get install python3 -y &> /dev/null | printf "${WHITE}\nINSTALLING PYTHON3\n"
    sudo apt-get install python3-pip -y &> /dev/null | printf "${WHITE}\nINSTALLING PIP"
    sudo pip3 install -r requirements.txt &> /dev/null | printf "${WHITE}\n\nINSTALLING-PYTHON-REQUIREMENTS..."
	printf "${YELLOW}\n\n[+]${WHITE}REQUIREMENTS INSTALLED SUCCESFULLY${YELLOW}[+]"
}

function installer {
    Packet-Installer
	sleep 1
	printf "\n\nPROGRAM INSTALLED CORRECTLY"
	printf "${YELLOW}\n\nTHANK YOU FOR HAVE INSTALLED DARKUS\n\n"
    exit 1
}

if [ $(id -u) -ne 0 ];
	then
	clear
    Banner
	printf "${RED}\n\n[!]${WHITE}THIS INSTALLER MUST BE RUN AS ROOT TRY WITH SUDO :)\n\n"
	exit 1
fi
clear
Banner
installer
