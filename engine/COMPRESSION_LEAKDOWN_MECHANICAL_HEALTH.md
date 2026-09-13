# 2014 Hyundai Accent SE — Compression, Leak-Down & Mechanical Engine Health

> **Purpose:** An offline-first guide for separating ignition, fuel, air, control-system, and mechanical-cylinder faults on a U.S.-market 2014 Hyundai Accent SE with the 1.6 L Gamma GDI engine.
>
> **Core rule:** A misfire code does **not** prove an ignition problem, injector problem, or bad engine. Mechanical condition must be tested when the evidence points there.

---

## 1. Scope

This guide covers:

- Dry compression testing
- Wet compression testing
- Cylinder leak-down testing
- Ring and cylinder-wall diagnosis
- Intake-valve and exhaust-valve leakage
- Head-gasket and combustion-to-coolant clues
- Valve-clearance effects
- Mechanical timing effects
- Cranking-speed effects
- Battery-voltage effects
- Borescope inspection
- Spark-plug evidence
- Blow-by clues
- Oil-consumption clues
- Coolant-loss clues
- Cylinder-to-cylinder comparison
- Interpreting a single low cylinder
- Interpreting two adjacent low cylinders
- Interpreting all cylinders low
- Deciding when mechanical engine repair is actually justified

Related repository files:

- `MISFIRE.md` if present in this directory, or `../diagnostics/MISFIRE.md`
- `TIMING_CVVT.md`
- `LUBRICATION_SYSTEM.md`
- `PCV_CRANKCASE_VENTILATION.md`
- `GDI_FUEL_SYSTEM.md`
- `IGNITION.md`
- `../diagnostics/CRANK_NO_START.md`
- `../diagnostics/FUEL_TRIM_DIAGNOSTICS.md`
- `../specs/TORQUE_SPECS.md`

---

# 2. What Compression Testing Actually Tells You

A gasoline engine cylinder must trap and compress its air charge before combustion.

That requires sealing at:

- Piston rings against the cylinder wall
- Intake valves against their seats
- Exhaust valves against their seats
- Cylinder-head gasket around the bore
- Cylinder head and block sealing surfaces
- Spark-plug sealing seat

A compression test asks:

> **How much pressure can this cylinder create while the starter cranks the engine?**

It is a system test, not a direct measurement of one component.

A low reading can result from:

- Worn, stuck, broken, or damaged piston rings
- Scored cylinder wall
- Burned, bent, sticking, or poorly seated valve
- Incorrect valve clearance
- Head-gasket leakage
- Cracked head or block
- Incorrect mechanical cam timing
- Insufficient cranking speed
- Weak battery
- Closed throttle during a test that requires wide-open throttle
- Test-equipment leakage
- A compression gauge that does not fit or seal correctly

Therefore:

```text
LOW COMPRESSION
      ≠
BAD RINGS
```

---

# 3. Confidence / Provenance Tags

Use these tags when adding future specifications:

- `VERIFIED — EXACT 2014 OWNER DATA`
- `VERIFIED — EXACT 2014 SERVICE DATA`
- `SERVICE-FAMILY — 2013 ACCENT 1.6 GDI`
- `GENERAL DIAGNOSTIC PRACTICE`
- `PROVISIONAL`
- `UNKNOWN`

This file currently uses **2013 Accent 1.6 GDI service information** for compression specifications because an exact 2014 factory service source has not yet been verified in this repository.

Do not silently promote service-family data to exact 2014 status.

---

# 4. Hyundai Same-Engine Compression Baseline

`SERVICE-FAMILY — 2013 ACCENT 1.6 GDI`

Hyundai service information for the same-generation 1.6 L GDI Accent specifies:

| Item | Specification |
|---|---:|
| Standard compression pressure | **1225.83 kPa / 12.5 kg/cm² / 177.79 psi** |
| Minimum compression pressure | **1078.73 kPa / 11.0 kg/cm² / 156.46 psi** |
| Maximum difference between cylinders | **98 kPa / 1.0 kg/cm² / 14 psi** |
| Reference cranking speed | **200–250 rpm** |

