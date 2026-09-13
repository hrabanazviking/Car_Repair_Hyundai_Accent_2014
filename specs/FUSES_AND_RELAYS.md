# 2014 Hyundai Accent SE — Fuses and Relays

> **Purpose:** Offline electrical-reference guide for a U.S.-market 2014 Hyundai Accent SE. Designed for roadside troubleshooting, maintenance, and AI/RAG retrieval.
>
> **Primary rule:** The fuse/relay label physically installed on the vehicle overrides a generic manual table when they disagree.

---

## 1. Scope and Source Hierarchy

This document is based primarily on the **2014 Hyundai Accent Owner's Manual**, Maintenance section, fuse pages 7-51 through 7-60.

Source copies consulted:

- Hyundai Accent 2014 Owner's Manual mirror: https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual
- Alternate searchable owner-manual copy: https://manuals.plus/m/28181eb364b39dbbb16f909d42f8e060859e68749899494eb6c5fca29f35b8b1

Hyundai explicitly warns that not every panel description in the printed manual applies to every vehicle. Equipment and market differences exist.

### Accuracy hierarchy

Use this order when sources disagree:

1. **Fuse/relay label physically on this exact vehicle**
2. **VIN/build-specific Hyundai service information**
3. **2014 Hyundai Accent owner's manual**
4. **Trusted third-party diagrams**
5. **Generic Internet fuse lists**

Do not install a fuse merely because a web diagram says it belongs there.

---

# 2. Fuse Panel Locations

The 2014 Accent has two primary fuse/relay locations:

## A. Instrument panel / driver's side

Located behind the driver's-side instrument-panel fuse cover.

This panel contains many low-current body, accessory, lighting, control-module, window, wiper, audio, and interior circuits.

## B. Engine compartment

Located in the engine bay in the main fuse/relay box.

This panel contains:

- high-amperage multi-fuses
- ignition feeds
- ECU/PCM feeds
- fuel-pump circuit
- ignition-coil circuit
- injector circuit
- cooling-fan circuit
- horn circuit
- headlamp feeds
- several relays

The fuse puller is normally stored in the engine-compartment fuse box.

---

# 3. Safety Rules

Before replacing a fuse:

1. Move the car to a safe location.
2. Switch the ignition OFF.
3. Switch electrical loads OFF.
4. For service work, disconnect the negative battery terminal when appropriate.
5. Replace a fuse **only with the same amperage rating**.

Never:

- install a higher-rated fuse
- bridge a fuse with foil, wire, or metal
- probe fuse sockets with random metal objects
- force an incorrect relay into a socket
- repeatedly replace a fuse that immediately blows

A fuse that repeatedly blows is telling you that the circuit has a fault.

```text
BLOWN FUSE
   ↓
REPLACE ONCE WITH CORRECT RATING
   ↓
BLOWS AGAIN?
   ↓ YES
STOP
   ↓
FIND SHORT / OVERLOAD / FAILED LOAD / DAMAGED WIRING
```

---

# 4. Fuse Types

Hyundai identifies three general fuse types in this vehicle:

- Blade fuse
- Cartridge fuse
- Multi-fuse

High-amperage and bolted fuse assemblies should not be casually removed roadside.

If a bolted multi-fuse or terminal assembly is damaged, verify the proper service procedure before disassembly.

---

# 5. How to Test a Fuse Correctly

## Visual inspection

A blade fuse with a visibly melted element is blown.

However, visual inspection is not always enough.

## Better method: voltage test

With the circuit powered when appropriate:

1. Set the multimeter to DC volts.
2. Ground the black meter lead.
3. Probe the small exposed test point on one side of the fuse.
4. Probe the test point on the other side.

Expected result for a powered circuit:

```text
Battery voltage on both sides = fuse conductive
Voltage on input side only     = fuse open/blown
No voltage on either side      = circuit may not currently be powered
```

Do not interpret "no voltage" as a blown fuse until you know that circuit should be powered in the current ignition/key state.

## Continuity test

A removed fuse can also be checked for continuity with power disconnected.

---

# 6. Instrument Panel Fuse Table

