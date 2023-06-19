#create sh script for histos root file creation
#pathf="/lustrehome/bdanzi/TestBeam2022/analysistestbeam2022/analysis_2021/drifttubes_offline_analysis/testbeam_analysis"
#path="/lustrehome/bdanzi/TestBeam2022/analysistestbeam2022/analysis_2021/drifttubes_offline_analysis/testbeam_analysis/executables"
path="/lustrehome/bdanzi/TestBeam2023/testbeam_analysis/executables"
pathf="/lustrehome/bdanzi/TestBeam2023/testbeam_analysis"
#############################################################################################
############### Gas Gain Study without efficiency or Ratio plots ############################
#runinputsevents_2_gsample=("40" "41" "42" "43" "54" "55" "56" "65" "69" "70" "71") # Study July 2022 Test Beam Scan in HV all gas mixtures and HV
runinputsevents_2_gsample=("43")
#####################################################################################################################################
############################## HV Study with all Gas Mixtures at 180 GeV ############################################################
#####################################################################################################################################
#runinputsevents_1_gsample=("53") # Study July 2022  Nom 90/10 Gas Mixture
#runinputsevents_2_gsample=("40" "64" "54" "41" "42" "69" "55" "43" "56") # Study July 2022 Test Beam Scan in HV (80/20 and 85/15 and 90/10): Nom -10V, Nom, Nom +10V, Nom +20V 80/20 Gas Mixture and 85/15 ########################
#runinputsevents_1p5_gsample=("71" "70")
####################################
######## Single Gas Mixtures #######
####################################
#runinputsevents_1_gsample=("53") # Study July 2022  Nom 90/10 Gas Mixture 45°
#runinputsevents_1p5_gsample=("71" "70")
#runinputsevents_2_gsample=("54" "55" "56") # Study July 2022  Nom -10V, Nom +10V, Nom +20V Gas Mixture 90/10
#runinputsevents_2_gsample=("40" "41" "42" "43") # Study July 2022 Test Beam Scan in HV : Nom -10V, Nom, Nom +10V, Nom +20V 80/20 Gas Mixture
#runinputsevents_2_gsample=("64" "71" "69" "70") # Study July 2022 Test Beam Scan in HV: Nom -10V, Nom, Nom +10V, Nom +20V Gas Mixture 85/15 
#####################################################################################################################################

#####################################################################################################################################
############################## Angle Study with all Gas Mixtures at 180 GeV #########################################################
#####################################################################################################################################
#runinputsevents_1p5_gsample=("71") #85/15 45
#runinputsevents_2_gsample=("62" "11" "44" "51" "45" "10" "41" "47" "46")
####################################
######## Single Gas Mixtures #######
####################################
#runinputsevents_2_gsample=("62") #85/15 0 
# runinputsevents_2_gsample=("11" "51" "10" "47") #90/10 0 30 45 60
# runinputsevents_2_gsample=("44" "45" "41" "46") #80/20 0 30 45 60
#####################################################################################################################################

#####################################################################################################################################
############################## Sampling Study with all Gas Mixtures at 180 GeV 45 Angle #########################################################
#####################################################################################################################################
#runinputsevents_1_gsample=("53") #90/10
#runinputsevents_1p5_gsample=("9") #90/10 
#runinputsevents_2_gsample=("10") #90/10
#####################################################################################################################################

#####################################################################################################################################
############################################################## Random Study for Franco ######################################################################
#####################################################################################################################################
# runinputsevents_2_gsample=("41" "44" "62")
# runinputsevents_1_gsample=("52")
#runinputsevents_1_gsample=("58")
#####################################################################################################################################

