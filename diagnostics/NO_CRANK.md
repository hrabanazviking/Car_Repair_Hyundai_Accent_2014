# 2014 Hyundai Accent SE — No-Crank Diagnostic Guide

> **Purpose:** A detailed, offline-first diagnostic workflow for a 2014 Hyundai Accent SE when the starter does not rotate the engine normally.
>
> **Core rule:** **No crank is not the same fault as crank/no-start.** First identify exactly what the starter and engine are doing.

---

## 1. Scope

This guide is written primarily for a U.S.-market **2014 Hyundai Accent SE five-door** with the 1.6 L GDI engine and six-speed automatic transmission.

Related repository files:

- `../specs/VEHICLE_BASELINE.md`
- `../specs/FUSES_AND_RELAYS.md`
- `../specs/FLUIDS_AND_CAPACITIES.md`
- `../guides/ROADSIDE_DIAGNOSTIC_TRIAGE.md`
- `OBD2_GUIDE.md`
- `../maintenance/NOMAD_SERVICE_LOG.md`

---

# 2. Define the Symptom Before Testing

The phrase **"car won't start"** is too vague for diagnosis.

Classify the symptom first.

## A. No crank / silence

Turning the key to START produces no starter rotation.

Possible observations:

- total silence
- one click
- relay click but no starter sound
- dash lights remain bright
- dash lights go very dim

## B. Rapid clicking

Repeated fast clicking usually indicates that starter-solenoid voltage is repeatedly collapsing and recovering.

Common causes include:

- discharged battery
- weak battery
- poor battery-terminal connection
- excessive resistance in a battery cable or ground

## C. Slow crank

The engine rotates, but much slower than normal.

Possible causes include:

- low battery state of charge
- failing battery
- high resistance in positive starter cable
- poor engine/battery ground
- failing starter motor
- extremely cold conditions
- excessive mechanical engine load

## D. Normal crank but engine does not start

This is **not a no-crank condition**.

Use the future `CRANK_NO_START.md` diagnostic guide.

## E. Starter spins but engine does not rotate

A high-speed whirring starter sound without normal engine rotation suggests a starter-drive / ring-gear engagement problem rather than a basic electrical no-crank fault.

## F. Engine rotates only intermittently

Examples:

- starts normally some days, silent other days
- works after shifting from Park to Neutral
- works after repeated key attempts
- worse when hot
- worse when cold

Intermittent faults are evidence-rich. Record the conditions before disturbing connectors or disconnecting the battery.

---

# 3. Hyundai Starting-System Facts

> **VERIFIED — HYUNDAI OWNER'S MANUAL / FUSE TABLE**

For the automatic-transmission 2014 Accent:

- The normal starting position is **P (Park)**.
- Hyundai states that the engine can also be started in **N (Neutral)**.
- The brake pedal should be fully depressed during normal starting.
- Hyundai warns not to operate the starter continuously for more than **10 seconds**.
- If the engine does not start, Hyundai instructs waiting roughly **5–10 seconds** before another attempt.

Relevant starting-circuit protection includes:

| Location | Label | Rating | Starting relevance |
|---|---|---:|---|
| Driver-side fuse panel | `START` | 10A | Transaxle range / start-related circuit |
| Engine compartment | `IG2` | 40A | Start relay and ignition-switch feed |
| Engine compartment | `IG1` | 40A | Ignition-switch feed |
| Engine compartment | `ALT` | 125A | Main charging/power distribution |
| Engine compartment | Start relay | relay | Starter-control circuit |

The exact physical fuse/relay label on the vehicle overrides a generic manual table if they disagree.

See `../specs/FUSES_AND_RELAYS.md`.

---

# 4. Safety First

Before starter diagnosis:

1. Park on stable ground.
2. Apply the parking brake.
3. Place the automatic transmission in Park unless a specific Neutral test is being performed.
4. Keep hands, clothing, tools, meter leads, and hair away from belts and other moving parts.
5. Treat the engine as capable of starting unexpectedly during electrical tests.
6. Do not crawl under a vehicle supported only by a jack.
7. Remove jewelry when working around the battery and starter power cable.
8. Protect eyes around batteries.

