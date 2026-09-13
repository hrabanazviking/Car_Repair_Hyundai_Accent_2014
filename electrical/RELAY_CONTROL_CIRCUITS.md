# Relay Control Circuits — 2014 Hyundai Accent SE

> **Scope:** Relay-controlled electrical loads and command circuits for the U.S.-market 2014 Hyundai Accent SE, centered on the engine-room fuse/relay box and the 1.6L Gamma GDI powertrain.
>
> **Core rule:** **A relay click is evidence that something happened on the coil side. It does not prove the contact side delivered usable power to the load.**

---

## 1. Purpose

Relays let a low-current control circuit switch a higher-current load. On this Accent, relay-controlled systems include starting, fuel delivery, engine-management power, cooling fans, horn, blower, lighting, and other body/equipment loads.

A relay circuit normally contains two electrically distinct paths:

```text
CONTROL / COIL SIDE
command source
    ↓
coil feed
    ↓
relay coil
    ↓
control transistor / switch / ground path

LOAD / CONTACT SIDE
battery or fused B+
    ↓
relay contacts
    ↓
load harness
    ↓
component
    ↓
ground
```

A failure on either side can leave the load dead.

---

## 2. Provenance Rules

This guide separates exact-2014 information from adjacent-year service-family procedures.

### EXACT 2014 OWNER DATA

The 2014 Accent owner manual identifies the engine-room fuse/relay box and names relay positions including:

- MAIN RELAY
- F/PUMP
- START
- C/FAN 1
- C/FAN 2
- HORN
- BLOWER
- headlamp-related relays
- wiper-related relays

The exact 2014 fuse table also identifies important upstream feeds:

| Fuse | Rating | Relevant relay/load relationship |
|---|---:|---|
| IG2 | 40 A | Start Relay, Ignition Switch |
| ECU 1 | 30 A | ECU 2 fuse, Engine Control Relay |
| C/FAN | 40 A | Cooling Fan High Relay, Cooling Fan Low Relay |
| HORN | 10 A | Horn Relay |
| F/PUMP | 15 A | Fuel Pump Relay |
| INJECTOR | 15 A | ECM/PCM, OCVs, O2 sensors, Fuel Pump Relay |
| SENSOR | 10 A | ECM/PCM, EVAP/VIS loads, Immobilizer, A/CON Relay, Cooling Fan High/Low Relays |
| ALT | 125 A | Alternator and engine-room fuse/relay box |

**Primary exact-2014 sources:**

- https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/?srch=relay
- https://www.dezosmanuals.com/wp-content/uploads/2021/07/2014-Hyundai-Accent-OM.pdf

### SERVICE-FAMILY SUPPORT

Same-generation 2012–2013 Accent service information is used for relay test methods and starter-circuit logic. These are tagged as supporting data, not silently promoted to exact 2014 VIN-specific facts.

- 2013 starter relay inspection:
  https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Relays%20and%20Modules/Relays%20and%20Modules%20-%20Starting%20and%20Charging/Starter%20Relay/Testing%20and%20Inspection/
- 2013 starter circuit troubleshooting:
  https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Starting%20and%20Charging/Starting%20System/Testing%20and%20Inspection/Component%20Tests%20and%20General%20Diagnostics/
- 2012 relay-box inspection:
  https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Relays%20and%20Modules/Relays%20and%20Modules%20-%20Power%20and%20Ground%20Distribution/Relay%20Box/Testing%20and%20Inspection/
- 2013 fuel-pressure test showing fuel-pump-relay use in service procedure:
  https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Powertrain%20Management/Fuel%20Delivery%20and%20Air%20Induction/Fuel%20Pump/Fuel%20Pressure/Testing%20and%20Inspection/

---

## 3. The Relay Is Two Circuits, Not One

A typical ISO-style automotive relay uses terminal numbers such as:

- **85 / 86** — relay coil
- **30** — common contact feed
- **87** — normally-open switched output
- **87a** — normally-closed contact on some relay designs

However:

> **DO NOT assume every relay in the Accent uses the same internal pinout merely because the plastic case looks similar.**

The physical relay diagram, service wiring diagram, or verified terminal map outranks generic relay conventions.

Same-generation Hyundai starter-relay service information explicitly tests a relay by applying **12 V to terminal 85 and ground to terminal 86**, then checking for continuity between **30 and 87**.

