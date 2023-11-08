#!/bin/bash
cd /eos/user/b/bdanzi/TestBeam2023/testbeam_analysis/CMSSW_10_6_22/src/
eval `scramv1 runtime -sh`
cd /eos/user/b/bdanzi/TestBeam2023/testbeam_analysis/
source setDCDataReaderEnv.sh
./read_data .  7 0 -1 1.0 9.000 2.000 1.000 1.500 25.0 1024 0.250 >&  /eos/user/b/bdanzi/TestBeam2023/testbeam_analysis/executables/log_N1_9.000_N2_2.000_N3_1.000_N4_1.500_cut_scale_0.250_sampling_1.0_7 &