> **VERIFIED — HYUNDAI OWNER'S MANUAL**
>
> Equipment varies. Always compare this list with the physical fuse-panel label.

| Fuse label | Rating | Primary protected components |
|---|---:|---|
| POWER OUTLET | 15A | Power outlet |
| C/LIGHTER | 15A | Cigarette lighter / accessory outlet |
| ACC | 10A | Audio, power outside-mirror switch |
| A/BAG IND | 10A | Instrument-cluster airbag indicator |
| A/BAG | 10A | SRS control module, telltale, passenger occupant detection |
| T/SIG | 10A | Hazard switch / turn-signal related feed |
| MDPS | 10A | EPS/MDPS control module |
| WIPER RR | 15A | Wiper multifunction switch, rear wiper motor |
| SPARE 6 | 15A | Not used / spare |
| SPARE 1 | 10A | Not used / spare |
| FOG LAMP FRT | 10A | Front fog-lamp relay |
| DRL | 10A | Daytime-running-light relay |
| STOP LAMP | 15A | Stop-lamp switch, battery sensor, stop-lamp relay, HAC-related feed, DLC |
| CLUSTER | 10A | Instrument cluster, BCM |
| IG1 | 10A | Stop-lamp switch, ECO switch, seat-heater modules, TPMS, shifter illumination, EPS, rheostat |
| ABS | 10A | ABS/ESC control, ESC OFF switch, related engine-bay connector/relay feed |
| B/UP LAMP | 10A | Back-up lamp switch |
| ECU | 10A | ECM/PCM |
| SPARE 7 | 10A | Not used / spare |
| IG2 (2) | 10A | A/C control module, BCM, smart-key unit if equipped, wiper control |
| HAZARD | 15A | Hazard relay, hazard switch |
| SPARE 2 | 25A | Not used / spare |
| SUNROOF | 15A | Sunroof motor, if equipped |
| SPARE 3 | 10A | Not used / spare |
| TCU | 15A | Vehicle-speed sensor, transaxle range switch |
| SPARE 4 | 15A | Not used / spare |
| IG2 (1) | 10A | Power-window relay, A/C control, cluster, BCM, sunroof, blower-relay feed |
| WIPER FRT | 25A | Front wiper switch and motor |
| DR LOCK | 20A | Door lock/unlock relays, two-turn unlock, driver lock actuator |
| SAFETY POWER WINDOW | 25A | Safety power-window module |
| S/HEATER | 15A | Driver/passenger seat-heater module, if equipped |
| SPARE 5 | 10A | Not used / spare |
| ROOM LP 1 | 10A | Cluster illumination, TPMS, BCM, A/C control, cargo/interior/map lamps |
| AUDIO | 20A | Audio system |
| TAIL LAMP LH | 10A | Left rear combination lamp, left headlamp marker/tail feed, left front turn/tail related feed, license lamps |
| TAIL LAMP RH | 10A | Right lamps plus various illumination circuits, audio/HVAC/control illumination |
| START | 10A | Transaxle range switch, ignition-lock/start-related circuit |
| H/LAMP | 10A | Instrument cluster and engine-bay headlamp-relay feed |
| P/WDW LH | 25A | Driver-side/main and left-rear power-window circuits |
| P/WDW RH | 25A | Passenger/right-side power-window circuits |
| HTD MIRR | 10A | ECM/PCM related feed, rear-defogger switch, heated outside mirrors |
| A/CON | 10A | Automatic A/C control module, if equipped |
| BLOWER | 10A | ECM/PCM, blower switch/resistor, manual A/C control |

### Important note about duplicated names

The manual uses similar labels such as `IG2` in more than one position and distinguishes some positions by diagram number. When servicing the car, use the **physical panel layout**, not just the text label.

---

# 7. Engine-Compartment Fuse Table

> **VERIFIED — HYUNDAI OWNER'S MANUAL**

## Multi-fuse / high-amperage section

| Fuse label | Rating | Protected component |
|---|---:|---|
| MDPS | 80A | EPS/MDPS control module |
| BLOWER | 40A | Blower relay |
| RR HTD | 40A | Rear-defogger relay feed through I/P junction box |
| ABS 2 | 40A | ABS/ESC control module |
| ABS 1 | 40A | ABS/ESC control module, multipurpose check connector |
| ALT | 125A | Alternator and engine-room fuse/relay box distribution |

