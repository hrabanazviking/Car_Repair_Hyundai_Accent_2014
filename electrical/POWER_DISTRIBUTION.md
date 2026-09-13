# Power Distribution and Fuse-Feed Diagnostics

**Vehicle focus:** 2014 Hyundai Accent SE, U.S.-market five-door, 1.6L Gamma GDI, 6-speed automatic

**Purpose:** Provide a source-aware diagnostic map for tracing electrical power from the battery to the vehicle's major loads without guessing, bypassing fuses, or replacing modules before proving that they are actually receiving clean power and ground.

> **Core rule:** A dead component is not automatically a failed component. First prove that battery power, switched power, fuse protection, relay control, and ground all reach it correctly under load.

---

## 1. Scope and provenance

This guide combines:

- exact 2014 Accent owner-manual fuse-panel data;
- same-generation Hyundai service-family starting-system diagnostics;
- general electrical diagnostic principles already used elsewhere in this repository;
- explicit uncertainty tags where exact 2014 wiring-diagram pinouts are not yet available.

### Source priority

1. **Exact 2014 Hyundai owner information** for fuse ratings, protected circuits, fuse-replacement rules, and panel location.
2. **Same-generation Hyundai service information** for diagnostic logic such as ignition-switch, starter-relay, and circuit-isolation workflow.
3. **General electrical principles** for loaded voltage-drop testing and relay logic.

If the physical fuse-box label on the car disagrees with a generic table, use the **physical vehicle label** for that car.

---

## 2. High-level power architecture

A useful simplified model is:

```text
BATTERY POSITIVE
      |
      +--> MAIN / MULTI-FUSE BLOCK
      |       |
      |       +--> ALT 125A path
      |       +--> MDPS 80A
      |       +--> ABS feeds
      |       +--> blower / rear defog feeds
      |
      +--> ENGINE-ROOM FUSE / RELAY BOX
      |       |
      |       +--> IG1 40A
      |       +--> IG2 40A
      |       +--> ECU1 30A
      |       +--> C/FAN 40A
      |       +--> B+1 / B+2 50A feeds
      |       +--> engine-control branch fuses
      |
      +--> INTERIOR / I-P JUNCTION BOX
              |
              +--> ACC / IG1 / IG2 branches
              +--> lighting / cluster / BCM branches
              +--> power window / lock / accessory branches
```

This is a **functional map**, not a substitute for the exact Hyundai ETM wiring diagram.

---

## 3. Exact 2014 engine-compartment power feeds

The 2014 Hyundai owner manual lists the following major engine-compartment feeds.

### Multi-fuse / high-current section

| Fuse | Rating | Primary protected load / branch |
|---|---:|---|
| ALT | 125 A | Alternator and engine-room fuse/relay box high-current feed |
| MDPS | 80 A | Electric power steering control module |
| BLOWER | 40 A | Blower relay circuit |
| RR HTD | 40 A | Rear-defogger relay feed through I/P junction box |
| ABS 1 | 40 A | ABS / ESC branch |
| ABS 2 | 40 A | ABS / ESC branch |
| B+1 | 50 A | Interior junction-box branch including room/audio/tail-related loads |

### Main cartridge / blade branch fuses

| Fuse | Rating | Primary protected load / branch |
|---|---:|---|
| IG2 | 40 A | Start relay and ignition-switch branch |
| IG1 | 40 A | Ignition-switch branch |
| ECU 1 | 30 A | ECU2 fuse and engine-control relay branch |
| C/FAN | 40 A | Cooling-fan high / low relay feeds |
| B+2 | 50 A | Interior junction-box branch including locks, hazard, sunroof, power-window relay |
| HORN | 10 A | Horn relay circuit |
| F/PUMP | 15 A | Fuel-pump relay circuit |
| H/LAMP RH | 10 A | Right headlamp |
| H/LAMP LH | 10 A | Left headlamp |
| INJECTOR | 15 A | ECM/PCM, both OCVs, O2 sensors, fuel-pump-relay control-related branch |
| SENSOR | 10 A | ECM/PCM, purge valve, VIS solenoid, canister-close valve, immobilizer, A/C and fan relay control circuits |
| ECU 2 | 10 A | ECM / PCM feed |
| IGN COIL | 15 A | Ignition coils 1-4 and condenser |
| B/UP LAMP | 10 A | PCM, range switch, cluster, rear lamps, shifter illumination branch |
| WIPER | 10 A | ECM/PCM, multifunction switch, front wiper motor branch |

