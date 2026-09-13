# Wiper, Washer & Rear Wiper Diagnostics — 2014 Hyundai Accent SE

> **Purpose:** diagnose front/rear wiper and washer faults on the 2014 Hyundai Accent SE while preserving safe visibility and avoiding unnecessary parts replacement.

## Source confidence

- **EXACT 2014 OWNER DATA** — Hyundai 2014 Accent owner manual.
- **SERVICE-FAMILY — 2012/2013 ACCENT 1.6** — same-generation Hyundai service information used as supporting guidance.
- **GENERAL DIAGNOSTIC PRACTICE** — standard automotive electrical/mechanical methods.

---

## Core doctrine

```text
VISIBILITY PROBLEM
→ IDENTIFY FRONT / REAR / WASHER / PARK FAULT
→ CHECK FUSES
→ CHECK SWITCH COMMAND
→ CHECK POWER + GROUND
→ CHECK MOTOR / PUMP
→ CHECK LINKAGE / ARM / HOSE / NOZZLE
→ REPAIR ROOT CAUSE
→ VERIFY ALL MODES
```

A motor that can be heard running does **not** prove the linkage is healthy.

A washer pump that can be heard running does **not** prove fluid is reaching the glass.

---

# Exact 2014 operating functions

## Front

With ignition ON, the front system provides:

- **MIST** — single wipe,
- **OFF**,
- **INT** — intermittent wipe, if equipped,
- **LO** — low speed,
- **HI** — high speed,
- intermittent timing adjustment, if equipped,
- front wash with brief wipes.

## Rear — 5-door

The rear control provides:

- wash with brief wipes,
- **ON** — normal rear-wiper operation,
- **OFF**.

---

# Exact 2014 fuse architecture

## Driver-side panel

```text
WIPER RR   15A
→ Multifunction Switch (Wiper)
→ Rear Wiper Motor

WIPER FRT  25A
→ Multifunction Switch (Wiper)
→ Front Wiper Motor
```

## Engine compartment

```text
WIPER      10A
→ ECM / PCM
→ Multifunction Switch (Wiper)
→ Front Wiper Motor
```

Practical routing:

```text
FRONT DEAD, REAR NORMAL
→ WIPER FRT 25A + engine-bay WIPER 10A + front circuit

REAR DEAD, FRONT NORMAL
→ WIPER RR 15A + rear motor/hatch circuit

FRONT + REAR BOTH ABNORMAL
→ shared switch/control feeds deserve early attention
```

Use only the original fuse rating.

---

# Visibility safety

Do not continue into rain, snow, sleet, road spray, mud, or other conditions that obstruct safe vision if the front wiper system cannot keep the windshield clear.

Stop driving when:

- front wipers do not operate in conditions that require them,
- a loose blade or arm threatens windshield damage,
- washer fluid freezes across the windshield,
- the linkage jams,
- the system overheats,
- vision cannot be kept safely clear.

The owner manual warns against operating the wipers on a dry windshield, forcing the wiper arms manually, and using the washer in freezing conditions before the windshield is warmed.

---

# Fast symptom map

| Symptom | First checks |
|---|---|
| No front wipers | front fuses, switch, motor feed/ground |
| HI works, LO dead | low-speed circuit, switch, motor |
| LO works, HI dead | high-speed circuit, switch, motor |
| INT dead, LO/HI normal | intermittent-control path |
| Stops wherever switched OFF | park circuit / motor / indexing |
| Motor runs, arms still | arm attachment / linkage |
| One arm moves | arm spline / linkage joint |
| Slow wipers | voltage, ground, binding linkage, frozen/dry blades |
| Fuse repeatedly opens | overcurrent, short, stalled motor/linkage |
| Pump silent | feed, switch, connector, pump, ground |
| Pump audible, no spray | reservoir, frozen fluid, hose, nozzle, leak |
| Rear only dead | WIPER RR 15A, rear motor, hatch harness |

---

# Front wiper workflow

1. Record which modes work: MIST, INT, LO, HI, wash.
2. Note whether the motor can be heard.
3. Inspect for ice, snow load, loose arms, and cowl obstruction.
4. Check `WIPER FRT 25A` and engine-bay `WIPER 10A`.
5. Verify switch command with the correct wiring/service diagram.
6. Verify motor power and ground under operating load.
7. If the motor runs but the arms do not move correctly, inspect the mechanical drive.

