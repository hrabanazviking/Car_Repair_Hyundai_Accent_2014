# 2014 Hyundai Accent SE - Ground Points and Ground-Circuit Diagnostics

> **Purpose:** A source-aware reference for diagnosing battery-negative, body, engine, transaxle, module, and sensor ground problems on a U.S.-market 2014 Hyundai Accent SE with the 1.6 L GDI engine and six-speed automatic transmission.
>
> **Core rule:** A component cannot work correctly unless current can return to battery negative through a low-resistance path. Test the ground **under load** before condemning the component.

---

## 1. Scope

This document covers:

- Battery-negative connections
- Body/chassis grounds
- Engine ground cable
- Automatic-transaxle ground cable
- Starter and alternator ground return paths
- Module ground concepts
- Sensor-ground concepts
- Voltage-drop testing
- Resistance testing where appropriate
- Corrosion, looseness, paint, contamination, and damaged terminals
- Intermittent ground faults
- Ground-related false DTCs and code storms
- Field diagnosis for remote/nomad use
- AI/RAG reasoning rules

Related repository files:

- `BATTERY_STARTER_ALTERNATOR.md`
- `../diagnostics/CHARGING_SYSTEM.md`
- `../diagnostics/NO_CRANK.md`
- `../diagnostics/OBD2_GUIDE.md`
- `../specs/FUSES_AND_RELAYS.md`
- `../roadside/EMERGENCY_FIELD_REPAIRS.md`

---

# 2. Confidence Labels

- **VERIFIED - 2014 PARTS CATALOG:** Confirmed in a 2014 Hyundai Accent parts catalog.
- **VERIFIED - HYUNDAI SERVICE FAMILY:** Confirmed in Hyundai service information for the same RB-generation Accent / 1.6 L family, but not treated as exact 2014 VIN-specific ETM data.
- **VERIFIED - HYUNDAI ALL-MODEL TSB:** Hyundai published the procedure for all applicable Hyundai models.
- **GENERAL ELECTRICAL PRACTICE:** Standard diagnostic technique, not an Accent-specific factory specification.
- **UNKNOWN - EXACT 2014 ETM LOCATION:** A physical ground-point code or exact body coordinate has not yet been verified from the exact 2014 Electrical Troubleshooting Manual.

> **Rule:** Do not invent ETM ground designations such as `Gxx`, `GFGxx`, or `GGGxx` unless an exact 2014 Accent ETM source is available.

---

# 3. Why Grounds Matter

Every electrical circuit needs a complete path:

```text
BATTERY +
   ↓
FUSE / RELAY / SWITCH / MODULE
   ↓
LOAD
   ↓
GROUND PATH
   ↓
BATTERY -
```

A bad ground adds resistance to the return path.

The component may then receive apparently correct positive-side voltage but still malfunction because current cannot return properly.

Ground faults can cause:

- Slow or no cranking
- Starter clicking
- Low charging voltage
- Intermittent charging
- Dim or flickering lamps
- MDPS heavy-steering symptoms
- ABS / ESC warnings
- Transmission-control faults
- ECU resets
- Cluster resets
- Relay chatter
- Multiple unrelated DTCs
- U-codes / communication faults
- Sensor readings that appear implausible
- Intermittent no-start or stall
- Heat at cables or terminals

Therefore:

```text
POWER PRESENT
      ≠
CIRCUIT HEALTHY
```

---

# 4. Confirmed 2014 Ground Hardware

The 2014 Hyundai Accent parts catalog identifies dedicated ground wiring for this platform.

## Engine ground cable

**VERIFIED - 2014 PARTS CATALOG**

```text
Hyundai part family: Wiring Assy - Engine Ground
Part number shown: 91860-1R200
```

The catalog lists this as the engine-ground wiring assembly for the 2014 Accent family.

Source:

- https://www.hyundaipartsdeal.com/parts-list/2014-hyundai-accent/electrical/miscellaneous_wiring.html
- https://www.hyundaipartsdeal.com/genuine/hyundai-wiring-assy-eng-grou~91860-1r200.html

## Automatic-transaxle ground cable

**VERIFIED - 2014 PARTS CATALOG**

For the six-speed automatic configuration, the catalog lists:

```text
Hyundai part family: Wiring Assy - T/M Ground
Part number shown: 91860-1R120
Application: 6AT 2WD
```

Source:

- https://www.hyundaipartsdeal.com/parts-list/2014-hyundai-accent/electrical/miscellaneous_wiring.html
- https://www.hyundaipartsdeal.com/genuine/hyundai-wiring-assy-t-m-grou~91860-1r120.html

### Important parts rule

The presence of a catalog part number does not eliminate the need to verify fitment by VIN before ordering.

---

# 5. Battery-Negative Architecture

Hyundai same-generation service information instructs technicians to inspect:

- Battery condition
- Battery electrical connections
- The battery-negative cable connection to the body
- Engine ground cables
- Starter electrical connections

for looseness and corrosion during starting-system diagnosis.

**VERIFIED - HYUNDAI SERVICE FAMILY**

Source:

- https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Starting%20and%20Charging/Starting%20System/Testing%20and%20Inspection/Component%20Tests%20and%20General%20Diagnostics/

A simplified return-path model is:

```text
STARTER / ALTERNATOR / ENGINE LOADS
             ↓
ENGINE OR TRANSAXLE CASE
             ↓
ENGINE / T-M GROUND CABLES
             ↓
BODY / BATTERY-NEGATIVE PATH
             ↓
BATTERY -
```

The starter housing and alternator housing depend on their mechanical mounting to the engine plus the engine/transaxle grounding network.

A corroded strap can therefore imitate:

- Weak battery
- Failed starter
- Failed alternator
- Bad ECU
- Bad transmission controller

---

# 6. Exact Ground-Point Locations

## What is currently verified

The repository can safely state that the 2014 Accent uses:

- Battery-negative wiring
- Dedicated engine-ground wiring
- Dedicated six-speed-automatic transaxle-ground wiring
- Body/chassis ground connections

## What is intentionally not hard-coded yet

The exact 2014 ETM ground-point designations and every physical bolt coordinate remain:

```text
UNKNOWN - EXACT 2014 ETM LOCATION
```

Do not infer them from:

- A different Accent generation
- A different Hyundai model
- An internet diagram without model-year provenance
- A generic code such as `GGG04`, `GGG05`, `GF03`, etc.

When an exact 2014 Accent ETM is available, add a table containing:

| ETM ID | Physical location | Circuits served | Fastener / service note | Source |
|---|---|---|---|---|
| TBD | TBD | TBD | TBD | Exact 2014 ETM required |

---

# 7. Voltage Drop Is the Preferred Ground Test

A cable can look clean and show near-zero resistance with the vehicle off, yet fail when hundreds of amps flow through it.

That is why high-current grounds should be tested **while carrying current**.

## Hyundai all-model voltage-drop guidance

Hyundai Technical Service Bulletin `08-BE-004`, titled **Diagnosis Voltage Drop**, instructs technicians to load the electrical system and voltage-drop test battery cables and grounds.

The bulletin uses:

```text
0.2 V maximum reference
```

for the following high-current ground-path checks:

- Negative battery cable
- Engine-compartment body grounds
- Engine ground straps
- Transmission ground straps

If voltage drop exceeds approximately 0.2 V in those checks, Hyundai directs repair or replacement of the affected cable, terminal, wiring assembly, or strap.

**VERIFIED - HYUNDAI ALL-MODEL TSB**

Source:

- https://charm.li/Hyundai/1995/Accent%20L4-1.5L%20SOHC%20Alpha%20Engine/Repair%20and%20Diagnosis/Starting%20and%20Charging/Power%20and%20Ground%20Distribution/Ground%20Strap/Technical%20Service%20Bulletins/Customer%20Interest/Electrical%20-%20Voltage%20Drop%20Diagnostics/

> The URL is hosted under an older Accent entry, but the bulletin itself states **Model: ALL**. Treat the 0.2 V figure as Hyundai all-model TSB guidance, not as a unique 2014 Accent specification.

---

# 8. How to Voltage-Drop Test a Ground

## Example: engine ground during cranking

1. Confirm battery condition is adequate.
2. Set the DVOM to DC volts.
3. Place the **positive** meter lead directly on the battery negative post, not merely the cable clamp.
4. Place the **negative** meter lead on clean exposed engine metal or the starter housing.
5. Crank the engine.
6. Read the voltage drop while the circuit is loaded.