That test method is useful supporting evidence for that relay family, not permission to blindly jumper every relay socket in the car.

---

## 4. What a Relay Click Actually Proves

If the relay clicks when commanded, it may prove that:

- the coil received enough electrical energy to move the armature,
- at least part of the control path is functioning,
- the relay is not mechanically frozen completely open.

It does **not** prove that:

- the contacts are clean,
- the contacts carry current under load,
- the contact feed has battery voltage,
- the output terminal has good voltage under load,
- the downstream harness is intact,
- the load has a good ground,
- the relay contacts are not burned/high-resistance.

Therefore:

```text
RELAY CLICKS
    ≠
LOAD CIRCUIT PROVEN GOOD
```

---

## 5. Core Diagnostic Workflow

```text
LOAD DOES NOT WORK
       ↓
VERIFY BATTERY VOLTAGE
       ↓
CHECK CORRECT FUSE / MAIN FEED
       ↓
COMMAND THE LOAD
       ↓
DOES RELAY CLICK?
   ├─ NO
   │   ↓
   │ CHECK COIL FEED
   │ CHECK COIL CONTROL
   │ CHECK COMMAND INPUT
   │ CHECK MODULE / SWITCH / INTERLOCK
   │
   └─ YES
       ↓
CHECK CONTACT FEED
       ↓
CHECK CONTACT OUTPUT UNDER LOAD
       ↓
VOLTAGE-DROP TEST CONTACTS
       ↓
CHECK LOAD HARNESS
       ↓
CHECK COMPONENT GROUND
       ↓
TEST COMPONENT
       ↓
REPAIR ROOT CAUSE
       ↓
VERIFY
```

---

## 6. Relay Coil-Side Diagnosis

The coil side answers:

> **Why is the relay not being actuated?**

Potential causes include:

- blown upstream fuse,
- open wire,
- corroded connector,
- ignition-switch fault,
- failed control switch,
- ECM/PCM/BCM not issuing command,
- missing module power or ground,
- safety/interlock condition not satisfied,
- damaged relay coil,
- control transistor fault,
- poor relay-socket terminal tension.

### High-side vs low-side control

Do not assume whether a module supplies power or supplies ground to the relay coil.

Possible strategies include:

```text
HIGH-SIDE CONTROL
module/switch supplies +V to coil
other coil side has ground
```

or:

```text
LOW-SIDE CONTROL
coil receives +V from fuse/ignition feed
module grounds other side to energize relay
```

The exact wiring diagram must identify which strategy the circuit uses.

---

## 7. Contact-Side Diagnosis

The contact side answers:

> **The relay moved, but did usable power reach the load?**

Check:

1. battery/feed voltage at the common contact,
2. switched output when relay is commanded,
3. voltage drop across the closed contacts under load,
4. downstream harness and connectors,
5. component power terminal,
6. component ground path.

### Static continuity is not enough

A relay can pass an ohmmeter test with almost no current yet fail when asked to carry a real load.

Burned or oxidized contacts may act like a resistor.

That creates a condition such as:

```text
NO-LOAD METER TEST:
looks normal

UNDER LOAD:
voltage collapses
```

Use loaded voltage-drop testing when possible.

---

## 8. Voltage Drop Across Closed Relay Contacts

With the load commanded ON:

1. place one meter lead at the relay contact input,
2. place the other lead at the contact output,
3. read voltage drop while current is flowing.

An ideal closed contact approaches zero voltage drop.

A meaningful drop indicates resistance inside the relay or connection.

Do not invent one universal numeric failure threshold for every Accent relay circuit. Current draw, relay design, connector construction, and factory diagnostic procedure matter.

The key principle is:

```text
CLOSED SWITCH / RELAY
SHOULD DROP VERY LITTLE VOLTAGE
```

---

## 9. Relay Bench Testing

### SERVICE-FAMILY — 2013 Accent starter relay

Hyundai’s 2013 procedure:

1. remove fuse-box cover,
2. remove starter relay,
3. inspect continuity,
4. apply 12 V to terminal 85 and ground to terminal 86,
5. verify continuity between 30 and 87,
6. replace relay if continuity does not behave correctly.

Source:
https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Relays%20and%20Modules/Relays%20and%20Modules%20-%20Starting%20and%20Charging/Starter%20Relay/Testing%20and%20Inspection/

### SERVICE-FAMILY — relay-box test

