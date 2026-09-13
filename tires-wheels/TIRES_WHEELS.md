# 2014 Hyundai Accent SE — Tires, Wheels, TPMS & Field Tire Safety

> **Purpose:** A practical, offline-first tire and wheel reference for a U.S.-market 2014 Hyundai Accent SE five-door. Designed for human use and AI/RAG retrieval.
>
> **Core rule:** A tire is a structural safety component. Pressure, tread, sidewall condition, wheel condition, load, age, and repair quality all matter. A tire that merely "holds air" is not automatically safe.

---

## 1. Vehicle Scope

Primary vehicle:

- 2014 Hyundai Accent SE five-door
- Front-wheel drive
- Factory SE wheel/tire package: **16-inch alloy wheels with P195/50R16 tires**
- Factory cold inflation pressure: **33 psi / 230 kPa front and rear**
- Compact spare, if equipped: **T125/80D15 at 60 psi / 420 kPa**
- Factory wheel lug-nut torque: **65–79 lb-ft / 88–107 N·m**
- Tire Pressure Monitoring System (TPMS)

Hyundai's official 2014 product information identifies the five-door SE with 16-inch alloy wheels and 195/50R16 tires.

Source:

- Hyundai Newsroom, 2014 Accent: https://www.hyundainews.com/releases/1756

The exact 2014 owner's manual tire-and-wheel specification table lists:

- P195/50R16 on 6.0Jx16 wheels
- 33 psi front and rear, normal or maximum load
- T125/80D15 compact spare on 3.5Jx15
- 60 psi compact-spare pressure
- 65–79 lb-ft / 88–107 N·m wheel-lug torque

Source:

- 2014 Accent owner's manual, tire/wheel specifications: https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/2/?srch=weight

---

# 2. Confidence Tags

Use these tags when storing tire information:

- `VERIFIED — 2014 HYUNDAI OWNER MANUAL`
- `VERIFIED — HYUNDAI OFFICIAL PRODUCT DATA`
- `VERIFIED — NHTSA`
- `VERIFIED — USTMA`
- `GENERAL TIRE PRACTICE`
- `OWNER OBSERVATION`
- `PROVISIONAL`
- `UNKNOWN`

Do not silently upgrade general tire-industry guidance into a Hyundai factory specification.

---

# 3. Canonical Factory Tire and Wheel Data

| Item | Specification | Confidence |
|---|---:|---|
| SE full-size tire | P195/50R16 | VERIFIED — HYUNDAI |
| Wheel | 6.0Jx16 alloy | VERIFIED — 2014 OWNER MANUAL |
| Cold pressure, front | 33 psi / 230 kPa | VERIFIED — 2014 OWNER MANUAL |
| Cold pressure, rear | 33 psi / 230 kPa | VERIFIED — 2014 OWNER MANUAL |
| Compact spare | T125/80D15 | VERIFIED — 2014 OWNER MANUAL |
| Compact spare pressure | 60 psi / 420 kPa | VERIFIED — 2014 OWNER MANUAL |
| Lug-nut torque | 65–79 lb-ft / 88–107 N·m | VERIFIED — 2014 OWNER MANUAL |
| Rotation interval | 7,500 mi / 12,000 km | VERIFIED — 2014 OWNER MANUAL |
| Tread replacement threshold | 2/32 in / 1.6 mm | VERIFIED — HYUNDAI + NHTSA |

### Important

The **driver-door tire and loading label on the actual car outranks a generic internet chart** if the vehicle configuration differs.

---

# 4. What "Cold Tire Pressure" Means

Hyundai defines a cold tire as one that:

- has been parked for at least about **3 hours**, or
- has been driven less than about **1 mile / 1.6 km**.

Check pressure when cold.

Warm tires normally rise several psi. Do **not** bleed a warm tire down to the cold specification, or it may become underinflated after cooling.

Source:

- 2014 Accent owner's manual tire-care section: https://www.manualslib.com/manual/1067849/Hyundai-2014-Accent.html

---

# 5. Nomad Rule: Pressure Is a Daily-Travel Variable

For ordinary paved-road travel, use the Hyundai placard pressure as the baseline:

```text
33 psi cold front
33 psi cold rear
```

For long-distance travel, remote-road use, large temperature swings, or heavy cargo:

1. Check cold pressure before departure.
2. Inspect all four tires visually.
3. Check the spare.
4. Record any tire that repeatedly loses pressure.
5. Recheck after a large ambient-temperature change.

