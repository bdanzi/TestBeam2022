//Author 
//Walaa Elmetenawee//////////

Int_t FindPeaks(Int_t jentry, Int_t channel, Int_t npt, Float_t *amplitude, Float_t rms, Int_t *pkPos, Float_t *pkHgt, Int_t isChannel_1cm, Int_t isChannel_2cm,Int_t isChannel_1p5cm) {

// Int_t pkPos[250];
// Float_t pkHgt[250];

int Nold = 0;
float Delta;
float sigDelta=0.0;
float Norm;
float sigNorm =0.0;
float Chi2;
float Chi2sum;
float sigChi2;
Int_t NPeak=0;
float sigerror=0.0;
Float_t sigHgt[250];
std::vector<float> Snew;
std::vector<float> sigSnew;
std::vector<float> F;
std::vector<float> sigF;
std::vector<float> ANorm;
std::vector<float> normamplitude;
Int_t maxNPeak_1cm = 120;
Int_t maxNPeak_2cm = 170; 
Float_t max_amplitude= -1.0;
Int_t index_max = -1;


 /* TH1F *hChi2sum_peaks = new TH1F("hChi2sum_peaks","hChi2sum_peaks",2000,0,200);
  TH1F *hChi2sum_Nopeaks = new TH1F("hChi2sum_Nopeaks","hChi2sum_Nopeaks",2000,0,200);
  TH1F *hChi2sum_peaksGood = new TH1F("hChi2sum_peaksGood","hChi2sum_peaksGood",2000,0,200);
  TH2F *hChi2sum_time = new TH2F("hChi2sum_time","hChi2sum_time",1000, 0, 1000, 2000,0,200);*/



/////////////////////////////////////
/*int Krise = 3;   //Fun 1
int Kfall = 9;*/

/*int Krise = 3;   //Fun 2 Gsa 1
int Kfall = 10;*/

/*int Krise = 4;   //Fun 3
int Kfall = 14;*/

////////////////////2Gsa Templates////////////////////////////////
/*int Krise = 4;   //Fun 0 Gsa 2 T_rise 0.4 ns T_fall 1 ns 
int Kfall = 10;*/

/*int Krise = 5;   //Fun 0 Gsa 2 T_rise 0.5 ns T_fall 1.3 ns
int Kfall = 12;*/


/*int Krise = 6;   //Fun 1 Gsa 2  T_rise 0.6 ns T_fall 1.6 ns
int Kfall = 15;*/

/*int Krise = 6;   //Fun 2 Gsa 2  T_rise 0.6 ns T_fall 2.0 ns
int Kfall = 19;*/

/*int Krise = 6;   //Fun 2 Gsa 2  T_rise 0.6 ns T_fall 2.4 ns
int Kfall = 23;*/
////////////////////End of 2Gsa Templates////////////////////////////////

////////////////////1 Gsa Templates////////////////////////////////
/*int Krise = 3;   // Gsa 1 T_rise 0.6 ns T_fall 1.6 ns 
int Kfall = 8;*/

int Krise = 2;   // Gsa 1 T_rise 0.4 ns T_fall 1.0 ns 
int Kfall = 5;

////////////////////End of 1Gsa Templates////////////////////////////////

int Ktot = Krise + Kfall +1;	 
normamplitude.assign(Ktot,0.0);
	  
/*normamplitude[0] = 0.007; //Fun 1
normamplitude[1] = 0.036;
normamplitude[2] = 0.189;
normamplitude[3] = 1.0;
normamplitude[4] = 0.594;
normamplitude[5] = 0.353;	
normamplitude[6] = 0.210;	
normamplitude[7] = 0.125;
normamplitude[8] = 0.074;
normamplitude[9] = 0.044;	
normamplitude[10] = 0.026;	
normamplitude[11] = 0.016;	
normamplitude[12] = 0.009;*/

/*normamplitude[0] = 0.004; //Fun 3
normamplitude[1] = 0.016;
normamplitude[2] = 0.062;
normamplitude[3] = 0.249;
normamplitude[4] = 1.000;
normamplitude[5] = 0.707;	
normamplitude[6] = 0.499;	
normamplitude[7] = 0.353;
normamplitude[8] = 0.249;
normamplitude[9] = 0.176;	
normamplitude[10] = 0.125;	
normamplitude[11] = 0.088;	
normamplitude[12] = 0.062;	
normamplitude[13] = 0.044;	
normamplitude[14] = 0.031;
normamplitude[15] = 0.022;
normamplitude[16] = 0.016;
normamplitude[17] = 0.011;
normamplitude[18] = 0.008;	*/


////////////////////2Gsa Templates////////////////////////////////
/*normamplitude[0] = 0.007; //Fun 0 Gsa 2 T_rise 0.4 ns T_fall 1 ns  
normamplitude[1] = 0.024;
normamplitude[2] = 0.082;
normamplitude[3] = 0.287;
normamplitude[4] = 1.000;
normamplitude[5] = 0.607;
normamplitude[6] = 0.368;
normamplitude[7] = 0.223;
normamplitude[8] = 0.135;
normamplitude[9] = 0.082;
normamplitude[10] = 0.050;
normamplitude[11] = 0.030;
normamplitude[12] = 0.018;
normamplitude[13] = 0.011;
normamplitude[14] = 0.007;*/


/*normamplitude[0] = 0.007; //Fun 0 Gsa 2 T_rise 0.5 ns T_fall 1.3 ns  
normamplitude[1] = 0.018;
normamplitude[2] = 0.050;
normamplitude[3] = 0.135;
normamplitude[4] = 0.368;
normamplitude[5] = 1.000;
normamplitude[6] = 0.681;
normamplitude[7] = 0.463;
normamplitude[8] = 0.315;
normamplitude[9] = 0.215;
normamplitude[10] = 0.146;
normamplitude[11] = 0.099;
normamplitude[12] = 0.068;
normamplitude[13] = 0.046;
normamplitude[14] = 0.031;
normamplitude[15] = 0.021;
normamplitude[16] = 0.015;
normamplitude[17] = 0.010;*/



/*normamplitude[0] = 0.007; //Fun 1 Gsa 2  T_rise 0.6 ns T_fall 1.6 ns
normamplitude[1] = 0.016;
normamplitude[2] = 0.036;
normamplitude[3] = 0.082;
normamplitude[4] = 0.189;
normamplitude[5] = 0.435;
normamplitude[6] = 1.000;
normamplitude[7] = 0.732;
normamplitude[8] = 0.535;
normamplitude[9] = 0.392;
normamplitude[10] = 0.287;
normamplitude[11] = 0.210;
normamplitude[12] = 0.153;
normamplitude[13] = 0.112;
normamplitude[14] = 0.082;
normamplitude[15] = 0.060;
normamplitude[16] = 0.044;
normamplitude[17] = 0.032;
normamplitude[18] = 0.024;
normamplitude[19] = 0.017;
normamplitude[20] = 0.013;
normamplitude[21] = 0.009;*/

/*normamplitude[0] = 0.007; //Fun 2 Gsa 2  T_rise 0.6 ns T_fall 2.0 ns
normamplitude[1] = 0.016;
normamplitude[2] = 0.036;
normamplitude[3] = 0.082;
normamplitude[4] = 0.189;
normamplitude[5] = 0.435;
normamplitude[6] = 1.000;
normamplitude[7] = 0.779;
normamplitude[8] = 0.607;
normamplitude[9] = 0.472;
normamplitude[10] = 0.368;
normamplitude[11] = 0.287;
normamplitude[12] = 0.223;
normamplitude[13] = 0.174;
normamplitude[14] = 0.135;
normamplitude[15] = 0.105;
normamplitude[16] = 0.082;
normamplitude[17] = 0.064;
normamplitude[18] = 0.050;
normamplitude[19] = 0.039;
normamplitude[20] = 0.030;
normamplitude[21] = 0.024;
normamplitude[22] = 0.018;
normamplitude[23] = 0.014;
normamplitude[24] = 0.011;
normamplitude[25] = 0.009;*/


/*normamplitude[0] = 0.007; //Fun 2 Gsa 2  T_rise 0.6 ns T_fall 2.4 ns
normamplitude[1] = 0.016;
normamplitude[2] = 0.036;
normamplitude[3] = 0.082;
normamplitude[4] = 0.189;
normamplitude[5] = 0.435;
normamplitude[6] = 1.000;
normamplitude[7] = 0.812;
normamplitude[8] = 0.659;
normamplitude[9] = 0.535;
normamplitude[10] = 0.435;
normamplitude[11] = 0.353;
normamplitude[12] = 0.287;
normamplitude[13] = 0.233;
normamplitude[14] = 0.189;
normamplitude[15] = 0.153;
normamplitude[16] = 0.125;
normamplitude[17] = 0.101;
normamplitude[18] = 0.082;
normamplitude[19] = 0.067;
normamplitude[20] = 0.054;
normamplitude[21] = 0.044;
normamplitude[22] = 0.036;
normamplitude[23] = 0.029;
normamplitude[24] = 0.024;
normamplitude[25] = 0.019;
normamplitude[26] = 0.016;
normamplitude[27] = 0.013;
normamplitude[28] = 0.010;
normamplitude[29] = 0.008;*/
////////////////////End of 2Gsa Templates////////////////////////////////

/*normamplitude[0] = 0.002; //Fun 2 Gsa 1
normamplitude[1] = 0.018;
normamplitude[2] = 0.135;
normamplitude[3] = 1.0;
normamplitude[4] = 0.607;
normamplitude[5] = 0.368;	
normamplitude[6] = 0.223;	
normamplitude[7] = 0.135;
normamplitude[8] = 0.082;
normamplitude[9] = 0.050;	
normamplitude[10] = 0.030;	
normamplitude[11] = 0.018;	
normamplitude[12] = 0.011;
normamplitude[13] = 0.007;	*/


/*normamplitude[0] = 0.007; // Gsa 1 T_rise 0.6 ns T_fall 1.6 ns 
normamplitude[1] = 0.036;
normamplitude[2] = 0.189;
normamplitude[3] = 1.0;
normamplitude[4] = 0.535;
normamplitude[5] = 0.287;	
normamplitude[6] = 0.153;	
normamplitude[7] = 0.082;
normamplitude[8] = 0.044;
normamplitude[9] = 0.024;	
normamplitude[10] = 0.013;	
normamplitude[11] = 0.007;	*/


normamplitude[0] = 0.007; // Gsa 1 T_rise 0.4 ns T_fall 1.0 ns 
normamplitude[1] = 0.082;
normamplitude[2] = 1.0;
normamplitude[3] = 0.368;
normamplitude[4] = 0.135;
normamplitude[5] = 0.050;	
normamplitude[6] = 0.018;	
normamplitude[7] = 0.007;


////////////////////End of 1Gsa Templates////////////////////////////////

ANorm.assign(Ktot,0.0);
Snew.assign(npt,0.0);
sigSnew.assign(npt,0.0);
F.assign(Ktot,0.0);
sigF.assign(Ktot,0.0);
  		for (int i=0; i<npt;i++ ){
   		 Snew[i]=amplitude[i];
   		 sigSnew[i] = rms;
   		 
  		}
		sigerror = rms;      ///to try the error
//	sigDelta = sqrt(2)*sigerror;
//	sigNorm = 2*sigerror;
        Delta=0.0;
        Norm=0.0;
 
	  do
        {
     //    cout<<"start new loop"<<endl;
     //    cout<<"NPeak start=  "<<NPeak<<endl;
		for (int j = Krise;j< (npt - Kfall);j++){	
	//	cout<<"NPeak start2=  "<<NPeak<<endl;	
	//	cout<<"start"<<endl;


		    Nold = NPeak;
			Delta = (Snew[j+Kfall] - Snew[j-Krise])/(float)(Ktot-1);
		//	Delta = (Snew[j+Kfall] - Snew[j-Krise])/(float)(Ktot);
			sigDelta = sqrt(pow(sigSnew[j+Kfall],2) + pow(sigSnew[j-Krise],2));
			Norm = Snew[j] - Snew[j-Krise] - fabs(Delta)*(float)(Krise);
            sigNorm = sqrt(pow(sigSnew[j],2)+pow(sigSnew[j-Krise],2)+ pow(sigDelta, 2));
       //     cout <<"jentry= "<< jentry<<"j= "<<j<<"Delta= "<<Delta<<"         sigDelta= "<< sigDelta<< "        Norm= "<< Norm<< "        sigNorm= "<<sigNorm<<endl;
		
			Chi2=0.0;
			Chi2sum=0.0;
			sigChi2=0.0;
			for(int k=0;k<Ktot;k++){
			pkPos[NPeak] = 0;
            pkHgt[NPeak] = 0;

     //      cout <<"j= "<< j<<"k=  "<<k<<"sigSnew[j+k-Krise]= "<<sigSnew[j+k-Krise]<<"         sigSnew[j-Krise]= "<< sigSnew[j-Krise]<< "        sigDelta= "<< sigDelta<<endl;
        	F[k]= Snew[j+k-Krise] - Snew[j-Krise] - fabs(Delta)*(float)k;
			sigF[k] = sqrt(2* (1+pow((float)k/(float)(Ktot-1),2)))*sigerror;
//			sigF[k] = sqrt(pow(sigSnew[j+k-Krise],2) + pow(sigSnew[j-Krise],2)) + pow(sigDelta,2);
//	     	cout<<"sigF[k]=  "<<sigF[k]<<"sigF_new=  "<<sqrt(pow(sigSnew[j+k-Krise],2) + pow(sigSnew[j-Krise],2) + pow(sigDelta,2))<<endl;

         	ANorm[k] = normamplitude[k]*Norm;
     //       cout <<"F[k] = "<<F[k]<<"ANorm[k]= "<<ANorm[k]<<endl;
    		Chi2 = pow((F[k] - ANorm[k]),2)/(pow(sigNorm,2)+pow(sigF[k],2));
	    //	sigChi2 = sqrt(pow(sigNorm,2)+pow(sigF[k],2));
		//	Chi2 = pow((F[k]-ANorm[k])/sigChi2,2);
			Chi2sum += Chi2;
		//	cout <<"check3"<<"j= "<<j<< "     k= "<<k<<"    F[k]= "<<F[k]<<"    F.at(k)= "<<F.at(k)<< "      sigF[k]= "<<sigF.at(k)<< "      sigF[k]= "<<sigF.at(k)<< "      ANorm[k]= " <<ANorm[k]<<"      ANorm.at(k)= " <<ANorm.at(k)<< "        Chi2= "<<Chi2<<"        Delta= "<< Delta << endl;
		//	cout <<"Snew[j-Krise+k+1]= "<<Snew[j-Krise+k+1]<<endl; 
    	//	if (j> 200 && j< 270 && jentry==2 && channel==7){cout <<"NPeak= "<< NPeak<<"    Channel="<<channel<<"    entry="<<jentry<<"    pkPos[NPeak-1]= "<<pkPos[NPeak-1]<<"   pktime="<< pkPos[NPeak-1] * 0.833<<"    pkHgt[NPeak-1]= "<<pkHgt[NPeak-1]<<"   sigHgt[NPeak-1]= "<<sigHgt[NPeak-1]<<"    Event no= "<< jentry<< "    j="<<j<<"   k="<< k <<"     Chi2sum=" << Chi2sum<<"     Chi2=" << Chi2<<"    fabs(F[Krise-1])= "<< fabs(F[Krise-1])  <<"amplitude[j]"<<amplitude[j]<<endl;}
			//		if (amplitude[j] > 0.01){cout <<"Chi2"<<Chi2<<"F[k]=  "<<F[k]<<"ANorm[k]=   "<<ANorm[k]<<"Norm=   "<<Norm<<"sigNorm=  "<<sigNorm<<"sigF[k]=   " <<sigF[k]<<endl;}

			}
			
  
		//	if(Chi2sum<10 && F[Krise-1] > 0.005){
		//	if(Chi2sum <300 && amplitude[j] > 0.01 && fabs(F[Krise-1]) > 0.0001){
		//	if(Chi2sum <300 && amplitude[j] > 0.01){
	//	    cout <<"j=  "<<j<< "NPeak= "<< NPeak<<"Chi2=  "<<Chi2<<"     Chi2sum=" << Chi2sum<<" amplitude[j]=  "<< amplitude[j]<<endl;

//		    if(Chi2sum<10 && fabs(F[Krise]) > 0.001) {
/*		    if(Chi2sum <100 && amplitude[j] > 0.01 && fabs(F[Krise]) > 0.0001){
				pkPos[NPeak] = j;
		     	pkHgt[NPeak]=amplitude[j];
				sigHgt[NPeak] = sigF[Krise];


                  NPeak++;
			for(int k=0;k<Ktot;k++){
			Snew[j+k-Krise]= Snew[j+k-Krise] - F[k];
			sigSnew[j+k-Krise] = sigF[k];

			}
         
			}*/
				if((Chi2sum <100  && amplitude[j] > 0.01) ){ 
	
			  
	if(NPeak==0){
	  pkHgt[NPeak]= amplitude[j];
//	  sigHgt[NPeak] = sigF[Krise];
	  pkPos[NPeak]= j;
	  NPeak++;
	}
	else{
	  if(j - pkPos[NPeak-1] > 1){ // Separated Electrons
      if (max_amplitude > 0. && index_max > 0){
        pkHgt[NPeak-1] = max_amplitude;
      //  sigHgt[NPeak] = sigF[Krise];
	      pkPos[NPeak-1] = index_max;
      }
      max_amplitude = -1.0; 
      index_max = -1; 
	    pkHgt[NPeak]= amplitude[j];
	 //   sigHgt[NPeak] = sigF[Krise];
	    pkPos[NPeak]= j;
	    NPeak++;
	  }
	  else{ // consecutive electrons
      if(amplitude[j]> max_amplitude){ 
        if(amplitude[j-1] > amplitude[j]){
          max_amplitude = amplitude[j-1]; 
          index_max = j-1; 
        }
        else{
        max_amplitude = amplitude[j]; 
        index_max = j; 
        }
      }
   /*   pkHgt[NPeak-1] = amplitude[j];
      sigHgt[NPeak] = sigF[Krise];
	  pkPos[NPeak-1] = j;*/
	  
	  pkHgt[NPeak-1] = max_amplitude;
   //   sigHgt[NPeak-1] = sigF[Krise];
	  pkPos[NPeak-1] = index_max;
	  }
	  
	}
				for(int k=0;k<Ktot;k++){
			Snew[j+k-Krise]= Snew[j+k-Krise] - F[k];
			sigSnew[j+k-Krise] = sigF[k];

			}

    
			  }
		//For Gsa 1.2	  
		// cout <<"Channel=   " <<channel<< "jentry= "<< jentry<<"j= "<<j<< "NPeak= "<< NPeak<<"    pkPos[NPeak-1]= "<<pkPos[NPeak-1]<<"   pktime="<< pkPos[NPeak-1] * 0.833<<"    pkHgt[NPeak-1]= "<<pkHgt[NPeak-1]/*<<"   sigHgt[NPeak-1]= "<<sigHgt[NPeak-1]*/<<"     Chi2sum=" << Chi2sum<<"     Chi2=" << Chi2<<"    F[Krise]= "<< F[Krise]  <<"amplitude[j]"<<amplitude[j]<<endl;
        //For Gsa 2
	//	 cout <<"Channel=   " <<channel<< "jentry= "<< jentry<<"j= "<<j<< "NPeak= "<< NPeak<<"    pkPos[NPeak-1]= "<<pkPos[NPeak-1]<<"   pktime="<< pkPos[NPeak-1] * 0.5<<"    pkHgt[NPeak-1]= "<<pkHgt[NPeak-1]/*<<"   sigHgt[NPeak-1]= "<<sigHgt[NPeak-1]*/<<"     Chi2sum=" << Chi2sum<<"     Chi2=" << Chi2<<"    F[Krise]= "<< F[Krise]  <<"amplitude[j]"<<amplitude[j]<<"amplitude[j]-amplitude[j-krise]"<<amplitude[j]-amplitude[j-Krise]<<endl;
	

		//	cout <<"NPeak= "<< NPeak<<"     Chi2sum=" << Chi2sum<<"amplitude[j]=   "<<amplitude[j]<< "fabs(F[Krise-1])=   "<< fabs(F[Krise-1])<<endl;
			//if (j> 200 && j< 270 && jentry==2 && channel==7){cout <<"NPeak= "<< NPeak<<"    Channel="<<channel<<"    entry="<<jentry<<"    pkPos[NPeak-1]= "<<pkPos[NPeak-1]<<"   pktime="<< pkPos[NPeak-1] * 0.833<<"    pkHgt[NPeak-1]= "<<pkHgt[NPeak-1]<<"   sigHgt[NPeak-1]= "<<sigHgt[NPeak-1]<<"    Event no= "<< jentry<< "    j="<<j<<"     Chi2sum=" << Chi2sum<<"     Chi2=" << Chi2<<"    fabs(F[Krise-1])= "<< fabs(F[Krise-1])  <<"amplitude[j]"<<amplitude[j]<<endl;}
     /*       if (NPeak >= 1)
            {
            hChi2sum_peaks->Fill(Chi2sum);
            }
             if (NPeak < 1)
            {
            hChi2sum_Nopeaks->Fill(Chi2sum);            
            }*/
             
	/*	     if(channel == 12 && jentry== 9)
		     {
		     hChi2sum_time->Fill(X[j],Chi2sum);
		     }*/
		     
           //  cout <<"check4"<<endl;
       //    if (jentry >2) break;
             if (NPeak == 0 || NPeak == Nold) continue;
             if((NPeak==100 && isChannel_1cm) || (NPeak==150 && isChannel_1p5cm) || (NPeak==200 && isChannel_2cm))  {
      // cout <<"\n";
      break;}
			}
	  }
 	while (NPeak != 0 && NPeak != Nold && ((NPeak <100 && isChannel_1cm)||(NPeak <150 && isChannel_1p5cm)||(NPeak <200 && isChannel_2cm) )); 
 //	cout<<"NPeak end=  "<<NPeak<<endl;
 // cout<<"end the loops"<<endl;
 return NPeak;
  }