## Main fuse section

| Fuse label | Rating | Protected component |
|---|---:|---|
| B+1 | 50A | Interior junction-box feeds including room lamp/audio/fog/stop-lamp/tail-lamp related circuits |
| IG2 | 40A | Start relay, ignition switch |
| IG1 | 40A | Ignition switch |
| ECU 1 | 30A | ECU 2 fuse and engine-control relay feed |
| C/FAN | 40A | Cooling-fan high/low relay circuits |
| B+2 | 50A | Interior junction-box feeds including seat heater, sunroof, door lock, hazard and power-window relay |
| HORN | 10A | Horn relay |
| F/PUMP | 15A | Fuel-pump relay |
| H/LAMP RH | 10A | Right headlamp |
| H/LAMP LH | 10A | Left headlamp |
| INJECTOR | 15A | ECM/PCM, oil-control valves, upstream/downstream oxygen sensors, fuel-pump-relay feed |
| SENSOR | 10A | ECM/PCM, purge valve, variable-intake solenoid, canister-close valve, immobilizer module, A/C and cooling-fan relay controls |
| ECU 2 | 10A | ECM/PCM |
| IGN COIL | 15A | Ignition coils 1-4, condenser |
| B/UP LAMP | 10A | PCM, transaxle range switch, cluster, rear lamps, shift-lever illumination |
| WIPER | 10A | ECM/PCM, wiper switch, front wiper motor |

---

# 8. Engine-Compartment Relay Labels

The 2014 manual's engine-bay diagram visibly identifies relay positions/functions including:

- Fuel pump relay
- Main / engine-control relay
- Blower relay
- Headlamp relay
- Headlamp-high relay
- Cooling fan relay 1
- Cooling fan relay 2
- Start relay
- Horn relay
- Rear-wiper relay
- Wiper-related relay position

**Do not assume that every drawn relay position is populated on every trim.** Verify against the lid diagram on the actual vehicle.

Some relays may be integrated or configured differently depending on options and market.

---

# 9. Roadside Symptom-to-Fuse Quick Reference

This table is for **first checks**, not final diagnosis.

| Symptom | First fuses/circuits to inspect |
|---|---|
| OBD scanner has no power | STOP LAMP / DLC-related feed, then connector pin 16 and grounds |
| Engine cranks but will not start | ECU, ECU 1, ECU 2, F/PUMP, INJECTOR, SENSOR, IGN COIL |
| Engine does not crank | START, IG1, IG2, battery/main feeds, range-switch circuit |
| Fuel pump appears inactive | F/PUMP, ECU feeds, fuel-pump relay/control |
| No ignition spark on all cylinders | IGN COIL, ECU/PCM feeds, SENSOR, engine-control relay |
| All injectors appear inactive | INJECTOR, ECU/PCM feeds, engine-control relay |
| Cooling fan inoperative | C/FAN, SENSOR, fan relays and fan circuit |
| Front wipers dead | WIPER FRT, WIPER, IG2-related feeds |
| Rear wiper dead | WIPER RR and rear-wiper relay/circuit |
| Horn dead | HORN plus horn relay |
| Radio dead | AUDIO, ACC, B+1-related feed |
| Power outlet dead | POWER OUTLET |
| Cigarette-lighter socket dead | C/LIGHTER |
| Power windows dead | P/WDW LH, P/WDW RH, SAFETY POWER WINDOW, IG2, B+2 |
| Door locks dead | DR LOCK, B+2 |
| Brake lamps dead | STOP LAMP, stop-lamp switch/circuit |
| ABS/ESC lamps on | ABS, ABS 1, ABS 2, system voltage and module scan |
| Power steering warning / no assist | MDPS 10A, MDPS 80A, system voltage |
| Blower fan dead | BLOWER 10A, BLOWER 40A, blower relay, switch/resistor/motor |
| Headlamp one side dead | H/LAMP LH or H/LAMP RH, bulb/connector/ground |
| Both headlamps dead | H/LAMP control fuse, relay/control, IG feeds |
| Hazard lights dead | HAZARD, T/SIG, hazard switch/relay |
| Reverse lamps dead | B/UP LAMP circuits, range/back-up switch |
| Interior lights dead | ROOM LP 1, B+1 feed, BCM |

