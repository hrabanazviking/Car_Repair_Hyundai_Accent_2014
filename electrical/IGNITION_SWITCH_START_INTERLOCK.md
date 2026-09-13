# Ignition Switch, Start Interlock, and Park/Neutral Starting Diagnostics

**Vehicle focus:** U.S.-market 2014 Hyundai Accent SE 5-door, 1.6L Gamma GDI, 6-speed automatic

**Purpose:** Provide a source-aware diagnostic guide for key-switch power states, starter-request logic, Park/Neutral starting authorization, ignition-switch faults, transaxle range-switch faults, starter-relay control, and intermittent no-crank conditions.

> **Core rule:** A no-crank condition is a circuit problem until testing proves which part of the circuit failed.

> **Second core rule:** Never defeat the Park/Neutral start-safety function as a permanent repair.

---

## 1. Source and confidence policy

This file separates exact 2014 owner/fuse information from same-generation service information.

### Confidence tags

- **EXACT-2014** — explicitly documented for the 2014 Accent owner/fuse information.
- **SERVICE-FAMILY** — Hyundai service information for the closely related 2012/2013 Accent RB 1.6L platform.
- **TSB-RB** — Hyundai technical-service information explicitly covering Accent RB models.
- **GENERAL-DIAGNOSTIC** — standard electrical diagnostic reasoning, not a claimed Hyundai specification.
- **UNKNOWN** — exact value, terminal mapping, or specification not verified from an accessible source.

If a source exposes a specification only as an unreadable image, this repository does **not** invent or transcribe a guessed value.

---

## 2. Exact 2014 ignition-key positions

**Source:** 2014 Hyundai Accent owner's manual.

- ManualsLib: https://www.manualslib.com/manual/1067849/Hyundai-2014-Accent.html
- Manualzz transcription: https://manualzz.com/doc/53857913/hyundai-2014-accent-owner-manual

### LOCK

**EXACT-2014**

- Key removable only in LOCK.
- Steering wheel locks for theft protection if the vehicle is equipped with that function.
- When returning to LOCK, Hyundai instructs the driver to push the key inward at ACC and turn toward LOCK.

### ACC

**EXACT-2014**

- Steering wheel is unlocked if equipped.
- Electrical accessories can operate.

### ON

**EXACT-2014**

- Warning lamps can be checked before starting.
- Normal key position while the engine is running.
- Hyundai warns not to leave the switch in ON for long with the engine stopped because the battery can discharge.

### START

**EXACT-2014**

- Turning the key to START commands engine cranking.
- The engine cranks until the key is released.
- The key then returns to ON.

Hyundai's 2014 starting instructions limit a normal START attempt to **10 seconds maximum**, followed by a **5–10 second wait** before another attempt if the engine does not start.

---

## 3. Exact 2014 automatic-transmission starting conditions

**Source:** 2014 Hyundai Accent owner's manual.

https://manualzz.com/doc/53857913/hyundai-2014-accent-owner-manual

For the automatic transmission:

1. Apply the parking brake.
2. Place the selector in **P (Park)**.
3. Depress the brake pedal fully.
4. Turn the ignition switch to START.

Hyundai explicitly states that the engine **can also be started in N (Neutral)**.

### Diagnostic significance

That gives the technician two valid factory start positions:

```text
PARK ─────┐
          ├── VALID START-ENABLE POSITION
NEUTRAL ──┘
```

Therefore:

- starts in **P and N** → Park/Neutral authorization is at least functioning at that moment;
- starts in **N but not P** → range-switch adjustment, Park-position recognition, connector, wiring, or mechanical selector alignment becomes more suspicious;
- starts in **P but not N** → Neutral-position recognition or range-switch adjustment/wiring becomes more suspicious;
- starts in **neither P nor N** → do not automatically blame the range switch; continue through battery, power feeds, ignition switch, relay, command wiring, starter solenoid, starter motor, and grounds.

This pattern is diagnostic evidence, not final proof.

---

## 4. Exact 2014 key-removal interlock

**EXACT-2014**

The 2014 owner's manual states that the ignition key cannot be removed unless the automatic-transmission selector is in **P (Park)**.

This means a complaint such as:

- key will not release,
- key intermittently refuses to return/remove,
- selector position and displayed range disagree,