Conceptually:

```text
BATTERY NEGATIVE POST
        │
      DVOM
        │
ENGINE / STARTER CASE
```

The meter measures voltage being lost across the return path.

### Interpretation

For a high-current ground path:

- Very low drop is desirable.
- A reading approaching or exceeding Hyundai's approximately **0.2 V** service-bulletin threshold deserves investigation.
- A much larger drop strongly suggests resistance in the cable, terminal, connection, mounting surface, or strap.

Do not test a starter ground only with the engine off. The fault may appear only under hundreds of amps of load.

---

# 9. Segment the Ground Path

If total ground-path drop is excessive, divide the path into smaller sections.

Example:

```text
BATTERY NEGATIVE POST
        ↓
NEGATIVE TERMINAL / CLAMP
        ↓
NEGATIVE CABLE
        ↓
BODY ATTACHMENT
        ↓
ENGINE / TRANSAXLE STRAP
        ↓
ENGINE / TRANSAXLE CASE
```

Measure each segment while the same load is active.

The segment with the largest voltage drop contains the excessive resistance.

This prevents replacing an entire cable assembly when the real problem is only:

- Loose bolt
- Corroded eyelet
- Damaged crimp
- Paint/contamination at the designed contact surface
- Broken strands inside a cable

---

# 10. Ground Testing Under Different Loads

Different faults require different loads.

## Cranking complaint

Load source:

```text
STARTER MOTOR
```

Test:

- Battery negative post to engine case
- Battery negative post to transaxle case
- Across engine/transaxle ground straps

## Charging complaint

Load the electrical system with available accessories, for example:

- Headlamps
- Blower
- Rear defogger where appropriate

Then test:

- Alternator housing / engine block to battery negative
- Engine ground cable
- Body ground path

## Intermittent module complaint

Operate the circuit while watching voltage drop and gently moving the relevant harness where safe.

Do not tug near rotating belts, fans, hot exhaust parts, or moving linkage.

---

# 11. Low-Current Module and Sensor Grounds

High-current ground thresholds must not be blindly reused for precision sensor circuits.

Hyundai same-generation diagnostic guidance states that, while operating a circuit, a voltage drop greater than about:

```text
0.1 V in ordinary wiring
50 mV in 5 V circuits
```

may indicate a wiring or connection problem.

**VERIFIED - HYUNDAI SERVICE FAMILY**

Source:

- https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Powertrain%20Management/Computers%20and%20Control%20Systems/Testing%20and%20Inspection/Initial%20Inspection%20and%20Diagnostic%20Overview/

### Why this matters

A 0.15 V ground error may be fairly small in a starter circuit but very significant in a 5 V sensor-reference system.

Therefore:

```text
GROUND TEST LIMIT
DEPENDS ON CIRCUIT TYPE
```

Do not use one universal number for every circuit.

---

# 12. Sensor Ground Is Not Always Chassis Ground

Many engine-management sensors use an ECU-provided low-reference or sensor-ground circuit.

Do **not** assume a sensor-ground wire should be jumpered directly to chassis ground.

Reasons include:

- The ECU may monitor or condition that reference.
- Multiple sensors may share a low-reference circuit.
- A short to chassis can distort several sensor signals.
- Improvised grounds can damage modules or create new faults.

For a sensor problem:

1. Identify the exact wiring diagram.
2. Identify the sensor's power, signal, and low-reference pins.
3. Test the circuit according to the diagram.
4. Do not add a chassis jumper unless the factory circuit specifically calls for chassis ground.

---

# 13. Resistance Testing: Useful but Limited

With power removed and the circuit isolated, resistance testing can find:

- Open cables
- Broken conductors
- Poor continuity
- Short-to-ground conditions

Same-generation Hyundai TCM service information uses:

```text
Below 1 ohm
```

as a ground-circuit continuity specification for the TCM diagnostic procedure.

**VERIFIED - HYUNDAI SERVICE FAMILY**

Source:

- https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Relays%20and%20Modules/Relays%20and%20Modules%20-%20Transmission%20and%20Drivetrain/Relays%20and%20Modules%20-%20A%2FT/Control%20Module/Service%20and%20Repair/Repair%20Procedures/

However:

```text
LOW OHMS WITH NO LOAD
        ≠
GOOD CONNECTION UNDER LOAD
```

A few damaged cable strands can pass a continuity test yet fail during cranking.

Use voltage drop for loaded high-current diagnosis.

---

# 14. Inspection of Ground Connections

Inspect for:

- Loose fastener
- Rust
- White/green corrosion
- Blackened or heat-damaged copper
- Broken strands
- Frayed braid
- Swollen insulation
- Oil saturation
- Coolant contamination
- Evidence of arcing
- Damaged ring terminal
- Poor crimp
- Bent terminal
- Missing fastener
- Non-factory accessories stacked badly on the same ground
- Paint, dirt, sealant, or corrosion where the designed contact interface should be electrically conductive

### Important repair caution

Hyundai TSB `08-BE-004` instructs technicians, during its ground-repair procedure, to clean the harness terminal and threads and specifically says **not to sand or grind body paint away indiscriminately**.

Do not create a new rust path by removing protective coatings beyond what the proper factory-style connection requires.

---

# 15. Ground Fault Symptom Patterns

## Slow crank but battery tests healthy

Check:

1. Battery terminal connection
2. Battery-negative cable
3. Engine/transaxle ground straps
4. Positive starter cable
5. Starter current draw / starter condition

High ground voltage drop can make a good starter behave like a bad starter.

## Charging voltage low at battery but alternator output seems better locally

Suspect:

- Positive B+ path resistance
- Main fuse / connection resistance
- Engine-to-battery negative path resistance

Test both sides under load.

## Random warning lights after starting

Especially after a slow crank, prioritize:

- Battery voltage
- Cable connections
- Engine/body grounds
- Charging-system health

before replacing modules.

## Heavy steering plus battery/charging symptoms

The Accent uses MDPS electric steering.

Low system voltage can reduce electric steering assist.

Check the electrical power and ground system before condemning steering hardware.

## Transmission codes plus unstable voltage

The six-speed automatic depends on stable module supply voltage and ground.

Ground integrity should be checked before treating every transmission-related DTC as internal transaxle failure.

## Multiple unrelated sensor codes

If several sensors become implausible simultaneously:

- Check system voltage.
- Check common power feeds.
- Check shared reference circuits.
- Check ECU grounds.
- Check harness damage.

Do not replace several sensors at once.

---

# 16. Intermittent Ground Faults

Ground faults can be condition-dependent.

They may appear only during:

- Cold starts
- Hot soak
- Rain or humidity
- Road vibration
- Engine movement under torque
- Rough roads
- Heavy electrical load
- High starter current

Useful tests include:

- Voltage-drop testing while the fault is active
- Wiggle testing safely away from rotating/hot parts
- Comparing cold and hot measurements
- Monitoring system voltage with OBD/live data
- Inspecting for cable movement when the engine rocks under load

Do not clear intermittent evidence before recording DTCs and freeze frame.

---

# 17. Field Bypass Test: Diagnostic Use Only

A heavy temporary jumper cable can sometimes be used as a **diagnostic bypass** for a suspected high-current ground path.

Example:

```text
BATTERY NEGATIVE
        ↓
HEAVY JUMPER CABLE
        ↓
CLEAN ENGINE METAL
```

If cranking suddenly improves, the original ground path becomes highly suspect.

### Safety rules

- Use a cable rated for starter current.
- Keep it away from belts, fans, exhaust, and moving linkage.
- Do not attach to fuel-system hardware.
- Do not use sensor wiring as a test ground.
- Do not leave an improvised cable routed permanently through moving or hot areas.

A bypass test is evidence, not the final repair.

---

# 18. Cleaning and Repair Workflow

For a verified serviceable ground connection:

```text
DISCONNECT BATTERY SAFELY
        ↓
REMOVE GROUND FASTENER
        ↓
INSPECT CABLE + EYELET + CRIMP
        ↓
CLEAN APPROPRIATE CONTACT SURFACES
        ↓
REPAIR DAMAGED TERMINAL / CABLE AS NEEDED
        ↓
REASSEMBLE WITH CORRECT FACTORY HARDWARE
        ↓
PROTECT CONNECTION APPROPRIATELY
        ↓
LOAD TEST / VOLTAGE DROP TEST
        ↓
VERIFY SYMPTOM IS GONE
```