Source:

- Hyundai 2013 Accent 1.6L compression check: https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Engine%2C%20Cooling%20and%20Exhaust/Engine/Tune-up%20and%20Engine%20Performance%20Checks/Compression%20Check/Testing%20and%20Inspection/

### Repository rule

Treat these numbers as **high-confidence service-family guidance**, not exact 2014 factory specifications until the exact 2014 service document is obtained.

---

# 5. Factory Compression-Test Preparation

`SERVICE-FAMILY — 2013 ACCENT 1.6 GDI`

Hyundai's same-engine procedure calls for:

1. Correct engine-oil level and viscosity.
2. A correctly charged battery.
3. Engine at normal operating temperature.
4. Ignition OFF before disconnecting components.
5. Injector extension connector disconnected.
6. Ignition-coil connectors disconnected.
7. Ignition coils removed.
8. All spark plugs removed.
9. Compression gauge installed in the spark-plug hole.
10. Throttle plate held wide open.
11. Engine cranked while pressure is measured.
12. Test repeated for all four cylinders.
13. Measurements completed in as short a period as practical so test conditions remain comparable.

Hyundai specifically notes the importance of adequate battery charge and cranking speed.

---

# 6. Safety Before Cranking

Before a compression test:

- Park on a stable surface.
- Select `P` on the automatic transmission.
- Set the parking brake.
- Keep hands, hair, clothing, tools, test hoses, and cables away from belts and rotating parts.
- Disable fuel and ignition using the service procedure rather than allowing raw fuel to be repeatedly injected.
- Do not allow loose ignition-coil connectors or wiring to fall into rotating components.
- Keep the compression hose away from the cooling fan and accessory belt.
- Do not touch hot exhaust components.

The engine may crank unexpectedly whenever the starter is commanded.

---

# 7. Dry Compression Test

## Procedure

1. Warm the engine to normal operating temperature if the engine can be safely run.
2. Shut the engine off.
3. Verify battery state of charge.
4. Disable fuel injection and ignition.
5. Remove all four ignition coils.
6. Remove all four spark plugs.
7. Inspect and label the plugs by cylinder before setting them aside.
8. Install the compression gauge in the first cylinder.
9. Hold the throttle plate in the test-required wide-open condition.
10. Crank the engine until the gauge stops increasing materially.
11. Record:
   - maximum pressure
   - how rapidly pressure built
   - approximate cranking speed if available through scan data
   - battery voltage during cranking if available
12. Repeat under the same conditions for all cylinders.

### Record the pattern, not merely the highest number

A useful log is:

| Cylinder | Dry PSI | Build pattern | Cranking RPM | Cranking voltage | Notes |
|---|---:|---|---:|---:|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |

Do **not** guess the physical end of the engine corresponding to cylinder 1 unless the exact 2014 service diagram has been verified. Preserve the cylinder numbering used by the service procedure or diagnostic tool.

---

# 8. Why Cranking Speed Matters

Compression pressure is partly a function of how quickly the engine turns during the test.

A weak battery, poor starter circuit, bad ground, dragging starter, or cold/thick oil can lower readings across the engine.

If all cylinders are unexpectedly low, first ask:

```text
ARE ALL CYLINDERS BAD?
        OR
IS THE TEST CONDITION BAD?
```

Check:

- Battery charge
- Cranking voltage
- Starter speed
- Grounds
- Positive cable voltage drop
- Throttle opening
- Gauge sealing
- Engine temperature

Cross-reference:

- `../diagnostics/NO_CRANK.md`
- `../diagnostics/CHARGING_SYSTEM.md`
- `../electrical/BATTERY_STARTER_ALTERNATOR.md`
- `../electrical/GROUND_POINTS.md`

---

# 9. Compression Pattern Interpretation

## Pattern A — All cylinders close together and above minimum

Mechanical sealing is less likely to be the root cause.

