# 2014 Hyundai Accent SE — Nomad Service Log

> **Purpose:** A persistent, offline-friendly maintenance and repair history for a 2014 Hyundai Accent SE used for travel, camping, and long-term mobile living.
>
> **Primary rule:** Record what actually happened to the car, not what should have happened. This file is the vehicle's living history.

---

# 1. How to Use This File

Use this document to track:

- Mileage
- Oil changes
- Tire rotations and pressure checks
- Brake inspections and repairs
- Battery replacement and charging issues
- Coolant service
- Automatic transmission service
- Air-filter replacement
- Cabin-filter replacement
- Spark plugs
- Drive belt
- Suspension and steering work
- Wheel/alignment work
- OBD-II codes
- Warning lights
- Strange noises or smells
- Rough-road impacts
- Fluid leaks
- Fuel-economy changes
- Parts replaced
- Costs
- Shops used
- DIY work
- Upcoming maintenance

Related repository files:

- `MAINTENANCE_SCHEDULE.md`
- `PRE_TRIP_INSPECTION.md`
- `../specs/VEHICLE_BASELINE.md`
- `../specs/FLUIDS_AND_CAPACITIES.md`
- `../specs/FUSES_AND_RELAYS.md`
- `../guides/ROADSIDE_DIAGNOSTIC_TRIAGE.md`

---

# 2. Vehicle Identity

Fill these once and update only if necessary.

```yaml
vehicle:
  year: 2014
  make: Hyundai
  model: Accent
  trim: SE
  body: five-door hatchback
  drivetrain: FWD
  engine: 1.6L GDI inline-4
  transmission: 6-speed automatic
  vin: UNKNOWN
  build_date: UNKNOWN
  license_plate: OPTIONAL
  current_owner_since: 2014
```

Do not store sensitive information in a public repository unless intentionally desired.

---

# 3. Current Vehicle Snapshot

Update this section whenever the overall condition meaningfully changes.

```yaml
current_status:
  date: YYYY-MM-DD
  odometer_miles: UNKNOWN
  engine_status: operational
  transmission_status: operational
  braking_status: operational
  steering_status: operational
  battery_status: UNKNOWN
  tire_status: UNKNOWN
  check_engine_light: false
  active_warning_lights: []
  known_fluid_leaks: []
  known_unresolved_issues: []
  next_service_due: []
```

---

# 4. Known Long-Term History

Record reliable owner-known history here, even if exact dates or mileages are unavailable.

## Example format

| Approx. Date | Approx. Mileage | Event | Notes | Confidence |
|---|---:|---|---|---|
| 2014 | new | Vehicle acquired | Owned since new | OWNER VERIFIED |
| UNKNOWN | UNKNOWN | Battery replacement | Add details when known | OWNER MEMORY |
| UNKNOWN | UNKNOWN | Tire replacement | Add brand/date/mileage when known | OWNER MEMORY |

### Confidence labels

Use:

- `OWNER VERIFIED` — directly known and certain
- `RECEIPT VERIFIED` — supported by invoice/receipt
- `SHOP VERIFIED` — confirmed by repair facility records
- `PHYSICAL EVIDENCE` — supported by markings, date codes, labels, etc.
- `OWNER MEMORY` — remembered but exact details uncertain
- `UNKNOWN` — not enough information

Never turn uncertain history into fake precision.

---

# 5. Master Service Timeline

Append every meaningful maintenance or repair event here.

| Date | Mileage | Category | Work Performed | Parts / Fluids | Cost | Performed By | Next Due | Notes |
|---|---:|---|---|---|---:|---|---|---|
| YYYY-MM-DD | 000000 | Oil | Example only | 5W-20 + filter | $0.00 | DIY | 000000 | Delete example when real data begins |

Recommended category names:

- `Oil`
- `Cooling`
- `Transmission`
- `Brakes`
- `Tires`
- `Battery`
- `Charging`
- `Ignition`
- `Fuel`
- `Air Intake`
- `HVAC`
- `Steering`
- `Suspension`
- `Exhaust`
- `Electrical`
- `OBD-II`
- `Body`
- `Recovery`
- `Inspection`
- `Other`

---

# 6. Engine Oil History

Track every oil change separately because oil history is one of the most important long-term engine records.

| Date | Mileage | Oil Brand | Viscosity | API/ILSAC | Filter | Quantity Added | Severe Service? | Next Due |
|---|---:|---|---|---|---|---:|---|---:|

Additional notes:

- Record abnormal oil consumption.
- Record if oil smelled strongly of fuel.
- Record metallic debris if observed.
- Record leakage around filter, drain plug, pan, valve cover, or other areas.

## Oil-level observations

| Date | Mileage | Level | Amount Added | Notes |
|---|---:|---|---:|---|

---

# 7. Coolant History

| Date | Mileage | Service | Coolant Used | Amount | Reason | Notes |
|---|---:|---|---|---:|---|---|

Also record:

- Any overheating event
- Any coolant loss
- Any hose replacement
- Thermostat replacement
- Radiator repair/replacement
- Water-pump work
- Cooling-fan fault

### Overheat incident template

```markdown
## Overheat Incident — YYYY-MM-DD

**Mileage:**
**Outside temperature:**
**Road conditions:**
**Vehicle speed:**
**A/C on/off:**
**Temperature warning observed:**
**Steam observed:**
**Coolant level after cooling:**
**Leak found:**
**OBD coolant temperature if available:**
**Repair performed:**
**Outcome:**
```

---

# 8. Automatic Transmission History

| Date | Mileage | Service | Fluid Specification | Quantity | Condition Observed | Notes |
|---|---:|---|---|---:|---|---|

Record any:

- Delayed engagement
- Harsh shift
- Slip
- Flare between gears
- Shudder
- Limp mode
- Fluid leak
- Transmission-related DTC

Do not record a transmission fluid as compatible merely because it was sold as "universal." Record the actual specification printed on the product.

---

# 9. Tire and Wheel History

## Tire inventory

| Position | Brand | Model | Size | DOT Date Code | Installed Date | Installed Mileage | Tread Depth | Notes |
|---|---|---|---|---|---|---:|---|---|
| LF | | | 195/50R16 | | | | | |
| RF | | | 195/50R16 | | | | | |
| LR | | | 195/50R16 | | | | | |
| RR | | | 195/50R16 | | | | | |
| Spare | | | Compact spare | | | | | |

## Tire rotation log

| Date | Mileage | Rotation Pattern | Pressure Set | Uneven Wear? | Notes |
|---|---:|---|---|---|---|

## Tire pressure log

| Date | Mileage | LF | RF | LR | RR | Spare | Ambient Temp | Notes |
|---|---:|---:|---:|---:|---:|---:|---:|---|

Use the door-jamb placard as the final authority for normal tire inflation.

## Tire incident log

Record:

- Punctures
- Sidewall damage
- Impact damage
- Bead leaks
- Bent wheels
- Tire replacements
- Flat repairs

---

# 10. Brake History

| Date | Mileage | Axle / Wheel | Inspection or Repair | Pad Thickness | Rotor Condition | Fluid Condition | Cost | Notes |
|---|---:|---|---|---|---|---|---:|---|

Record symptoms such as:

- Pulling
- Pulsation
- Grinding
- Squeal
- Soft pedal
- Long pedal travel
- ABS warning
- Parking-brake weakness

Any hydraulic leak is safety-critical.

---

# 11. Battery and Charging History

## Battery inventory

| Installed Date | Installed Mileage | Brand | Model | Group | CCA | Date Code | Removed Date | Reason |
|---|---:|---|---|---|---:|---|---|---|

## Voltage observations

