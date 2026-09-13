# 2014 Hyundai Accent SE — Wiring and Connector Diagnostics

> **Purpose:** A practical, source-aware electrical-circuit troubleshooting guide for a U.S.-market 2014 Hyundai Accent SE. It is designed for human field use and offline AI/RAG retrieval.
>
> **Core rule:** Do not replace a sensor, actuator, module, relay, or motor until its **power, ground, signal/control circuit, connector condition, and wiring path** have been tested under the conditions where the fault occurs.

---

## 1. Scope

This guide covers:

- Open circuits
- Shorts to ground
- Shorts to power
- Excessive resistance
- Voltage-drop testing
- Continuity testing
- Connector inspection
- Terminal tension / pin-fit problems
- Back-probing
- Waterproof connectors
- Intermittent faults
- Wiggle testing
- Heat / vibration / load reproduction
- 5 V reference circuits
- Sensor signal circuits
- Actuator and solenoid circuits
- Relay-controlled circuits
- CAN communication basics
- Data Link Connector (DLC) checks
- Harness damage from vibration, sharp edges, heat, fluids, corrosion, and prior repairs
- Field-safe temporary stabilization versus permanent repair
- AI diagnostic reasoning rules

Related repository files:

- `GROUND_POINTS.md`
- `BATTERY_STARTER_ALTERNATOR.md`
- `../diagnostics/OBD2_GUIDE.md`
- `../specs/FUSES_AND_RELAYS.md`
- `../guides/ROADSIDE_DIAGNOSTIC_TRIAGE.md`
- `../roadside/EMERGENCY_FIELD_REPAIRS.md`

---

# 2. Source / Confidence Labels

- **VERIFIED — STANDARD:** Defined by an applicable SAE / OBD standard.
- **VERIFIED — HYUNDAI ALL-MODEL:** Hyundai technical guidance explicitly published for all Hyundai models.
- **SERVICE-FAMILY — 2013 ACCENT 1.6 GDI:** Same-generation / same-engine Hyundai Accent service information. Very relevant, but not treated as a substitute for an exact 2014 VIN-specific ETM.
- **GENERAL DIAGNOSTIC PRACTICE:** Common professional electrical-diagnostic method, not a Hyundai-specific numeric specification.
- **UNKNOWN:** Exact 2014 circuit pinout, wire color, splice location, connector cavity number, or ground ID not yet verified from a 2014 Accent Electrical Troubleshooting Manual.

> **Repository rule:** If the exact 2014 wiring diagram is not verified, do not invent a wire color, pin number, connector ID, splice ID, or ground-location code.

---

# 3. First Principle: A Component Needs a Complete Circuit

An electrical component can be perfectly healthy and still fail to operate because of the circuit around it.

A simplified device circuit is:

```text
POWER SOURCE
   ↓
FUSE / FUSIBLE LINK
   ↓
RELAY / SWITCH / MODULE DRIVER
   ↓
WIRE / CONNECTOR / SPLICE
   ↓
LOAD (sensor / motor / solenoid / lamp / module)
   ↓
GROUND RETURN
   ↓
BATTERY NEGATIVE
```

For a sensor, the circuit may instead be:

```text
ECM 5 V REFERENCE
      ↓
   SENSOR
      ↓
SIGNAL RETURN TO ECM
      ↓
SENSOR GROUND
```

A DTC naming a sensor does **not** prove the sensor is defective.

Possible causes include:

- Missing power
- Missing ground
- Open signal wire
- Short-to-ground
- Short-to-power
- Excessive resistance
- Corroded or loose terminal
- Spread female terminal
- Water intrusion
- Harness chafing
- Module driver fault
- Shared 5 V reference pulled down by another device
- Mechanical fault causing an implausible but electrically valid reading

The mental model is:

```text
CODE / SYMPTOM
      ↓
WHAT CIRCUIT FUNCTION IS MISSING OR IMPLAUSIBLE?
      ↓
POWER + GROUND + SIGNAL / CONTROL
      ↓
TEST
      ↓
ISOLATE
      ↓
REPAIR ROOT CAUSE
```

---

# 4. Safety Before Probing Anything

## Do not casually probe these circuits

Use the proper Hyundai procedure before testing:

- Supplemental Restraint System (SRS) / airbags / pretensioners
- Pyrotechnic devices
- GDI injector drive circuits
- High-current starter and alternator circuits
- ABS hydraulic-unit motor circuits
- Electronic throttle motor circuits
- Module communication circuits when the correct pinout is unknown

### SRS rule

Do **not** measure resistance across an airbag squib or pretensioner circuit with a generic ohmmeter. Do not use a test light on SRS circuits.