Hyundai’s 2012 Accent relay-box procedure describes power-relay testing and warns:

- do not use pliers to remove relays,
- use the relay puller,
- physical relay damage can create stall/no-start conditions.

Source:
https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Relays%20and%20Modules/Relays%20and%20Modules%20-%20Power%20and%20Ground%20Distribution/Relay%20Box/Testing%20and%20Inspection/

### Safety

Bench-energize a relay only after its pinout is known.

Never randomly apply battery voltage to unidentified terminals.

---

## 10. Relay Substitution

Swapping a suspected relay with another relay can be a useful diagnostic test **only if the relays are truly interchangeable**.

Verify:

- identical Hyundai/OEM part number or confirmed equivalent,
- identical terminal layout,
- identical internal schematic,
- same contact function,
- same current rating,
- same suppression component if present,
- same normally-open / normally-closed behavior.

Do not rely on:

- same physical size,
- same color,
- “it fits the socket.”

A relay can physically fit and still be electrically wrong.

---

## 11. Starter Relay

### Exact-2014 upstream anchor

The 2014 owner manual lists:

```text
IG2 40A
→ Start Relay
→ Ignition Switch
```

### SERVICE-FAMILY starter logic

The 2013 Accent service procedure tells the technician to inspect, in order, items including:

- battery condition,
- battery and ground connections,
- ignition-switch circuit,
- transaxle range-switch / interlock path,
- starter relay,
- starter and solenoid.

This supports the repo rule:

```text
NO CRANK
  ≠
BAD STARTER
```

Cross-reference:

- `diagnostics/NO_CRANK.md`
- `electrical/BATTERY_STARTER_ALTERNATOR.md`
- `electrical/POWER_DISTRIBUTION.md`

### Relay-specific decision tree

```text
KEY TO START
   ↓
RELAY CLICKS?
  ├─ NO
  │  → verify IG2 feed
  │  → verify ignition-switch/start request
  │  → verify Park/Neutral interlock path
  │  → verify relay coil and socket
  │
  └─ YES
     → verify contact feed
     → verify output to starter-solenoid circuit
     → voltage-drop test
     → verify starter solenoid / motor / grounds
```

---

## 12. Fuel Pump Relay

### Exact-2014 anchors

The owner manual identifies:

```text
F/PUMP 15A
→ Fuel Pump Relay
```

and:

```text
INJECTOR 15A
→ ECM/PCM
→ OCVs
→ O2 sensors
→ Fuel Pump Relay
```

These relationships mean that a dead fuel-pump circuit may require checking more than the pump itself.

### Service evidence

Hyundai’s 2013 fuel-pressure procedure removes the fuel-pump relay to release residual fuel pressure and warns that doing so may set a DTC.

Source:
https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Powertrain%20Management/Fuel%20Delivery%20and%20Air%20Induction/Fuel%20Pump/Fuel%20Pressure/Testing%20and%20Inspection/

### Diagnosis

```text
NO LOW-SIDE FUEL PRESSURE
        ↓
CHECK F/PUMP FUSE
        ↓
CHECK RELAY COMMAND
        ↓
CHECK RELAY CONTACT FEED
        ↓
CHECK OUTPUT TO PUMP
        ↓
CHECK PUMP GROUND
        ↓
CHECK ACTUAL PUMP CURRENT / PRESSURE
```

A relay that clicks does not prove the pump is receiving adequate voltage.

Cross-reference:

- `engine/GDI_FUEL_SYSTEM.md`
- `diagnostics/CRANK_NO_START.md`

---

## 13. Engine Control / Main Relay

### Exact-2014 anchor

```text
ECU 1 30A
→ ECU 2 fuse
→ Engine Control Relay
```

The exact engine-room diagram identifies a **MAIN RELAY** position.

Loss of main-relay output can potentially remove power from multiple engine-management circuits at once.

Therefore a cluster such as:

- no injector operation,
- no actuator power,
- multiple sensor/actuator codes,
- no-start,
- communication symptoms,

must trigger common-power diagnosis before individual parts are condemned.

### SERVICE-FAMILY relay type caution

Hyundai’s 2012 relay-box test includes more than one relay internal configuration, including a special main-relay test type.

Therefore:

> **Do not assume the main relay is a generic four-pin normally-open relay. Verify its exact internal diagram.**

---

## 14. Cooling Fan Relays