| Date | Mileage | Engine Off | Cranking | Engine Running | Electrical Load | Notes |
|---|---:|---:|---:|---:|---|---|

## Charging incidents

Record:

- Battery warning lamp
- Dead battery
- Slow crank
- Jump starts
- Alternator replacement
- Cable/terminal repair
- Parasitic-draw diagnosis

---

# 12. Spark Plug and Ignition History

| Date | Mileage | Plugs Installed | Gap | Coils Replaced | Reason | Notes |
|---|---:|---|---|---|---|---|

For any removed spark plug, useful observations include:

- Normal tan/gray deposit
- Wet with fuel
- Oil fouling
- Heavy carbon
- White/overheated appearance
- Damaged electrode
- Unusual gap

Do not diagnose solely from plug color; use it as supporting evidence.

---

# 13. Engine Air Filter History

| Date | Mileage | Action | Brand / Part | Condition | Dust Exposure | Notes |
|---|---:|---|---|---|---|---|

For nomad use, add a note after significant dust-road exposure.

---

# 14. Cabin Filter History

| Date | Mileage | Action | Brand / Part | Condition | Notes |
|---|---:|---|---|---|---|

---

# 15. Drive Belt History

| Date | Mileage | Condition | Tension | Cracking | Fraying | Replaced? | Notes |
|---|---:|---|---|---|---|---|---|

---

# 16. Suspension and Steering History

| Date | Mileage | Location | Symptom | Inspection | Repair | Alignment Performed? | Notes |
|---|---:|---|---|---|---|---|---|

Record:

- Clunks
- Steering looseness
- Pulling
- Wandering
- Vibration
- Uneven tire wear
- Strut leakage
- Ball-joint play
- Tie-rod play
- Damaged boots
- Bent components

---

# 17. Rough-Road and Impact Log

This section is specifically for primitive-camping and unpaved-road use.

Record any significant event even if the car seems fine afterward.

| Date | Mileage | Location | Road Type | Event | Speed | Contact Point | Immediate Symptoms | Follow-up |
|---|---:|---|---|---|---:|---|---|---|

Examples:

- Bottomed suspension
- Hit deep pothole
- Scraped center crown
- Rock contacted underbody
- Wheel dropped into rut
- Mud/water crossing
- Heavy washboard road
- Traction-board recovery
- Tow/recovery event

### Post-impact checklist

After a meaningful impact, inspect when safe:

- [ ] Tire sidewalls
- [ ] Wheel rims
- [ ] Tire pressure
- [ ] Oil leaks
- [ ] Coolant leaks
- [ ] Transmission-fluid leaks
- [ ] Exhaust damage
- [ ] Plastic splash shields
- [ ] Steering feel
- [ ] Brake feel
- [ ] New vibration
- [ ] New noises
- [ ] Alignment/pulling

---

# 18. OBD-II Diagnostic History

Never erase a code from history merely because it was cleared from the ECU.

| Date | Mileage | Stored Codes | Pending Codes | Permanent Codes | Symptoms | Freeze Frame Saved? | Repair | Returned? |
|---|---:|---|---|---|---|---|---|---|

## Detailed diagnostic incident template

```markdown
## Diagnostic Event — YYYY-MM-DD — Odometer _____

### Symptoms


### Stored DTCs


### Pending DTCs


### Permanent DTCs


### Freeze Frame


### Live Data

- Battery voltage:
- RPM:
- Coolant temperature:
- STFT:
- LTFT:
- MAP:
- Other:

### Tests Performed


### Findings


### Root Cause


### Repair


### Verification


### Did the fault return?

```

---

# 19. Warning-Light History

| Date | Mileage | Warning Light(s) | Driving Condition | Codes | Cause | Repair | Notes |
|---|---:|---|---|---|---|---|---|

Useful lights to track include:

- Check engine / MIL
- Oil pressure
- Battery/charging
- ABS
- ESC
- TPMS
- Airbag/SRS
- Steering/MDPS
- Brake warning