---

# 10. No-Start Electrical Triage

For a crank/no-start where an electrical supply fault is suspected:

```text
CRANKS BUT WILL NOT START
        ↓
Read DTCs and live RPM
        ↓
Check ECU / ECU 1 / ECU 2
        ↓
Check SENSOR
        ↓
Check IGN COIL
        ↓
Check INJECTOR
        ↓
Check F/PUMP
        ↓
Verify power at loads/relays
        ↓
Verify grounds and ECU commands
```

A good fuse does not prove that the downstream device is receiving usable voltage under load.

After fuse checks, use voltage-drop testing and circuit testing as appropriate.

---

# 11. No-Crank Electrical Triage

```text
NO CRANK
  ↓
Battery voltage / terminal condition
  ↓
Main ALT/B+ distribution intact?
  ↓
IG1 / IG2 feeds
  ↓
START fuse
  ↓
Try Neutral as well as Park
  ↓
Start relay / range switch / ignition switch
  ↓
Starter control voltage
  ↓
Starter / cable voltage drop / mechanical condition
```

Never condemn the starter based on a fuse check alone.

---

# 12. OBD-II Scanner Has No Power

The standardized OBD-II connector normally uses:

- Pin 16: battery positive
- Pin 4: chassis ground
- Pin 5: signal ground

If the scanner is dead:

1. Confirm the scanner itself is functional.
2. Inspect the relevant interior fuse, especially the stop-lamp/DLC-associated feed shown by Hyundai.
3. Check voltage at DLC pin 16.
4. Check grounds at pins 4 and 5.
5. Inspect the socket for spread, bent, or pushed-back terminals.

Do not randomly jumper OBD pins.

---

# 13. A Fuse Is Good, but the Device Still Does Not Work

Move downstream logically:

```text
FUSE GOOD
  ↓
Is power present at fuse output?
  ↓
Is relay commanded?
  ↓
Is relay output present?
  ↓
Is voltage reaching the device?
  ↓
Does the device have a good ground?
  ↓
Does the device itself operate?
```

Possible causes include:

- failed relay
- corroded connector
- broken wire
- damaged ground
- failed switch
- module command problem
- failed motor/solenoid/load
- network/BCM/ECU problem

---

# 14. Relay Testing Basics

For a removable conventional relay, diagnosis may include:

- verifying relay coil power and ground/control
- verifying switched power into the relay
- verifying output from the relay
- bench-testing coil/contact operation when appropriate
- temporarily swapping only with a **known identical relay** whose pinout and rating match

Do not swap relays merely because their plastic cases look similar.

Never force a relay into a socket.

---

# 15. Repeatedly Blown Fuse Diagnostic Tree

```text
FUSE BLOWS
  ↓
Record exactly when it blows
  ↓
Key off? Key on? Cranking? Device activated?
  ↓
Inspect recently disturbed wiring/components
  ↓
Disconnect suspected loads one at a time
  ↓
Inspect harness for rub-through / pinch / heat damage
  ↓
Measure circuit for short to ground where appropriate
  ↓
Repair root cause
  ↓
Install correct fuse
  ↓
Verify under normal load
```

Useful clues:

- Blows instantly with key OFF: likely constant-power short.
- Blows when key turns ON: switched circuit fault.
- Blows only when a device is activated: device, motor, harness, or downstream circuit fault.
- Blows intermittently over bumps: harness chafing or loose connector becomes more likely.

These are diagnostic patterns, not absolute rules.

---

# 16. Spare Fuses

The interior diagram includes several positions identified as `SPARE` / `Not Used`.

A spare fuse is useful only if:

- it is actually populated in this car
- it has the same amperage rating needed
- the physical fuse type matches

Do not convert an unused circuit slot into an improvised power source without proper circuit design and protection.

---

