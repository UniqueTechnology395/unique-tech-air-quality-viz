import streamlit as st
import serial
import pandas as pd
import time
from datetime import datetime

# Ρύθμιση της σελίδας
st.set_page_config(page_title="Unique Tech Live Dashboard", layout="wide")
st.title("📊 Unique Tech: Live Air Quality Analysis")
st.write("Παρακολούθηση δεδομένων από το Arduino σε πραγματικό χρόνο.")

# Ρυθμίσεις Σειριακής Θύρας (Αλλάξτε το 'COM3' ανάλογα με τη δική σας θύρα)
SERIAL_PORT = 'COM3' 
BAUD_RATE = 9600

# Αποθήκευση δεδομένων σε ένα DataFrame στη μνήμη
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=['Time', 'CO2', 'Temp'])

# Containers για τα γραφήματα
placeholder = st.empty()

try:
    # Σύνδεση με το Arduino
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    time.sleep(2) # Αναμονή για σταθεροποίηση

    while True:
        line = ser.readline().decode('utf-8').strip()
        if line:
            values = line.split(',')
            if len(values) == 2:
                new_row = {
                    'Time': datetime.now().strftime('%H:%M:%S'),
                    'CO2': float(values[0]),
                    'Temp': float(values[1])
                }
                
                # Ενημέρωση δεδομένων (κρατάμε τις τελευταίες 20 μετρήσεις)
                st.session_state.data = pd.concat([st.session_state.data, pd.DataFrame([new_row])], ignore_index=True)
                if len(st.session_state.data) > 20:
                    st.session_state.data = st.session_state.data.iloc[-20:]

                # Σχεδίαση Dashboard
                with placeholder.container():
                    col1, col2 = st.columns(2)
                    col1.metric("Current CO2", f"{values[0]} ppm")
                    col2.metric("Current Temp", f"{values[1]} °C")

                    st.subheader("Μεταβολή CO2")
                    st.line_chart(st.session_state.data.set_index('Time')['CO2'])
                    
                    st.subheader("Μεταβολή Θερμοκρασίας")
                    st.line_chart(st.session_state.data.set_index('Time')['Temp'])

        time.sleep(0.1)

except Exception as e:
    st.error(f"Σφάλμα σύνδεσης: {e}. Βεβαιωθείτε ότι το Arduino είναι συνδεδεμένο στη θύρα {SERIAL_PORT}.")