may involve the shift-position/key-interlock system rather than the mechanical key cylinder alone.

Do not force the key or steering lock.

---

## 5. Exact 2014 starting-related fuses and feeds

**Primary exact-year source:** Hyundai Canada 2014 Accent maintenance/fuse documentation.

https://www.hyundaicanada.com/-/media/hyundai/feature/ownerssection/manuals/english/2014/accent/rb-cane-7.pdf

### Engine-compartment feeds

| Feed | Rating | Exact 2014 protected component information | Confidence |
|---|---:|---|---|
| IG2 | 40 A | Start Relay, Ignition Switch | EXACT-2014 |
| IG1 | 40 A | Ignition Switch | EXACT-2014 |
| ECU 1 | 30 A | ECU 2 fuse, Engine Control Relay | EXACT-2014 |
| ECU 2 | 10 A | ECM, PCM | EXACT-2014 |
| B/UP LAMP | 10 A | PCM, Transaxle Range Switch, cluster, reverse lamps, shift-lever illumination | EXACT-2014 |

### Instrument-panel feeds

| Fuse | Rating | Exact 2014 protected component information | Confidence |
|---|---:|---|---|
| START | 10 A | Transaxle Range Switch, Ignition Lock Switch | EXACT-2014 |
| TCU | 15 A | Vehicle Speed Sensor, Transaxle Range Switch | EXACT-2014 |

### Important implication

A start complaint can involve more than one electrical branch.

For example, the exact fuse table shows that the transaxle range switch appears in more than one protected circuit. Therefore:

> **Do not replace a range switch merely because one range-related fuse has failed. Determine why the fuse failed and test the circuit.**

Use the physical fuse-panel label on the actual vehicle as the final authority for its installed configuration.

---

## 6. Same-generation starting-system architecture

**SERVICE-FAMILY — 2013 Accent 1.6L**

Hyundai service information describes the starting system as including:

- battery,
- starter motor,
- starter solenoid switch,
- inhibitor switch / transaxle range switch for automatic transmission,
- ignition switch,
- ignition lock switch,
- connecting wiring,
- battery cable.

Source:

https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Starting%20and%20Charging/Starting%20System/Description%20and%20Operation/

The service description explains that START-position current energizes the starter-solenoid coil; the solenoid then moves the pinion into engagement and closes the high-current contacts that allow the starter motor to crank the engine.

### Simplified functional chain

```text
BATTERY B+
   │
   ├── MAIN / IGNITION POWER DISTRIBUTION
   │
IGNITION SWITCH REQUEST
   │
P/N START AUTHORIZATION
   │
STARTER RELAY CONTROL
   │
STARTER SOLENOID S-TERMINAL
   │
SOLENOID CONTACTS CLOSE
   │
STARTER MOTOR RECEIVES HIGH CURRENT
   │
ENGINE CRANKS
```

This is a functional diagnostic representation, not an exact wiring diagram.

---

## 7. What the Park/Neutral interlock actually does

The automatic-transmission range/inhibitor switch is part of the safety chain that prevents normal starter operation when the transmission is in a drive range.

The exact 2014 owner's manual proves that P and N are accepted start positions. Hyundai service information for the RB platform further identifies the inhibitor/range switch as a starting-system component.

### Do not bypass it

A permanent jumper that allows cranking in R or D can create uncontrolled vehicle movement.

**Never convert a diagnostic bypass into a repair.**

---

## 8. Hyundai RB inhibitor-switch TSB

**TSB-RB**

Hyundai TSB 12-AT-022-1 applies to the Accent **RB** six-speed automatic and addresses inhibitor/range-switch faults.

Service information mirror:

https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Transmission%20and%20Drivetrain/Technical%20Service%20Bulletins/Customer%20Interest/A%2FT%20Controls%20-%20MIL%20ON%2FDTC%27s%20P0705%2FP0707%2FP0706%2FP0708/

The bulletin associates an improperly adjusted or improperly operating inhibitor switch with:

- **P0705** — range-switch sensor circuit,
- **P0706** — range/performance,
- **P0707** — open circuit,
- **P0708** — short circuit or multiple inputs,
- MIL illumination,
- and possible inability to start in P or N.

### Diagnostic lesson

