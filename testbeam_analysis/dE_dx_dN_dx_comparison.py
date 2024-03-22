"""
 
   Author: B. D'Anzi - University and INFN Bari
 
 
"""
import numpy as np
import matplotlib.pyplot as plt
import ROOT
import sys
import os
import shutil
from ROOT import gROOT
gROOT.SetBatch(True)
import argparse

# Create an argument parser
parser = argparse.ArgumentParser(description='Process integral charge data.')

# Add an argument for cut percentage
parser.add_argument('--cut_percentage', type=float, default=0.8, # cut on dE/dx can be changed from here
                    help='Percentage of events to keep for integral charge distribution')
parser.add_argument('--filename', type=str, default="output.txt",
                    help='Filename from which take data')
parser.add_argument('--directoryname', type=str, default="histosTB_run_53_N1_10.000_N2_1.200_N3_0.000_N4_0.000_cut_scale_0.200_sampling_1.0",
                    help='Directory in which saving plots')
# Parse the command-line arguments
args = parser.parse_args()

# Access the cut_percentage value
cut_percentage = args.cut_percentage
filename = args.filename
directory_name = args.directoryname
if not os.path.exists(directory_name):
    print("Directory does not exist. Creating it.")
    os.makedirs(directory_name)
    #shutil.rmtree(directory_name)  # Remove the directory and all its contents
    
# Function to define a Gaussian
def gaussian(x, params):
    return params[0] * ROOT.TMath.Gaus(x[0], params[1], params[2])

# Read data from the file
with open(filename, 'r') as file:
    lines = file.readlines()

# Extract integral charge values
charge_values = [float(line.split(':')[1].split()[0]) for line in lines]
#print("Carica: ", charge for charge in charge_values)
# Order the values
charge_values.sort()
#print("Carica Dopo: ",charge for charge in charge_values)
# Take the first percentage of values
num_values_to_keep = int(cut_percentage * len(charge_values))
selected_charge_values = charge_values[:num_values_to_keep]
# Compute mean and sigma
mean_value = np.mean(selected_charge_values)
sigma_value = np.std(selected_charge_values)
# Compute the ratio between sigma and mean
ratio_sigma_mean = sigma_value / mean_value

########################################################
#           Integral All Charge Values                     #
########################################################
# Plot values gutted of integral charge into a ROOT TH1D
# Create canvas
c0 = ROOT.TCanvas("c0", "Integral (All) Charge Values", 800, 600)
c0.cd()
c0.SetLogy()
c0.Draw("same")
hist_charge_all_values = ROOT.TH1D("hist_charge_all_values", "Integral (All) Charge Values", 100, 0, max(charge_values))
[hist_charge_all_values.Fill(charge) for charge in charge_values]
# Define a Landau function
landau_function = ROOT.TF1("landau_function", "[0]*TMath::Landau(x, [1], [2])", 0, 10)
landau_function.SetParameters(max(charge_values), 2, .0)  # Set initial parameters (amplitude, MPV, sigma)
# Fit the histogram with the Landau function
fit_result = hist_charge_all_values.Fit(landau_function, "S","",min(charge_values),max(charge_values))
# Check if the fit converged
if fit_result.IsValid():
    print("Fit converged successfully!")
    # Access fit parameters
    amplitude = landau_function.GetParameter(0)
    MPV = landau_function.GetParameter(1)
    sigma = landau_function.GetParameter(2)
    chi_square = fit_result.Chi2()
    # Print fit results
    print("Amplitude: {}".format(amplitude))
    print("Most Probable Value (MPV): {}".format(MPV))
    print("Sigma: {}".format(sigma))
    # Plot the histogram
    hist_charge_all_values.Draw("same")
    # Draw the Landau fit function
    landau_function.Draw("same")

    # Draw a box containing fit results
    box = ROOT.TPaveText(0.2, 0.6, 0.5, 0.8, "NDC")
    box.SetFillColor(0)
    box.SetFillStyle(0)
    box.SetBorderSize(0)
    box.SetTextAlign(12)
    box.AddText("Amplitude: {}".format(amplitude))
    box.AddText("Most Probable Value (MPV): {}".format(MPV))
    box.AddText("Sigma: {}".format(sigma))
    box.AddText("Chi-square/ndf: {}".format(chi_square))
    box.Draw("same")

    # Save the canvas as a PDF file
    c0.SaveAs(directory_name+ "/" + "IntegralChargeAllValuesnWithLandauFit" + filename + ".pdf")