### Exact-2014 anchors

```text
C/FAN 40A
→ Cooling Fan High Relay
→ Cooling Fan Low Relay
```

and:

```text
SENSOR 10A
→ Cooling Fan High Relay
→ Cooling Fan Low Relay
```

The engine-room layout identifies **C/FAN 1** and **C/FAN 2** relay positions.

### Diagnostic logic

If fan operation is wrong:

```text
OVERHEAT / FAN NOT RUNNING
         ↓
CHECK COOLANT TEMP DATA
         ↓
CHECK FAN COMMAND
         ↓
CHECK C/FAN 40A FEED
         ↓
CHECK SENSOR 10A CONTROL FEED
         ↓
CHECK RELAY(S)
         ↓
CHECK FAN MOTOR / RESISTOR / HARNESS AS EQUIPPED
```

Do not condemn a fan motor until relay feed and output have been proven under load.

Cross-reference:

- `engine/COOLING_SYSTEM.md`
- `diagnostics/OVERHEATING.md`
- `electrical/POWER_DISTRIBUTION.md`

---

## 15. A/C Relay

The exact 2014 fuse table shows the **SENSOR 10A** branch feeding the A/CON relay.

A compressor that does not engage can therefore involve:

- A/C request logic,
- pressure/temperature protection logic,
- fuse/feed problem,
- relay coil/control path,
- relay contacts,
- compressor-clutch circuit,
- compressor/clutch hardware,
- ECM/PCM control conditions.

Do not bridge relay contacts as a substitute for diagnosing pressure or protection logic.

A forced compressor clutch can create system damage if the ECM is intentionally withholding A/C operation.

---

## 16. Horn Relay

Exact 2014:

```text
HORN 10A
→ Horn Relay
```

Basic split:

```text
HORN DEAD
  ↓
FUSE GOOD?
  ↓
RELAY COMMAND?
  ↓
RELAY OUTPUT?
  ↓
HORN POWER?
  ↓
HORN GROUND / HORN UNIT
```

A horn relay makes a useful simple training circuit for learning coil-side versus contact-side diagnosis because the load is easy to verify acoustically and electrically.

---

## 17. Blower Relay

Exact 2014 multi-fuse data identifies:

```text
BLOWER 40A
→ Blower Relay
```

A non-running blower can involve:

- 40 A feed,
- blower relay,
- interior HVAC fuse/control feed,
- blower switch/control module,
- resistor or power transistor depending on HVAC configuration,
- blower motor,
- wiring/ground.

Again:

```text
RELAY CLICK
    ≠
BLOWER MOTOR PROVEN GOOD
```

---

## 18. Relay Socket Inspection

A perfectly good relay can fail in a damaged socket.

Inspect for:

- heat discoloration,
- melted plastic,
- loose terminal grip,
- pushed-back terminal,
- green/white corrosion,
- water intrusion,
- spread female terminals,
- overheated contact feed,
- evidence of arcing.

If a relay terminal is burned, replacing only the relay may not repair the cause.

High contact resistance can generate heat:

```text
RESISTANCE
   +
CURRENT
   =
HEAT
```

Repair the terminal/socket damage and determine why overheating occurred.

---

## 19. Thermal / Intermittent Relay Faults

Relays can fail only when:

- hot,
- cold,
- vibrating,
- carrying high current,
- after long run time.

Useful tests include:

- compare behavior cold vs hot,
- monitor voltage drop while failure occurs,
- light tap on relay/fuse-box area as a diagnostic clue only,
- wiggle harness/box while monitoring output,
- scan command vs actual load behavior,
- inspect for heat damage after failure.

Do not strike the fuse box or relay aggressively.

---

## 20. Stuck-Closed Relay Contacts

A relay can fail **closed** as well as open.

Possible symptoms:

- fan continues running unexpectedly,
- horn remains on,
- pump/load remains powered,
- battery drains while parked,
- starter remains engaged if a start-control fault exists,
- component runs without expected command.

Diagnosis:

1. verify actual unwanted voltage at load,
2. remove relay if safe,
3. observe whether load turns off,
4. inspect command circuit,
5. bench-test relay,
6. inspect socket for bridging/water intrusion.

Do not assume a stuck load automatically means welded relay contacts. A control module can also be commanding the relay continuously.

---

## 21. Parasitic-Draw Relationship

A relay held on after key-off can produce a battery drain.