### GDI injector rule

Do not apply battery voltage directly to a GDI injector. Injector drivers may use specialized high-voltage / high-current control strategies.

### Control-module rule

Never assume a circuit can tolerate a conventional incandescent test light. A test light can draw far more current than an ECM/TCM/sensor circuit was designed to supply.

For low-current electronics, use a high-impedance digital volt-ohm meter (DVOM) unless the service procedure specifies another tool.

---

# 5. Basic Electrical Failure Types

## Open circuit

An open circuit interrupts current flow.

Common causes:

- Broken conductor
- Terminal backed out of connector
- Unplugged connector
- Broken crimp
- Corroded-through wire
- Burned fuse
- Broken splice
- Internal switch / relay contact failure

Typical symptom:

```text
POWER EXISTS UPSTREAM
POWER DISAPPEARS DOWNSTREAM
```

---

## Short to ground

A powered or signal circuit unintentionally contacts ground.

Possible effects:

- Fuse blows
- Signal is forced low
- 5 V reference collapses
- Module sets circuit-low DTC
- Wire or component overheats if insufficiently protected

---

## Short to power

A signal or control wire unintentionally contacts a powered circuit.

Possible effects:

- Sensor signal stuck high
- Actuator stays energized
- Module reports circuit-high fault
- Communication circuit disrupted
- Backfeeding occurs through another circuit

---

## Excessive resistance

The circuit is technically continuous but cannot carry current correctly.

Common causes:

- Corrosion
- Loose terminal
- Loose eyelet
- Partially broken conductor
- Poor crimp
- Burned relay contact
- Oxidized splice
- Connector terminal with weak contact pressure

This is why:

```text
CONTINUITY = YES
```

does **not** necessarily mean:

```text
CIRCUIT = GOOD UNDER LOAD
```

Voltage-drop testing is often the better test.

---

# 6. Hyundai Connector-Handling Rules

**SERVICE-FAMILY — 2013 ACCENT 1.6 GDI**

Hyundai same-generation Accent service information gives several excellent connector rules:

1. **Do not pull on the wire harness to disconnect a connector.** Hold the connector body.
2. Operate the connector lock / lever correctly.
3. Listen / feel for the connector to click securely into the locked position.
4. When measuring voltage or continuity, Hyundai instructs technicians to insert the tester probe from the **wire-harness side** where accessible.
5. Waterproof connectors may require checking from the connector side because the harness side is sealed.
6. Use a **fine test probe / fine wire** so the terminal is not spread or damaged.
7. Check for missing terminals, poor crimps, broken conductor cores, rust, contamination, deformation, or bent pins.
8. Lightly pull individual wires to verify the conductor is properly retained in the terminal.
9. Terminal tension can be checked using the correct spare male terminal in the female terminal.
10. If contact pressure is abnormal, replace the female terminal.
11. Hyundai specifically warns **not to use sandpaper on electrical contact points**, because it can damage the contact surface.

Source:

- https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Powertrain%20Management/Computers%20and%20Control%20Systems/Testing%20and%20Inspection/Initial%20Inspection%20and%20Diagnostic%20Overview/

---

# 7. Connector Inspection Checklist

Before measuring anything, inspect the connector.

## Connected

Check:

- Is the latch fully engaged?
- Does the connector sit squarely?
- Does moving the connector change the symptom?
- Is the connector body cracked?
- Is oil, coolant, water, or dirt entering it?
- Is the harness pulling sideways on the connector?

## Disconnected

Check:

- Bent pins
- Pushed-back terminals
- Missing terminals
- Green/white corrosion
- Heat discoloration
- Melted plastic
- Fluid contamination
- Torn seals
- Broken secondary locks
- Loose female-terminal tension
- Broken conductor directly behind the terminal

### Terminal pushed backward

A terminal can look present from the face of the connector yet slide backward when the mating connector is installed.

This can produce a maddening intermittent fault that disappears as soon as the connector is unplugged for inspection.

Always verify terminal retention.

---

# 8. Back-Probing Without Creating a New Fault

Back-probing means measuring the circuit while the connector remains plugged in and operating.

Advantages:

- Circuit remains loaded.
- Sensor / actuator is operating normally.
- Real voltage can be observed.
- Intermittent contact problems are more likely to remain present.

## Rules

- Use the thinnest suitable probe.
- Enter from the harness side where the connector design permits.
- Never force a probe alongside a sealed terminal.
- Do not spread female terminals.
- Do not let two probes touch each other.
- Do not short adjacent terminals.
- Do not use a probe large enough to deform a weather seal.

### Waterproof connectors

Hyundai service information notes that waterproof connectors may not be accessible from the harness side. Use the specified access method and fine probe without damaging the seal or terminal.