else:
    print("Fit did not converge!")

########################################################
#           Integral Charge Values                     #
########################################################
# Plot the histogram
c1 = ROOT.TCanvas("c1", "Integral Charge Values", 800, 600)
# Create a Gaussian fit function
c1.cd()
c1.Draw("same")
# Plot values gutted of integral charge into a ROOT TH1D
hist_charge_values = ROOT.TH1D("hist_charge_values", "Integral Charge Values {} Cut".format(cut_percentage), 100, 0, max(charge_values))
[hist_charge_values.Fill(charge) for charge in selected_charge_values]
fit_function = ROOT.TF1("gaussian_fit", gaussian, min(charge_values), max(charge_values), 3)
fit_function.SetParameters(1, hist_charge_values.GetMean(), hist_charge_values.GetRMS())
# Fit the histogram with the Gaussian function
fit_result = hist_charge_values.Fit("gaussian_fit", "SR")
# Access the fit results
fit_parameters = fit_result.GetParams()
fit_mean = fit_parameters[1]
def append_to_file(value):
    with open("MeandEdx.txt", "a") as file:
        file.write(str(value) + "\n")
append_to_file(fit_mean)
fit_sigma = fit_parameters[2]
chi_square = fit_result.Chi2()
# Add a box to display fit parameters
info_box = ROOT.TPaveText(0.1, 0.8, 0.4, 0.9, "NDC")
info_box.SetFillColor(0)
info_box.AddText("Fit Mean: {}".format(fit_mean))
info_box.AddText("Fit Sigma: {}".format(fit_sigma))
info_box.AddText("Chi-square/ndf: {}".format(chi_square))
info_box.AddText("Resolution: {}".format(fit_sigma/fit_mean))
info_box.Draw("same")
hist_charge_values.Draw("same")
c1.SetLogy()
c1.Draw("same")
c1.SaveAs(directory_name+ "/" + "IntegralChargeValues" + filename + ".pdf")

mean_value = fit_mean
sigma_value = fit_sigma
ratio_sigma_mean = fit_sigma/fit_mean

########################################################
#           NPeak Cluster Values                        #
########################################################

# Extract NPeak cluster values
npeak_cluster_values = [int(line.split(':')[2].split()[0]) for line in lines]
#npeak_cluster_values = [int(line.split(':')[2]) for line in lines]
# Plot NPeak cluster values into a ROOT TH1D
hist_npeak_cluster_values = ROOT.TH1D("hist_npeak_cluster_values", "NPeak Cluster Values", max(npeak_cluster_values), 0, max(npeak_cluster_values))
[hist_npeak_cluster_values.Fill(npeak) for npeak in npeak_cluster_values]
fit_min = min(npeak_cluster_values)
fit_max = max(npeak_cluster_values)
# Fit the histogram with a Gaussian distribution
fit_result = hist_npeak_cluster_values.Fit("gaus", "S","", fit_min, fit_max)
# Access fit parameters
fit_parameters = fit_result.GetParams()
mean_npeak_cluster = fit_parameters[1]
def append_to_file_clusters(value):
    with open("MeandNdx.txt", "a") as file:
        file.write(str(value) + "\n")
append_to_file_clusters(mean_npeak_cluster)
sigma_npeak_cluster = fit_parameters[2]
chisquaredNdx = fit_result.Chi2()
# Calculate the resolution ratio
ratio_sigma_mean_npeak_cluster = sigma_npeak_cluster / mean_npeak_cluster
# Plot the histogram and draw the fit
c2 = ROOT.TCanvas("c2", "NPeak Cluster Values", 800, 600)
c2.cd()
c2.Draw()
hist_npeak_cluster_values.Draw("same")
hist_npeak_cluster_values.GetFunction("gaus").SetLineColor(ROOT.kRed)  # Set fit line color
# Draw fit parameters on the canvas
info_box_dNdx = ROOT.TPaveText(0.6, 0.5, 0.8, 0.7, "NDC")
info_box_dNdx.SetFillColor(0)
info_box_dNdx.AddText("Fit Mean: {}".format(mean_npeak_cluster))
info_box_dNdx.AddText("Fit Sigma: {}".format(sigma_npeak_cluster))
info_box_dNdx.AddText("Chi-square/ndf: {}".format(chisquaredNdx))
info_box_dNdx.AddText("Resolution: {}".format(ratio_sigma_mean_npeak_cluster))
info_box_dNdx.Draw("same")
# Set logarithmic scale on the y-axis
#c2.SetLogy()
# Save the canvas as a PDF file
c2.SaveAs(directory_name+ "/" +"NPeakClusterDistribution"+ filename + ".pdf")

