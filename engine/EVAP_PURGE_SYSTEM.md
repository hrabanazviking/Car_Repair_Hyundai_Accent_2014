# 2014 Hyundai Accent SE — EVAP / Purge System

> **Purpose:** A practical, offline-first guide to the evaporative-emissions system on a U.S.-market 2014 Hyundai Accent SE with the 1.6 L GDI engine. Written for both human diagnosis and AI/RAG retrieval.
>
> **Core rule:** An EVAP code does **not** automatically mean “replace the gas cap” or “replace the purge valve.” Preserve the code, identify what the ECM detected, then test the relevant part of the vapor system.

---

## 1. Scope and confidence model

This document covers:

- Fuel-tank vapor handling
- Fuel filler cap and filler-neck sealing
- Charcoal canister
- Purge Control Solenoid Valve (PCSV)
- Canister Close Valve (CCV)
- Fuel Tank Pressure Sensor (FTPS)
- Fuel-tank air filter / vent path
- Vapor hoses, tubes, quick-connects, O-rings, and seals
- EVAP leak testing
- Purge-flow diagnosis
- Hard-start-after-refueling patterns
- Fuel odor complaints
- Common P044x/P045x/P2422-style EVAP faults
- Dust / primitive-road considerations
- AI diagnostic rules

### Confidence tags used here

- **VERIFIED — 2014 PARTS/OWNER DATA:** exact 2014 Accent catalog or owner-manual evidence.
- **SERVICE-FAMILY — 2012/2013 ACCENT 1.6:** same-generation / same-engine Hyundai service information, highly relevant but not silently promoted to exact 2014 shop-manual authority.
- **HYUNDAI TSB — BROADER ACCENT/EVAP:** Hyundai diagnostic bulletin applicable as a system-level reference.
- **GENERAL DIAGNOSTIC PRACTICE:** standard automotive diagnostic reasoning, not a Hyundai-specific specification.
- **UNKNOWN:** exact 2014 value or procedure not yet verified.

Related repository files:

- `../diagnostics/CRANK_NO_START.md`
- `../diagnostics/FUEL_TRIM_DIAGNOSTICS.md`
- `../engine/PCV_CRANKCASE_VENTILATION.md`
- `../engine/GDI_FUEL_SYSTEM.md`
- `../electrical/WIRING_AND_CONNECTOR_DIAGNOSTICS.md`
- `../diagnostics/OBD2_GUIDE.md`
- `../maintenance/MAINTENANCE_SCHEDULE.md`
- `../guides/ROADSIDE_DIAGNOSTIC_TRIAGE.md`

---

# 2. What the EVAP system does

Gasoline evaporates continuously inside the fuel tank. The EVAP system prevents those hydrocarbon vapors from venting directly to atmosphere.

A simplified 2014 Accent vapor path is:

```text
FUEL TANK
   ↓ vapor
VAPOR LINES / TUBES
   ↓
CHARCOAL CANISTER
   ├──────────────→ CCV / AIR FILTER → ATMOSPHERE
   │
   └──────────────→ PCSV → INTAKE MANIFOLD
                              ↓
                           ENGINE
```

The charcoal canister stores fuel vapor when purge is not occurring.

When the ECM decides conditions are appropriate, it commands the **Purge Control Solenoid Valve (PCSV)** to meter stored vapor into the intake manifold so the engine burns it.

During EVAP leak testing, the ECM also uses the **Canister Close Valve (CCV)** and **Fuel Tank Pressure Sensor (FTPS)** to seal and monitor the system.

**SERVICE-FAMILY — Hyundai Accent 1.6:** Hyundai describes the PCSV as a duty-controlled solenoid in the passage between the canister and intake manifold, the FTPS as the pressure/vacuum feedback device for EVAP monitoring, and the CCV as the valve that closes the canister air inlet when the system must be sealed for testing.

Source:

- https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Powertrain%20Management/Emission%20Control%20Systems/Evaporative%20Emissions%20System/Description%20and%20Operation/Schematic%20Diagrams%20And%20Component%20Descriptions/

---

# 3. Verified 2014 hardware anchors

## Purge Control Solenoid Valve

**VERIFIED — 2014 PARTS DATA**

The 2014 Accent GDI catalog identifies a genuine purge control valve:

```text
PCSV / Canister Purge Valve
Part number: 28910-3C200
```

Catalog terminology includes:

- Purge Control Valve
- Purge Solenoid
- Vapor Canister Purge Valve

Source:

- https://www.hyundaipartsdeal.com/oem-2014-hyundai-accent-canister_purge_valve.html

> **Parts rule:** Always verify the VIN before ordering. Catalog supersessions and production changes are possible.

## Charcoal canister

**VERIFIED — 2014 PARTS DATA**

```text
Canister Assembly — Fuel / Vapor Canister
Part number: 31420-1R500
```

This canister is cataloged for 2011–2017 GDI Accent applications, including the 2014 model year.

Sources:

- https://www.hyundaipartsdeal.com/genuine/hyundai-canister-assy-fuel~31420-1r500.html
- https://www.hyundaipartsdeal.com/parts-list/2014-hyundai-accent/engine/fuel_system.html

## Fuel Tank Pressure Sensor

**VERIFIED — 2014 PARTS DATA**

```text
Fuel Tank Pressure Sensor (FTPS)
Part number: 31435-2J000
```

Source:

- https://www.hyundaipartsdeal.com/oem-2014-hyundai-accent-fuel_pressure_sensor.html

## Canister Close Valve / vent-filter hardware

**VERIFIED — 2014 PARTS DATA**

The 2014 GDI parts catalog lists canister-close / filter assemblies including:

```text
31453-3K500
```

and additional production-dependent vent/filter hardware.

The 2014 fuel-system catalog also shows:

```text
Fuel-tank air-filter assembly family
31453-1R100
```

for relevant production ranges.

Because vent/filter hardware can vary by production date, verify by VIN before ordering.

Sources:

- https://www.hyundaipartsdeal.com/oem-2014-hyundai-accent-canister_purge_valve.html
- https://www.hyundaipartsdeal.com/parts-list/2014-hyundai-accent/engine/fuel_system.html

---

# 4. Fuel filler cap matters, but it is not the whole EVAP system

The exact 2014 owner manual says to tighten the fuel cap clockwise until it **clicks one time** and stops turning.

It also warns not to top off the tank after the pump nozzle automatically shuts off.

Source:

- https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/10

A poor cap seal can create an EVAP leak, but so can:

- cracked vapor hose
- damaged quick connector
- split O-ring
- leaking canister
- leaking fuel-pump top plate
- stuck-open PCSV
- CCV that does not seal
- cracked filler neck
- damaged tank seal

Therefore:

```text
EVAP LEAK CODE
      ≠
AUTOMATIC GAS-CAP REPLACEMENT
```

Check the cap first because it is easy, not because it is always the cause.

---

# 5. Do not top off the fuel tank

Hyundai specifically warns against topping off after automatic nozzle shutoff.

Repeated overfilling can force liquid fuel into vapor-system components that are designed primarily to handle vapor.

Possible consequences include:

- saturated charcoal canister
- fuel odor
- purge irregularities
- EVAP leak or flow codes
- difficult refueling
- reduced canister life

**Rule:** Stop fueling when the pump nozzle automatically shuts off.

---

# 6. PCSV: the intake-side gatekeeper

The PCSV is the electrically controlled valve between the charcoal canister and the intake manifold.

Normal simplified logic:

```text
PCSV CLOSED
→ intake manifold isolated from canister

PCSV COMMANDED OPEN
→ engine vacuum draws stored fuel vapor
  from canister into intake manifold
```

The ECM does not simply leave the purge valve fully open. It meters purge according to operating conditions.

## Why a stuck-open purge valve matters

