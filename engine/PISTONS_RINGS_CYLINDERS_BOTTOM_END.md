# 2014 Hyundai Accent SE - Pistons, Rings, Cylinders & Bottom End

> **Purpose:** An offline-first mechanical-health guide for the 2014 Hyundai Accent SE 1.6 L Gamma GDI engine. This chapter focuses on the lower engine: pistons, rings, cylinder bores, connecting rods, rod bearings, crankshaft, main bearings, thrust control, oil-clearance diagnosis, mechanical noise, blow-by, oil consumption, and evidence-based decisions about teardown.
>
> **Core rule:** Do not condemn the bottom end from a noise, a misfire code, blue smoke, or one compression number. Build a chain of evidence.

---

## 1. Vehicle Scope

Primary vehicle:

- U.S.-market 2014 Hyundai Accent SE five-door
- 1.6 L Gamma DOHC GDI gasoline engine
- Four cylinders
- Timing chain
- Dual CVVT
- Six-speed automatic where applicable

This file uses three evidence levels:

- **VERIFIED - 2014 PARTS / OWNER DATA:** exact 2014 Accent hardware or owner-document information.
- **SERVICE-FAMILY - 2013 ACCENT 1.6 GDI:** Hyundai service information from the immediately adjacent model year using the same engine family. Useful and often directly applicable, but not silently promoted to exact 2014 factory specification.
- **GENERAL DIAGNOSTIC PRACTICE:** accepted mechanical-diagnostic reasoning that is not a Hyundai-specific specification.

When an exact 2014 workshop value has not been verified, it remains explicitly unresolved.

Related files:

- `COMPRESSION_LEAKDOWN_MECHANICAL_HEALTH.md`
- `CYLINDER_HEAD_HEAD_GASKET.md`
- `LUBRICATION_SYSTEM.md`
- `VALVE_CLEARANCE_VALVETRAIN.md`
- `TIMING_CVVT.md`
- `IGNITION.md`
- `GDI_FUEL_SYSTEM.md`
- `../diagnostics/MISFIRE.md`
- `../specs/TORQUE_SPECS.md`

---

# 2. What the 2014 Engine Hardware Actually Contains

The exact 2014 Accent OE catalog confirms the 1.6 L Gamma GDI lower-engine family includes:

- Four piston-and-pin assemblies
- Standard piston grades A, B, and C
- A piston-ring set
- Four connecting rods
- Four connecting-rod bearing pairs
- Five crankshaft main-bearing positions
- A center crankshaft bearing / thrust location
- A crankshaft assembly
- Eight connecting-rod bolts
- Ten main-bearing-cap bolts in the cylinder-block catalog
- Standard and undersize bearing selections

### Exact 2014 examples

Piston grades listed for 2014 include:

```text
23041-2B600  STD-A
23041-2B610  STD-B
23041-2B620  STD-C
```

The 2014 catalog also lists multiple color-coded connecting-rod and crankshaft main-bearing grades.

**Diagnostic consequence:** bearing and piston sizing is a measured fit system. Do not assume that every standard bearing shell or piston is dimensionally interchangeable merely because it fits the same engine family.

Sources:

- https://www.hyundaipartsdeal.com/parts-list/2014-hyundai-accent/engine/crankshaft_piston.html
- https://www.hyundaipartsdeal.com/parts-list/2014-hyundai-accent/engine/cylinder_block.html
- https://www.hyundaipartsdeal.com/oem-2014-hyundai-accent-piston.html

---

# 3. Lower-Engine Functional Map

```text
COMBUSTION PRESSURE
        ↓
      PISTON
        ↓
  PISTON PIN
        ↓
 CONNECTING ROD
        ↓
  ROD BEARING
        ↓
 CRANKSHAFT PIN
        ↓
    CRANKSHAFT
        ↓
  MAIN BEARINGS
        ↓
 CYLINDER BLOCK
```

At the cylinder wall:

```text
COMPRESSION RINGS
→ retain combustion pressure

OIL-CONTROL RING
→ meters oil on cylinder wall

CYLINDER BORE
→ guides piston and provides sealing surface
```

Failure in one part of this system can imitate failure somewhere else.

Examples:

- Worn rings can cause low compression, blow-by, and oil consumption.
- Tight or burned valves can also cause low compression.
- A head-gasket leak can also cause low compression.
- Fuel-washed cylinder walls can temporarily reduce sealing.
- A weak battery can lower cranking speed and make all cylinders read low.
- A rod-bearing problem can create a knock without causing low compression.

