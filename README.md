# 🚀 Unique Tech: Air Quality Innovation & AI Prediction

<div align="center">
  <img src="https://img.shields.io/badge/ACSTAC%202026-WINNER-gold?style=for-the-badge&logo=award" alt="ACSTAC 2026 Winner">
  <img src="https://img.shields.io/badge/Arduino-Prototyping-00979D?style=for-the-badge&logo=arduino" alt="Arduino">
  <img src="https://img.shields.io/badge/Python-Dashboard-3776AB?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Streamlit-UI-FF4B4B?style=for-the-badge&logo=streamlit" alt="Streamlit">
</div>

---

> 🎉 **🥇 Νικητής του Βραβείου Καινοτομίας ACSTAC 2026!**
> Το project μας αντιμετωπίζει το πρόβλημα της κακής ποιότητας αέρα στις σχολικές αίθουσες, συνδυάζοντας προηγμένους αισθητήρες hardware με Τεχνητή Νοημοσύνη (AI) για πρόβλεψη κινδύνου.

## 🌟 Επισκόπηση
Αυτό το αποθετήριο περιέχει τον πλήρη πηγαίο κώδικα (source code) του συστήματός μας. Η λύση μας δεν καταγράφει απλά δεδομένα, αλλά τα μετατρέπει σε **δράση**.

## 📂 Δομή Repository
| Φάκελος | Περιεχόμενο | Τεχνολογίες |
| :--- | :--- | :--- |
| **`/src`** | <img src="https://img.shields.io/badge/-Arduino-00979D?logo=arduino&logoColor=white" alt="Arduino"> Κώδικας αισθητήρων (`.ino`) & διαγράμματα σύνδεσης. | I2C, Serial, SCD4x |
| **`/src/software`** | <img src="https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white" alt="Python"> <img src="https://img.shields.io/badge/-Streamlit-FF4B4B?logo=streamlit&logoColor=white" alt="Streamlit"> Το Live Dashboard, η επικοινωνία με το Arduino (`app.py`) και οι εξαρτήσεις (`requirements.txt`). | Pandas, PySerial |

## 🚀 Γρήγορη Εκκίνηση

### Hardware (Arduino)
1. Συνδέστε τους αισθητήρες SCD4x και PMS5003 στο Arduino.
2. Ανεβάστε τον κώδικα `hardware/sensor_reader.ino`.

### Software (Python)
1. **Κλωνοποίηση:** `git clone https://github.com/unique-tech/air-quality-viz.git`
2. **Εγκατάσταση Εξαρτήσεων:** `pip install -r software/requirements.txt`
3. **Εκτέλεση Dashboard:** `streamlit run software/app.py`

## 📊 Χαρακτηριστικά Dashboard
- **Live Monitoring:** Παρακολούθηση CO2 (ppm), PM2.5, Θερμοκρασίας & Υγρασίας.
- **AI Prediction:** Πρόβλεψη των επιπέδων CO2 για τα επόμενα 30 λεπτά.
- **Alert System:** Ηχητική και οπτική ειδοποίηση όταν τα όρια ασφαλείας ξεπεραστούν.

## 🏆 Διακρίσεις
- **ACSTAC 2026** (Anatolia College Science & Technology Annual Conference): **1ο Βραβείο Καινοτομίας**.

---
**Αναπτύχθηκε με ❤️ από την Ομάδα Unique Tech.**

[Email](mailto:UniqueTech2025@outlook.com.gr) 
