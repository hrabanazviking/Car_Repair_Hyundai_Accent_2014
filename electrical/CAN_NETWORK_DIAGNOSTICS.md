# 2014 Hyundai Accent SE — CAN Network Diagnostics

> **Purpose:** A practical, offline-first guide to Controller Area Network (CAN) diagnosis for a U.S.-market 2014 Hyundai Accent SE. It is written for humans and for AI/RAG use in the field.
>
> **Core rule:** A communication code does **not** automatically mean the CAN wires are bad, and it does **not** automatically mean the named module has failed. First verify battery/system voltage, scan-tool/DLC power and ground, and the supposedly missing module's own power and ground.

---

## 1. Vehicle Scope

Primary target:

- U.S.-market 2014 Hyundai Accent SE five-door
- 1.6 L GDI engine
- Six-speed automatic transmission where applicable
- ABS / ESC / TCS / VSM
- Motor Driven Power Steering (MDPS / EPS)
- OBD-II diagnostic connector

Hyundai changed network details, module packaging, connector pinouts, and termination locations across years, trims, transmissions, and markets.

Therefore:

> **Do not assume an exact 2012 or 2013 connector pin number, module terminal, splice, or termination-resistor location is automatically identical on a 2014 vehicle.**

This guide uses:

- exact 2014 owner-manual/fuse information where available,
- 2013 Accent service information as close platform evidence,
- 2012 Accent service information as supporting same-generation evidence,
- SAE J1962 for standardized DLC assignments,
- general CAN electrical principles where appropriate.

---

# 2. Confidence / Provenance Tags

Use these tags when reading or extending this file.

- **VERIFIED — 2014 HYUNDAI OWNER DATA**: explicitly documented for the 2014 Accent.
- **VERIFIED — STANDARD**: standardized SAE/ISO connector or network concept.
- **CORROBORATED — 2013 ACCENT SERVICE DATA**: close same-generation service information.
- **CORROBORATED — 2012 ACCENT SERVICE DATA**: same-generation supporting information.
- **GENERAL CAN PRACTICE**: broadly accepted electrical/network diagnostic practice, not an exact Hyundai specification.
- **UNKNOWN EXACT 2014 TOPOLOGY**: do not invent connector pins, splice numbers, terminating-module locations, or full network maps.

Unknown is preferable to a confident wrong answer.

---

# 3. What CAN Does

CAN allows multiple electronic control modules to share information over a small number of wires rather than duplicating individual signal wires between every module.

Examples of information that can be shared include:

- Engine speed
- Accelerator-pedal information
- Requested engine torque reduction
- Transmission state
- Vehicle speed
- Wheel-speed-derived information
- ESC/TCS requests
- Steering-related information
- Warning/status information

Same-generation Hyundai Accent service data explicitly describes CAN communication among powertrain and chassis controllers for engine, transmission, ABS/ESC, and steering-related functions.

Supporting sources:

- 2012 Accent U0101, Lost Communication With TCM:
  https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/A%20L%20L%20%20Diagnostic%20Trouble%20Codes%20%28%20DTC%20%29/Testing%20and%20Inspection/U%20Code%20Charts/U0101/General%20Information/
- 2012 Accent C1687, CAN Time-out MDPS:
  https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/A%20L%20L%20%20Diagnostic%20Trouble%20Codes%20%28%20DTC%20%29/Testing%20and%20Inspection/C%20Code%20Charts/C1687/General%20Information/
- 2012 Accent C1612, CAN Time-out TCM:
  https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/A%20L%20L%20%20Diagnostic%20Trouble%20Codes%20%28%20DTC%20%29/Testing%20and%20Inspection/C%20Code%20Charts/C1612/General%20Information/

---

# 4. Known Network Participants

The exact complete 2014 topology is **not yet locked down** in this repository.

However, the following modules/systems are clearly relevant to the 2014 Accent's electronic architecture and/or same-generation CAN service data:

- ECM / PCM
- Automatic-transmission control function / TCM logic where applicable
- ABS / ESC HECU
- MDPS / EPS control module
- Instrument cluster
- BCM and other body electronics
- Diagnostic scan tool through the DLC

Additional modules may participate depending on equipment and market.

## Important distinction

A module can be:

1. alive and communicating normally,
2. alive but unable to communicate,
3. powered but internally failed,
4. completely unpowered,
5. grounded poorly,
6. connected to a damaged CAN branch,
7. causing the network itself to fail.

A scan tool simply reporting **"no communication"** does not tell you which case applies.

---

# 5. The Two-Wire Differential Bus

**GENERAL CAN PRACTICE / HYUNDAI-SUPPORTED ARCHITECTURE**

High-speed CAN uses two complementary signal wires:

```text
CAN-H
CAN-L
```

They are normally routed as a twisted pair to reject electrical noise.

