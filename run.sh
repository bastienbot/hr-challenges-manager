#!/bin/bash
echo "HRCM Started"
flask run --host=0.0.0.0 --port=5100 --debugger
# while :
# do
# 	sleep 1
# done