### Important consequence

A single upstream fuse can disable **multiple apparently unrelated systems**.

Example:

```text
INJECTOR fuse opens
      |
      +--> OCVs lose feed
      +--> O2 sensor branch loses feed
      +--> fuel-pump relay branch affected
      +--> ECM/PCM related symptoms may appear
```

Therefore:

> **Several simultaneous codes or dead loads do not automatically mean several failed parts. Look for a shared feed first.**

---

## 4. Interior fuse panel as the second half of the map

The 2014 Accent has two main fuse panels:

1. driver-side interior panel;
2. engine-compartment panel.

Hyundai specifically says that if the electrical system is not operating, the driver-side panel should be checked first.

Useful exact 2014 interior examples include:

| Fuse | Rating | Example protected loads |
|---|---:|---|
| ACC | 10 A | Audio and power mirror switch |
| STOP LAMP | 15 A | Stop-lamp switch, battery sensor, stop relay / related branch, DLC-related branch |
| CLUSTER | 10 A | Instrument cluster and BCM |
| IG1 | 10 A | Several switched accessories including TPMS module and EPS-related low-current control feed |
| ABS | 10 A | ABS/ESC control-related low-current branch |
| ECU | 10 A | ECM / PCM low-current feed |
| IG2 | 10 A | A/C control, BCM and wiper-control branch |
| HAZARD | 15 A | Hazard relay and switch |

Do not assume the printed manual table exactly matches every option package. Hyundai says to verify the **actual fuse-panel label on the vehicle**.

---

## 5. Power-state logic

Think in electrical states instead of component names.

### Constant battery power

Some circuits are fed regardless of ignition-switch position.

Use this when diagnosing:

- hazard lamps;
- memory circuits;
- certain BCM functions;
- door-lock / room-lamp branches;
- diagnostic connector power;
- main high-current feeds.

### ACC power

ACC powers selected convenience loads without placing the entire powertrain into RUN.

Typical symptoms of a failed ACC feed:

- radio dead;
- accessory outlet branch dead;
- mirror control dead;
- unrelated engine systems still normal.

### IG1 / RUN power

IG1 powers modules and controls expected while the vehicle is operating.

A lost IG1 branch can create:

- multiple warning lamps;
- modules offline;
- no communication with certain controllers;
- engine-control or body-control anomalies.

### IG2 / START-support power

The exact 2014 engine-room fuse table shows the 40 A **IG2** fuse feeding the start relay and ignition switch.

A no-crank condition therefore belongs in a power-distribution diagnostic path before starter replacement.

---

## 6. Diagnostic hierarchy for a dead electrical load

Use this sequence.

```text
1. IDENTIFY WHAT IS DEAD
2. IDENTIFY WHAT STILL WORKS
3. FIND THE SHARED FEED
4. VERIFY BATTERY VOLTAGE
5. VERIFY FUSE POWER ON BOTH SIDES
6. VERIFY RELAY INPUTS
7. VERIFY LOAD-SIDE VOLTAGE
8. VERIFY GROUND UNDER LOAD
9. TEST THE COMPONENT
10. REPAIR ROOT CAUSE
11. VERIFY OPERATION
```

### Why "what still works" matters

Suppose the engine cranks but will not start.

If the starter operates normally, then:

- the battery can deliver at least substantial current;
- the starter high-current path is not completely open;
- the ignition-switch/start branch is at least partially functional.

That does **not** prove ECU, fuel-pump, injector, ignition-coil, or sensor feeds are present.

Now examine the next shared branches instead of blaming the battery again.

---

## 7. Fuse testing: do not rely only on eyesight

A fuse can look intact yet still suffer:

- poor blade contact;
- corrosion;
- heat damage;
- cracked element not obvious through plastic;
- loose terminal tension in the fuse box.

Preferred checks:

### Key-off continuity check

With the circuit safely de-energized:

- remove fuse;
- measure resistance / continuity;
- verify element integrity.

### Key-on voltage check

For many circuits, a faster test is to probe the fuse's exposed test points.

Expected patterns:

| Input side | Output side | Meaning |
|---|---|---|
| battery voltage | battery voltage | fuse powered and passing current path |
| battery voltage | 0 V | open fuse or poor contact |
| 0 V | 0 V | upstream feed missing |

This test is especially powerful because it distinguishes:

```text
BAD FUSE
from
NO POWER REACHING THE FUSE
```

---

## 8. Never up-rate a fuse

The 2014 owner manual is explicit:

- replace with the **same rating**;
- do not substitute wire or foil;
- do not install a higher-amperage fuse;
- repeated blowing means the underlying electrical fault must be found.

The fuse protects the **wire**, not just the load.

Oversizing a fuse can turn:

```text
SHORT CIRCUIT
     |
     v
CONTROLLED FUSE FAILURE
```

into:

```text
SHORT CIRCUIT
     |
     v
OVERHEATED HARNESS
     |
     v
MELTED INSULATION / FIRE
```

---

## 9. Multi-fuse safety

The exact 2014 manual gives special handling rules for the high-current multi-fuse assembly.

Before removing it:

1. ignition OFF;
2. electrical loads OFF;
3. disconnect the battery negative terminal.

Hyundai warns against casually disassembling / reassembling bolted multi-fuse connections because incomplete fastening can create a fire risk.

### Repository rule

> **A blown multi-fuse is not a roadside invitation to improvise with metal straps, wire, coins, foil, or oversized protection.**

If a 125 A, 80 A, 50 A, or 40 A high-current link has opened, determine why before restoring the circuit.

---

## 10. Loaded voltage-drop testing

Continuity tests can lie when a circuit carries real current.

A corroded cable may show almost zero resistance on a meter with no load, then lose several volts when the starter, blower, EPS, or cooling fan draws current.

### Positive-side test

For a high-current circuit:

```text
meter red  -> battery positive
meter black -> load positive terminal
operate load
```

The meter displays how much voltage is being **lost in the positive path**.

### Ground-side test

```text
meter red   -> load ground / case
meter black -> battery negative
operate load
```

The meter displays how much voltage is being **lost in the ground path**.

Cross-reference:

- `electrical/GROUND_POINTS.md`
- `electrical/BATTERY_STARTER_ALTERNATOR.md`
- `electrical/WIRING_AND_CONNECTOR_DIAGNOSTICS.md`

### High-current ground anchor

Hyundai service information used elsewhere in this repository treats roughly **0.2 V loaded drop** on major battery-to-body / engine ground paths as a repair-level concern.

Do not blindly apply that same number to precision 5 V sensor circuits.

---

## 11. Relay logic

A relay normally has two sides:

### Control side

The coil needs:

- power;
- ground or ECM/BCM-controlled ground;
- valid command conditions.

### Load side

The switched contacts need:

- battery / fused input power;
- good contact resistance;
- intact output wiring to the load.

### Relay diagnostic ladder

```text
LOAD DEAD
   |
   +--> Is relay commanded?
   |       |
   |       +--> NO -> check command conditions / control circuit
   |       |
   |       +--> YES
   |              |
   |              +--> Is fused power present at relay input?
   |              |
   |              +--> Does output become powered when commanded?
   |              |
   |              +--> Does power reach the load?
   |              |
   |              +--> Is the load ground good?
```

A clicking relay does **not** prove the contacts are passing current.

---

## 12. Starter power-distribution example

Same-generation Hyundai starting-system diagnostics provide a good model for the whole car.

If the starter will not crank:

1. verify battery condition and connections;
2. verify Park / Neutral logic on automatic transmission;
3. verify starter main B+ feed;
4. verify starter S-terminal control signal;
5. if the starter works when control power is correctly applied, inspect upstream wiring;
6. inspect the path through the under-dash junction box, ignition switch, range-switch circuit, and starter relay.

