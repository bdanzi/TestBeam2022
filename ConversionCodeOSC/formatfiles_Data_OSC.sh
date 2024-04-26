#!/bin/bash

# for dir in `echo 10 11 12 13  14  15  16  17  18  19  20  21  22  23  24  25  26  6  8  9`; do
# for dir in `echo 10 11 12 13 14 15 16 17 19 20 21 23 24 25 26 6 8 9`; do 

for dir in `echo 1 2 4`; do

 echo "Run"$dir

 mkdir -p Data_OSC_Run${dir}_formatted; 

# for file in `ls /lustre/cms/store/user/defilip/TestBeam2023/TestBeam_2023_Disk2/run5/*.txt`; do 
# for file in `ls /lustre/cms/store/user/defilip/TestBeam2023/TestBeam_2023_Disk2/run7/C4--ev--02424.txt`; do

 for channel in `echo 1 2 3 4 5 6 7 8`; do
  # for file in `ls /lustre/cms/store/user/defilip/TestBeam2023/TestBeam_2023_Disk2/run${dir}/C${channel}*--ev--*.txt`; do
  for file in `ls /lustre/cms/store/user/defilip/TestBeam2023/TestBeam_2023_Disk1/run${dir}/C${channel}*--ev--*.txt`; do
   trigger=`cat $file | grep -e "Trigger Time"  | awk -F "," '{print $4}'`
   newfile=`basename $file | sed "s?.txt?--Trigger${trigger}_formatted.txt?g"` ;
   echo $newfile ; rm -f Data_OSC_Run${dir}_formatted/$newfile; rm -f tmp.txt;

 # cat $file | grep Hor | awk -F "," '{print $2,"0.0\n"}' > Data_OSC_Run${dir}_formatted/$newfile;
 # trigger=`cat $file | grep -e "Trigger Time"  | awk -F "," '{print $4}'`

   cat $file | grep -A 50000 Hor | grep -v Hor |awk -F "," '{print $4,$5}' > Data_OSC_Run${dir}_formatted/$newfile;

  done
 done

done