---

# 9. Avoid Piercing Insulation When Possible

**GENERAL DIAGNOSTIC PRACTICE**

Prefer:

- Back-probing
- Breakout leads
- Adapter harnesses
- Connector test terminals

Piercing a wire creates a future corrosion path.

If insulation must be pierced for a diagnostic test:

1. Use the smallest practical puncture.
2. Avoid areas exposed to water / road salt if possible.
3. Seal the puncture properly afterward with an automotive-grade method.
4. Record that the wire was pierced.

Do not leave a pinhole in a road-salt-exposed harness and call the test finished.

---

# 10. Continuity Testing

## Critical rule

**Never measure resistance / continuity on an energized circuit.**

Turn power off and isolate the circuit according to the service procedure.

Why:

- External voltage can damage the meter.
- Modules can create false resistance readings.
- Parallel paths can make an open wire appear continuous.

## Same-generation Hyundai reference values

**SERVICE-FAMILY — 2013 ACCENT 1.6 GDI**

For Hyundai's basic wire-isolation examples:

```text
≤ 1 Ω     → treated as continuous / normal wire in the example
≥ 1 MΩ    → treated as open in the example
```

These are troubleshooting reference values from the Hyundai circuit-inspection method, not universal specifications for every component.

A high-current cable can fail under load even if an unloaded ohmmeter reads much less than 1 Ω.

---

# 11. Finding an Open Circuit

## Method A — continuity segmentation

Example:

```text
MODULE A ───── CONNECTOR B ───── SENSOR C
```

Power off and isolate the required modules.

1. Measure A-to-C.
2. If open, divide the circuit.
3. Measure A-to-B.
4. Measure B-to-C.
5. The failing segment contains the open.

This is a binary-search mindset:

```text
WHOLE PATH BAD
     ↓
DIVIDE PATH
     ↓
BAD HALF
     ↓
DIVIDE AGAIN
```

Do not peel the entire harness open before proving where the fault lives.

## Method B — live voltage tracing

Hyundai's same-generation example shows a 5 V circuit where:

```text
Connector A = 5 V
Connector B = 5 V
Connector C = 0 V
```

Therefore, the open exists between B and C.

Live voltage tracing is often faster than continuity testing because the circuit remains in its working state.

---

# 12. Finding a Short to Ground

Power off and isolate the circuit as required.

A general isolation method:

1. Disconnect the load and controlling module as specified.
2. Measure the suspect conductor to chassis ground.
3. If the conductor is grounded when it should not be, divide the harness path by disconnecting intermediate connectors / splices.
4. Repeat until the grounded segment is isolated.

**SERVICE-FAMILY — 2013 ACCENT 1.6 GDI**

Hyundai's simplified diagnostic example treats:

```text
≤ 1 Ω to chassis ground  → short-to-ground condition
≥ 1 MΩ                   → not shorted to ground
```

Only apply this after the circuit is properly isolated. Many legitimate loads and modules provide normal paths to ground.

---

# 13. Finding a Short to Power

**GENERAL DIAGNOSTIC PRACTICE**

Symptoms can include:

- Circuit-high DTC
- Actuator energized when it should be off
- Signal stuck near B+
- Backfeeding through another fuse or module

Method:

1. Identify what voltage should normally exist on the circuit.
2. Disconnect the intended source / module as appropriate.
3. Check whether unwanted voltage remains.
4. Remove related fuses or disconnect harness branches one at a time.
5. When the unwanted voltage disappears, the last isolated branch is strongly implicated.

Do not randomly remove modules from a live network. Record DTCs first and follow safe power-down procedures.

---

# 14. Voltage-Drop Testing

Voltage drop measures **how much voltage is lost across a wire, terminal, connector, switch, relay contact, ground, or cable while current is actually flowing**.

This is one of the best tools for finding excessive resistance.

## Basic method

1. Place one meter lead on one side of the suspect section.
2. Place the other lead on the other side.
3. Operate the circuit under its normal load.
4. Read the voltage difference.

A perfect conductor would have almost no measurable drop.

A bad connection consumes voltage.

## Same-generation Hyundai electronic-circuit guidance

**SERVICE-FAMILY — 2013 ACCENT 1.6 GDI**

Hyundai states that a voltage drop greater than approximately:

```text
0.1 V on ordinary wiring
0.05 V (50 mV) on a 5 V circuit
```

may indicate a loose or dirty connection.

These are diagnostic reference values, not a universal pass/fail specification for every circuit.

Source:

- https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Powertrain%20Management/Computers%20and%20Control%20Systems/Testing%20and%20Inspection/Initial%20Inspection%20and%20Diagnostic%20Overview/