If the PCSV leaks when it should be closed, the intake manifold can receive uncommanded vapor or air.

Potential symptoms:

- rough idle
- unstable fuel trims
- difficult restart after refueling
- rich or lean transient behavior depending on vapor loading
- extended crank
- occasional stall after refueling
- P0441 or related purge-flow fault

A hard-start-after-refueling complaint should therefore move the PCSV high on the suspect list, but not make it an automatic replacement.

### Useful discrimination

```text
HARD START MAINLY AFTER REFUELING
            ↓
CHECK PURGE VALVE SEALING
CHECK CANISTER CONDITION
CHECK EVAP HOSES
CHECK FUEL PRESSURE / GDI DATA
```

Do not skip ignition, fuel-pressure, or mechanical checks merely because the symptom occurs after refueling.

---

# 7. PCSV service-family inspection

**SERVICE-FAMILY — 2012 Accent 1.6**

Hyundai service information instructs technicians to:

1. Turn ignition OFF.
2. Disconnect the PCSV electrical connector.
3. Measure resistance across the PCSV terminals.
4. Compare against the service specification.

The exact numerical resistance value is image-only in the retrieved source and is therefore **not copied into this repository as an exact 2014 value**.

```text
PCSV resistance:
UNKNOWN EXACT 2014 VALUE
```

Same-family service data gives a PCSV bracket-bolt torque of:

```text
9.8–11.8 N·m
7.2–8.7 lb-ft
```

Tag: **SERVICE-FAMILY — not yet exact 2014 shop-manual locked**.

Source:

- https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Powertrain%20Management/Emission%20Control%20Systems/Evaporative%20Emissions%20System/Canister%20Purge%20Control%20Valve/Service%20and%20Repair/

---

# 8. Canister Close Valve (CCV)

The CCV controls the atmospheric vent side of the charcoal canister.

Simplified behavior:

```text
NORMAL VENTING
CCV allows fresh-air path through filter/canister

EVAP LEAK TEST
CCV closes vent path
ECM applies purge vacuum
FTPS watches tank pressure/vacuum
```

If the CCV cannot close, the system may never seal for leak testing.

If it sticks closed or the vent/filter path is blocked, the fuel tank may have difficulty breathing.

Possible symptoms of vent restriction include:

- difficult or slow refueling
- nozzle repeatedly clicking off
- unusual tank vacuum/pressure
- vent-related EVAP DTCs
- P2422 / P0446-family faults

Before condemning the CCV electrically, inspect for:

- mud
- dust
- insects / debris
- kinked vent hose
- clogged vent filter
- physical impact damage

---

# 9. Primitive-road / dusty-road warning

This matters specifically for a travel/nomad Accent.

Hyundai EVAP diagnostic guidance warns that under severe dusty or unpaved-road conditions, the **CCV air filter may require more frequent attention/replacement**.

That is especially relevant after:

- long gravel-road travel
- dry forest roads
- desert dust
- deep roadside powder
- mud around the rear underbody

Source:

- https://charm.li/Hyundai/2010/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Powertrain%20Management/Computers%20and%20Control%20Systems/Technical%20Service%20Bulletins/All%20Technical%20Service%20Bulletins/Emissions%20-%20Supplemental%20EVAP%20System%20Diagnostics/

### Nomad post-dust check

After very dusty primitive-road use:

- inspect the vent/filter area when safely accessible
- check for crushed or packed-mud vapor hoses
- note any new refueling difficulty
- note any new fuel odor
- scan any new EVAP DTC before clearing it

---

# 10. Fuel Tank Pressure Sensor (FTPS)

The FTPS is not a fuel-rail pressure sensor.

It measures the pressure/vacuum behavior of the **fuel tank / EVAP system**.

The ECM uses it to judge whether commanded purge and vent actions produce the expected tank-pressure response.

Therefore:

```text
FTPS DATA
      ↓
TELLS US ABOUT
TANK / EVAP PRESSURE

NOT
GDI RAIL PRESSURE
```

