source /cvmfs/sft.cern.ch/lcg/views/LCG_98python3/x86_64-centos7-gcc10-opt/setup.sh
source setDCDataReaderEnv.sh
g++ -DSTANDALONE -I "$ROOTSYS/include"  -I $WAVEDATA_DIR/inc -I $WAVEDATA_DIR/linkdef_inc read_datalist_OSC.C `root-config --glibs --libs --cflags`  -L$WAVEDATA_DIR/lib -lWaveData  -o read_datalist_OSC
g++ -DSTANDALONE -I "$ROOTSYS/include"  -I $WAVEDATA_DIR/inc -I $WAVEDATA_DIR/linkdef_inc compile_getWaveForm.C `root-config --glibs --libs --cflags`  -L$WAVEDATA_DIR/lib -lWaveData  -o getWaveForm
