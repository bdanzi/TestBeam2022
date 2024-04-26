#include <TTree.h>
#include <TFile.h>
#include <TString.h>
#include <TROOT.h>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <TSystem.h>
#include <TH2.h>
#include "TGraph.h"
#include "TCanvas.h"
#include "TString.h"
#include <stdlib.h>
#include <string>
#include <libgen.h>
#include <cstdlib>
#include <stdio.h>
#include <bits/stdc++.h> 
#include "ROOT/RDataFrame.hxx"
#include "ROOT/RVec.hxx"


// New
#include <WaveData.h>
#include <RunHeader.h>
#include <boost/format.hpp>

using namespace ROOT::RDF;
using namespace ROOT::VecOps;

#define NBOARDS 1

typedef struct {
   char event_header[4];
   unsigned int event_serial_number;
   unsigned short year;
   unsigned short month;
   unsigned short day;
   unsigned short hour;
   unsigned short minute;
   unsigned short second;
   unsigned short millisecond;
   unsigned short range;
} EHEADER;

//

int main (int argc, char ** argv){

 std::ifstream fdatalist;
 fdatalist.open(argv[1]);
 int nchannels=8;
 
 if (!fdatalist) {
      printf("Cannot find file %s \n",argv[1]);
      return 1;
 }

 Char_t eventfile[500];
 sprintf(eventfile,"%s",argv[1]);
 TString eventfileBase=basename(eventfile);
 std::cout << "eventfile is= " << eventfileBase.Data() << std::endl;
 eventfileBase.ReplaceAll("listfiles_","");
 eventfileBase.ReplaceAll(".txt","");
 //eventfileBase.ReplaceAll("Run","");
 //eventfileBase.ReplaceAll("Event","");
 std::cout << "eventfile is= " << eventfileBase.Data()  << std::endl;

 //char rootfile[256]="waveform.root";
 char rootfile[256];
 // std::system("mkdir -p Data_OSC_tmp_ROOT"); 
 sprintf(rootfile,"run_OSC_%s.root",eventfileBase.Data());

 TFile *outfile = new TFile(rootfile, "RECREATE");


 char eventfilechar[256];
 sprintf(eventfilechar,"%s",eventfileBase.Data());

 TString s_run,s_event;
 __uint32_t runnum;
 __uint32_t evnum;

 std::stringstream ss(eventfileBase.Data());
 std::string str;
 int i=0;

 while (getline(ss, str, '_')) {
   //std::cout << str << std::endl;
   if (i==0) s_run=str; 
   if (i==1) s_event=str;
   i++;
 }

 s_run.ReplaceAll("Run","");
 s_event.ReplaceAll("Event","");
 runnum=atoi(s_run.Data());
 evnum=atoi(s_event.Data());

 std::cout << "Run number is= " << runnum << " Event number is= " << evnum << std::endl;

 


// NEW
 EHEADER eh;
 eh.second=-1;

 double waveform[NBOARDS][8][2496], time[NBOARDS][8][2496];

 RunHeader runHeader(NBOARDS, 8,/////
		     runnum, eh.second);
 WaveData waveData(runHeader);
 __uint16_t nX742PointsPerCh=2496;
 __uint16_t* chdata0 = new __uint16_t[nX742PointsPerCh];

 TTree *rec;
 rec = new TTree("data", "");
 //rec->Branch("x", &waveData, 64000);
 rec->Branch("x", &waveData);
 waveData.setEventNumber(evnum);

 std::string sa;
 int channel=0;

 while (getline(fdatalist, sa)) { 
   std::cout << "ChFile is= " << sa.c_str() << "\n"; 
    
   std::ifstream flist;
   int nlines=2496;
   double timef[nlines];
   unsigned short voltage[nlines];
   double voltage2[nlines];
   double triggertime=0.;
   double timeunit=1E09;

   flist.open(sa);

   if (!flist) {
     printf("Cannot find file %s \n",sa.c_str());
      return 1;
   }

   if(!flist) return 1;

   Char_t channelfile[500];
   sprintf(channelfile,"%s",sa.c_str());
   std::cout << channelfile << std::endl;
   TString channelfileBase=basename(channelfile);
   channelfileBase.ReplaceAll("_formatted.txt","");
   //channelfileBase.ReplaceAll("--","");
   //channelfileBase.ReplaceAll("ev","");

   std::cout << "channelfile is= " << channelfileBase.Data() << std::endl;

   std::stringstream ssch(channelfileBase.Data());
   std::string strch;
   int ich=0;

   TString s_triggertime;


   while (getline(ssch, strch, 'T')) {
     //std::cout << str << std::endl;
     if (ich==1) s_triggertime=strch; 
     ich++;
   }

   s_triggertime.ReplaceAll("rigger","");
   std::cout << "Trigger time is= " << s_triggertime.Data() << std::endl;
   triggertime=atof(s_triggertime.Data());
   std::cout << "Trigger time is= " << s_triggertime.Data() << " Trigger time= " << triggertime << std::endl;


   int i=0;
   std::cout << "NBoards=" << NBOARDS << std::endl;
   int b=NBOARDS-1;
   
   for(int i=0;i<nlines;i++){
    flist >> timef[i] >> voltage2[i];
    //    if (i==0) triggertime=timef[i];
    timef[i]=timef[i]-triggertime;
    // timef[i]=timef[i]*timeunit;
    std::cout << "Line is= " << i << " Time (ns)= " << timef[i] << " V=" << voltage2[i] << std::endl;
    waveform[b][channel][i]=voltage2[i];
    time[b][channel][i]=timef[i];

    //voltage2[i]*=-1.;
    voltage[i]=int(65536*(voltage2[i]+0.5));
    std::cout << "Line is= " << i << " Time (ns)= " << timef[i] << " Vch=" << voltage[i] << std::endl;
   }

   for(int i=0;i<nlines;i++){
     std::cout << "Voltage= " << i << " " << voltage[i] << std::endl;
   }
   waveData.setX742ChannelData(channel, voltage);

   channel++;
 }

 rec->Fill();
 rec->SetDirectory(0);
 rec->Write();

 outfile->Close();

 return 0;
}