The receiver looks primarily at the **difference between the two wires**, which helps CAN remain reliable in a noisy automotive environment.

A representative Hyundai waveform description uses a recessive/reference state near 2.5 V and a dominant transition in which CAN-H rises while CAN-L falls. Hyundai service-family references commonly illustrate approximately:

```text
CAN-H dominant: ~3.5 V
CAN-L dominant: ~1.5 V
Reference center: ~2.5 V
```

These are useful waveform concepts, **not exact 2014 Accent pass/fail DC-voltage specifications**.

Do not diagnose CAN by expecting a digital multimeter to display perfect textbook numbers. A DMM averages rapidly changing network activity.

---

# 6. Standard OBD-II / DLC CAN Pins

**VERIFIED — STANDARD, SAE J1962**

For the standardized 16-pin diagnostic connector:

| DLC pin | Standard function |
|---:|---|
| 4 | Chassis ground |
| 5 | Signal ground |
| 6 | CAN-H |
| 14 | CAN-L |
| 16 | Permanent battery positive |

Source:

- SAE J1962 diagnostic-connector standard:
  https://saemobilus.sae.org/standards/j1962_201207-diagnostic-connector-equivalent-iso-dis-15031-3-december-14-2001

The 2013 Accent ABS diagnostic procedure specifically uses:

- DLC terminal 16 for approximately battery-positive voltage,
- DLC terminal 4 for ground continuity,
- DLC terminals 6 and 14 for CAN continuity checks.

Source:

- 2013 Accent ABS/ESC testing:
  https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Brakes%20and%20Traction%20Control/Antilock%20Brakes%20%2F%20Traction%20Control%20Systems/Testing%20and%20Inspection/

---

# 7. 2014 DLC Power Source

**VERIFIED — 2014 HYUNDAI OWNER DATA**

The 2014 Accent owner's manual identifies the **STOP LAMP 15A** interior fuse as protecting several circuits including the **Data Link Connector**.

Therefore, if a scan tool will not power up:

```text
DO NOT BEGIN BY CONDEMNING THE SCAN TOOL OR ECM.
```

Check:

1. battery voltage,
2. DLC pin 16 power,
3. DLC ground,
4. the relevant fuse and feed path,
5. connector condition.

Sources:

- 2014 Accent owner's manual fuse information:
  https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/2/?srch=fuse
- Hyundai 2014 Accent owner's manual mirror:
  https://www.manualslib.com/manual/1067849/Hyundai-2014-Accent.html

---

# 8. First Rule of CAN Diagnosis: Check Voltage First

Low system voltage can generate multiple warning lamps, resets, communication faults, and misleading U-codes.

The 2014 Accent owner's manual specifically notes that a low battery after jump-starting can illuminate the ABS warning lamp without an actual ABS-system failure.

That principle generalizes diagnostically:

```text
LOW VOLTAGE
   ↓
MODULE RESET / BROWNOUT
   ↓
MISSING MESSAGES
   ↓
OTHER MODULES LOG COMMUNICATION CODES
```

Before network diagnosis, record:

- battery open-circuit voltage,
- voltage during cranking if the fault occurs at start,
- charging voltage with engine running,
- whether lights or modules reset/flicker,
- whether the fault followed a dead battery, jump start, charging problem, or battery replacement.

Related files:

- `BATTERY_STARTER_ALTERNATOR.md`
- `GROUND_POINTS.md`
- `WIRING_AND_CONNECTOR_DIAGNOSTICS.md`

---

# 9. A U-Code Is a Witness Statement

A communication DTC often means:

> "The module setting this code did not receive a message it expected."

It does **not** automatically mean:

- the CAN pair is open,
- the named module is internally bad,
- the module that stored the code is bad,
- the harness must be replaced.

Example:

**CORROBORATED — 2012 ACCENT SERVICE DATA**

`U0101` is documented as **Lost Communication With TCM**. The ECM sets it when the expected TCM message is absent.

Source:

https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/A%20L%20L%20%20Diagnostic%20Trouble%20Codes%20%28%20DTC%20%29/Testing%20and%20Inspection/U%20Code%20Charts/U0101/General%20Information/

That missing message could result from:

- TCM/control function not powered,
- TCM ground failure,
- connector problem,
- open CAN branch,
- shorted CAN branch,
- module internal failure,
- broader network collapse,
- severe system-voltage event.

---

# 10. Hyundai Communication-Code Examples

These examples are from same-generation Accent service data and show the **type of logic** Hyundai uses.

Do not assume every code applies identically to every 2014 configuration.

| Code | Same-generation meaning | Diagnostic lesson |
|---|---|---|
| U0101 | Lost communication with TCM | Missing TCM message does not automatically prove failed TCM |
| C1612 | CAN time-out TCM | ABS/ESC HECU can notice missing transmission messages |
| C1687 | CAN time-out MDPS/EPS | ABS/ESC can notice missing steering-module messages |
| C1616 | CAN bus off | Network/controller may have entered bus-off due to communication errors |
| C1605 | CAN hardware error | Internal/network hardware problems are distinct from ordinary time-outs |

