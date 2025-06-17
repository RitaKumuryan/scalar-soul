
import numpy as np
from astropy.time import Time
from astropy.coordinates import EarthLocation, AltAz, get_sun
import astropy.units as u
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Constants
SCALAR_CONSTANT = 1.01666667  # Haykyan drift multiplier
AVELYATS_DAYS = 6              # Annual correction phase

def calculate_drift(year: int, day_of_year: int) -> float:
    spiral_progress = (year % 4) * 30  # 30° per year, reset every 4 years
    daily_drift = spiral_progress * SCALAR_CONSTANT * (day_of_year / 360)
    return daily_drift

def get_celestial_azimuth(target_star: str, obs_time: Time, obs_location: EarthLocation) -> float:
    from astroquery.simbad import Simbad
    from astropy.coordinates import SkyCoord

    if target_star.lower() == 'betelgeuse':
        star_coord = SkyCoord.from_name('Betelgeuse')
    else:
        star_coord = SkyCoord.from_name('Delta Ori')  # Mintaka

    altaz_frame = AltAz(obstime=obs_time, location=obs_location)
    star_altaz = star_coord.transform_to(altaz_frame)
    return star_altaz.az.deg

tatev = EarthLocation(lat=39.3792*u.deg, lon=46.2503*u.deg, height=1600*u.m)
obs_time = Time(datetime.utcnow(), format='datetime')

def plot_spiral_cycle(years=4):
    theta = np.linspace(0, years * 2 * np.pi, 1000)
    r = (theta / (2 * np.pi)) * 30  # 30° per year

    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.plot(theta, r, color='#9c27b0', linewidth=2)
    ax.set_title("Haykyan Spiral Time Cycle (4-Year Reset)", pad=20)
    ax.set_rlabel_position(135)
    plt.savefig('haykyan_spiral.png', dpi=300)
    plt.show()

def gregorian_to_haykyan(date: datetime) -> tuple[int, int]:
    day_of_year = date.timetuple().tm_yday
    haykyan_year = date.year
    if day_of_year > 360:
        return (haykyan_year + 1, day_of_year - 360)
    else:
        return (haykyan_year, day_of_year)

def run_full_simulation():
    print("\n=== Sidereal-Solar Drift ===")
    for year in range(1, 5):
        drift = calculate_drift(year, 180)
        print(f"Year {year}, Midyear Drift: {drift:.2f}°")

    print("\n=== Celestial Anchors ===")
    mintaka_az = get_celestial_azimuth('Mintaka', obs_time, tatev)
    print(f"Mintaka azimuth from Tatev: {mintaka_az:.2f}° (Expected ~98°)")

    plot_spiral_cycle()

    print("\n=== Avelyats Correction ===")
    xmas = datetime(2024, 12, 25)
    hy, hd = gregorian_to_haykyan(xmas)
    print(f"Dec 25, 2024 → Haykyan Year {hy}, Day {hd}")

if __name__ == "__main__":
    run_full_simulation()