---

# 4. Compression Is the First Mechanical Screening Test

**SERVICE-FAMILY - 2013 Accent 1.6 GDI** Hyundai service data gives this reference procedure and values:

```text
Engine warm
Battery fully charged
Injectors disabled
Ignition coils disabled
All spark plugs removed
Throttle held wide open
Cranking speed: approximately 200-250 rpm

Standard compression:
177.79 psi / 1225.83 kPa

Minimum:
156.46 psi / 1078.73 kPa

Maximum cylinder-to-cylinder difference:
14 psi / 98 kPa
```

Source:

- https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Engine%2C%20Cooling%20and%20Exhaust/Engine/Tune-up%20and%20Engine%20Performance%20Checks/Compression%20Check/Testing%20and%20Inspection/

These are **service-family references**, not silently declared exact 2014 limits.

## Why relative compression matters

A group of four reasonably even cylinders can be more informative than one isolated number.

Patterns:

```text
ONE CYLINDER LOW
→ valve / ring / piston / local gasket / local timing issue

TWO ADJACENT CYLINDERS LOW
→ gasket bridge / head issue / localized valve or timing problem

ALL CYLINDERS LOW AND EVEN
→ test setup / cranking speed / throttle position / mechanical timing

ONE CYLINDER MUCH LOWER THAN REST
→ prioritize that cylinder for wet test + leak-down
```

---

# 5. Wet Compression Test

Hyundai's same-engine procedure explicitly uses a small amount of engine oil as a second-stage test when a cylinder reads low.

### Interpretation

```text
LOW COMPRESSION
      ↓
ADD SMALL AMOUNT OF OIL
      ↓
RETEST

PRESSURE RISES SIGNIFICANTLY
→ rings / bore sealing becomes more suspicious

PRESSURE STAYS LOW
→ valve seating / head gasket / timing becomes more suspicious
```

The oil temporarily improves sealing between piston rings and the cylinder wall.

### Important limitations

A wet test is evidence, not final proof.

Do not use excessive oil. Too much liquid in a cylinder can create misleading readings and can risk hydraulic lock.

Follow with leak-down testing before condemning pistons, rings, or bores.

---

# 6. Leak-Down: Where Is the Cylinder Losing Pressure?

Leak-down testing is one of the best ways to separate bottom-end leakage from top-end leakage.

With the cylinder at TDC on its compression stroke:

```text
AIR HEARD AT OIL FILLER / CRANKCASE
→ rings / piston / bore leakage

AIR HEARD AT THROTTLE / INTAKE
→ intake valve leakage

AIR HEARD AT TAILPIPE
→ exhaust valve leakage

BUBBLES IN COOLANT / RADIATOR
→ head gasket / crack / combustion-to-coolant path

AIR HEARD IN ADJACENT CYLINDER
→ possible gasket bridge or crack
```

Do not use a universal leak-down percentage as an Accent factory pass/fail specification unless the exact Hyundai procedure and tester convention are known.

Trend and leakage location matter greatly.

---

# 7. Blow-By

Some combustion gas always passes the rings. Excessive leakage into the crankcase is called excessive blow-by.

Possible clues:

- Strong pulsing from oil-filler opening
- Excessive crankcase pressure
- Oil pushed past seals or gaskets
- Oil mist in breather plumbing
- High oil consumption
- Low compression
- Leak-down strongly audible in crankcase

### Do not confuse PCV faults with ring failure

A restricted PCV system can create excessive crankcase pressure even when the rings are mechanically acceptable.

Before condemning rings:

1. Inspect PCV valve.
2. Inspect PCV hose.
3. Inspect fresh-air breather hose.
4. Check crankcase ventilation path.
5. Then evaluate compression and leak-down.

See `PCV_CRANKCASE_VENTILATION.md`.

---

# 8. Oil Consumption: Build Evidence Before Blaming Rings

Oil consumption can come from multiple routes:

```text
EXTERNAL
- oil pan
- drain plug
- filter
- timing cover
- crank seals
- rocker cover
- other seals / joints

INTERNAL
- oil-control rings
- compression rings / bore wear
- valve stem seals / guides
- PCV ingestion
- severe mechanical damage
```

## Oil-ring problems

An oil-control ring can become worn, stuck, carbon-packed, damaged, or unable to scrape oil effectively from the cylinder wall.

