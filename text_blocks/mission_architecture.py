
"""
Mission Architecture and Concept Blocks
"""

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

ALTERNATIVE_ARCHITECTURE_AND_CONCEPT = """Mission Concept vs. Architecture
AA: Selection and combination of fundamental mission elements 
AMC: how those elements work together (data flow, control, communication)

Focus
AA: What is used for the mission (hardware, orbit, etc.)
AMC: How the mission operates (data transmission, task allocation)

Elements
AA: Payload, bus, launch, orbit, comms, ground system, end-user
AMC: Data transmission, task allocation and control, comms arch, timeline

Change
AA: At least one fundamental element is chosen differently 
AMC: New ways of executing the mission (workflows, automation)

Relationship
AA: Elements influence the MC; a new C might need a different A
AMC: The way components interact may require different architecture elem.

Iterative Process
AA: Development can start from an existing architecture and explore 
multiple concepts, or vice versa.
AMC: Same iterative approach
"""

DART_ALTERNATIVE_ARCHITECTURE = """InSight Alternative Architecture
Use a smaller, custom-built lander with RTG power instead of solar panels 
Keep all scientific instruments on the lander deck rather than deploying
Rely on direct-to-Earth communication (no relay orbiter)
Landing site closer to potential tectonic activity, higher landing risk
"""

DART_ALTERNATIVE_MISSION_CONCEPT = """InSIGHT Alternative Mission Concept
Deploy multiple smaller landers across different locations on Mars
Each lander has a basic seismometer to triangulate seismic events
Coordinate data collection via a shared communication protocol
Use orbit-based measurements
"""