## Hyundai high-current guidance

**VERIFIED — HYUNDAI ALL-MODEL**

Hyundai TSB 08-BE-004 uses **0.2 V** as the repair threshold when loaded voltage-drop testing:

- Positive battery-cable branches
- Negative battery cable
- Engine-compartment body grounds
- Engine ground straps
- Transmission ground straps

Source:

- https://charm.li/Hyundai/2008/Sonata%20V6-3.3L/Repair%20and%20Diagnosis/Technical%20Service%20Bulletins/Customer%20Interest/Electrical%20-%20Voltage%20Drop%20Diagnostics/

### Do not confuse the two contexts

```text
HIGH-CURRENT CABLE / STRAP TEST
≈ 0.2 V Hyundai TSB threshold

LOW-CURRENT SIGNAL / SENSOR WIRING
much smaller drops can matter
```

---

# 15. Why Continuity Alone Can Lie

Suppose a corroded wire has only a few strands remaining.

An ohmmeter sends tiny current and may report:

```text
0.3 Ω
```

The wire appears continuous.

But a motor tries to draw several amps and the same damaged section produces a large voltage drop.

Therefore:

```text
LOW RESISTANCE WITH NO LOAD
          ≠
GOOD CIRCUIT UNDER REAL LOAD
```

Use voltage drop whenever the circuit can safely be operated.

---

# 16. Intermittent Fault Diagnosis

**SERVICE-FAMILY — 2013 ACCENT 1.6 GDI**

Hyundai specifically recommends recreating the conditions in which the fault occurs.

## Wiggle test

Gently move:

- Connector
- Harness branch
- Sensor lead
- Relay
- Suspect component

while watching:

- Live data
- Voltage
- Continuity / resistance on a powered-off isolated circuit
- Misfire counter
- Warning lamp
- Scan-tool communication

Hyundai instructs technicians to lightly shake the connector and harness vertically and horizontally.

Do not yank or aggressively bend wiring.

## Heat simulation

Hyundai allows cautious heating of a suspected component with a suitable heat source.

Rules:

- Do not overheat the part.
- Do **not** directly heat the ECM.

Useful for faults that appear only hot.

## Electrical-load simulation

Hyundai recommends reproducing electrical-load conditions using equipment such as:

- Headlights
- Blower
- Rear defogger
- Other normal vehicle loads

This is particularly useful for:

- Weak grounds
- High-resistance battery cables
- Marginal alternator output
- Intermittent connectors

---

# 17. Harness Inspection

Hyundai same-generation service information directs inspection for:

- Twisted harness
- Pulled harness
- Loose harness
- Abnormally hot wiring
- Harness contacting a sharp edge
- Harness moving or vibrating against another part
- Incorrect attachment / routing
- Damaged outer covering

For nomad / primitive-road use, add special attention to:

- Lower engine-bay harnesses after gravel or brush contact
- Wheel-speed sensor wiring near wheels
- Underbody connectors after mud / water crossings
- Harnesses near engine mounts that may flex more on rough roads
- Rodent damage after remote camping
- Salt and moisture intrusion

---

# 18. 5 V Reference Circuits

Many engine sensors share one or more regulated reference-voltage circuits from the ECM.

A typical sensor has:

```text
5 V REFERENCE
SENSOR GROUND
SIGNAL
```

If one sensor or harness branch shorts the 5 V reference to ground, multiple unrelated sensors can suddenly report impossible values.

Possible clues:

- Several sensor DTCs appear simultaneously.
- Multiple signals are stuck near 0 V.
- 5 V reference disappears at more than one sensor.
- Disconnecting one sensor restores the reference voltage.

## Isolation method

1. Verify battery/system voltage first.
2. Confirm whether the 5 V reference is actually missing.
3. Identify sensors sharing that reference using a verified wiring diagram.
4. Disconnect branches/components one at a time.
5. If reference voltage returns when one branch is disconnected, inspect that branch/component for a short.

### AI rule

Never recommend an ECM solely because several 5 V sensors fail simultaneously.

A shared shorted sensor or harness is often a more economical hypothesis to test first.

---

# 19. Sensor Signal Diagnosis

A sensor circuit must be judged by **plausibility**, not merely by the presence of voltage.

Example checks:

- Does ECT roughly match ambient temperature after an overnight cold soak?
- Does MAP change logically with engine load?
- Does throttle position change smoothly?
- Does RPM appear during cranking?

A stable but impossible value can come from:

- Biased sensor
- Signal shorted to reference
- Signal shorted to ground
- High-resistance sensor ground
- Mechanical condition producing a real but abnormal measurement