A range-switch code is not automatically a failed switch.

Potential causes include:

- switch adjustment,
- selector/cable alignment,
- connector condition,
- open wiring,
- shorted wiring,
- conflicting range inputs,
- switch internal failure,
- control-module input fault after external causes are proven good.

Hyundai's bulletin instructs technicians to diagnose and verify the condition rather than immediately condemn the whole transmission.

---

## 9. Symptom: starts in N but not P

This is one of the most useful field clues.

### First suspects

1. selector not reaching true Park mechanically,
2. range/inhibitor switch misadjusted,
3. Park contact inside switch not recognized,
4. shift cable / linkage alignment problem,
5. connector terminal issue,
6. wiring fault in the Park-range/start-authorize path.

### What it makes less likely

If the starter cranks normally in N:

- battery is capable of cranking at that moment,
- starter motor can operate,
- starter solenoid can operate,
- major high-current starter cable path can operate,
- starter relay/load path can operate at that moment.

Those facts do **not** prove every part is perfect, but they move the investigation strongly toward the P/N authorization side.

### Field check

With the vehicle stationary, parking brake firmly set, service brake applied, and nobody in front of or behind the vehicle:

- attempt a normal start in P;
- attempt a normal start in N;
- observe the cluster gear-position indication;
- note whether moving the selector gently within the P gate changes the symptom;
- scan the transmission module for range-switch DTCs and live range status.

Do not aggressively manipulate the shifter while holding the key in START.

---

## 10. Symptom: starts in P but not N

Use the same reasoning in reverse.

Suspect:

- Neutral contact / Neutral recognition,
- range-switch adjustment,
- connector or harness problem,
- selector/cable alignment.

Because Hyundai explicitly permits starting in N, consistent failure only in N is diagnostic information.

---

## 11. Symptom: no crank in either P or N

Do **not** immediately replace the range switch.

Use this order:

```text
NO CRANK IN P AND N
       ↓
BATTERY STATE / TERMINALS
       ↓
ENGINE + BODY GROUNDS
       ↓
IG2 / START FUSES
       ↓
IGNITION SWITCH START REQUEST
       ↓
P/N AUTHORIZATION
       ↓
STARTER RELAY COMMAND
       ↓
RELAY OUTPUT
       ↓
SOLENOID S-TERMINAL COMMAND
       ↓
STARTER B+ / VOLTAGE DROP
       ↓
STARTER / SOLENOID
```

Cross-reference:

- [`../diagnostics/NO_CRANK.md`](../diagnostics/NO_CRANK.md)
- [`BATTERY_STARTER_ALTERNATOR.md`](BATTERY_STARTER_ALTERNATOR.md)
- [`GROUND_POINTS.md`](GROUND_POINTS.md)
- [`POWER_DISTRIBUTION.md`](POWER_DISTRIBUTION.md)
- [`RELAY_CONTROL_CIRCUITS.md`](RELAY_CONTROL_CIRCUITS.md)

---

## 12. Hyundai same-generation starter troubleshooting sequence

**SERVICE-FAMILY — 2013 Accent 1.6L**

Hyundai's service procedure begins with a **fully charged, good battery** and then instructs technicians to test the start system with the selector in N or P.

If the starter does not crank, Hyundai next directs attention to:

1. battery condition,
2. battery electrical connections,
3. battery negative-to-body connection,
4. engine ground cables,
5. starter connections,
6. wiring between the driver's under-dash fuse/relay box and ignition switch,
7. wiring between the fuse/relay box and starter,
8. ignition switch,
9. transaxle range-switch connector / ignition-lock-switch connector,
10. starter relay.

Source:

https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Starting%20and%20Charging/Starting%20System/Testing%20and%20Inspection/Component%20Tests%20and%20General%20Diagnostics/

This is exactly why a no-crank complaint should not begin with replacing the starter.

---

## 13. Ignition-switch diagnosis

### Possible ignition-switch symptoms

- no crank even though battery and starter are healthy,
- intermittent no crank depending on key position,
- START request cuts in/out with very slight key movement,
- some key-switched circuits fail together,
- accessories/IGN circuits behave abnormally between ACC and ON,
- engine starts only after repeated key cycling.

These symptoms are clues, not proof.

### Same-generation Hyundai inspection

