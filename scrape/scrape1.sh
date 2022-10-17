#!/bin/bash


pids=`ps -ef | grep 'scrape.py' | grep -v 'grep' | awk '{print $2}'`

echo "pids=$pids"

for pid in $pids
do
  echo "scrape.py already running on pid $pid"
  echo "killing pid $pid"
  kill -9 $pid
done

echo 'starting scrape'

nohup python3 scrape.py 2>&1 >scrape.out &

sleep 10

pids=`ps -ef | grep 'scrape.py' | grep -v 'grep' | awk '{print $2}'`
for pid in $pids
do
  echo "started scrape.py running on pid $pid"
done

exit 0