Do not replace a sensor until wiring and plausibility are checked.

---

# 20. Actuator / Solenoid Circuits

Actuators may be controlled by:

- Switched power with module-controlled ground
- Module-controlled power
- Pulse-width modulation (PWM)
- H-bridge motor control
- Dedicated driver circuitry

Examples include:

- Purge-control solenoid
- Fuel-pump relay control
- Ignition coils
- Injectors
- Electronic throttle motor
- Transmission solenoids
- Cooling fan control

## Important

A DVOM may display an averaged voltage on a PWM circuit.

Example:

```text
Meter says 6.5 V
```

This does not necessarily mean the circuit is receiving a steady 6.5 V. It may be a rapidly switched 12 V signal.

An oscilloscope may be required for waveform-level diagnosis.

---

# 21. Relay Circuit Diagnosis

A relay contains two different circuits:

```text
CONTROL SIDE
coil power + coil ground / module command

LOAD SIDE
battery feed + switched output to component
```

A relay can click and still have burned load contacts.

A relay that does not click may have:

- Missing coil power
- Missing module ground command
- Broken coil
- Poor socket terminal
- Module logic preventing command because another prerequisite is missing

Do not conclude "bad relay" from sound alone.

---

# 22. Fuse Testing

Do not rely only on visual inspection.

Useful methods:

## Continuity test

Power off, fuse removed:

```text
continuity → fuse element intact
open       → fuse blown
```

## Voltage test

Circuit powered:

Check the two fuse test points.

```text
B+ on both sides → fuse is carrying source voltage
B+ on one side only → fuse open
0 V both sides → source/feed problem upstream or circuit not powered in current state
```

### Repeated blown fuse

Never install a larger fuse.

A repeatedly blown fuse means:

```text
EXCESS CURRENT EXISTS
       ↓
FIND WHY
```

Possible causes:

- Shorted wire
- Shorted motor
- Failed actuator
- Water intrusion
- Incorrect aftermarket wiring

See `../specs/FUSES_AND_RELAYS.md`.

---

# 23. CAN Communication Basics

The 2014 Accent uses CAN communication for multiple control modules.

Examples of information shared over the network include:

- Engine speed
- Transmission information
- ABS / ESC data
- Torque-reduction requests
- Steering / vehicle-dynamics information

A U-code often means:

```text
A MODULE DID NOT RECEIVE AN EXPECTED MESSAGE
```

It does **not** automatically mean the named module is dead.

Possible causes:

- Module has no power
- Module has no ground
- CAN-H open
- CAN-L open
- CAN shorted together
- CAN shorted to power / ground
- Connector problem
- Low system voltage
- One failed module disrupting the bus

---

# 24. OBD-II Data Link Connector

**VERIFIED — STANDARD / VEHICLE SERVICE-FAMILY**

Important standardized DLC pins include:

| Pin | Function |
|---:|---|
| 4 | Chassis ground |
| 5 | Signal ground |
| 6 | CAN High |
| 14 | CAN Low |
| 16 | Battery positive |

SAE J1962 defines the standardized diagnostic connector and contact allocation.

Source:

- https://saemobilus.sae.org/standards/j1962_201607-diagnostic-connector

Same-generation Hyundai Accent ABS diagnostic information instructs checking:

```text
DLC pin 16 → approximately battery voltage
DLC pin 4  → continuity to body ground
DLC pins 6 and 14 → CAN communication path
```

Source:

- https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Brakes%20and%20Traction%20Control/Antilock%20Brakes%20%2F%20Traction%20Control%20Systems/Testing%20and%20Inspection/

---

# 25. CAN Resistance

**SERVICE-FAMILY — 2013 ACCENT**

Same-generation Hyundai ABS/cluster troubleshooting uses approximately:

```text
60 Ω
```

across the CAN pair in a specific diagnostic configuration with ignition OFF and the service procedure's specified connectors disconnected.

This agrees with the expected behavior of a two-termination CAN network, but it must **not** be blindly applied to every connector state or subnetwork.

### Rule

Do not write:

```text
pins 6–14 must always equal exactly 60 Ω
```

Instead:

1. Power the network down correctly.
2. Follow the exact service configuration.
3. Measure only after modules/capacitors have settled.
4. Interpret resistance in context.

Possible broad patterns in a conventional two-terminator CAN network:

```text
~60 Ω    → both terminators likely present
~120 Ω   → one termination / one branch may be missing
very low → possible short / extra termination
open     → broken CAN path / no termination seen
```

These are **general network heuristics**, not exact 2014 Accent factory pass/fail values outside the documented test state.

---

# 26. Scanner Will Not Communicate

Use this order:

```text
SCANNER DEAD?
   ↓
CHECK DLC PIN 16 POWER
   ↓
CHECK DLC GROUNDS
   ↓
TRY KNOWN-GOOD SCANNER / CABLE
   ↓
CHECK RELATED FUSES
   ↓
CHECK CAN PATH
   ↓
CHECK MODULE POWER + GROUND
```

Do not immediately condemn the ECM.

A dead DLC power feed, poor ground, or network fault can make every module appear absent.

---

# 27. U-Code / Multiple-Module Fault Strategy

When many modules suddenly report communication faults:

1. Check battery voltage.
2. Check charging voltage if engine runs.
3. Preserve all U-codes before clearing.
4. Identify which modules still communicate.
5. Identify the missing module(s).
6. Verify power and ground at the missing module before network surgery.
7. Inspect shared CAN branches/connectors.
8. If one module disconnect restores network communication, investigate that module and its branch.

### Important pattern

```text
LOW VOLTAGE
   ↓
MULTIPLE MODULES RESET
   ↓
U-CODE STORM
```

A network full of DTCs after a weak-battery event does not prove the CAN harness failed.

---

# 28. Terminal Tension / Pin-Fit Faults

A terminal can look clean and still fail electrically because the female terminal no longer grips the male pin tightly.

Symptoms:

- Fault appears over bumps.
- Fault changes when connector is pushed sideways.
- Voltage looks normal unloaded but collapses when component draws current.
- Wiggle test reproduces issue.

Hyundai same-generation guidance checks female-terminal tension with the appropriate spare male terminal.

Do not jam an oversized generic probe into the female terminal to "test tightness." That can permanently spread the contact.

---

# 29. Corrosion and Contamination

Common sources:

- Water
- Road salt
- Coolant
- Oil
- Battery acid vapor / residue
- Mud
- Rodent contamination

Corrosion increases resistance and can migrate under insulation by capillary action.

If green corrosion extends into the strands, cleaning only the visible terminal may not be enough.

Inspect conductor quality behind the crimp.

---

# 30. Heat-Damaged Connectors

Heat is evidence of resistance or excessive current.

Look for:

- Brown/black plastic
- Warped connector shell
- Softened fuse socket
- Discolored terminal
- Melted insulation

If a high-current connector is heat damaged:

```text
DO NOT JUST CLEAN IT
```

Find why it heated:

- Weak terminal grip
- Corrosion
- Loose connection
- Excessive load
- Wrong fuse
- Failed motor/component

A replacement connector installed without correcting the root cause may melt again.

---

# 31. Harness Repair Principles

**GENERAL DIAGNOSTIC PRACTICE**

A permanent automotive wire repair should preserve:

- Correct conductor gauge
- Adequate current capacity
- Appropriate temperature rating
- Oil / fuel / moisture resistance as required
- Mechanical strain relief
- Weather sealing where required
- Correct routing and protection

Preferred repair methods use proper automotive terminals or sealed crimp-splice systems and appropriate heat-shrink / sealing methods.

## Avoid permanent repairs made from:

- Twisted bare wires plus electrical tape
- Household wire nuts
- Scotch-lock style taps on critical circuits
- Unsealed butt connectors in wet underbody areas
- Random smaller-gauge wire
- Speaker wire in engine-bay circuits

### CAN pair repair

CAN wiring geometry matters.

If repairing a twisted CAN pair:

- Maintain conductor gauge/type.
- Preserve the twist as closely as practical.
- Keep the repaired untwisted section short.
- Do not add unnecessary long stubs.
- Seal and mechanically support the repair.

Exact Hyundai repair limits should come from the correct 2014 ETM/service information when available.

---

# 32. Temporary Field Stabilization

Temporary field action may be reasonable when the problem is **mechanical harness movement**, not internal conductor failure.

Examples:

- Re-secure a harness away from a sharp edge.
- Secure a loose splash shield that is rubbing wiring.
- Re-seat a connector with an intact lock.
- Protect an intact wire loom from further abrasion.

Do not treat these as permanent repairs:

- Bare conductor twisted together
- Critical sensor wire held by tape alone
- Exposed copper in wet conditions
- Bypassed fuse
- Jumpered relay that defeats safety control

See `../roadside/EMERGENCY_FIELD_REPAIRS.md`.

---

# 33. Diagnostic Decision Tree

