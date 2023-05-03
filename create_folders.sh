#!/bin/bash

# Loop through numbers 12 to 60 and create folder case_X
for i in {12..60}
do
    foldername="case_$i"
    mkdir "$foldername"
    # Create problem.txt file inside each folder
    touch "$foldername/problem.txt"
done