Possible pattern:

- Oil consumption
- Blue exhaust smoke under some conditions
- Oily or carbon-fouled plugs
- Compression that is still reasonably normal

**Important:** normal compression does not completely rule out oil-control-ring trouble.

The compression rings and oil-control ring do different jobs.

---

# 9. Exact Same-Engine Cylinder and Piston Reference Data

**SERVICE-FAMILY - 2013 Accent 1.6 GDI** Hyundai overhaul information gives:

### Cylinder bore diameter

```text
77.00-77.03 mm
3.0315-3.0327 in
```

### Piston outside diameter

Measured at Hyundai's specified location on the piston:

```text
76.97-77.00 mm
3.0303-3.0315 in
```

### Piston-to-cylinder clearance

```text
0.02-0.04 mm
0.0008-0.0016 in
```

Hyundai instructs technicians to visually inspect the cylinder for vertical scratches and states that deep scratches require block replacement in that service-family procedure.

Source:

- https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Engine%2C%20Cooling%20and%20Exhaust/Engine/Service%20and%20Repair/Overhaul/Repair%20Procedures/

Do not convert these adjacent-year values into exact 2014 machining instructions without confirming 2014 workshop data.

---

# 10. Piston Ring Side Clearance

**SERVICE-FAMILY - 2013 Accent 1.6 GDI:** 

```text
No. 1 compression ring:
0.04-0.08 mm
Limit 0.10 mm

No. 2 compression ring:
0.04-0.08 mm
Limit 0.10 mm

Oil ring:
0.02-0.06 mm
Limit 0.20 mm
```

Side clearance measures how the ring fits in its piston groove.

Excessive clearance can interfere with sealing and oil control.

Hyundai instructs replacing the piston if side clearance exceeds the specified service limit in this procedure.

---

# 11. Piston Ring End Gap

**SERVICE-FAMILY - 2013 Accent 1.6 GDI:**

```text
No. 1 ring:
0.14-0.28 mm
Limit 0.30 mm

No. 2 ring:
0.30-0.45 mm
Limit 0.50 mm

Oil ring:
0.20-0.40 mm
Limit 0.80 mm
```

Hyundai's method places the ring squarely in the bore and measures the end gap with a feeler gauge.

If end gap is excessive, the ring and bore both matter. A new ring cannot compensate for a cylinder that is outside usable geometry.

---

# 12. Piston Pins

**SERVICE-FAMILY - 2013 Accent 1.6 GDI:**

```text
Piston pin diameter:
18.001-18.006 mm

Piston-pin-to-piston clearance:
0.010-0.020 mm

Piston-pin-to-connecting-rod relationship:
Hyundai specifies an interference fit in the service-family procedure.
```

The same procedure uses a hydraulic press for piston/connecting-rod assembly.

This is not a hammer-and-socket field operation.

---

# 13. Connecting Rods and Rod Bearings

The connecting rod transfers piston force to the crankshaft.

The rod bearing rides on a pressurized oil film between the bearing shell and the crankshaft pin journal.

## Same-engine bearing oil clearance

**SERVICE-FAMILY - 2013 Accent 1.6 GDI:**

```text
Connecting-rod bearing oil clearance:
0.032-0.052 mm
0.0013-0.0020 in
```

Hyundai checks this with Plastigage during overhaul.

### Same-engine rod-cap bolt tightening

```text
17.7-21.6 N·m
13.0-15.9 lb-ft
then 88-92°
```

Hyundai explicitly says **do not reuse the connecting-rod bolts** in this procedure.

Source:

- https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Engine%2C%20Cooling%20and%20Exhaust/Engine/Service%20and%20Repair/Overhaul/Repair%20Procedures/

### Important

Bearing clearance is not adjusted by sanding, filing, scraping, or adding improvised shims.

Hyundai uses matched bearing grades.

The exact 2014 parts catalog confirms color-coded rod-bearing grades and undersize bearing sets.

---

# 14. Crankshaft and Main Bearings

The crankshaft is supported by five main-bearing positions in the 2014 cataloged architecture.

A pressurized oil film separates the crank journals from the bearing shells.

If that film fails, metal-to-metal contact can rapidly damage both bearing and crankshaft.

## Same-engine main-bearing oil clearance

**SERVICE-FAMILY - 2013 Accent 1.6 GDI:**

```text
Main bearings No. 1-5:
0.021-0.042 mm
0.0008-0.0017 in
```

