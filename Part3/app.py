import streamlit as st
import pandas as pd
import numpy as np
import re
import smtplib
from email.message import EmailMessage
from io import BytesIO

st.set_page_config(page_title="TOPSIS Web Service")
st.title("TOPSIS Web Service")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
weights_input = st.text_input("Enter weights (comma separated)")
impacts_input = st.text_input("Enter impacts (+ or -, comma separated)")
email = st.text_input("Enter email ID")

def valid_email(e):
    return re.match(r"[^@]+@[^@]+\.[^@]+", e)

def run_topsis(df, weights, impacts):
    data = df.iloc[:, 1:].astype(float)

    norm = data / np.sqrt((data ** 2).sum())

    for i in range(len(weights)):
        norm.iloc[:, i] *= weights[i]

    ideal_best = []
    ideal_worst = []

    for i in range(len(impacts)):
        if impacts[i] == "+":
            ideal_best.append(norm.iloc[:, i].max())
            ideal_worst.append(norm.iloc[:, i].min())
        else:
            ideal_best.append(norm.iloc[:, i].min())
            ideal_worst.append(norm.iloc[:, i].max())

    s_plus = np.sqrt(((norm - ideal_best) ** 2).sum(axis=1))
    s_minus = np.sqrt(((norm - ideal_worst) ** 2).sum(axis=1))

    score = s_minus / (s_plus + s_minus)
    df["Topsis Score"] = score
    df["Rank"] = df["Topsis Score"].rank(ascending=False).astype(int)

    return df

def send_email(receiver, csv_bytes):
    msg = EmailMessage()
    msg["Subject"] = "TOPSIS Result"
    msg["From"] = st.secrets["EMAIL"]
    msg["To"] = receiver
    msg.set_content("Please find the TOPSIS result attached.")

    msg.add_attachment(
        csv_bytes.getvalue(),
        maintype="application",
        subtype="octet-stream",
        filename="output.csv"
    )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(st.secrets["EMAIL"], st.secrets["PASSWORD"])
        server.send_message(msg)

if st.button("Run TOPSIS"):
    try:
        if uploaded_file is None:
            st.error("Please upload a CSV file")
            st.stop()

        if not valid_email(email):
            st.error("Invalid email ID")
            st.stop()

        weights = [float(i) for i in weights_input.split(",")]
        impacts = impacts_input.split(",")

        df = pd.read_csv(uploaded_file)

        if df.shape[1] < 3:
            st.error("Input file must contain at least three columns")
            st.stop()

        if len(weights) != len(impacts) or len(weights) != df.shape[1] - 1:
            st.error("Number of weights, impacts, and criteria must match")
            st.stop()

        for i in impacts:
            if i not in ["+", "-"]:
                st.error("Impacts must be + or - only")
                st.stop()

        result = run_topsis(df, weights, impacts)

        buffer = BytesIO()
        result.to_csv(buffer, index=False)

        send_email(email, buffer)

        st.success("TOPSIS computation successful. Result sent to email.")
        st.dataframe(result)

    except Exception as e:
        st.error(str(e))