## Never do this

Do **not** bridge starter terminals with a screwdriver or other metal object.

Do **not** bypass the Park/Neutral safety function for routine diagnosis.

Do **not** install larger fuses.

Do **not** repeatedly hammer the starter with long crank attempts.

Do **not** connect a meter configured for current measurement directly across the battery.

The starter circuit can carry several hundred amps. An accidental short can cause burns, fire, battery damage, welded tools, or wiring damage.

---

# 5. Master No-Crank Decision Tree

```text
TURN KEY TO START
      │
      ├── Normal engine cranking
      │      └── Not a no-crank fault → use CRANK_NO_START.md
      │
      ├── No electrical power / dash dark
      │      ├── Battery discharged?
      │      ├── Battery terminals loose/corroded?
      │      ├── Main cable/ground open?
      │      └── Main fuse/distribution fault?
      │
      ├── Rapid clicking
      │      ├── Battery state of charge
      │      ├── Battery condition under load
      │      ├── Terminal resistance
      │      └── Cable/ground voltage drop
      │
      ├── One click
      │      ├── Battery/load capacity
      │      ├── Positive cable voltage drop
      │      ├── Ground-side voltage drop
      │      ├── Starter solenoid/motor
      │      └── Engine mechanically locked?
      │
      ├── Complete silence but dash normal
      │      ├── Try Neutral
      │      ├── START fuse
      │      ├── IG1 / IG2 feeds
      │      ├── Start relay
      │      ├── Range-switch circuit
      │      ├── Ignition-switch/start command
      │      └── Starter-solenoid control circuit
      │
      └── Slow crank
             ├── Battery charge/health
             ├── Positive-cable drop
             ├── Ground-cable drop
             ├── Starter condition
             └── Mechanical engine resistance
```

---

# 6. Step Zero — Preserve Evidence

Before disconnecting the battery, record:

- date
- mileage
- outside temperature
- engine hot/cold
- how long vehicle had been parked
- battery voltage before attempting start
- dashboard behavior
- exact sound
- whether headlights dim greatly during START
- whether Park and Neutral behave differently
- any recent electrical work
- any recent battery discharge
- any water exposure or rough-road impact
- stored/pending DTCs if the scanner communicates

If the failure is intermittent, this information can be more valuable than the failed start itself.

Log the incident in `../maintenance/NOMAD_SERVICE_LOG.md`.

---

# 7. First 60-Second Roadside Check

Before using tools:

1. Verify transmission is firmly in **Park**.
2. Press the brake pedal fully.
3. Attempt one normal start.
4. Observe the dashboard and interior lights.
5. Listen carefully.
6. Try starting in **Neutral**.
7. Inspect battery terminals visually.
8. Look for a loose or disconnected battery cable.
9. Smell for burned wiring.
10. Stop immediately if cables smoke or become dangerously hot.

The Park-versus-Neutral comparison is unusually useful because the automatic Accent uses a transaxle range circuit in the starting logic.

---

# 8. Park vs. Neutral Test

The 2014 automatic Accent can start in Park or Neutral.

Perform this test safely with the brake firmly applied and parking brake set.

```text
WILL NOT CRANK IN PARK
        ↓
Try Neutral
        ↓
CRANKS IN NEUTRAL?
   ├── YES
   │    ↓
   │  Strongly investigate:
   │  - transaxle range switch
   │  - range-switch adjustment
   │  - connector/wiring
   │  - shifter/range recognition
   │
   └── NO
        ↓
Continue battery/start-circuit diagnosis
```

A Neutral-only start does **not** automatically prove the range switch itself is defective. Wiring, connectors, mechanical adjustment, or shift-linkage issues can create the same symptom.

---

# 9. Battery Open-Circuit Voltage

Measure directly on the **battery posts**, not on the cable clamps, for the initial battery reading.