Do not confuse FTPS faults with high-pressure GDI fuel-system faults.

Possible FTPS-related problems include:

- sensor electrical fault
- reference-voltage problem
- ground fault
- signal-circuit fault
- hose/port problem
- real abnormal tank pressure

A plausible-looking sensor value does not prove the physical EVAP system is leak-free.

---

# 11. How Hyundai leak monitoring works

**SERVICE-FAMILY**

Hyundai describes EVAP monitoring broadly as:

1. Confirm test-enabling conditions.
2. Use purge to create vacuum in the EVAP system.
3. Use the CCV to close the atmospheric path.
4. Observe FTPS response.
5. Close purge.
6. Monitor vacuum decay.

Too much vacuum decay indicates leakage.

This is why one EVAP DTC can have many possible physical causes.

---

# 12. Common EVAP DTC families

These are diagnostic families, not guaranteed 2014 code-support promises for every software calibration.

## P0441 — Incorrect purge flow

Hyundai EVAP guidance associates this code with incorrect purge behavior and specifically notes that a PCSV leaking vacuum at idle can set it.

Possible causes:

- PCSV leaking while commanded closed
- PCSV restricted or not flowing when commanded
- reversed/misrouted hoses after repair
- wiring or control fault
- vacuum leak in purge path

## P0442 — Small EVAP leak

Potential causes include:

- cap seal
- small hose crack
- connector/O-ring leak
- canister leak
- fuel-pump top-plate leak
- CCV sealing leak

## P0455 — Large EVAP leak

Think of a large path that prevents the system from sealing or holding vacuum:

- cap missing or grossly loose
- large disconnected hose
- broken vapor line
- open CCV when it should seal
- major canister crack

## P0456 — Very small EVAP leak

A tiny leak can be real and difficult to find visually.

Same-family Hyundai logic identifies P0456 when vacuum decays faster than the calibrated very-small-leak threshold.

## P0446 / P2422 — vent-control / restricted-vent style faults

Possible causes:

- CCV electrical fault
- CCV stuck
- plugged vent filter
- dirt or insect blockage
- kinked vent hose

Source:

- https://charm.li/Hyundai/2010/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Powertrain%20Management/Computers%20and%20Control%20Systems/Technical%20Service%20Bulletins/All%20Technical%20Service%20Bulletins/Emissions%20-%20Supplemental%20EVAP%20System%20Diagnostics/

---

# 13. EVAP leak diagnosis without a parts cannon

Start with the evidence.

```text
EVAP DTC
  ↓
RECORD STORED / PENDING / PERMANENT CODES
  ↓
RECORD FREEZE FRAME
  ↓
INSPECT CAP + FILLER NECK
  ↓
INSPECT VAPOR HOSES / QUICK CONNECTORS
  ↓
CHECK PCSV SEALING + COMMAND
  ↓
CHECK CCV / FILTER / VENT PATH
  ↓
CHECK FTPS PLAUSIBILITY
  ↓
LEAK TEST THE SYSTEM
  ↓
REPAIR ROOT CAUSE
  ↓
VERIFY MONITOR COMPLETION
```

Do not clear codes before preserving freeze-frame evidence.

---

# 14. Visual inspection points

Inspect for:

- fuel cap gasket cuts/hardening
- filler-neck rust or damage at sealing surface
- loose vapor connectors
- cracked plastic vapor tube
- hose chafing
- underbody impact damage
- canister cracks
- mud around canister/CCV
- damaged vent-filter housing
- fuel-pump module/top-plate sealing problems
- recent repair work that may have disturbed hoses

**SERVICE-FAMILY:** Hyundai canister service specifically calls for visual inspection of canister cracks/leakage and loose, distorted, or damaged vapor hose/tube connections.

Source:

- https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Powertrain%20Management/Emission%20Control%20Systems/Evaporative%20Emissions%20System/Evaporative%20Emission%20Control%20Canister/Service%20and%20Repair/