## Do not assume lower pressure is automatically better on gravel

The SE uses a relatively low-profile **195/50R16** tire.

Lower pressure can increase sidewall flex and wheel-impact exposure. On a low-clearance, low-profile passenger car, aggressive "airing down" can create more risk than benefit.

Repository rule:

> **For normal travel, retain placard pressure unless the tire manufacturer or a qualified tire professional gives a different vehicle-specific recommendation.**

If pressure is temporarily reduced for a very low-speed traction situation, reinflate before returning to normal road speed.

---

# 6. TPMS Is a Warning System, Not a Tire Gauge

The 2014 Accent is equipped with TPMS.

Hyundai instructs the owner to check tire pressure **monthly when cold**, even though TPMS is present.

TPMS warns when one or more tires are significantly underinflated, but it is not intended to replace routine gauge checks.

Source:

- 2014 Accent TPMS section: https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/?srch=tire+replacement

## If the low-pressure light comes on

1. Reduce speed.
2. Avoid hard cornering.
3. Expect increased stopping distance.
4. Stop safely.
5. Check all tires with a gauge.
6. Inflate to the placard pressure if the tire can safely hold air.
7. Inspect for a puncture or damage.

Significant underinflation causes heat buildup and can lead to tire failure.

## TPMS malfunction indicator

A TPMS malfunction is not the same thing as a low-pressure warning.

If the system indicates a malfunction:

- manually check pressures,
- inspect for recent wheel/tire work,
- consider sensor or communication faults,
- do not assume tire pressure is normal merely because the system cannot report it.

---

# 7. Tire Rotation

Hyundai calls for tire rotation every:

```text
7,500 miles / 12,000 km
```

or sooner if irregular wear appears.

Source:

- 2014 Accent maintenance schedule: https://manualsfile.com/product/rh5bdc40j.html
- 2014 Accent owner's manual: https://www.manualslib.com/manual/1067849/Hyundai-2014-Accent.html

During rotation:

- inspect tread depth,
- inspect sidewalls,
- check for bulges,
- check for exposed cord,
- check wheel damage,
- check balance symptoms,
- check brake-pad condition,
- set all pressures correctly,
- torque lug nuts correctly.

## Directional or asymmetric tires

Follow the tire sidewall markings.

- `OUTSIDE` must face outward on asymmetric tires.
- Directional tires must rotate in the marked direction.
- Do not blindly apply a cross-rotation pattern if the tire design does not allow it.

Do **not** include the compact spare in the rotation pattern.

---

# 8. Lug Nuts and Wheel Installation

Factory wheel-lug torque:

```text
65–79 lb-ft
88–107 N·m
```

Source:

- 2014 Accent owner's manual: https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/?srch=wheel+torque

## Installation procedure

1. Make sure the wheel and hub mating surfaces are reasonably clean.
2. Install the wheel squarely on the hub/studs.
3. Start every lug nut by hand.
4. Tighten in a star/cross pattern.
5. Lower the vehicle enough that the wheel cannot rotate freely.
6. Final-torque with a torque wrench.
7. Recheck after wheel service if appropriate.

### Never

- use damaged lug nuts,
- force a cross-threaded lug nut,
- substitute unknown thread hardware,
- apply final torque with an impact gun alone,
- lubricate threads unless a specific service procedure explicitly calls for it.

Torque specifications normally assume the thread condition expected by the manufacturer.

---

# 9. Tread Depth

Hyundai states that the tread-wear indicators appear when approximately **1/16 inch / 1.6 mm / 2/32 inch** of tread remains.

Replace the tire when the tread reaches the wear bars.

Source:

- 2014 Accent owner's manual tire replacement section: https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/?srch=traction+control

NHTSA likewise says tires are not safe and should be replaced at **2/32 inch** remaining tread.

Source:

- NHTSA TireWise: https://www.nhtsa.gov/vehicle-safety/tires

## Remote-travel reality

2/32 inch is a minimum replacement threshold, not a claim that wet-road or snow performance remains excellent until that exact point.

For nomad travel, consider tread condition before entering:

- sustained heavy rain,
- deep standing water,
- snow,
- mud,
- loose gravel,
- long remote roads.

---

# 10. Tire Age and DOT Date Code

Tires age even when tread remains.

The DOT Tire Identification Number includes a four-digit manufacture date code:

```text
WWYY
```

Example:

```text
0324
=
3rd week of 2024
```

NHTSA notes that some vehicle and tire manufacturers recommend replacement at approximately **6–10 years**, regardless of tread depth.