General lead-acid reference values around room temperature:

| Resting voltage | Approximate state of charge |
|---:|---:|
| 12.60–12.72 V | ~100% |
| 12.45 V | ~75% |
| 12.30 V | ~50% |
| 12.15 V | ~25% |

> **GENERAL DIAGNOSTIC PRACTICE — FLUKE REFERENCE**
>
> Temperature, surface charge, battery chemistry, battery age, and recent charging affect these readings. Resting voltage indicates state of charge better than battery health.

A battery can read approximately 12.6 V with no load yet fail badly when asked to operate the starter.

Therefore:

```text
GOOD RESTING VOLTAGE ≠ PROVEN GOOD BATTERY
```

If surface charge may be present, briefly applying a moderate load such as headlights and then allowing the voltage to settle can improve the usefulness of the resting measurement.

---

# 10. Measure Voltage During the Start Attempt

Use a multimeter with MIN/MAX capture if available.

1. Measure directly across the battery posts.
2. Have an assistant attempt to start the engine, or use a safe meter capture feature.
3. Record minimum voltage.
4. Compare the result with battery condition, temperature, and starter behavior.

A severe collapse in battery voltage during START suggests one or more of:

- discharged battery
- internally weak battery
- extremely high starter current
- mechanical engine/starter problem

A battery load tester or conductance tester can provide better battery-health information than voltage alone.

Do not condemn the starter based on battery voltage alone.

---

# 11. Battery Terminal Check

A terminal can look acceptable and still have enough resistance to stop the starter.

Inspect for:

- loose clamps
- white/green corrosion
- cracked terminal ends
- damaged strands
- overheated cable insulation
- previous clamp repairs
- loose negative cable at body/engine ground

## Post-to-clamp voltage-drop test

During a start attempt:

- Place one meter probe on the actual battery post.
- Place the other probe on the cable clamp attached to that same post.

A healthy clean connection should show essentially no meaningful voltage drop.

Measurable drop across the post/clamp interface under starter load indicates resistance at that connection.

This test can expose a terminal that looks clean from the outside but is electrically poor.

---

# 12. Starter-Circuit Voltage-Drop Testing

> **GENERAL DIAGNOSTIC PRACTICE — FLUKE**

Voltage-drop testing evaluates the circuit **while current is flowing**. This is usually far more useful in a high-current starter circuit than an unloaded continuity test.

Fluke gives a general starter-circuit guideline of approximately:

- **0.3 V** positive-side drop
- **0.2 V or less** ground-side drop
- roughly **0.2–0.5 V total** starter-circuit drop

These are general diagnostic guidelines, not Hyundai factory specifications for this exact model.

If Hyundai build-specific service data supplies different limits, use the Hyundai limits.

---

# 13. Positive-Side Voltage Drop

Purpose: detect resistance between battery positive and starter positive feed.

General procedure:

1. Parking brake set.
2. Transmission in Park or Neutral.
3. Meter set to DC volts.
4. Red probe on battery **positive post**.
5. Black probe on the starter's main battery-feed terminal.
6. Attempt to crank for only a few seconds.
7. Record voltage drop.

Excessive drop can result from:

- corroded battery terminal
- damaged cable
- loose starter-terminal connection
- internal cable corrosion
- poor junction/fusible connection

## Safety warning

The starter battery terminal is electrically hot and unfused or very heavily fused depending on the path. Avoid accidental contact between the terminal/tool and chassis/engine metal.

If safe access is not available, do not improvise underneath the vehicle.

---

# 14. Ground-Side Voltage Drop

Purpose: detect excessive resistance between starter/engine ground and battery negative.

General procedure:

1. Red probe on clean starter housing or engine block metal.
2. Black probe on battery **negative post**.
3. Attempt to crank for a few seconds.
4. Record voltage drop.

Excessive ground-side drop can result from:

- loose battery-negative terminal
- damaged negative cable
- poor body ground
- poor engine/transmission ground strap
- corrosion between ground lug and metal