---

# 15. Smoke testing

A proper EVAP smoke test is often the fastest way to find a physical leak.

## Use the right equipment

Use an automotive EVAP leak/smoke machine designed for low-pressure vapor-system testing.

Do **not** improvise by forcing unrestricted shop air into the fuel tank or canister.

Reasons:

- EVAP systems are low-pressure systems
- excess pressure can damage components
- gasoline vapor is flammable
- sparks/open flames are dangerous

### Smoke-test targets

Look for smoke at:

- fuel-cap seal
- filler-neck joints
- vapor hose connections
- quick connectors
- canister seams
- CCV interface
- fuel-pump top plate / tank service interface
- purge-line connections

A smoke test proves a leak location. It does not automatically prove which electrical component caused a code.

---

# 16. Manual vacuum testing

Same-generation Accent service information uses hand vacuum/gauge testing to divide the system into sections.

The logic is powerful even when the exact factory fixtures are unavailable:

```text
DOES VACUUM HOLD IN PURGE LINE?
        ↓
YES / NO
        ↓
DIVIDE SYSTEM
        ↓
CANISTER + CCV SECTION
        ↓
TANK / VAPOR LINE SECTION
        ↓
ISOLATE LEAK
```

Source:

- https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/A%20L%20L%20%20Diagnostic%20Trouble%20Codes%20%28%20DTC%20%29/Testing%20and%20Inspection/P%20Code%20Charts/P0442/System%20Inspection/

---

# 17. Hard start after refueling

This symptom deserves its own branch.

If the vehicle normally starts well but cranks longer, stumbles, or briefly runs poorly immediately after refueling:

```text
AFTER-REFUEL HARD START
        ↓
SCAN FOR EVAP / MIXTURE / MISFIRE DTCs
        ↓
CHECK PURGE VALVE FOR LEAKING OPEN
        ↓
CHECK CANISTER FOR POSSIBLE FUEL SATURATION
        ↓
CHECK TANK VENTING / CCV
        ↓
CHECK GDI RAIL PRESSURE
        ↓
CHECK IGNITION / COMPRESSION IF NEEDED
```

### Why purge matters

A PCSV that fails to seal can allow excessive vapor into the intake during a restart, especially when the canister has just received a large vapor load from refueling.

Do not diagnose by symptom alone. Confirm with scan data, valve testing, and system inspection.

---

# 18. Rough idle / fuel-trim interaction

A purge leak can imitate an intake-system fault.

Possible pattern:

```text
ROUGH IDLE
POSITIVE OR ERRATIC FUEL TRIM
PURGE SYSTEM ACTIVE / LEAKING
        ↓
TEMPORARILY ISOLATE / TEST PURGE PATH
        ↓
DO TRIMS / IDLE NORMALIZE?
```

Do not permanently block the purge system as a “repair.”

Cross-reference:

- `../diagnostics/FUEL_TRIM_DIAGNOSTICS.md`
- `PCV_CRANKCASE_VENTILATION.md`

### PCV versus purge

Both systems connect to the intake side, but they do different jobs.

```text
PCV
→ crankcase vapor management

EVAP PURGE
→ fuel-tank vapor management
```

A vacuum leak diagnosis must distinguish between them.

---

# 19. Fuel odor diagnosis

Fuel odor can come from EVAP leakage, but **raw-liquid fuel leakage is a different and more urgent problem**.

## STOP / DO NOT DRIVE if:

- liquid fuel is visibly leaking
- fuel drips from under the car
- a fuel line is wet under pressure
- fuel is collecting near ignition/exhaust sources

For vapor-only odor with no liquid leak visible:

- inspect cap
- inspect filler neck
- inspect vapor hoses
- inspect canister and connections
- inspect tank top / pump module area if accessible safely
- scan for EVAP codes

Never use a flame to locate a fuel-vapor leak.

---

# 20. Refueling problems

