#!/bin/bash
#./scout/scout.py &
echo ${0%SCO*nd}
cd ${0%SCO*nd}
ls
./scoutmaster.py