Shift attention toward:

- Ignition
- Injector operation
- Fuel pressure
- MAP/IAT plausibility
- Vacuum leak
- EVAP purge
- Throttle control
- Wiring
- Sensor synchronization

Do not keep tearing into a mechanically healthy engine because a misfire code exists.

---

## Pattern B — One cylinder clearly low

Possible causes include:

- Burned valve
- Bent valve
- Valve not seating
- Incorrect valve clearance
- Broken/stuck ring
- Scored cylinder
- Localized head-gasket leak
- Damaged piston

Next tests:

1. Wet compression test.
2. Leak-down test.
3. Borescope inspection.
4. Valve-clearance inspection if evidence points toward valve seating.

---

## Pattern C — Two adjacent cylinders low

Possible causes include:

- Head-gasket leakage between neighboring cylinders
- Cylinder-head sealing problem
- Local timing/valve damage affecting both cylinders

This pattern is **evidence**, not automatic proof of a head gasket.

Confirm with leak-down, cooling-system evidence, borescope findings, and service measurements.

---

## Pattern D — All cylinders uniformly low

Possible causes include:

- Low cranking speed
- Weak battery
- Closed throttle
- Incorrect test method
- Gauge error
- Mechanical cam timing shifted
- Severe overall wear

Uniformly low compression does not automatically mean four cylinders failed independently.

Check shared causes first.

---

## Pattern E — Compression extremely low or near zero on one cylinder

Possible causes include:

- Valve held open
- Bent/broken valve
- Severe valve-seat damage
- Piston damage
- Large head-gasket leak
- Major mechanical-timing problem

Do not repeatedly crank an engine showing new severe mechanical noise or evidence of internal contact.

---

# 10. Wet Compression Test

Hyundai's same-engine procedure instructs adding a **small amount of engine oil** to a low cylinder and repeating the compression test.

It does **not** require this repository to invent a universal volume.

## Interpretation

### Compression rises meaningfully after adding oil

Likely direction:

- Piston-ring sealing problem
- Cylinder-wall wear or damage

The temporary oil film improves ring-to-wall sealing.

### Compression stays low

Likely direction:

- Intake valve leak
- Exhaust valve leak
- Sticking valve
- Poor valve seating
- Head-gasket leakage

Hyundai's same-engine service procedure explicitly uses this wet-test logic.

### Important limitation

A wet test is not perfectly exclusive.

Oil can sometimes alter sealing in more than one way, and combined faults are possible.

Use it as **directional evidence**, then confirm with leak-down.

---

# 11. Cylinder Leak-Down Test

`GENERAL DIAGNOSTIC PRACTICE`

A leak-down test answers a different question than compression testing:

> **When the cylinder is held closed at top dead center on the compression stroke, where does supplied air escape?**

A leak-down tester applies regulated compressed air through the spark-plug hole and compares supply pressure with retained cylinder pressure.

General reference:

- Mobil leak-down overview: https://www.mobil.com/en/lubricants/for-personal-vehicles/auto-care/vehicle-maintenance/how-to-do-a-leakdown-test

---

# 12. Leak-Down Safety

Compressed air can rotate the engine violently if the piston is not securely positioned at TDC compression.

Before applying air:

- Engine OFF.
- Transmission in `P`.
- Parking brake applied.
- Keep hands and tools away from belts and pulleys.
- Bring the test cylinder to **TDC on the compression stroke**.
- Verify both valves should be closed.
- Use a breaker bar and crank bolt only according to a proper service method.
- Expect the crankshaft to try to rotate when air is introduced.
- Never place fingers near a pulley or belt while the cylinder is pressurized.
- Never remove a hot radiator cap to look for bubbles.

If coolant observation is required, perform it only with the cooling system safely cooled and depressurized.

---

# 13. Finding TDC Compression

TDC occurs twice in a four-stroke cycle:

1. TDC between compression and power strokes, both valves closed.
2. TDC between exhaust and intake strokes, valve overlap may occur.

