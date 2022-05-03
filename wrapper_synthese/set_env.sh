#!/bin/bash
# script-name: set_env.sh
# Description: set_env.sh adds the path
# of synthese_ghdl.py to the PATH-variable.
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
