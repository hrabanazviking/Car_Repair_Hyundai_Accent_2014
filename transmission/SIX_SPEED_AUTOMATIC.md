# 2014 Hyundai Accent SE - Six-Speed Automatic Transaxle

> **Purpose:** Practical, source-aware reference for the six-speed automatic transaxle used in the U.S.-market 2014 Hyundai Accent SE with the 1.6 L Gamma GDI engine. Written for human field use and AI/RAG retrieval.
>
> **Core rule:** A shift symptom or transmission DTC identifies a system to test. It does **not** automatically prove that the complete transaxle is failed.

---

## 1. Scope

This document covers:

- six-speed automatic transaxle architecture
- transmission identity
- torque converter
- gear train and clutch elements
- valve body and solenoids
- transaxle range / inhibitor switch
- input and output speed sensing
- transmission-fluid-temperature sensing
- PCM/TCM control logic
- ATF specification and service interval
- delayed engagement
- slipping and flare
- harsh shifts
- fail-safe / limp behavior
- overheating and fluid-related faults
- DTC-driven diagnosis
- towing precautions
- field / nomad inspection
- AI diagnostic rules

Related repository files:

- `../specs/VEHICLE_BASELINE.md`
- `../specs/FLUIDS_AND_CAPACITIES.md`
- `../maintenance/MAINTENANCE_SCHEDULE.md`
- `../maintenance/PRE_TRIP_INSPECTION.md`
- `../maintenance/NOMAD_SERVICE_LOG.md`
- `../diagnostics/OBD2_GUIDE.md`
- `../diagnostics/CHARGING_SYSTEM.md`
- `../electrical/BATTERY_STARTER_ALTERNATOR.md`

---

# 2. Confidence Labels

This file uses the following labels:

- **VERIFIED - 2014 OWNER MANUAL:** Confirmed in the 2014 Hyundai Accent owner's manual.
- **VERIFIED - 2014 OE CATALOG:** Confirmed by 2014 Accent genuine-parts catalog data.
- **VERIFIED - HYUNDAI TSB:** Confirmed in a Hyundai technical service bulletin applicable to Accent RB.
- **CORROBORATED - SERVICE FAMILY:** Confirmed by same-generation / same-transaxle service information, but not treated as a VIN-specific 2014 workshop specification.
- **GENERAL AUTOMATIC-TRANSMISSION PRACTICE:** Standard diagnostic method, not a Hyundai-specific threshold.
- **PROVISIONAL:** Useful but not yet locked to an exact build/VIN source.

When a service-family value conflicts with an exact 2014 source, the exact 2014 source wins.

---

# 3. Transmission Identity

## Factory configuration

The 2014 Accent SE automatic uses:

- front-wheel drive
- six forward speeds
- one reverse speed
- electronically controlled automatic operation
- SHIFTRONIC / manual-select mode
- torque converter
- hydraulic valve body
- electronically controlled solenoids

The 2014 owner's manual explicitly states that the automatic transaxle has six forward speeds and one reverse speed.

## Model code

The six-speed unit used with the Gamma 1.6 GDI in the Accent RB is widely identified as:

```text
A6GF1
```

**Confidence:** CORROBORATED - SERVICE FAMILY / transmission application data.

Same-generation Hyundai service information identifies the automatic transaxle production code prefix `NA` as A6GF1, paired with the Gamma 1.6 GDI and a final-drive ratio of about 2.937.

Transmission-industry application guides also list:

```text
Hyundai Accent 2012-2017
1.6 L
A6GF1
```

Do not order an entire transmission solely from the model name. Verify by VIN, transaxle tag, production code, build date, and superseded part number.

---

# 4. Gear Ratios

Multiple 2014 vehicle-specification sources list approximately:

| Gear | Ratio |
|---|---:|
| 1st | 4.40 to 4.44 : 1 |
| 2nd | 2.73 : 1 |
| 3rd | 1.83 : 1 |
| 4th | 1.39 : 1 |
| 5th | 1.00 : 1 |
| 6th | 0.77 : 1 |
| Reverse | 3.44 : 1 |
| Final drive | about 2.94 : 1 |

