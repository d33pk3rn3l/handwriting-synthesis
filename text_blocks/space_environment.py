
"""
Space Environment Blocks
"""

SPACE_ENVIRONMENT = """Space Environment Overview

1. Layers of the Atmosphere
Troposphere (0-20 km): 
- Weather processes, convection, mixing of air.
- Ends at the tropopause (7km poles, 10km mid-lat, 20km equator).
Stratosphere (20-40 km): 
- Temperature incr. with alt due to UV absorption (ozone layer).
Mesosphere (40-80 km): 
- Temperature decreases with altitude, coldest region (-143C).
- Where most meteors burn up.
Thermosphere (80-100 km): 
- Heated by extreme UV/X-ray from Sun; home to the ionosphere.
- High presence of atomic oxygen, can degrade spacecraft surfaces.
Exosphere (greater 1000 km): 
- Transition to space, dominated by hydrogen and helium.
- No clear boundary; solar radiation pressure gt Earths gravity

2. Ionosphere
Region within thermosphere with free electrons and ions.
Varies with solar activity; affects radio communication.
Different layers (D, E, F) change between day/night.

3. Magnetosphere
Region dominated by Earths magnetic field.
Shields Earth from charged solar particles.
Includes Van Allen Belts: 
- Trapped high-energy protons and electrons.
- Inner belt (700-10,000 km), outer belt (13,000-60,000 km).
- Radiation intensities vary and can damage spacecraft electronics.

4. Solar Activity and Cosmic Rays
Solar cycle (11 years): 
- High sunspot counts means more solar flares and CMEs
- SEPs can arrive in minutes, harmful to satellites.
Galactic and extragalactic cosmic rays: 
- High-energy particles from supernovae, quasars, gamma-ray bursts.
- Can penetrate shielding, cause single-event effects

5. Space Radiation Environment
High-energy particles (electrons, protons, ions) can induce:
- Single-Event Upsets: bit flips or circuit malfunctions.
- Material degradation, especially from atomic oxygen in LEO.
- Charging effects: differential charging, electrostatic discharge

6. Microgravity
Objects in orbit experience free-fall, so no effective weight
Fluid behavior changes, no convection or buoyancy effects.
Tidal (gravity gradient) forces matter over large structures

7. Orbital Debris
Growing concern due to increasing space activity.
Risks: Collisions that generate more debris.
Mitigation and remediation strategies:
- Collision avoidance, EoL deorbiting, active debris removal
"""

VAN_ALLEN_BELTS = """Van Allen Belts
Regions of trapped high-energy particles:
Inner Belt: 0.2 to 2 Earth radii, dominated by protons (100s MeV)
Outer Belt: 3 to 10 Earth radii, with electrons 100 keV to 10 MeV
Dynamic environments affected by solar activity.
"""

CHARGING_SHIELDING = """Charging and Shielding
1. Charging Mechanisms
Surface Charging: due to plasma interactions or photoelectric currents.
Deep Charging: Charging due high-energy partl. in spacecraft interior
2. Effects:
Electrostatic Discharges (ESDs) can disrupt or damage electronics.
Differential charging creates localized electric fields, risking arcing.
3. Shielding Strategies:
Use of conductive coatings and materials to reduce potentials
Shielding against low-energy particles, watch out for Bremsstrahlung
"""