```text
ELECTRICAL SYMPTOM / DTC
          ↓
PRESERVE CODES + FREEZE FRAME
          ↓
VERIFY BATTERY / SYSTEM VOLTAGE
          ↓
CHECK FUSE / SOURCE POWER
          ↓
CHECK COMPONENT GROUND
          ↓
CHECK CONNECTOR / PIN FIT
          ↓
CHECK SIGNAL OR CONTROL
          ↓
WIGGLE / LOAD / HEAT IF INTERMITTENT
          ↓
VOLTAGE DROP UNDER REAL LOAD
          ↓
SEGMENT HARNESS IF OPEN / SHORT SUSPECTED
          ↓
REPAIR ROOT CAUSE
          ↓
CLEAR ONLY AFTER EVIDENCE SAVED
          ↓
VERIFY HOT + COLD + ROAD TEST AS APPROPRIATE
```

---

# 34. Symptom Patterns

## Component dead, no DTC

Check:

- Fuse
- Power feed
- Ground
- Connector
- Relay
- Module command

## Several sensors suddenly low

Check:

- Shared 5 V reference
- Shared sensor ground
- Harness damage
- ECM power/ground

## Fault appears over bumps

Check:

- Loose connector
- Terminal tension
- Broken conductor inside insulation
- Harness rubbing / tension

## Fault appears hot only

Check:

- Heat-sensitive sensor/coil/module
- Expanding connector terminal
- Internal conductor break
- Relay contact

## Fault appears in rain / humidity

Check:

- Connector seals
- Ignition insulation
- Water intrusion
- Chafed harness

## Many U-codes after weak battery

Check voltage and charging system first.

---

# 35. What Not To Do

Do not:

- Replace a module before testing its power and grounds.
- Assume a DTC description names the failed part.
- Pierce every wire in the harness looking for voltage.
- Stuff oversized meter probes into female terminals.
- Sand connector terminals.
- Pull connectors apart by their wires.
- Ohm-test a powered circuit.
- Use an incandescent test light on a 5 V reference, CAN, or unknown module circuit.
- Apply 12 V directly to an unknown actuator.
- Use a larger fuse to stop repeated fuse failures.
- Twist CAN wires apart for long distances.
- Probe SRS squib/pretensioner circuits with a generic meter.
- Clear intermittent DTC evidence before recording it.

---

# 36. Field Electrical Kit

Useful mobile kit:

- Quality high-impedance DVOM
- Fine back-probe pins
- Fused jumper leads
- Small alligator clips
- Spare fuses of correct ratings
- Plastic trim tools
- Small terminal pick set
- Headlamp
- Inspection mirror
- Contact-safe cleaning supplies
- Automotive wire in selected common gauges
- Proper sealed crimp connectors
- Quality crimp tool
- Adhesive-lined heat shrink
- Split loom
- Fabric automotive harness tape
- Zip ties for routing / strain relief
- Small wire labels / marker

Optional advanced tools:

- Oscilloscope
- Current clamp
- Power probe used only with full understanding of circuit limitations
- Breakout leads
- Hyundai-capable enhanced scan tool

---

# 37. AI Reasoning Rules

An AI using this file must:

1. Ask what circuit function is missing before naming a failed component.
2. Distinguish **power**, **ground**, **signal**, and **control** circuits.
3. Treat connector/terminal condition as a first-class diagnostic cause.
4. Prefer loaded voltage-drop testing for high-current circuits.
5. Never recommend resistance testing on an energized circuit.
6. Never recommend a test light on CAN, SRS, 5 V reference, or unknown ECM circuits.
7. Never invent 2014 connector pin numbers or wire colors.
8. Preserve U-codes and low-voltage context before diagnosing a network failure.
9. Consider shared 5 V reference / shared ground when several sensor faults appear together.
10. Treat 60 Ω CAN resistance as context-dependent, not a universal always-on specification.
11. Treat the Hyundai 0.2 V cable/ground threshold and 0.1 V / 50 mV electronic guidance as **different test contexts**.
12. Recommend permanent automotive-quality harness repair, not household wiring methods.
13. Escalate SRS, GDI injector-driver, and unknown high-energy circuits to the correct service procedure.

---

# 38. AI Diagnostic Prompt Template

```text
Vehicle: 2014 Hyundai Accent SE 1.6 GDI automatic

Electrical symptom:

When it occurs:
- cold / hot / wet / bumps / idle / driving / load

Battery voltage:

Charging voltage:

Stored DTCs:

Pending DTCs:

U-codes:

Relevant fuse status:

Power at component:

Ground voltage drop:

Reference voltage:

Signal voltage / live data:

Connector condition:

Wiggle-test result:

Known harness damage:

Recent repairs / battery events:

Use an evidence-first diagnostic tree. Do not assume the named DTC component is failed. Do not invent wire colors, connector IDs, or pins that are not verified.
```

---

# 39. Electrical Incident Log