The small 4.40-versus-4.44 discrepancy appears among third-party specification databases. Do not use this table for rebuilding or gear identification without VIN-specific Hyundai service data.

---

# 5. Major System Components

The automatic transaxle is not one indivisible component. It is a system containing mechanical, hydraulic, electrical, and electronic elements.

## Mechanical / hydraulic components

- torque converter
- internal oil pump
- planetary gear sets
- multiple clutch packs
- brake elements
- one-way clutch elements
- differential / final drive
- valve body
- accumulator circuits
- hydraulic passages
- pressure-control valves

## Electronic / electro-hydraulic components

2014 OE catalog data confirms a valve body containing:

- multiple solenoid valves
- pressure-control valves
- pressure switches
- oil-temperature sensor
- internal valve-body harness
- manual valve
- fail-safe valve

The same catalog identifies the 6AT 2WD internal harness and oil-temperature sensor family used by the 2014 Accent.

---

# 6. Torque Converter

The torque converter transfers engine power into the transaxle hydraulically and can include a lock-up clutch for efficient cruising.

Possible torque-converter-related symptoms include:

- shudder during lock-up
- RPM oscillation at steady cruise
- excessive slip
- stall or drag when stopping if lock-up remains applied
- delayed movement if hydraulic pressure is not established
- abnormal noise

Do not diagnose the torque converter from one symptom alone. Similar symptoms can result from:

- low or incorrect ATF
- engine misfire
- damaged mounts
- valve-body faults
- solenoid faults
- pressure-control faults
- internal clutch slip
- speed-sensor faults

---

# 7. Valve Body and Solenoids

The valve body is the hydraulic control center of the transaxle.

The PCM/TCM commands solenoids, and the valve body routes hydraulic pressure to the appropriate clutch and brake elements.

The 2014 Accent OE parts catalog confirms multiple valve-body solenoids and pressure-control components in the 6AT 2WD assembly.

Symptoms that may involve valve-body / solenoid operation include:

- harsh shifts
- delayed engagement
- no shift / stuck in one gear
- gear-ratio codes
- abnormal line pressure
- flare between gears
- missing gear
- limp mode

But the same symptoms can also come from wiring, sensor, fluid, mechanical, or engine problems.

---

# 8. Input and Output Speed Sensors

The controller compares input and output rotational speeds to determine whether the commanded gear ratio is actually occurring.

Useful diagnostic signals include:

- input/turbine speed
- output speed
- vehicle speed
- commanded gear
- actual ratio
- engine RPM

## Hyundai TSB relevance

Hyundai TSB **13-AT-014** applies to Accent RB and addresses:

- `P0717` - input speed sensor signal problem
- `P0721` - output speed sensor range/performance problem
- `P0722` - output speed sensor no signal

The bulletin's important diagnostic message is:

> Do not automatically replace the complete transaxle for these DTCs.

Hyundai directs diagnosis toward the related sensor / internal harness system.

### AI rule

If one of these codes is present:

```text
READ DTC + FREEZE FRAME
        ↓
CHECK LIVE INPUT / OUTPUT SPEED DATA
        ↓
CHECK WIRING / CONNECTORS
        ↓
CHECK INTERNAL SENSOR / HARNESS PATH
        ↓
ONLY THEN CONSIDER INTERNAL MECHANICAL FAILURE
```

Do not jump directly from `P0717`, `P0721`, or `P0722` to "transmission replacement."

---

# 9. Transmission Fluid Temperature Sensor

The controller uses ATF temperature to adjust pressure, shift scheduling, and protection strategies.

A failed temperature sensor can create bizarre shift behavior even when the mechanical gear train is intact.

## Hyundai TSB 14-AT-010

Hyundai TSB **14-AT-010**, issued June 2014, applies to Accent RB and addresses:

- `P0711` - transmission fluid temperature sensor rationality
- `P0712` - transmission fluid temperature sensor circuit low
- `P0713` - transmission fluid temperature sensor circuit high

Hyundai explicitly states that the transaxle should **not** automatically be replaced for these codes. The bulletin directs diagnosis toward the oil-temperature sensor and valve-body harness.

