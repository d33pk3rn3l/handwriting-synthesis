

LAGRANGE_POINTS = """LAGRANGE POINTS
Equilibrium points, five in total, where gravitational 
forces and centrifugal forces balance.

L1, L2, L3 are unstable.
L4 and L5 are stable.
"""

ORBITAL_ELEMENTS = """ORBITAL ELEMENTS
a: Semi-major axis, defines the size of the orbit.
e: Eccentricity, determines the shape of the orbit.
i: Inclination, tilt relative to the equatorial plane.
O: Right ascension of ascending node (RAAN).
w: Argument of perigee, orientation of the orbit.
v: True anomaly, current position in the orbit.
"""

ORBIT_TYPES = """ORBIT TYPES
Molniya Orbit is a highly elliptical orbit with 63.4 inclination
Provides excellent high-latitude coverage but high cost and radiation
Sun Synchronous Orbit keeps a constant sun angle relative to Earth
Enables consistent lighting conditions but involves high cost
Repeating Groundtrack Orbit ensures periodic coverage of the same areas
Offers predictable coverage patterns, can suffer from perturbations
"""


SOURCES_OF_PERTURBATIONS = """SOURCES OF PERTURBATIONS
Earth Oblateness (J2) causes nodal regression and 
apsidal precession, (canceled at Molniya Orbit)
Third-Body Effects come from the Sun, Moon, or other celestial bodies
Atmospheric Drag reduces altitude and lifetime in low orbits
Solar Radiation Pressure affects large spacecraft in high orbits
"""

TYPES_OF_MANEUVERS = """TYPES OF MANEUVERS
Hohmann Transfer: Most efficient transfer between circular coplanar orbits
Delta-v for impulses: 
For rendezvous: 
bi-elliptic transfer: Efficient for large ratio changes in orbit size.
Plane change: Expensive maneuvers altering inclination.
"""

TYPES_OF_ORBITAL_MANEUVERS = """Orbital Maneuvers
Impulsive Maneuvers: Short-duration firing, fast but propellant-intensive
Extended Maneuvers: Used with ion engines for sustained adjustments.
Gravity Assist: Uses gravity to alter trajectory without propellant
Δv is modified; enables "grand tour" like Cassini's flyby
Aerobraking: Reduces velocity using atmospheric drag
Phasing Maneuvers: Adjusts the time-position alignment of a spacecraft
"""

DELTA_V_MAP = """DELTA-V MAP"""