Sources:

- U0101:
  https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/A%20L%20L%20%20Diagnostic%20Trouble%20Codes%20%28%20DTC%20%29/Testing%20and%20Inspection/U%20Code%20Charts/U0101/General%20Information/
- C1612:
  https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/A%20L%20L%20%20Diagnostic%20Trouble%20Codes%20%28%20DTC%20%29/Testing%20and%20Inspection/C%20Code%20Charts/C1612/General%20Information/
- C1687:
  https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/A%20L%20L%20%20Diagnostic%20Trouble%20Codes%20%28%20DTC%20%29/Testing%20and%20Inspection/C%20Code%20Charts/C1687/General%20Information/
- C1616:
  https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/A%20L%20L%20%20Diagnostic%20Trouble%20Codes%20%28%20DTC%20%29/Testing%20and%20Inspection/C%20Code%20Charts/C1616/Brake/General%20Information/
- C1605:
  https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/A%20L%20L%20%20Diagnostic%20Trouble%20Codes%20%28%20DTC%20%29/Testing%20and%20Inspection/C%20Code%20Charts/C1605/General%20Information/

---

# 11. Scan the Whole Vehicle, Not Just the Engine

A generic emissions scanner may read engine codes but miss useful communication evidence stored in:

- ABS/ESC,
- EPS/MDPS,
- transmission,
- BCM,
- instrument cluster,
- other manufacturer-specific modules.

When diagnosing a network issue, use a scanner capable of **all-module / enhanced Hyundai diagnostics** if available.

## Record before clearing

For each module:

- Is the module visible/responding?
- Stored DTCs
- Pending/current DTCs
- History DTCs if available
- Communication DTCs
- Voltage-related DTCs
- Timestamp/odometer/environmental data if supported

Do not clear everything before seeing which modules are accusing which other modules.

That relationship is evidence.

---

# 12. Network Pattern Recognition

## Pattern A: One module is missing, everyone else communicates

Example:

```text
ECM     ONLINE
ABS     ONLINE
EPS     ONLINE
CLUSTER ONLINE
TCM     NO RESPONSE
```

Prioritize:

1. TCM/module power,
2. module ground,
3. connector condition,
4. local CAN branch continuity,
5. only then internal module failure.

Do **not** start by replacing the entire harness.

---

## Pattern B: Many modules are missing

Possible causes:

- system voltage too low,
- DLC/scanner power issue,
- CAN-H shorted,
- CAN-L shorted,
- CAN-H shorted to CAN-L,
- one module pulling the network down,
- damaged central/splice area,
- major power/ground distribution problem.

The fault is more likely to be **shared** than five modules failing simultaneously.

---

## Pattern C: Car starts and drives but ABS/ESC/MDPS lights appear together

Possible causes include:

- charging-system/low-voltage event,
- ABS/ESC HECU power/ground fault,
- MDPS/EPS power/ground fault,
- communication timeout,
- shared CAN issue,
- specific sensor/calibration faults unrelated to the physical CAN bus.

Read all modules before deciding.

---

## Pattern D: Problem appears after rough road, rain, repair, or battery work

Prioritize:

- disturbed connector,
- loose ground,
- partially seated connector lock,
- pin backed out of connector,
- chafed harness,
- water intrusion,
- battery-terminal movement,
- harness pulled tight against bracket/edge.

---

# 13. The Correct Diagnostic Order

Use this sequence:

```text
COMMUNICATION FAULT
       ↓
PRESERVE ALL-MODULE DTC EVIDENCE
       ↓
VERIFY BATTERY / CHARGING VOLTAGE
       ↓
VERIFY DLC POWER + GROUND
       ↓
IDENTIFY WHICH MODULES RESPOND
       ↓
IF ONE MODULE IS MISSING:
   CHECK THAT MODULE POWER + GROUND
       ↓
CHECK CONNECTOR / LOCAL CAN BRANCH
       ↓
IF MANY MODULES ARE MISSING:
   CHECK SHARED CAN ELECTRICAL STATE
       ↓
RESISTANCE / SHORT / WAVEFORM TESTING
       ↓
ISOLATE BRANCH OR MODULE IF NECESSARY
       ↓
REPAIR ROOT CAUSE
       ↓
VERIFY NETWORK + CLEAR/RETEST
```

This order prevents expensive module replacement when the real problem is a fuse, ground, connector, or low battery.

---

# 14. CAN Resistance Testing

## 14.1 What approximately 60 ohms means

A conventional two-termination CAN network commonly uses two 120-ohm terminating resistors in parallel:

```text
120 Ω || 120 Ω ≈ 60 Ω
```

Same-generation Hyundai service information supports this concept.

The 2013 Accent ABS diagnostic procedure specifies **60 Ω** in a particular ignition-off test between the relevant cluster CAN terminals.

Source:

https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Brakes%20and%20Traction%20Control/Antilock%20Brakes%20%2F%20Traction%20Control%20Systems/Testing%20and%20Inspection/

The 2012 Accent C1687 description also describes CAN-H/CAN-L with two terminating resistors in the network.

Source:

https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/A%20L%20L%20%20Diagnostic%20Trouble%20Codes%20%28%20DTC%20%29/Testing%20and%20Inspection/C%20Code%20Charts/C1687/General%20Information/

## 14.2 Critical caution

Do **not** create the rule:

```text
DLC 6-to-14 MUST ALWAYS = EXACTLY 60.0 Ω
```

Resistance depends on:

- ignition state,
- which modules/connectors are attached,
- the exact topology,
- where the measurement is taken,
- internal module circuitry,
- vehicle configuration.

Hyundai's own 2013 procedure specifies 60 Ω only under a defined connector/test configuration.

## 14.3 General interpretation heuristic

**GENERAL CAN PRACTICE, NOT AN EXACT HYUNDAI PASS/FAIL TABLE**

With the network fully powered down and measurement conditions known:

- Around 60 Ω may indicate both expected terminations are present.
- Around 120 Ω may suggest one termination/path is missing.
- Very low resistance may suggest a short, extra termination, or module/harness fault.
- Open/infinite resistance may suggest severe open-circuit conditions or an inappropriate measurement configuration.

Always compare against the exact wiring/service procedure before condemning a component.

---

# 15. Power Must Be OFF for Resistance Tests

Never measure resistance on a powered circuit.

Before a CAN resistance test:

1. ignition OFF,
2. allow modules to go to sleep as required,
3. follow the service procedure for battery isolation if required,
4. verify the circuit is not energized,
5. measure only in the configuration specified by the procedure.

Applying an ohmmeter to a live network can produce meaningless results and may damage test equipment.

---

# 16. CAN-H / CAN-L Short Tests

With power safely removed and according to the wiring diagram, check for:

- CAN-H open,
- CAN-L open,
- CAN-H short to CAN-L,
- CAN-H short to ground,
- CAN-L short to ground,
- CAN-H short to B+,
- CAN-L short to B+.

Do not interpret continuity alone as proof that a wire is healthy.

A nearly broken/corroded wire can pass a low-current continuity test yet fail dynamically.

Connector inspection and voltage/waveform testing remain important.

---

# 17. Continuity of an Individual CAN Leg

**CORROBORATED — 2013 ACCENT SERVICE DATA**

Hyundai's ABS diagnostic procedure checks continuity from the ABS-module CAN terminals to DLC pins 6 and 14.

That is strong evidence for a fundamental diagnostic method:

```text
MODULE CAN-H → DLC / known CAN-H point
MODULE CAN-L → DLC / known CAN-L point
```

But exact module terminal numbers must come from the correct 2014 wiring diagram.

The 2013 Accent procedure also uses **below 1 Ω** for certain disconnected point-to-point CAN wiring checks.

This is a wiring-continuity reference under a defined service procedure, not a universal live-network specification.

Source:

https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Brakes%20and%20Traction%20Control/Antilock%20Brakes%20%2F%20Traction%20Control%20Systems/Testing%20and%20Inspection/

---

# 18. Voltage Testing the CAN Pair

A DMM can provide clues but cannot show message integrity.

With a communicating network, both CAN lines carry rapidly changing data.

A meter may display an averaged voltage near the midrange rather than the actual switching waveform.

## Useful DMM questions

- Is one line stuck near ground?
- Is one line stuck near battery voltage?
- Are both lines unexpectedly identical and fixed?
- Is one wire radically different from the other?
- Does the reading change when an affected module is disconnected?

## Do not use this simplistic rule

```text
CAN-H = X.X V
CAN-L = Y.Y V
THEREFORE NETWORK GOOD
```

Correct average voltage does not prove clean timing, amplitude, edges, termination, or message content.

---

# 19. Oscilloscope Diagnosis

An oscilloscope is the best electrical tool for seeing the network actually communicate.

## Preferred setup

Use two channels simultaneously:

- Channel A: CAN-H
- Channel B: CAN-L

Observe:

- complementary switching,
- symmetry,
- dominant/recessive behavior,
- ringing,
- missing transitions,
- one line pinned high/low,
- noise,
- intermittent collapse during wiggle/heat/vibration testing.

A representative Hyundai service-family waveform uses a center near 2.5 V, with CAN-H moving upward and CAN-L moving downward during dominant signaling.

Do not treat those illustration voltages as exact 2014 pass/fail thresholds without the exact service specification.

