# NVH Noise, Vibration & Harshness Matrix — 2014 Hyundai Accent SE

> **Purpose:** provide a master symptom-routing guide for noises, vibrations, shudders, pulsations, rattles, clunks, hums, growls, whines, buzzes, and harshness complaints on the 2014 Hyundai Accent SE.
>
> **Core principle:** NVH is not a parts list. It is a pattern-recognition problem. Classify **when** the symptom happens, **what speed it follows**, **what input changes it**, and **where it is felt** before choosing a subsystem to inspect.

## Source Confidence

- **EXACT 2014 OWNER DATA** — Hyundai 2014 Accent owner-manual information.
- **SERVICE-FAMILY — 2012/2013 ACCENT 1.6** — same-generation Accent workshop information used as supporting diagnostic data.
- **GENERAL NVH PRACTICE** — standard automotive NVH isolation methods used only as routing logic, not as Hyundai-specific specifications.

Primary sources are linked in [Sources](#sources).

---

# 1. Core NVH Rule

```text
NOISE / VIBRATION / HARSHNESS
        ↓
DO NOT NAME A PART YET
        ↓
CLASSIFY THE PATTERN
        ↓
ENGINE SPEED?
VEHICLE SPEED?
THROTTLE / LOAD?
STEERING INPUT?
BRAKE INPUT?
ROAD SURFACE?
TEMPERATURE?
        ↓
ROUTE TO THE MOST LIKELY SYSTEM
        ↓
TEST
        ↓
PROVE ROOT CAUSE
```

A useful shorthand for Runa/Aesir is:

```text
WHEN + SPEED SOURCE + LOAD + LOCATION + INPUT = NVH SIGNATURE
```

Example:

```text
WHEN: 45–60 mph
SPEED SOURCE: vehicle-speed dependent
LOAD: little change on/off throttle
LOCATION: steering wheel
INPUT: changes with road surface

→ tire/wheel path rises strongly
```

That is much more useful than:

```text
"car shakes"
```

---

# 2. First Question: Engine Speed or Vehicle Speed?

## Follows engine RPM even while parked

Suspect systems that rotate or react to engine torque:

- engine misfire / combustion roughness,
- engine/transaxle mounts,
- roll rod,
- accessory-drive pulley or bearing,
- A/C compressor pulley/clutch,
- exhaust contact,
- engine mechanical imbalance,
- loose shields or brackets.

Crosslinks:

- [`../diagnostics/MISFIRE.md`](../diagnostics/MISFIRE.md)
- [`ENGINE_TRANSAXLE_MOUNTS_VIBRATION.md`](ENGINE_TRANSAXLE_MOUNTS_VIBRATION.md)
- [`../engine/ACCESSORY_DRIVE_BELT.md`](../engine/ACCESSORY_DRIVE_BELT.md)
- [`../hvac/AC_COMPRESSOR_REFRIGERANT_DIAGNOSTICS.md`](../hvac/AC_COMPRESSOR_REFRIGERANT_DIAGNOSTICS.md)

## Follows vehicle speed regardless of engine RPM

Suspect rotating road-speed components:

- tire/wheel imbalance,
- out-of-round tire,
- tire force variation,
- bent wheel,
- irregular tire wear,
- wheel bearing,
- CV axle/joint,
- brake rotor/drum contact,
- final drive/differential,
- debris or mud packed in a wheel.

Crosslinks:

- [`../tires-wheels/TIRES_WHEELS.md`](../tires-wheels/TIRES_WHEELS.md)
- [`CV_AXLES_WHEEL_BEARINGS.md`](CV_AXLES_WHEEL_BEARINGS.md)
- [`DIFFERENTIAL_FINAL_DRIVE_AXLE_SEALS.md`](DIFFERENTIAL_FINAL_DRIVE_AXLE_SEALS.md)
- [`../brakes/BRAKE_SYSTEM.md`](../brakes/BRAKE_SYSTEM.md)

## Changes primarily with road surface

Raise tire tread / tire construction / wheel / suspension interaction on the list.

If a hum or vibration is strong on coarse pavement but falls sharply on smooth pavement, that pattern is more tire-like than a failing bearing or differential.

The 2014 owner manual states that vibration on a smooth road may indicate the wheels need rebalancing.

---

# 3. Master Symptom Matrix

| Symptom | Strongest pattern clues | First systems to inspect | Important look-alikes |
|---|---|---|---|
| Steering-wheel shake at highway speed | vehicle-speed dependent, strongest on smooth road | front tires/wheels, balance, bent rim, tire force variation | brake pulsation, front suspension looseness |
| Seat/floor vibration at highway speed | vehicle-speed dependent, rearward feel | rear tires/wheels, rear hub/bearing | exhaust resonance, driveline vibration |
| Clicking on tight turns | steering angle + low-speed torque | outer CV joint/boot | brake shield contact, loose wheel hardware |
| Shudder mainly during acceleration | load dependent, road-speed related | inner CV joint, mount/roll rod | engine misfire, transaxle slip |
| Clunk R↔D while stationary | torque reversal, not road-speed dependent | mounts/roll rod, inner CV play | harsh transaxle engagement |
| Hum/growl rising with road speed | road-speed dependent | tire tread, wheel bearing | differential/final drive |
| Hum changes with road surface | pavement dependent | tire tread / tire construction | bearing noise |
| Growl changes with gentle left/right loading | wheel-load sensitive | wheel bearing/hub | tire cupping |
| Whine on acceleration | load dependent | transaxle/final drive, bearing | tire noise, alternator/accessory noise |
| Whine on coast | changes when throttle released | final drive/differential, wheel bearing | tire tread |
| Rhythmic thump once per wheel revolution | low-speed periodic | tire defect, separated belt, flat spot, bent wheel | brake rotor contamination |
| Vibration only while braking | brake-input dependent | rotor runout/thickness variation, wheel/hub mating | suspension looseness |
| Pedal pulsation during ABS event | hard braking / low traction | normal ABS modulation if conditions justify it | warped rotor complaint |
| Brake pedal pulsation during ordinary braking | repeatable at same speeds | rotor/runout/hub surface | ABS activation from wheel-speed fault |
| Idle shake in Park/Neutral | engine-speed related | misfire, mounts, accessory load | exhaust contact |
| Smooth engine but body buzz at idle | engine-speed related, RPM smooth | mounts, exhaust/body contact | misfire |
| Buzz only with A/C on | compressor load dependent | A/C compressor/pulley, mount amplification | radiator/condenser fan contact |
| Rattle over bumps | road-input dependent | sway links, strut mount, loose shield, exhaust | loose cargo/interior trim |
| Knock over potholes | sharp suspension travel | ball joint, control arm bushing, strut, tie rod | loose brake hardware |
| Chirp/squeal with engine RPM | RPM related | accessory belt/pulley | brake squeal if only moving |
| Scrape/grind with wheel rotation | road-speed periodic | brakes, dust shield, bearing, CV | tire contacting liner |
| Steering vibration during turns | steering/load sensitive | tire/wheel, CV, bearing, tie rod/ball joint | MDPS feedback/road texture |
| Vibration after tire service | immediate post-service | wheel seating, lug torque, balance, bead seating | bent hub/wheel |
| Vibration after axle service | post-repair onset | axle seating, hub/axle nut, inner joint, seal/bearing | tire balance |
| Vibration after brake service | brake-related or wheel-speed related | rotor/hub mating, wheel torque, caliper drag | tire/wheel issue |

The matrix routes investigation. It does **not** prove failure.

---

# 4. Highway-Speed Steering-Wheel Vibration

## Strong pattern

```text
SMOOTH ROAD
+
SPECIFIC SPEED BAND
+
STEERING-WHEEL SHAKE
        ↓
TIRE / WHEEL PATH FIRST
```

Check:

1. cold tire pressure,
2. missing balance weights,
3. bent wheel flange,
4. mud/ice packed inside wheel,
5. irregular tire wear,
6. incomplete bead seating,
7. tire bulge or deformation,
8. lug-nut seating and torque,
9. dynamic balance,
10. tire radial-force variation if ordinary balance does not solve the complaint.

NHTSA states that tire balancing is used so wheels rotate properly without causing vehicle shake or vibration.

Hyundai also published broader wheel/tire vibration guidance that treats imbalance, tire force variation, and temporary flat spotting as separate possibilities.

### Important

A wheel can be perfectly balanced and still have:

- radial runout,
- tire force variation,
- a shifted belt,
- bent rim,
- hub-mating contamination,
- or structural tire damage.

So:

```text
BALANCE MACHINE SAYS 0.00
        ≠
TIRE / WHEEL ASSEMBLY PROVEN GOOD
```

---

# 5. Tire Flat Spot vs Mechanical Vibration

After sitting for an extended period, especially in cold weather, tires can temporarily develop flat spots.

Typical pattern:

- vibration is strongest during the first part of the drive,
- decreases as tires warm,
- may be worse in cold ambient temperatures,
- does not necessarily indicate a damaged wheel bearing or axle.

But a vibration that remains constant or worsens should not be dismissed as a temporary flat spot.

Inspect for actual tire damage.

---

# 6. Wheel Bearing vs Tire Noise

## Tire-like clues

- changes dramatically with pavement type,
- follows tread pattern,
- accompanied by cupping/scalloping,
- shifts after tire rotation,
- worsens with irregular pressure or wear.

## Bearing-like clues

- hum/growl rises with road speed,
- less dependent on pavement texture,
- may change as vehicle load shifts left/right,
- may accompany hub roughness, play, or ABS wheel-speed irregularity.

But:

```text
NO PLAY
  ≠
BEARING GOOD
```

A noisy bearing can exist before obvious free play develops.

See [`CV_AXLES_WHEEL_BEARINGS.md`](CV_AXLES_WHEEL_BEARINGS.md).

---

# 7. CV Joint Pattern Matrix

## Outer CV joint

Classic clues:

- clicking or snapping during tight turns,
- worse under light-to-moderate throttle,
- torn outer boot,
- grease thrown around wheel-well area.

## Inner CV joint

Classic clues:

- shudder or vibration during acceleration,
- may reduce when throttle is released,
- can mimic mount or tire vibration,
- inner boot damage or grease loss may be present.

Do not condemn an inner CV joint without checking mounts, tires, and engine running quality.

See [`CV_AXLES_WHEEL_BEARINGS.md`](CV_AXLES_WHEEL_BEARINGS.md).

---

# 8. Mount vs Misfire vs Inner CV

This is one of the most valuable three-way splits.

## Misfire more likely when

- vibration follows engine RPM,
- idle quality is rough,
- tachometer/RPM behavior may fluctuate,
- misfire counters or P030x codes are present,
- exhaust note is uneven,
- symptoms can exist while stationary.

## Mount/roll rod more likely when

- engine runs smoothly but vibration transfers strongly into body,
- clunk occurs during torque reversal,
- visible powertrain movement is excessive,
- exhaust/body contact appears under load,
- symptom can occur while stationary.

## Inner CV more likely when

- shudder appears mainly while the car is moving under acceleration,
- strongly tied to drivetrain torque,
- often fades when throttle is reduced,
- not reproduced by revving stationary in Park/Neutral.

Crosslinks:

- [`../diagnostics/MISFIRE.md`](../diagnostics/MISFIRE.md)
- [`ENGINE_TRANSAXLE_MOUNTS_VIBRATION.md`](ENGINE_TRANSAXLE_MOUNTS_VIBRATION.md)
- [`CV_AXLES_WHEEL_BEARINGS.md`](CV_AXLES_WHEEL_BEARINGS.md)

---

# 9. Brake Pulsation vs ABS Pulsation

## Normal ABS feedback

Same-generation Hyundai service information notes that brake-pedal vibration can occur during ABS operation because hydraulic pressure is being modulated to prevent wheel lock.

That is not automatically a brake defect.

## Ordinary brake pulsation

If pulsation occurs repeatedly during normal braking on dry pavement without a legitimate ABS event, investigate:

- brake disc runout,
- rotor thickness variation,
- hub/rotor mating contamination,
- wheel-bearing/hub issues,
- uneven wheel-lug torque,
- caliper drag,
- suspension looseness.

Same-generation Accent front-disc service information gives a supporting new-disc runout limit of **0.04 mm / 0.0016 in** and instructs measurement near the outer circumference.

That value remains tagged **SERVICE-FAMILY**, not exact 2014 VIN workshop authority.

See [`../brakes/BRAKE_SYSTEM.md`](../brakes/BRAKE_SYSTEM.md).

---

# 10. Steering-Sensitive NVH

If the symptom changes with steering input, classify **why**.

## At parking-lot speeds

Suspect:

- outer CV joint,
- strut mount/bearing,
- tie rod end,
- ball joint,
- spring bind,
- tire rubbing,
- steering rack/MDPS mechanical path.

## At road speed

Suspect:

- wheel bearing load shift,
- tire construction/irregular wear,
- wheel imbalance interacting with steering system,
- front suspension looseness.

## Warning

Do not perform aggressive weaving to diagnose NVH.

Use only gentle steering inputs on a safe road with ample space and within traffic laws.

---

# 11. Road-Bump Clunks and Rattles

## Sharp metallic rattle

Check:

- brake pad/caliper hardware,
- exhaust heat shields,
- underbody shields,
- loose brackets,
- sway-bar links,
- loose cargo or trim.

## Heavy knock

Check:

- ball joint,
- control-arm bushing,
- strut mount,
- loose strut-to-knuckle hardware,
- tie rod,
- subframe attachment,
- broken spring.

## Repeated clunk on rough primitive roads

Stop and inspect promptly.

Primitive-road vibration can loosen or damage:

- splash shields,
- exhaust hangers,
- wheel-well liners,
- sway links,
- underbody fasteners,
- brake or ABS harness retainers.

See [`../suspension-steering/STEERING_SUSPENSION.md`](../suspension-steering/STEERING_SUSPENSION.md).

---

# 12. Whine: Accessory, Tire, Bearing, or Final Drive?

## Engine-RPM whine while stationary

Raise:

- alternator,
- water-pump bearing,
- idler,
- A/C compressor pulley,
- belt system.

## Vehicle-speed whine

Raise:

- tire tread,
- wheel bearing,
- final-drive/differential,
- transaxle bearing.

## Load-sensitive whine

If it changes substantially between acceleration and coast, final-drive/transaxle investigation rises on the list.

If it stays similar regardless of throttle but tracks speed, tire/wheel-bearing causes remain strong.

See:

- [`../engine/ACCESSORY_DRIVE_BELT.md`](../engine/ACCESSORY_DRIVE_BELT.md)
- [`DIFFERENTIAL_FINAL_DRIVE_AXLE_SEALS.md`](DIFFERENTIAL_FINAL_DRIVE_AXLE_SEALS.md)

---

# 13. Buzz, Boom, Drone, and Resonance

These are often transmission-path problems rather than failed rotating parts.

Potential causes:

- weakened engine/transaxle mount,
- exhaust touching body/subframe,
- loose heat shield,
- underbody panel resonance,
- tire tread resonance,
- interior trim/cargo resonance.

A mount can amplify an otherwise modest engine vibration into a strong cabin boom.

A heat shield can sound like an engine failure at one very specific RPM.

Do not diagnose by drama level.

---

# 14. Temperature-Dependent NVH

## Cold only

Consider:

- temporary tire flat spots,
- belt stiffness,
- mount rubber stiffness,
- cold transmission-fluid behavior,
- heat-shield contraction/contact.

## Hot only

Consider:

- bearing expansion,
- belt/pulley thermal behavior,
- exhaust expansion/contact,
- electrical connector fault aggravated by heat,
- A/C compressor/fan operation.

Same-generation Hyundai diagnostic guidance explicitly uses controlled vibration and heat simulation to reproduce intermittent electrical faults in connectors, sensors, actuators, and relays.

---

# 15. Location of Felt Vibration

## Steering wheel

Bias investigation toward:

- front tire/wheel,
- front hub/bearing,
- front brake rotor,
- steering/suspension.

## Seat / floor

Bias investigation toward:

- rear tire/wheel,
- rear hub,
- powertrain mounts,
- exhaust contact,
- drivetrain resonance.

## Brake pedal

Bias toward:

- ABS event,
- rotor/runout/thickness issue,
- wheel/hub issue.

## Accelerator pedal / firewall

Bias toward:

- powertrain mount,
- engine roughness,
- exhaust/body contact,
- drivetrain load vibration.

These are routing clues only.

---

# 16. After-Repair NVH

If the complaint began immediately after service, start with whatever was disturbed.

## After tire/wheel service

Check:

- wheel centered on hub,
- correct wheel hardware,
- proper lug torque,
- balance,
- bead seating,
- tire pressure,
- missing weights.

## After brake service

Check:

- rotor/hub mating surface,
- wheel-lug torque,
- caliper hardware,
- rotor runout,
- dragging pad/caliper.

## After axle service

Check:

- inner CV fully seated,
- axle splines,
- axle lock nut,
- wheel bearing/hub,
- axle seal area,
- ABS tone/sensor condition.

## After mount service

Check:

- mount seating,
- bracket alignment,
- fastener torque,
- exhaust clearance,
- harness/ground straps disturbed during repair.

---

# 17. Primitive-Road / Nomad NVH Inspection

After rough washboard, potholes, gravel, ruts, or primitive-road travel, inspect for:

- missing wheel weights,
- mud/stone packed inside wheels,
- tire sidewall damage,
- fresh CV grease sling,
- bent splash shields,
- exhaust/heat-shield contact,
- loose underbody panels,
- broken wire/hose retainers,
- torn CV boots,
- strut or shock leakage,
- loosened cargo that can mimic chassis noise.

For this low-clearance Accent:

```text
NEW NOISE AFTER UNDERBODY CONTACT
        ↓
STOP AND INSPECT
```

Do not assume it is merely cosmetic.

---

# 18. NVH Road-Test Record

Use a repeatable record instead of memory.

```yaml
nvh_event:
  date:
  odometer_miles:
  ambient_temperature:
  road_surface:
  speed_mph:
  engine_rpm:
  gear:
  throttle_state: idle | cruise | accel | decel
  braking: none | light | moderate | hard
  steering: straight | left | right
  symptom_type: click | clunk | hum | growl | whine | buzz | shake | shudder | pulsation | rattle
  frequency: constant | intermittent | rhythmic
  felt_location: steering_wheel | seat | floor | pedal | body | unknown
  changes_with_engine_rpm:
  changes_with_vehicle_speed:
  changes_with_throttle:
  changes_with_braking:
  changes_with_steering:
  changes_with_road_surface:
  cold_vs_hot:
  warning_lamps:
  dtcs:
  recent_service:
  recent_impact_or_rough_road:
  suspected_systems:
  confidence:
```

---

# 19. Severity Classes

## GREEN — investigate soon

Examples:

- minor trim rattle,
- mild tire noise with no damage,
- small buzz at one RPM with no structural concern.

## YELLOW — diagnose before remote travel

Examples:

- new highway vibration,
- clicking CV joint,
- wheel-bearing growl,
- recurring brake pulsation,
- mount clunk,
- load-sensitive drivetrain shudder.

## RED — stop driving or tow

Examples:

- severe new vibration with uncertain cause,
- wheel visibly loose or wobbling,
- bulged/separated tire,
- grinding wheel bearing with play,
- violent brake pulsation with loss of control,
- broken suspension/steering component,
- axle visibly displaced,
- major ATF leak plus drivetrain noise,
- vibration after impact with damaged wheel/tire/structure.

---

# 20. AI / Runa Diagnostic Rules

When answering an NVH complaint:

1. Do not name a failed part from sound description alone.
2. Ask or infer whether the symptom follows engine RPM or vehicle speed.
3. Record the speed band where it is strongest.
4. Record whether throttle/load changes it.
5. Record whether braking changes it.
6. Record whether steering input changes it.
7. Record whether road surface changes it.
8. Record where the vibration/noise is felt.
9. Check recent service or road impact.
10. Route to the appropriate subsystem guide.
11. Treat multiple simultaneous clues as a pattern, not separate failures by default.
12. If wheel/tire structural damage, steering looseness, brake failure, severe bearing play, or axle displacement is suspected, prioritize safety over further road testing.

### Confidence labels

Use:

- **OBSERVED** — directly seen/heard/measured.
- **STRONG PATTERN MATCH** — symptom behavior strongly fits a known subsystem.
- **PLAUSIBLE** — fits but has important competing causes.
- **UNCONFIRMED** — insufficient evidence.
- **PROVEN** — confirmed by a direct test or failed component inspection.

Never promote **STRONG PATTERN MATCH** to **PROVEN** without testing.

---

# 21. Master Routing Flow

```text
NVH COMPLAINT
      ↓
SAFE TO ROAD TEST?
      ↓
IF NO → STOP / TOW / INSPECT
      ↓
ENGINE RPM OR VEHICLE SPEED?
      ↓
THROTTLE-SENSITIVE?
BRAKE-SENSITIVE?
STEERING-SENSITIVE?
ROAD-SURFACE-SENSITIVE?
      ↓
LOCATE WHERE FELT
      ↓
CHECK RECENT SERVICE / IMPACT
      ↓
ROUTE:
ENGINE / MOUNTS
TIRES / WHEELS
CV / HUB / BEARING
BRAKES
SUSPENSION / STEERING
FINAL DRIVE / TRANSAXLE
EXHAUST / BODY
ACCESSORY DRIVE
      ↓
TEST ROOT CAUSE
      ↓
REPAIR
      ↓
REPEAT SAME ROAD TEST
      ↓
LOG RESULT
```

---

# 22. Crosslinks

- [`../tires-wheels/TIRES_WHEELS.md`](../tires-wheels/TIRES_WHEELS.md)
- [`CV_AXLES_WHEEL_BEARINGS.md`](CV_AXLES_WHEEL_BEARINGS.md)
- [`ENGINE_TRANSAXLE_MOUNTS_VIBRATION.md`](ENGINE_TRANSAXLE_MOUNTS_VIBRATION.md)
- [`DIFFERENTIAL_FINAL_DRIVE_AXLE_SEALS.md`](DIFFERENTIAL_FINAL_DRIVE_AXLE_SEALS.md)
- [`../brakes/BRAKE_SYSTEM.md`](../brakes/BRAKE_SYSTEM.md)
- [`../suspension-steering/STEERING_SUSPENSION.md`](../suspension-steering/STEERING_SUSPENSION.md)
- [`../diagnostics/MISFIRE.md`](../diagnostics/MISFIRE.md)
- [`../engine/ACCESSORY_DRIVE_BELT.md`](../engine/ACCESSORY_DRIVE_BELT.md)
- [`../transmission/SIX_SPEED_AUTOMATIC.md`](../transmission/SIX_SPEED_AUTOMATIC.md)
- [`../maintenance/PRE_TRIP_INSPECTION.md`](../maintenance/PRE_TRIP_INSPECTION.md)

---

# Sources

## Exact 2014 owner data

- Hyundai 2014 Accent owner manual, tire balance / vibration guidance:
  https://www.carmanualsonline.info/amp/hyundai-accent-2014-owner-s-manual/2/?srch=weight

## Same-generation Hyundai service information

- 2013 Accent front brake disc inspection/runout:
  https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Brakes%20and%20Traction%20Control/Disc%20Brake%20System/Service%20and%20Repair/Front%20Disc%20Brake/Repair%20Procedures/

- 2013 Accent rear hub/bearing service:
  https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Steering%20and%20Suspension/Wheels%20and%20Tires/Wheel%20Hub/Service%20and%20Repair/Rear%20Hub%20-%20Carrier/Repair%20Procedures/

- 2013 Accent ABS diagnostic notes:
  https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Brakes%20and%20Traction%20Control/Antilock%20Brakes%20%2F%20Traction%20Control%20Systems/Testing%20and%20Inspection/

- 2013 Accent intermittent fault vibration/heat simulation guidance:
  https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Powertrain%20Management/Computers%20and%20Control%20Systems/Testing%20and%20Inspection/Initial%20Inspection%20and%20Diagnostic%20Overview/

- 2013 Accent engine/mount/roll-rod service information:
  https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Engine%2C%20Cooling%20and%20Exhaust/Engine/Service%20and%20Repair/Removal%20and%20Replacement/

## Tire safety / NVH support

- NHTSA TireWise:
  https://www.nhtsa.gov/vehicle-safety/tires

- Hyundai wheel/tire vibration service bulletin, broader Hyundai-family supporting NVH methodology:
  https://static.nhtsa.gov/odi/tsbs/2020/MC-10183960-0001.pdf

---

# Final Doctrine

```text
DO NOT DIAGNOSE THE SOUND.
DIAGNOSE THE CONDITIONS THAT CREATE THE SOUND.
```

Or, in full:

```text
WHEN DOES IT HAPPEN?
WHAT SPEED DOES IT FOLLOW?
WHAT INPUT CHANGES IT?
WHERE IS IT FELT?
WHAT WAS RECENTLY DISTURBED?

CLASSIFY → ROUTE → TEST → PROVE → REPAIR → REPEAT THE SAME TEST
```

A dramatic noise can come from a small shield. A subtle hum can come from a failing bearing. **Volume is not severity. Pattern plus evidence is diagnosis.**