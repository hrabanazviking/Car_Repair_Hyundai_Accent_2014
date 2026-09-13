# Exterior Lighting, Turn, Stop & Hazard Diagnostics — 2014 Hyundai Accent SE

> **Purpose:** diagnose headlamp, parking/tail, stop-lamp, turn-signal, hazard, reverse, license-plate, and related exterior-lighting faults on the 2014 Hyundai Accent SE without replacing bulbs, switches, relays, or modules by guesswork.

## Source Confidence

- **EXACT 2014 OWNER DATA** — Hyundai 2014 Accent owner-manual information, including fuse assignments, bulb specifications, operating behavior, and safety warnings.
- **SERVICE-FAMILY — 2012/2013 ACCENT** — same-generation Accent service procedures used for component-test concepts where exact 2014 workshop information is not publicly available.
- **GENERAL ELECTRICAL PRACTICE** — standard 12 V automotive diagnostic methods clearly separated from Hyundai-specific specifications.

Primary sources are linked in [Sources](#sources).

---

# Core Rule

```text
LIGHT DOES NOT WORK
       ≠
BAD BULB PROVEN
```

The correct diagnostic chain is:

```text
VERIFY SYMPTOM
     ↓
COMPARE LEFT / RIGHT / FRONT / REAR
     ↓
CHECK BULB / LED HARDWARE
     ↓
CHECK FUSE / SHARED FEED
     ↓
CHECK SWITCH / COMMAND
     ↓
CHECK RELAY / CONTROL
     ↓
CHECK POWER AT LOAD
     ↓
CHECK GROUND UNDER LOAD
     ↓
CHECK CONNECTOR / HARNESS
     ↓
REPAIR ROOT CAUSE
     ↓
VERIFY ALL RELATED LAMPS
```

A lighting fault becomes much easier to diagnose when it is classified by **scope**:

- one lamp,
- one side,
- one function,
- several lamps on a shared branch,
- or nearly the entire lighting system.

---

# 1. Exact 2014 Exterior-Lighting Hardware

## Headlamp configurations

**EXACT 2014 OWNER DATA**

The 2014 Accent manual lists two headlamp configurations:

### Type A — Multi Focus Reflector

```text
Low / High beam bulb:
HB2 L/L
55 / 60 W
```

### Type B — Bi-Function Projection

```text
Headlamp bulb:
9005L+
60 W
```

Hyundai notes that the bi-function projection headlamp changes low/high beam using a solenoid mechanism, so a switching sound can be normal.

Do not assume the vehicle has one headlamp type without inspecting the actual installed assembly.

## Exact 2014 bulb table relevant to the 5-door SE

| Function | 2014 specification |
|---|---:|
| Front turn signal | 28/8 W, PY28/8W |
| Position lamp, Type A | 5 W, W5W L/L |
| Position lamp, Type B | LED |
| Side marker, Type A | 5 W, W5W L/L |
| Side marker, Type B | LED |
| Side repeater, if equipped | 5 W, WY5W |
| Front fog lamp, if equipped | 27 W, GE881 |
| Stop / tail lamp | 28/8 W, P28/8W |
| Rear turn signal, 5-door | 27 W, PY27W |
| Back-up lamp | 16 W, W16W |
| High-mounted stop lamp, 5-door | 5 W, W5W L/L |
| License-plate lamp | 5 W, W5W L/L |

Source: exact 2014 Accent owner-manual bulb table.

---

# 2. Exact 2014 Fuse and Feed Map

## Interior fuse panel

**EXACT 2014 OWNER DATA**

### T/SIG — 10 A

Protected component:

```text
Hazard switch
```

This is a useful clue if turn-signal behavior and hazard-switch behavior fail together.

### STOP LAMP — 15 A

Protected components include:

```text
Stop lamp switch
Battery sensor
Stop lamp relay
Engine-room fuse / relay box HAC relay
Data link connector
```

Because this fuse feeds more than the rear brake bulbs themselves, a blown STOP LAMP fuse can create symptoms beyond “no brake lights.”

### HAZARD — 15 A

Protected components:

```text
Hazard relay
Hazard switch
```

### TAIL LAMP LH — 10 A

Protected components include:

```text
Rear combination lamp LH
Headlamp LH
Front turn signal lamp LH
License lamp(s)
```

### TAIL LAMP RH — 10 A

Protected components include:

```text
Headlamp RH
Rear combination lamp RH
Front turn signal lamp RH
Hazard switch
instrument-panel illumination and several switch-illumination loads
```

### H/LAMP — 10 A

Protected components:

```text
Instrument cluster
Engine-room fuse / relay box headlamp relay
```

## Engine-room fuse panel

**EXACT 2014 OWNER DATA**

```text
H/LAMP RH   10 A → right headlamp
H/LAMP LH   10 A → left headlamp
B/UP LAMP   10 A → PCM, range switch, cluster, rear combination lamps, shift illumination
```

The left and right headlamp branches being separately fused is diagnostically important.

### Practical interpretation

```text
ONE HEADLAMP OUT
→ first suspect local bulb / fuse / connector / ground

BOTH HEADLAMPS OUT
→ look farther upstream at H/LAMP control, relay, multifunction switch, shared feed, power distribution
```

---

# 3. Headlamp Diagnostics

## One headlamp out

Check in this order:

1. Verify whether both low and high beam are affected.
2. Inspect the correct left or right headlamp fuse.
3. Inspect the bulb or headlamp module appropriate to Type A or Type B.
4. Verify connector terminal condition.
5. Measure power at the lamp while commanded ON.
6. Measure ground voltage drop under load.
7. Wiggle the connector and nearby harness while watching lamp operation.

### Important interpretation

```text
POWER PRESENT + GOOD GROUND + LAMP DARK
→ lamp / bulb hardware strongly suspect

NO POWER AT LAMP
→ trace upstream

POWER COLLAPSES ONLY UNDER LOAD
→ high resistance in fuse / relay / connector / harness
```

## Both headlamps out

Before replacing both bulbs, verify:

- H/LAMP control fuse,
- headlamp relay control,
- multifunction switch command,
- battery voltage,
- IG / lighting-system feed,
- relay socket condition,
- common power distribution.

See:

- [`POWER_DISTRIBUTION.md`](POWER_DISTRIBUTION.md)
- [`RELAY_CONTROL_CIRCUITS.md`](RELAY_CONTROL_CIRCUITS.md)
- [`WIRING_AND_CONNECTOR_DIAGNOSTICS.md`](WIRING_AND_CONNECTOR_DIAGNOSTICS.md)

## High beam works but low beam does not

Possible causes include:

- failed low-beam filament or lamp element,
- multifunction-switch fault,
- headlamp internal fault,
- Type B bi-function solenoid/control fault,
- connector or circuit damage affecting only the low-beam path.

Do not assume both headlamp configurations behave identically.

## Low beam works but high beam does not

Check:

- high-beam filament or bi-function mechanism,
- multifunction-switch high/passing command,
- associated wiring and connector state.

For Type B projection headlamps, remember that a solenoid is involved in high/low switching.

---

# 4. Multifunction / Combination Switch

**SERVICE-FAMILY — 2012 ACCENT**

Hyundai service information checks the multifunction switch by verifying continuity in each switch position for:

- lighting switch,
- high beam,
- low beam,
- flash-to-pass,
- turn signal,
- front fog lamp.

If continuity is not as specified, the service procedure directs replacement of the multifunction switch.

### Diagnostic rule

```text
MULTIPLE LIGHTING FUNCTIONS FAIL
THAT SHARE THE STALK
       ↓
TEST SWITCH COMMAND
BEFORE REPLACING MULTIPLE LAMPS
```

A switch can fail mechanically or electrically while downstream bulbs remain healthy.

---

# 5. Turn-Signal Diagnostics

## Exact 2014 operating behavior

The ignition switch must be ON for normal turn signals to operate.

Hyundai states:

- green arrows in the cluster indicate the active direction,
- the lever normally self-cancels after a completed turn,
- one-touch lane-change operation, if equipped, flashes three times,
- an indicator that stays on without flashing or flashes abnormally can indicate a burned-out bulb,
- abnormally fast or slow flashing can also indicate a poor electrical connection.

## Fast flash

Do not automatically replace the flasher/hazard electronics.

Check:

1. front turn lamp on affected side,
2. rear turn lamp on affected side,
3. bulb type and wattage,
4. socket condition,
5. corrosion,
6. ground quality,
7. aftermarket LED conversion or incorrect load,
8. harness damage.

### Wrong bulb warning

A wrong-wattage bulb may still illuminate but can change circuit load and flash behavior.

Use the exact 2014 bulb type unless a properly engineered replacement has been verified.

## Turn signal does not flash but stays lit

Possible causes:

- burned-out companion bulb,
- poor socket connection,
- wrong bulb/load,
- ground fault,
- hazard/turn control fault,
- multifunction-switch fault.

## Neither left nor right turn signal works

Check:

- T/SIG fuse,
- HAZARD fuse,
- hazard switch,
- hazard relay/control,
- ignition-state requirements,
- body/junction-box power,
- multifunction switch.

---

# 6. Hazard-Flasher Diagnostics

## Exact 2014 behavior

The hazard warning flasher:

- operates with the ignition switch in any position,
- operates whether the engine is running or not,
- flashes all turn-signal lamps simultaneously,
- disables normal turn-signal operation while the hazards are active.

### Diagnostic leverage

```text
TURN SIGNALS DEAD
BUT HAZARDS WORK
       ↓
BULBS / GROUNDS / MUCH OF LOAD PATH PROVEN
LOOK HARDER AT TURN COMMAND / IGNITION-SWITCHED SIDE
```

Conversely:

```text
HAZARDS DEAD
AND TURN SIGNALS DEAD
       ↓
CHECK SHARED POWER / HAZARD SWITCH / HAZARD RELAY / COMMON WIRING
```

---

# 7. Brake / Stop-Lamp Diagnostics

## Exact 2014 feed

```text
STOP LAMP fuse: 15 A
```

Protected components include the stop-lamp switch and stop-lamp relay.

## No brake lamps at all

Check:

1. STOP LAMP fuse.
2. Brake-pedal stop-lamp switch operation.
3. Switch connector.
4. Stop-lamp relay/control.
5. Shared power feed.
6. Rear-lamp harness.
7. Ground paths.

Do not begin by replacing both rear bulbs when the high-mounted stop lamp is also dead.

## High-mounted stop lamp works, lower brake lamps do not

This strongly suggests the pedal switch and much of the upstream command path are functioning.

Shift attention toward:

- rear combination-lamp bulbs,
- rear lamp connectors,
- side-specific feeds,
- common rear grounding,
- body harness.

## Lower brake lamps work, high-mounted stop lamp does not

Inspect:

- 5-door high-mounted stop bulb(s),
- hatch harness/flex section,
- connector,
- ground,
- lamp assembly.

The 5-door high-mounted stop lamp uses 5 W W5W L/L bulbs per the 2014 specification table.

## Brake lamps remain on continuously

Possible causes include:

- stop-lamp switch adjustment or failure,
- brake-pedal stopper/interface problem,
- wiring short,
- relay/control fault.

Do not ignore this condition. Continuous stop lamps can discharge the battery and remove the visual distinction between braking and cruising.

See also:

- [`PARASITIC_DRAW_BATTERY_DRAIN.md`](PARASITIC_DRAW_BATTERY_DRAIN.md)

---

# 8. Tail / Parking / Position Lamp Diagnostics

## One side out

Because left and right tail-lamp branches are separately protected, check the corresponding side fuse and local harness first.

```text
LEFT SIDE DARK
→ TAIL LAMP LH branch + local lamp + connector + ground

RIGHT SIDE DARK
→ TAIL LAMP RH branch + local lamp + connector + ground
```

## Both sides out

Check:

- lighting switch command,
- tail-lamp relay/control,
- upstream junction-box feed,
- common power distribution,
- body control logic where applicable.

## One side dimmer than the other

Suspect resistance, especially ground resistance.

Measure voltage drop under load rather than relying only on continuity.

---

# 9. Bad Grounds and Cross-Lighting Symptoms

Exterior lamps share body grounds and can create strange symptoms when the ground path becomes resistive.

Possible signs include:

- brake lamp makes turn signal glow,
- turn signal changes tail-lamp brightness,
- lamp glows dimly through another filament,
- multiple lamps pulse together,
- brightness changes when another electrical load is activated.

### Why it happens

Current seeks an alternate return path when the normal ground is poor.

The alternate path may travel backward through another bulb filament or circuit, producing symptoms that appear illogical until the ground is tested.

### Test method

With the lamp operating:

```text
METER + → lamp ground terminal / ground side of load
METER - → clean battery negative
```

A meaningful voltage reading indicates voltage is being lost in the ground path.

See:

- [`GROUND_POINTS.md`](GROUND_POINTS.md)

---

# 10. License-Plate Lamp Diagnostics

For the 5-door Accent, the 2014 manual lists:

```text
License lamp: 5 W W5W L/L
```

The left-side tail-lamp fuse description specifically includes the 5-door license lamp.

If both license lamps or the single applicable lamp function are dark, inspect:

- TAIL LAMP LH fuse,
- bulb(s),
- hatch harness,
- connector corrosion,
- ground,
- water intrusion near the hatch/lamp area.

Because hatch wiring flexes repeatedly, intermittent opens deserve special attention.

---

# 11. Reverse-Lamp Diagnostics

The 2014 manual lists:

```text
Back-up lamp bulb: 16 W W16W
Engine-room B/UP LAMP fuse: 10 A
```

That fuse also participates in circuits involving the PCM, transaxle range switch, cluster, rear combination lamps, and shift illumination.

Therefore:

```text
REVERSE LAMPS DEAD
        +
RANGE / SHIFT-INDICATOR ANOMALY
        ↓
CHECK RANGE-SWITCH INPUT / B/UP FEED / SHARED WIRING
```

Do not assume two failed reverse bulbs when transmission-range information is also abnormal.

Cross-reference:

- [`IGNITION_SWITCH_START_INTERLOCK.md`](IGNITION_SWITCH_START_INTERLOCK.md)
- [`../transmission/SIX_SPEED_AUTOMATIC.md`](../transmission/SIX_SPEED_AUTOMATIC.md)

---

# 12. Bulb and Socket Inspection

Look for:

- broken filament,
- darkened bulb glass,
- melted socket,
- green/white corrosion,
- overheated terminal,
- spread female terminal,
- loose bulb fit,
- water intrusion,
- damaged seal,
- evidence of wrong bulb type.

## A continuity test is not enough

A socket can show continuity with no load yet fail under operating current.

Use:

- voltage under load,
- voltage drop,
- test light where appropriate,
- connector tension inspection.

---

# 13. Halogen-Bulb Safety

**EXACT 2014 OWNER DATA**

Hyundai warns that halogen bulbs contain pressurized gas and can produce flying glass if broken.

When servicing:

- allow the bulb to cool,
- wear eye protection,
- do not scratch the bulb,
- do not contact a lit bulb with liquid,
- do not touch the glass with bare fingers,
- replace cracked or damaged bulbs.

Oil from skin can cause local overheating and shorten bulb life or contribute to failure.

---

# 14. LED / Aftermarket Conversion Caution

The factory electrical system was designed around specified bulb loads and, for some configurations, factory LEDs.

Aftermarket LED substitutions can create:

- hyperflash,
- bulb-out behavior,
- dim glow,
- radio interference,
- polarity problems,
- heat at added resistors,
- incorrect beam pattern,
- poor weather sealing.

Do not add load resistors casually. They intentionally convert electrical energy into heat and can damage nearby wiring or plastic if installed poorly.

---

# 15. Roadside Night-Driving Decision

## Stop / do not continue normal night driving when

- both low beams are unavailable,
- brake lamps are not functioning,
- tail lamps are not visible at night,
- the electrical fault is producing smoke, heat, or repeated fuse failure,
- a harness is visibly shorting,
- lighting operation is unstable enough that other traffic cannot reliably see or interpret the vehicle.

## Limited movement may be reasonable only when

- traffic law permits,
- visibility remains adequate,
- required lighting functions remain operational,
- the fault is understood and stable,
- movement is only to reach a safer repair location.

Do not use hazard flashers as a substitute for functional required nighttime lighting.

---

# 16. Repeated Fuse Failure

If a replacement fuse blows again:

```text
STOP REPLACING FUSES
       ↓
FIND THE SHORT / OVERLOAD
```

Hyundai explicitly requires the same fuse rating and warns against wire, foil, or oversized substitutes.

Look for:

- crushed harness,
- melted socket,
- water-filled lamp,
- chafed wire,
- incorrect bulb,
- aftermarket wiring,
- trailer/accessory wiring modifications,
- failed component internally shorted.

---

# 17. Diagnostic Patterns

## One lamp only

```text
BULB / LED
SOCKET
LOCAL CONNECTOR
LOCAL GROUND
LOCAL HARNESS
```

## One whole side

```text
SIDE-SPECIFIC FUSE
SIDE HARNESS
COMMON SIDE GROUND
JUNCTION CONNECTOR
```

## Both sides, same function

```text
SHARED FUSE
SWITCH COMMAND
RELAY
BODY / JUNCTION CONTROL
COMMON POWER
```

## Several unrelated lamps

```text
SHARED POWER
SHARED GROUND
JUNCTION BOX
BODY HARNESS
AFTERMARKET WIRING
LOW SYSTEM VOLTAGE
```

## Strange cross-lighting

```text
GROUND FIRST
THEN SOCKET / HARNESS BACKFEED
```

---

# 18. AI / Runa Diagnostic Rules

An offline AI using this repository should:

1. Record exactly which lamps fail.
2. Record left/right/front/rear.
3. Record ignition state.
4. Record whether hazards work.
5. Record whether cluster indicators work.
6. Record whether the high-mounted stop lamp works.
7. Record related fuses and their measured state.
8. Distinguish bulb failure from missing power and missing ground.
9. Never infer a failed switch only from a dead lamp.
10. Never infer a bad BCM from multiple lighting faults before verifying shared feeds and grounds.
11. Treat repeated fuse failure as an active electrical fault, not a reason to install a larger fuse.
12. Preserve Type A vs Type B headlamp configuration.
13. Prefer exact-year owner data over adjacent-year service assumptions.

### Recommended evidence record

```yaml
lighting_fault:
  date:
  ignition_state:
  engine_running:
  battery_voltage:
  affected_lamps:
    left_front:
    right_front:
    left_rear:
    right_rear:
    high_mount_stop:
    license:
    reverse:
  hazards_work:
  turn_left_work:
  turn_right_work:
  cluster_indicators:
  fuse_checks:
  voltage_at_load:
  ground_voltage_drop:
  bulb_type_verified:
  connector_condition:
  water_intrusion:
  aftermarket_wiring_present:
  repair:
  post_repair_verification:
```

---

# 19. Core Diagnostic Doctrine

```text
DARK LAMP
   ↓
CLASSIFY SCOPE
   ↓
VERIFY BULB / LOAD
   ↓
VERIFY FUSE
   ↓
VERIFY COMMAND
   ↓
VERIFY POWER
   ↓
VERIFY GROUND UNDER LOAD
   ↓
VERIFY HARNESS / CONNECTOR
   ↓
REPAIR ROOT CAUSE
   ↓
VERIFY EVERY RELATED LAMP
```

And the central rule:

> **A light bulb is only the final load. Diagnose the circuit that is supposed to make it glow.**

---

# Related Repository Guides

- [`FUSES_AND_RELAYS.md`](../specs/FUSES_AND_RELAYS.md)
- [`POWER_DISTRIBUTION.md`](POWER_DISTRIBUTION.md)
- [`RELAY_CONTROL_CIRCUITS.md`](RELAY_CONTROL_CIRCUITS.md)
- [`GROUND_POINTS.md`](GROUND_POINTS.md)
- [`WIRING_AND_CONNECTOR_DIAGNOSTICS.md`](WIRING_AND_CONNECTOR_DIAGNOSTICS.md)
- [`BODY_CONTROL_DOOR_LATCH_INTERIOR_LIGHTING.md`](BODY_CONTROL_DOOR_LATCH_INTERIOR_LIGHTING.md)
- [`PARASITIC_DRAW_BATTERY_DRAIN.md`](PARASITIC_DRAW_BATTERY_DRAIN.md)
- [`IGNITION_SWITCH_START_INTERLOCK.md`](IGNITION_SWITCH_START_INTERLOCK.md)
- [`../roadside/EMERGENCY_FIELD_REPAIRS.md`](../roadside/EMERGENCY_FIELD_REPAIRS.md)

---

# Sources

## Exact 2014 Hyundai owner information

- Hyundai 2014 Accent Owner Manual — lighting operation, hazard operation, turn-signal behavior, fuse assignments, bulb specifications, bulb-service warnings:
  https://manualzz.com/doc/53857913/hyundai-2014-accent-owner-manual

- Hyundai 2014 Accent Owner Manual — searchable copy, headlamp and bulb specifications:
  https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/?srch=headlamp

- Hyundai 2014 Accent Owner Manual — fuse information:
  https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/?srch=fuse

- Hyundai 2014 Accent Owner Manual PDF mirror — bulb table:
  https://www.dezosmanuals.com/wp-content/uploads/2021/07/2014-Hyundai-Accent-OM.pdf

## Same-generation Hyundai service-family information

- 2012 Accent multifunction/combination-switch inspection:
  https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Sensors%20and%20Switches/Sensors%20and%20Switches%20-%20Lighting%20and%20Horns/Combination%20Switch/Service%20and%20Repair/Repair%20Procedures/

- 2012 Accent relay-box testing and relay internal configurations:
  https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Relays%20and%20Modules/Relays%20and%20Modules%20-%20Power%20and%20Ground%20Distribution/Relay%20Box/Testing%20and%20Inspection/

- 2013 Accent lighting/horn repair index:
  https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/

---

## Provenance Note

Exact 2014 owner-manual data is treated as primary for bulb type, fuse assignment, operating behavior, and owner-level safety procedures. Same-generation 2012/2013 service information is used only for diagnostic structure and component-test concepts where exact 2014 workshop information is not publicly available. Unknown exact 2014 circuit details remain unknown rather than being guessed.