A ground cable can pass a continuity test yet fail badly when carrying starter current.

---

# 15. Why Continuity Tests Can Mislead

An ohmmeter uses tiny current.

A starter uses enormous current.

A cable with only a few corroded strands remaining may beep for continuity yet fail to deliver enough current to crank the engine.

Therefore:

```text
CONTINUITY TEST
      ↓
Confirms a path exists

VOLTAGE-DROP TEST UNDER LOAD
      ↓
Shows whether that path can actually carry useful current
```

For starter faults, load testing is often the stronger test.

---

# 16. Symptom: Rapid Clicking

Rapid starter/relay clicking usually means system voltage falls below the level needed to keep the solenoid/relay engaged, then recovers when the load disconnects, producing a repeating cycle.

Diagnostic order:

1. Measure battery resting voltage.
2. Inspect/tighten battery terminals.
3. Attempt a known-safe jump start if appropriate.
4. Measure cranking/start-attempt voltage.
5. Test terminal voltage drop.
6. Test positive cable voltage drop.
7. Test ground-side voltage drop.
8. Battery-test if the problem remains.

Do not immediately replace the starter.

---

# 17. Symptom: One Solid Click

One substantial click can mean the control circuit is successfully commanding the starter solenoid but the starter motor is not rotating.

Possible causes:

- battery voltage/current inadequate under load
- high resistance in battery cables
- poor ground
- failed starter solenoid contacts
- failed starter motor
- starter drive jammed
- engine mechanically unable to rotate

Diagnostic order:

```text
ONE CLICK
   ↓
Battery known charged and healthy?
   ↓
Positive-side voltage drop acceptable?
   ↓
Ground-side voltage drop acceptable?
   ↓
Starter receives correct control command?
   ↓
Starter/motor fault or mechanical lock becomes more likely
```

Do not condemn the starter until cable integrity and battery capability are established.

---

# 18. Symptom: Complete Silence, Dash Normal

If lights and dashboard appear normal but there is no click and no starter activity:

First inspect/test:

1. Park versus Neutral behavior
2. `START` 10A fuse
3. `IG2` 40A feed
4. `IG1` 40A feed
5. Start relay
6. Transaxle range-switch circuit
7. Ignition-switch START command
8. Starter-solenoid control circuit
9. Related connectors/grounds

The `START` fuse and range circuit are especially important on the automatic-transmission car.

---

# 19. Start Relay Diagnosis

The engine-compartment fuse/relay box contains a start-relay position according to Hyundai's 2014 documentation.

A relay diagnosis may include:

- verify relay feed power
- verify relay coil command
- verify relay ground/control path
- verify switched output
- test relay outside the vehicle if proper pinout is known
- substitute only a **known identical relay with matching pinout and rating** when appropriate

Do not assume two relays are interchangeable because the plastic housings look identical.

Do not bridge relay-socket terminals blindly.

The vehicle's fuse-box lid/label outranks a generic diagram.

---

# 20. Starter-Solenoid Control Voltage

If the battery and cables test correctly but the starter remains silent, determine whether the starter solenoid receives a proper START command.

Two broad outcomes:

```text
CORRECT START COMMAND REACHES SOLENOID
                ↓
Starter/solenoid, main power feed,
ground, or mechanical problem becomes more likely
```

```text
NO START COMMAND AT SOLENOID
                ↓
Work upstream:
START fuse → relay → range switch → ignition switch/control → wiring
```

Because starter access may require working near high-current terminals and moving components, do not improvise if the connector cannot be safely reached.

---

# 21. Slow-Crank Diagnosis

A slow crank differs from total no-crank because current is reaching the starter.

Diagnostic sequence:

1. Battery state of charge
2. Battery health/load capability
3. Battery post/clamp integrity
4. Positive starter-cable voltage drop
5. Engine/starter ground voltage drop
6. Starter motor condition
7. Mechanical engine drag
8. Oil viscosity/extreme cold conditions

## Useful clue

