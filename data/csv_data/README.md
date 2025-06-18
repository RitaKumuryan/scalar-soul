# 📊 Haykyan Astronomical Reference Data

This folder contains structured `.csv` datasets used in the Haykyan Boon Tomar (HBT) model. Each file documents key sidereal or solar astronomical alignments used to validate the spiral time framework and sacred site synchronization.

---

### 🟩 `hbt_new_year_marker.csv`
- 📅 **Date:** August 11
- 🌠 **Event:** Mintaka rises at 98° azimuth above the Gavazan pillar at Tatev
- 🕓 **Time:** 04:00 AM (AST)
- 🔭 **Role:** Marks the beginning of the Haykyan sidereal year (0° of the spiral)

---

### 🟨 `mintaka_risings_tatev.csv`
- 📆 **Timestamps:** 12 Haykyan sidereal months
- 🌌 **Star:** Mintaka (δ Orionis)
- 📈 **Azimuth:** Always ~98°
- 🔁 **Purpose:** Demonstrates Mintaka’s azimuthal constancy at monthly reset points

---

### 🟥 `zero_hour_alignment.csv`
- 📅 **Date:** August 5
- 🕓 **Time:** 04:24 AM (Mintaka), 06:00 AM (Sun)
- 🌠 **Mintaka:** 360th rise (completion of sidereal cycle)
- ☀️ **Sun:** Rises at az. 67.5° (Tatev axis alignment)
- 🌀 **Role:** Triggers entry into Avelyats (“Time Outside Time”)

---

### 🟦 `orion_anchor_events.csv`
- 📌 **Three Anchors:**
  - Mintaka → August 11 (New Year)
  - Betelgeuse → August 5 (Reset Point)
  - Mintaka → August 5, 04:24 (Zero Hour)
- 📡 **Data:** Azimuths, RA/Dec, elevation, site coordinates
- 🔗 **Purpose:** Consolidated sidereal alignment logic based on Orion’s motion

---

### 📝 Format Notes:
- All times include UTC and AST (Armenia Standard Time)
- RA and Declination match observed star catalogs
- Elevation values apply where known (e.g., Mintaka at Tatev)

---

> These datasets are used throughout `/models/`, `Annex B`, and in spiral phase simulations. All files are open-source and may be forked for sidereal model comparison or scalar synchronization research.
