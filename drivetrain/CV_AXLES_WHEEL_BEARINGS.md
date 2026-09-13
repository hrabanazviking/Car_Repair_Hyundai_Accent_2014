# CV Axles & Wheel Bearings — 2014 Hyundai Accent SE

> **Purpose:** diagnose front-drive axle, CV-joint, wheel-bearing, hub, ABS-tone-wheel, and related vibration/noise faults on the 2014 Hyundai Accent SE without confusing tires, brakes, suspension, engine mounts, or transmission symptoms for failed axle or hub parts.

## Source Confidence

- **EXACT 2014 OWNER DATA** — Hyundai 2014 Accent owner-manual inspection guidance.
- **EXACT 2014 PARTS-CATALOG DATA** — 2014 Accent OE catalog architecture and part families.
- **SERVICE-FAMILY — 2012/2013 ACCENT 1.6** — same-generation Accent workshop procedures used as supporting service data where exact 2014 workshop text is not publicly available.
- **GENERAL DIAGNOSTIC PRACTICE** — standard front-wheel-drive noise, vibration, and CV-joint diagnostic methods, clearly separated from Hyundai-specific specifications.

Primary source links are collected in [Sources](#sources).

---

# Core Rule

```text
CLICK / HUM / VIBRATION / PLAY
        ≠
FAILED CV AXLE OR BEARING PROVEN
```

Before replacing parts, classify the complaint by:

```text
VEHICLE SPEED
      ↓
STEERING ANGLE
      ↓
ACCELERATION / DECELERATION
      ↓
ROAD SURFACE
      ↓
BRAKING
      ↓
ENGINE RPM
      ↓
WHEEL / TIRE CONDITION
      ↓
BOOT / HUB / BEARING EVIDENCE
```

The same noise can be produced by:

- tires,
- wheel bearings,
- CV joints,
- bent wheels,
- brakes,
- engine/transaxle mounts,
- suspension joints,
- loose wheel hardware,
- damaged hub or knuckle,
- or drivetrain/transaxle faults.

---

# 1. Exact 2014 Accent Architecture

## Front drive system

**EXACT 2014 PARTS-CATALOG DATA**

The 2014 Accent is front-wheel drive and uses separate left and right front drive-shaft assemblies with wheel-side and differential-side CV joints.

For the 6-speed automatic configuration, the OE catalog lists examples including:

- LH drive-shaft assembly: `49500-1R100`,
- RH drive-shaft assembly: `49501-1R100`,
- LH wheel-side joint/shaft kit: `49526-1R101`,
- RH wheel-side joint/shaft kit: `49525-1R003`,
- LH differential-side joint kit: `49536-1R101`,
- RH differential-side joint kit: `49535-1R101`,
- LH differential-side boot kit: `49543-1R001`,
- RH differential-side boot kit: `49542-1R001`,
- ABS tone wheel: `49590-0X000`.

Production and VIN variation exist. **Verify by VIN before ordering parts.**

## Front hub and bearing

**EXACT 2014 PARTS-CATALOG DATA**

The front uses a separate hub and press-fit wheel bearing:

- front wheel bearing: `51720-1C000`,
- front hub assembly: `51750-1J000`.

This means front bearing service is a press operation, not simply four bolts and a complete hub cartridge.

## Rear hub and bearing

**EXACT 2014 PARTS-CATALOG DATA**

The rear uses a hub-and-bearing assembly:

- rear wheel hub assembly: `52750-0U000`.

The SE configuration has rear disc brakes, so use the disc-brake rear-hub service path.

---

# 2. Factory Maintenance Inspection

## Drive shafts and boots

**EXACT 2014 OWNER DATA**

Hyundai includes **drive shafts and boots** in the normal maintenance schedule at the 15,000-mile / 24,000-km service point and repeatedly thereafter at the applicable major service intervals.

The owner manual specifically says to inspect:

- drive shafts,
- CV boots,
- and boot clamps

for:

- cracks,
- deterioration,
- or damage.

Damaged parts should be replaced and grease repacked when necessary.

### Nomad interpretation

For a vehicle spending time on gravel, dusty roads, primitive campsites, potholes, snow, mud, or brush:

Inspect the boots more often than the formal schedule.

A quick visual check can catch a torn boot before dirt turns a cheap boot repair into an expensive CV-joint replacement.

---

# 3. CV Joint Symptom Patterns

## Outer CV joint pattern

A common outer-joint pattern is:

```text
CLICK / POP / RHYTHMIC SNAP
DURING TIGHT TURN
UNDER LIGHT TO MODERATE POWER
```

This is most suspicious when:

- the noise repeats with wheel rotation,
- it becomes more obvious at larger steering angles,
- and it is strongest while accelerating through the turn.

Do **not** treat this pattern as absolute proof.

Check:

- wheel nuts,
- brake hardware,
- ball joint,
- tie rod,
- strut mount,
- wheel bearing,
- tire interference,
- and CV boots.

## Inner CV joint pattern

A common inner-joint pattern is:

```text
SHUDDER / VIBRATION
MOST NOTICEABLE UNDER ACCELERATION
LESS NOTICEABLE WHEN COASTING
```

Possible causes also include:

- engine/transaxle mounts,
- tire or wheel defects,
- bent axle shaft,
- transaxle problems,
- suspension geometry,
- or severe wheel-bearing wear.

## Clicking straight ahead

Clicking while driving straight is less specific.

Investigate:

- wheel bearing,
- tire damage,
- loose wheel hardware,
- brake shield/contact,
- damaged tone wheel,
- axle spline/hub fit,
- and suspension joints.

---

# 4. CV Boot Inspection

Inspect both inner and outer boots for:

- radial cracks,
- splits between bellows,
- punctures,
- hardened rubber,
- loose or missing clamps,
- grease sling on the strut, knuckle, wheel, control arm, or underbody,
- and evidence of dirt or water entry.

## Grease sling is evidence

```text
GREASE ON SURROUNDING PARTS
        ↓
FIND THE SOURCE
        ↓
DO NOT JUST WIPE IT OFF
```

A boot can split only when flexed, so rotate and articulate the joint during inspection where safe and properly supported.

## Boot torn but joint quiet

If caught early, a boot/joint service may still be possible if:

- contamination has not damaged the joint,
- there is no clicking or excessive play,
- and service inspection shows the joint remains usable.

## Boot torn and joint noisy

A noisy joint with known contamination is much stronger evidence that the joint itself has been damaged.

Replacing only the boot at that stage may preserve a worn joint rather than fix the fault.

---

# 5. Exact 2014 ABS Tone-Wheel Relevance

**EXACT 2014 PARTS-CATALOG DATA**

The front-drive-shaft catalog includes ABS tone-wheel hardware.

Therefore a front axle/hub complaint may overlap with:

- ABS warning lamps,
- ESC/TCS faults,
- implausible wheel-speed data,
- or intermittent wheel-speed dropout.

Do not automatically replace a wheel-speed sensor because its signal is erratic.

Check:

- tone wheel condition,
- axle seating,
- wheel-bearing play,
- sensor gap/position where applicable,
- sensor wiring,
- rust/debris,
- connector condition,
- and live wheel-speed data.

Crosslink: [`../electrical/CAN_NETWORK_DIAGNOSTICS.md`](../electrical/CAN_NETWORK_DIAGNOSTICS.md)

---

# 6. Wheel-Bearing Symptom Patterns

## Common bearing-noise pattern

Wheel-bearing noise often presents as:

- hum,
- growl,
- rumble,
- drone,
- or rough rotational noise

that increases primarily with **vehicle speed** rather than engine RPM.

## Steering-load clue

A bearing may become louder or quieter as lateral load changes during a gentle sweeping turn.

Use this only as a clue.

Cabin acoustics can make the apparent side misleading.

Always confirm with physical inspection, comparison, and other evidence.

## Bearing play

Possible bearing play may be detected by checking wheel movement with the vehicle safely supported.

But:

```text
NO MEASURABLE PLAY
        ≠
BEARING DEFINITELY GOOD
```

A bearing can become noisy before obvious looseness develops.

Likewise, wheel movement can come from:

- ball joints,
- tie rods,
- suspension bushings,
- or hub/knuckle damage.

Watch the individual joints while the wheel is loaded by hand.

---

# 7. Tire Noise vs Wheel-Bearing Noise

Tire noise is one of the most common bearing mimics.

Suspect tires when:

- the sound changes dramatically with pavement texture,
- tread is cupped or feathered,
- a tire has shifted belts or irregular wear,
- the noise follows a tire after rotation,
- or pressure/wear is abnormal.

Suspect a bearing more strongly when:

- the sound is consistently tied to vehicle speed,
- road-surface changes have less effect,
- gentle lateral loading changes the sound,
- or physical hub/bearing evidence is present.

Crosslink: [`../tires-wheels/TIRES_WHEELS.md`](../tires-wheels/TIRES_WHEELS.md)

---

# 8. Brake Noise vs Bearing Noise

Check for:

- bent dust shield,
- stone trapped near rotor,
- pad wear indicator,
- caliper drag,
- rotor contact,
- overheated brake,
- and parking-brake drag at the rear.

A dragging brake can also heat the hub and imitate bearing distress.

Compare wheel/hub temperatures carefully after driving, without touching potentially hot brake components.

Crosslink: [`../brakes/BRAKE_SYSTEM.md`](../brakes/BRAKE_SYSTEM.md)

---

# 9. Front Hub/Bearing Service — Service-Family Data

**SERVICE-FAMILY — 2012/2013 ACCENT 1.6**

Hyundai service information shows that the front bearing is pressed into the knuckle and the hub is pressed into the bearing.

Important service rules include:

- replace the wheel bearing with a new bearing,
- use correct support adapters,
- do not load the wrong bearing race during pressing,
- inspect the hub for cracks and spline wear,
- inspect the knuckle for cracks,
- inspect the bearing for damage.

Incorrect pressing can damage a new bearing before the car ever returns to the road.

## Front driveshaft lock nut

**SERVICE-FAMILY — 2013 ACCENT**

```text
196.1–274.5 N·m
144.6–202.5 lb-ft
```

Hyundai service information also states:

- use a **new** driveshaft lock nut after removal,
- then stake the installed nut.

This is already preserved in [`../specs/TORQUE_SPECS.md`](../specs/TORQUE_SPECS.md).

Do not reuse an old staked lock nut merely because it threads back on.

---

# 10. Rear Hub/Bearing Service — Service-Family Data

**SERVICE-FAMILY — 2013 ACCENT, DISC TYPE**

The rear disc-brake service procedure removes the complete rear hub from the torsion-beam axle after the brake components are moved aside.

Supporting service-family hub-mounting-bolt torque:

```text
49.0–58.8 N·m
36.1–43.3 lb-ft
```

Treat this as **service-family supporting data**, not exact-VIN authority unless exact 2014 workshop information confirms it.

---

# 11. Axle Removal and Transaxle-Seal Risk

Removing a front axle is not merely a wheel-end operation.

The differential-side shaft enters the transaxle and its removal can affect:

- oil seals,
- retaining hardware,
- fluid containment,
- and contamination control.

Same-generation Hyundai automatic-transaxle service information specifically warns that a damaged transaxle-side oil seal can cause fluid leakage and must be replaced.

After axle service, inspect carefully for:

- ATF leakage,
- incomplete axle seating,
- damaged seals,
- abnormal spline engagement,
- and new drivetrain noise.

Crosslink: [`../transmission/SIX_SPEED_AUTOMATIC.md`](../transmission/SIX_SPEED_AUTOMATIC.md)

---

# 12. Noise and Vibration Decision Tree

```text
NOISE / VIBRATION
      ↓
TIED TO ENGINE RPM?
  ├─ YES → engine / mounts / accessories / transaxle
  └─ NO
       ↓
TIED TO VEHICLE SPEED?
  ├─ NO → investigate non-rotational causes
  └─ YES
       ↓
CHANGES WITH ROAD SURFACE?
  ├─ YES → tires become strong suspect
  └─ NO
       ↓
CHANGES WITH STEERING LOAD?
  ├─ YES → wheel bearing / CV / tire / suspension
  └─ NO
       ↓
CHANGES WITH ACCELERATION?
  ├─ YES → inner CV / mounts / drivetrain
  └─ NO
       ↓
CLICKS ON TIGHT TURN?
  ├─ YES → outer CV becomes strong suspect
  └─ NO
       ↓
INSPECT HUB / BEARING / BRAKES / TIRES / SUSPENSION
```

---

# 13. Rough-Road / Nomad Inspection

After rough gravel, deep potholes, mud, snow, ruts, or brush exposure, inspect:

- all four CV boots,
- boot clamps,
- grease sling,
- axle shafts,
- wheel rims,
- tire sidewalls,
- front hubs/knuckles,
- wheel-speed sensor wiring,
- brake hoses,
- underbody contact points,
- and any new wheel-speed-related warning lamps.

## Especially after a hard impact

If a wheel strikes a pothole or rock hard enough to produce a new noise, do not assume the bearing absorbed the entire event.

Also inspect:

- tire belt/sidewall,
- wheel runout,
- strut,
- control arm,
- ball joint,
- tie rod,
- knuckle,
- and alignment.

Crosslink: [`../suspension-steering/STEERING_SUSPENSION.md`](../suspension-steering/STEERING_SUSPENSION.md)

---

# 14. Stop-Driving Conditions

Treat the situation as **RED / DO NOT CONTINUE NORMAL DRIVING** when any of the following is present:

- wheel visibly wobbling,
- major hub/bearing looseness,
- grinding accompanied by looseness or overheating,
- loose or visibly backed-off driveshaft lock nut,
- CV joint showing severe mechanical play with clunking or binding,
- axle visibly damaged or partly disengaged,
- active ATF leakage after axle disturbance,
- wheel-speed fault combined with another brake-system safety concern,
- damaged steering/suspension parts discovered during inspection,
- or any condition suggesting the wheel/hub assembly may not remain mechanically retained.

Use a flatbed when wheel, hub, bearing, axle, steering, or suspension integrity is uncertain.

Crosslink: [`../roadside/RECOVERY_TOWING_JACKING.md`](../roadside/RECOVERY_TOWING_JACKING.md)

---

# 15. Field Safety

Never diagnose wheel bearings or CV joints by crawling under a vehicle supported only by the factory jack.

For inspection:

- park on firm, level ground,
- secure the vehicle,
- use rated lifting equipment,
- use verified support points,
- support with rated jack stands before working underneath,
- keep hands clear of rotating components,
- and do not run the vehicle in gear while unsupported or while someone is beneath it.

See:

- [`../roadside/RECOVERY_TOWING_JACKING.md`](../roadside/RECOVERY_TOWING_JACKING.md)
- [`../tools/NOMAD_AUTOMOTIVE_TOOLKIT.md`](../tools/NOMAD_AUTOMOTIVE_TOOLKIT.md)

---

# 16. AI / Runa Diagnostic Rules

When given a CV axle or wheel-bearing complaint, the AI should record:

```yaml
complaint:
  noise_type: click | hum | growl | clunk | vibration | grind | unknown
  location_reported: LF | RF | LR | RR | center | unknown
  vehicle_speed_related: true | false | unknown
  engine_rpm_related: true | false | unknown
  acceleration_related: true | false | unknown
  steering_angle_related: true | false | unknown
  road_surface_related: true | false | unknown
  braking_related: true | false | unknown

inspection:
  outer_cv_boot: good | cracked | torn | leaking | unknown
  inner_cv_boot: good | cracked | torn | leaking | unknown
  grease_sling: true | false | unknown
  axle_damage_visible: true | false | unknown
  wheel_play: none | slight | major | unknown
  bearing_roughness: true | false | unknown
  wheel_temperature_abnormal: true | false | unknown
  tire_damage_or_cupping: true | false | unknown
  wheel_damage: true | false | unknown
  abs_esc_warning: true | false | unknown
  transaxle_fluid_leak: true | false | unknown

assessment:
  likely_system: cv_outer | cv_inner | bearing_hub | tire_wheel | brake | suspension | mount | transmission | unknown
  driveability: green | caution | red
  confidence: low | medium | high
```

AI rules:

1. Do not diagnose a CV joint from clicking alone.
2. Do not diagnose a wheel bearing from humming alone.
3. Check tires before condemning bearings.
4. Check boots before replacing complete axles.
5. Treat grease sling as evidence of a leak source that must be found.
6. Treat ABS wheel-speed faults as possible sensor, tone-wheel, bearing, wiring, or hub problems.
7. Preserve service-family torque values as supporting data unless exact 2014 documentation confirms them.
8. Never recommend reusing a removed staked front driveshaft lock nut when Hyundai service information specifies a new one.
9. Never recommend driving on major hub play, wheel wobble, severe grinding, or an axle that may be disengaging.
10. Unknown is preferable to a confident wrong answer.

---

# 17. Core Diagnostic Doctrine

```text
NOISE / VIBRATION
      ↓
CLASSIFY WHEN IT HAPPENS
      ↓
INSPECT TIRE / WHEEL
      ↓
INSPECT CV BOOTS / SHAFTS
      ↓
INSPECT HUB / BEARING
      ↓
CHECK BRAKES / SUSPENSION
      ↓
CHECK ABS TONE / SENSOR DATA
      ↓
ISOLATE THE ROTATING COMPONENT
      ↓
REPAIR ROOT CAUSE
      ↓
VERIFY QUIET / SMOOTH / SECURE
```

> **The loudest part is not always the failed part. Let speed, load, steering angle, and physical evidence triangulate the source.**

---

# Crosslinks

- [`../tires-wheels/TIRES_WHEELS.md`](../tires-wheels/TIRES_WHEELS.md)
- [`../suspension-steering/STEERING_SUSPENSION.md`](../suspension-steering/STEERING_SUSPENSION.md)
- [`../brakes/BRAKE_SYSTEM.md`](../brakes/BRAKE_SYSTEM.md)
- [`../transmission/SIX_SPEED_AUTOMATIC.md`](../transmission/SIX_SPEED_AUTOMATIC.md)
- [`../electrical/CAN_NETWORK_DIAGNOSTICS.md`](../electrical/CAN_NETWORK_DIAGNOSTICS.md)
- [`../roadside/RECOVERY_TOWING_JACKING.md`](../roadside/RECOVERY_TOWING_JACKING.md)
- [`../maintenance/PRE_TRIP_INSPECTION.md`](../maintenance/PRE_TRIP_INSPECTION.md)
- [`../specs/TORQUE_SPECS.md`](../specs/TORQUE_SPECS.md)

---

# Sources

## Exact 2014 owner information

- Hyundai Accent 2014 owner manual, maintenance schedule and drive-shaft/boot inspection:  
  https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/?srch=boot

- Hyundai Accent 2014 owner manual, full manual:  
  https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/hyundai-accent-2014-owner-s-manual

## Exact 2014 parts architecture

- 2014 Accent front drive-shaft catalog:  
  https://www.hyundaipartsdeal.com/parts-list/2014-hyundai-accent/transmission/drive_shaft_front.html

- 2014 Accent front-axle catalog:  
  https://www.hyundaipartsdeal.com/parts-list/2014-hyundai-accent/chassis/front_axle.html

- 2014 Accent wheel-bearing catalog:  
  https://www.hyundaipartsdeal.com/oem-2014-hyundai-accent-wheel_bearing.html

- 2014 Accent rear-axle catalog:  
  https://www.hyundaipartsdeal.com/parts-list/2014-hyundai-accent/chassis/rear_axle.html

## Same-generation Accent service-family information

- 2013 Accent front driveshaft nut specification:  
  https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Steering%20and%20Suspension/Suspension/Wheel%20Hub/Axle%20Nut/Specifications/Front/

- 2012 Accent front hub/knuckle bearing replacement procedure:  
  https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Maintenance/Wheels%20and%20Tires/Wheel%20Hub/Service%20and%20Repair/Front%20Hub%20%2F%20Knuckle/Repair%20Procedures/

- 2013 Accent rear hub service procedure:  
  https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Steering%20and%20Suspension/Wheels%20and%20Tires/Wheel%20Hub/Service%20and%20Repair/Rear%20Hub%20-%20Carrier/Repair%20Procedures/

- 2013 Accent automatic-transaxle service procedure, axle removal context and oil-seal warning:  
  https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Transmission%20and%20Drivetrain/Automatic%20Transmission%2FTransaxle/Service%20and%20Repair/Removal%20and%20Replacement/Automatic%20Transaxle%20Repair%20Procedures/