A leak-down test requires **TDC compression**.

Same-generation Hyundai valve-clearance service information sets No. 1 cylinder to TDC/compression by aligning the crank pulley timing mark and verifying the intake/exhaust CVVT sprocket marks.

Source:

- https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Maintenance/Tune-up%20and%20Engine%20Performance%20Checks/Valve%20Clearance/Testing%20and%20Inspection/

Do not confuse a timing reference with permission to force the engine backward or improvise against valvetrain load.

---

# 14. Leak-Down Listening Map

With the cylinder pressurized at TDC compression:

## Air heard at throttle body / intake manifold

Likely:

- Intake valve not sealing
- Intake valve burned, bent, sticking, or held off seat
- Valve-clearance issue
- Carbon or debris at seat

## Air heard at tailpipe / exhaust manifold

Likely:

- Exhaust valve not sealing
- Burned exhaust valve
- Bent/sticking valve
- Valve-clearance issue

## Air heard strongly at oil filler / crankcase / PCV path

Likely:

- Ring leakage
- Piston damage
- Cylinder-wall damage

Some ring leakage is normal. Compare cylinders and use the tester manufacturer's calibration method.

## Bubbles or pressure appearing in cooling system

Possible:

- Head-gasket leakage
- Cracked head
- Cracked block

Do not diagnose a head gasket from one clue alone.

## Air appearing in adjacent spark-plug hole

Possible:

- Head-gasket breach between cylinders
- Crack communicating between cylinders

---

# 15. Why This Guide Does Not Publish a Universal Leak-Down Percentage

Leak-down percentage depends on:

- Tester design
- Regulator calibration
- Supply pressure
- Orifice size
- Engine temperature
- Piston position
- Ring-gap orientation
- Cylinder size

Generic percentages such as “10% good, 20% bad” can be useful as broad tool-manufacturer guidance, but they are **not Hyundai 2014 specifications**.

Repository rule:

> Prefer cylinder-to-cylinder consistency, leak location, tester instructions, and manufacturer service limits over folklore thresholds.

---

# 16. Valve Clearance and Compression

A valve can be mechanically healthy yet fail to seal if clearance is incorrect.

`SERVICE-FAMILY — 2013 ACCENT 1.6 GDI`

Cold valve-clearance specification at approximately 20°C / 68°F:

| Valve | Clearance |
|---|---:|
| Intake | **0.17–0.23 mm / 0.0067–0.0091 in** |
| Exhaust | **0.22–0.28 mm / 0.0087–0.0110 in** |

Source:

- https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Maintenance/Tune-up%20and%20Engine%20Performance%20Checks/Valve%20Clearance/Testing%20and%20Inspection/

A clearance fault can contribute to:

- Poor valve seating
- Low compression
- Misfire
- Rough idle
- Hot-running cylinder problems
- Burned valve over time

Do not condemn a valve face before verifying the valvetrain can actually let the valve close.

---

# 17. Mechanical Timing and Compression

Incorrect cam timing can lower compression across multiple cylinders because the valves open and close at the wrong crankshaft positions.

If all cylinders are similarly low and test conditions are good, inspect:

- CKP/CMP correlation DTCs
- Actual versus target cam positions
- Timing-chain alignment
- Chain tensioner condition
- CVVT phaser position
- Mechanical timing marks

Cross-reference:

- `TIMING_CVVT.md`

Do not replace rings or rebuild the bottom end before checking shared valve-timing causes.

---

# 18. Spark-Plug Evidence

When removing plugs for compression testing, keep each plug identified by cylinder.

Compare:

- Color
- Wet fuel
- Oil fouling
- Heavy deposits
- Cracked insulator
- Electrode damage
- Unusual cleanliness

Possible clues:

### One unusually clean plug

Can suggest coolant or steam exposure, but is not proof by itself.

### One oily plug

Possible:

- Ring/cylinder problem
- Valve-seal problem
- PCV/oil-ingestion issue

### One fuel-wet plug