The service procedure also requires technicians to monitor the temperature-sensor PID while driving and check external wiring/connector condition before replacing internal components.

### Diagnostic pattern

```text
P0711 / P0712 / P0713
        ↓
PRESERVE DATA
        ↓
MONITOR TFT LIVE DATA
        ↓
FIXED / IMPOSSIBLE / ERRATIC READING?
        ↓
CHECK EXTERNAL HARNESS + CONNECTORS
        ↓
CHECK INTERNAL TFT SENSOR / HARNESS
        ↓
DO NOT CONDEMN WHOLE TRANSAXLE WITHOUT EVIDENCE
```

---

# 10. Range / Inhibitor Switch

The automatic transaxle must know which position the driver selected:

- P
- R
- N
- D
- manual / sports mode positions as applicable

The range / inhibitor switch participates in:

- starter-inhibit logic
- gear-position reporting
- reverse operation
- shift strategy
- transmission control

Possible symptoms of a range-switch or related-circuit fault include:

- starts in Neutral but not Park
- wrong gear displayed
- reverse lights incorrect
- unexpected limp mode
- no-crank despite good battery/starter
- range-related DTCs such as `P0705` / `P0706` / `P0707` / `P0708`, depending on exact fault

See also:

- `../diagnostics/NO_CRANK.md`
- `../specs/FUSES_AND_RELAYS.md`

---

# 11. Shift-Lever Operation

**VERIFIED - 2014 OWNER MANUAL**

Hyundai states:

- the transaxle has 6 forward speeds and one reverse
- the brake pedal must be depressed to move out of Park
- the vehicle should come to a complete stop before selecting Park or Reverse
- do not hold the vehicle on an incline with engine power
- do not select Drive or Reverse from Park/Neutral with the engine above idle
- always use the parking brake instead of relying solely on Park

## Shift lock

If the lever cannot be shifted normally from P or N into R even with the brake pedal depressed, Hyundai provides a mechanical shift-lock override procedure.

Using the override is not a repair. A shift-lock fault still needs diagnosis.

---

# 12. SHIFTRONIC / Sports Mode

The manual-selection mode allows the driver to request an upshift or downshift.

The controller still protects the drivetrain.

The 2014 manual notes that:

- only forward gears are selected in sports mode
- automatic downshifts occur as vehicle speed falls
- first gear is selected when the vehicle stops
- the controller may reject a requested shift when needed for protection
- an automatic upshift can occur near engine redline

Therefore:

```text
DRIVER REQUEST
      ≠
UNCONDITIONAL MECHANICAL COMMAND
```

The PCM/TCM remains in control of safe shift execution.

---

# 13. Automatic Transaxle Fluid

## Required specification

**VERIFIED - 2014 OWNER MANUAL**

Hyundai specifies:

```text
SP-IV / SP-4 type ATF
```

Examples listed in the manual include:

- MICHANG ATF SP-4
- SK ATF SP-4
- NOCA ATF SP-4
- Hyundai Genuine ATF SP-4
- other brands meeting the Hyundai-approved specification

Factory-listed system quantity:

```text
7.71 US qt
7.3 L
```

### Critical rule

Do **not** assume that the 7.3 L system capacity is a normal drain-and-refill amount.

Fluid remains inside:

- torque converter
- valve body
- clutch circuits
- passages
- cooler path
- case cavities

Use the correct service/level procedure.

## Do not substitute generic fluid casually

Incorrect friction characteristics can cause:

- harsh shifts
- flare
- clutch slip
- shudder
- overheating
- accelerated wear

"Universal ATF" is not automatically acceptable just because it is red.

---

# 14. ATF Color

Hyundai specifically warns that ATF color changes with use.

Fresh fluid is typically red, but darker fluid by itself does **not** prove that the fluid needs replacement.

Evaluate the whole picture:

- service interval
- odor
- debris
- shift quality
- overheating history
- contamination
- fluid specification
- DTCs

Dark color alone is not a diagnosis.

---

# 15. Maintenance Interval

## Normal service

