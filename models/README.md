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
---

### 📍 `observer.py` – Scalar Phase-Sensitive Observer Logic

This module defines the `Observer` class, which detects "collapse" events when azimuthal alignments (e.g., Mintaka, Betelgeuse) approach a symbolic scalar threshold — typically 0.5°.

**Core Use Case**:
- Detect when an observer is “phase-aligned” with a celestial anchor.
- Trigger memory registration or scalar event based on sidereal resonance.

**Example**:
```python
from observer import Observer

observer = Observer(threshold=0.5)
print(observer.check_alignment(azimuth_actual=98.02, azimuth_expected=98.0))
# Output: True (within phase alignment)
Used in conjunction with haykyan_phase1.py for resonance tracking and symbolic synchronization logic.

---

#### 2. **Next Optional Tasks**
- Add `observer.py` import into `haykyan_phase1.py` for potential inline alignment checks.
- Begin writing unit tests for symbolic hour validation (optional but encouraged).