There is no single universal federal expiration age for every tire.

Source:

- NHTSA TireWise: https://www.nhtsa.gov/vehicle-safety/tires

## Nomad inspection rule

At least annually, record:

- DOT date code,
- tread depth,
- sidewall cracking,
- weather checking,
- bulges,
- bead condition,
- recurring pressure loss,
- vibration/noise changes.

Also inspect the compact spare. A spare can age silently for many years.

---

# 11. Damage That Means STOP / DO NOT DRIVE

Do not continue normal driving with:

- visible cord or fabric,
- sidewall bulge,
- tread bulge,
- obvious tread separation,
- large sidewall cut,
- exposed structural material,
- wheel visibly loose,
- severe wheel bend causing air loss,
- cracked wheel,
- tire rubbing hard against body/suspension,
- rapid pressure loss,
- tire partly unseated from rim,
- severe vibration after an impact,
- structural damage after running flat.

A tire that has been driven significantly while nearly flat can have hidden internal damage even after it is reinflated.

---

# 12. Puncture Repair: What Is Actually Repairable?

The U.S. Tire Manufacturers Association (USTMA) recommends considering permanent repair only when:

- the damage is in the **repairable tread area**,
- the puncture is **no larger than 1/4 inch / 6 mm**,
- the tire is removed from the wheel for internal inspection,
- the injury is filled with a rubber stem/plug,
- the inner liner is sealed with a patch.

USTMA states that **a plug alone is not an acceptable permanent repair**.

Repairs should not be made in the shoulder/belt-edge or sidewall area.

Sources:

- USTMA Tire Repair Basics: https://www.ustires.org/tire-care-safety/tire-repair-basics
- USTMA Passenger Tire Puncture Repair: https://www.ustires.org/resources/puncture-repair-procedures-passenger-and-light-truck-tires-0

---

# 13. External Rope Plug: Field Use Classification

A roadside external rope/string plug can sometimes restore temporary mobility after a small tread puncture.

However:

```text
EXTERNAL ROPE PLUG
      ≠
USTMA-COMPLIANT PERMANENT REPAIR
```

Repository classification:

### `TEMPORARY MOBILITY ONLY`

Use only when all of the following are true:

- puncture is in the central tread area,
- no sidewall/shoulder damage,
- no bulge,
- no exposed cord,
- tire was not destroyed by prolonged run-flat operation,
- puncture is small,
- repair holds pressure,
- speed and distance are kept conservative until professional inspection.

Then have the tire removed and inspected properly.

### Never field-plug

- sidewall,
- shoulder,
- large tear,
- bulge,
- exposed cord,
- bead damage,
- multiple close-together injuries,
- obvious run-flat structural damage.

---

# 14. Tire Mobility Kit

Some 2014 Accents may use a Tire Mobility Kit instead of a compact spare.

Hyundai's exact 2014 manual describes the kit as temporary emergency mobility equipment for suitable small tread punctures.

The manual references punctures up to approximately **0.24 in / 6 mm** and warns that the vehicle should not be driven if the repaired tire cannot maintain adequate pressure.

Source:

- 2014 Accent owner's manual emergency tire section: https://www.manualslib.com/manual/1067849/Hyundai-2014-Accent.html

Sealant is not a substitute for later tire inspection.

Sealant can also affect TPMS hardware, so inform the tire technician when sealant has been used.

---

# 15. Compact Spare

Factory compact spare, if equipped:

```text
T125/80D15
60 psi cold
```

Hyundai classifies the compact spare as **temporary emergency equipment**.

The repository's existing roadside guide records the Hyundai limit of approximately **50 mph maximum** for compact-spare use.

Related file:

- `../roadside/EMERGENCY_FIELD_REPAIRS.md`

## Compact-spare rules

- Check it whenever the regular tires are checked.
- Maintain 60 psi cold.
- Do not use it in the regular tire rotation.
- Replace it when its wear bars are reached.
- Do not treat it as a normal long-distance tire.
- Repair/replace the full-size tire as soon as practical.

---

# 16. Sidewall Damage

The sidewall flexes continuously and carries structural load.

### Replace / remove from service if there is:

- a bulge or bubble,
- exposed cords,
- deep cut into structural layers,
- severe curb-impact damage,
- obvious bead damage,
- separation.

A superficial cosmetic scuff is not automatically structural damage, but if the depth is uncertain, professional inspection is appropriate.

### No sidewall plug

