#!/bin/bash
source /lustrehome/bdanzi/cmsset_default.sh
cd /lustrehome/bdanzi/TestBeam2022/analysistestbeam2022/analysis_2021/drifttubes_offline_analysis/testbeam_analysis/CMSSW_10_6_22/src/
eval `scramv1 runtime -sh`
cd /lustrehome/bdanzi/TestBeam2022/analysistestbeam2022/analysis_2021/drifttubes_offline_analysis/testbeam_analysis/
source setDCDataReaderEnv.sh
./read_data . 10 0 -1 1.5 >&  /lustrehome/bdanzi/TestBeam2022/analysistestbeam2022/analysis_2021/drifttubes_offline_analysis/testbeam_analysis/executables/log10 &
