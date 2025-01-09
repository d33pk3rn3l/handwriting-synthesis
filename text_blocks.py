"""
This module contains text blocks used for handwriting synthesis.
"""

# General Things Systems Engineering

STEPS = """Define Objectives and Constraints
1. Define the Broad (qualitative) Objectives and Constraints
2. Define the Principal Players
3. Define the Program Timescale
4. Estimate the quantitative Needs, reqs, and Constraints

Define Alternative Mission Concepts or Designs
5. Define Alternative Mission Architectures
6. Define Alternative Mission Concepts
7. Define the Likely System Drivers and Key reqs

Evaluate the Alternative Mission Concepts
8. Conduct Performance Assessments and System Trades
9. Evaluate Mission Utility
10. Define the Baseline Mission Concept and Architecture
11. Revise the quantitative reqs and Constraints
12. Iterate and Explore Other Alternatives

Define and Allocate System reqs
13. Define System reqs
14. Allocate the reqs to System Elements
"""

TRL = """TRL
1. Basic principles observed and reported.  
2. Technology concept and application formulated.  
3. Analytical, experimental critical function characteristic PoC
4. Component and breadboard validation in laboratory environment
5. Component and breadboard validation in relevant environment 
6. System/sub-system model or prototype demo in an operational env
7. System prototype demonstration in an operational environment
8. Actual system completed and flight qualified through test and demo
9. Actual system flight proven through successful mission operations
"""

# Mission Architecture

MISSION_ARCHITECTURE = """Mission Architecture
1. Subject: Observing or interacting with passive or active subjects
2. Payload: Spacecraft hw or sw for observing or interacting with subject
3. Spacecraft Bus: Subsystems supporting the payload
4. Ground Segment: Communications equipment for control and comms
5. Mission Operations: People and software managing the mission daily
6. Command, Control, and Communications Architecture
7. Orbit: Spacecrafts path; constellations for coordinated orbits
8. Launch Segment: Getting the spacecraft to orbit system
Mission Concept: Definition of how mission elements meet objectives
"""

COMMON_ALTERNATIVES_MISSION_ELEMENTS = """Common Alternatives Mission Elements
MISSION CONCEPT
1. Data Delivery: direct to user, automated ground, manual
2. Tasking: Ground centralized, autonomous, simple ops

CONTROLLABLE SUBJECT
1. Selection: Standard, private receivers, ship, plane, special purpose
2. Performance: Effective isotropic radiated power, gain over noise temp
3. Steering: fixed, tracking, mechanical

PASSIVE SUBJECT
1. What: subject change, thermal env, emitted radiation, contrast to bg

PAYLOAD
1. Frequency: Comms: bands; Observations: IR, VIS, MW, UV, X-ray
2. Size vs. sensitivity: Small A with high P (or sens.) or vice versa

SPACECRAFT BUS
1. Propulsion: Chemical (bi, mono), electric, solar sail, gravity assist
2. Orbit Control: If needed, ground or onbaord
3. Navigation: GPS, star tracker, ground tracking
4. ADCS: None, spinning, 3-axis, articulated payload vs pointing
5. Power: Solar, nuclear, battery, fuel cell, or other. Pointed arrays.

LAUNCH SYSTEM
1. Launch Vehicle: Rocket, plane, balloon, sling. With upper stage?
2. Launch Site: Ground, sea, air, space, or country specific

ORBIT
1. Special Orbits: Sun-synchronous, GEO, SSO, molniya, ground repeat
2. Alt: LEO: 200-2000km; MEO: 2000-35786km; GEO: 35786km
3. Inclination: Polar: 90; Equatorial: 0; SSO: 98; GEO: 0
4. Constellation: Single, multiple, walker, phased, or other

GROUND SYSTEM: existing or dedicated, private or gov (NASA, USN, NOAA)

COMMS ARCHITECTURE
1. Timeliness: Store n dump, real-time, near-real-time
2. Control and dissemination: single, distributed, usercontrol, commercial
3. Relay: TDRSS, sat-to-sat, commercial system (Starlink, Iridium, IDRS)

MISSION OPERATIONS
1. Automation Level: Fully auto, part-time ops, full-time ops
2. Autonomy level: Full ground command n control, partial, full onboard
"""

# Mission Concept