#runinputsevents_2_gsample=("10") #Study July 2022 Test Beam Runs Scan in Sampling rate: 1.5 2.0 180 GeV
#runinputsevents_1p5_gsample=("9") #Study July 2022 Test Beam Runs Scan in Sampling rate: 1.5 2.0 180 GeV
#runinputsevents_2_gsample=("44" "45" "41" "46") # Study July 2022 Test Beam Scan in Angle 0° 30° 45° 60° 180 GeV Gas Mixture 80/20
#runinputsevents_2_gsample=("41" "63" "10") # Study July 2022 Test Beam Scan in Gas Mixtures 80/20 85/15 90/10 180 GeV
#runinputsevents_1p2_gsample=("99" "98" "96" "94" "91") # Nov 2021 TestBeam Scan in Angle 1.2 Gsample 90/10 165 GeV 0° 15° 30° 45° 60°
#runinputsevents_1p2_gsample=("117" "127") # Nov 2021 TestBeam Scan in Angle 1.2 Gsample 80/20 165 GeV 0° 15° 30° 45° 60° 
############################################################################################################################################################
dim=1024
binTimeInterval=25.0
rm plots_oldTestBeam.txt
# Original cuts for Nov 2021 cut_scale 0.26 N1 10.0 N_2 1.0 N_3 0.2 N_4 0.2 gsample 3
# Last cuts for July 2022 cut scale  0.2 N_1 10.0 N_2 1.2 N_3 0.0 N_4 0.0 gsample 0 2
for cut_scale in 0.250 #0.22 0.22 0.20 # 0.26 0.22 0.24 0.20 0.26 0.28 #0.1 0.4 0.5 #con N_2 1.0 # second derivative in the peak candidate
do
    for N_1 in 9.000 #6 # Amplitude cut
    do
        for N_2 in 2.000 #1.1 1.5 0.8 0.5 #1.0 amplitude on the average before and after the peak candidate 1.100
        do
            for N_3 in 1.000 #0.050 0.1 0.4 0.5 #con N_2 1.0 # first derivative in the peak candidate
            do
                for N_4 in 1.500 #0.025 0.1 0.4 0.5 #con N_2 1.0 # second derivative in the peak candidate
                do
                #for gsample in 1 2 0 # Scan HV
                #for gsample in 1 0 2 # Scan Sampling Rate
                #for gsample in 0 2 # Scan Angle
                for gsample in 2 # Run 43
                    do
                        runinputs=()
                        if [ $gsample -eq 0 ]
                        then
                    	sampling=1.5
                            runinputs=("${runinputsevents_1p5_gsample[@]}")
                        fi
                        if [ $gsample -eq 1 ]
                        then
                    	sampling=1.0
                            runinputs=("${runinputsevents_1_gsample[@]}")
                        fi

                        if [ $gsample -eq 2 ]
                        then
                    	sampling=2.0
                            runinputs=("${runinputsevents_2_gsample[@]}")
                        fi

                        if [ $gsample -eq 3 ]
                        then
                    	sampling=1.2
                            runinputs=("${runinputsevents_1p2_gsample[@]}")
                        fi

                        for i in ${runinputs[@]}
                        do

                    	rm ${path}/log_N1_${N_1}_N2_${N_2}_N3_${N_3}_N4_${N_4}_cut_scale_${cut_scale}_sampling_${sampling}_$i
                        #rm ${path}/test_N1_${N_1}_N2_${N_2}_N3_${N_3}_N4_${N_4}_cut_scale_${cut_scale}_sampling_${sampling}_$i.cfg 
                        rm ${path}/test_conversion_N1_${N_1}_N2_${N_2}_N3_${N_3}_N4_${N_4}_cut_scale_${cut_scale}_sampling_${sampling}_$i.cfg
                        rm ${path}/submit_executable_conversion_N1_${N_1}_N2_${N_2}_N3_${N_3}_N4_${N_4}_cut_scale_${cut_scale}_sampling_${sampling}_$i.sh
                        rm ${path}/submitted_recas_conversion_N1_${N_1}_N2_${N_2}_N3_${N_3}_N4_${N_4}_cut_scale_${cut_scale}_sampling_${sampling}_$i.log
                        rm ${path}/submitted_recas_conversion_N1_${N_1}_N2_${N_2}_N3_${N_3}_N4_${N_4}_cut_scale_${cut_scale}_sampling_${sampling}_$i.error
                        rm ${path}/submitted_recas_conversion_N1_${N_1}_N2_${N_2}_N3_${N_3}_N4_${N_4}_cut_scale_${cut_scale}_sampling_${sampling}_$i.out
                        echo '#!/bin/bash' >> ${path}/submit_executable_conversion_N1_${N_1}_N2_${N_2}_N3_${N_3}_N4_${N_4}_cut_scale_${cut_scale}_sampling_${sampling}_$i.sh
                        echo "source /lustrehome/bdanzi/cmsset_default.sh" >> ${path}/submit_executable_conversion_N1_${N_1}_N2_${N_2}_N3_${N_3}_N4_${N_4}_cut_scale_${cut_scale}_sampling_${sampling}_$i.sh
                        echo "cd ${pathf}/CMSSW_10_6_22/src/" >> ${path}/submit_executable_conversion_N1_${N_1}_N2_${N_2}_N3_${N_3}_N4_${N_4}_cut_scale_${cut_scale}_sampling_${sampling}_$i.sh
                        echo 'eval `scramv1 runtime -sh`' >> ${path}/submit_executable_conversion_N1_${N_1}_N2_${N_2}_N3_${N_3}_N4_${N_4}_cut_scale_${cut_scale}_sampling_${sampling}_$i.sh
                        echo "cd ${pathf}/" >> ${path}/submit_executable_conversion_N1_${N_1}_N2_${N_2}_N3_${N_3}_N4_${N_4}_cut_scale_${cut_scale}_sampling_${sampling}_$i.sh
                        echo "source setDCDataReaderEnv.sh" >> ${path}/submit_executable_conversion_N1_${N_1}_N2_${N_2}_N3_${N_3}_N4_${N_4}_cut_scale_${cut_scale}_sampling_${sampling}_$i.sh
                    	#echo "./read_data . $i 0 -1 $sampling $N_1 $N_2 $N_3 $N_4 $binTimeInterval $dim $cut_scale >&  ${path}/log_N1_${N_1}_N2_${N_2}_N3_${N_3}_N4_${N_4}_cut_scale_${cut_scale}_sampling_${sampling}_$i &" >> ${path}/submit_executable_conversion_N1_${N_1}_N2_${N_2}_N3_${N_3}_N4_${N_4}_cut_scale_${cut_scale}_sampling_${sampling}_$i.sh
                        echo "./read_data /lustre/cms/store/user/bdanzi/TestBeam20212022Analysis $i 0 -1 $sampling $N_1 $N_2 $N_3 $N_4 $binTimeInterval $dim $cut_scale >&  ${path}/log_N1_${N_1}_N2_${N_2}_N3_${N_3}_N4_${N_4}_cut_scale_${cut_scale}_sampling_${sampling}_$i &" >> ${path}/submit_executable_conversion_N1_${N_1}_N2_${N_2}_N3_${N_3}_N4_${N_4}_cut_scale_${cut_scale}_sampling_${sampling}_$i.sh
                        #echo "./read_data . $i 0 -1 $sampling $N_1 $N_2 $N_3 $N_4 $binTimeInterval $dim $cut_scale >&  ${path}/log_N1_${N_1}_N2_${N_2}_N3_${N_3}_N4_${N_4}_cut_scale_${cut_scale}_sampling_${sampling}_$i &" >> ${path}/submit_executable_conversion_N1_${N_1}_N2_${N_2}_N3_${N_3}_N4_${N_4}_cut_scale_${cut_scale}_sampling_${sampling}_$i.sh
                        chmod +x ${path}/submit_executable_conversion_N1_${N_1}_N2_${N_2}_N3_${N_3}_N4_${N_4}_cut_scale_${cut_scale}_sampling_${sampling}_$i.sh
                        echo "histosTB_run_${i}_N1_${N_1}_N2_${N_2}_N3_${N_3}_N4_${N_4}_cut_scale_${cut_scale}_sampling_${sampling}.root ${N_1} ${N_2} ${N_3} ${N_4} ${cut_scale} ${sampling} histosTB_run_${i}.root 16 100000" >> ${pathf}/plots_oldTestBeam.txt

                        #creates the cfg file to call the sh
                        echo "universe = vanilla" > ${path}/test_conversion_N1_${N_1}_N2_${N_2}_N3_${N_3}_N4_${N_4}_cut_scale_${cut_scale}_sampling_${sampling}_$i.cfg
                        echo "Executable = ${path}/submit_executable_conversion_N1_${N_1}_N2_${N_2}_N3_${N_3}_N4_${N_4}_cut_scale_${cut_scale}_sampling_${sampling}_$i.sh" >> ${path}/test_conversion_N1_${N_1}_N2_${N_2}_N3_${N_3}_N4_${N_4}_cut_scale_${cut_scale}_sampling_${sampling}_$i.cfg   
                        echo "RequestMemory = 500000" >> ${path}/test_conversion_N1_${N_1}_N2_${N_2}_N3_${N_3}_N4_${N_4}_cut_scale_${cut_scale}_sampling_${sampling}_$i.cfg
                    	#echo "Should_Transfer_Files = YES" >> ${path}/test_conversion_N1_${N_1}_N2_${N_2}_N3_${N_3}_N4_${N_4}_cut_scale_${cut_scale}_sampling_${sampling}_$i.cfg
                        #echo "Transfer_Input_Files = /lustre/cms/store/user/bdanzi/TestBeam20212022Analysis/run_$i.root" >> ${path}/test_conversion_N1_${N_1}_N2_${N_2}_N3_${N_3}_N4_${N_4}_cut_scale_${cut_scale}_sampling_${sampling}_$i.cfg
                        #echo "RequestDisk = 5000" >> ${path}/test_conversion_N1_${N_1}_N2_${N_2}_N3_${N_3}_N4_${N_4}_cut_scale_${cut_scale}_sampling_${sampling}_$i.cfg
                        echo "WhenToTransferOutput = ON_EXIT" >> ${path}/test_conversion_N1_${N_1}_N2_${N_2}_N3_${N_3}_N4_${N_4}_cut_scale_${cut_scale}_sampling_${sampling}_$i.cfg  
                        echo 'Requirements = TARGET.OpSys == "LINUX" && (TARGET.Arch != "DUMMY" )' >> ${path}/test_conversion_N1_${N_1}_N2_${N_2}_N3_${N_3}_N4_${N_4}_cut_scale_${cut_scale}_sampling_${sampling}_$i.cfg  
                        echo "Log = ${path}/submitted_recas_conversion_N1_${N_1}_N2_${N_2}_N3_${N_3}_N4_${N_4}_cut_scale_${cut_scale}_sampling_${sampling}_$i.log" >> ${path}/test_conversion_N1_${N_1}_N2_${N_2}_N3_${N_3}_N4_${N_4}_cut_scale_${cut_scale}_sampling_${sampling}_$i.cfg  
                        echo "Output = ${path}/submitted_recas_conversion_N1_${N_1}_N2_${N_2}_N3_${N_3}_N4_${N_4}_cut_scale_${cut_scale}_sampling_${sampling}_$i.out" >> ${path}/test_conversion_N1_${N_1}_N2_${N_2}_N3_${N_3}_N4_${N_4}_cut_scale_${cut_scale}_sampling_${sampling}_$i.cfg  
                        echo "Error = ${path}/submitted_recas_conversion_N1_${N_1}_N2_${N_2}_N3_${N_3}_N4_${N_4}_cut_scale_${cut_scale}_sampling_${sampling}_$i.error" >> ${path}/test_conversion_N1_${N_1}_N2_${N_2}_N3_${N_3}_N4_${N_4}_cut_scale_${cut_scale}_sampling_${sampling}_$i.cfg  
                        echo "Queue" >> ${path}/test_conversion_N1_${N_1}_N2_${N_2}_N3_${N_3}_N4_${N_4}_cut_scale_${cut_scale}_sampling_${sampling}_$i.cfg  
                        ###then submit the job
			echo "${path}/log_N1_${N_1}_N2_${N_2}_N3_${N_3}_N4_${N_4}_cut_scale_${cut_scale}_sampling_${sampling}_$i"
                        echo "condor_submit -name ettore test_conversion_N1_${N_1}_N2_${N_2}_N3_${N_3}_N4_${N_4}_cut_scale_${cut_scale}_sampling_${sampling}_$i.cfg"
                        cd ${path}
                        #condor_submit -name ettore test_conversion_N1_${N_1}_N2_${N_2}_N3_${N_3}_N4_${N_4}_cut_scale_${cut_scale}_sampling_${sampling}_$i.cfg
                        bash submit_executable_conversion_N1_${N_1}_N2_${N_2}_N3_${N_3}_N4_${N_4}_cut_scale_${cut_scale}_sampling_${sampling}_$i.sh 
                        done
                    done
                done
            done
        done
    done
done
echo "DONE!"