---

# 20. Noise / Vibration / Smell Log

Small changes often appear before failures.

| Date | Mileage | Type | Description | When It Happens | Temperature | Speed / RPM | Suspected Area | Outcome |
|---|---:|---|---|---|---|---|---|---|

Suggested `Type` values:

- Noise
- Vibration
- Smell
- Handling
- Performance
- Electrical

Describe sounds instead of only labeling them:

Good:

> Rapid metallic ticking for 3 seconds on cold start after sitting overnight.

Less useful:

> Weird engine noise.

---

# 21. Fuel Economy Log

Changes in fuel economy can reveal maintenance problems.

| Date | Odometer | Gallons Added | Miles Since Fill | MPG | Driving Type | A/C Use | Notes |
|---|---:|---:|---:|---:|---|---|---|

Formula:

```text
MPG = miles driven / gallons added
```

Do not overreact to one tank. Look for trends across several comparable fill-ups.

Potential causes of meaningful MPG decline include:

- Low tire pressure
- Winter fuel
- Cold temperatures
- Heavy idling
- Roof/cargo drag
- Heavy load
- Brake drag
- Alignment issues
- Dirty air filter
- Sensor/fuel-trim problems
- Driving-condition changes

---

# 22. Repair Parts History

| Date | Mileage | Part | Manufacturer | Part Number | Source | Warranty | Removed/Replaced Date | Notes |
|---|---:|---|---|---|---|---|---|---|

This is particularly useful for identifying whether a failed component is OEM, original, aftermarket, or previously replaced.

---

# 23. Repair and Maintenance Cost Log

| Date | Mileage | Category | Description | Parts | Labor | Tax/Fees | Total |
|---|---:|---|---|---:|---:|---:|---:|

### Annual totals

| Year | Maintenance | Repairs | Tires | Recovery/Towing | Total |
|---|---:|---:|---:|---:|---:|

This is not only budgeting data. Rising repair frequency can reveal when reliability is changing.

---

# 24. Shop / Mechanic History

| Name | Location | Phone | Work Performed | Experience | Would Return? | Notes |
|---|---|---|---|---|---|---|

Avoid storing private personal information about individual mechanics unless necessary.

---

# 25. Recovery / Breakdown History

| Date | Mileage | Location | Failure | Vehicle Movable? | Recovery Method | Tow Distance | Cost | Root Cause |
|---|---:|---|---|---|---|---:|---:|---|

Record even minor recoveries. Repeated incidents may reveal a pattern.

---

# 26. Upcoming Maintenance Queue

Keep this current.

## Urgent

- [ ] None recorded

## Due soon

- [ ] None recorded

## Monitor

- [ ] None recorded

## Optional / convenience

- [ ] None recorded

---

# 27. Next-Due Table

Update whenever service is completed.

| Item | Last Done Date | Last Done Mileage | Next Due Date | Next Due Mileage | Severe Schedule? | Status |
|---|---|---:|---|---:|---|---|
| Engine oil/filter | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | likely | UNKNOWN |
| Tire rotation | UNKNOWN | UNKNOWN | — | UNKNOWN | — | UNKNOWN |
| Engine air filter | UNKNOWN | UNKNOWN | — | UNKNOWN | dust-dependent | UNKNOWN |
| Cabin filter | UNKNOWN | UNKNOWN | — | UNKNOWN | dust-dependent | UNKNOWN |
| Coolant | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | no | UNKNOWN |
| ATF | UNKNOWN | UNKNOWN | — | UNKNOWN | use-dependent | UNKNOWN |
| Spark plugs | UNKNOWN | UNKNOWN | — | UNKNOWN | — | UNKNOWN |
| Drive belt inspection | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | — | UNKNOWN |
| Brake inspection | UNKNOWN | UNKNOWN | — | UNKNOWN | use-dependent | UNKNOWN |