Potential causes:

- welded contacts,
- relay coil continuously commanded,
- module that fails to sleep,
- water intrusion in relay box,
- wiring short that energizes coil,
- aftermarket wiring.

Isolation logic:

```text
PARASITIC DRAW
     ↓
IDENTIFY ACTIVE CIRCUIT
     ↓
REMOVE SUSPECT RELAY
     ↓
DRAW CHANGES?
   ├─ YES → determine contact vs coil/control cause
   └─ NO  → continue circuit isolation
```

Cross-reference:

- `electrical/BATTERY_STARTER_ALTERNATOR.md`

---

## 22. Do Not Use a Relay as a Fuse Bypass

Never:

- jumper a relay socket blindly,
- insert wire or foil in place of a fuse,
- feed battery power into an unknown control terminal,
- force a cooling fan or fuel pump through an unfused jumper,
- bypass starter interlocks casually,
- bypass A/C protection logic as a repair.

A jumper, if used diagnostically, must be:

- based on a verified wiring diagram,
- correctly fused,
- connected only to identified terminals,
- used briefly,
- removed immediately after the test.

---

## 23. Safe Relay-Jumper Philosophy

Before jumping a relay contact:

```text
1. IDENTIFY TERMINALS
2. VERIFY LOAD CIRCUIT
3. VERIFY FUSE PROTECTION
4. VERIFY LOAD WILL NOT CREATE A SAFETY HAZARD
5. USE A FUSED JUMPER
6. KEEP HANDS / TOOLS CLEAR OF MOVING PARTS
7. REMOVE JUMPER AFTER TEST
```

Examples of hazards:

- starter can crank unexpectedly,
- cooling fan can start unexpectedly,
- fuel pump can pressurize system,
- A/C clutch can engage,
- horn can sound,
- lighting circuits can heat damaged wiring.

---

## 24. Starter-Relay Special Safety

Never casually bridge starter-relay contacts with the vehicle in gear.

For an automatic Accent:

- parking brake applied,
- transmission in P or N,
- wheels appropriately controlled,
- people clear of vehicle path,
- hands clear of engine/accessories.

Same-generation Hyundai starter diagnostics explicitly require P/N during starter testing.

---

## 25. Fuel-Pump Relay Special Safety

Fuel-system relay testing can pressurize gasoline.

Rules:

- no smoking/open flame,
- no sparks near fuel,
- maintain ventilation,
- relieve residual pressure using the proper procedure before opening fuel lines,
- wipe spills immediately,
- keep extinguisher access appropriate for the work environment,
- never defeat GDI high-pressure precautions.

Cross-reference:

- `engine/GDI_FUEL_SYSTEM.md`

---

## 26. Cooling-Fan Relay Special Safety

Electric cooling fans may start without warning when commanded.

Keep:

- fingers,
- hair,
- clothing,
- meter leads,
- jumper wires,
- tools

away from the fan whenever ignition is on or a fan circuit is being tested.

---

## 27. Commanded vs Actual Diagnosis

If scan-tool bidirectional control is available:

```text
MODULE COMMANDS RELAY ON
          ↓
DOES COIL ACTUATE?
          ↓
DOES CONTACT OUTPUT CHANGE?
          ↓
DOES LOAD RECEIVE POWER?
          ↓
DOES LOAD OPERATE?
```

This divides the circuit into four layers:

1. module command,
2. relay coil/control,
3. contact/load feed,
4. component operation.

That is far stronger than listening for a click.

---

## 28. Common Diagnostic Patterns

### Pattern A — no click, no output

Likely areas:

- coil feed,
- command/ground,
- fuse,
- wiring,
- module/interlock,
- open relay coil.

### Pattern B — click, no output

Likely areas:

- missing contact feed,
- burned relay contacts,
- wrong relay,
- socket damage,
- open downstream harness.

### Pattern C — output present, component dead

Likely areas:

- downstream voltage drop,
- component connector,
- component ground,
- failed component.

### Pattern D — component weak/intermittent

Likely areas:

- high-resistance contacts,
- terminal heat damage,
- poor ground,
- corroded connector,
- failing load.

### Pattern E — component never shuts off

Likely areas:

- welded contacts,
- continuous coil command,
- module fault,
- wiring short,
- water intrusion.

---

## 29. AI / Runa Rules

When diagnosing a relay-related fault, the AI must:

1. identify the exact relay and controlled load,
2. identify the reporting symptom and DTCs,
3. verify battery/system voltage first,
4. identify upstream fuse(s),
5. identify coil-side feed/control,
6. identify contact-side feed/output,
7. separate command failure from power-delivery failure,
8. use loaded voltage testing when useful,
9. inspect relay socket and terminal condition,
10. verify component ground,
11. avoid assuming generic terminal layouts,
12. avoid recommending relay substitution unless interchangeability is verified,
13. preserve safety interlocks,
14. verify repair under the same conditions that produced the fault.

### AI forbidden shortcuts

Do not say:

- “the relay clicked, so it is good,”
- “swap any same-size relay,”
- “jump the relay” without exact terminal identification,
- “replace the starter” before proving starter feed/control,
- “replace the fuel pump” before checking relay output and pump power/ground,
- “replace the fan” before checking fan-relay feed and command.

---

## 30. Field Diagnostic Record

```yaml
relay_diagnostic:
  date:
  odometer_miles:
  symptom:
  dtcs:
  battery_voltage_key_off:
  battery_voltage_running:
  relay_name:
  relay_part_number:
  relay_internal_diagram_verified: false
  upstream_fuses:
  coil_feed_voltage:
  coil_control_observed:
  relay_clicks: false
  contact_feed_voltage:
  contact_output_voltage:
  loaded_contact_voltage_drop:
  load_voltage:
  load_ground_drop:
  socket_condition:
  heat_damage_present: false
  corrosion_present: false
  relay_bench_test:
  swap_test_used: false
  swap_relay_verified_identical: false
  root_cause:
  repair:
  verification:
  source_confidence:
```

---

## 31. Cross-References

- `electrical/POWER_DISTRIBUTION.md`
- `electrical/WIRING_AND_CONNECTOR_DIAGNOSTICS.md`
- `electrical/GROUND_POINTS.md`
- `electrical/SENSOR_5V_REFERENCE_AND_SENSOR_GROUNDS.md`
- `electrical/BATTERY_STARTER_ALTERNATOR.md`
- `diagnostics/NO_CRANK.md`
- `diagnostics/CRANK_NO_START.md`
- `diagnostics/CHARGING_SYSTEM.md`
- `engine/GDI_FUEL_SYSTEM.md`
- `engine/COOLING_SYSTEM.md`
- `diagnostics/OVERHEATING.md`
- `specs/FUSES_AND_RELAYS.md`
- `roadside/EMERGENCY_FIELD_REPAIRS.md`

---

## 32. Source Summary

### Exact 2014

- Hyundai Accent 2014 owner manual, relay/fuse descriptions:
  https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/?srch=relay
- 2014 owner manual PDF with engine-room relay layout:
  https://www.dezosmanuals.com/wp-content/uploads/2021/07/2014-Hyundai-Accent-OM.pdf
- Alternate owner-manual mirror:
  https://manualzz.com/doc/53857913/hyundai-2014-accent-owner-manual

### Service-family supporting information

- 2013 starter relay bench inspection:
  https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Relays%20and%20Modules/Relays%20and%20Modules%20-%20Starting%20and%20Charging/Starter%20Relay/Testing%20and%20Inspection/
- 2013 starter-system diagnostic procedure:
  https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Starting%20and%20Charging/Starting%20System/Testing%20and%20Inspection/Component%20Tests%20and%20General%20Diagnostics/
- 2012 relay-box / power-relay testing:
  https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Relays%20and%20Modules/Relays%20and%20Modules%20-%20Power%20and%20Ground%20Distribution/Relay%20Box/Testing%20and%20Inspection/
- 2013 fuel-pressure test / fuel-pump-relay service use:
  https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Powertrain%20Management/Fuel%20Delivery%20and%20Air%20Induction/Fuel%20Pump/Fuel%20Pressure/Testing%20and%20Inspection/

---

## 33. Final Diagnostic Doctrine

```text
LOAD DOES NOT WORK
      ↓
PROVE COMMAND
      ↓
PROVE COIL
      ↓
PROVE CONTACT FEED
      ↓
PROVE CONTACT OUTPUT
      ↓
PROVE WIRING
      ↓
PROVE GROUND
      ↓
THEN BLAME THE COMPONENT
```

And the short version:

> **A relay click is a clue. Loaded voltage is evidence.**