---

# 20. Bus-Off

CAN controllers include error detection and fault confinement.

If communication errors accumulate severely enough, a controller can enter a **bus-off** condition to stop disrupting the network.

**CORROBORATED — 2012 ACCENT SERVICE DATA**

Hyundai documents `C1616 CAN Bus off` in the Accent ABS/ESC system, with the HECU recognizing a CAN bus-off state.

Source:

https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/A%20L%20L%20%20Diagnostic%20Trouble%20Codes%20%28%20DTC%20%29/Testing%20and%20Inspection/C%20Code%20Charts/C1616/Brake/General%20Information/

Bus-off is a **condition**, not a parts diagnosis.

Possible causes include:

- wiring short/open,
- bad connector,
- electrical noise,
- poor module power/ground,
- failing transceiver/module,
- network topology/termination fault.

---

# 21. Module Power/Ground Before Module Replacement

If one module will not communicate:

## Power checks

Verify all relevant:

- constant B+ feeds,
- ignition-switched feeds,
- fuses,
- relays,
- connector terminal voltage under load.

## Ground checks

Verify:

- ground continuity,
- loaded voltage drop,
- ground eyelets,
- body/engine/transmission ground condition where relevant.

A module that has no power cannot communicate.

A module with a weak ground may communicate intermittently or corrupt the bus.

Related:

- `GROUND_POINTS.md`
- `WIRING_AND_CONNECTOR_DIAGNOSTICS.md`
- `FUSES_AND_RELAYS.md`

---

# 22. 2014 Fuse Relationships Worth Remembering

**VERIFIED — 2014 HYUNDAI OWNER DATA**

Relevant 2014 fuse assignments include:

- `MDPS 80A` engine compartment → EPS control module
- `MDPS 10A` interior → EPS control module
- `ABS 1 40A` → ABS/ESC control module and multipurpose check connector
- `ABS 2 40A` → ABS/ESC control module
- `ABS 10A` interior → ABS/ESC control module and associated circuits
- `ECU 1 30A`
- `ECU 2 10A`
- `ECU 10A` interior
- `STOP LAMP 15A` → includes Data Link Connector

The physical fuse-box label on the actual car outranks a generic table if there is a discrepancy.

Source:

https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/2/?srch=fuse

---

# 23. Isolating a Module That Pulls the Bus Down

This is an advanced procedure.

## Concept

If the entire network is abnormal, one connected module or branch can sometimes drag CAN-H/CAN-L into an unusable state.

A careful technician can isolate branches/modules one at a time and observe whether network resistance or waveform returns to normal.

Hyundai-family service information uses a related strategy: modules are disconnected/connected while CAN waveforms are monitored to identify a module associated with abnormal communication.

Supporting Hyundai-family example:

https://charm.li/Hyundai/2012/Veloster%20L4-1.6L/Repair%20and%20Diagnosis/A%20L%20L%20%20Diagnostic%20Trouble%20Codes%20%28%20DTC%20%29/Testing%20and%20Inspection/U%20Code%20Charts/U0001/Engine/Component%20Inspection/

## Safety / method

1. Preserve DTC evidence first.
2. Ignition OFF before disconnecting control modules unless the exact service procedure says otherwise.
3. Do not hot-unplug modules casually.
4. Disconnect only one logical branch/module at a time.
5. Recheck network resistance/waveform/scan visibility.
6. Reconnect before moving to the next suspect unless the test procedure requires otherwise.
7. Do not condemn a module solely because the network recovers when it is unplugged. Inspect its power, ground, connector, and branch wiring first.

A short in the local harness can disappear when the module connector is unplugged and falsely frame the module.

---

# 24. Intermittent CAN Faults

Intermittent faults are common because CAN wiring and connectors are exposed to:

- vibration,
- heat cycling,
- water,
- salt,
- connector fretting,
- harness tension,
- prior repair damage,
- underhood movement,
- rodent damage,
- rough roads.

## Evidence to record

- hot or cold,
- wet or dry,
- after rain/car wash,
- after rough road,
- turning left/right,
- braking event,
- heavy electrical load,
- engine movement under torque,
- recent battery work,
- recent dashboard/steering/ABS repair.

## Wiggle testing

With the vehicle safely stationary and data/waveform monitored:

- gently move suspect harness sections,
- connector backshells,
- ground paths,
- fuse-box harnesses.

Do not yank wiring or flex delicate pins.

---

# 25. Rough-Road / Nomad Inspection

After a severe washboard road, underbody impact, deep rut, or heavy vibration event:

1. Check battery terminals.
2. Check major grounds.
3. Inspect engine-bay fuse/relay box seating.
4. Inspect ABS/ESC HECU connector area visually.
5. Inspect MDPS-related harness routing around steering-column areas if accessible without disassembly.
6. Inspect lower engine/transmission harness areas for snagging or abrasion.
7. Scan every available module before clearing anything.

