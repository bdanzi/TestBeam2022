#!/bin/bash

mkdir -p Data_OSC_merged_ROOT

# for run in `echo 10 11 12 13  14  15  16  17  18  19  20  21  22  23  24  25  26  5 7 8 1 2 4`; do
# for run in `echo 11 20  21  22  23  24  25  26  5 6 7 8 9 1 2 4`; do
# for run in `echo 26  5 6 7 8 9 2 4`; do
# for run in `echo 1`; do
 for run in `echo 2`; do

 echo "Processing Run${run}"

 expected=`ls Data_OSC_Run${run}_formatted/*list*.txt | wc | awk '{print $1}'`
 observed=`ls Data_OSC_Run${run}_ROOT/*.root | wc | awk '{print $1}'`

 echo "Processing ${expected} ${observed}"

 if [ ${expected} -eq ${observed} ]; then
  echo "Matched Run${run}"
  echo "Merging root file in Data_OSC_merged_ROOT/run_OSC_Run${run}.root"
  hadd -f Data_OSC_merged_ROOT/run_${run}.root Data_OSC_Run${run}_ROOT/*.root
 else
  echo "Run${run} not completed"
 fi

done