If cranking speed becomes dramatically better with a known-good booster source, battery state/health or connection resistance rises on the suspect list.

It does not automatically prove the battery alone is bad; the booster connection may also temporarily improve a poor terminal connection.

---

# 22. Starter Spins but Engine Does Not Turn

Listen carefully.

A smooth, high-speed electric whir with no normal engine compression rhythm can indicate that the starter motor spins but the drive is not engaging the engine ring gear.

Possible causes:

- starter drive / overrunning clutch fault
- solenoid engagement problem
- damaged ring-gear teeth
- starter mounting/alignment problem

Do not confuse this sound with an engine that cranks unusually fast because it has lost compression.

Confirm visually/diagnostically whether the crankshaft actually rotates before choosing a repair path.

---

# 23. Intermittent No-Crank

Intermittent failures deserve detailed logging.

Record whether the problem correlates with:

- hot engine
- cold engine
- rain/humidity
- rough-road travel
- steering/shifter position
- Park versus Neutral
- repeated key cycling
- battery charging
- recent jump start

Possible intermittent causes include:

- loose battery terminal
- internally failing battery
- corroded cable
- failing starter solenoid
- worn starter motor
- range-switch fault/adjustment
- ignition-switch electrical fault
- relay/contact fault
- loose connector
- damaged wiring

Avoid disturbing connectors before recording the failed state whenever practical.

---

# 24. Hot No-Crank vs. Cold No-Crank

## Fails mainly when hot

Possible directions:

- starter/solenoid heat-related failure
- increased resistance at a marginal connection
- relay/contact fault
- mechanical heat-related issue

## Fails mainly when cold

Possible directions:

- weak battery with reduced cold output
- thickened engine oil
- marginal connection resistance
- temperature-sensitive starter fault

Temperature correlation is evidence, not diagnosis.

---

# 25. Headlight Observation Test

This is only a rough preliminary clue, not a substitute for meter testing.

Observe headlights/interior lighting during a start attempt.

### Lights become extremely dim

Possible high-current load or weak supply:

- discharged/weak battery
- poor high-current connection
- starter drawing excessive current
- mechanically locked starter/engine

### Lights barely change and starter is silent

Possible control-side fault:

- START circuit
- range switch
- ignition switch
- start relay
- solenoid-control wiring

These are trends, not proof.

---

# 26. Safe Jump-Starting

> **VERIFIED — HYUNDAI OWNER'S MANUAL**

Hyundai specifies a **12-volt** booster system.

Do not use a 24-volt source.

The factory procedure instructs connecting:

1. positive cable to the discharged battery positive terminal
2. other positive end to booster positive
3. negative cable to booster negative
4. final negative connection to a solid stationary metallic engine/body ground point away from the discharged battery

Hyundai specifically warns against connecting the final negative jumper directly to the discharged battery's negative terminal.

Keep vehicles from touching when using another vehicle as the booster source.

Keep sparks/flames away from the battery.

Do not jump-start a frozen battery.

### Diagnostic meaning of a successful jump

If the Accent cranks normally with a booster:

Investigate:

- discharged battery
- failing battery
- charging-system fault
- parasitic drain
- poor terminals/cables

A jump start gets the engine running; it does not identify why the battery became unable to crank the engine.

---

# 27. Automatic Transmission: Do Not Push-Start

> **VERIFIED — HYUNDAI OWNER'S MANUAL**

The automatic-transmission Accent cannot be push-started.

Do not attempt to tow-start it.

Use correct jump-starting, diagnosis, repair, or towing procedures.

---

# 28. Could the Engine Be Mechanically Locked?

Mechanical seizure is much less common than battery/cable faults, but it must remain in the diagnostic tree when the starter receives substantial current yet the engine does not rotate.

Possible causes include:

- internal engine seizure
- liquid/hydrolock in a cylinder
- seized accessory driven by the belt
- starter mechanically jammed

Clues may include:

- one heavy click with major voltage drop
- starter/cables heating rapidly
- recent overheating
- recent coolant ingestion symptoms
- abnormal mechanical noise before shutdown
- sudden stop while running

Do not repeatedly energize the starter against a mechanically locked engine.

Mechanical rotation testing should be performed only with the correct tools, correct crankshaft direction/procedure, and verified service information.

---

# 29. Battery Is Repeatedly Dead

If the battery is repeatedly discharged, the no-crank event may be a symptom of another problem.

Investigate:

- alternator/charging output
- loose/corroded battery connections
- battery age/condition
- parasitic draw
- lamp left on
- module failing to sleep
- aftermarket accessory draw
- damaged wiring

Do not repeatedly replace batteries without determining why they discharge.

---

# 30. Low Voltage Can Create Secondary Codes

A weak battery or severe voltage drop can create multiple module faults and communication codes.

If a scan after a failed start shows a swarm of seemingly unrelated DTCs:

1. preserve the codes
2. verify battery/system voltage
3. repair the primary voltage problem
4. retest modules afterward

Do not replace multiple control modules because they all complained during a brownout.

---

# 31. Diagnostic Results Matrix

| Finding | What it suggests | Next step |
|---|---|---|
| Battery very low at rest | Discharged battery | Charge/test battery; find reason for discharge |
| Battery voltage collapses severely under START | Weak/discharged battery or extreme current load | Battery load test + starter/cable diagnosis |
| Large post-to-clamp drop | Poor terminal connection | Clean/repair terminal |
| Excessive positive-side starter drop | Cable/connection resistance | Isolate cable/junction drop |
| Excessive ground-side drop | Ground cable/connection resistance | Inspect/repair engine/body ground path |
| Starts in Neutral but not Park | Range-recognition problem likely | Test range switch, adjustment, wiring |
| START fuse repeatedly blows | Short/overload | Stop replacing fuses; diagnose circuit |
| Start relay commanded but no output | Relay/contact/feed problem | Test feed/relay/output |
| Proper solenoid command + good main power/ground + no crank | Starter/solenoid or mechanical problem likely | Test starter/mechanical rotation |
| No solenoid command | Upstream control fault | Work toward relay/range/ignition circuit |
| Booster restores normal crank | Battery/connection/charging problem likely | Test battery, cables, charging system |

---

# 32. What NOT to Replace Based on One Symptom

Do not replace the starter simply because:

- it clicked once
- the engine did not crank
- a jump start worked
- the car is old

Do not replace the battery simply because:

- it is discharged
- voltage is low after repeated starting attempts
- a charging fault exists

Do not replace the range switch merely because:

- Park failed once
- Neutral worked once

Each of those observations narrows the diagnosis. None is conclusive by itself.

---

# 33. Roadside Minimal Tool Set for No-Crank Diagnosis

Useful tools:

- digital multimeter with MIN/MAX if available
- 12 V jump pack
- battery-terminal brush
- metric socket/wrench set
- flashlight/headlamp
- fuse puller
- correct spare fuses
- OBD-II scanner
- safety glasses
- gloves

Optional but useful:

- battery conductance tester
- DC current clamp capable of starter current
- long test leads
- small wire brush

Do not carry improvised starter-jumper tools as a diagnostic strategy.

---

# 34. AI Diagnostic Input Template

```text
Vehicle: 2014 Hyundai Accent SE 1.6 GDI automatic
Mileage:
Outside temperature:
Engine hot/cold:
Time parked before failure:

No-crank type:
- silence
- rapid clicks
- one click
- slow crank
- intermittent
- starter spins but engine does not rotate

Dash lights normal?:
Headlights during START:
Starts in Park?:
Starts in Neutral?:

Battery resting voltage at POSTS:
Minimum battery voltage during START:
Positive-side starter voltage drop:
Ground-side starter voltage drop:
Post-to-clamp voltage drop:

START 10A fuse status:
IG2 40A fuse status:
IG1 40A fuse status:
Start relay test/result:
Starter-solenoid control voltage during START:

Stored DTCs:
Pending DTCs:
Recent battery/charging history:
Recent repairs:
Recent rough-road/water exposure:

Rank likely causes using the evidence above.
Do not recommend replacing a starter, battery, relay, or range switch
until tests distinguish it from the other plausible causes.
Identify unsafe tests and do not recommend bypassing safety interlocks.
```