Industry puncture-repair guidance does not treat the sidewall as a repairable puncture zone.

---

# 17. Wheel Damage

The 2014 SE uses alloy wheels.

After a pothole, rock strike, curb strike, or deep rut, inspect for:

- bent rim lip,
- crack,
- air leakage at bead,
- steering vibration,
- new wheel wobble,
- sudden alignment change,
- tire sidewall injury,
- damaged valve stem / TPMS sensor area.

## No-go wheel conditions

- visible crack,
- severe bend,
- wheel cannot hold tire pressure,
- lug seat damaged,
- stud/lug cannot retain wheel correctly,
- wheel visibly oscillates/wobbles.

---

# 18. Uneven Wear Diagnostic Map

Uneven wear is evidence.

Do not merely replace the tire without asking why it wore that way.

## Center wear

Possible causes:

- chronic overinflation,
- tire/load/application effects.

## Both shoulders worn

Possible causes:

- chronic underinflation,
- overload,
- heat buildup.

## One shoulder worn

Possible causes:

- alignment error,
- bent component,
- worn steering/suspension component.

## Feathering

Possible causes:

- toe error,
- looseness in steering/suspension,
- alignment problem.

## Cupping / scalloping

Possible causes:

- imbalance,
- weak/damaged strut or shock,
- loose suspension,
- wheel/tire runout.

## One isolated damaged area

Possible causes:

- impact,
- locked-wheel event,
- internal tire defect,
- severe braking event.

Related file:

- `../suspension-steering/STEERING_SUSPENSION.md`

---

# 19. Vibration Diagnostic Map

## Vibration mainly at certain road speeds

Investigate:

- wheel balance,
- tire radial-force variation,
- bent wheel,
- tire runout,
- tread separation.

## Vibration mostly during braking

Investigate:

- brake rotor variation,
- brake hardware,
- wheel/hub condition.

## Vibration mainly during acceleration

Investigate:

- inner CV joint,
- drivetrain,
- engine/transmission mount,
- wheel/tire only if evidence supports it.

## Steering-wheel shake

Often points toward front wheel/tire/suspension involvement, but do not assume.

## Seat/floor vibration

Often feels stronger from rear wheel/tire issues, but verify with rotation or measured testing rather than guessing.

---

# 20. Pulling and Drift

A vehicle that pulls can have:

- unequal tire pressure,
- mismatched tire construction,
- tire conicity/radial pull,
- alignment error,
- brake drag,
- suspension damage,
- road crown effects.

Before ordering an alignment:

1. Verify all tire pressures.
2. Inspect tread and damage.
3. Confirm wheel/tire sizes match.
4. Check for brake drag.
5. Check steering/suspension play.
6. Then use alignment measurements.

---

# 21. Hydroplaning and Wet Roads

Hydroplaning risk rises with:

- speed,
- standing-water depth,
- worn tread,
- improper pressure,
- heavy rain.

Field rule:

> **If water depth is unknown, slow down before entering it. Do not use speed to "push through."**

Worn tires lose wet-road margin before they necessarily look bald.

---

# 22. Snow, Ice and Cold Weather

Cold weather reduces tire pressure.

A tire adjusted correctly in warm weather may become underinflated after a major temperature drop.

Before winter travel:

- check cold pressure,
- inspect tread,
- inspect tire age,
- verify spare pressure,
- verify inflator operation,
- verify traction-board condition.

Do not confuse TPMS activation caused by a temperature-related pressure drop with an automatic TPMS hardware failure.

---

# 23. Gravel, Primitive Roads and the Accent

This vehicle is a low-clearance front-wheel-drive passenger car.

The tires and wheels are especially vulnerable to:

- sharp rocks,
- pothole edges,
- washouts,
- hidden ruts,
- cattle guards,
- exposed roots,
- washboard impacts.

## Primitive-road tire rules

- Reduce speed before rough sections.
- Avoid sharp-edged impacts.
- Do not straddle rocks that threaten the oil pan or exhaust.
- Avoid spinning tires against sharp rocks.
- After a hard impact, stop and inspect.
- Recheck pressure after rough-road travel.
- Look for fresh sidewall cuts and rim damage.

### Very important

Traction boards can create traction.

They do **not** create:

- ground clearance,
- stronger sidewalls,
- stronger wheels,
- suspension travel.

Related file:

- `../maintenance/PRE_TRIP_INSPECTION.md`

---

# 24. Tire Load and Nomad Cargo

Tires carry the vehicle and everything placed inside it.