**SERVICE-FAMILY — 2013 Accent 1.6L**

Hyundai's procedure disconnects the ignition-switch and key-switch connectors under the steering column and checks terminal continuity for the appropriate switch positions.

Source:

https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Powertrain%20Management/Ignition%20System/Sensors%20and%20Switches%20-%20Ignition%20System/Ignition%20Switch/Service%20and%20Repair/

The exact continuity table is presented graphically in that source and is **not transcribed here** because this repository will not guess unreadable terminal mappings.

### Better field method when exact switch pinout is unavailable

Verify the circuit functionally:

- is the appropriate upstream fuse powered?
- does the START-related output become powered when the key is held in START?
- does the output remain stable while the symptom occurs?
- does loaded voltage remain near source voltage, or is there a large drop?

Do not pierce random wires merely because they are physically near the ignition cylinder.

---

## 14. Starter-relay test

**SERVICE-FAMILY — 2013 Accent 1.6L**

For the documented starter relay, Hyundai specifies:

- apply 12 V to relay terminal 85,
- ground terminal 86,
- verify continuity between terminals 30 and 87 when energized.

Source:

https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Relays%20and%20Modules/Relays%20and%20Modules%20-%20Starting%20and%20Charging/Starter%20Relay/Testing%20and%20Inspection/

### Important limitation

Do not assume all relays share the same internal terminal arrangement.

Verify the actual relay diagram before bench power or substitution.

Cross-reference:

[`RELAY_CONTROL_CIRCUITS.md`](RELAY_CONTROL_CIRCUITS.md)

---

## 15. A relay click does not prove starter command delivery

A click only proves that something inside the relay moved.

Possible remaining faults include:

- burned/high-resistance relay contacts,
- poor relay socket tension,
- no high-current feed at the contact side,
- open output wire,
- corroded connector,
- high resistance at starter S-terminal connection,
- starter-solenoid fault.

Therefore:

```text
RELAY CLICKS
    ↓
VERIFY CONTACT FEED
    ↓
VERIFY CONTACT OUTPUT UNDER LOAD
    ↓
VERIFY S-TERMINAL COMMAND
```

---

## 16. S-terminal versus B-terminal

At the starter solenoid:

- **B-terminal** is the heavy battery feed.
- **S-terminal** is the start-command input to the solenoid.

**SERVICE-FAMILY** Hyundai starter documentation confirms both terminals on the Accent starter assembly.

Starter service source:

https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Starting%20and%20Charging/Starting%20System/Starter%20Motor/Service%20and%20Repair/Removal%20and%20Replacement/Repair%20Procedures/

### Diagnostic split

If the starter B-terminal has proper battery power but the S-terminal never receives a START command, investigate upstream control/interlock circuitry.

If B+ and S-command are both correct under load but the starter does not operate, starter/solenoid or high-current ground-path failure becomes much more likely.

---

## 17. Voltage-drop diagnosis is stronger than unloaded continuity

A corroded connection can pass an ohmmeter test yet fail under starter-current demand.

Check voltage drop during the actual fault condition.

### High-current side

Investigate:

- battery positive post to starter B-terminal,
- starter case / engine to battery negative,
- battery terminals,
- engine ground strap,
- body ground path.

Use the repo's existing ground and starter guides for threshold interpretation.

### Control side

Trace START-command voltage through each accessible stage while the key is actually held in START.

The point where voltage disappears or collapses localizes the fault.

---

## 18. No-crank symptom matrix

| Symptom | Higher-priority suspects | Important next check |
|---|---|---|
| Silence in P, cranks in N | Range switch adjustment/P contact, linkage, connector | Scan range status, inspect P recognition |
| Silence in N, cranks in P | Neutral contact/range recognition | Scan range status, switch/linkage |
| Silence in P and N | Battery/grounds, IG2/START, ignition switch, relay, S-command, starter | Trace start command |
| Single click | Solenoid engages but high-current path/starter may fail | Battery voltage + loaded cable drop |
| Rapid clicking | Low system voltage / high resistance | Battery and terminal/ground tests |
| Starter stays engaged after key release | Solenoid/relay/contact/key-switch fault possible | Shut down safely, inspect command and contacts |
| Start works after key wiggling | Ignition-switch/key-switch/connector possible | Reproduce carefully, loaded voltage test |
| Key will not remove | P/key-interlock recognition or mechanical lock issue | Confirm true P and selector indication |
| Range DTC + start problem | Range switch adjustment, wiring, connector | Diagnose P0705/P0706/P0707/P0708 path |
| No cluster/key-switched power plus no crank | Upstream ignition feed / switch / main distribution | IG1/IG2 and junction-box feeds |