Use `MAINTENANCE_SCHEDULE.md` to calculate intervals.

---

# 28. Service Due Calculation Rules for AI

When an AI reads this file:

1. Find the **latest confirmed service event** for the component.
2. Find the applicable interval in `MAINTENANCE_SCHEDULE.md`.
3. Determine whether the vehicle is being used under normal or severe conditions.
4. Calculate both mileage-based and time-based due points where applicable.
5. Use whichever comes first.
6. If history is unknown, say **history unknown** instead of assuming the service was completed.
7. If the vehicle is already overdue by age, do not reset the interval until service is actually documented.
8. If two records conflict, prefer the one with stronger provenance.

### Example

```text
Last oil change: 72,000 miles
Current mileage: 74,900 miles
Severe interval: 3,750 miles
Next due: 75,750 miles
Remaining: 850 miles
```

---

# 29. AI Query Examples

This service log should eventually support questions such as:

```text
What maintenance is due in the next 2,000 miles?
```

```text
When was the battery last replaced?
```

```text
Has this car ever had a recurring P0302 misfire?
```

```text
How many times has it overheated?
```

```text
Has fuel economy declined over the last six tanks?
```

```text
Which repairs have cost the most money?
```

```text
Has the right-front tire lost pressure repeatedly?
```

```text
What changed before the steering vibration began?
```

```text
What service should I do before driving 2,000 highway miles?
```

```text
Show every event after a rough-road underbody impact.
```

---

# 30. Machine-Readable Summary

Keep this small and current. Detailed history remains in the tables above.

```yaml
service_summary:
  updated: UNKNOWN
  odometer_miles: UNKNOWN

  operating_profile:
    nomad_use: planned
    primitive_road_use: planned
    severe_service_assumption: true_when_conditions_apply

  last_service:
    engine_oil:
      date: UNKNOWN
      mileage: UNKNOWN
    tire_rotation:
      date: UNKNOWN
      mileage: UNKNOWN
    engine_air_filter:
      date: UNKNOWN
      mileage: UNKNOWN
    cabin_filter:
      date: UNKNOWN
      mileage: UNKNOWN
    coolant:
      date: UNKNOWN
      mileage: UNKNOWN
    automatic_transmission_fluid:
      date: UNKNOWN
      mileage: UNKNOWN
    spark_plugs:
      date: UNKNOWN
      mileage: UNKNOWN
    brake_inspection:
      date: UNKNOWN
      mileage: UNKNOWN

  unresolved_faults: []
  recurring_dtcs: []
  active_leaks: []
  active_noises: []
  active_vibrations: []
  upcoming_services: []
```

---

# 31. Repository Data Discipline

The service log should distinguish:

```text
FACT
│
├── exact date/mileage from receipt
├── owner-observed event
├── physical evidence
└── diagnostic measurement

from

INFERENCE
│
├── likely service date
├── suspected part age
├── estimated mileage
└── probable cause
```

Never convert an estimate into a factual maintenance record.

If the exact mileage is unknown, use:

```text
UNKNOWN
```

or:

```text
~75,000 mi
```

if the approximation is genuinely useful and clearly marked.

---

# 32. Core Philosophy

A repair manual tells you what a Hyundai Accent is supposed to need.

A service log tells you what **this Hyundai Accent** has actually experienced.

Both matter.

```text
FACTORY SCHEDULE
      +
REAL VEHICLE HISTORY
      +
CURRENT SYMPTOMS
      ↓
BETTER MAINTENANCE DECISIONS
```

The longer this log is maintained, the more useful it becomes to both the owner and an offline AI diagnostic system.

---

## Document Status

- **Vehicle:** 2014 Hyundai Accent SE
- **Document type:** Persistent maintenance / repair history
- **Primary use:** Human + offline AI retrieval
- **Initial state:** Template awaiting actual vehicle-history data
- **Data policy:** Unknown values remain unknown until verified