# 17. Useful Nomad Electrical Kit

For long-distance/nomadic use, a compact electrical kit can include:

- assorted correct-size blade fuses in the ratings used by the car
- fuse puller
- digital multimeter
- small test leads
- headlamp/flashlight
- electrical-contact cleaner
- quality electrical tape
- heat-shrink tubing
- wire stripper/crimper
- a small quantity of automotive primary wire
- insulated crimp connectors
- battery-terminal brush

A repair kit should help restore a known circuit fault safely. It should not encourage bypassing circuit protection.

---

# 18. Critical Fuse Ratings Worth Memorizing

These are especially relevant to a roadside no-start or major electrical failure:

```yaml
engine_bay:
  ALT: 125A
  MDPS: 80A
  B_PLUS_1: 50A
  B_PLUS_2: 50A
  IG1: 40A
  IG2: 40A
  C_FAN: 40A
  ECU_1: 30A
  F_PUMP: 15A
  INJECTOR: 15A
  IGN_COIL: 15A
  SENSOR: 10A
  ECU_2: 10A
  HORN: 10A
  H_LAMP_LH: 10A
  H_LAMP_RH: 10A
  B_UP_LAMP: 10A
  WIPER: 10A

interior:
  START: 10A
  ECU: 10A
  TCU: 15A
  STOP_LAMP: 15A
  WIPER_FRT: 25A
  WIPER_RR: 15A
  DR_LOCK: 20A
  AUDIO: 20A
  POWER_OUTLET: 15A
  C_LIGHTER: 15A
```

This YAML is intended for AI indexing and quick retrieval. It does **not** replace the complete tables above.

---

# 19. AI Retrieval Rules

When an AI uses this file:

1. Do not treat a blown fuse as the root cause unless evidence supports it.
2. Never recommend a larger fuse.
3. Never recommend bypassing a fuse.
4. If a replacement fuse immediately blows, stop replacement attempts and diagnose the circuit.
5. Distinguish between:
   - fuse intact
   - fuse powered
   - downstream circuit powered
   - device commanded
   - device functional
6. If the user's physical fuse-panel label differs from this document, trust the car's label.
7. Treat trim-dependent or option-dependent circuits as conditional.
8. Do not infer relay pinout from appearance alone.

Recommended AI phrasing:

```text
Check fuse X first because Hyundai lists it as feeding Y.
If the fuse is intact, verify voltage on both sides before moving downstream.
If it blows again, do not install another fuse until the short/overload is isolated.
```

---

# 20. Owner-Specific Verification Checklist

For this exact vehicle, photograph and archive:

- [ ] Driver-side fuse-panel label
- [ ] Engine-bay fuse-box lid diagram
- [ ] VIN
- [ ] Build-date label
- [ ] Any aftermarket electrical additions
- [ ] Battery model/specification

Once photographed, this repository can add an **OWNER-VERIFIED** overlay documenting which fuse/relay positions are actually populated on this exact Accent.

That will be more authoritative for field use than a generic 2014 table.

---

# 21. Document Status

- **Vehicle:** 2014 Hyundai Accent SE
- **Market:** U.S. baseline
- **Document:** Fuse and relay reference
- **Primary source:** 2014 Hyundai Accent Owner's Manual
- **Confidence:** High for listed manual circuits; exact installed configuration still requires physical-label confirmation
- **Copyright approach:** Original reference/diagnostic organization; no reproduction of manual diagrams

---

# 22. Source Notes

Hyundai's 2014 owner's manual states that:

- the car has two fuse panels, one at the driver's-side panel and one in the engine compartment
- a blown fuse must be replaced with one of the same rating
- the actual fuse/relay panel label may differ based on vehicle equipment
- the physical fuse-panel label should be referenced when inspecting the vehicle

Primary references:

- https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/?srch=fuses
- https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/?srch=relay
- https://manuals.plus/m/28181eb364b39dbbb16f909d42f8e060859e68749899494eb6c5fca29f35b8b1

---

## Core Rule

```text
FUSE PROTECTS WIRING.
A BLOWN FUSE IS EVIDENCE.
FIND WHY IT BLEW.
```
