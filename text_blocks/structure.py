
"""
Structure-Related Text Blocks
"""

STRUCTURE_REQUIREMENTS = """Structure reqs
- Mission reqs: Mission life, orbit and Payload specifications
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

STRUCTURAL_CLASSIFICATION = """Structural Classification
Primary: Main load path to launch vehicle, stiff and strong 
(sat bus, launch vehicle adapter)
Secondary: Mounting for payloads, solar arrays, antennas. 
Sub-structures in orbit (appendage booms, support trusses)
Tertiary: monolithic, stiff, posit. stability, sensitive to vibration
(brackets, component housings)
"""

STRUCTURE_DESIGN_PROCESS = """Structure Design Process
1. Initial Configuration: Conceptual design, system-level
2. Preliminary Design: Trade studies, material selection
3. Detailed Analysis: Sizing components, creating drawings
4. Production: Manufacturing and supply chain
5. Testing: Qualification, acceptance, and workmanship tests
"""

MATERIALS_REQUIREMENTS = """Materials reqs
Mechanical Properties: Strength-to-weight ratio
Young's modulus (stiffness), Fatigue resistance

Thermal Properties: Thermal expansion coefficient, thermal conductivity

Env. Resistance: Outgassing, Radiation resistance, Corrosion resistance
"""

STRUCTURE_TESTING = """Structure Testing
Static Load Testing: Applying loads to measure structural response
Modal Survey: Sine sweep tests to find natural frequencies and damping
Acoustic Testing: Simulating launch noise in a reverberant chamber
Random Vibration Testing: Using a shaker to simulate random vibrations
Shock Testing: Simulating pyrotechnic shocks
"""

COMMON_MATERIALS = """Common Materials
Aluminium: Lightweight, good conductivity
Titanium: High strength, lower CTE
Polymer composites: Lightweight, customizable: complex (sandwich panels)
Steel and Ni/Cr superalloys: High strength: bolts or high-load structures
Ceramics: Thermal protection systems (TPS)
"""