Cross-reference:

- `diagnostics/NO_CRANK.md`
- `electrical/BATTERY_STARTER_ALTERNATOR.md`

The lesson is broader than the starter:

> **Do not condemn the load until the circuit feeding the load has been proven.**

---

## 13. ECU / engine-management shared-feed logic

The 2014 engine-room fuse table gives several important engine-management branches:

```text
ECU 1 30A
  |
  +--> ECU 2 branch
  +--> engine-control relay

ECU 2 10A
  +--> ECM / PCM

IGN COIL 15A
  +--> ignition coils 1-4

INJECTOR 15A
  +--> OCVs
  +--> O2-sensor branch
  +--> fuel-pump-relay-related branch
  +--> ECM/PCM-related feed

SENSOR 10A
  +--> ECM/PCM
  +--> purge valve
  +--> variable-intake solenoid
  +--> canister-close valve
  +--> immobilizer branch
  +--> fan / A-C relay-control branches
```

### Diagnostic implication

If multiple engine-control devices fail together:

```text
DO NOT START WITH:
"Which three sensors failed?"

START WITH:
"What fuse, relay, power feed, or ground do these devices share?"
```

---

## 14. Cooling-fan branch

The exact 2014 engine-compartment table shows:

- **C/FAN 40 A**;
- high-speed fan relay branch;
- low-speed fan relay branch;
- SENSOR 10 A involvement in relay-control circuits.

If the fan does not run during an overheating diagnosis, check:

1. battery voltage;
2. C/FAN fuse;
3. SENSOR branch;
4. fan relay command;
5. relay contact output;
6. fan motor power and ground;
7. ECM command conditions / ECT data.

Cross-reference:

- `engine/COOLING_SYSTEM.md`
- `diagnostics/OVERHEATING.md`

Do not jump straight to a fan-motor replacement.

---

## 15. MDPS power branch

The 2014 engine-room table gives the EPS / MDPS module an **80 A high-current feed**.

The interior panel also contains a lower-current MDPS / ignition-related branch.

This is important because steering assist depends on more than one electrical condition.

If steering suddenly becomes heavy:

```text
CHECK SYSTEM VOLTAGE
      |
CHECK 80A MDPS FEED
      |
CHECK LOWER-CURRENT CONTROL / IG FEEDS
      |
CHECK GROUNDS
      |
SCAN EPS MODULE
      |
THEN CONSIDER MDPS HARDWARE
```

Cross-reference:

- `suspension-steering/STEERING_SUSPENSION.md`
- `electrical/GROUND_POINTS.md`
- `diagnostics/CHARGING_SYSTEM.md`

---

## 16. Low voltage can create fake complexity

A weak battery, loose terminal, poor ground, failing alternator, or bad main feed can create:

- multiple U-codes;
- EPS warnings;
- ABS/ESC warnings;
- transmission faults;
- sensor plausibility faults;
- communication dropouts;
- intermittent relay chatter;
- no-start or stall symptoms.

Therefore:

```text
MULTIPLE MODULE FAULTS
        |
        v
VERIFY SYSTEM VOLTAGE FIRST
        |
        v
VERIFY MAIN POWER + GROUNDS
        |
        v
THEN DIAGNOSE INDIVIDUAL MODULES
```

Cross-reference:

- `diagnostics/CHARGING_SYSTEM.md`
- `electrical/CAN_NETWORK_DIAGNOSTICS.md`

---

## 17. Parasitic-current and parked-vehicle logic

The Accent includes a memory-fuse strategy for long-term parking.

Do not confuse:

```text
NORMAL KEEP-ALIVE LOAD
```

with:

```text
ABNORMAL PARASITIC DRAW
```

A proper parasitic-draw test requires:

- battery fully charged;
- doors / hatch latched or switches simulated closed;
- modules allowed to time out / sleep;
- ammeter connected correctly;
- fuses removed one at a time only after the baseline draw is established.

Cross-reference:

- `electrical/BATTERY_STARTER_ALTERNATOR.md`

Do not pull high-current fuses under load through a meter connected in series.

---

## 18. Power-distribution symptom patterns

### Entire car electrically dead

Check first:

- battery state of charge;
- battery terminal integrity;
- battery ground path;
- main positive cable;
- multi-fuse / main-feed integrity.

### Cranks but will not start

Check:

- ECU1 / ECU2;
- IGN COIL;
- INJECTOR;
- SENSOR;
- F/PUMP;
- engine-control relay;
- live-data communication.

Then continue into:

- `diagnostics/CRANK_NO_START.md`

### No crank, dash powers normally

Check:

- IG2 high-current branch;
- starter relay;
- range-switch logic;
- ignition-switch command;
- starter S-terminal signal.

### Several unrelated systems fail together

Look for:

- B+1 / B+2 shared branch;
- IG1 / IG2 shared branch;
- loose fuse-box feed;
- battery / ground problem;
- water intrusion in fuse / junction boxes.

### Fuse repeatedly blows

Stop replacing it repeatedly.

Investigate:

- wire chafing;
- water intrusion;
- shorted motor or solenoid;
- melted connector;
- crushed harness;
- incorrect previous repair;
- internal component short.

---

## 19. Water intrusion and fuse-box protection

The 2014 owner manual specifically warns that the engine-compartment fuse-panel cover must be securely reinstalled because water contact can produce electrical failures.

After:

- heavy rain;
- engine-bay washing;
- deep standing water;
- underhood repair;
- off-road splash exposure;

inspect for:

- water tracks;
- green corrosion;
- white oxide deposits;
- overheated terminals;
- pushed-back terminals;
- loose fuses;
- damaged cover seal.

A wet junction box can produce intermittent faults that masquerade as module failure.

---

## 20. Field-safe electrical stabilization

Potentially acceptable temporary actions:

- reseat a properly rated fuse;
- replace a blown fuse with the **same rating** after the cause has been reasonably assessed;
- clean / tighten accessible battery terminals;
- secure a chafing harness away from a sharp edge after confirming conductor integrity;
- repair a low-current wire with a mechanically and electrically sound temporary splice until permanent repair;
- protect an exposed connector from water after inspection.

Never use:

- foil around a fuse;
- wire instead of a fuse;
- larger fuse as an experiment;
- screws or metal objects inserted into fuse sockets;
- unfused jumper wires across high-current circuits;
- bypassed ABS / EPS / airbag protection;
- improvised multi-fuse bridges.

---

## 21. Nomad / rough-road inspection priorities

For primitive-road travel, vibration and dust become part of electrical maintenance.

Periodically inspect:

- battery hold-down;
- terminal tightness;
- engine and chassis grounds;
- engine-room fuse-box cover seating;
- harnesses near brackets and sharp edges;
- lower engine harnesses after underbody contact;
- wheel-speed-sensor wiring;
- exposed connectors near splash zones;
- accessory wiring added by the owner.

### After a hard underbody strike

Before blaming electronics, inspect for:

- pinched harnesses;
- pulled grounds;
- damaged sensor wiring;
- cracked connectors;
- blown branch fuses.

---

## 22. Accessory-installation rule

Any added electrical equipment should have:

- an appropriately sized fuse close to its power source;
- correct conductor gauge;
- strain relief;
- abrasion protection;
- secure ground;
- routing away from exhaust, belts, sharp edges, and moving suspension;
- no dependence on stuffing bare wires into OEM fuse sockets.

For higher-current camping / nomad loads, use a dedicated fused auxiliary distribution strategy rather than piggybacking major loads onto unknown factory accessory circuits.

---

## 23. AI diagnostic rules

When an AI system uses this file, it should follow these rules:

1. A DTC does not prove a module has failed.
2. A dead load does not prove the load itself has failed.
3. Check battery voltage before interpreting clusters of electrical codes.
4. Identify all dead systems and all working systems.
5. Search for shared power feeds and shared grounds.
6. Verify power **on both sides of the fuse**.
7. Test relay control and load sides separately.
8. Prefer loaded voltage-drop testing over unloaded continuity for high-current circuits.
9. Never recommend a larger fuse.
10. Never recommend bypassing a fuse as a field repair.
11. Treat the physical fuse-box label as vehicle-specific authority if it differs from a generic table.
12. Preserve uncertainty where an exact 2014 ETM pinout has not been verified.

---

## 24. Power-distribution diagnostic template

```yaml
power_distribution_diagnosis:
  vehicle: "2014 Hyundai Accent SE 1.6 GDI 6AT"
  symptom: ""
  battery_resting_voltage: null
  battery_loaded_voltage: null
  charging_voltage: null

  systems_working: []
  systems_dead: []

  suspected_shared_feed: ""

  fuses_checked:
    - name: ""
      rating_amps: null
      input_voltage: null
      output_voltage: null
      result: ""

  relays_checked:
    - name: ""
      coil_power: null
      coil_control: null
      contact_input_voltage: null
      contact_output_voltage: null
      result: ""

  voltage_drop_tests:
    - path: ""
      load_active: false
      drop_volts: null
      result: ""

  grounds_checked: []
  connectors_checked: []
  harness_damage_found: []
  water_intrusion_found: false

  root_cause: ""
  repair: ""
  verification: ""
  confidence: "low | medium | high"
```

---

## 25. Quick-reference flow

```text
ELECTRICAL SYMPTOM
        |
        v
CHECK BATTERY VOLTAGE
        |
        v
IDENTIFY DEAD + WORKING SYSTEMS
        |
        v
FIND SHARED FEED / GROUND
        |
        v
CHECK UPSTREAM MAIN FUSE
        |
        v
CHECK BRANCH FUSE ON BOTH SIDES
        |
        v
CHECK RELAY COMMAND + OUTPUT
        |
        v
CHECK LOAD VOLTAGE UNDER LOAD
        |
        v
CHECK GROUND VOLTAGE DROP
        |
        v
CHECK HARNESS / CONNECTORS
        |
        v
ONLY THEN TEST / REPLACE LOAD
```

---

## 26. Cross-links

Use this guide with:

- `specs/FUSES_AND_RELAYS.md`
- `electrical/BATTERY_STARTER_ALTERNATOR.md`
- `electrical/GROUND_POINTS.md`
- `electrical/WIRING_AND_CONNECTOR_DIAGNOSTICS.md`
- `electrical/CAN_NETWORK_DIAGNOSTICS.md`
- `diagnostics/NO_CRANK.md`
- `diagnostics/CRANK_NO_START.md`
- `diagnostics/CHARGING_SYSTEM.md`
- `diagnostics/DTC_INDEX.md`
- `roadside/EMERGENCY_FIELD_REPAIRS.md`
- `tools/NOMAD_AUTOMOTIVE_TOOLKIT.md`

---

## 27. Sources

### Exact 2014 Hyundai owner information

- 2014 Hyundai Accent Owner Manual, Hyundai / mirrored PDF:
  - https://cdn.dealereprocess.org/cdn/servicemanuals/hyundai/2014-accent.pdf
- Hyundai Canada 2014 Accent manual, engine-compartment fuse data:
  - https://www.hyundaicanada.com/-/media/hyundai/feature/ownerssection/manuals/english/2014/accent/rb-cane-7.pdf
- Searchable 2014 owner manual mirror:
  - https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/
- Alternate searchable owner manual mirror:
  - https://manualzz.com/doc/53857913/hyundai-2014-accent-owner-manual

### Same-generation Hyundai service-family support

- 2013 Accent 1.6L starting-system component diagnostics:
  - https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Starting%20and%20Charging/Starting%20System/Testing%20and%20Inspection/Component%20Tests%20and%20General%20Diagnostics/

---

## 28. Final rule

```text
POWER SOURCE
    -> PROTECTION
        -> SWITCH / RELAY
            -> WIRING
                -> LOAD
                    -> GROUND
```

When a circuit fails, test that chain in order.

**Do not replace the device at the end of the wire until the wire has proven it delivered what the device needed.**