---

# 35. Machine-Readable Diagnostic Summary

```yaml
vehicle:
  year: 2014
  make: Hyundai
  model: Accent
  trim: SE
  engine: 1.6L_GDI
  transmission: 6_speed_automatic

no_crank:
  first_checks:
    - battery_state_of_charge
    - battery_terminal_condition
    - park_vs_neutral
    - START_10A_fuse
    - IG2_40A_fuse
    - IG1_40A_fuse
    - start_relay
    - starter_circuit_voltage_drop
  factory_start_positions:
    - Park
    - Neutral
  max_starter_engagement_seconds: 10
  retry_wait_seconds: "5-10"

starter_voltage_drop_general_guidelines:
  source_type: general_diagnostic_practice
  source: Fluke
  positive_side_v: "~0.3"
  ground_side_v: "~0.2_or_less"
  total_v: "~0.2-0.5"
  note: "Not a Hyundai model-specific factory specification"

starting_circuit:
  interior_START_fuse_a: 10
  engine_IG2_fuse_a: 40
  engine_IG1_fuse_a: 40
  start_relay: true
  range_switch_relevant: true

safety:
  automatic_push_start: prohibited
  use_24v_booster: prohibited
  bridge_starter_terminals: prohibited
  bypass_range_interlock: prohibited
  replace_fuse_with_higher_rating: prohibited
```

---

# 36. Source Notes

## Hyundai sources

Primary vehicle-specific information comes from the 2014 Hyundai Accent Owner's Manual, including:

- starting procedure
- Park/Neutral start capability
- starter duty-cycle warning
- emergency jump-start procedure
- automatic-transmission push-start prohibition
- fuse/relay descriptions

Useful public copies:

- https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual
- https://manualzz.com/doc/53857913/hyundai-2014-accent-owner-manual
- Hyundai Canada 2014 Accent maintenance/fuse section: https://www.hyundaicanada.com/-/media/hyundai/feature/ownerssection/manuals/english/2014/accent/rb-cane-7.pdf

## Electrical-diagnostic source

General starter-circuit voltage-drop practices and battery state-of-charge references are based on Fluke automotive diagnostic documentation:

- https://www.fluke.com/en-us/learn/blog/digital-multimeters/how-to-check-starter-circuit-voltage-drop-with-a-multimeter
- https://www.fluke.com/en/learn/blog/automotive/electrical-automotive-troubleshooting

These general electrical thresholds are clearly labeled as **general diagnostic practice**, not Hyundai factory specifications.

---

# 37. Core Diagnostic Philosophy

```text
NO CRANK
   ↓
CLASSIFY THE SOUND / BEHAVIOR
   ↓
VERIFY BATTERY ENERGY
   ↓
VERIFY CONNECTIONS UNDER LOAD
   ↓
VERIFY PARK / NEUTRAL LOGIC
   ↓
VERIFY FUSES / RELAY / START COMMAND
   ↓
VERIFY STARTER POWER + GROUND
   ↓
ONLY THEN CONDEMN THE STARTER
```

The starter is the last large component in a chain of power and control. Diagnose the chain before firing the parts cannon.

---

## Document Status

- **Vehicle:** 2014 Hyundai Accent SE
- **System:** Starting / no-crank diagnosis
- **Status:** Initial detailed diagnostic guide
- **Vehicle-specific facts:** Hyundai-owner-manual based
- **Electrical thresholds:** General professional diagnostic references, explicitly labeled
- **Design:** Offline-first, human-readable, AI/RAG-friendly
- **Safety philosophy:** Measure before bypassing; never defeat starting safety interlocks for routine diagnosis
