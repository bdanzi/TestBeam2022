#if !defined(__CINT__) || defined(__MAKECINT__)

#include "WaveData/inc/WaveData.h"
#include "WaveData/inc/RunHeader.h"
//#include "WaveData/inc/RunHeaderOSC.h"
#include <TTree.h>
#include <TFile.h>
#include <TString.h>
#include <TGraph.h>
#include "TCanvas.h"
#include <TROOT.h>
//#include <string>
#include <iostream>
#include <TSystem.h>
#include <TH2.h>
#include "TChain.h"
#include <stdlib.h>
#include <cstring>
#include <fstream>


#endif

using namespace std;


int main (int argc, char ** argv){
  
  Char_t name[300];
  char fld[200];
  if (argc>=2) {
    //	  if (argv[1][0]=='d') {
    if (strcmp(argv[1],"d")==0) {
      sprintf(fld,"/lustre/cms/store/user/taliercio/TestBeam/Drift");
    } else {
      sprintf(fld,"%s",argv[1]);
    }
  }
  int Run_number=0;
  if (argc>=3) {
#ifndef _OSC
    sprintf(name,"%s/run_%d.root",fld,atoi(argv[2]));
    Run_number=atoi(argv[2]);
#else
    sprintf(name,"%s/run-%05d.root",fld,atoi(argv[2]));
#endif
  } else {
#ifndef _OSC
    sprintf(name,"%s/run_126.root",fld);
#else
    sprintf(name,"%s/run-00000.root",fld);
#endif
  }

  std::cout << "File is =" << name << endl;

  float gsample=2.5; //Gsa
  float binsize=1./gsample; // 0.4 ns per bin	

  TFile *outfile = new TFile("drawWaveform.root", "RECREATE");
  //outfile->cd();

  // create canvas
  TCanvas *c1 = new TCanvas();
  TGraph *gr;
  //c1->cd();
  c1->Divide(2,4);


  int channel=0;
  int nchannels=8;
  int entry=0;

  auto fl = TFile::Open(name, "read");
  auto tree = static_cast<TTree*>(fl->Get("data"));
  int n = tree->GetEntries();
  std::cout << "Entries =" << n << endl;
  WaveData* wd = new WaveData();

  // for (int entry=0;entry<n;entry++){
  for (int entry=0;entry<5;entry++){

    
    std::cout << "Analizing entry= " << entry << std::endl;

    tree->SetBranchAddress("x", &wd);
    tree->GetEntry(entry);
    double voltage=0.;
    int canvas_i=0;
    
    
    for(int channel=0;channel<nchannels;channel++){
      canvas_i=channel+1;
      c1->cd(canvas_i);
      gr=new TGraph();
   
      float time=0; // ns
      for (auto point : wd->getX742Data()) {
      // cout << point.first << " Channel / Vch" << point.second[2495] << endl;
      if (point.first == channel) {
	//cout << "Found input for channel= " << channel << endl; 
      for (int i = 0; i < 2496; ++i) {
      //cout << "i= " << i << " " << point.first << " " << (double) point.second[i] << endl;
	    time=(i+1)*binsize;
	    voltage=((1.0/65536.0)*point.second[i]-0.5); //Volt from OSC
	    voltage*=-1;
	    gr->SetPoint(i, (double) time, (double) voltage);
	    c1->Update();
	  }
	  break;
	}
      }
      
      
      gr->SetMarkerStyle(7);
      gr->SetTitle("Pulses for Particle Detector");
      gr->GetXaxis()->SetTitle("Time (ns)");
      gr->GetYaxis()->SetTitle("Voltage (V)");
      gr->Draw("ACP");
      
    }
    

    outfile->cd();
    c1->Update();
    c1->Write();
    
  }
  fl->Close();
  delete wd;
  outfile->Close();
  
  return 0;
  
}
