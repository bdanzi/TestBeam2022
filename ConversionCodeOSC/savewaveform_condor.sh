#!/bin/bash

source /cvmfs/sft.cern.ch/lcg/views/LCG_98python3/x86_64-centos7-gcc10-opt/setup.sh

cd /lustre/home/nicola/CentOS7/TestBeam2023_OSCAnalysis/ConversionCodeOSC
source setDCDataReaderEnv.sh

filelist=`basename eventfilelist`
rootfile=`echo ${filelist} |sed "s?listfiles_??g" | sed "s?.txt?.root?g"`
rootfile=`echo run_OSC_${rootfile}`
logfile=`echo run_OSC_${filelist} |sed "s?listfiles_??g" | sed "s?.txt?.log?g"`

echo "Output files are ${rootfile} and ${logfile}"

./read_datalist_OSC eventfilelist >& ${logfile}

mv ${rootfile} rootdir/.
mv ${logfile} rootdir/.