Do not crawl under a car supported only by the factory jack.

---

# 26. Communication Fault After Battery Replacement / Jump Start

Possible causes:

- low residual battery voltage,
- poor battery terminal connection,
- ground cable not fully tightened,
- voltage spike/event,
- stored history U-codes from the low-voltage episode,
- module initialization/calibration issue,
- coincidental connector disturbance.

Workflow:

```text
STABILIZE BATTERY / CHARGING VOLTAGE
        ↓
SCAN ALL MODULES
        ↓
SAVE CODES
        ↓
CLEAR ONLY AFTER RECORDING
        ↓
CYCLE / DRIVE AS APPROPRIATE
        ↓
SEE WHAT RETURNS
```

Do not replace modules because of one historical communication-code storm after a dead battery.

---

# 27. Symptoms That May Point Toward CAN / Shared Communication

Possible network-related patterns include:

- multiple unrelated warning lights appearing at once,
- scan tool can communicate with some modules but not others,
- several modules store time-out codes against the same missing module,
- intermittent loss of speed/torque/steering-related shared data,
- ABS/ESC/MDPS interaction faults without clear local sensor failure,
- transmission fail-safe occurring with network codes,
- cluster indications dropping out with communication DTCs.

But each symptom can also have non-network causes.

Use DTC relationships and electrical testing.

---

# 28. Symptoms That Are Often Misdiagnosed as CAN

Before attacking the network, exclude:

- weak battery,
- failed alternator,
- loose battery terminal,
- bad engine/body ground,
- blown module fuse,
- damaged individual sensor circuit,
- failed wheel-speed sensor,
- range-switch fault,
- steering-angle calibration issue,
- local connector problem,
- bad scan-tool adapter.

---

# 29. Scanner Will Not Connect At All

Use this order:

```text
SCANNER DOES NOT POWER?
   ↓
CHECK DLC PIN 16 B+
CHECK DLC GROUND
CHECK STOP LAMP / DLC FEED

SCANNER POWERS BUT NO VEHICLE COMMUNICATION?
   ↓
VERIFY BATTERY VOLTAGE
TRY KNOWN-GOOD SCANNER IF AVAILABLE
CHECK CAN 6/14 ELECTRICAL CONDITION
CHECK MAJOR MODULE POWER/GROUND
SCAN FOR PARTIAL NETWORK ACCESS
```

A powered scanner does not prove the CAN network is healthy.

A dead scanner does not prove the CAN network is dead.

---

# 30. Multiple Modules Blame One Module

This is powerful evidence.

Example:

```text
ABS: lost communication with TCM
EPS: lost communication with TCM
ECM: lost communication with TCM
```

That pattern raises suspicion toward:

- TCM/control-function power,
- TCM ground,
- TCM connector,
- TCM branch wiring,
- TCM itself.

It is less consistent with three unrelated receiving modules failing simultaneously.

Still verify shared power and voltage first.

---

# 31. One Module Blames Many Others

Example:

```text
ABS stores:
- timeout ECM
- timeout TCM
- timeout EPS
```

Prioritize:

- ABS/HECU power,
- ABS/HECU ground,
- ABS connector,
- its CAN connection,
- broader network state.

The observer may be the problem.

Communication DTCs are relational evidence.

---

# 32. Steering / ESC Interaction

Same-generation Accent service data shows VSM interaction between ESC and EPS/MDPS over CAN.

The HECU can send a requested steering torque value to the EPS ECU, which participates in steering control.

Source:

https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/A%20L%20L%20%20Diagnostic%20Trouble%20Codes%20%28%20DTC%20%29/Testing%20and%20Inspection/C%20Code%20Charts/C1687/General%20Information/

Therefore simultaneous ESC/MDPS symptoms can be related through:

- shared CAN communication,
- voltage/power,
- calibration/data dependencies,
- or an individual system fault.

Do not assume both systems independently failed.

---

# 33. ESC / Engine / Transmission Interaction

Same-generation Accent service data explains that ABS/ESC can request engine torque reduction over CAN and can coordinate with transmission control during stability intervention.

Source:

https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/A%20L%20L%20%20Diagnostic%20Trouble%20Codes%20%28%20DTC%20%29/Testing%20and%20Inspection/C%20Code%20Charts/C1612/General%20Information/

This explains why a communication problem can produce symptoms spanning:

- engine torque management,
- shifting/fail-safe,
- ESC/TCS,
- warning lamps.

One network fault can masquerade as several subsystem failures.

---

# 34. Connector Handling Rules

From the general electrical-diagnostics rules in this repository:

- ignition OFF before disconnecting modules unless the service procedure specifically requires otherwise,
- never pull a connector apart by the wires,
- inspect terminal lock and secondary locks,
- do not force oversized meter probes into female terminals,
- do not sand plated electrical terminals,
- back-probe from the harness side when appropriate,
- use fine probes designed for automotive terminals,
- restore weather sealing after repair.