**SERVICE-FAMILY:** Hyundai 2012/2013 Accent service information specifies continuity testing of the wiper/washer switch in its operating positions. Publicly accessible terminal charts are image-rendered, so this repository does not invent terminal numbers.

---

# Motor runs but arms do not move

Possible causes:

- loose arm fastener,
- stripped arm spline,
- disconnected linkage joint,
- damaged linkage,
- seized pivot,
- damaged motor-to-linkage connection.

```text
MOTOR AUDIBLE + NO BLADE MOTION
→ CHECK MECHANICAL DRIVE FIRST
```

---

# Park-position faults

Symptoms include:

- blades stop wherever the switch is turned off,
- inconsistent resting position,
- blades rest too high or too low after previous work.

Possible causes:

- internal motor park circuit,
- motor wiring/connector,
- incorrect linkage indexing,
- incorrectly installed arms.

If the motor consistently completes a park cycle but the blades rest in the wrong physical position, mechanical indexing is more likely than an internal park-contact fault.

---

# Slow wipers

Electrical possibilities:

- low battery/charging voltage,
- high-resistance feed or ground,
- failing motor.

Mechanical possibilities:

- binding pivots,
- frozen blades,
- snow/ice loading,
- excessive dry-glass friction,
- bent linkage.

Measure voltage at the motor while it is actually operating. An unloaded reading alone does not prove the circuit can deliver current.

Cross-reference:

- [`../diagnostics/CHARGING_SYSTEM.md`](../diagnostics/CHARGING_SYSTEM.md)
- [`GROUND_POINTS.md`](GROUND_POINTS.md)
- [`WIRING_AND_CONNECTOR_DIAGNOSTICS.md`](WIRING_AND_CONNECTOR_DIAGNOSTICS.md)

---

# Repeated fuse failure

Do not repeatedly replace a fuse without finding the cause.

Possible causes include:

- wiring short,
- internally failed motor,
- motor stalled by seized linkage,
- frozen blades,
- moisture or connector damage.

Investigate the overcurrent cause before installing another fuse.

---

# Washer diagnosis

## Pump silent

Check:

- fluid level,
- circuit feed,
- switch command,
- pump connector power/ground,
- pump condition.

## Pump runs but no spray

Check:

- empty or low reservoir,
- frozen fluid,
- disconnected/split hose,
- kinked hose,
- blocked nozzle,
- leakage.

## Weak spray

Check:

- low fluid,
- partial freezing,
- restricted nozzle,
- hose restriction/leak,
- weak pump,
- low voltage at pump.

---

# Winter use

Hyundai warns not to use the washer in freezing temperatures without first warming the windshield because fluid may freeze on contact and obscure vision.

For cold-weather travel:

- use temperature-appropriate washer fluid,
- warm the glass before spraying in severe cold,
- clear frozen nozzles before repeated washer operation,
- carry spare washer fluid.

---

# Rear wiper workflow — 5-door

```text
REAR WIPER DEAD
→ VERIFY SWITCH COMMAND
→ CHECK WIPER RR 15A
→ CHECK REAR MOTOR CONNECTOR
→ CHECK HATCH FLEX-HARNESS
→ VERIFY MOTOR POWER / GROUND
→ CHECK ARM / SPLINE
```

The hatch harness flexes whenever the liftgate moves. Inspect it for damaged insulation, broken conductors, moisture, or faults that change with hatch position.

If rear wiper, hatch latch, rear defogger, or rear lighting problems appear together, inspect the hatch transition harness early.

See:

- [`BODY_CONTROL_DOOR_LATCH_INTERIOR_LIGHTING.md`](BODY_CONTROL_DOOR_LATCH_INTERIOR_LIGHTING.md)
- [`EXTERIOR_LIGHTING_TURN_STOP_HAZARD.md`](EXTERIOR_LIGHTING_TURN_STOP_HAZARD.md)

---

# Rear washer

If rear wash does not reach the glass:

- verify pump activity,
- inspect hose routing,
- inspect the hatch/body transition area,
- check for blockage or freezing,
- look for fluid leaking behind trim.

If washer fluid is leaking inside body trim, stop repeated operation and repair the leak before electrical components become soaked.

---

# Blade problems vs system problems

Blade faults include:

- streaking,
- chatter,
- skipping,
- smearing,
- poor glass contact.