Possible:

- No spark
- Weak spark
- Injector leakage
- Low compression preventing reliable ignition

Plug evidence must be combined with compression, leak-down, ignition, and injector tests.

---

# 19. Borescope Inspection

`GENERAL DIAGNOSTIC PRACTICE`

A small borescope through the spark-plug hole can add useful visual evidence without engine disassembly.

Look for:

- Deep vertical cylinder-wall scoring
- Unusual piston-crown damage
- Foreign-object impact marks
- Heavy localized deposits
- Unusually steam-cleaned appearance
- Coolant residue
- Oil wetting

Limitations:

- A borescope cannot measure ring tension.
- It may not show the complete cylinder circumference.
- Carbon appearance varies greatly.
- Valve faces may be difficult to inspect through the spark-plug opening.

Do not condemn an engine solely from a dramatic-looking borescope image.

---

# 20. Blow-By and Crankcase Evidence

Combustion leakage past rings enters the crankcase as blow-by.

Possible evidence includes:

- Excessive crankcase pressure
- Strong pulsing from the oil-filler opening
- Oil pushed from seals
- High oil consumption
- Heavy vapor load through PCV

But PCV restriction can create similar crankcase-pressure symptoms.

Therefore:

```text
CRANKCASE PRESSURE
      ↓
CHECK PCV PATH
      ↓
THEN EVALUATE RING SEAL
```

Cross-reference:

- `PCV_CRANKCASE_VENTILATION.md`

---

# 21. Oil Consumption Is Not Automatically Ring Wear

Before blaming piston rings, inspect:

- External oil leaks
- PCV valve and hoses
- Valve-stem seals
- Oil level and fill history
- Oil viscosity
- Extended high-RPM operation
- Fuel dilution
- Cylinder leakage pattern

A ring diagnosis should be supported by evidence such as:

- Low dry compression
- Meaningful wet-test improvement
- Leak-down air into crankcase
- Borescope evidence
- Persistent oil consumption after external and PCV causes are excluded

---

# 22. Head-Gasket Diagnosis

Possible clues include:

- Compression low in adjacent cylinders
- Leak-down air entering cooling system
- Coolant loss without visible external leak
- Combustion gas in cooling system
- Persistent unexplained cooling-system pressure
- Coolant contamination in oil
- Oil contamination in coolant
- White exhaust vapor after full warm-up beyond normal condensation
- Overheating history

No single clue is definitive.

A head-gasket diagnosis should combine several independent findings.

### Important

Do not open a hot cooling system for diagnosis.

See:

- `COOLING_SYSTEM.md`
- `../diagnostics/OVERHEATING.md`

---

# 23. Cylinder Head and Block Evidence After Disassembly

`SERVICE-FAMILY — 2013 ACCENT 1.6 GDI`

Same-generation Hyundai overhaul information specifies cylinder-block deck flatness of:

- less than **0.05 mm / 0.0020 in** over the total gasket surface
- less than **0.02 mm / 0.0008 in** over a 100 mm × 100 mm area

It also specifies a nominal cylinder-bore diameter of approximately:

- **77.00–77.03 mm / 3.0315–3.0327 in**

Source:

- https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Engine%2C%20Cooling%20and%20Exhaust/Engine/Service%20and%20Repair/Overhaul/Repair%20Procedures/

These values matter **after** disassembly and precision measurement. They are not roadside diagnostic shortcuts.

---

# 24. Cylinder-Head Fastener Warning

Same-engine Hyundai service information specifies:

- New cylinder-head gasket
- New cylinder-head bolts
- Controlled tightening sequence
- Torque-plus-angle procedure

Do not reuse cylinder-head bolts merely because they visually appear good.

Cross-reference:

- `../specs/TORQUE_SPECS.md`

Service-family source:

- https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Engine%2C%20Cooling%20and%20Exhaust/Engine/Cylinder%20Head%20Assembly/Service%20and%20Repair/Repair%20Procedures/Part%202/

---