The 2014 Hyundai maintenance schedule states:

```text
Automatic transaxle fluid:
No check, no service required under normal usage schedule
```

This should not be interpreted as "fluid can never deteriorate."

## Severe service

Hyundai specifies:

```text
Replace automatic transaxle fluid every 60,000 miles (96,000 km)
```

under applicable severe-use conditions.

Severe conditions include several patterns relevant to vehicle-based travel, such as:

- rough roads
- dusty roads
- muddy roads
- unpaved roads
- gravel roads
- extensive idling / low-speed driving
- heavy traffic in high temperatures
- frequent mountain driving
- towing / heavy-use conditions

For primitive-camping and nomad use, the severe-service interval may be the appropriate planning baseline.

---

# 16. Fluid-Level Work

Exact level-setting procedure must come from appropriate Hyundai service information for the exact transaxle/build.

Do not use a generic "fill until full" rule.

Hyundai 6-speed service procedures commonly involve:

- specified SP-IV fluid
- controlled fluid temperature
- cycling the selector through positions
- a defined fill/level or overflow check
- level verification with the vehicle positioned correctly

Because exact service procedure and temperature windows matter, do not improvise from system capacity alone.

### AI rule

If asked "how much ATF do I add after draining?" answer:

1. identify what service was performed
2. identify how much was actually drained
3. use SP-IV only
4. use the proper Hyundai level-setting procedure
5. do not blindly add 7.3 L

---

# 17. Symptom Classification

Before diagnosing, classify the behavior.

## A. Delayed engagement

Examples:

- shift P/R/N into D, vehicle waits before moving
- shift into R, long pause before reverse applies

Possible causes include:

- low ATF
- air ingestion
- hydraulic pressure leak
- valve-body problem
- solenoid / pressure-control fault
- worn clutch seals or clutch pack
- torque-converter drain-back
- incorrect fluid
- cold-temperature behavior

## B. Flare

Engine RPM rises during an upshift before the next gear applies.

Possible causes:

- clutch slip
- low hydraulic pressure
- valve-body leakage
- solenoid-control fault
- worn clutch
- incorrect/low ATF

Persistent flare is not normal.

## C. Slip under load

RPM rises disproportionately without matching vehicle acceleration.

Possible causes:

- clutch slip
- torque-converter slip
- inadequate hydraulic pressure
- fluid issue
- internal wear

Stop prolonged high-load operation until diagnosed.

## D. Harsh shift

Possible causes:

- low voltage
- adaptive strategy
- TFT sensor error
- input/output speed-sensor error
- pressure-control issue
- solenoid problem
- valve body
- engine torque-management fault
- mounts
- internal mechanical fault

## E. Stuck in one gear / fail-safe

Possible causes:

- critical sensor fault
- speed-sensor fault
- solenoid fault
- range fault
- wiring problem
- internal mechanical problem
- low system voltage

Scan all applicable modules before condemning hardware.

---

# 18. First Diagnostic Capture

Before disconnecting the battery or clearing codes, record:

```text
Mileage:
Outside temperature:
Cold or hot start:
ATF leak visible?:
Battery / charging voltage:
Gear selected:
Gear displayed:
Engine RPM:
Vehicle speed:
Commanded gear:
Input speed:
Output speed:
ATF temperature:
Stored DTCs:
Pending DTCs:
Freeze frame:
When symptom occurs:
  [ ] cold
  [ ] hot
  [ ] idle
  [ ] light throttle
  [ ] heavy throttle
  [ ] uphill
  [ ] downhill
  [ ] after highway run
  [ ] only D
  [ ] only R
  [ ] specific shift
```

This evidence is more valuable than clearing the warning light first.

---

# 19. Transmission DTC Families

Examples of useful code families include:

## Control-system overview

- `P0700` - transmission control system request / fault indication on implementations that use it

## Fluid-temperature sensor

- `P0711`
- `P0712`
- `P0713`

Hyundai TSB 14-AT-010 specifically addresses these on Accent RB.

## Input / output speed

- `P0717`
- `P0721`
- `P0722`