## Nozzle repeatedly clicks off before tank is full

Possible causes:

- restricted vent path
- clogged canister air filter
- stuck-closed CCV
- kinked vapor/vent hose
- saturated canister
- filler-neck issue

Do not force fuel into the tank after repeated early shutoffs.

## Excessive hiss when opening cap

A small pressure/vacuum change can occur normally with temperature and fuel-vapor changes.

But unusually strong recurring pressure/vacuum plus refueling difficulty should raise suspicion of a venting problem.

Hyundai instructs the driver to open the fuel cap carefully and slowly, and to wait if fuel is venting or a hissing sound persists before fully removing the cap.

Source:

- https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/10

---

# 21. Electrical diagnosis

Treat PCSV, CCV, and FTPS like normal controlled electrical components.

Check:

- battery/system voltage
- relevant fuse feeds
- connector condition
- terminal tension
- corrosion or water intrusion
- continuity where appropriate
- shorts to ground
- shorts to power
- ECM control signal
- sensor reference/ground/signal for FTPS

See:

- `../electrical/WIRING_AND_CONNECTOR_DIAGNOSTICS.md`
- `../electrical/GROUND_POINTS.md`

Do not condemn a valve because a scan tool says it was commanded.

A command proves the ECM requested an action, not that the valve physically moved or that wiring delivered the command correctly.

---

# 22. Using a scan tool

Useful EVAP-capable scan-tool functions may include:

- stored/pending/permanent DTCs
- freeze frame
- FTPS data
- commanded purge percentage
- PCSV actuation test
- CCV actuation test
- readiness-monitor state

Not every generic scanner exposes Hyundai-enhanced EVAP controls.

### Commanded versus actual reasoning

```text
ECM COMMANDS PURGE
       ↓
FTPS SHOULD RESPOND APPROPRIATELY
       ↓
NO RESPONSE?
       ↓
PCSV / LINE / CCV / FTPS /
WIRING / SYSTEM LEAK
```

One PID alone is not a diagnosis.

---

# 23. Readiness monitor behavior

After an EVAP repair or code clear, the EVAP monitor may not run immediately.

EVAP tests depend on enabling conditions such as:

- fuel level
- ambient/engine temperature
- operating history
- time since start
- purge conditions

Therefore:

```text
CODE CLEARED
      ≠
REPAIR VERIFIED
```

Verification requires:

1. no returning stored/pending fault
2. no physical leak
3. normal purge/vent behavior
4. EVAP monitor eventually completing when enabling conditions are met

---

# 24. Do not confuse EVAP with GDI fuel pressure

The 2014 Accent has both:

- an EVAP fuel-tank pressure sensor
- a GDI high-pressure fuel rail sensor

These are entirely different systems.

```text
FTPS
→ vapor-system pressure/vacuum

RPS / rail pressure sensor
→ high-pressure gasoline rail
```

A P045x fault is not a high-pressure fuel-pump diagnosis.

Cross-reference:

- `GDI_FUEL_SYSTEM.md`

---

# 25. Canister removal / service reference

**SERVICE-FAMILY — 2013 Accent 1.6**

Hyundai service information shows the canister connected to three functional paths:

```text
A: canister ↔ atmosphere / fuel-tank air filter
B: canister ↔ intake manifold
C: canister ↔ fuel tank
```

Same-family canister fastener torque:

```text
19.6–29.4 N·m
14.5–21.7 lb-ft
```

Tag: **SERVICE-FAMILY — verify exact 2014 procedure before service**.

Source:

- https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Powertrain%20Management/Emission%20Control%20Systems/Evaporative%20Emissions%20System/Evaporative%20Emission%20Control%20Canister/Service%20and%20Repair/

---

# 26. Safety

Gasoline vapor is highly flammable.

## Never:

- smoke while servicing EVAP/fuel components
- use open flame to find a leak
- create sparks near fuel vapor
- deliberately short valve terminals
- pressurize the tank with unrestricted shop air
- open GDI high-pressure fuel components as part of EVAP diagnosis
- crawl under an unsupported vehicle