# 25. Diagnostic Workflow for a Misfire

```text
MISFIRE / ROUGH RUNNING
        ↓
PRESERVE DTC + FREEZE FRAME
        ↓
VERIFY BATTERY / VOLTAGE
        ↓
CHECK IGNITION
        ↓
CHECK INJECTOR / FUEL
        ↓
CHECK AIR / VACUUM
        ↓
STILL CYLINDER-SPECIFIC?
        ↓
DRY COMPRESSION
        ↓
LOW?
   ├─ NO → return to ignition/fuel/control diagnosis
   └─ YES
        ↓
WET COMPRESSION
        ↓
LEAK-DOWN
        ↓
LISTEN TO LEAK PATH
        ↓
BORESCOPE / VALVE CLEARANCE / TIMING AS NEEDED
        ↓
IDENTIFY ROOT CAUSE
        ↓
ONLY THEN PLAN INTERNAL REPAIR
```

---

# 26. Decision Matrix

| Finding | Most useful next step |
|---|---|
| All cylinders healthy and even | Return to ignition/fuel/air/control diagnosis |
| One cylinder low | Wet test + leak-down |
| Wet test raises pressure substantially | Investigate rings/bore |
| Wet test does not help | Investigate valves/head gasket |
| Air at intake during leak-down | Intake-valve sealing |
| Air at exhaust during leak-down | Exhaust-valve sealing |
| Strong crankcase air during leak-down | Rings/piston/bore |
| Cooling-system bubbles during leak-down | Head gasket/head/block |
| Two adjacent cylinders low | Investigate inter-cylinder head-gasket leak |
| All cylinders low | Verify cranking speed, throttle, gauge, mechanical timing |
| Compression normal but misfire persists | Ignition/injector/control fault more likely |
| New mechanical knock + compression loss | Stop running; internal damage possible |

---

# 27. Do Not Make These Diagnostic Errors

## Error: replacing coils because a P030x exists

A cylinder with poor compression can misfire with a perfectly good coil.

## Error: replacing an injector because its cylinder is weak

A mechanically weak cylinder may not burn a correct fuel dose.

## Error: condemning rings from low compression alone

Use wet testing and leak-down.

## Error: condemning a head gasket from white exhaust vapor alone

Cold-weather condensation can appear white.

## Error: testing with a weak battery

Low cranking speed can depress every result.

## Error: performing leak-down away from TDC compression

An open valve creates a false failure.

## Error: using a universal leak-down percentage as a Hyundai factory limit

No exact 2014 Hyundai leak-down percentage has been verified here.

---

# 28. Remote / Nomad Triage

For travel use, compression testing is appropriate when:

- A persistent cylinder misfire remains after basic ignition testing.
- Spark and injector function appear present.
- Power loss is persistent.
- One spark plug looks dramatically different from the others.
- Oil consumption becomes abnormal.
- A no-start cranks unusually fast or unevenly.
- A timing event is suspected.

A portable compression gauge is much easier to carry than a leak-down tester plus compressor.

Therefore a practical field sequence is:

```text
OBD DATA
  ↓
SPARK / COIL-SWAP TEST
  ↓
INJECTOR / FUEL EVIDENCE
  ↓
COMPRESSION GAUGE
  ↓
IF LOW → REACH SERVICE WHERE LEAK-DOWN / BORESCOPE IS AVAILABLE
```

Do not carry out major internal-engine disassembly at an unsafe roadside location.

---

# 29. Tool List

Useful tools include:

- OBD-II scanner with live data
- Compression tester with correct spark-plug adapter
- Fully charged battery or approved support charger
- Digital multimeter
- Spark-plug socket / 16 mm service-family reference
- Ignition-coil tools
- Torque wrench
- Cylinder leak-down tester
- Regulated compressed-air supply
- Breaker bar and correct crankshaft socket where appropriate
- Borescope
- Feeler gauges for valve-clearance inspection
- Cooling-system combustion-gas test kit when appropriate
- Notebook or digital log