Do not exceed:

- the vehicle's certified load limits,
- axle limits,
- tire load ratings.

Use the vehicle's actual certification and tire/loading labels.

Do not estimate payload from memory.

For nomad configuration changes:

- removing seats reduces some vehicle weight,
- adding batteries, water, tools, camping gear, food, electronics, recovery gear, and storage adds weight,
- weight distribution matters as much as total weight.

A tire that is correctly inflated for the car should still not be asked to carry more than its rated load.

---

# 25. Replacement Tire Rules

Hyundai cautions that replacement tires should match the required vehicle specification.

For the SE, the factory size is:

```text
P195/50R16
```

When replacing tires, verify:

- size,
- load index,
- speed rating,
- construction,
- wheel compatibility,
- TPMS compatibility,
- directionality/asymmetry,
- seasonal use.

## Do not casually change overall diameter

Changing tire diameter can affect:

- speedometer/odometer accuracy,
- ABS/ESC behavior,
- ground clearance,
- gearing,
- fender clearance,
- steering geometry,
- snow-chain clearance.

---

# 26. Mixing Tires

For predictable handling, keep tire construction and performance characteristics as consistent as practical.

Avoid mixing:

- radial and bias construction,
- dramatically different tread types,
- incompatible sizes,
- grossly different wear levels.

When only two tires are replaced, follow the tire manufacturer's placement guidance. Many tire manufacturers recommend installing the pair with deeper/newer tread on the rear axle to preserve rear wet-road stability, even on front-wheel-drive vehicles.

Treat this as tire-industry guidance, not a Hyundai-specific 2014 specification.

---

# 27. Valve Stems and Slow Leaks

A slow leak may come from:

- tread puncture,
- valve core,
- valve stem,
- TPMS valve hardware,
- bead leak,
- wheel corrosion,
- bent/cracked rim.

Do not assume the tire carcass is the leak source.

A valve cap is not the primary pressure seal, but it helps keep dirt and moisture away from the valve core.

If a tire repeatedly needs air, find the leak.

---

# 28. Nomad Tire Kit

Recommended mobile tire equipment:

- accurate digital or dial tire gauge,
- 12 V inflator,
- compact spare or confirmed Tire Mobility Kit,
- wheel chock,
- 21 mm lug wrench / socket as applicable,
- torque wrench when practical,
- factory jack,
- additional stable support equipment when appropriate,
- tread-depth gauge,
- valve-core tool,
- spare valve cores and caps,
- temporary tread-puncture plug kit,
- pliers for removing puncturing object,
- soap solution for locating leaks,
- flashlight/headlamp,
- gloves,
- reflective vest/triangles.

### Safety rule

Never crawl under the vehicle when supported only by the emergency jack.

---

# 29. Quick Roadside Flat-Tire Workflow

```text
TIRE WARNING / FLAT FEEL
        ↓
SLOW DOWN SMOOTHLY
        ↓
STOP SOMEWHERE SAFE
        ↓
INSPECT TIRE + WHEEL
        ↓
STRUCTURAL DAMAGE?
   ├─ YES → SPARE / RECOVERY
   └─ NO
        ↓
SMALL CENTRAL TREAD PUNCTURE?
   ├─ YES → temporary mobility repair may be possible
   └─ NO  → spare / recovery
        ↓
VERIFY PRESSURE HOLDS
        ↓
DRIVE CONSERVATIVELY
        ↓
PROFESSIONAL INSPECTION / PERMANENT REPAIR
```

---

# 30. Tire Condition Severity Classes

## GREEN — SERVICEABLE

- pressure stable,
- no visible structural damage,
- tread above replacement threshold,
- no bulges,
- no exposed cord,
- no abnormal vibration.

## YELLOW — INSPECT / SERVICE SOON

- slow leak,
- irregular tread wear,
- aging/weather cracking,
- mild vibration,
- recent pothole impact,
- repeated pressure loss,
- borderline tread for upcoming severe weather.

## ORANGE — TEMPORARY MOBILITY ONLY

- properly installed compact spare,
- temporary Tire Mobility Kit seal,
- temporary external tread plug,
- repaired tire awaiting professional internal inspection.

## RED — DO NOT DRIVE

- sidewall bulge,
- exposed cord,
- tread separation,
- cracked/severely bent wheel,
- rapid pressure loss,
- unseated bead,
- severe run-flat damage,
- wheel not securely retained,
- tire rubbing hard against suspension/body.

---

# 31. AI Diagnostic Rules

