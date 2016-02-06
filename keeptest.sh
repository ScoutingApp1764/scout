#!/bin/bash

while [ "1" = "1" ]
do
	python scout.py
	if [ "$?" = "1" ]; then
		sleep 1
	fi
	sleep 1
done