---

## 19. Starter remains engaged after key release

This is potentially destructive.

Possible causes include:

- starter-solenoid plunger/switch sticking,
- damaged or dirty pinion/overrunning-clutch mechanism,
- starter relay contacts welded/stuck,
- START command remaining electrically active,
- ignition switch failing to return electrically even if the key feels released.

Hyundai's same-generation troubleshooting specifically tells technicians to investigate solenoid/plunger switching and pinion/overrunning-clutch problems if the starter fails to disengage.

If the starter continues running unexpectedly, stop the engine and electrical event as safely as possible rather than repeatedly cycling the starter.

---

## 20. Range-switch live-data diagnosis

If the scanner can read transmission data, observe selected-range information while slowly moving the selector through the normal positions with the vehicle stationary and brakes applied.

Look for:

- P displayed when physically in P,
- N displayed when physically in N,
- unstable/flickering range,
- two impossible ranges reported at once,
- delayed transition,
- mismatch between cluster indication and scan data.

A live-data disagreement can be more informative than simply checking whether a DTC exists.

Do not shift through ranges with the engine revved.

---

## 21. P0705 / P0706 / P0707 / P0708 quick routing

| Code | General diagnostic direction from Hyundai RB TSB |
|---|---|
| P0705 | Range-switch sensor/circuit fault |
| P0706 | Range/performance or plausibility problem |
| P0707 | Open/low-side circuit condition in Hyundai bulletin terminology |
| P0708 | Short/multiple-input condition in Hyundai bulletin terminology |

### Before replacing the switch

Check:

- connector fully seated,
- terminal damage or corrosion,
- harness chafe,
- selector cable adjustment,
- range-switch alignment,
- actual live-data range,
- supply and ground where the exact wiring diagram confirms them.

Do not infer wire colors or pin numbers from another model.

---

## 22. Intermittent no-crank strategy

Intermittent faults are easiest to diagnose **while failing**.

Record:

- ambient temperature,
- engine hot/cold,
- P versus N behavior,
- dash/cluster behavior,
- relay click/no click,
- headlights bright/dim during START,
- battery voltage during START,
- S-terminal command present/absent,
- range data,
- relevant DTCs,
- whether slight key movement changes the symptom.

Same-generation Hyundai diagnostic literature specifically emphasizes recreating the conditions under which intermittent faults occur.

General source:

https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Powertrain%20Management/Computers%20and%20Control%20Systems/Testing%20and%20Inspection/Initial%20Inspection%20and%20Diagnostic%20Overview/

---

## 23. What **not** to do

### Do not permanently jumper the Park/Neutral interlock

That can allow the vehicle to crank in gear.

### Do not install an oversized START/IG fuse

A larger fuse hides the fault while sacrificing wiring protection.

### Do not repeatedly crank for long periods

2014 Hyundai limit: normal START attempt **maximum 10 seconds**, then wait **5–10 seconds** before trying again.

### Do not assume brake-pedal application proves an electrical brake-start interlock

The 2014 owner's procedure tells the driver to press the brake pedal for automatic-transmission starting, but this document does **not** claim an exact brake-switch-to-starter interlock path without the exact wiring diagram.

### Do not jumper unknown relay terminals

Verify terminal identity first.

### Do not test starter circuits underneath an unsupported vehicle

Never rely on the factory emergency jack as an under-vehicle work support.

### Do not bypass safety interlocks when people are in front of or behind the car

Any controlled starter/solenoid test must account for unexpected vehicle motion.

---

## 24. Controlled advanced starter-command testing

Hyundai's same-generation service procedure includes a controlled test that supplies battery power to the starter-solenoid command terminal after the normal safety prerequisites are established.

That test distinguishes:

- a starter/solenoid/high-current failure,
- from an upstream start-command/control failure.