Check blade rubber, contamination, arm condition, correct fitment, and windshield condition before dismantling electrical components.

---

# Nomad / rough-road inspection

Periodically inspect:

- front and rear arms,
- blade attachment,
- cowl debris,
- washer-fluid level,
- nozzle alignment,
- washer hoses,
- rear hatch harness boot,
- rear washer hose routing,
- blade rubber after dusty travel,
- correct spare fuses.

Dust and grit become abrasive under dry blades. Wet heavily dusty glass before wiping when practical.

---

# AI / Runa rules

Before naming a failed part, Runa should determine:

```text
NO COMMAND
NO POWER
NO GROUND
MOTOR FAILURE
MECHANICAL DISCONNECT
MECHANICAL BIND
PARK FAULT
WASHER DELIVERY FAULT
```

Ask for:

- front or rear,
- modes that work,
- motor/pump sound,
- physical arm movement,
- park behavior,
- weather/temperature,
- frozen-blade history,
- washer-fluid behavior,
- fuse condition,
- charging condition if wipers are slow.

---

# YAML incident record

```yaml
wiper_washer_incident:
  date: null
  mileage: null
  weather: null
  ambient_temperature: null
  front_wiper:
    mist: unknown
    intermittent: unknown
    low: unknown
    high: unknown
    parks_correctly: unknown
    motor_audible: unknown
  rear_wiper:
    on: unknown
    wash_wipe: unknown
    motor_audible: unknown
  washer:
    front_pump_audible: unknown
    front_spray: unknown
    rear_pump_audible: unknown
    rear_spray: unknown
    fluid_level: unknown
  fuses:
    wiper_frt_25a: unknown
    wiper_rr_15a: unknown
    engine_bay_wiper_10a: unknown
  diagnosis: null
  repair: null
  verified_all_modes: false
```

---

# Cross-references

- [`../specs/FUSES_AND_RELAYS.md`](../specs/FUSES_AND_RELAYS.md)
- [`POWER_DISTRIBUTION.md`](POWER_DISTRIBUTION.md)
- [`WIRING_AND_CONNECTOR_DIAGNOSTICS.md`](WIRING_AND_CONNECTOR_DIAGNOSTICS.md)
- [`GROUND_POINTS.md`](GROUND_POINTS.md)
- [`BODY_CONTROL_DOOR_LATCH_INTERIOR_LIGHTING.md`](BODY_CONTROL_DOOR_LATCH_INTERIOR_LIGHTING.md)
- [`EXTERIOR_LIGHTING_TURN_STOP_HAZARD.md`](EXTERIOR_LIGHTING_TURN_STOP_HAZARD.md)
- [`../diagnostics/CHARGING_SYSTEM.md`](../diagnostics/CHARGING_SYSTEM.md)
- [`../roadside/EMERGENCY_FIELD_REPAIRS.md`](../roadside/EMERGENCY_FIELD_REPAIRS.md)

---

# Sources

## Exact 2014 owner information

- Hyundai 2014 Accent Owner Manual: https://www.manualslib.com/manual/1067849/Hyundai-2014-Accent.html
- Rear wiper/washer, 5-door: https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/?srch=rear+washer
- Wiper operating modes: https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/?srch=wiper
- Fuse descriptions: https://manualzz.com/doc/53857913/hyundai-2014-accent-owner-manual
- Fuse search mirror: https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/2/?srch=fuse
- Engine-compartment fuse data: https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/?srch=relay

## Supporting same-generation Hyundai service information

- 2013 Accent wiper-switch service procedure: https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Sensors%20and%20Switches/Sensors%20and%20Switches%20-%20Wiper%20and%20Washer%20Systems/Wiper%20Switch/Service%20and%20Repair/
- 2012 Accent multifunction-switch inspection: https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Sensors%20and%20Switches/Sensors%20and%20Switches%20-%20Lighting%20and%20Horns/Combination%20Switch/Service%20and%20Repair/Repair%20Procedures/

---

# Final doctrine

```text
BAD VISIBILITY
→ VERIFY FUSES
→ VERIFY COMMAND
→ VERIFY POWER + GROUND
→ VERIFY MOTOR / PUMP
→ VERIFY LINKAGE / HOSE / NOZZLE
→ REPAIR ROOT CAUSE
→ VERIFY EVERY MODE BEFORE TRUSTING IT
```

> **If the glass cannot stay clear, the repair problem has become a driving-safety problem.**
