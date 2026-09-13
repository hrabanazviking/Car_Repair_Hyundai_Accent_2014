# Alignment Geometry & Tire Wear — 2014 Hyundai Accent SE

> **Purpose:** diagnose pulling, drifting, steering-wheel misalignment, abnormal tire wear, post-pothole geometry changes, and alignment complaints without treating the alignment machine as a substitute for mechanical inspection.

## Source confidence

- **EXACT 2014 OWNER DATA** — 2014 Hyundai Accent owner manual.
- **SERVICE-FAMILY — 2013 ACCENT RB** — same-generation Accent service information and Hyundai alignment bulletin, used as supporting geometry data where exact 2014 workshop specifications were not located publicly.
- **GENERAL ALIGNMENT PRACTICE** — standard chassis-diagnostic principles, kept separate from Hyundai-specific numbers.

Primary sources are linked in [Sources](#sources).

---

# Core rule

```text
ALIGNMENT COMPLAINT
      ≠
ALIGNMENT ADJUSTMENT REQUIRED
```

Before changing geometry, prove that the chassis is mechanically sound.

```text
VERIFY TIRE PRESSURE
      ↓
VERIFY TIRE / WHEEL CONDITION
      ↓
CHECK WHEEL BEARINGS
      ↓
CHECK BALL JOINTS / TIE RODS / BUSHINGS
      ↓
CHECK STRUTS / SPRINGS / RIDE HEIGHT
      ↓
CHECK FOR BENT OR SHIFTED PARTS
      ↓
THEN MEASURE ALIGNMENT
      ↓
ADJUST ONLY WHAT IS DESIGNED TO ADJUST
      ↓
VERIFY STEERING-WHEEL CENTER + ROAD BEHAVIOR
```

A loose joint can move while the machine is measuring it. A bent part can produce an apparently “adjustable” problem that returns immediately. A damaged tire can pull even when the numbers are perfect.

---

# 1. Exact 2014 owner guidance

The 2014 Accent owner manual says:

- the vehicle was aligned and balanced at the factory,
- unusual tire wear or pulling can justify an alignment check,
- vibration on a smooth road can indicate a wheel-balance problem,
- irregular tire wear can be caused by incorrect pressure, improper alignment, out-of-balance wheels, severe braking, or severe cornering,
- correct wheel alignment helps reduce tire wear,
- tires should be rotated every **7,500 miles / 12,000 km**, or sooner if irregular wear develops,
- worn, unevenly worn, bulged, damaged, or cord-exposed tires should not be treated as an alignment-only problem.

Exact 2014 SE baseline already established elsewhere in this repository:

```text
Tire size: P195/50R16
Cold pressure: 33 psi front / rear
Wheel-lug torque: 88–107 N·m / 65–79 lb-ft
```

See:

- [`../tires-wheels/TIRES_WHEELS.md`](../tires-wheels/TIRES_WHEELS.md)
- [`../specs/TORQUE_SPECS.md`](../specs/TORQUE_SPECS.md)

---

# 2. Service-family alignment reference

## IMPORTANT

The following geometry values come from **2013 Accent RB** Hyundai service information and Hyundai's 2013 model-year alignment bulletin.

They are highly relevant same-generation references, but are **not labeled in this repository as exact 2014 VIN-specific workshop specifications**.

```text
FRONT
Camber:        -0.5° ± 0.5°
Caster:         4.1° ± 0.5°
Total toe:      0.15° ± 0.2°
Individual toe: 0.075° ± 0.1°

REAR
Camber:        -1.5° ± 0.5°
Total toe:      0.5° (+0.4° / -0.5°)
Individual toe: 0.25° (+0.2° / -0.25°)
```

Same-generation Hyundai service information states:

- **front toe is adjustable** at the tie rods,
- **front camber and caster are factory-set, not normal service adjustments**, and out-of-spec values call for damaged-part inspection/repair,
- **rear toe and rear camber are factory-set, not normal service adjustments**, and out-of-spec values call for damaged-part inspection/repair.

This is critical.

```text
OUT-OF-SPEC NON-ADJUSTABLE ANGLE
            ↓
DO NOT "ALIGN AROUND" IT
            ↓
LOOK FOR BENT / SHIFTED / WORN STRUCTURE
```

Possible causes include:

- bent strut,
- bent knuckle,
- bent control arm,
- damaged ball joint,
- shifted or damaged front subframe,
- collapsed spring,
- ride-height difference,
- rear torsion-beam damage,
- damaged hub/bearing interface,
- impact-damaged wheel,
- unibody/chassis deformation,
- or measurement setup error.

Aftermarket camber hardware exists, but it should not be used to hide collision, pothole, or structural damage.

---

# 3. What the alignment angles actually mean

## Toe

Viewed from above:

```text
TOE-IN
front edges of tires closer together

TOE-OUT
front edges of tires farther apart
```

Toe is one of the strongest causes of rapid feathered tread wear.

Too much toe-in often produces one feather direction; too much toe-out tends to reverse that direction. Exact hand-feel interpretation can be affected by tire design and rotation history, so use feathering as a clue, not an angle gauge.

### Toe clues

- feathered tread blocks,
- steering wheel not centered after prior service,
- instability or wandering,
- changed steering feel after tie-rod work,
- rapid wear across otherwise healthy tires,
- steering-wheel center changes after pothole impact.

### Accent-specific service-family rule

Front toe adjustment is made through the tie rods, and Hyundai specifies turning left and right tie rods by equal amounts when correcting total toe so steering-wheel centering is preserved.

Supporting service-family tie-rod locknut torque:

```text
23.5–33.3 N·m
17.4–24.6 lb-ft
```

Do not use this value as an exact 2014 VIN authority without exact-year service documentation.

---

## Camber

Viewed from the front:

```text
NEGATIVE CAMBER
wheel top leans inward

POSITIVE CAMBER
wheel top leans outward
```

Moderate designed negative camber is normal. Excessive or asymmetric camber can produce edge wear or pulling tendencies.

### Camber clues

- persistent inside-edge wear,
- persistent outside-edge wear,
- visible wheel lean,
- cross-camber difference after an impact,
- abnormal reading following strut/knuckle/control-arm damage,
- rear wheel visibly leaning differently from the opposite side.

On the same-generation Accent, normal front and rear camber are not factory service adjustments.

Therefore:

```text
CAMBER OUT OF RANGE
      ↓
INSPECT HARD PARTS + RIDE HEIGHT
```

not:

```text
CAMBER OUT OF RANGE
      ↓
FORCE IT INTO RANGE SOMEHOW
```

---

## Caster

Viewed from the side, caster describes steering-axis tilt.

Caster strongly influences:

- straight-line stability,
- steering self-centering,
- return-to-center feel,
- and pull tendency when left/right values differ materially.

Same-generation Accent caster is factory-set rather than routinely adjustable.

An out-of-spec or asymmetric caster reading therefore raises suspicion for:

- bent control arm,
- bent strut or knuckle,
- shifted subframe,
- impact damage,
- damaged bushings,
- ride-height difference,
- or chassis distortion.

---

# 4. Steering wheel off-center

A crooked steering wheel does not automatically mean the vehicle has a serious alignment error.

Possible causes include:

- toe adjusted without centering the steering wheel,
- one tie rod changed more than the other,
- prior steering repair,
- steering rack not centered during alignment,
- road crown giving a false impression,
- unequal tire pull,
- bent steering/suspension component,
- rear thrust-angle problem,
- subframe shift.

Diagnostic order:

```text
VERIFY TIRE PRESSURES
      ↓
ROAD TEST ON FLAT ROAD
      ↓
VERIFY WHEEL / TIRE MATCH
      ↓
CHECK STEERING / SUSPENSION PLAY
      ↓
MEASURE FRONT + REAR GEOMETRY
      ↓
VERIFY STEERING RACK / WHEEL CENTER
      ↓
ADJUST TOE CORRECTLY
      ↓
ROAD TEST AGAIN
```

Do not center the steering wheel by moving only one tie rod enough to create unequal left/right geometry.

---

# 5. Pull versus drift

## Pull

A **pull** is a distinct tendency for the car to steer toward one side that requires noticeable driver correction.

Possible causes:

- tire conicity / radial pull,
- unequal tire pressure,
- dragging brake,
- front camber difference,
- caster difference,
- bent suspension part,
- subframe shift,
- wheel bearing or hub issue,
- road crown,
- rear thrust-angle problem.

## Drift

A **drift** is a slower directional movement that may be caused by road crown, wind, tire construction, or mild geometry asymmetry.

Never diagnose pull on one crowned lane only.

### Tire-swap logic

If a directional pull changes or reverses after a controlled tire-position swap, tire construction becomes more likely than chassis geometry.

Do not use damaged, mismatched, directionally incorrect, or structurally questionable tires for this test.

---

# 6. Tire-wear pattern matrix

| Wear pattern | First suspects | Do not forget |
|---|---|---|
| Both shoulders | Underinflation | Load, driving history |
| Center wear | Chronic overinflation | Tire design / use history |
| One edge | Camber, toe, bent part | Tire conicity, ride height |
| Feathering | Toe error | Worn tie rods/bushings |
| Cupping / scalloping | Damping / balance / looseness | Strut, bearing, tire defect |
| Flat spot | Lockup, storage, tire defect | Balance and road-force behavior |
| Diagonal wear | Toe + suspension compliance | Rear geometry / worn parts |
| Rapid isolated patch wear | Tire defect, locked brake, severe imbalance | Wheel runout |
| Both fronts wearing quickly | Pressure, toe, driving style | Rotation interval |
| One tire wearing very differently | Local geometry or tire defect | Hub/bearing/brake drag |

Wear pattern is evidence, not a final diagnosis.

---

# 7. Feathering

Feathering feels like the tread blocks have a smooth edge in one direction and a sharper edge in the other.

Most important suspects:

- toe error,
- worn tie rods,
- compliant control-arm bushings,
- impact-induced alignment change,
- rear thrust misalignment.

Do not simply align the car if tie-rod or bushing movement allows toe to change dynamically while driving.

---

# 8. Cupping and scalloping

Cupping is often a repeated high-low pattern around the tire circumference.

Possible causes:

- worn or weak strut/shock damping,
- wheel imbalance,
- tire/wheel radial-force variation,
- bent wheel,
- wheel-bearing looseness,
- loose suspension joint,
- chronic rough-road use.

The 2014 Accent uses MacPherson front struts and a torsion-axle rear suspension with separate rear shocks.

See:

- [`STEERING_SUSPENSION.md`](STEERING_SUSPENSION.md)
- [`../drivetrain/CV_AXLES_WHEEL_BEARINGS.md`](../drivetrain/CV_AXLES_WHEEL_BEARINGS.md)
- [`../drivetrain/NVH_NOISE_VIBRATION_HARSHNESS_MATRIX.md`](../drivetrain/NVH_NOISE_VIBRATION_HARSHNESS_MATRIX.md)

---

# 9. Inside-edge wear

Inside-edge wear may result from:

- excessive negative camber,
- toe error,
- combination of toe + camber,
- bent suspension component,
- changed ride height,
- rear torsion-beam damage,
- overloaded or altered suspension.

Important:

```text
NEGATIVE CAMBER
      ≠
AUTOMATICALLY THE CAUSE
```

A tire can wear its inner edge very rapidly from toe even when camber looks visually dramatic but remains within specification.

Always read the actual alignment sheet.

---

# 10. Outside-edge wear

Possible causes:

- chronic underinflation,
- positive camber or reduced negative camber,
- heavy cornering,
- toe error,
- worn/shifted suspension parts.

Compare both shoulders and all four tires before assigning geometry as the cause.

---

# 11. Pothole / curb / rough-road event

After a hard pothole, curb strike, washboard hit, or underbody event:

1. inspect tire sidewall for bulge/cut,
2. inspect wheel for bend/crack,
3. verify tire pressure,
4. check steering-wheel center,
5. check tie rods and ball joints,
6. check control-arm bushings,
7. check strut/knuckle geometry,
8. check wheel bearing/hub,
9. check front subframe position/damage,
10. inspect rear torsion beam if rear impact occurred,
11. then measure alignment.

### Red conditions after impact

Do not continue driving normally if any of these are present:

- tire sidewall bulge,
- exposed cord,
- visibly bent/cracked wheel,
- wheel rubbing body or suspension,
- severe new steering-wheel offset,
- severe pull,
- clunk with looseness,
- wheel visibly displaced in wheel opening,
- obvious strut/control-arm/tie-rod damage,
- wheel-bearing looseness,
- loss of steering stability.

---

# 12. Ride height matters

Alignment angles change when suspension position changes.

Possible ride-height causes:

- broken or sagging coil spring,
- overloaded vehicle,
- cargo asymmetry,
- worn spring seat,
- collision damage,
- incorrect spring/strut parts.

For nomad use, heavy permanent cargo can change ride height and alter real-world geometry even without any adjustment being touched.

Before interpreting an alignment printout:

```text
UNLOAD UNUSUAL CARGO IF PRACTICAL
VERIFY TIRE PRESSURES
VERIFY RIDE HEIGHT / SPRING CONDITION
```

Do not align around a collapsed spring.

---

# 13. Rear geometry and thrust angle

The rear torsion-beam suspension has no normal factory toe/camber adjustment in same-generation Hyundai service information.

Therefore a rear out-of-spec reading may point toward:

- bent torsion beam,
- bent spindle/hub mounting interface,
- wheel/hub damage,
- body mounting-point damage,
- accident or curb impact,
- measurement error.

Rear geometry can influence the car's thrust direction and steering-wheel center even when the front toe is technically within range.

A crooked steering wheel after a front-only alignment can therefore be a reason to inspect the **whole four-wheel geometry**, not endlessly tweak front tie rods.

---

# 14. Alignment before and after suspension work

Alignment should be considered after work that changes or disturbs geometry, including:

- tie-rod replacement,
- steering rack service,
- strut or knuckle replacement,
- control-arm replacement,
- ball-joint replacement when geometry is disturbed,
- subframe movement,
- major wheel-bearing/knuckle work,
- collision repair,
- significant ride-height change.

But first:

```text
TORQUE / ASSEMBLE CORRECTLY
      ↓
SETTLE SUSPENSION
      ↓
VERIFY NO PLAY
      ↓
THEN ALIGN
```

---

# 15. Tire pressure versus alignment wear

Incorrect pressure can imitate geometry problems.

The exact 2014 SE placard baseline is **33 psi cold front and rear**.

Before interpreting tread wear:

- check pressure cold,
- compare all four tires,
- verify there is no slow leak,
- verify tire size matches,
- inspect age and structural condition,
- check rotation history.

Do not perform an alignment diagnosis on one tire at 25 psi and the others at 33 psi and expect the wear evidence to tell a clean story.

---

# 16. Balance versus alignment

```text
PULL / UNEVEN WEAR
→ alignment / tire / brake / chassis investigation

SMOOTH-ROAD VIBRATION
→ balance / tire / wheel / hub investigation
```

Alignment does not normally cure a classic speed-specific imbalance vibration.

Balance does not normally correct persistent pull or feathered wear caused by geometry.

Some complaints can involve both.

See:

- [`../tires-wheels/TIRES_WHEELS.md`](../tires-wheels/TIRES_WHEELS.md)
- [`../drivetrain/NVH_NOISE_VIBRATION_HARSHNESS_MATRIX.md`](../drivetrain/NVH_NOISE_VIBRATION_HARSHNESS_MATRIX.md)

---

# 17. Steering/suspension inspection before alignment

Minimum pre-alignment inspection:

## Front

- tire pressure and size,
- tire structural condition,
- wheel damage/runout,
- wheel bearing play/noise,
- outer and inner tie rods,
- rack boots,
- ball joints,
- control-arm bushings,
- strut condition,
- spring condition,
- upper strut mount,
- steering rack mounting,
- subframe evidence of shift/damage,
- brake drag.

## Rear

- tire pressure and condition,
- wheel damage,
- hub/bearing play,
- rear shock condition,
- spring condition,
- torsion-beam damage,
- body mounting-point damage,
- brake drag.

If a loose part can change wheel position by hand, an alignment reading is not yet trustworthy.

---

# 18. Steering-wheel centering procedure concept

The steering wheel should be held centered while toe is adjusted.

General logic:

```text
CENTER STEERING SYSTEM
      ↓
LOCK / HOLD STEERING WHEEL
      ↓
MEASURE TOTAL + INDIVIDUAL TOE
      ↓
ADJUST LEFT + RIGHT APPROPRIATELY
      ↓
VERIFY TOTAL TOE
      ↓
VERIFY INDIVIDUAL TOE
      ↓
VERIFY STEERING WHEEL CENTER
      ↓
ROAD TEST
```

Never assume “green total toe” automatically means the steering wheel is centered correctly.

---

# 19. Alignment printout interpretation

A useful printout should preserve:

- before values,
- after values,
- left/right values,
- total toe,
- front camber,
- caster,
- rear camber,
- rear toe,
- thrust angle if reported,
- vehicle loading/setup notes.

For Runa/Aesir, photograph or store the full printout rather than typing only “alignment good.”

### AI-friendly record

```yaml
alignment_event:
  date: null
  odometer_mi: null
  reason: null
  impact_event: null
  tire_pressure_cold_psi:
    LF: null
    RF: null
    LR: null
    RR: null
  before:
    LF_camber_deg: null
    RF_camber_deg: null
    LF_caster_deg: null
    RF_caster_deg: null
    LF_toe_deg: null
    RF_toe_deg: null
    rear_left_camber_deg: null
    rear_right_camber_deg: null
    rear_left_toe_deg: null
    rear_right_toe_deg: null
    thrust_angle_deg: null
  after:
    LF_camber_deg: null
    RF_camber_deg: null
    LF_caster_deg: null
    RF_caster_deg: null
    LF_toe_deg: null
    RF_toe_deg: null
    rear_left_camber_deg: null
    rear_right_camber_deg: null
    rear_left_toe_deg: null
    rear_right_toe_deg: null
    thrust_angle_deg: null
  mechanical_repairs_before_alignment: []
  steering_wheel_centered_after: null
  pull_after: null
  notes: null
```

---

# 20. Nomad / primitive-road guidance

For repeated gravel, washboard, pothole, forest-road, and dispersed-camping use:

- inspect tire shoulders and sidewalls frequently,
- watch for new steering-wheel offset after impacts,
- look for a tire that starts feathering faster than the others,
- inspect tie rods and ball joints after a severe impact,
- inspect wheels for dents after hard potholes,
- do not ignore a new pull after a road strike,
- recheck cold tire pressures after temperature changes,
- keep cargo distribution reasonably balanced,
- do not use alignment as a substitute for fixing bent or loose hardware.

The Accent is a low-clearance road car. Repeatedly striking suspension or underbody components is a route-selection problem as much as a maintenance problem.

---

# 21. Stop-driving conditions

Treat these as RED until proven safe:

- loose tie rod,
- loose ball joint,
- severe wheel-bearing play,
- cracked/bent wheel,
- tire sidewall bulge or exposed cord,
- visibly bent steering component,
- severe pull after impact,
- steering wheel suddenly far off-center,
- wheel visibly displaced in opening,
- tire rubbing suspension/body,
- broken spring,
- structural torsion-beam damage,
- unstable steering response.

Alignment can wait. Structural safety cannot.

---

# 22. Diagnostic workflows

## Uneven tire wear

```text
VERIFY PRESSURE
      ↓
CLASSIFY WEAR PATTERN
      ↓
CHECK TIRE / WHEEL CONDITION
      ↓
CHECK SUSPENSION / STEERING PLAY
      ↓
CHECK RIDE HEIGHT
      ↓
MEASURE ALIGNMENT
      ↓
REPAIR ROOT CAUSE
      ↓
ROTATE / REPLACE TIRE AS JUSTIFIED
      ↓
VERIFY WEAR STABILIZES
```

## Pull

```text
VERIFY PRESSURES + TIRE SIZE
      ↓
ROAD TEST ON FLAT ROAD
      ↓
CHECK BRAKE DRAG
      ↓
CHECK TIRE PULL
      ↓
CHECK SUSPENSION PLAY / DAMAGE
      ↓
MEASURE 4-WHEEL ALIGNMENT
      ↓
REPAIR ROOT CAUSE
```

## Post-pothole steering-wheel offset

```text
INSPECT TIRE + WHEEL
      ↓
CHECK FOR LOOSE / BENT PARTS
      ↓
CHECK BEARING / HUB
      ↓
CHECK RIDE HEIGHT
      ↓
MEASURE ALIGNMENT
      ↓
IF NON-ADJUSTABLE ANGLE IS WRONG:
FIND BENT / SHIFTED PART
```

---

# 23. Rules for Runa / Aesir

When diagnosing alignment or tire wear:

1. Never diagnose alignment from tread wear alone.
2. Never diagnose a bent part from one alignment number alone.
3. Verify cold tire pressure before interpreting geometry.
4. Separate balance vibration from alignment pull/wear.
5. Check mechanical looseness before trusting alignment measurements.
6. Preserve the full before/after alignment printout.
7. Treat 2013 geometry values in this file as **service-family supporting values**, not exact 2014 VIN authority.
8. Do not invent camber/caster adjustment procedures where Hyundai says those angles are factory-set.
9. Do not recommend aftermarket camber hardware merely to mask collision or impact damage.
10. If steering stability is compromised, prioritize towing/repair over alignment convenience.

---

# 24. Sources

## Exact 2014 owner information

- 2014 Hyundai Accent Owner Manual, wheel alignment, tire wear, rotation and balance:
  https://manualzz.com/doc/53857913/hyundai-2014-accent-owner-manual
- CarManualsOnline mirror, 2014 Accent tire maintenance / replacement:
  https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/?srch=tire+replacement
- ManualsLib 2014 Accent owner manual:
  https://www.manualslib.com/manual/1067849/Hyundai-2014-Accent.html

## Same-generation service-family information

- 2013 Hyundai Accent alignment service procedure:
  https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Maintenance/Alignment/Service%20and%20Repair/
- Hyundai 2013 model-year alignment specification bulletin, Accent RB:
  https://static.nhtsa.gov/odi/tsbs/2013/SB-10065908-0699.pdf

---

# Core doctrine

```text
TIRE WEAR / PULL / CROOKED WHEEL
             ↓
PRESSURE
             ↓
TIRE + WHEEL
             ↓
MECHANICAL PLAY / DAMAGE
             ↓
RIDE HEIGHT
             ↓
ALIGNMENT MEASUREMENT
             ↓
REPAIR THE CAUSE
             ↓
ADJUST ONLY WHAT SHOULD ADJUST
             ↓
ROAD TEST + VERIFY
```

> **Do not align around damage. Geometry is evidence of the chassis, not a substitute for inspecting it.**
