LAUNCH_VEHICLE_DESIGN = """Propulsion Technologies
Liquid-fueled systems: high efficiency, cryogenic handling
Hypergolic propellants: simple, storable, toxic
Modularity and Scalability
Adaptability for payloads. Example: Ariane 6 modular design
Accuracy Principles
Solid upper stages: less precise than liquid
Long burn stages: less precise than short burn
Smaller engines: more precise than larger ones
"""

VIBRATIONS_AND_STRUCTURAL_CONSIDERATIONS = """Vibrational Loads
Sinusoidal vibrations: narrow-band, engine resonances, structural dynamics
Persistent during entire burn phase
Random vibrations: broad-spectrum, caused by turbulent airflow, combustion
Prominent at liftoff
Dynamic Coupling and Resonance Management
Spacecraft and launch vehicle form a single dynamic system
Resonance occurs when frequencies align
Avoid by designing spacecraft with higher fundamental frequencies
Coupled Load Analysis
Simulate critical resonances and decouple spacecraft from launch vehicle
Acoustic Loads
Engine noise, aerodynamic high acoustic pressures during liftoff, max-Q
Mitigation: Acoustic blankets (Falcon 9: 4-6 dB reduction)
Rules of Thumb
Larger launch vehicles: smaller sinusoidal vibrations
Smaller launch vehicles: smaller acoustic loads
Shock Events During Launch
High to low shocks: spacecraft separation, fairing deployment, stage sep
booster separation, release of hold-down at liftoff
"""

IMPORTANT_FORMULAS_AND_METRICS = """Launch Vehicle Metrics
Payload Fraction: Payload Mass / Total Launch Mass
Evaluates launch efficiency, Cost-per-Kilogram to Orbit
Cost Efficiency: Total Launch Cost / Payload Mass
Key metric improved by reusable rockets
Reliability: Successful Launches / Total Launches
"""