Do not merely tighten a visibly heat-damaged cable and call it repaired.

A high-resistance crimp can exist inside intact-looking insulation.

---

# 19. What Not to Do

Do not:

- Replace the ECU because several codes appeared after a weak-battery event.
- Assume shiny cable insulation means the conductor is healthy.
- Diagnose a starter solely from open-circuit battery voltage.
- Diagnose an alternator solely from battery voltage with no cable testing.
- Add random chassis grounds to sensor low-reference circuits.
- Sand large areas of body paint away around a ground.
- Stack many accessory ring terminals under critical factory grounds without engineering the connection.
- Use a tiny wire as a starter-ground bypass.
- Work around belts or the cooling fan with loose jewelry, clothing, or test leads.
- Trust a static resistance test when the failure happens only under load.

---

# 20. Nomad / Primitive-Road Inspection Routine

Before remote travel, periodically inspect:

- Battery terminals tight and clean
- Negative cable secure
- Visible engine ground cable intact
- Visible transaxle ground cable intact
- No frayed braid
- No cable rubbing against sharp metal
- No cable routed near exhaust heat
- No fresh corrosion from water/mud exposure
- No evidence of rodent damage

After a severe underbody strike, mud crossing, water splash, or major road vibration:

1. Inspect accessible cables and harnesses.
2. Check charging voltage.
3. Scan for new DTCs if warning lamps appear.
4. If cranking speed changed, voltage-drop test the ground path.

---

# 21. Minimal Field Diagnostic Kit

Useful items:

- Digital multimeter
- OBD-II scanner
- Heavy jumper cables
- Battery-terminal cleaning tool
- Small wire brush appropriate for terminals
- Electrical contact cleaner
- Flashlight / headlamp
- Basic sockets and wrenches
- Gloves and eye protection
- Dielectric grease for appropriate weather sealing of connectors, **not** as a substitute for clean metal-to-metal high-current contact

---

# 22. AI Diagnostic Rules

An AI assistant using this document should follow these rules:

1. **Do not condemn a component until power and ground are tested.**
2. Prefer voltage-drop testing over unloaded resistance checks for starter, alternator, battery-cable, engine-ground, and transaxle-ground diagnosis.
3. Keep the approximately `0.2 V` Hyundai TSB threshold associated with loaded high-current battery/body/engine/transmission ground checks.
4. Do not apply the `0.2 V` rule blindly to precision 5 V sensor circuits.
5. Do not invent exact 2014 ETM ground-point labels or physical locations.
6. Treat simultaneous unrelated DTCs as possible voltage/ground evidence before recommending multiple component replacements.
7. A good positive-side voltage reading does not prove the ground path is good.
8. A good static continuity reading does not prove the cable can carry starter current.
9. If a temporary heavy ground bypass fixes the symptom, recommend proper cable/terminal diagnosis and permanent repair, not permanent improvised wiring.
10. Record before/after measurements in the service log.

---

# 23. Diagnostic Decision Tree

```text
ELECTRICAL / STARTING / MODULE SYMPTOM
                 ↓
VERIFY BATTERY STATE + SYSTEM VOLTAGE
                 ↓
CHECK TERMINALS VISUALLY
                 ↓
LOAD THE AFFECTED CIRCUIT
                 ↓
MEASURE GROUND VOLTAGE DROP
                 ↓
DROP EXCESSIVE?
      ├─ YES
      │    ↓
      │ SEGMENT THE PATH
      │    ↓
      │ FIND CABLE / EYELET / BOLT / CRIMP FAULT
      │    ↓
      │ REPAIR
      │    ↓
      │ RE-TEST UNDER LOAD
      │
      └─ NO
           ↓
       TEST POSITIVE FEED / CONTROL / COMPONENT
```

---

# 24. Incident Record Template