Hyundai TSB 13-AT-014 specifically addresses these on Accent RB.

## Range sensor family

- `P0705`
- `P0706`
- `P0707`
- `P0708`

Exact applicability and code wording must be verified by code source and scan tool.

## Gear-ratio codes

A ratio code may reflect:

- actual clutch slip
- hydraulic problem
- speed-sensor data problem
- solenoid/control fault
- incorrect fluid level
- mechanical damage

A ratio code does not by itself prove a worn clutch pack.

---

# 20. Low Voltage Can Imitate Transmission Failure

Electronic automatic transmissions depend on stable system voltage.

Low voltage can affect:

- sensor readings
- solenoid operation
- PCM/TCM communication
- shift-lock behavior
- range-switch interpretation
- network messages

If multiple unrelated DTCs appear after a weak-battery event, jump-start, or charging-system failure:

```text
CHECK BATTERY / CHARGING SYSTEM FIRST
```

See:

- `../diagnostics/CHARGING_SYSTEM.md`
- `../electrical/BATTERY_STARTER_ALTERNATOR.md`

---

# 21. Engine Problems Can Feel Like Transmission Problems

A transmission diagnosis must include engine health.

Possible impostors:

- ignition misfire
- fuel-pressure loss
- lean condition
- throttle-control fault
- engine mount failure
- severe low engine power
- unstable idle
- charging voltage problem

Example:

```text
"SHUDDER UNDER LOAD"
        ↓
Could be transmission lock-up shudder
OR
could be ignition misfire under load
```

Read engine DTCs and live data along with transmission data.

---

# 22. Cold Behavior

Cold ATF is thicker.

Some shift behavior may change temporarily after a cold start.

But do not dismiss:

- repeated harsh banging
- long engagement delay
- flare
- slipping
- warning lights
- gear-ratio DTCs

as "just cold" without evidence.

Record whether the symptom disappears as ATF temperature rises.

---

# 23. Heat and Mountain Use

Heat is one of the main enemies of automatic transmissions.

Conditions that raise thermal load include:

- long climbs
- repeated low-speed climbing
- heavy cargo
- high ambient temperature
- stop-and-go traffic
- repeated acceleration on steep grades
- excessive converter slip
- low fluid

For nomad / primitive travel:

- reduce speed before long steep grades
- avoid unnecessary heavy throttle
- avoid holding the car stationary with accelerator pressure
- stop if a burning ATF smell appears with abnormal shifting
- investigate any new leak before entering remote country

---

# 24. Stop-Driving Conditions

Stop and arrange towing / professional diagnosis when practical if any of the following occurs:

- major ATF leak
- vehicle will not reliably engage Drive or Reverse
- severe repeated slipping
- grinding / metallic internal noise
- transmission locks wheels
- smoke or burning fluid
- severe overheat behavior
- sudden loss of multiple gears
- shift into gear causes violent mechanical shock
- car cannot maintain safe traffic speed because of fail-safe operation

A short limp to a safer shoulder may be appropriate when necessary for immediate safety, but do not turn a failing transmission into a long-distance experiment.

---

# 25. Towing Rules

**VERIFIED - 2014 OWNER MANUAL**

Hyundai warns that if the automatic Accent is emergency-towed with all four wheels on the ground:

- tow from the front
- put the transaxle in Neutral
- unlock steering as required
- keep speed at or below about **10 mph / 15 km/h**
- keep distance under about **1 mile / 1.5 km**

If ATF is leaking, Hyundai directs use of a flatbed or towing dolly.

For normal recovery, a flatbed is the safest default when available.

---

# 26. Primitive-Road / Nomad Inspection

Before remote travel:

- look for ATF seepage under the vehicle
- verify no unresolved transmission warning / DTC condition
- confirm normal engagement of D and R
- confirm no new flare or slip
- confirm charging voltage is healthy
- inspect CV boots / drive shafts
- inspect underside after hard impacts
- confirm no fluid smell after steep or rough access roads

After deep ruts, rocks, or underbody contact:

- inspect transmission case and pan area
- inspect harness / connector area
- inspect mounts
- inspect drive shafts / CV boots
- look for fresh leaks

