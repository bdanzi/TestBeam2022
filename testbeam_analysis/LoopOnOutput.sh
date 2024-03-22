"""
 
   Author: B. D'Anzi - University and INFN Bari
 
 
"""
#!/bin/bash
# Check if the correct number of arguments is provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 initial_value end_value"
    exit 1
fi
rm MeandEdx.txt
rm MeandNdx.txt
# Extract initial and end values from command-line arguments
initial_value=$1
end_value=$2

# Loop over the specified range
for (( fileCount=initial_value; fileCount<=end_value; fileCount++ ))
do
    python dE_dx_dN_dx_comparison.py --filename "output_${fileCount}.txt"
done