Use tools according to their manufacturer instructions.

---

# 30. AI / RAG Rules

An AI using this file must follow these rules:

1. Never infer internal-engine failure from a DTC alone.
2. Never call a coil, injector, piston ring, valve, or head gasket failed without supporting tests.
3. Preserve cylinder-specific evidence.
4. Treat compression as a pattern across all cylinders.
5. Verify battery/cranking condition before interpreting low compression.
6. Treat 2013 compression specifications as **service-family**, not exact 2014 data.
7. Do not invent an exact 2014 leak-down percentage threshold.
8. Do not invent the physical location of cylinder 1 without an exact verified service diagram.
9. Recommend leak-down only at TDC compression.
10. Warn that compressed air can rotate the engine.
11. Never instruct opening a hot cooling system.
12. Cross-reference timing, PCV, ignition, GDI, cooling, and lubrication documents before recommending engine teardown.
13. Prefer reversible diagnostic tests before destructive disassembly.
14. `UNKNOWN` is safer than fabricated precision.

---

# 31. Mechanical Health Incident Log

```yaml
date:
odometer_miles:
engine_temperature:
battery_voltage_resting:
battery_voltage_cranking:
cranking_rpm:
dtc_stored: []
dtc_pending: []
freeze_frame_notes:

compression_test:
  cylinder_1_psi:
  cylinder_2_psi:
  cylinder_3_psi:
  cylinder_4_psi:
  throttle_condition:
  build_pattern_notes:

wet_test:
  cylinder:
  dry_psi:
  wet_psi:
  interpretation:

leakdown_test:
  cylinder_1_percent:
  cylinder_2_percent:
  cylinder_3_percent:
  cylinder_4_percent:
  tester_model:
  supply_pressure:
  intake_noise: false
  exhaust_noise: false
  crankcase_noise: false
  coolant_bubbles: false
  adjacent_cylinder_air: false

spark_plug_observations:
borescope_observations:
valve_clearance_checked: false
mechanical_timing_checked: false
pcv_checked: false
cooling_system_evidence:
oil_consumption_history:
root_cause:
repair_performed:
verification:
```

---

# 32. Source Notes

Primary service-family sources used in this document:

- 2013 Hyundai Accent 1.6 GDI compression test and specifications:
  https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Engine%2C%20Cooling%20and%20Exhaust/Engine/Tune-up%20and%20Engine%20Performance%20Checks/Compression%20Check/Testing%20and%20Inspection/

- 2013 Hyundai Accent valve-clearance inspection:
  https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Maintenance/Tune-up%20and%20Engine%20Performance%20Checks/Valve%20Clearance/Testing%20and%20Inspection/

- 2013 Hyundai Accent cylinder block / overhaul inspection:
  https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Engine%2C%20Cooling%20and%20Exhaust/Engine/Service%20and%20Repair/Overhaul/Repair%20Procedures/

- 2013 Hyundai Accent cylinder-head installation:
  https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Engine%2C%20Cooling%20and%20Exhaust/Engine/Cylinder%20Head%20Assembly/Service%20and%20Repair/Repair%20Procedures/Part%202/

General leak-down reference:

- Mobil engine leak-down overview:
  https://www.mobil.com/en/lubricants/for-personal-vehicles/auto-care/vehicle-maintenance/how-to-do-a-leakdown-test

---

# 33. Core Doctrine

```text
MISFIRE IS A SYMPTOM
        ↓
TEST SPARK
        ↓
TEST FUEL
        ↓
TEST AIR / CONTROL
        ↓
TEST COMPRESSION
        ↓
IF LOW, FIND WHERE PRESSURE ESCAPES
        ↓
RINGS? VALVES? GASKET? TIMING?
        ↓
REPAIR THE ROOT CAUSE
        ↓
VERIFY COMPRESSION + COMBUSTION
```

And the most important mechanical-health rule:

> **Do not rebuild an engine because a scanner named a cylinder. Make the cylinder prove it is mechanically sick.**
