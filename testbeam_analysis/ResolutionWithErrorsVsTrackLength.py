import os
import re
import numpy as np
from ROOT import TCanvas, TGraphErrors, gROOT, TF1

# Start ROOT in batch mode
gROOT.SetBatch(True)

# Function to compute resolution
def compute_resolution(mean, sigma):
    return sigma / mean

# Function to compute error in resolution
def compute_resolution_error(mean, sigma, mean_error, sigma_error):
    resolution = compute_resolution(mean, sigma)
    return resolution * np.sqrt((sigma_error / sigma)**2 + (mean_error / mean)**2)

# Function to create a graph with error bars
def create_graph_with_errors(factors, resolutions, resolution_errors, title, xAxisTitle):
    graph = TGraphErrors(len(factors), np.array(factors), np.array(resolutions),
                         np.zeros(len(factors)), np.array(resolution_errors))
    graph.SetMarkerStyle(20)
    graph.SetMarkerColor(4)
    graph.SetTitle(title)
    graph.GetXaxis().SetTitle(xAxisTitle)
    graph.GetYaxis().SetTitle("Resolution")
    return graph

# Initialize lists to store resolutions, errors, and factors
resolutions_edx = []
resolution_errors_edx = []
factors_edx = []
resolutions_ndx = []
resolution_errors_ndx = []
factors_ndx = []

# Traverse through folders
for folder in os.listdir('.'):
    if folder.startswith("Outputs_"):
        # Extract hitsPerTrack from folder name
        match = re.search(r'\d+hitsPerTrack', folder)
        if match:
            hitsPerTrack = int(match.group(0)[:-len('hitsPerTrack')])  # Extract numerical part
            factor = 0.8 * 1.414 * hitsPerTrack
            counting = hitsPerTrack * 1.414
            

            # Look for MeandEdx.txt and MeandNdx.txt
            edx_file = os.path.join(folder, "MeandEdx.txt")
            ndx_file = os.path.join(folder, "MeandNdx.txt")

            # Check if both files exist
            if os.path.exists(edx_file) and os.path.exists(ndx_file):
                # Read data
                edx_data = np.loadtxt(edx_file)
                ndx_data = np.loadtxt(ndx_file)

                # Compute resolutions and errors
                res_edx = compute_resolution(edx_data.mean(), edx_data.std())
                res_ndx = compute_resolution(ndx_data.mean(), ndx_data.std())
                error_edx = compute_resolution_error(edx_data.mean(), edx_data.std(),
                                                      edx_data.mean() * 0.05, edx_data.std() * 0.05)  # Assuming 5% error
                error_ndx = compute_resolution_error(ndx_data.mean(), ndx_data.std(),
                                                      ndx_data.mean() * 0.05, ndx_data.std() * 0.05)  # Assuming 5% error

                resolutions_edx.append(res_edx)
                resolution_errors_edx.append(error_edx)
                factors_edx.append(factor)
                resolutions_ndx.append(res_ndx)
                resolution_errors_ndx.append(error_ndx)
                factors_ndx.append(counting)

# Create TGraphs for MeandEdx.txt and MeandNdx.txt
graph_edx = create_graph_with_errors(factors_edx, resolutions_edx, resolution_errors_edx,
                                     "Resolution vs Track Length for MeandEdx.txt","L [cm]")
graph_ndx = create_graph_with_errors(factors_ndx, resolutions_ndx, resolution_errors_ndx,
                                     "Resolution vs Number of Clusters for MeandNdx.txt","N")

# Proceed with plotting...
# Continue from where we left off...

if len(resolutions_edx) == len(resolutions_ndx):
    # Create canvas for MeandEdx.txt
    canvas_edx = TCanvas("canvas_edx", "MeandEdx", 800, 600)
    canvas_edx.cd()
    # Define the power law function for dEdx
    fit_function_edx = TF1("fit_function_edx", "[0]*pow(x, -0.37)", min(factors_edx), max(factors_edx))
    # Set initial parameter values (optional)
    fit_function_edx.SetParameter(0, 1.0)  # Initial guess for the amplitude
    # Fit the graph for MeandEdx.txt
    graph_edx.Fit("fit_function_edx")
    # Draw the graph with fit function
    graph_edx.Draw("AP")
    canvas_edx.Update()
    canvas_edx.SaveAs("resolution_vs_factor_edx.pdf")

    # Extract fit results for MeandEdx.txt
    parameter0_edx = fit_function_edx.GetParameter(0)
    print("Fit Results for MeandEdx.txt:")
    print("Parameter 0 (Amplitude):", parameter0_edx)

    # Create canvas for MeandNdx.txt
    canvas_ndx = TCanvas("canvas_ndx", "MeandNdx", 800, 600)
    canvas_ndx.cd()
    # Define the power law function for dNdx
    fit_function_ndx = TF1("fit_function_ndx", "[0]*pow(x, -0.5)", min(factors_ndx), max(factors_ndx))
    # Set initial parameter values (optional)
    fit_function_ndx.SetParameter(0, 1.0)  # Initial guess for the amplitude
    # Fit the graph for MeandNdx.txt
    graph_ndx.Fit("fit_function_ndx")
    # Draw the graph with fit function
    graph_ndx.Draw("AP")
    canvas_ndx.Update()
    canvas_ndx.SaveAs("resolution_vs_factor_ndx.pdf")

    # Extract fit results for MeandNdx.txt
    parameter0_ndx = fit_function_ndx.GetParameter(0)
    print("Fit Results for MeandNdx.txt:")
    print("Parameter 0 (Amplitude):", parameter0_ndx)
else:
    print("Not all points are available for both MeandEdx.txt and MeandNdx.txt, graphs cannot be plotted yet.")