See:

`WIRING_AND_CONNECTOR_DIAGNOSTICS.md`

---

# 35. Repairing CAN Wiring

**GENERAL CAN PRACTICE**

CAN is more sensitive to repair quality than an ordinary lamp wire.

When repairing CAN wiring:

- preserve twisted-pair geometry as much as practical,
- keep untwisted repair length minimal,
- use appropriate automotive wire gauge/type,
- use sealed/approved repair technique in exposed areas,
- avoid long pigtails/stubs,
- route away from ignition/high-current noise sources where the factory did so,
- restore clips and strain relief,
- avoid sharp bends and chafe points.

Exact Hyundai approved splice method should come from the applicable service manual/ETM when available.

---

# 36. What NOT to Do

Do not:

- replace the ECM because a U-code mentions ECM,
- replace the TCM because U0101 exists,
- replace the ABS HECU because several lights are on,
- clear codes before recording them,
- resistance-test a powered bus,
- pierce CAN insulation repeatedly,
- short DLC pins with improvised jumpers,
- connect battery voltage to CAN-H or CAN-L,
- assume every CAN system must measure exactly 60.0 Ω at every point,
- assume averaged DMM voltage proves clean communication,
- use an incandescent test light on a CAN data wire,
- hot-unplug modules casually,
- condemn a module before proving its powers and grounds.

---

# 37. Minimal Field CAN Kit

Useful items:

- quality digital multimeter,
- fused meter leads,
- fine back-probe pins,
- OBD-II scanner capable of Hyundai enhanced/all-module scans,
- known-good basic OBD adapter if practical,
- wiring/connector pick tools,
- contact-safe electrical cleaner,
- flashlight/headlamp,
- inspection mirror,
- notebook/service log,
- exact offline wiring diagrams when obtained.

Advanced:

- two-channel oscilloscope,
- breakout leads / DLC breakout box,
- low-current amp clamp where relevant.

---

# 38. Roadside Decision Tree

```text
MULTIPLE WARNING LIGHTS / U-CODES
             ↓
IS BATTERY / CHARGING VOLTAGE STABLE?
   ├─ NO → fix power problem first
   └─ YES
             ↓
DOES SCANNER POWER AT DLC?
   ├─ NO → check pin 16 / ground / DLC fuse feed
   └─ YES
             ↓
SCAN ALL AVAILABLE MODULES
             ↓
ONE MODULE MISSING?
   ├─ YES → check that module power + ground
   │         ↓
   │       connector / local CAN branch
   └─ NO
             ↓
MANY MODULES MISSING / BUS ABNORMAL?
   ├─ YES → CAN resistance / short / waveform testing
   │         ↓
   │       isolate branch/module carefully
   └─ NO → diagnose the specific non-network fault
```

---

# 39. Verification After Repair

A repair is not complete because the code clears once.

Verify:

1. stable battery/charging voltage,
2. scan communication with all expected modules,
3. no active network DTCs,
4. CAN-related live data appears plausible,
5. warning lamps self-test normally,
6. affected function works,
7. road test under the conditions that originally produced the fault,
8. rescan after the road test.

For intermittent problems, repeat hot/cold or vibration conditions if safe.

---

# 40. AI Diagnostic Rules

An AI using this repository should follow these rules:

1. Treat communication codes as **relationships**, not failed-part labels.
2. Preserve all-module DTC evidence before clearing.
3. Check battery/charging voltage before diagnosing CAN.
4. Verify DLC power/ground before declaring the network dead.
5. If one module is missing, verify that module's power and ground first.
6. If many modules disappear together, search for a shared cause.
7. Never interpret approximately 60 Ω outside the stated test configuration as absolute proof of health.
8. Never resistance-test a live CAN bus.
9. Use an oscilloscope for waveform quality when DMM/resistance testing is inconclusive.
10. Distinguish a module that is not powered from a module whose CAN transceiver has failed.
11. A module unplug test must not be treated as automatic proof that the module itself is defective.
12. Low-voltage code storms should be re-evaluated after system voltage is corrected.
13. Do not invent exact 2014 connector pin numbers, splice IDs, termination-resistor locations, or topology.
14. Preserve CAN twist/repair quality.
15. Verify the repair by rescanning every available module.

---

# 41. Core Diagnostic Doctrine

```text
U-CODE / NO COMMUNICATION
        ↓
WHO REPORTED IT?
        ↓
WHO IS ACTUALLY MISSING?
        ↓
IS SYSTEM VOLTAGE GOOD?
        ↓
DOES THE MISSING MODULE HAVE POWER + GROUND?
        ↓
IS ITS CAN BRANCH ELECTRICALLY INTACT?
        ↓
IS THE WHOLE BUS HEALTHY?
        ↓
ONLY THEN SUSPECT MODULE HARDWARE
        ↓
REPAIR → VERIFY EVERY MODULE
```