```yaml
ground_diagnostic:
  date: YYYY-MM-DD
  mileage: null
  symptom: ""
  battery_resting_voltage_v: null
  cranking_voltage_v: null
  charging_voltage_v: null
  loads_active: []
  dtcs:
    stored: []
    pending: []
    permanent: []
  ground_tests:
    - path: "battery negative to engine case"
      operating_condition: "cranking"
      voltage_drop_v: null
      result: "unknown"
    - path: "battery negative to body"
      operating_condition: "loaded engine running"
      voltage_drop_v: null
      result: "unknown"
    - path: "engine/transaxle strap end-to-end"
      operating_condition: "loaded"
      voltage_drop_v: null
      result: "unknown"
  visual_findings: []
  temporary_bypass_test:
    performed: false
    result: ""
  repair_performed: ""
  post_repair_voltage_drop_v: null
  symptom_resolved: null
```

---

# 25. Machine-Readable Ground Profile

```yaml
vehicle_ground_profile:
  vehicle: "2014 Hyundai Accent SE 5-door"
  engine: "1.6L Gamma GDI"
  transmission: "6-speed automatic"
  confirmed_hardware:
    engine_ground:
      part_number: "91860-1R200"
      confidence: "VERIFIED - 2014 PARTS CATALOG"
    automatic_transaxle_ground:
      part_number: "91860-1R120"
      application: "6AT 2WD"
      confidence: "VERIFIED - 2014 PARTS CATALOG"
  diagnostic_thresholds:
    high_current_ground_voltage_drop_v:
      value: 0.2
      relation: "repair concern if greater than"
      source_context: "Hyundai TSB 08-BE-004, model ALL"
    general_wire_voltage_drop_v:
      value: 0.1
      relation: "may indicate problem if greater than"
      confidence: "HYUNDAI SERVICE FAMILY"
    five_volt_circuit_drop_v:
      value: 0.05
      relation: "may indicate problem if greater than"
      confidence: "HYUNDAI SERVICE FAMILY"
    tcm_ground_resistance_ohm:
      value: 1.0
      relation: "below"
      confidence: "HYUNDAI SERVICE FAMILY"
  exact_2014_etm_ground_ids:
    status: "UNKNOWN"
    rule: "do not infer from other model years or Hyundai models"
  preferred_test:
    high_current: "loaded voltage drop"
    low_current: "wiring-diagram-directed voltage drop / continuity"
```

---

# 26. Sources

## Hyundai / Hyundai-derived service information

- 2013 Accent starting-system diagnostics, battery negative/body ground and engine-ground inspection:
  https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Starting%20and%20Charging/Starting%20System/Testing%20and%20Inspection/Component%20Tests%20and%20General%20Diagnostics/

- Hyundai TSB 08-BE-004, Diagnosis Voltage Drop, model ALL:
  https://charm.li/Hyundai/1995/Accent%20L4-1.5L%20SOHC%20Alpha%20Engine/Repair%20and%20Diagnosis/Starting%20and%20Charging/Power%20and%20Ground%20Distribution/Ground%20Strap/Technical%20Service%20Bulletins/Customer%20Interest/Electrical%20-%20Voltage%20Drop%20Diagnostics/

- 2013 Accent general electrical voltage-drop diagnostic guidance:
  https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Powertrain%20Management/Computers%20and%20Control%20Systems/Testing%20and%20Inspection/Initial%20Inspection%20and%20Diagnostic%20Overview/

- 2013 Accent TCM ground inspection:
  https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Relays%20and%20Modules/Relays%20and%20Modules%20-%20Transmission%20and%20Drivetrain/Relays%20and%20Modules%20-%20A%2FT/Control%20Module/Service%20and%20Repair/Repair%20Procedures/

## 2014 parts catalog references

- 2014 Accent miscellaneous wiring, engine ground and 6AT transaxle ground:
  https://www.hyundaipartsdeal.com/parts-list/2014-hyundai-accent/electrical/miscellaneous_wiring.html

- Engine-ground cable 91860-1R200:
  https://www.hyundaipartsdeal.com/genuine/hyundai-wiring-assy-eng-grou~91860-1r200.html

- Automatic-transaxle ground cable 91860-1R120:
  https://www.hyundaipartsdeal.com/genuine/hyundai-wiring-assy-t-m-grou~91860-1r120.html

---

# Core Principle

```text
A COMPONENT WITH POWER
CAN STILL FAIL
IF CURRENT CANNOT GET HOME.

LOAD THE CIRCUIT
→ MEASURE THE DROP
→ FIND THE RESISTANCE
→ REPAIR THE PATH
→ VERIFY UNDER LOAD
```
