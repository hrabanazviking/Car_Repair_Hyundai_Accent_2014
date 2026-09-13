# Body Control, Door-Ajar, Tailgate & Interior-Lighting Diagnostics — 2014 Hyundai Accent SE

> **Purpose:** diagnose door-ajar, tailgate, room/map/luggage-lamp, keyless-entry, warning-chime, door-lock, and body-control symptoms without confusing a switch input, lamp load, fuse, wiring fault, or BCM/body-control problem with one another.

## Source Confidence

- **EXACT 2014 OWNER DATA** — Hyundai 2014 Accent owner-manual behavior and fuse information.
- **EXACT 2014 PARTS DATA** — 2014 Accent parts-catalog evidence, VIN/build verification still required.
- **SERVICE-FAMILY — 2012/2013 ACCENT** — same-generation RB Accent service information used as supporting diagnostic evidence where exact 2014 workshop text is not publicly available.
- **GENERAL ELECTRICAL PRACTICE** — standard automotive low-voltage diagnostic methods, clearly separated from Hyundai-specific specifications.

Primary sources are linked in [Sources](#sources).

---

## Core Rule

```text
LIGHT STAYS ON
DOOR-AJAR INDICATOR WRONG
LOCKS / CHIMES BEHAVE STRANGELY
BATTERY DRAINS
        ↓
DO NOT ASSUME "BAD BCM"
        ↓
VERIFY THE INPUT
VERIFY THE FEED
VERIFY THE LOAD
VERIFY THE WIRING
VERIFY THE CONTROL LOGIC
```

The body-control system acts on information from switches and other inputs. A bad input can make a healthy controller behave exactly as commanded by the bad information.

A tiny mechanical switch can therefore create a surprisingly large electrical symptom.

---

# 1. System Overview

The 2014 Accent body/interior-lighting system includes several interacting pieces:

- door-jamb / door-ajar switches,
- tailgate or trunk-open sensing,
- map lamp,
- center/room lamp,
- luggage-room lamp on the 5-door,
- door-lock / unlock relays and actuators,
- remote transmitter inputs,
- warning chime logic,
- instrument-cluster indications,
- body control module (BCM),
- interior fuse/junction-box power distribution,
- ignition-state inputs,
- and wiring/connectors between all of the above.

The simplified logic is:

```text
DOOR / TAILGATE / KEY / REMOTE INPUT
                ↓
        BODY-CONTROL LOGIC
                ↓
     LAMP / LOCK / CHIME OUTPUT
                ↓
          TIMER / SLEEP STATE
```

A failure anywhere in that chain can look like a failure somewhere else.

Examples:

```text
BAD DOOR SWITCH
    ↓
BCM SEES "DOOR OPEN"
    ↓
ROOM LAMP / CHIME / LOCK LOGIC
BEHAVES AS IF DOOR IS OPEN
```

or:

```text
ROOM LAMP DOES NOT LIGHT
        ↓
COULD BE:
BULB / LAMP ASSEMBLY
ROOM-LAMP FUSE
DOOR SWITCH
WIRING
GROUND / CONTROL PATH
BCM INPUT OR OUTPUT
```

---

# 2. Exact 2014 Interior-Lamp Behavior

## Automatic shutoff

**EXACT 2014 OWNER DATA**

Hyundai states that, if equipped, the interior lamps automatically turn off approximately **20 minutes after the ignition switch is turned off**.

This is battery-protection logic.

It does **not** mean every possible body-electrical load is guaranteed to shut off after exactly 20 minutes.

It also does not prove that a lamp or module behaving abnormally is harmless.

See:

- `https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/14`
- `https://www.dezosmanuals.com/wp-content/uploads/2021/07/2014-Hyundai-Accent-OM.pdf`

## DOOR-mode behavior

**EXACT 2014 OWNER DATA**

With the map/room lamp switch in **DOOR** mode:

- the map and room lamps come on when a door is opened,
- this occurs regardless of ignition-switch position,
- unlocking with the transmitter can illuminate the lamps for approximately 30 seconds while the doors remain closed,
- locking all doors or switching ignition ON turns that courtesy illumination off immediately,
- a door opened with ignition in ACC or LOCK can keep the lamp illuminated for about 20 minutes,
- a door opened with ignition ON can keep the lamp illuminated continuously.

These behaviors are extremely useful diagnostically because they allow the technician to compare **commanded body logic** with the physical door state.

## Manual ON mode

**EXACT 2014 OWNER DATA**

If the lamp is manually placed in **ON**, it can remain illuminated independent of door state.

Do not diagnose a door-switch fault until the lamp switch position has been verified.

## Manual OFF mode

**EXACT 2014 OWNER DATA**

In **OFF**, the room lamp remains off even when a door is opened.

Again, lamp-switch position must be verified before diagnosing a switch or controller.

---

# 3. 5-Door Luggage-Room Lamp

This repository is centered on the **2014 Accent SE 5-door**.

**EXACT 2014 OWNER DATA**

Hyundai states that the luggage-room lamp comes on when the tailgate is opened and warns that the tailgate should be closed securely to prevent unnecessary charging-system drain.

```text
TAILGATE OPEN
     ↓
LUGGAGE LAMP ON
```

The luggage lamp should therefore be treated as a separate diagnostic branch from the passenger-compartment map/room-lamp DOOR logic.

### Important battery-drain clue

A tailgate that is physically shut but electrically reported as open can create a hidden or intermittent battery-drain condition.

Possible causes include:

- latch/switch not reaching its normal closed position,
- latch contamination,
- mechanical misalignment,
- worn switch contacts,
- damaged tailgate wiring,
- connector corrosion,
- or body-control input trouble.

Do not assume the lamp itself is the root cause merely because it is the visible load.

Source:

- `https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/14`

---

# 4. Exact 2014 Fuse Anchors

## ROOM LP 1 — 10 A

**EXACT 2014 OWNER DATA**

The 2014 instrument-panel fuse table lists:

```text
ROOM LP 1 — 10 A
```

Protected components include:

- instrument-cluster indicator/illumination circuits,
- TPMS module,
- BCM,
- A/C control module,
- luggage-room lamp,
- trunk-room lamp,
- center room lamp,
- overhead-console lamp,
- map lamp.

This is a crucial shared-feed clue.

```text
MULTIPLE ROOM / BODY FUNCTIONS DEAD
              ↓
CHECK ROOM LP 1 FEED
BEFORE CONDEMNING MULTIPLE COMPONENTS
```

Source:

- `https://www.hyundaicanada.com/-/media/hyundai/feature/ownerssection/manuals/english/2014/accent/rb-cane-7.pdf`

## DR LOCK — 20 A

**EXACT 2014 OWNER DATA**

The 2014 panel lists:

```text
DR LOCK — 20 A
```

feeding the:

- door lock/unlock relay,
- two-turn unlock relay,
- driver-door lock actuator.

This does not mean every door-lock complaint is caused by this fuse, but a multi-door lock failure should begin with feed verification.

## IG2 body-control feed

The 2014 panel also lists a 10 A IG2 branch feeding, among other loads, the BCM.

A body-control symptom that changes with ignition state therefore warrants checking both always-hot and ignition-switched feeds rather than assuming the module itself has failed.

Sources:

- `https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/2/?srch=fuse`
- `https://www.hyundaicanada.com/-/media/hyundai/feature/ownerssection/manuals/english/2014/accent/rb-cane-7.pdf`

---

# 5. Exact 2014 Door-Jamb Switch Hardware

**EXACT 2014 PARTS DATA**

The 2014 Accent parts catalog lists door-jamb / door-ajar switch assemblies, including:

```text
93560-3L000
```

for applicable 2014 Accent configurations.

Another production/configuration-dependent switch is also cataloged, so **VIN and installed hardware remain the final authority**.

The catalog explicitly describes the component as a door-ajar / door-jamb switch.

Source:

- `https://www.hyundaipartsdeal.com/oem-2014-hyundai-accent-door_jamb_switch.html`

### Diagnostic implication

This generation does not require every door-open input to be inferred from a lock motor or software state. Same-generation documentation identifies discrete door switches at individual doors.

A bad switch can therefore produce a local symptom even when the door-lock actuator itself still works normally.

---

# 6. Same-Generation Door-Switch Layout

**SERVICE-FAMILY — 2012 ACCENT**

The same-generation service library identifies distinct connector/component entries for:

```text
F05  Driver Door Switch
F06  Passenger Door Switch
F07  Rear Door Switch LH
F08  Rear Door Switch RH
F14  Luggage Room Lamp (5DR)
```

It also identifies trunk/liftgate switch hardware in the body-electrical service tree.

This strongly supports treating each door input as an individually diagnosable branch.

Source:

- `https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/`

---

# 7. BCM Role

**SERVICE-FAMILY — 2013 ACCENT**

Same-generation 2013 Accent service information includes a dedicated BCM electrical diagram and BCM connector documentation.

Source:

- `https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Diagrams/Electrical%20Diagrams/Body%20Control%20Module/`

The BCM should be viewed as a controller receiving inputs and commanding outputs, not as the first component to replace when several body functions behave strangely.

### Before condemning a BCM, prove:

1. battery voltage is healthy,
2. BCM B+ feeds are present,
3. ignition-switched feeds are present,
4. grounds are healthy under load,
5. door/tailgate inputs make sense,
6. affected lamp/lock loads and wiring are intact,
7. connectors are seated and free of water/corrosion,
8. communication with the module is normal if a capable scan tool is available.

```text
BAD INPUT
CAN MAKE A GOOD BCM
MAKE A BAD DECISION
```

---

# 8. Door-Ajar Diagnostic Strategy

## Symptom: door is open but car thinks it is closed

Possible symptoms:

- room/map lamps do not respond in DOOR mode,
- door-open indicator does not respond,
- warning chime behavior is missing,
- remote/lock logic behaves unexpectedly,
- battery-saver behavior may differ from expectation.

Diagnostic order:

```text
VERIFY LAMP SWITCH MODE
        ↓
COMPARE OTHER DOORS
        ↓
OBSERVE CLUSTER / SCAN DATA IF AVAILABLE
        ↓
OPERATE SUSPECT DOOR SWITCH BY HAND
        ↓
CHECK CONNECTOR
        ↓
CHECK SWITCH CONTINUITY / STATE CHANGE
        ↓
CHECK WIRING TO BODY CONTROL
```

## Symptom: door is closed but car thinks it is open

Possible symptoms:

- door-ajar indication remains active,
- courtesy lamps remain commanded on,
- chime logic activates unexpectedly,
- remote locking or alarm logic may behave differently,
- body-control sleep can be delayed,
- battery drain may occur.

Do not immediately replace the BCM.

Start at the physical switch and door alignment.

### Mechanical checks

Inspect for:

- switch plunger not being fully depressed,
- bent switch bracket/body contact area,
- loose switch,
- damaged rubber boot,
- door sag or striker misalignment,
- contamination,
- water intrusion,
- crushed harness near the jamb.

A switch can be electrically good on the bench yet fail in the vehicle because the door never pushes it far enough.

---

# 9. Switch Continuity Testing

**GENERAL ELECTRICAL PRACTICE with same-generation Hyundai support**

Hyundai service procedures on related same-era vehicles diagnose door and tailgate switches by checking continuity/state change across the switch circuit.

Same-generation Accent service documentation also identifies discrete door switches.

The safe generic method is:

1. ignition OFF,
2. disconnect the switch if required,
3. identify the correct terminals from the wiring diagram,
4. measure continuity/resistance while operating the switch,
5. verify a clean repeatable state transition,
6. wiggle the connector and harness while observing the reading.

Do not assume the switch is simply "normally open" or "normally closed" without checking the actual diagram or observed circuit behavior.

### A useful test result

```text
SWITCH CHANGES CLEANLY
AT SWITCH CONNECTOR
BUT BCM / CLUSTER DATA DOES NOT CHANGE
        ↓
HARNESS / CONNECTOR / MODULE INPUT PATH
MOVES HIGHER ON SUSPECT LIST
```

---

# 10. Scan-Tool Input-State Testing

A capable Hyundai-aware scan tool can be extremely valuable for body diagnostics.

Instead of guessing from the lamp alone, observe body/BCM current data when available:

```text
DRIVER DOOR: OPEN / CLOSED
PASSENGER DOOR: OPEN / CLOSED
REAR LH: OPEN / CLOSED
REAR RH: OPEN / CLOSED
TAILGATE: OPEN / CLOSED
LOCK / UNLOCK INPUTS
IGNITION STATE
```

Exact data-list naming varies by scan tool and control-module implementation.

### Why this is powerful

If the physical door is closed but scan data says OPEN:

```text
THE CONTROLLER IS RECEIVING
OR INTERPRETING AN OPEN SIGNAL
```

That is very different from:

```text
SCAN DATA SAYS CLOSED
BUT LAMP REMAINS ON
```

The second case pushes diagnosis toward output control, lamp circuit, manual switch mode, or wiring rather than the door input itself.

---

# 11. Interior Lamp Does Not Work

## One lamp only dead

Likely branches include:

- failed bulb/LED assembly,
- lamp switch/contact,
- local connector,
- local ground/control path,
- local harness damage.

## Several interior lamps dead

Check:

1. `ROOM LP 1` 10 A fuse,
2. fuse power on both sides,
3. BCM/body-control power and ground,
4. lamp-switch mode,
5. common wiring/connectors,
6. scan-tool body inputs if available.

Do not replace multiple lamp assemblies before proving their common feed.

See:

- [`POWER_DISTRIBUTION.md`](POWER_DISTRIBUTION.md)
- [`WIRING_AND_CONNECTOR_DIAGNOSTICS.md`](WIRING_AND_CONNECTOR_DIAGNOSTICS.md)
- [`FUSES_AND_RELAYS.md`](../specs/FUSES_AND_RELAYS.md)

---

# 12. Interior Lamp Stays On

First eliminate normal operation.

Check:

- lamp switch accidentally in ON,
- one map lamp manually pressed on,
- one door actually open,
- tailgate not fully latched,
- expected courtesy-delay period still active.

Then test for abnormal inputs.

```text
LAMP STAYS ON
AFTER NORMAL DELAY
        ↓
VERIFY SWITCH POSITION
        ↓
CHECK EACH DOOR INPUT
        ↓
CHECK TAILGATE INPUT / LUGGAGE LAMP
        ↓
CHECK FOR STUCK SWITCH / HARNESS SHORT
        ↓
CHECK BCM OUTPUT / BODY LOGIC
```

### Important exact-owner-data nuance

The owner manual states that pressing an individual map-lamp lens ON can keep that lamp on even if the central selector is in OFF.

So always inspect the actual lamp controls before escalating the diagnosis.

---

# 13. Luggage Lamp Stays On With Tailgate Closed

This is especially relevant to the 5-door SE.

## First inspection

- verify lamp is truly on after the hatch is fully latched,
- check whether the tailgate-open indication agrees with reality,
- reopen and firmly reclose the hatch,
- inspect latch alignment,
- inspect latch/switch connector and harness,
- inspect wiring where it flexes between body and tailgate.

### Flex-harness warning

Tailgate wiring repeatedly bends whenever the hatch is opened.

General electrical failure modes in any flex section include:

- conductor breaking inside apparently intact insulation,
- insulation cracking,
- intermittent opens,
- intermittent shorts,
- water intrusion,
- connector-terminal fretting.

Use a wiggle test while watching:

- lamp state,
- scan-tool tailgate state if available,
- continuity or voltage.

Do not pierce insulation unnecessarily.

---

# 14. Remote Unlock and Courtesy Lighting

**EXACT 2014 OWNER DATA**

Unlocking by transmitter can illuminate the map and room lamps for approximately 30 seconds while the doors remain closed.

If ignition is switched ON or all doors are locked, those lamps turn off immediately.

This creates useful functional tests.

### Test A — remote unlock response

```text
LOCK VEHICLE
        ↓
WAIT FOR NORMAL STATE
        ↓
REMOTE UNLOCK
        ↓
COURTESY LAMPS RESPOND?
```

If they respond normally to remote unlock but not to a particular door opening, the problem is more likely associated with the affected door-input branch than with the lamps themselves.

### Test B — lock cancellation

While courtesy lamps are on from remote unlock, lock the doors.

If the lamps shut off normally, the output side and at least some BCM logic are functioning.

This does not prove every input circuit is healthy, but it narrows the tree.

---

# 15. Door Locks and Body Control

The door-lock system shares body-electrical infrastructure with the door-state system, but the two must not be conflated.

A door can:

- lock/unlock correctly while its door-ajar switch is wrong,
- report door state correctly while its lock actuator is dead,
- have both faults if the harness or connector is damaged.

## Multi-door lock failure

Check common infrastructure first:

- `DR LOCK` 20 A fuse,
- relay operation,
- shared power feed,
- BCM command,
- common harness/ground paths.

## One door lock failure

Move toward:

- local actuator,
- local connector,
- local harness,
- mechanical latch resistance,
- door-specific command path.

See:

- [`RELAY_CONTROL_CIRCUITS.md`](RELAY_CONTROL_CIRCUITS.md)
- [`POWER_DISTRIBUTION.md`](POWER_DISTRIBUTION.md)

---

# 16. Door Locks Work, Courtesy Lamp Does Not

This is a classic example of why systems must be divided into their actual functions.

If the door actuator works but the door-open response does not:

```text
LOCK ACTUATOR OPERATION
DOES NOT PROVE
DOOR-AJAR INPUT OPERATION
```

Concentrate on:

- door-jamb switch,
- switch ground/input circuit,
- connector,
- body-to-door wiring where applicable,
- BCM input state.

---

# 17. Warning Chime Symptoms

Body-state inputs can influence warning behavior.

A false door-open or key-state input can create a chime complaint that appears unrelated to lighting.

Examples of diagnostic questions:

- Does the chime occur only with the driver door?
- Does opening another door reproduce it?
- Does the driver-door input change on scan data?
- Does manipulating the jamb switch change the chime?
- Does the symptom change with ignition/key state?

Do not disable the chime as a "repair."

Find the false input or control fault.

---

# 18. Body-Control Sleep and Battery Drain

Body-input faults matter because control modules and lamps may remain awake longer than expected.

A useful distinction:

```text
VISIBLE LAMP ON
        →
OBVIOUS LOAD

NO VISIBLE LAMP
        →
DOES NOT PROVE
BODY SYSTEM IS ASLEEP
```

A bad switch, module wake-up, remote/receiver activity, stuck relay, or aftermarket connection can create key-off current without an obvious glowing bulb.

For actual current testing, use:

- [`PARASITIC_DRAW_BATTERY_DRAIN.md`](PARASITIC_DRAW_BATTERY_DRAIN.md)

### Door/tailgate setup during parasitic-draw testing

If doors or tailgate must remain physically open for meter access:

- simulate the latched/closed state only with a method that does not damage the latch,
- verify scan data or lamp behavior confirms the car sees the opening as closed,
- do not accidentally lock a latch with the door open and then slam the door,
- restore the latch to its normal open-ready state before closing the door/tailgate.

If the vehicle still thinks a door is open, sleep-current testing can be invalid.

---

# 19. Memory Fuse Interaction

The exact 2014 manual states that raising/pulling the memory fuse disables functions including interior lamps and warning chime during long-term storage.

This makes the memory fuse a useful **diagnostic divider**, not a repair.

```text
EXCESS DRAW
        ↓
MEMORY FUSE ISOLATION CHANGES DRAW?
   ├─ YES → BODY / MEMORY-FED BRANCHES MOVE UP LIST
   └─ NO  → SEARCH OTHER ALWAYS-HOT BRANCHES
```

Never leave the car permanently altered simply to hide a drain.

Source:

- `https://www.manualslib.com/manual/1067849/Hyundai-2014-Accent.html`

---

# 20. Battery-Saver / Parking-Lamp Interaction

**EXACT 2014 OWNER DATA**

The Accent battery-saver function can automatically turn off parking lamps when the key is removed and the driver door is opened.

The owner literature warns that leaving through a different door can prevent expected battery-saver operation.

This makes the **driver-door state** particularly important when diagnosing parking lamps that remain on after shutdown.

```text
PARKING LAMPS REMAIN ON
AFTER NORMAL EXIT
        ↓
VERIFY DRIVER DOOR INPUT
BEFORE CONDEMNING LIGHT SWITCH / BCM
```

Source:

- `https://www.hyundaiaccentmanual.com/accent-81-battery_saver_function.html`

Use the exact vehicle behavior as the final authority because equipment varies by market/configuration.

---

# 21. Water Intrusion and Corrosion

Door, rocker, jamb, tailgate, and hatch areas live in a harsh environment.

Inspect connectors for:

- green/blue corrosion,
- white oxide,
- moisture,
- bent terminals,
- spread female terminals,
- backed-out terminals,
- damaged seals,
- dirt inside weatherproof connectors,
- previous probe damage.

A high-resistance or intermittent input circuit can create flickering state changes rather than a permanent fault.

See:

- [`WIRING_AND_CONNECTOR_DIAGNOSTICS.md`](WIRING_AND_CONNECTOR_DIAGNOSTICS.md)
- [`GROUND_POINTS.md`](GROUND_POINTS.md)

---

# 22. Voltage Testing at a Lamp

If a lamp does not illuminate, do not stop at "12 V is present."

A circuit can show battery voltage unloaded and still fail under load.

Test:

1. supply voltage with circuit commanded on,
2. voltage across the lamp/load,
3. ground/control-side voltage drop,
4. connector integrity under load.

```text
12 V ON AN OPEN CIRCUIT
        ≠
12 V DELIVERED UNDER LOAD
```

A test light can be useful on ordinary 12 V lamp feeds, but do not use an incandescent test light on sensitive module signal circuits without first understanding the circuit.

---

# 23. Short-to-Ground Door-Input Fault

Many body switch circuits are interpreted through a switched input/ground relationship.

Do **not** assume the exact Accent switch topology without the wiring diagram.

Conceptually, however, a harness short can imitate a permanently active switch.

Diagnostic strategy:

```text
INPUT STUCK ACTIVE
        ↓
DISCONNECT PHYSICAL SWITCH
        ↓
INPUT STILL ACTIVE?
   ├─ NO  → SWITCH / MECHANICAL ACTUATION SUSPECT
   └─ YES → HARNESS / CONNECTOR / CONTROLLER INPUT SUSPECT
```

Only use this isolation test when disconnecting the switch is safe and the correct circuit is known.

---

# 24. Open-Circuit Door-Input Fault

An open circuit can make the controller fail to see an actual door-opening event, depending on circuit topology.

If a door never registers:

- inspect switch connection,
- inspect connector tension,
- inspect harness continuity,
- inspect local ground/reference path where applicable,
- compare the suspect branch to a known-good door circuit.

A known-good neighboring door is often a useful functional comparison even when wire colors or connector locations differ.

---

# 25. Intermittent Door-Ajar Flicker While Driving

Possible causes include:

- marginal jamb-switch adjustment/contact,
- loose switch mounting,
- door movement from worn hinge/striker alignment,
- loose connector,
- harness chafe,
- water/corrosion,
- tailgate latch movement on rough roads.

## Reproduction strategy

With the vehicle safely parked:

- monitor scan data or door indicator,
- gently press/pull the closed door,
- operate the switch manually,
- wiggle nearby harnesses,
- gently move the tailgate/latch if that branch is suspected.

Do not perform distracting body-electrical tests while driving.

---

# 26. Rough-Road / Nomad Relevance

Primitive roads add vibration, dust, moisture, and repeated hatch use.

Periodically inspect:

- tailgate harness boots,
- jamb switches,
- latch cleanliness,
- hatch alignment,
- lamp housings,
- fuse-panel cover seating,
- aftermarket accessory wiring routed through the hatch or doors.

### High-value pre-trip test

Before remote travel:

```text
OPEN EACH DOOR ONE AT A TIME
        ↓
VERIFY EXPECTED COURTESY / AJAR RESPONSE
        ↓
CLOSE EACH DOOR
        ↓
VERIFY RESPONSE CLEARS
        ↓
OPEN / CLOSE TAILGATE
        ↓
VERIFY LUGGAGE LAMP STATE
```

This takes less than a minute and can expose a switch beginning to fail before it becomes an overnight battery problem.

---

# 27. Aftermarket Lighting and Nomad Wiring

For a vehicle used as a mobile workspace/camp, body circuits can be tempting power sources.

Do **not** casually splice camping loads into:

- room-lamp wiring,
- BCM outputs,
- door-switch inputs,
- tailgate-switch circuits,
- keyless-entry wiring.

These are control-system circuits, not general-purpose accessory buses.

For auxiliary power:

- use a properly fused dedicated feed,
- size wire for the actual load,
- use appropriate relay/control architecture,
- keep high-current loads away from BCM signal circuits.

A camping light should never be allowed to confuse the car about whether a door is open.

---

# 28. Do Not Backfeed BCM Circuits

Never apply battery voltage blindly to a door-switch or BCM input wire.

Possible results include:

- module damage,
- damaged transistor outputs,
- fuse failure,
- damaged network electronics,
- unintended lock/lamp operation.

When testing an input:

- identify the circuit,
- use high-impedance measurement where appropriate,
- use continuity tests only with circuit power removed where appropriate,
- use fused jumpers only when the factory circuit design supports the test.

See:

- [`SENSOR_5V_REFERENCE_AND_SENSOR_GROUNDS.md`](SENSOR_5V_REFERENCE_AND_SENSOR_GROUNDS.md)
- [`WIRING_AND_CONNECTOR_DIAGNOSTICS.md`](WIRING_AND_CONNECTOR_DIAGNOSTICS.md)

---

# 29. BCM Replacement Is a Last Step

A BCM replacement should follow evidence, not frustration.

Before replacement:

```text
VERIFY BATTERY
VERIFY CHARGING
VERIFY BCM B+
VERIFY IGNITION FEEDS
VERIFY GROUNDS
VERIFY INPUT STATES
VERIFY OUTPUT CIRCUITS
VERIFY CONNECTORS
VERIFY NETWORK / SCAN COMMUNICATION
```

Only then does internal module failure become a strong conclusion.

A module that follows a false input perfectly is not malfunctioning.

---

# 30. Quick Symptom Matrix

| Symptom | First branches to inspect |
|---|---|
| One door never triggers room lamp | Door switch, local connector, local wiring, BCM input |
| All doors fail to trigger interior lamps | Lamp selector, ROOM LP 1, BCM feed/ground, common output/control |
| Lamp stays on after one specific door closes | That door switch/mechanical actuation, connector, wiring |
| Lamp stays on regardless of every door | Lamp manually ON, common control, wiring, BCM output |
| Luggage lamp stays on with hatch shut | Tailgate/latch switch state, alignment, flex harness |
| Locks dead on all doors | DR LOCK fuse, shared relay/feed, BCM command |
| One lock actuator dead | Local actuator, connector, harness, mechanical latch |
| Parking lamps fail to auto-cut after driver exit | Driver-door input, ignition/key state, body-control logic |
| Battery repeatedly dead after parking | Battery/charging first, then parasitic draw and body-input sleep state |
| Door-ajar flickers on rough road | Switch actuation, latch/door alignment, loose connector, flex/chafed harness |

---

# 31. Field Diagnostic Flow

```text
BODY / INTERIOR-LIGHT SYMPTOM
            ↓
VERIFY BATTERY VOLTAGE
            ↓
VERIFY FUSE / POWER DISTRIBUTION
            ↓
VERIFY LAMP SWITCH POSITION
            ↓
IDENTIFY WHICH DOOR / TAILGATE INPUT MATTERS
            ↓
COMPARE PHYSICAL STATE TO SCAN / INDICATOR STATE
            ↓
TEST SWITCH AND CONNECTOR
            ↓
TEST HARNESS
            ↓
VERIFY BCM POWER / GROUND / COMMAND
            ↓
TEST OUTPUT / LOAD UNDER VOLTAGE
            ↓
REPAIR ROOT CAUSE
            ↓
VERIFY TIMER / LOCK / LIGHT / SLEEP BEHAVIOR
```

---

# 32. AI / RAG Rules

When an AI uses this document:

1. **Do not diagnose a BCM solely from strange body symptoms.**
2. **Ask which exact door or tailgate produces the symptom.**
3. **Ask for lamp-selector position before diagnosing the circuit.**
4. **Separate door-ajar input from door-lock actuator operation.**
5. **Separate 5-door luggage-lamp behavior from passenger-compartment DOOR-mode lighting.**
6. **Check `ROOM LP 1` and `DR LOCK` shared feeds when multiple related functions fail.**
7. **Treat exact 2014 owner behavior as higher confidence than adjacent-year service details.**
8. **Do not invent BCM pin numbers, wire colors, terminal identities, or exact switch polarity without an exact diagram.**
9. **For battery-drain complaints, verify battery and charging health before blaming body electronics.**
10. **A lamp turning off does not prove every body module has entered sleep.**
11. **Do not recommend backfeeding battery voltage into BCM or switch inputs.**
12. **Record the physical state and the controller-observed state separately.**

---

# 33. Diagnostic Record Template

```yaml
body_electrical_event:
  date: ""
  odometer_miles: null
  ambient_temp_f: null

  symptom:
    description: ""
    intermittent: null
    battery_drain_present: null

  ignition_state: "OFF|ACC|ON|START|unknown"
  key_present: null

  lamp_switch:
    map_manual_on: null
    room_mode: "ON|DOOR|OFF|unknown"

  physical_state:
    driver_door: "open|closed|unknown"
    passenger_door: "open|closed|unknown"
    rear_left: "open|closed|unknown"
    rear_right: "open|closed|unknown"
    tailgate: "open|closed|unknown"

  controller_observed_state:
    driver_door: "open|closed|not_read"
    passenger_door: "open|closed|not_read"
    rear_left: "open|closed|not_read"
    rear_right: "open|closed|not_read"
    tailgate: "open|closed|not_read"

  fuses:
    room_lp_1_10a: "good|open|not_checked"
    dr_lock_20a: "good|open|not_checked"
    ig2_body_feed: "good|open|not_checked"

  voltage:
    battery_resting_v: null
    lamp_feed_v: null
    lamp_ground_drop_v: null

  switch_test:
    component: ""
    continuity_changes_with_operation: null
    connector_condition: ""
    wiggle_test_result: ""

  scan:
    bcm_communication: null
    dtcs: []

  parasitic_draw:
    tested: null
    sleep_current_ma: null

  root_cause: ""
  repair: ""
  verification: ""
```

---

# 34. Cross-References

- [`PARASITIC_DRAW_BATTERY_DRAIN.md`](PARASITIC_DRAW_BATTERY_DRAIN.md)
- [`POWER_DISTRIBUTION.md`](POWER_DISTRIBUTION.md)
- [`RELAY_CONTROL_CIRCUITS.md`](RELAY_CONTROL_CIRCUITS.md)
- [`WIRING_AND_CONNECTOR_DIAGNOSTICS.md`](WIRING_AND_CONNECTOR_DIAGNOSTICS.md)
- [`GROUND_POINTS.md`](GROUND_POINTS.md)
- [`SENSOR_5V_REFERENCE_AND_SENSOR_GROUNDS.md`](SENSOR_5V_REFERENCE_AND_SENSOR_GROUNDS.md)
- [`../specs/FUSES_AND_RELAYS.md`](../specs/FUSES_AND_RELAYS.md)
- [`../diagnostics/OBD2_GUIDE.md`](../diagnostics/OBD2_GUIDE.md)

---

# 35. Sources

## Exact 2014 owner data

Hyundai Accent 2014 owner manual — interior-light behavior, automatic shutoff, luggage-room lamp:

- `https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/14`
- `https://www.dezosmanuals.com/wp-content/uploads/2021/07/2014-Hyundai-Accent-OM.pdf`
- `https://www.manualslib.com/manual/1067849/Hyundai-2014-Accent.html`

Hyundai Canada 2014 Accent maintenance/fuse section:

- `https://www.hyundaicanada.com/-/media/hyundai/feature/ownerssection/manuals/english/2014/accent/rb-cane-7.pdf`

2014 owner-manual fuse search/table mirror:

- `https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/2/?srch=fuse`

Battery-saver function owner-manual mirror:

- `https://www.hyundaiaccentmanual.com/accent-81-battery_saver_function.html`

## Exact 2014 parts data

2014 Accent door-jamb / door-ajar switch catalog:

- `https://www.hyundaipartsdeal.com/oem-2014-hyundai-accent-door_jamb_switch.html`

2014 Accent tailgate-lock/latch catalog:

- `https://www.hyundaipartsdeal.com/oem-2014-hyundai-accent-tailgate_lock.html`

2014 Accent 5-door tailgate actuator listing:

- `https://www.hyundaipartsdeal.com/oem-2014-hyundai-accent-trunk_latch.html`

## Same-generation service-family data

2013 Accent BCM electrical diagram / connector documentation:

- `https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Diagrams/Electrical%20Diagrams/Body%20Control%20Module/`

2012 Accent service-library index showing individual door switches and 5-door luggage-lamp components:

- `https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/`

---

## Final Doctrine

```text
THE DOOR IS PHYSICALLY OPEN OR CLOSED.
THE SWITCH REPORTS A STATE.
THE BCM ACTS ON THE STATE IT RECEIVES.
THE LAMP / LOCK / CHIME IS THE OUTPUT.

WHEN THEY DISAGREE,
FIND WHERE REALITY AND THE SIGNAL PART COMPANY.
```
