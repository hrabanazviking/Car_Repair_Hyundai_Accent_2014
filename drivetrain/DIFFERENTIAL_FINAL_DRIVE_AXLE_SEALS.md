# Differential, Final Drive & Axle Seal Diagnostics — 2014 Hyundai Accent SE

> **Purpose:** diagnose front final-drive, differential, inner-drive-shaft, and transaxle axle-seal problems on the U.S.-market 2014 Hyundai Accent SE with the 6-speed automatic transaxle without confusing them with CV-joint, wheel-bearing, tire, brake, or general transmission faults.

## Source Confidence

- **EXACT 2014 PARTS DATA** — Hyundai parts catalog data for the 2014 Accent 1.6 GDI, 6AT, 2WD.
- **SERVICE-FAMILY — 2012/2013 ACCENT 1.6** — same-generation Accent service information used where exact 2014 workshop text is not publicly available.
- **HYUNDAI 6-SPEED TSB** — Hyundai 6-speed ATF-level procedure applicable to Accent RB and related Hyundai models.
- **GENERAL DRIVETRAIN PRACTICE** — standard front-wheel-drive diagnostic reasoning, clearly separated from Hyundai-specific specifications.

Primary sources are linked in [Sources](#sources).

---

# Core Rule

```text
AXLE-SEAL LEAK / WHINE / VIBRATION
        ≠
FAILED DIFFERENTIAL PROVEN
```

A noise or leak near the inner CV joint can come from:

- an axle seal,
- an incompletely seated drive shaft,
- a worn sealing surface,
- a damaged inner CV joint,
- a wheel bearing,
- tires,
- brakes,
- a transmission case or cover leak,
- a venting problem,
- low automatic-transaxle fluid,
- differential bearings,
- transfer/final-drive bearings,
- internal gear wear,
- or damage created during previous axle service.

Correct sequence:

```text
LOCATE FLUID / NOISE
      ↓
IDENTIFY SYSTEM
      ↓
CHECK ATF LEVEL / SHAFT SEATING
      ↓
CHECK CV + HUB + TIRE ALTERNATIVES
      ↓
CHECK SEAL / CASE / VENT
      ↓
VERIFY BEARING / FINAL-DRIVE EVIDENCE
      ↓
REPAIR ROOT CAUSE
      ↓
SET ATF LEVEL CORRECTLY
      ↓
ROAD TEST + RECHECK FOR LEAKS
```

---

# 1. Exact 2014 Automatic-Transaxle Architecture

The 2014 Accent SE automatic is a **front-wheel-drive 6-speed automatic transaxle**. The final-drive and differential assembly are integrated into the transaxle rather than existing as a separate rear-style differential housing.

**EXACT 2014 PARTS DATA** confirms the 6AT/2WD automatic transaxle contains dedicated differential and final-drive hardware including:

- differential case,
- differential gear set,
- differential drive gear,
- transfer drive gear,
- transfer-driven gear hardware,
- tapered-roller and other supporting bearings,
- thrust washers/spacers,
- left/right automatic-transaxle case oil seals.

The exact 2014 catalog lists, among other components:

- `45821-26000` — differential case,
- `45837-26000` — differential gear set,
- `45832-26020` — differential drive gear,
- `45811-26010` — transfer drive gear,
- `45737-26300` — tapered roller bearing family,
- `45829-3B700` — transfer-driven-gear bearing family.

These listings confirm the internal mechanical architecture. They do **not** by themselves prove a noisy component is failed.

## A6GF1 identification

**SERVICE-FAMILY — 2013 ACCENT 1.6** identifies the six-speed automatic transaxle model as **A6GF1**.

That same service-family identification table encodes a **2.937 final-drive ratio** for the applicable transaxle code family and explicitly includes an `E` production-year code for 2014.

Treat the 2.937 value as **same-generation service-family evidence**, not a substitute for decoding the actual transaxle tag when exact configuration matters.

---

# 2. What the Differential Does

The differential allows the two front wheels to rotate at different speeds while transmitting engine torque through the transaxle final drive.

During a turn:

- the outside wheel travels farther,
- the inside wheel travels a shorter path,
- the differential permits that speed difference.

The final-drive gearset also provides the final speed reduction between the transmission geartrain and the front axle shafts.

A fault in this area can therefore create symptoms that depend on:

- vehicle speed,
- throttle load,
- coast versus acceleration,
- steering angle,
- left/right wheel loading,
- ATF level,
- and temperature.

---

# 3. Exact 2014 Axle-Seal Hardware

**EXACT 2014 PARTS DATA** shows two distinct automatic-transaxle case oil-seal families for the 6AT 2WD Accent:

- `45245-26110` — oil seal, replacing earlier `45245-26100`,
- `45245-26210` — oil seal, replacing earlier `45245-26200`.

The exact catalog lists both updated seals for **2014 Accent 4-door and 5-door 6AT 2WD** configurations.

These seals live where the front drive shafts interface with the automatic-transaxle case/differential area.

## Important

Left/right seal part identity should be confirmed by VIN/catalog position before ordering. Do not assume two similar-looking seals interchange side-to-side.

---

# 4. Axle-Seal Leak vs CV-Boot Leak

A wet area around the inner drive shaft does not automatically mean the transaxle seal is leaking.

## Axle-seal / ATF leak tends to appear as

- thin oily fluid around the shaft where it enters the transaxle,
- wetness spreading over the case below the seal,
- drip formation after parking,
- fluid tracks on the transmission case or underbody,
- declining ATF level if leakage is significant.

## Inner-CV boot leak tends to appear as

- thick grease,
- grease thrown in a circular pattern,
- grease on suspension or underbody near the rotating joint,
- visible boot crack, split, puncture, or loose clamp.

## Engine-oil leak can migrate

Engine oil from above can run down onto the transmission and imitate a case or seal leak.

Before replacing a seal:

```text
CLEAN AREA
   ↓
DRY AREA
   ↓
DRIVE / RUN BRIEFLY
   ↓
TRACE FRESH FLUID TO HIGHEST WET POINT
```

Do not diagnose solely from old residue.

---

# 5. Axle-Seal Leak Severity

## GREEN — monitor / schedule repair

Examples:

- slight dampness,
- no drip,
- verified correct ATF level,
- no transmission symptoms,
- no rapidly expanding wet area.

Still document and recheck it.

## YELLOW — repair soon

Examples:

- fresh wetness after each drive,
- occasional drops,
- seal leak after recent axle work,
- ATF level requires correction,
- oil tracks reach splash shield or underbody.

## RED — stop or tow

Examples:

- active dripping or stream,
- fresh puddle after a short drive,
- delayed engagement or slipping after fluid loss,
- new whining accompanied by known fluid loss,
- shaft visibly displaced from transaxle,
- severe vibration/clunk plus fluid leakage,
- metal fragments or catastrophic internal noise,
- inability to verify sufficient ATF.

A leaking seal is a **fluid-loss problem**, not merely a cleanliness problem.

---

# 6. Do Not Refill by Total Capacity Alone

The same-generation Accent service specification lists approximately:

```text
A6GF1 TOTAL ATF CAPACITY
7.71 US qt / 7.3 L
```

That is a **total system capacity**, not the amount automatically required after an axle-seal repair or partial leak.

Do not pour in 7.3 L because the seal leaked.

Correct logic:

```text
REPAIR LEAK
   ↓
ADD APPROPRIATE SP-IV AS NEEDED
   ↓
PERFORM TEMPERATURE-CONTROLLED LEVEL CHECK
```

---

# 7. ATF Specification and Level Check

**SERVICE-FAMILY — 2013 ACCENT 1.6** specifies **ATF SP-IV** or a Hyundai-approved equivalent meeting the SP-IV requirement.

Hyundai's 6-speed ATF-level procedure, applicable to the Accent RB, uses the transmission oil-temperature PID and checks the fluid at:

```text
50–60°C
122–140°F
```

The vehicle is level, the engine is running, the selector has been cycled through the ranges, and the level port is opened.

Correct level is indicated by ATF exiting in a **thin steady stream**.

No flow indicates shortage under the prescribed test conditions.

## Critical diagnostic rule

```text
TOTAL CAPACITY
      ≠
CORRECT OPERATING LEVEL
```

A leak repair is not complete until the operating level is verified by the correct procedure.

See also:

- [`../transmission/SIX_SPEED_AUTOMATIC.md`](../transmission/SIX_SPEED_AUTOMATIC.md)
- [`../specs/FLUIDS_AND_CAPACITIES.md`](../specs/FLUIDS_AND_CAPACITIES.md)

---

# 8. Why an Axle Seal Starts Leaking

Possible causes include:

- seal lip wear,
- hardened seal material,
- installation damage,
- shaft spline cutting the seal during installation,
- drive shaft installed at an angle,
- drive shaft not fully seated,
- worn or damaged sealing surface,
- excessive shaft movement,
- internal bearing wear allowing radial movement,
- damaged transaxle case seal bore,
- dirt or corrosion on sealing surfaces,
- previous improper removal tool placement,
- transaxle vent restriction increasing internal pressure.

The exact 2014 automatic-transaxle case catalog confirms the transaxle includes a dedicated breather-hose assembly (`45270-3B000`).

Therefore, persistent repeat leakage should not automatically be blamed on a second defective seal. Verify the shaft, support bearings, case, and venting.

---

# 9. Hyundai Service Rule for a Damaged Seal

**SERVICE-FAMILY — 2013 ACCENT 1.6** states that if the transaxle-case oil seal is damaged and fluid is leaking, the seal should be replaced.

The same service procedure specifies special oil-seal installer:

```text
SST 09452-26100
```

for installing the replacement seal.

The point is not that this exact SST must always be personally owned. The important principle is:

- drive the seal squarely,
- support it at the correct surface,
- install it to the correct depth,
- do not distort the case bore,
- do not hammer randomly on the seal shell,
- do not damage the sealing lip.

---

# 10. Axle Removal Can Create the Leak

The shaft-to-seal interface is vulnerable during axle removal and installation.

Common service-created problems include:

- pry tool inserted too deeply,
- tool contact with seal lip,
- nicked seal bore,
- dragging splines across the lip,
- shaft hanging unsupported,
- forcing the shaft in at an angle,
- failing to verify full shaft engagement.

If an axle seal begins leaking immediately after drive-shaft replacement, inspect the service interface before assuming unrelated internal transmission failure.

---

# 11. Verify the Shaft Is Fully Seated

After axle installation inspect for:

- abnormal gap at the transaxle interface,
- obvious shaft misalignment,
- fresh ATF leakage,
- new clunk on acceleration/deceleration,
- vibration that did not exist before service,
- abnormal inner-joint angle,
- wheel-speed/ABS issues caused by disturbed axle/hub components.

Do not use "it went in far enough" as the final test.

The shaft must be mechanically seated as designed and the seal must remain dry.

---

# 12. Final-Drive / Differential Noise

Internal final-drive noise is often confused with wheel bearings and tires.

## Differential/final-drive becomes more plausible when

- noise clearly changes between acceleration and coast,
- noise follows vehicle speed rather than engine RPM,
- there is known low-ATF history,
- metal is found in drained fluid,
- noise originates centrally near the transaxle,
- noise began after substantial fluid loss,
- axle/hub/tire causes have been reasonably excluded.

## Wheel bearing becomes more plausible when

- hum/growl follows road speed,
- noise changes as wheel loading shifts through gentle turns,
- sound localizes near one hub,
- bearing roughness/play is found,
- ATF level and transaxle behavior remain normal.

See:

- [`CV_AXLES_WHEEL_BEARINGS.md`](CV_AXLES_WHEEL_BEARINGS.md)

## Tire noise becomes more plausible when

- noise changes dramatically with pavement texture,
- tread is cupped or feathered,
- rotation changes the sound,
- noise remains insensitive to throttle/coast state.

See:

- [`../tires-wheels/TIRES_WHEELS.md`](../tires-wheels/TIRES_WHEELS.md)

---

# 13. Acceleration Whine vs Coast Whine

A load-sensitive gear or bearing noise may change when driveline torque reverses.

Useful observations:

- louder under acceleration,
- quieter on coast,
- louder on coast,
- unchanged with throttle,
- changes with steering load,
- changes with pavement.

These observations are **diagnostic clues**, not standalone proof of which bearing or gear has failed.

Do not condemn a differential from a smartphone sound clip alone.

---

# 14. Vibration Near the Differential Is Often Not the Differential

A vibration under acceleration can come from:

- inner CV joint,
- bent drive shaft,
- engine/transaxle mount,
- wheel/tire imbalance,
- damaged hub/bearing,
- transmission engagement problem,
- differential/final-drive damage.

Use this hierarchy:

```text
VIBRATION UNDER LOAD
      ↓
ENGINE RUNNING QUALITY
      ↓
MOUNTS
      ↓
INNER CV JOINTS / SHAFTS
      ↓
TIRES / WHEELS / HUBS
      ↓
ATF / TRANSAXLE DATA
      ↓
INTERNAL FINAL DRIVE
```

See:

- [`ENGINE_TRANSAXLE_MOUNTS_VIBRATION.md`](ENGINE_TRANSAXLE_MOUNTS_VIBRATION.md)
- [`CV_AXLES_WHEEL_BEARINGS.md`](CV_AXLES_WHEEL_BEARINGS.md)

---

# 15. Differential Bearing / Transfer Bearing Evidence

The exact 2014 automatic-transaxle parts catalog confirms multiple bearings associated with the differential and transfer/final-drive sections.

Potential signs of internal bearing trouble include:

- persistent growl/whine from the transaxle centerline,
- shaft movement beyond normal design clearance,
- repeat axle-seal failure with verified correct seal installation,
- metallic debris in fluid,
- roughness that remains after tire/hub/CV causes are excluded.

But internal teardown should follow evidence.

```text
REPEAT SEAL LEAK
      ≠
AUTOMATICALLY BAD DIFFERENTIAL BEARING
```

First prove abnormal shaft movement or internal noise.

---

# 16. One Wheel vs Both Wheels

Do not overinterpret which side seems noisy.

The differential mechanically connects both front axle outputs. Structure-borne sound can travel through:

- transaxle case,
- subframe,
- shafts,
- knuckles,
- body structure.

A noise that sounds left-side inside the cabin can originate somewhere else.

Use physical inspection, chassis-ear style localization when available, temperature comparison, shaft play inspection, and road-test pattern analysis.

Never run the driven wheels at speed with the car supported only by a jack.

---

# 17. ATF Leak After Axle Replacement

If leakage starts after axle work:

1. Stop and inspect before extended driving.
2. Clean the area.
3. Confirm the fluid is ATF rather than CV grease or engine oil.
4. Inspect shaft seating.
5. Inspect seal lip/bore area.
6. Verify the shaft is not visibly wobbling.
7. Replace a damaged seal.
8. Correct ATF level using the temperature-controlled procedure.
9. Road test briefly.
10. Reinspect immediately for fresh leakage.

Do not keep adding fluid indefinitely to "manage" a damaged seal.

---

# 18. Low ATF Can Turn a Seal Leak Into a Transmission Failure

A leak at the axle seal removes fluid from the same automatic-transaxle fluid supply used by the rest of the transmission.

Low fluid can contribute to:

- delayed engagement,
- flare/slip,
- abnormal shift quality,
- overheating,
- lubrication loss,
- pump cavitation/aeration,
- internal wear.

If shifting behavior changes after known fluid loss:

```text
STOP DRIVING
   ↓
REPAIR LEAK
   ↓
VERIFY CORRECT LEVEL
   ↓
SCAN TCM
   ↓
REASSESS TRANSMISSION OPERATION
```

---

# 19. Fluid Color Alone Is Not a Diagnosis

Do not decide ATF health solely by color.

Evaluate:

- level,
- odor,
- contamination,
- suspended metal,
- water/coolant contamination,
- shift symptoms,
- temperature history,
- service history.

A dark fluid sample may justify investigation, but it does not identify which mechanical component failed.

---

# 20. Metal in the ATF

Small magnetic fuzz and catastrophic metal are not equivalent.

Concern rises sharply with:

- flakes,
- chips,
- needle-like fragments,
- bronze/copper-colored material,
- substantial shiny debris,
- repeated debris after service,
- debris plus noise/slip.

When metal is significant, do not merely replace an axle seal and call the problem solved.

The seal may be only the visible symptom of internal wear.

---

# 21. Breather / Vent Checks

The automatic transaxle needs pressure equalization as temperature changes.

The exact 2014 catalog includes an automatic-transaxle breather hose.

Inspect for:

- kinked hose,
- blockage,
- mud/debris contamination,
- incorrect routing,
- crush damage from previous work.

A blocked vent can increase internal case pressure and can contribute to leakage at vulnerable seals.

Do not intentionally plug the breather to stop a leak.

---

# 22. Primitive-Road / Nomad Inspection

After rough gravel, washboard, ruts, or a hard underbody impact:

check:

- inner CV boots,
- outer CV boots,
- axle-to-transaxle seal areas,
- transmission case for fresh impact marks,
- splash shields,
- transaxle breather routing,
- lower engine/transaxle area for fresh fluid,
- new vibration under acceleration,
- new whine/growl,
- ABS/ESC warning lamps.

A low-clearance car can contact debris before the driver feels a dramatic impact.

See:

- [`../maintenance/PRE_TRIP_INSPECTION.md`](../maintenance/PRE_TRIP_INSPECTION.md)
- [`../suspension-steering/STEERING_SUSPENSION.md`](../suspension-steering/STEERING_SUSPENSION.md)

---

# 23. What Is Field-Serviceable?

## Reasonable field diagnosis

- inspect leak location,
- clean and trace fresh fluid,
- inspect CV boots,
- inspect shaft seating visually,
- scan TCM/ABS modules,
- record noise behavior,
- inspect for case impact,
- verify no catastrophic fluid loss,
- arrange proper ATF-level service.

## Shop-level work is preferred for

- axle-seal replacement without proper support/tools,
- drive-shaft removal where contamination control is poor,
- differential bearing diagnosis,
- final-drive teardown,
- case bearing replacement,
- gear backlash/preload work,
- transmission internal repair.

A roadside campsite is a poor place to open a transmission to dust and grit.

---

# 24. Do Not Work Under a Jack-Supported Car

Any inspection requiring a person beneath the vehicle requires proper support.

```text
FACTORY JACK / BOTTLE JACK
        ≠
SAFE UNDER-VEHICLE SUPPORT
```

Use rated stands or professional lifting equipment on verified support points and stable ground.

See:

- [`../roadside/RECOVERY_TOWING_JACKING.md`](../roadside/RECOVERY_TOWING_JACKING.md)

---

# 25. Decision Tree — Fluid at Inner CV Joint

```text
WET INNER CV / TRANSAXLE AREA
        ↓
CLEAN + IDENTIFY FLUID
        ↓
THICK GREASE?
   ├─ YES → CV BOOT / CLAMP / JOINT
   └─ NO
        ↓
THIN ATF FROM SHAFT-CASE INTERFACE?
   ├─ YES → AXLE SEAL / SHAFT / BEARING / VENT
   └─ NO
        ↓
TRACE LEAK FROM ABOVE / CASE / COVER
        ↓
REPAIR SOURCE
        ↓
VERIFY ATF LEVEL
```

---

# 26. Decision Tree — Whine / Growl

```text
WHINE / GROWL
     ↓
FOLLOWS ENGINE RPM WHILE STOPPED?
   ├─ YES → ENGINE / ACCESSORY / PUMP PATH
   └─ NO
        ↓
FOLLOWS ROAD SPEED?
   ├─ NO → RECLASSIFY
   └─ YES
        ↓
CHANGES WITH PAVEMENT?
   ├─ YES → TIRES HIGHER ON LIST
   └─ NO
        ↓
CHANGES WITH GENTLE LEFT/RIGHT LOAD?
   ├─ YES → HUB BEARING HIGHER ON LIST
   └─ NO
        ↓
CHANGES ACCEL vs COAST?
   ├─ YES → CV / FINAL DRIVE / TRANSAXLE
   └─ NO
        ↓
VERIFY ATF + AXLES + HUBS BEFORE INTERNAL TEARDOWN
```

---

# 27. Decision Tree — Leak After Axle Work

```text
AXLE JUST SERVICED
      ↓
NEW ATF LEAK
      ↓
VERIFY SHAFT SEATING
      ↓
INSPECT SEAL / CASE BORE
      ↓
CHECK FOR SHAFT WOBBLE
      ↓
REPLACE DAMAGED SEAL CORRECTLY
      ↓
SET SP-IV LEVEL AT 50–60°C
      ↓
ROAD TEST
      ↓
RECHECK DRYNESS
```

---

# 28. AI / Runa Rules

When diagnosing differential/final-drive/axle-seal symptoms, the AI must:

1. Ask whether the car is automatic or manual before using transmission-specific data.
2. For this vehicle profile, treat the 6AT as A6GF1 service-family architecture.
3. Distinguish ATF from CV grease and engine oil before diagnosing a seal.
4. Never use total ATF capacity as a leak-repair refill amount.
5. Require temperature-controlled ATF level verification after leakage/repair.
6. Never condemn a differential from noise description alone.
7. Compare tires, wheel bearings, CV joints, mounts, brakes, and transmission before internal teardown.
8. Treat repeat axle-seal leakage as a reason to inspect shaft/bearing/case/vent condition.
9. Preserve exact-2014 parts data separately from 2012/2013 service-family specifications.
10. Never invent differential preload, backlash, bearing-clearance, or seal-depth values.
11. Never advise continued driving with rapid ATF loss or transmission slip after leakage.
12. Never recommend working under a vehicle supported only by a jack.

---

# 29. Suggested Incident Record

```yaml
incident_type: drivetrain_final_drive
vehicle:
  year: 2014
  model: Hyundai Accent SE
  body: 5-door
  transmission: 6AT
symptom:
  leak: true
  noise: false
  vibration: false
fluid:
  suspected_type: ATF
  leak_location: left_axle_seal_area
  drip_rate: unknown
transaxle_behavior:
  delayed_engagement: false
  slip: false
  harsh_shift: false
noise_pattern:
  road_speed_related: unknown
  acceleration_related: unknown
  coast_related: unknown
inspection:
  cv_boot_damaged: false
  shaft_visibly_seated: true
  shaft_wobble: unknown
  case_damage: false
  breather_obstructed: unknown
atf:
  specification: SP-IV
  level_verified_at_50_60C: false
action:
  drive_status: CAUTION
  next_step: verify_source_and_ATF_level
confidence: medium
```

---

# 30. Core Doctrine

```text
LEAK / WHINE / VIBRATION
        ↓
IDENTIFY SYSTEM
        ↓
VERIFY ATF LEVEL
        ↓
VERIFY AXLE + SEAL + HUB + TIRE
        ↓
VERIFY VENT / CASE
        ↓
PROVE INTERNAL FINAL-DRIVE FAULT
        ↓
REPAIR ROOT CAUSE
        ↓
SET FLUID LEVEL CORRECTLY
        ↓
VERIFY DRY + QUIET + NORMAL OPERATION
```

> **An axle seal is the boundary. If it leaks, find out why, restore the fluid correctly, and prove the rest of the drivetrain survived.**

---

# Cross-References

- [`CV_AXLES_WHEEL_BEARINGS.md`](CV_AXLES_WHEEL_BEARINGS.md)
- [`ENGINE_TRANSAXLE_MOUNTS_VIBRATION.md`](ENGINE_TRANSAXLE_MOUNTS_VIBRATION.md)
- [`../transmission/SIX_SPEED_AUTOMATIC.md`](../transmission/SIX_SPEED_AUTOMATIC.md)
- [`../specs/FLUIDS_AND_CAPACITIES.md`](../specs/FLUIDS_AND_CAPACITIES.md)
- [`../specs/TORQUE_SPECS.md`](../specs/TORQUE_SPECS.md)
- [`../roadside/RECOVERY_TOWING_JACKING.md`](../roadside/RECOVERY_TOWING_JACKING.md)
- [`../roadside/EMERGENCY_FIELD_REPAIRS.md`](../roadside/EMERGENCY_FIELD_REPAIRS.md)
- [`../tires-wheels/TIRES_WHEELS.md`](../tires-wheels/TIRES_WHEELS.md)

---

# Sources

## Exact 2014 Hyundai Accent parts architecture

- 2014 automatic-transaxle case, including the updated axle-seal families `45245-26110` and `45245-26210`, breather hose, case components:
  https://www.hyundaipartsdeal.com/parts-list/2014-hyundai-accent/transmission/auto_transmission_case.html

- 2014 automatic-transaxle gear architecture, differential case, differential gear set, differential drive gear, transfer gears and bearings:
  https://www.hyundaipartsdeal.com/parts-list/2014-hyundai-accent/transmission/transaxle_gear_auto.html

- Genuine Hyundai `45245-26110` oil seal fitment:
  https://www.hyundaipartsdeal.com/genuine/hyundai-seal-oil~45245-26110.html

- Genuine Hyundai `45245-26210` oil seal fitment:
  https://www.hyundaipartsdeal.com/genuine/hyundai-seal-oil~45245-26210.html

## Same-generation Accent service information

- 2013 Accent automatic-transaxle removal/installation; damaged transaxle-case oil seal replacement and SST `09452-26100`:
  https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Transmission%20and%20Drivetrain/Automatic%20Transmission%2FTransaxle/Service%20and%20Repair/Removal%20and%20Replacement/Automatic%20Transaxle%20Repair%20Procedures/

- 2013 Accent transaxle identification, A6GF1 and service-family final-drive coding:
  https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Application%20and%20ID/Transaxle%20Number/

- 2013 Accent ATF capacity:
  https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Transmission%20and%20Drivetrain/Automatic%20Transmission%2FTransaxle/Fluid%20-%20A%2FT/Specifications/Capacity%20Specifications/

- 2013 Accent SP-IV fluid specification:
  https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Maintenance/Fluids/Fluid%20-%20A%2FT/Specifications/Fluid%20Type%20Specifications/

- 2012 Accent automatic-transaxle fluid level procedure, including 50–60°C check and overflow-level method:
  https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Transmission%20and%20Drivetrain/Automatic%20Transmission%2FTransaxle/Fluid%20-%20A%2FT/Service%20and%20Repair/Repair%20Procedures/

## Hyundai 6-speed ATF procedure

- Hyundai TSB 13-AT-006, 6-speed ATF level checking procedure including Accent RB:
  https://charm.li/Hyundai/2013/Santa%20Fe%20FWD%20L4-2.0L%20Turbo/Repair%20and%20Diagnosis/Transmission%20and%20Drivetrain/Automatic%20Transmission%2FTransaxle/Technical%20Service%20Bulletins/All%20Technical%20Service%20Bulletins/A%2FT%20%286%20Speed%29%20-%20ATF%20Fluid%20Level%20Checking%20Procedure/
