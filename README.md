# Topsis

This repository contains the complete implementation of the TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) assignment, divided into three parts.

---

## Part I – Command Line Program

A Python-based command line implementation of the TOPSIS method.

- Accepts CSV input file, weights, and impacts
- Computes TOPSIS scores and ranks
- Generates an output CSV file
- Includes comprehensive input validation


---

## Part II – PyPI Package

The TOPSIS implementation has been packaged and published to PyPI.

- Package Name: topsis-vansh-102303922
- Installable via pip
- Executable via command line

PyPI Link:
https://pypi.org/project/topsis-vansh-102303922/


---

## Part III – Web Application (Streamlit)

A web-based TOPSIS service built using Streamlit.

- Allows CSV upload and parameter input
- Validates weights, impacts, and email format
- Computes TOPSIS using the same logic as Part I
- Sends the output CSV file via email

Secrets (email credentials) are securely managed using Streamlit Cloud Secrets.