An AI using this repository should follow these rules:

1. Do not diagnose a tire from TPMS alone.
2. Ask for actual cold pressure.
3. Ask which corner is affected.
4. Ask whether the pressure loss is sudden or gradual.
5. Ask whether there was a pothole/curb/road impact.
6. Ask for tread and sidewall condition.
7. Distinguish tread puncture from shoulder/sidewall damage.
8. Do not recommend a permanent external plug repair.
9. Do not recommend repairing a sidewall puncture.
10. Do not recommend driving on a bulged tire.
11. Do not treat a compact spare as a normal travel tire.
12. Do not recommend lowering tire pressure for gravel as a generic solution.
13. Check steering/suspension and wheel damage when tire wear is irregular.
14. Do not call a wheel bearing bad merely because tire noise changes in a curve.
15. Use the vehicle placard and actual installed tire specifications before ordering parts.
16. Unknown is preferable to a confident wrong answer.

---

# 32. Tire/Wheel Incident Record

```yaml
tire_wheel_incident:
  date:
  odometer_miles:
  location:
  road_surface:
  ambient_temperature:

  corner:
    - LF
    - RF
    - LR
    - RR
    - spare

  tire:
    brand:
    model:
    size:
    load_index:
    speed_rating:
    dot_code:
    tread_depth_32nds:
    cold_pressure_psi:
    warm_pressure_psi:

  symptom:
    pressure_loss:
    vibration:
    pull:
    noise:
    visible_damage:
    tpms_warning:

  damage_location:
    - tread
    - shoulder
    - sidewall
    - bead
    - wheel
    - valve
    - unknown

  event_before_symptom:
    pothole:
    curb_strike:
    rock_strike:
    rough_road:
    prolonged_low_pressure:

  temporary_action:
    - reinflated
    - compact_spare
    - mobility_kit
    - external_tread_plug
    - tow
    - none

  final_repair:
  alignment_checked:
  balance_checked:
  wheel_inspected:
  notes:
```

---

# 33. Cross-References

Related repository documents:

- `../maintenance/PRE_TRIP_INSPECTION.md`
- `../maintenance/MAINTENANCE_SCHEDULE.md`
- `../maintenance/NOMAD_SERVICE_LOG.md`
- `../roadside/EMERGENCY_FIELD_REPAIRS.md`
- `../suspension-steering/STEERING_SUSPENSION.md`
- `../brakes/BRAKE_SYSTEM.md`
- `../specs/TORQUE_SPECS.md`

---

# 34. Core Field Doctrine

```text
PRESSURE
   ↓
TREAD
   ↓
SIDEWALL
   ↓
WHEEL
   ↓
LOAD
   ↓
AGE
   ↓
DAMAGE HISTORY
   ↓
REPAIR QUALITY
   ↓
SAFE TO DRIVE?
```

And for remote travel:

```text
SMALL TIRE PROBLEM NEAR SERVICES
              <
BIG TIRE PROBLEM 40 MILES DOWN A FOREST ROAD
```

Fix small tire problems while help, pavement, tools, and replacement tires are still easy to reach.

---

# 35. Sources

## Hyundai

- Hyundai Newsroom, 2014 Accent official product information: https://www.hyundainews.com/releases/1756
- 2014 Accent owner's manual, tire/wheel specifications: https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/2/?srch=weight
- 2014 Accent owner's manual, wheel torque: https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/?srch=wheel+torque
- 2014 Accent owner's manual, tire replacement/tread: https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/?srch=traction+control
- 2014 Accent owner's manual, TPMS: https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/?srch=tire+replacement
- 2014 Accent owner's manual, maintenance schedule: https://manualsfile.com/product/rh5bdc40j.html
- ManualsLib 2014 Accent owner's manual: https://www.manualslib.com/manual/1067849/Hyundai-2014-Accent.html

## Tire industry / safety

- NHTSA TireWise: https://www.nhtsa.gov/vehicle-safety/tires
- U.S. Tire Manufacturers Association, Tire Repair Basics: https://www.ustires.org/tire-care-safety/tire-repair-basics
- USTMA, Passenger and Light Truck Tire Puncture Repair: https://www.ustires.org/resources/puncture-repair-procedures-passenger-and-light-truck-tires-0

---

## Final Principle

> **A tire problem is not merely an inconvenience. It is a load-bearing, heat-generating, high-speed structural problem. Measure it, inspect it, classify it correctly, and do not gamble on sidewall or wheel damage.**