Do not assume a low-clearance impact only damaged cosmetic plastic.

---

# 27. Decision Tree - Harsh Shifting

```text
HARSH SHIFT
    ↓
Any DTCs?
    ↓
Battery / charging healthy?
    ↓
TFT data plausible and changing?
    ↓
Input/output speed data plausible?
    ↓
Range data correct?
    ↓
ATF leak / wrong-fluid history?
    ↓
Engine torque / misfire problem?
    ↓
Solenoid / valve body / hydraulic test
    ↓
Internal mechanical diagnosis
```

---

# 28. Decision Tree - Delayed Drive or Reverse Engagement

```text
DELAY SELECTING D OR R
        ↓
Cold only or hot too?
        ↓
ATF leak visible?
        ↓
Correct SP-IV service history?
        ↓
Range position reported correctly?
        ↓
Any solenoid / TFT / speed DTCs?
        ↓
Hydraulic pressure / valve body
        ↓
Internal clutch / seal / converter diagnosis
```

---

# 29. Decision Tree - Flare / Slip

```text
RPM FLARES DURING SHIFT
       ↓
Which shift?
       ↓
Cold / hot / load dependent?
       ↓
Check DTCs + speed data
       ↓
Verify fluid condition / level by correct procedure
       ↓
Check control / solenoid / pressure operation
       ↓
If commanded gear is correct but ratio slips:
internal hydraulic / clutch diagnosis becomes stronger
```

Do not repeatedly reproduce severe slip under heavy throttle just to "see if it does it again."

---

# 30. Known Hyundai TSB Diagnostic Lessons

## TSB 14-AT-010

Applicable to Accent RB from 2012 onward within the bulletin.

Codes:

```text
P0711
P0712
P0713
```

Diagnostic lesson:

```text
TFT SENSOR CODE
  ≠
TRANSMISSION REPLACEMENT
```

Check TFT data, wiring, sensor, and valve-body harness.

## TSB 13-AT-014

Applicable to Accent RB from 2012 onward within the bulletin.

Codes:

```text
P0717
P0721
P0722
```

Diagnostic lesson:

```text
SPEED SENSOR CODE
  ≠
TRANSMISSION REPLACEMENT
```

Check sensor/harness system before condemning the complete unit.

---

# 31. AI Diagnostic Rules

When an AI assistant answers a transmission question, it should:

1. Identify the exact symptom.
2. Ask whether the fault is cold-only, hot-only, load-dependent, or constant when that information is available.
3. Preserve and interpret DTCs and freeze-frame data.
4. Check battery/charging health before diagnosing electronic control faults.
5. Compare commanded state with measured state.
6. Use input/output speed data when available.
7. Treat TFT sensor codes according to Hyundai TSB logic.
8. Treat speed-sensor codes according to Hyundai TSB logic.
9. Check ATF specification and leak history.
10. Separate engine shudder/misfire from transmission shudder.
11. Escalate to hydraulic/mechanical failure only after electrical/control evidence has been considered.
12. Never recommend an entire transmission solely because one sensor-related DTC is present.
13. Never invent fluid-level temperatures, torque values, or pressure specifications.
14. If exact build-specific data is unknown, label it UNKNOWN or SERVICE-FAMILY instead of guessing.

---

# 32. Machine-Readable Summary

