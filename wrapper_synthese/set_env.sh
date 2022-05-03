#!/bin/bash
# script-name: set_env.sh
# description: This script checks
# if the synthese_ghdl.py
# inside the current folder
# exist and adds then the 
# path to the PATH-Environment
# Variable.
# Author: Siegfried Kienzle
# Date : 03.05.2022

CURRENT=$(pwd)
SCRIPTNAME="synthese_ghdl.py"

if [ -f "$CURRENT/$SCRIPTNAME" ]
then 
	

	if [[ "$PATH" == *"$CURRENT"* ]]
	then
		echo "$CURRENT already in PATH!"
		echo "$PATH"
	else
		export PATH=$PATH:$CURRENT
		echo "Adding of $CURRENT to PATH was successful!"
		echo "$PATH"
	fi
fi
