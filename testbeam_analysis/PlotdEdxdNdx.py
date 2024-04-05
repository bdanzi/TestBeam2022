import ROOT
import argparse
from ROOT import gROOT
gROOT.SetBatch(True)

def fit_histogram(file_name):
    # Open the text file and read the values
    values = []
    with open(file_name, "r") as file:
        for line in file:
            value = float(line.strip())  # Assuming one value per line
            values.append(value)

    # Create a histogram
    histogram = ROOT.TH1F("histogram", file_name, int(max(values) - min(values)), min(values), max(values))
    for value in values:
        histogram.Fill(value)

    # Fit the histogram with a Gaussian function
    fit_func = ROOT.TF1("fit_func", "gaus")
    histogram.Fit(fit_func)

    # Print the fit parameters
    fit_mean = fit_func.GetParameter(1)
    fit_sigma = fit_func.GetParameter(2)
    print("Fit Mean:", fit_mean)
    print("Fit Sigma:", fit_sigma)
    resolution = fit_sigma / fit_mean

    # Create a canvas
    canvas = ROOT.TCanvas("canvas", "Histogram Canvas", 800, 600)

    # Draw the histogram
    histogram.Draw()

    # Draw the fit function on top
    fit_func.Draw("same")

    # Add a text box to display fit parameters and resolution
    textbox = ROOT.TPaveText(0.8, 0.6, 0.9, 0.7, "NDC")
    textbox.AddText("Fit Mean: {:.4f}".format(fit_mean))
    textbox.AddText("Fit Sigma: {:.4f}".format(fit_sigma))
    textbox.AddText("Resolution: {:.4f}".format(resolution))
    textbox.SetFillColor(0)
    textbox.SetBorderSize(0)
    textbox.Draw()

    # Save the plot as a PDF
    output_pdf_name = file_name.split('.')[0] + "_plot.pdf"
    canvas.Print(output_pdf_name)

    # Keep the plot open
    canvas.Update()
    canvas.Draw()
    #ROOT.gApplication.Run()

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Fit histogram of values with a Gaussian function and save plot as PDF")
    parser.add_argument("file", help="Input text file containing the values")
    args = parser.parse_args()

    # Call fit_histogram function with the provided file name
    fit_histogram(args.file)
