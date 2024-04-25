#!/bin/env python3

import subprocess
import os
import sys

def test_data_product_writer():
    # Specify the directory where the .bin files are located
    directory = os.path.abspath(os.path.dirname(__file__))
    # Loop through each file in the specified directory
    for filename in os.listdir(directory):
        # Check if the file is a .bin file
        if filename.endswith(".bin"):
            # Construct the full path to the file
            file_path = os.path.join(directory, filename)
            
            # Construct the command to run
            command = f"../../../src/fprime_gds/executables/data_product_writer.py {file_path}"
            
            # Execute the command
            process = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            # Output the result
            print(f"Running command: {command}")
            print(process.stdout.decode())
            print(process.stderr.decode())