## Crankshaft end play

**SERVICE-FAMILY - 2013 Accent 1.6 GDI:**

```text
Standard:
0.05-0.25 mm
0.0020-0.0098 in

Limit:
0.30 mm
0.0118 in
```

Hyundai's same-engine procedure places the thrust function at the center main-bearing location.

## Same-engine main-bearing-cap bolt tightening

```text
17.7-21.6 N·m
13.0-15.9 lb-ft
then 88-92°
```

A related Hyundai specification page states that the main-bearing-cap bolts should not be reused.

Sources:

- https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Engine%2C%20Cooling%20and%20Exhaust/Engine/Service%20and%20Repair/Overhaul/Repair%20Procedures/
- https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Specifications/Mechanical%20Specifications/Engine/Crankshaft%20Main%20Bearing/

---

# 15. Bearing Selection Is Measurement-Based

Hyundai's overhaul procedure uses identification marks on:

- Cylinder block
- Crankshaft
- Connecting rods
- Bearing shells

and then selects the appropriate bearing grade from a table.

The exact 2014 catalog reinforces this architecture by listing multiple standard bearing grades with color identifiers.

Therefore:

> **Do not order internal bearings by diameter guess, visual appearance, or generic engine name alone. Measure and identify the exact grade system.**

If crankshaft journals have been machined or replaced, the required bearing selection can change.

---

# 16. Rod Knock: Treat It as a Hypothesis, Not a Sound Effect

**GENERAL DIAGNOSTIC PRACTICE**

A connecting-rod bearing with excessive clearance can produce a deep metallic knock that often tracks engine speed and load.

But many other sounds can imitate it:

- Injector ticking
- High-pressure fuel-pump noise
- Valve-train noise
- Timing-chain or tensioner noise
- Accessory bearing noise
- Exhaust contact
- Loose heat shield
- Piston slap
- Detonation / combustion knock

Do not condemn a rod bearing from a phone recording.

### Evidence that increases concern for bottom-end bearing damage

- Oil-pressure warning or verified low mechanical oil pressure
- Metal flakes or bearing-colored debris in drained oil/filter
- Deep knock that changes predictably with load
- Known oil-starvation event
- Severe overheat combined with oil-pressure loss
- Excessive measured bearing clearance during teardown

### Stop condition

A new deep knock together with an oil-pressure warning, metallic debris, or major mechanical vibration is a **STOP ENGINE / TOW** condition.

Do not intentionally keep loading the engine to make a suspected bearing knock louder.

---

# 17. Main-Bearing Failure Patterns

Possible signs include:

- Low oil pressure
- Deep lower-engine rumble or knock
- Crankshaft end-play problems
- Metal contamination
- Severe vibration after advanced damage

Main-bearing wear can reduce oil pressure throughout the engine because excessive clearance becomes an internal oil leak.

However, low oil pressure can also come from:

- Low oil level
- Wrong viscosity
- Oil aeration
- Pickup restriction
- Oil pump problem
- Pressure-relief problem
- Excessive rod-bearing clearance
- Excessive main-bearing clearance
- Severe internal leakage elsewhere

See `LUBRICATION_SYSTEM.md`.

---

# 18. Piston Slap vs Bearing Knock

**GENERAL DIAGNOSTIC PRACTICE**

These are pattern clues only.

## Piston slap pattern

Often described as:

- Hollow or skirt-like mechanical knock
- More noticeable cold
- May reduce as piston and cylinder warm and expand

## Rod-bearing knock pattern

Often described as:

- Deeper metallic knock
- Closely follows engine speed
- Can become more pronounced under load or certain transitions

## Valve-train / injector ticking

Often:

- Higher frequency
- More obviously localized to cylinder head / upper engine

### Critical rule

```text
SOUND CHARACTER
      ≠
PROOF
```

Use a stethoscope, oil-pressure test, cylinder-balance evidence, oil/filter inspection, compression/leak-down, and known operating history before reaching an internal-engine conclusion.

---

# 19. Metal in Oil

Metallic debris is important evidence, but appearance alone may not identify the source with certainty.

Possible sources include:

- Bearings
- Crankshaft
- Camshafts / valvetrain
- Timing system
- Oil pump
- Cylinder / piston damage
- Normal break-in residue on a newly rebuilt engine

## Useful inspection procedure

When serious internal damage is suspected:

1. Drain oil into a clean pan.
2. Inspect oil in strong light.
3. Cut open the oil filter using a proper filter cutter if available.
4. Spread filter media and inspect for metallic particles.
5. Record color, magnetic response, amount, and distribution.
6. Do not run the engine repeatedly merely to generate more evidence.

### Magnet limitations

Not all bearing materials are strongly magnetic.

A clean magnet does not prove the bearings are healthy.

---

# 20. Cylinder Scoring

Hyundai's same-engine overhaul instructions specifically tell technicians to inspect bores for vertical scratches.

Potential causes of scoring include:

- Dirt ingestion
- Oil starvation
- Broken ring
- Foreign material
- Overheating
- Piston damage
- Severe fuel wash

Possible signs:

- Low compression
- High blow-by
- Oil consumption
- Visible vertical scoring by borescope
- Abnormal piston noise

A borescope is useful, but light reflections, carbon patterns, and harmless marks can be misleading.

If the diagnosis matters enough to justify an engine rebuild, dimensional measurement is stronger evidence than a photograph alone.

---

# 21. Borescope Use

A borescope through the spark-plug hole can inspect:

- Piston crown
- Portions of cylinder wall
- Unusual liquid in the cylinder
- Heavy localized deposits
- Severe vertical scoring
- Signs of foreign-object damage
- Unusual steam-cleaning pattern when compared across cylinders

### Best practice

Photograph all four cylinders under similar piston positions and lighting.

Comparison is more useful than staring at one dramatic-looking carbon patch.

A borescope does not replace:

- Compression
- Leak-down
- Bore-gauge measurements
- Oil-pressure testing

---

# 22. Fuel Wash and Cylinder Sealing

A severely rich or non-start condition can wash the oil film from cylinder walls.

Possible consequences:

- Temporarily lower compression
- Increased ring leakage
- Fuel dilution of engine oil
- Accelerated wear if prolonged

If the oil smells strongly of gasoline or the level has risen unexpectedly after repeated failed starts, investigate fuel dilution.

Do not continue repeated long cranking attempts without diagnosing the root cause.

See `GDI_FUEL_SYSTEM.md` and `CRANK_NO_START.md`.

---

# 23. Overheating and the Bottom End

Severe overheating can affect more than the head gasket.

Potential consequences include:

- Piston scuffing
- Cylinder-wall damage
- Oil-film breakdown
- Bearing damage
- Distorted sealing surfaces
- Ring damage
- Oil degradation

After a severe overheat event, do not stop diagnostics after proving that the head gasket survived.

Check:

- Oil condition
- Oil pressure if symptoms justify it
- Compression balance
- Leak-down if abnormal
- Mechanical noise
- Coolant contamination

---

# 24. Oil Starvation and Bearing Damage

The crankshaft and rod bearings rely on continuous pressurized lubrication.

Possible oil-starvation causes:

- Low oil level
- Damaged oil pan
- Pickup problem
- Oil-pump failure
- Foamed/aerated oil
- Severe contamination
- Incorrect assembly after engine work

### Immediate rule

If the oil-pressure warning remains illuminated while the engine is running:

```text
STOP ENGINE
      ↓
VERIFY LEVEL
      ↓
IF LEVEL LOW:
correct level + identify leak/consumption
      ↓
IF LEVEL NORMAL OR WARNING RETURNS:
DO NOT KEEP RUNNING
      ↓
MECHANICAL PRESSURE TEST / TOW
```

A full dipstick does not prove the engine has pressure.

---

# 25. Oil Pressure vs Bearing Clearance

Oil pressure is created by the interaction of pump flow, oil viscosity, temperature, and restriction throughout the lubrication system.

Excessive bearing clearance provides an easier escape path for oil.

Therefore worn rod or main bearings can contribute to low pressure, especially hot at idle.

But:

```text
LOW OIL PRESSURE
      ≠
AUTOMATICALLY BAD BEARINGS
```

Check the whole lubrication system.

---

# 26. Exact Same-Engine Overhaul Rules Worth Preserving

**SERVICE-FAMILY - 2013 Accent 1.6 GDI:**

Hyundai's lower-engine overhaul procedure includes these important rules:

- Do not turn the crankshaft while Plastigage is installed.
- Do not file, shim, or scrape bearing shells or caps to alter clearance.
- Use bearing grade selection rather than improvised clearance correction.
- Clean identification marks with solvent/detergent rather than damaging them with abrasive tools.
- Lubricate sliding and rotating surfaces with fresh engine oil during assembly.
- Replace gaskets, O-rings, and oil seals during overhaul as directed.
- Orient piston and connecting-rod marks correctly toward the timing-chain side.
- Install compression-ring markings facing upward as directed by the service procedure.