```text
Date:
Odometer:
Location / road conditions:
Weather:

Symptom:
Warning lights:
Stored DTCs:
Pending DTCs:
Permanent DTCs:
U-codes:
Freeze frame preserved: yes / no

Battery resting voltage:
Cranking voltage:
Charging voltage:

Circuit tested:
Power-feed result:
Ground result:
Voltage-drop result:
Continuity result:
Reference-voltage result:
Signal result:

Connector inspection:
Terminal-tension issue:
Harness damage:
Wiggle-test result:
Heat/load reproduction result:

Repair performed:
Permanent or temporary:
Post-repair verification:
Follow-up required:
```

---

# 40. Machine-Readable Summary

```yaml
vehicle:
  market: US
  year: 2014
  make: Hyundai
  model: Accent
  trim: SE
  body: five-door
  engine: 1.6L Gamma GDI
  transmission: six-speed automatic

wiring_diagnostics:
  primary_failure_modes:
    - open_circuit
    - short_to_ground
    - short_to_power
    - excessive_resistance
    - poor_terminal_tension
    - corrosion
    - intermittent_connection
    - shared_reference_failure
    - shared_ground_failure
    - network_fault

  connector_rules:
    pull_connector_body_not_wires: true
    use_fine_probe: true
    avoid_spreading_female_terminal: true
    sand_contacts: false
    verify_terminal_retention: true
    verify_latch: true

  service_family_reference:
    continuity_normal_example_ohms_max: 1
    open_example_ohms_min: 1000000
    electronic_voltage_drop_warning_v: 0.1
    five_volt_circuit_drop_warning_v: 0.05
    can_resistance_specific_test_ohms: 60

  hyundai_all_model_high_current:
    cable_ground_voltage_drop_repair_threshold_v: 0.2

  obd_dlc:
    pin_4: chassis_ground
    pin_5: signal_ground
    pin_6: CAN_H
    pin_14: CAN_L
    pin_16: battery_positive

  prohibitions:
    - do_not_ohm_test_live_circuit
    - do_not_test_srs_squibs_with_generic_ohmmeter
    - do_not_use_test_light_on_can
    - do_not_use_test_light_on_5v_reference
    - do_not_apply_12v_to_gdi_injector
    - do_not_install_higher_amp_fuse
    - do_not_invent_wire_colors_or_pin_numbers

  exact_2014_etm:
    connector_ids: UNKNOWN
    splice_ids: UNKNOWN
    ground_ids: UNKNOWN
    wire_colors: UNKNOWN unless separately verified
    module_pinouts: UNKNOWN unless separately verified
```

---

# 41. Sources

## Hyundai / same-generation service information

- Hyundai 2013 Accent 1.6L, Initial Inspection and Diagnostic Overview: connector handling, intermittent testing, harness inspection, open/short testing, continuity examples, voltage-drop guidance.
  - https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Powertrain%20Management/Computers%20and%20Control%20Systems/Testing%20and%20Inspection/Initial%20Inspection%20and%20Diagnostic%20Overview/

- Hyundai TSB 08-BE-004, Diagnosis Voltage Drop, model applicability listed as ALL: loaded battery cable / body / engine / transmission ground diagnosis.
  - https://charm.li/Hyundai/2008/Sonata%20V6-3.3L/Repair%20and%20Diagnosis/Technical%20Service%20Bulletins/Customer%20Interest/Electrical%20-%20Voltage%20Drop%20Diagnostics/

- Hyundai 2013 Accent ABS / ESC testing: DLC power/ground, CAN continuity, and a specific 60-ohm CAN resistance test configuration.
  - https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Brakes%20and%20Traction%20Control/Antilock%20Brakes%20%2F%20Traction%20Control%20Systems/Testing%20and%20Inspection/

- Hyundai 2012 Accent U0101 CAN communication description.
  - https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/A%20L%20L%20%20Diagnostic%20Trouble%20Codes%20%28%20DTC%20%29/Testing%20and%20Inspection/U%20Code%20Charts/U0101/General%20Information/

## Standard

- SAE J1962 diagnostic connector standard.
  - https://saemobilus.sae.org/standards/j1962_201607-diagnostic-connector

---

# 42. Core Doctrine

```text
ELECTRICAL FAULT
    ↓
POWER?
    ↓
GROUND?
    ↓
SIGNAL / COMMAND?
    ↓
CONNECTOR / TERMINAL?
    ↓
WIRE UNDER LOAD?
    ↓
SHARED CIRCUIT / NETWORK?
    ↓
ONLY THEN CONDEMN THE COMPONENT
```

A wire that reads continuous can still fail under load.
A component named in a DTC can still be healthy.
A connector that looks clean can still have poor terminal tension.

**Measure the circuit in the state where it fails.**