## Compute the ratio between sigma and mean for NPeak cluster values
#mean_npeak_cluster = np.mean(npeak_cluster_values)
#sigma_npeak_cluster = np.std(npeak_cluster_values)
#ratio_sigma_mean_npeak_cluster = sigma_npeak_cluster / mean_npeak_cluster

########################################################
#           NPeak Electrons Values                     #
########################################################

# Extract NPeak cluster values
npeak_electrons_values = [int(line.split(':')[3]) for line in lines]
# Plot NPeak cluster values into a ROOT TH1D
hist_npeak_electrons_values = ROOT.TH1D("hist_npeak_electrons_values", "NPeak Cluster Values", max(npeak_electrons_values), 0, max(npeak_electrons_values))
[hist_npeak_electrons_values.Fill(npeak) for npeak in npeak_electrons_values]
# Plot the histogram and draw the fit
c3 = ROOT.TCanvas("c3", "NPeak Electrons Values", 800, 600)
c3.cd()
c3.Draw()
# Define a Landau function
landau_function_electrons = ROOT.TF1("landau_function_electrons", "[0]*TMath::Landau(x, [1], [2])", 0, 10)
landau_function_electrons.SetParameters(max(npeak_electrons_values), 2, .0)  # Set initial parameters (amplitude, MPV, sigma)
# Fit the histogram with the Landau function
fit_result_electrons = hist_npeak_electrons_values.Fit(landau_function_electrons, "S","",min(npeak_electrons_values),max(npeak_electrons_values))
#c3.SetLogy()
# Check if the fit converged
if fit_result_electrons.IsValid():
    print("Fit converged successfully!")
    # Access fit parameters
    amplitude_electrons = landau_function_electrons.GetParameter(0)
    MPV_electrons = landau_function_electrons.GetParameter(1)
    sigma_electrons = landau_function_electrons.GetParameter(2)
    chi_square_electrons = fit_result_electrons.Chi2()
    # Print fit results
    info_box_electrons = ROOT.TPaveText(0.6, 0.5, 0.8, 0.7, "NDC")
    info_box_electrons.SetFillColor(0)
    info_box_electrons.AddText("Amplitude: {}".format(amplitude_electrons))
    info_box_electrons.AddText("Most Probable Value (MPV): {}".format(MPV_electrons))
    info_box_electrons.AddText("Chi2Square: {}".format(fit_result.Chi2()))
    info_box_electrons.AddText("Sigma: {}".format(sigma_electrons))
    info_box_electrons.Draw("same")
# Set logarithmic scale on the y-axis
#c3.SetLogy()
hist_npeak_electrons_values.Draw("same")
landau_function_electrons.Draw("same")
# Save the canvas as a PDF file
c3.SaveAs(directory_name+ "/" +"NPeakElectronsDistribution"+ filename + ".pdf")

# Print mean, sigma, and ratio for NPeak cluster values
print("Mean NPeak dN/dx: {}".format(mean_npeak_cluster))
print("Sigma NPeak dN/dx: {}".format(sigma_npeak_cluster))
print("Ratio (Sigma/Mean) dN/dx: {}".format(ratio_sigma_mean_npeak_cluster))
# Print mean, sigma, and ratio
print("Mean Value dE/dx: {}".format(mean_value))
print("Sigma Value dE/dx: {}".format(sigma_value))
print("Ratio (Sigma/Mean) dE/dx: {}".format(ratio_sigma_mean))

print("Ratio (Sigma/Mean of dE/dx over dN/dx {}".format(ratio_sigma_mean/ratio_sigma_mean_npeak_cluster))
print("Ratio (Sigma/Mean of dN/dx over dE/dx {}".format(ratio_sigma_mean_npeak_cluster/ratio_sigma_mean))
# Keep the ROOT application open
#ROOT.gApplication.Run()
