"""
 
   Author: B. D'Anzi - University and INFN Bari
 
 
"""
import numpy as np
import matplotlib.pyplot as plt
import ROOT
import sys
from ROOT import gROOT
gROOT.SetBatch(True)
import argparse

# Create an argument parser
parser = argparse.ArgumentParser(description='Process integral charge data.')

# Add an argument for cut percentage
parser.add_argument('--cut_percentage', type=float, default=0.70, # cut on dE/dx can be changed from here
                    help='Percentage of events to keep for integral charge distribution')
parser.add_argument('--filename', type=str, default="output.txt",
                    help='Filename from which take data')

# Parse the command-line arguments
args = parser.parse_args()

# Access the cut_percentage value
cut_percentage = args.cut_percentage
filename = args.filename
# Function to define a Gaussian
def gaussian(x, params):
    return params[0] * ROOT.TMath.Gaus(x[0], params[1], params[2])

# Read data from the file
with open(filename, 'r') as file:
    lines = file.readlines()

# Extract integral charge values
charge_values = [float(line.split(':')[1].split()[0]) for line in lines]
# Order the values
charge_values.sort()
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
hist_charge_all_values = ROOT.TH1D("hist_charge_values", "Integral (All) Charge Values", 20, 0, max(charge_values)+100)
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
    # Print fit results
    print("Amplitude: {}".format(amplitude))
    print("Most Probable Value (MPV): {}".format(MPV))
    print("Sigma: {}".format(sigma))
    # Create canvas
    c0 = ROOT.TCanvas("c1", "Integral (All) Charge Values", 800, 600)
    c0.cd()
    c0.SetLogy()
    c0.Draw("same")
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
    box.Draw("same")

    # Save the canvas as a PDF file
    c0.SaveAs("IntegralChargeAllValuesnWithLandauFit.pdf")
else:
    print("Fit did not converge!")

########################################################
#           Integral Charge Values                     #
########################################################
# Plot values gutted of integral charge into a ROOT TH1D
hist_charge_values = ROOT.TH1D("hist_charge_values", "Integral Charge Values {} Cut".format(cut_percentage), 20, 0, max(charge_values)+100)
[hist_charge_values.Fill(charge) for charge in selected_charge_values]
# Plot the histogram
c1 = ROOT.TCanvas("c1", "Integral Charge Values", 800, 600)
# Create a Gaussian fit function
c1.cd()
fit_function = ROOT.TF1("gaussian_fit", gaussian, min(charge_values)-20, max(charge_values)+20, 3)
fit_function.SetParameters(1, hist_charge_values.GetMean(), hist_charge_values.GetRMS())
# Fit the histogram with the Gaussian function
fit_result = hist_charge_values.Fit("gaussian_fit", "SR")
# Access the fit results
fit_parameters = fit_result.GetParams()
fit_mean = fit_parameters[1]
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
c1.SaveAs("IntegralChargeValues.pdf")

mean_value = fit_mean
sigma_value = fit_sigma
ratio_sigma_mean = fit_sigma/fit_mean
# Print mean, sigma, and ratio
print("Mean Value dE/dx: {}".format(mean_value))
print("Sigma Value dE/dx: {}".format(sigma_value))
print("Ratio (Sigma/Mean) dE/dx: {}".format(ratio_sigma_mean))

########################################################
#           NPeak Cluster Values                        #
########################################################

# Extract NPeak cluster values
npeak_cluster_values = [int(line.split(':')[2]) for line in lines]
# Plot NPeak cluster values into a ROOT TH1D
hist_npeak_cluster_values = ROOT.TH1D("hist_npeak_cluster_values", "NPeak Cluster Values", 20, -10, max(npeak_cluster_values)+10)
[hist_npeak_cluster_values.Fill(npeak) for npeak in npeak_cluster_values]
fit_min = -10
fit_max = max(npeak_cluster_values)+10
# Fit the histogram with a Gaussian distribution
fit_result = hist_npeak_cluster_values.Fit("gaus", "S","", fit_min, fit_max)
# Access fit parameters
fit_parameters = fit_result.GetParams()
mean_npeak_cluster = fit_parameters[1]
sigma_npeak_cluster = fit_parameters[2]
chisquaredNdx = fit_result.Chi2()
# Calculate the resolution ratio
ratio_sigma_mean_npeak_cluster = sigma_npeak_cluster / mean_npeak_cluster
# Plot the histogram and draw the fit
c2 = ROOT.TCanvas("c2", "NPeak Cluster Values", 800, 600)
hist_npeak_cluster_values.Draw()
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
c2.SetLogy()
c2.Draw()
# Save the canvas as a PDF file
c2.SaveAs("NPeakClusterDistribution.pdf")

## Compute the ratio between sigma and mean for NPeak cluster values
#mean_npeak_cluster = np.mean(npeak_cluster_values)
#sigma_npeak_cluster = np.std(npeak_cluster_values)
#ratio_sigma_mean_npeak_cluster = sigma_npeak_cluster / mean_npeak_cluster

# Print mean, sigma, and ratio for NPeak cluster values
print("Mean NPeak dN/dx: {}".format(mean_npeak_cluster))
print("Sigma NPeak dN/dx: {}".format(sigma_npeak_cluster))
print("Ratio (Sigma/Mean) dN/dx: {}".format(ratio_sigma_mean_npeak_cluster))

print("Ratio (Sigma/Mean of dE/dx over dN/dx {}".format(ratio_sigma_mean/ratio_sigma_mean_npeak_cluster))
print("Ratio (Sigma/Mean of dN/dx over dE/dx {}".format(ratio_sigma_mean_npeak_cluster/ratio_sigma_mean))
# Keep the ROOT application open
#ROOT.gApplication.Run()