Source:

- https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Engine%2C%20Cooling%20and%20Exhaust/Engine/Service%20and%20Repair/Overhaul/Repair%20Procedures/

---

# 27. Do Not Perform a Bottom-End Tear-Down as a First Test

Before removing the oil pan, cylinder head, pistons, or crankshaft, collect as much non-invasive evidence as practical.

Recommended progression:

```text
SYMPTOM
  ↓
OIL LEVEL + CONDITION
  ↓
OBD / MISFIRE EVIDENCE
  ↓
COMPRESSION
  ↓
WET COMPRESSION IF LOW
  ↓
LEAK-DOWN
  ↓
BORESCOPE
  ↓
MECHANICAL OIL PRESSURE IF INDICATED
  ↓
OIL / FILTER DEBRIS INSPECTION
  ↓
ONLY THEN CONSIDER TEARDOWN
```

Teardown destroys some evidence and creates opportunities for contamination and assembly error.

---

# 28. Symptom Matrix

| Symptom | Higher-priority possibilities | Useful separating tests |
|---|---|---|
| One-cylinder misfire | spark, injector, valve, ring/bore | coil swap, injector test, compression, leak-down |
| Low compression that improves wet | rings/bore | leak-down, borescope |
| Low compression unchanged wet | valves/gasket/timing | leak-down, timing verification |
| Oil consumption with normal compression | PCV, oil-control rings, valve seals, external leaks | leak inspection, PCV test, plug/borescope evidence |
| Strong crankcase leakage on leak-down | rings/piston/bore | wet compression, borescope, bore measurement |
| Deep knock + low oil pressure | bearing/oil-system damage | stop engine, mechanical pressure, filter inspection |
| Cold knock that fades warm | piston clearance or other temperature-sensitive noise | localization, oil pressure, history, further testing |
| Metal in oil | internal wear/damage | filter inspection, magnetic response, oil pressure, teardown if severe |
| All cylinders low | cranking/test setup, throttle, timing | battery/cranking rpm, repeat test, timing verification |

This table is diagnostic guidance, not a replacement for testing.

---

# 29. Stop-Driving Conditions

**STOP ENGINE / TOW** when any of these occur:

- Oil-pressure warning remains on with engine running.
- New deep mechanical knock appears with low oil pressure.
- Significant metallic debris is found with active mechanical noise.
- Engine partially or fully seizes.
- Severe vibration suggests internal mechanical failure.
- Oil rapidly disappears or pours from the engine.
- Severe overheat is followed by new lower-engine knocking.
- Connecting-rod or piston failure is suspected.

A damaged crankshaft can turn a repairable engine into a destroyed block very quickly.

---

# 30. Nomad / Remote-Road Considerations

For remote travel, the best bottom-end repair is prevention.

Before long remote stretches:

- Check oil level.
- Look under vehicle for fresh leakage.
- Inspect oil pan for impact damage.
- Pay attention to new ticking, knocking, or rumbling.
- Keep correct engine oil available for top-off.
- Record oil consumption over distance.
- Treat the oil-pressure warning as an emergency.

After a significant underbody strike:

1. Stop safely.
2. Inspect oil pan.
3. Look for fresh oil.
4. Recheck oil level.
5. Start only if there is no evidence of dangerous leakage or pan damage.
6. Shut down immediately if oil-pressure warning persists.

The Accent has limited ground clearance. Do not use an oil pan as a skid plate.

---

# 31. AI / RAG Diagnostic Rules

An AI using this repository should follow these rules:

1. **Do not diagnose rod bearings from sound description alone.**
2. **Do not diagnose worn rings from oil consumption alone.**
3. **Do not diagnose rings from low compression without considering valves, timing, gasket, and test setup.**
4. **A wet-test improvement increases suspicion of rings/bore but does not finish the diagnosis.**
5. **Crankcase air during leak-down supports ring/piston/bore leakage.**
6. **Normal compression does not fully exclude oil-control-ring problems.**
7. **Low oil pressure is a system problem until the failed subsystem is isolated.**
8. **A full dipstick does not prove adequate oil pressure.**
9. **If an oil-pressure warning accompanies mechanical knock, prioritize engine shutdown over further running tests.**
10. **2013 service-family measurements must remain labeled as service-family until exact 2014 workshop data verifies them.**
11. **Internal bearing selection must respect grade codes and actual measurement.**
12. **Never recommend filing, sanding, shimming, or scraping a bearing to create clearance.**
13. **Do not reuse torque-to-yield or explicitly non-reusable internal fasteners where Hyundai service information says replacement is required.**
14. **Prefer evidence chains over single-symptom conclusions.**

