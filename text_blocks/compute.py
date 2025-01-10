TESTING = """How to Test
Low-level software (unit, module) and hardware (component, acceptance)
stand-alone functional tests for ground- and space-based systems, 
system integration, testing, and on-orbit calibration
"""

SYSTEM_REQUIREMENTS_DEFINITION = """Compute Requirements Definition
What must the system do? Why must it be done? How can we achieve it 
and what are the alternatives? What functions can we allocate to which 
parts of the system? Are all functions technically feasible?
Is the system testable?
"""

LAYERED_SERVICES = """Layered Services
Standard API for each layer and service.
Encapsulated implementation details.
Allows internal changes without affecting other layers.
"""

BUS_ARCHITECTURE = """Bus Architecture
Standard-sized, message-oriented communication system.
Minimizes interdependencies.
Enables independent testing and plug-and-play capabilities.
"""

CORE_FLIGHT_SYSTEM = """Core Flight System (cFS)
NASA-developed reusable software framework.
Modular architecture for scalability and portability.
"""

COMMONALITY_IN_SOFTWARE_ISSUES = """Commonality Examples Software
Beresheet (Israeli Moon Lander)
A sensor malfunction triggered a software command.
The command unexpectedly shut down the main engine.
The lander crashed due to lack of engine power during descent.
Mars Climate Orbiter
Ground software used imperial units instead of metric.
This mismatch caused incorrect trajectory calculations.
The spacecraft entered Mars atmosphere at the wrong angle
Astro-H
Faulty software misread the satellites rotation.
Attitude control system overcompensated, causing a spin.
Incorrectly configured thrusters worsened the spin, leading to breakup.
"""
