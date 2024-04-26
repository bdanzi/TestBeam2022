#!/bin/bash

mkdir -p jobs

# for run in `echo 10 11 12 13  14  15  16  17  18  19  20  21  22  23  24  25  26  5 6 7 8 9`; do

# for run in `echo 15  16  17  18  19  20  21  22  23  24  25  26  5 6 8 9`; do
for run in `echo 1 2 4`; do

 echo "Processing run ${run}"

 savedir=`echo /lustre/home/nicola/CentOS7/TestBeam2023_OSCAnalysis/ConversionCodeOSC/Data_OSC_Run${run}_ROOT`
 mkdir -p ${savedir}

 source /cvmfs/sft.cern.ch/lcg/views/LCG_98python3/x86_64-centos7-gcc10-opt/setup.sh
 cd /lustre/home/nicola/CentOS7/TestBeam2023_OSCAnalysis/ConversionCodeOSC

 for file in `ls /lustre/home/nicola/CentOS7/TestBeam2023_OSCAnalysis/ConversionCodeOSC/Data_OSC_Run${run}_formatted/listfiles_Run*.txt`; do 

  eventfile=`basename $file | sed "s?.txt??g"`
 
  rm -f jobs/condor_savewaveform_${eventfile}.cfg
  rm -f jobs/savewaveform_condor_${eventfile}.sh
  cat condor_savewaveform.cfg | sed "s?savewaveform_condor.sh?savewaveform_condor_${eventfile}.sh?g" > jobs/condor_savewaveform_${eventfile}.cfg
  cat savewaveform_condor.sh | sed "s?eventfilelist?${file}?g" | sed "s?rootdir?${savedir}?g" > jobs/savewaveform_condor_${eventfile}.sh
  cd jobs;
  sleep 0.1
  condor_submit condor_savewaveform_${eventfile}.cfg
  cd ..
 done

sleep 3600
done

 # mv Data_OSC_tmp_ROOT Data_OSC_Run1_ROOT
 # hadd -f Data_OSC_Run1_ROOT_merged.root Data_OSC_Run1_ROOT/*.root

