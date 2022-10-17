#!/bin/bash
#
# scrape.sh

export PYTHONUNBUFFERED=1

pids=`ps -ef | grep 'scrape.py' | grep -v 'grep' | awk '{print $2}'`

#echo "pids=$pids"

if [ "$pids" = "" ]
then
  echo 'starting scrape'
  #nohup python3 scrape.py 2>&1 >scrape.out &
  nohup python3 -u scrape.py 2>&1 &
  
  sleep 10
  
  echo 'writing output to scrape.out'
  
  pids=`ps -ef | grep 'scrape.py' | grep -v 'grep' | awk '{print $2}'`
  
  for pid in $pids
  do
    echo "started scrape.py running on pid $pid"
  done
else
  for pid in $pids
  do
    echo "scrape.py already running on pid $pid"
    #echo "killing pid $pid"
    #kill -9 $pid
done
fi

exit 0