---

# 32. Diagnostic Decision Tree

```text
MISFIRE / OIL USE / BLOW-BY / KNOCK
                ↓
       ANY OIL-PRESSURE WARNING?
          ├─ YES → STOP ENGINE
          │          ↓
          │     VERIFY LEVEL
          │          ↓
          │     MECHANICAL PRESSURE TEST
          │
          └─ NO
                ↓
       CLASSIFY THE COMPLAINT
                ↓
    COMPRESSION / LEAK-DOWN IF NEEDED
                ↓
       BOTTOM-END LEAKAGE EVIDENCE?
          ├─ NO → pursue ignition / fuel /
          │       valve / gasket / timing / PCV
          │
          └─ YES
                ↓
       BORESCOPE + OIL/FILTER INSPECTION
                ↓
       OIL PRESSURE IF INDICATED
                ↓
       STRONG INTERNAL EVIDENCE?
          ├─ NO → monitor / continue diagnosis
          └─ YES → plan measured teardown
```

---

# 33. Measurement Record Template

```yaml
bottom_end_diagnostic:
  date:
  odometer_miles:
  engine_temp_state:
  battery_voltage_before_test:
  cranking_rpm_if_known:

  oil:
    level:
    viscosity:
    age_miles:
    fuel_smell: false
    coolant_contamination_seen: false
    metallic_debris_seen: false

  compression_psi:
    cyl_1:
    cyl_2:
    cyl_3:
    cyl_4:

  wet_compression_psi:
    cyl_1:
    cyl_2:
    cyl_3:
    cyl_4:

  leakdown:
    test_pressure:
    cyl_1_percent:
    cyl_1_leak_location:
    cyl_2_percent:
    cyl_2_leak_location:
    cyl_3_percent:
    cyl_3_leak_location:
    cyl_4_percent:
    cyl_4_leak_location:

  oil_pressure:
    measured: false
    coolant_temp:
    idle_pressure:
    rpm_pressure:
    rpm_value:

  noise:
    present: false
    cold_only: false
    hot_only: false
    load_sensitive: false
    rpm_sensitive: false
    suspected_location:

  borescope:
    performed: false
    cyl_1:
    cyl_2:
    cyl_3:
    cyl_4:

  conclusion:
    confidence:
    next_test:
```

---

# 34. Verified / Supporting Sources

## Exact 2014 parts catalog

- Crankshaft and piston:
  https://www.hyundaipartsdeal.com/parts-list/2014-hyundai-accent/engine/crankshaft_piston.html

- Cylinder block:
  https://www.hyundaipartsdeal.com/parts-list/2014-hyundai-accent/engine/cylinder_block.html

- 2014 piston listings:
  https://www.hyundaipartsdeal.com/oem-2014-hyundai-accent-piston.html

## Same-engine / adjacent-model-year Hyundai service-family data

- 2013 Accent 1.6 GDI overhaul procedure:
  https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Engine%2C%20Cooling%20and%20Exhaust/Engine/Service%20and%20Repair/Overhaul/Repair%20Procedures/

- 2013 Accent compression test:
  https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Engine%2C%20Cooling%20and%20Exhaust/Engine/Tune-up%20and%20Engine%20Performance%20Checks/Compression%20Check/Testing%20and%20Inspection/

- 2013 Accent crankshaft main-bearing specification page:
  https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Specifications/Mechanical%20Specifications/Engine/Crankshaft%20Main%20Bearing/

---

# 35. Repository Principle

```text
NOISE IS A CLUE
SMOKE IS A CLUE
A DTC IS A CLUE
LOW COMPRESSION IS A CLUE
METAL IS EVIDENCE
MEASUREMENT IS STRONGER EVIDENCE

BUILD THE CASE
BEFORE OPENING THE ENGINE
```

A bottom-end rebuild is one of the most invasive decisions that can be made on an engine. The standard for evidence should rise with the cost and invasiveness of the repair.