Use eye protection and fuel-resistant gloves when fuel exposure is possible.

For any actual high-pressure GDI fuel work, follow the residual-pressure-release procedure in `GDI_FUEL_SYSTEM.md`.

---

# 27. Field / roadside triage

Most EVAP faults are **not immediate breakdown faults** if there is no liquid fuel leak, no severe drivability issue, and the vehicle starts/runs normally.

## Usually driveable to repair

Examples:

- loose cap corrected
- isolated EVAP leak code
- small-leak code with normal drivability
- failed readiness monitor

## Stop and reassess

- strong raw-fuel odor
- hard starting severe enough to create stranding risk
- repeated stalling after refueling
- tank strongly pressurized/vacuum-locked with refueling trouble

## Do not continue driving

- visible liquid fuel leak
- fuel dripping near exhaust/electrical sources
- damaged fuel tank
- crash/impact damage to fuel-system components

---

# 28. Diagnostic symptom matrix

| Symptom | High-priority checks |
|---|---|
| P0441 | PCSV sealing, purge command, hoses, wiring |
| P0442 | cap seal, small hose/O-ring leaks, canister, CCV |
| P0455 | cap missing/loose, disconnected hose, large leak, CCV not sealing |
| P0456 | tiny hose/seal/canister/tank-top leak, smoke test |
| P0446/P2422-style vent fault | CCV, vent filter, dirt/mud, kinked hose, wiring |
| Hard start after refueling | PCSV leaking open, saturated canister, venting, then fuel/ignition checks |
| Nozzle repeatedly clicks off | blocked vent/filter, CCV stuck closed, kinked vent hose |
| Fuel odor, no visible liquid | cap, filler neck, vapor lines, canister, tank-top seals |
| Rough idle + purge anomaly | PCSV leak, purge hose, intake interaction, fuel trims |
| Multiple EVAP electrical codes | system voltage, shared power/ground, harness, connectors |

---

# 29. AI / RAG rules

An AI using this file should follow these rules:

1. **Never equate an EVAP code with an automatic gas-cap replacement.**
2. **Never equate P0441 with automatic PCSV replacement.** Test sealing, wiring, command, and hose routing.
3. Treat P0442/P0455/P0456 as leak-size clues, not component names.
4. Distinguish EVAP tank pressure from GDI rail pressure.
5. On hard start after refueling, prioritize purge/canister/vent checks without excluding fuel-pressure, ignition, or mechanical faults.
6. On dusty-road use, include CCV filter/vent restriction in the hypothesis list.
7. If liquid fuel is visible, escalate immediately to a fuel-leak safety condition.
8. Do not use unrestricted compressed air on the EVAP system.
9. Do not open GDI high-pressure lines for EVAP diagnosis.
10. Do not invent exact PCSV resistance, FTPS voltage, or CCV resistance values when exact 2014 data is unavailable.
11. Preserve DTCs, freeze frame, and readiness state before clearing.
12. Confirm repair by both physical testing and monitor behavior.

---

# 30. Core reasoning model

```text
EVAP SYMPTOM / DTC
        ↓
PRESERVE EVIDENCE
        ↓
IS THERE A LIQUID-FUEL SAFETY PROBLEM?
        ↓
CHECK CAP / FILLER / VISIBLE HOSES
        ↓
CLASSIFY FAULT:
LEAK / PURGE / VENT / SENSOR / ELECTRICAL
        ↓
TEST PCSV + CCV + FTPS + VAPOR PATH
        ↓
SMOKE / VACUUM TEST IF NEEDED
        ↓
ISOLATE ROOT CAUSE
        ↓
REPAIR
        ↓
VERIFY DRIVABILITY + EVAP MONITOR
```

---

# 31. Source notes

Primary and supporting references used for this document:

- 2014 Hyundai Accent owner manual fuel-cap/refueling instructions:
  https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/10
- 2014 Accent purge-valve catalog:
  https://www.hyundaipartsdeal.com/oem-2014-hyundai-accent-canister_purge_valve.html
- 2014 Accent fuel-system parts catalog:
  https://www.hyundaipartsdeal.com/parts-list/2014-hyundai-accent/engine/fuel_system.html
- 2014 Accent FTPS catalog:
  https://www.hyundaipartsdeal.com/oem-2014-hyundai-accent-fuel_pressure_sensor.html
- 2012 Accent EVAP system description:
  https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Powertrain%20Management/Emission%20Control%20Systems/Evaporative%20Emissions%20System/Description%20and%20Operation/Schematic%20Diagrams%20And%20Component%20Descriptions/
- 2013 Accent canister inspection/service:
  https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Powertrain%20Management/Emission%20Control%20Systems/Evaporative%20Emissions%20System/Evaporative%20Emission%20Control%20Canister/Service%20and%20Repair/
- 2012 Accent PCSV service:
  https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Powertrain%20Management/Emission%20Control%20Systems/Evaporative%20Emissions%20System/Canister%20Purge%20Control%20Valve/Service%20and%20Repair/
- Hyundai supplemental EVAP diagnostics:
  https://charm.li/Hyundai/2010/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Powertrain%20Management/Computers%20and%20Control%20Systems/Technical%20Service%20Bulletins/All%20Technical%20Service%20Bulletins/Emissions%20-%20Supplemental%20EVAP%20System%20Diagnostics/
- 2012 Accent P0442 system inspection:
  https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/A%20L%20L%20%20Diagnostic%20Trouble%20Codes%20%28%20DTC%20%29/Testing%20and%20Inspection/P%20Code%20Charts/P0442/System%20Inspection/

---

# 32. Machine-readable summary

```yaml
vehicle:
  market: US
  year: 2014
  make: Hyundai
  model: Accent
  trim_focus: SE five-door
  engine: 1.6L GDI

system:
  name: EVAP
  purpose: prevent fuel vapors from escaping and route stored vapor to engine
  primary_components:
    - fuel_tank
    - filler_cap
    - filler_neck
    - vapor_lines
    - charcoal_canister
    - purge_control_solenoid_valve
    - canister_close_valve
    - fuel_tank_pressure_sensor
    - vent_air_filter

verified_2014_parts:
  pcsv:
    part_number: 28910-3C200
    confidence: verified_2014_parts_catalog
  canister:
    part_number: 31420-1R500
    confidence: verified_2014_parts_catalog
  ftps:
    part_number: 31435-2J000
    confidence: verified_2014_parts_catalog
  ccv_filter_family:
    examples:
      - 31453-3K500
      - 31453-1R100
    note: verify VIN and production date

owner_manual:
  fuel_cap:
    instruction: tighten clockwise until one click and stop
  refueling:
    do_not_top_off: true

service_family_values:
  pcsv_bracket_torque_nm: [9.8, 11.8]
  canister_fastener_torque_nm: [19.6, 29.4]
  exact_2014_confirmation_required: true

unknown_exact_2014_values:
  - pcsv_resistance
  - ccv_resistance
  - ftps_voltage_specification

common_fault_families:
  P0441: purge_flow_incorrect
  P0442: small_evap_leak
  P0455: large_evap_leak
  P0456: very_small_evap_leak
  P0446_or_P2422: vent_control_or_restriction_family

nomad_notes:
  dusty_roads_can_clog_vent_filter: true
  inspect_after_heavy_dust_exposure: true

hard_stop_conditions:
  - visible_liquid_fuel_leak
  - damaged_fuel_tank
  - fuel_near_ignition_or_exhaust_source

ai_core_rule: >-
  Preserve evidence, distinguish leak/purge/vent/sensor/electrical faults,
  test the system, and never replace a cap or purge valve merely because
  an EVAP DTC is present.
```
