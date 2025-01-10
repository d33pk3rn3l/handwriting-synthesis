COMMUNICATION_TOPOLOGIES = """Communication Topologies
Data Relay: European Data Relay System (EDRS) with 2 GEO satellites
Uses mainly laser terminals, one with RF capability. Lacks global coverage
Direct-to-Earth: High-bandwidth data transfer from LEO.
Feederlinks: High-bandwidth data transfer to remote areas via GEO. (TV)
"""

RF_COMMUNICATION = """RF Communication
Weather independent, suitable for direct communication with end users
Low bandwidth due to lower frequency range (10kHz to 10GHz, with M/Gbps)
Typical specifications: lightweight (a few kg) and around 50W consumption
Requires maintaining a signal-to-noise ratio for communication.
"""

OPTICAL_COMMUNICATION = """Optical Communication
Weather dependent and requires dedicated laser terminals
Provides high bandwidth (100s Gbps) and is undergoing standardization
Operates at ~200 THz frequency range (mostly around 1550nm)
System specifications: heavier (10s of kg to 150kg) with also 50W
Optical SNR is affected by atmospheric conditions and pointing accuracy
"""

MODULATION_TECHNIQUES = """Modulation Techniques
Information over EM waves by modulating a carrier wave with fix freq
Bandwidth: Widthd with sidebands around carrier freq due to modulation
On-Off-Keying (OOK): The bitstream directly multiplies with the carrier
Simple and straightforward but less robust to noise.
Pulse-Position Modulation (PPM)
Encodes chunks with one signal in each chunk
More effective than OOK, with higher energy pulses per bit (better SNR)
Differential Phase Shift Keying (DPSK)
Uses 2 power k states in a constellation diagram, encoding k bits.
Efficient and energy-saving (QPSK offers 2dB gain over OOK).
Implementation is complex and requires advanced equipment.
Simpler forms modify only phase; advanced forms also alter amplitude.
Example: BPSK (Binary Phase Shift Keying) or QPSK (Quadrature PSK)
"""

ERROR_CORRECTION_TECHNIQUES = """Error Correction Techniques
Forward Error Correction (FEC)
Encodes additional bits (checksum) for data verification and correction
error code rate: r = bits_payload / (bits_payload + #bits_redundancy)
Backward Error Correction (BEC): Uses NACKing, two-way comm
Interleaving: Mixes consecutive data chunks with added redundancy.
Allows reconstruction of original data in case of local errors.
Increases latency and requires more memory.
"""