```yaml
vehicle:
  year: 2014
  make: Hyundai
  model: Accent
  trim: SE
  body: 5-door
  engine: 1.6L Gamma GDI
  drivetrain: FWD

transmission:
  type: conventional automatic transaxle
  speeds_forward: 6
  reverse_gears: 1
  shiftronic: true
  torque_converter: true
  model_code:
    value: A6GF1
    confidence: corroborated_service_family
  final_drive:
    value: 2.937
    confidence: corroborated_service_family

fluid:
  specification: SP-IV / SP-4
  factory_system_capacity_liters: 7.3
  factory_system_capacity_us_quarts: 7.71
  capacity_is_not_drain_fill_amount: true
  normal_schedule: no_routine_service
  severe_replace_miles: 60000
  severe_replace_km: 96000

controls:
  valve_body: true
  electronic_solenoids: true
  input_speed_sensor: true
  output_speed_sensor: true
  fluid_temperature_sensor: true
  range_switch: true

hyundai_tsb:
  - number: 14-AT-010
    system: transmission_fluid_temperature_sensor
    dtcs: [P0711, P0712, P0713]
    key_rule: do_not_replace_complete_transaxle_without_sensor_harness_diagnosis
  - number: 13-AT-014
    system: input_output_speed_sensor
    dtcs: [P0717, P0721, P0722]
    key_rule: do_not_replace_complete_transaxle_without_sensor_harness_diagnosis

stop_driving_if:
  - major_ATF_leak
  - severe_repeated_slip
  - violent_mechanical_noise
  - smoke_or_burning_fluid
  - loss_of_safe_acceleration
  - wheel_locking
  - multiple_gears_lost

towing:
  flatbed_preferred: true
  four_wheels_ground_emergency_only:
    max_speed_mph: 10
    max_distance_miles: 1
    gear: neutral

core_diagnostic_rule: "CODE OR SHIFT SYMPTOM -> PRESERVE DATA -> ELECTRICAL/CONTROL TESTS -> FLUID/HYDRAULIC TESTS -> INTERNAL MECHANICAL DIAGNOSIS"
```

---

# 33. Sources

Primary and high-value references used in this document:

## 2014 Hyundai Accent owner's manual

- https://www.manualslib.com/manual/1067849/Hyundai-2014-Accent.html
- https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/
- https://manuals.plus/m/28181eb364b39dbbb16f909d42f8e060859e68749899494eb6c5fca29f35b8b1

Key owner-manual items used:

- six-speed automatic operation
- P/R/N/D usage rules
- SHIFTRONIC behavior
- shift-lock override
- SP-IV specification
- 7.3 L listed capacity
- normal vs severe ATF maintenance
- emergency towing limits

## 2014 Accent OE parts catalog

- Valve body:
  https://www.hyundaipartsdeal.com/parts-list/2014-hyundai-accent/transmission/transmission_valve_body.html

- Automatic transaxle assembly:
  https://www.hyundaipartsdeal.com/parts-list/2014-hyundai-accent/transmission/transaxle_assy_auto.html

- Automatic gear train:
  https://www.hyundaipartsdeal.com/parts-list/2014-hyundai-accent/transmission/transaxle_gear_auto.html

## Hyundai TSB 14-AT-010

Subject: 6-speed automatic-transaxle oil-temperature sensor, P0711/P0712/P0713.

Searchable copy:

- https://manualzz.com/doc/23798011/hyundai-accent--azera--elantra--santa-fe--sonata--tucson-...

NHTSA document identifier referenced by public TSB indexes:

```text
SB-10059669-2273.pdf
NHTSA TSB 10059669
```

## Hyundai TSB 13-AT-014

Subject: automatic-transaxle input/output speed sensor DTCs P0717/P0721/P0722.

Searchable copy:

- https://manuals.plus/m/d9fa3aafcb1f2ea8b2c4480a178a3f3667fdc518fe8dcbd033a2bed899c11d7d

## A6GF1 application / architecture corroboration

- ATRA / transmission-industry application guide:
  https://atracom.blob.core.windows.net/webinars/import%2Fa6mf1_rebuild.pdf

This source lists the 2012-2017 Hyundai Accent 1.6 L application as A6GF1.

---

# 34. Repository Philosophy

A transmission is expensive enough that uncertainty must be handled explicitly.

```text
SHIFT PROBLEM
   ↓
PRESERVE DATA
   ↓
VERIFY VOLTAGE
   ↓
VERIFY SENSOR INPUTS
   ↓
VERIFY COMMANDS / SOLENOIDS
   ↓
VERIFY CORRECT FLUID / LEAK STATUS
   ↓
VERIFY HYDRAULIC RESPONSE
   ↓
ONLY THEN CONDEMN INTERNAL HARD PARTS
```

The most expensive possible repair should not be the first guess.

**Unknown is preferable to confidently wrong.**
