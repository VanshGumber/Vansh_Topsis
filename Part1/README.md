# Part I – Command Line Implementation of TOPSIS

## 1. Objective
To implement TOPSIS method using Python and execute it as a command line program.

## 2. Description
The program accepts a CSV file containing alternatives and criteria, along with user-defined weights and impacts. It computes the TOPSIS score for each alternative and outputs a ranked result file.

## 3. Usage
python topsis.py topsis.csv 1,1,1,1,1 +,+,+,+,+ output.csv

## 4. Input Requirements
- Input file must be a CSV file
- The file must contain three or more columns
- First column should contain alternative names
- Columns from second to last must contain numeric values only
- Weights and impacts must be comma-separated
- Number of weights, impacts, and criteria columns must be equal
- Impacts must be either + or -

## 5. Output
The output CSV file contains:
- Original input data
- Topsis Score column
- Rank column

## 6. Error Handling
The program handles incorrect arguments, file not found errors, invalid data, and mismatched inputs.

