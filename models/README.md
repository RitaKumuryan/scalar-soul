# Haykyan Spiral Time – Computational Models

This directory contains Phase 1 implementation code for simulating the Haykyan Boon Tomar (HBT) system — an ancient sidereal-solar calendar based on spiral time mechanics.

## 📌 Modules

- **`haykyan_phase1.py`**  
  Core simulation including:
  - Sidereal-solar drift with scalar constant `1.01666667`
  - Astronomical azimuth validation for Mintaka & Betelgeuse
  - Spiral time visualization (4-year loop)
  - Avelyats correction phase (days 361–366)

## 🚀 How to Run

1. Install dependencies:
   ```bash
   pip install astropy numpy matplotlib astroquery
