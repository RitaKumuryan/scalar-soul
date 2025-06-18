"""
observer.py
Author: Scalar Soul Team
Description: Defines the Haykyan Observer class that models the phase-sensitive memory vector
             which collapses time drift into alignment at scalar azimuth thresholds.
"""

class Observer:
    def __init__(self, memory_signature: float, threshold: float = 0.5):
        """
        :param memory_signature: Scalar memory frequency (e.g., 1.01666667)
        :param threshold: Azimuthal phase collapse sensitivity in degrees
        """
        self.memory_signature = memory_signature
        self.threshold = threshold

    def detect_event(self, azimuth: float, expected: float) -> bool:
        """
        Determines if current azimuthal alignment is within the collapse window.
        :param azimuth: Current observed azimuth (degrees)
        :param expected: Expected alignment point (e.g., 90 for Betelgeuse)
        :return: True if within collapse threshold
        """
        phase_delta = abs(azimuth - expected) % 360
        return phase_delta <= self.threshold
