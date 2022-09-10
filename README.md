<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![MIT][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#Drift-Tubes-2021-Test-Beam-offline-analysis">Drift Tubes 2021 Test Beam offline analysis</a>
      <ul>
        <li><a href="#authors">Authors</a></li>
        <li><a href="#setup">Setup</a></li>
         <li> <a href="#instructions">Instructions</a></li>
        <li><a href="#channels-correspondance">Channels correspondance</a></li>
      </ul>
    </li>
  </ol>
</details>

# TestBeam2022

The `run_table.xlsx` file contains the details of the different configurations associated to the ROOT files used for this data analysis.
The focus is on different momenta (165,40,180 GeV) muon beam runs from 6th July.

The following README could be deprecated in some parts, so please read carefully the general instructions in `TestBeam2022/drifttubes_offline_analysis/instructions.txt` ,
`TestBeam2022/drifttubes_offline_analysis/testbeam_analysis/instructions_first.txt`and  `TestBeam2022/drifttubes_offline_analysis/testbeam_analysis/instructions_second.txt`to run the code.

## Authors

- [Federica Cuna](https://github.com/federicacuna) (University and INFN Lecce)
- [Brunella D'Anzi](https://github.com/bdanzi) (University and INFN Bari)
- [Nicola De Filippis](https://github.com/ndefilip) (Politecnico and INFN Bari)


## Setup

On Bari ReCAS and in the `testbeam_analysis\` directory of this repository:

```bash
$ source /cvmfs/sft.cern.ch/lcg/views/LCG_98python3/x86_64-centos7-gcc10-opt/setup.sh
$ source setDCDataReaderEnv.sh
$ bash compile.sh
$ ./read_data . 4 0 -10 1
```
On lxplus and in the `testbeam_analysis\` directory of this repository:

```bash
$ source setDCDataReaderEnv.sh
$ bash compile.sh
$ ./read_data . 4 0 -10 1
```
where in the last code line:

- 4 is the run number

- 0 -10 is the number of events to be processed

- 1 is the sampling rate.

## Instructions

These macros find voltage amplitude peaks without any filter algorithm is applied to the waveform.
For each sample and each channel it is able to count how many events with an actual signal we have.
Config files and executables are created to run on more than one ROOT file (not available here, too much large in size).

```bash
$ bash submit_root_to_histos_root.sh
```

It will produce in `executables\`:
- executable files `submit_executable_conversion*.sh` per each `run_*.root` file that has to be converted in a root file containing histos 
with the most important physical variables
- config files that can be run as job in recas for accelerating the process of the histos ROOT file generation
```bash
$ bash submit_recas.sh 
```
It will produce in `executables\`::
- executable file `submit_executable.sh`
- config file that can be run as job in Recas
```bash
$ bash submit_executable.sh
```

It will produce:
- by using the plots.txt, per each .root file in the first column, per each channel in the second column,
per each event in the third column some physical quantities which are related to 
1) number of peaks, First Time Peak and Last Time Peak distributions
2) maxima
3) integral of the wavefunction 
4) wave functions w & w/o peak arrows
5) minima
6) number of events per each channel which passes a voltage amplitude requirement for the waveform maximum of 5 mV


## Channels correspondance

- 1,2,3,5,6,8,9,10 : 8 Drift Tubes of 1 cm cell size respectively:
  - Channel 2,3 Wire diameter of 15 micrometer 
  - Channel 1,5,6,8 and 7 Wire diameter of 20 micrometer 
  - Channel 9 and 10 Wire diameter of 25 micrometer 
- 0,4,7,11 : 4 Drift Tubes of 1.5 cm cell size respectively:
  - Channel 7,11 Wire diameter of 15 micrometer 
  - Channel 0 Wire diameter of 20 micrometer 
  - Channel 4 Wire diameter of 25 micrometer 
- 12,13,14,15 : Trigger Counters

<img width="964" alt="Channel Schematics" src="https://github.com/bdanzi/TestBeam2022/blob/main/Schermata%202022-09-10%20alle%2020.18.11.png">
Credits for the Channel Schematics: Federica Cuna (https://indico.ihep.ac.cn/event/16837/)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/bdanzi/drifttubes_offline_analysis.svg?style=for-the-badge
[contributors-url]: https://github.com/bdanzi/drifttubes_offline_analysis/contributors

[forks-shield]: https://img.shields.io/github/forks/bdanzi/ML_COURSEBARI.svg?style=for-the-badge
[forks-url]: https://github.com/bdanzi/drifttubes_offline_analysis/network/members

[stars-shield]: https://img.shields.io/github/stars/bdanzi/ML_COURSEBARI.svg?style=for-the-badge
[stars-url]: https://github.com/bdanzi/drifttubes_offline_analysis/stargazers

[issues-shield]: https://img.shields.io/github/issues/bdanzi/drifttubes_offline_analysis.svg?style=for-the-badge
[issues-url]: https://github.com/bdanzi/drifttubes_offline_analysis/issues

[license-shield]: https://img.shields.io/github/license/bdanzi/drifttubes_offline_analysis.svg?style=for-the-badge
[license-url]: https://github.com/bdanzi/drifttubes_offline_analysis/blob/main/LICENSE.txt

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/brunella-d-anzi


 