FIRESAT_MISSION_CONCEPT_ELEMENTS = """FS Mission Concept Elements
1. Data Delivery: How imagery collected, identified, and transmitted
2. Tasking, Scheduling, and Control: What, when, and how to image
3. Comms Architecture: What network is used to transmit data
4. Program Timeline: When operational, schedule for replenishment
"""

DEFINE_MISSION_CONCEPT = """Define Mission Concept
A. Define data delivery and housekeeping data:
Space vs. ground processing, level of autonomy, central vs. distributed

B. Define tasking, scheduling, and control: LoA, central vs. distributed
C. Define comms architecture: Data rates, bandwidth, timeliness
D. Define preliminary program timeline: 
Replenishment, EoL-options, deployment for multiple sats, flexibility

E. Iterate and document
"""

# Space Environment Summaries

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

# Structure

STRUCTURE_REQUIREMENTS = """Structure reqs
- Mission reqs: Mission life, orbit & Payload specifications
- System reqs: Satellite bus, propulsion, avionics, deplorables
- Structural Subsystem reqs: loads, materials, alignment, mass, CoG

Types of Reqs
- Performance: Pointing, stability, orbit parameters
- Environment: Thermal, outgassing, radiation, loads (static, dynamic)
- Interface: Alignments, mechanical Interface Control Document, CoG, mass
- Programmatic: Schedule and cost
"""

LOADS = """Loads
Static: acceration launch, thermal loads
Dynamic: vibration (rocket), acoustics (random), shock (separation)
"""

STRUCTULAR_CLASSIFICATION = """Structural Classification
Primary: Main load path to launch vehicle, stiff and strong 
(sat bus, launch vehicle adapter)
Secondary: Mounting for payloads, solar arrays, antennas. 
Sub-structures in orbit (appendage booms, support trusses)
Tertiary: monolithic, stiff, posit. stability, sensitive to vibration.
(brackets, component housings)
"""

STRUCTURE_DESIGN_PROCESS = """Structure Design Process
1. Initial Configuration: Conceptual design, system-level.
2. Preliminary Design: Trade studies, material selection.
3. Detailed Analysis: Sizing components, creating drawings.
4. Production: Manufacturing and supply chain.
5. Testing: Qualification, acceptance, and workmanship tests.
"""

MATERIALS_REQUIREMENTS = """Materials reqs
Mechanical Properties: Strength-to-weight ratio
Young's modulus (stiffness), Fatigue resistance

Thermal Properties: Thermal expansion coefficient, thermal conductivity

Env. Resistance: Outgassing, Radiation resistance, Corrosion resistance
"""

STRUCTURE_TESTING = """Structure Testing
Static Load Testing: Applying loads to measure structural response.
Modal Survey: Sine sweep tests to find natural frequencies and damping.
Acoustic Testing: Simulating launch noise in a reverberant chamber.
Random Vibration Testing: Using a shaker to simulate random vibrations.
Shock Testing: Simulating pyrotechnic shocks.
"""

COMMON_MATERIALS = """Common Materials
Aluminium: Lightweight, good conductivity
Titanium: High strength, lower CTE
Polymer composites: Lightweight, customizable: complex (sandwich panels)
Steel and Ni/Cr superalloys: High strength: bolts or high-load structures
Ceramics: Thermal protection systems (TPS)
"""

# Thermal

HEAT_TRANSFER = """Heat Transfer
Conduction: within a material or between materials in contact:
Convection: fluid movement, not present in space:
Radiation: electromagnetic radiation:
"""

RADIANT_ENERGY = """Radiant Energy
- Direct Solar Flux: dependent on distance and orientation:
- Albedo: Reflected solar energy from a planet.
- Planetary Infrared Energy: Infrared radiation from a planet.
- Radiated Energy: Heat emitted from the spacecraft into space.

—> Earth reflects 25-55 percent of the incident solar energy
"""

THERMAL_CONTROL = """Thermal Control
Passive
MLI: Layers of low-emittance film with thermal spacers
Conductive Isolators: Thermal stand-offs made of non-metallic material
Thermal Fillers: Conductive materials between surfaces
Surface Coatings: for specific absorptivity and emissivity
Radiators: External panels to radiate energy (optical solar reflectors)

Active
Heaters: Electrical resistance elements for generating heat
Heat Pipes: transfer heat via a two-phase process using capillary action
"""

# Space Environment

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

