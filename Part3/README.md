# Part III – TOPSIS Web Application (Streamlit)

## 1. Objective
To develop a web-based TOPSIS service using Streamlit that allows users to compute TOPSIS rankings through a browser interface.

---

## 2. Description
This application provides an interactive interface where users can:
- Upload a CSV input file
- Enter weights and impacts
- Provide an email ID
- Receive the computed TOPSIS result as an email attachment

The TOPSIS algorithm used here follows the same mathematical formulation as implemented in Part I.

---

## 3. Features

- CSV file upload
- Validation of weights and impacts
- Email format validation
- TOPSIS computation
- Output CSV file sent via email

---
## 4. Live Deployment

The TOPSIS web application has been deployed using Streamlit Cloud and can be accessed at:

https://topsis-vansh-102303922.streamlit.app/

Users can upload the CSV file, enter weights and impacts, and receive the TOPSIS result via email without running the application locally.


---
## 5. Constraints

- Number of weights must equal number of impacts
- Number of weights must match the number of criteria
- Impacts must be either + or -
- Weights and impacts must be comma-separated
- Email ID must be valid

---

## 6. Email Configuration

The application uses Gmail SMTP with an App Password.

Secrets are configured using Streamlit Cloud:
- EMAIL: Sender Gmail address
- PASSWORD: Gmail App Password

---

## 7. Running the Application

```bash
streamlit run app.py
```