Because directly energizing a starter can cause sudden vehicle movement if performed incorrectly, this repository treats that as an **advanced service test**, not a casual roadside bypass.

Before any such test:

- transmission must be verified in P or N,
- parking brake firmly applied,
- wheels chocked,
- vehicle securely immobilized,
- nobody positioned in front of or behind it,
- exact starter terminals positively identified.

Never convert the test connection into permanent wiring.

---

## 25. Roadside / nomad triage

For a remote no-crank event:

```text
1. MAKE VEHICLE SAFE
2. TRY NORMAL START IN P
3. TRY NORMAL START IN N
4. RECORD CLICK / SILENCE / RAPID CLICK
5. CHECK BATTERY VOLTAGE + TERMINALS
6. CHECK GROUND CONNECTIONS
7. CHECK START / IG2 FUSES
8. SCAN ALL MODULES
9. CHECK RANGE DATA + DTCs
10. LISTEN / FEEL FOR STARTER RELAY COMMAND
11. TEST RELAY FEED / OUTPUT IF SAFE
12. TEST STARTER S-COMMAND IF ACCESSIBLE AND SAFE
13. DECIDE: FIELD REPAIR OR RECOVERY
```

### Field-repair candidates

Potentially reasonable in the field when confirmed and safely accessible:

- loose/corroded battery terminal,
- loose accessible ground,
- correctly rated blown fuse after root cause is understood,
- failed removable relay replaced by a verified identical relay,
- connector not fully seated,
- obvious non-damaged selector linkage issue that can be correctly restored.

### Recovery candidates

Prefer recovery when diagnosis indicates:

- starter replacement is inaccessible or unsafe at the site,
- burned junction-box/socket damage,
- recurring fuse failure from an unknown short,
- damaged range-switch harness requiring proper wiring repair,
- unsafe selector/interlock behavior,
- starter remains engaged,
- vehicle may crank in a drive range,
- reliable P/N status cannot be established.

---

## 26. AI / RAG diagnostic rules

An AI using this repository should follow these rules:

1. **Never translate “no crank” into “bad starter” without tests.**
2. Ask whether the vehicle cranks in **P, N, both, or neither**.
3. Ask whether the relay clicks.
4. Ask whether battery voltage collapses during START.
5. Preserve scan data before clearing codes.
6. Distinguish `starter motor does not turn` from `engine cranks but does not start`.
7. A range-switch DTC is evidence about a circuit/function, not permission to automatically replace the switch.
8. If N works and P does not, prioritize Park-range recognition before condemning the starter.
9. Verify exact physical fuse labels before relying on a generic diagram.
10. Never invent ignition-switch pinouts, wire colors, or continuity tables.
11. Never recommend permanently defeating the P/N interlock.
12. If the starter remains energized after key release, treat it as an urgent fault.
13. Use loaded voltage-drop tests when possible instead of trusting unloaded continuity alone.
14. Prefer **UNKNOWN** to fabricated specificity.

---

## 27. YAML diagnostic record

```yaml
start_interlock_diagnostic:
  vehicle:
    model: "2014 Hyundai Accent SE 5-door"
    engine: "1.6L Gamma GDI"
    transmission: "6-speed automatic"

  symptom:
    no_crank: null
    crank_no_start: null
    intermittent: null
    starter_stays_engaged: null
    key_removal_problem: null

  position_test:
    cranks_in_P: null
    cranks_in_N: null
    cluster_range_in_P: null
    cluster_range_in_N: null
    scan_tool_range_in_P: null
    scan_tool_range_in_N: null

  electrical:
    battery_resting_voltage: null
    battery_voltage_during_start: null
    ig2_40a_ok: null
    start_10a_ok: null
    starter_relay_clicks: null
    starter_relay_input_voltage: null
    starter_relay_output_voltage: null
    starter_s_terminal_command: null
    starter_b_terminal_voltage: null
    positive_cable_voltage_drop: null
    negative_path_voltage_drop: null

  dtcs:
    p0705: null
    p0706: null
    p0707: null
    p0708: null
    other: []

  physical_inspection:
    battery_terminals: null
    engine_ground: null
    body_ground: null
    range_switch_connector: null
    selector_linkage: null
    ignition_switch_connector: null
    starter_connections: null

  conclusion:
    root_cause: null
    confidence: null
    repair_performed: null
    verified_in_P: null
    verified_in_N: null
    rescan_clean: null
```