Or in one sentence:

> **Power the witnesses before interrogating the network.**

---

# 42. Source Index

## 2014 Hyundai Accent owner information

- Owner manual / fuse tables:
  https://www.manualslib.com/manual/1067849/Hyundai-2014-Accent.html
- Searchable owner-manual mirror:
  https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/2/?srch=fuse

## 2013 Accent service information

- ABS/ESC diagnostic procedure, DLC power/ground, CAN continuity, 60-ohm defined test:
  https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Brakes%20and%20Traction%20Control/Antilock%20Brakes%20%2F%20Traction%20Control%20Systems/Testing%20and%20Inspection/
- Steering-angle sensor / GDS CAN context:
  https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Sensors%20and%20Switches/Sensors%20and%20Switches%20-%20Brakes%20and%20Traction%20Control/Steering%20Angle%20Sensor/Description%20and%20Operation/

## 2012 Accent service information

- U0101 Lost Communication With TCM:
  https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/A%20L%20L%20%20Diagnostic%20Trouble%20Codes%20%28%20DTC%20%29/Testing%20and%20Inspection/U%20Code%20Charts/U0101/General%20Information/
- C1612 CAN Time-out TCM:
  https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/A%20L%20L%20%20Diagnostic%20Trouble%20Codes%20%28%20DTC%20%29/Testing%20and%20Inspection/C%20Code%20Charts/C1612/General%20Information/
- C1687 CAN Time-out MDPS:
  https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/A%20L%20L%20%20Diagnostic%20Trouble%20Codes%20%28%20DTC%20%29/Testing%20and%20Inspection/C%20Code%20Charts/C1687/General%20Information/
- C1616 CAN Bus Off:
  https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/A%20L%20L%20%20Diagnostic%20Trouble%20Codes%20%28%20DTC%20%29/Testing%20and%20Inspection/C%20Code%20Charts/C1616/Brake/General%20Information/
- C1605 CAN Hardware Error:
  https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/A%20L%20L%20%20Diagnostic%20Trouble%20Codes%20%28%20DTC%20%29/Testing%20and%20Inspection/C%20Code%20Charts/C1605/General%20Information/

## Standard

- SAE J1962 diagnostic connector:
  https://saemobilus.sae.org/standards/j1962_201207-diagnostic-connector-equivalent-iso-dis-15031-3-december-14-2001

---

# 43. Machine-Readable Summary

```yaml
vehicle:
  make: Hyundai
  model: Accent
  year: 2014
  trim: SE
  market: US
  engine: 1.6L_GDI
  transmission_target: 6_speed_automatic

network:
  type: CAN
  exact_2014_topology: unknown_pending_ETM
  standardized_dlc:
    pin_4: chassis_ground
    pin_5: signal_ground
    pin_6: CAN_H
    pin_14: CAN_L
    pin_16: battery_positive

known_or_supported_modules:
  - ECM_PCM
  - transmission_control_function
  - ABS_ESC_HECU
  - MDPS_EPS
  - instrument_cluster
  - BCM

2014_fuse_relationships:
  dlc_feed:
    fuse: STOP_LAMP
    amperage_A: 15
  mdps_main_A: 80
  abs1_A: 40
  abs2_A: 40
  ecu1_A: 30
  ecu2_A: 10

same_generation_reference:
  can_defined_test_resistance_ohm: 60
  warning: only_under_defined_service_test_configuration
  individual_can_wire_continuity_reference_ohm: "<1 in defined 2013 Accent ABS test"
  example_codes:
    U0101: lost_communication_with_TCM
    C1612: CAN_timeout_TCM
    C1687: CAN_timeout_MDPS
    C1616: CAN_bus_off
    C1605: CAN_hardware_error

diagnostic_priority:
  - preserve_all_module_DTCs
  - verify_battery_and_charging_voltage
  - verify_DLC_power_ground
  - identify_responding_and_missing_modules
  - verify_missing_module_power_ground
  - inspect_connector_and_local_branch
  - test_bus_resistance_short_conditions
  - scope_CAN_H_and_CAN_L_if_needed
  - isolate_branch_or_module_carefully
  - repair_root_cause
  - rescan_all_modules_and_road_test

prohibitions:
  - do_not_replace_module_from_U_code_alone
  - do_not_measure_resistance_on_powered_bus
  - do_not_apply_B_plus_to_CAN_lines
  - do_not_short_DLC_pins
  - do_not_assume_60_ohm_is_universal
  - do_not_hot_unplug_modules_without_procedure
  - do_not_invent_2014_pinouts_or_termination_locations

core_rule: "Power the witnesses before interrogating the network."
```