---

## 28. Cross-references

- [`../diagnostics/NO_CRANK.md`](../diagnostics/NO_CRANK.md)
- [`../diagnostics/CRANK_NO_START.md`](../diagnostics/CRANK_NO_START.md)
- [`../diagnostics/DTC_INDEX.md`](../diagnostics/DTC_INDEX.md)
- [`BATTERY_STARTER_ALTERNATOR.md`](BATTERY_STARTER_ALTERNATOR.md)
- [`GROUND_POINTS.md`](GROUND_POINTS.md)
- [`POWER_DISTRIBUTION.md`](POWER_DISTRIBUTION.md)
- [`RELAY_CONTROL_CIRCUITS.md`](RELAY_CONTROL_CIRCUITS.md)
- [`WIRING_AND_CONNECTOR_DIAGNOSTICS.md`](WIRING_AND_CONNECTOR_DIAGNOSTICS.md)
- [`CAN_NETWORK_DIAGNOSTICS.md`](CAN_NETWORK_DIAGNOSTICS.md)
- [`../transmission/SIX_SPEED_AUTOMATIC.md`](../transmission/SIX_SPEED_AUTOMATIC.md)
- [`../roadside/EMERGENCY_FIELD_REPAIRS.md`](../roadside/EMERGENCY_FIELD_REPAIRS.md)

---

## 29. Sources

### Exact 2014 owner information

- 2014 Hyundai Accent owner's manual, ignition positions and starting procedure:  
  https://www.manualslib.com/manual/1067849/Hyundai-2014-Accent.html

- 2014 Hyundai Accent owner's manual transcription, ignition/start/P-N/key-interlock information:  
  https://manualzz.com/doc/53857913/hyundai-2014-accent-owner-manual

- Hyundai Canada 2014 Accent fuse documentation, exact START/IG1/IG2/TCU/range-switch feeds:  
  https://www.hyundaicanada.com/-/media/hyundai/feature/ownerssection/manuals/english/2014/accent/rb-cane-7.pdf

### Same-generation Hyundai service information

- 2013 Accent starting-system description:  
  https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Starting%20and%20Charging/Starting%20System/Description%20and%20Operation/

- 2013 Accent starting-system troubleshooting:  
  https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Starting%20and%20Charging/Starting%20System/Testing%20and%20Inspection/Component%20Tests%20and%20General%20Diagnostics/

- 2013 Accent ignition-switch inspection/service:  
  https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Powertrain%20Management/Ignition%20System/Sensors%20and%20Switches%20-%20Ignition%20System/Ignition%20Switch/Service%20and%20Repair/

- 2013 Accent starter-relay test:  
  https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Relays%20and%20Modules/Relays%20and%20Modules%20-%20Starting%20and%20Charging/Starter%20Relay/Testing%20and%20Inspection/

- 2013 Accent starter-motor service and B/S terminal identification:  
  https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Starting%20and%20Charging/Starting%20System/Starter%20Motor/Service%20and%20Repair/Removal%20and%20Replacement/Repair%20Procedures/

- Hyundai Accent RB six-speed inhibitor/range-switch TSB P0705/P0706/P0707/P0708:  
  https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Transmission%20and%20Drivetrain/Technical%20Service%20Bulletins/Customer%20Interest/A%2FT%20Controls%20-%20MIL%20ON%2FDTC%27s%20P0705%2FP0707%2FP0706%2FP0708/

---

## 30. Final diagnostic doctrine

```text
NO CRANK
   ↓
P OR N?
   ↓
BATTERY + GROUNDS
   ↓
IG2 / START POWER
   ↓
IGNITION SWITCH REQUEST
   ↓
P/N AUTHORIZATION
   ↓
STARTER RELAY
   ↓
S-TERMINAL COMMAND
   ↓
HIGH-CURRENT PATH
   ↓
STARTER / SOLENOID
   ↓
REPAIR ROOT CAUSE
   ↓
VERIFY IN BOTH P AND N
```

**The key asks for a start. The interlock decides whether starting is allowed. The relay carries the command. The solenoid closes the gate. The starter turns the engine. Diagnose the chain instead of guessing the link.**
