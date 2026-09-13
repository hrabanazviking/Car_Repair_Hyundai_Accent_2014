# 2014 Hyundai Accent SE - Cylinder Head & Head Gasket

> **Purpose:** A practical, evidence-first diagnostic and service reference for suspected cylinder-head, head-gasket, combustion-to-coolant, coolant-to-cylinder, and overheating-related mechanical faults on the U.S.-market 2014 Hyundai Accent SE 1.6 L GDI engine.
>
> **Core rule:** Do not diagnose a head gasket from one symptom. Build a case from multiple independent tests.

---

## 1. Vehicle Scope

Primary vehicle:

- U.S.-market 2014 Hyundai Accent SE five-door
- 1.6 L Gamma GDI DOHC inline-four
- Dual CVVT
- Timing chain
- Aluminum cylinder head and aluminum engine architecture

Related repository files:

- `ENGINE_OVERVIEW.md`
- `COOLING_SYSTEM.md`
- `OVERHEATING.md`
- `COMPRESSION_LEAKDOWN_MECHANICAL_HEALTH.md`
- `VALVE_CLEARANCE_VALVETRAIN.md`
- `TIMING_CVVT.md`
- `LUBRICATION_SYSTEM.md`
- `GDI_FUEL_SYSTEM.md`
- `EXHAUST_CATALYST_O2_SENSORS.md`

---

# 2. Evidence and Confidence Tags

This document uses the repository's normal evidence model.

- **VERIFIED - 2014 PARTS DATA** - exact 2014 Accent catalog evidence
- **VERIFIED - 2014 OWNER MANUAL** - exact 2014 Hyundai owner information
- **SERVICE-FAMILY - 2013 ACCENT 1.6 GDI** - adjacent-year same-generation, same-engine Hyundai service data
- **SERVICE-FAMILY - 2012 ACCENT 1.6 GDI** - adjacent-year same-generation, same-engine Hyundai service data
- **GENERAL DIAGNOSTIC PRACTICE** - standard automotive diagnostic method, not a Hyundai-specific specification
- **UNKNOWN** - intentionally unresolved rather than guessed

A service-family value is useful diagnostic evidence, but it is not silently promoted into an exact 2014 factory specification.

---

# 3. Exact 2014 Hardware Anchors

Hyundai parts data for the 2014 Accent 1.6 L Gamma GDI confirms:

- Cylinder head assembly: `22100-2B701`
- Cylinder-head gasket: `22311-2B003`, superseded by `22311-2B004`
- Cylinder-head bolts: `22321-2B700`
- Cylinder-head bolt quantity: 10
- Cylinder-head bolt washers: `22322-2B700`, superseded by `22322-2B701`

The catalog identifies the 2014 cylinder-head gasket as a dedicated 1.6 L Gamma DOHC-GDI part.

Sources:

- https://www.hyundaipartsdeal.com/parts-list/2014-hyundai-accent/engine/cylinder_head.html
- https://www.hyundaipartsdeal.com/oem-2014-hyundai-accent-cylinder_head_gasket.html

---

# 4. What the Head Gasket Actually Does

The head gasket must seal several different environments at once:

```text
COMBUSTION PRESSURE
      |
      | sealed from
      v
COOLANT PASSAGES
      |
      | sealed from
      v
ENGINE-OIL PASSAGES
      |
      | sealed from
      v
OUTSIDE OF ENGINE
```

A head-gasket failure can therefore occur in several different ways.

## Common failure paths

1. Combustion chamber -> cooling system
2. Cooling system -> combustion chamber
3. Oil passage -> cooling system
4. Coolant passage -> oil system
5. Combustion chamber -> adjacent combustion chamber
6. Oil or coolant -> outside of engine

Not every failed gasket produces mayonnaise under the oil cap, white smoke, or visible coolant in the oil.

---

# 5. Major Fault Patterns

## A. Combustion gas entering coolant

Possible clues:

- Cooling system becomes pressurized unusually fast from a cold start
- Repeated coolant push-out into reservoir
- Upper radiator hose becomes very firm unusually early
- Repeated unexplained coolant loss
- Bubbles or gas activity in coolant under controlled test conditions
- Overheating despite otherwise functional fan, thermostat, radiator, and coolant level
- Positive combustion-gas chemical test
- Leak-down produces bubbles in cooling system

This is one of the stronger head-gasket patterns when several of these occur together.

---

## B. Coolant entering a cylinder

Possible clues:

- Cold-start misfire that improves after several seconds
- One spark plug unusually clean compared with the others
- Coolant loss with no obvious external leak
- Sweet-smelling persistent exhaust vapor after full warm-up
- Cylinder with visible liquid or an unusually steam-cleaned piston crown during borescope inspection
- Cooling-system pressure drops while one cylinder accumulates coolant
- Rough restart after a hot soak

A small internal leak may not contaminate engine oil.

---

## C. Leakage between adjacent cylinders

Possible clues:

- Two neighboring cylinders show similarly low compression
- Ignition and injector tests do not move the misfire
- Leak-down indicates communication between adjacent cylinders
- Mechanical timing is correct
- Valve sealing appears normal

This pattern raises suspicion for a gasket breach or a crack between cylinders.

---

## D. Coolant entering oil

Possible clues:

- Oil level rising without oil being added
- Tan, creamy, or emulsified oil throughout the crankcase
- Coolant level falling
- Coolant contamination evident on drained oil

### Important caution

A small amount of beige emulsion under the oil-filler cap can also result from condensation, especially with repeated short trips and cold weather.

Do not diagnose a head gasket solely from cap residue.

---

## E. Oil entering coolant

Possible clues:

- Oily film or sludge in coolant
- Coolant reservoir contamination
- Cooling hoses becoming oil-softened over time

Oil in coolant can have causes other than a head gasket, depending on engine configuration and any oil-to-coolant heat exchangers present. Verify the actual source before teardown.

---

# 6. What Is NOT Proof of a Head-Gasket Failure

The following are clues only:

- White vapor on a cold morning
- Water dripping from the exhaust during warm-up
- Milky residue only under the oil cap
- One overheating event
- One low compression reading taken with a weak battery
- One cylinder misfire code
- Coolant loss without first checking for external leaks
- Bubbles caused by trapped air immediately after cooling-system service
- A hard upper radiator hose after the engine is fully hot
- A failed thermostat
- A failed cooling fan
- A leaking radiator cap
- A loose hose clamp

The cooling system naturally develops pressure when hot.

---

# 7. Stop-Driving Conditions

Stop the engine and do not continue driving if any of the following occurs:

- Steam is escaping from under the hood
- Coolant is actively pouring or spraying from the vehicle
- Coolant temperature is dangerously high
- Repeated overheating continues after cooldown
- Engine oil is heavily contaminated with coolant
- A cylinder is suspected of containing enough liquid to hydro-lock
- Severe misfire occurs together with coolant loss
- Combustion pressure is forcing coolant out rapidly
- A severe mechanical knock begins after overheating

The exact 2014 Hyundai owner manual instructs the driver to stop if coolant is leaking out or if the water-pump drive belt is broken, and warns never to remove the radiator cap while hot.

Source:

- https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/?srch=overheating

---

# 8. Diagnostic Order

Use the least invasive tests first.

```text
SUSPECT HEAD / GASKET
        |
        v
VERIFY COOLANT LEVEL + EXTERNAL LEAKS
        |
        v
VERIFY FAN / BELT / THERMOSTAT / RADIATOR BASICS
        |
        v
COOLING-SYSTEM PRESSURE TEST
        |
        v
SCAN DATA + MISFIRE PATTERN
        |
        v
COMPRESSION TEST
        |
        v
LEAK-DOWN TEST
        |
        v
COMBUSTION-GAS TEST
        |
        v
BORESCOPE / COLD-START EVIDENCE
        |
        v
MECHANICAL TIMING / VALVE CLEARANCE
        |
        v
ONLY THEN CONSIDER TEARDOWN
```

---

# 9. First Step: Rule Out External Coolant Loss

Before blaming the head gasket, inspect:

- Radiator
- Radiator cap and sealing surfaces
- Upper and lower radiator hoses
- Hose clamps
- Thermostat housing / water-temperature-control assembly
- Water pump area
- Heater hoses
- Heater core clues
- Reservoir hose
- Cylinder-head external coolant joints
- Coolant residue under engine
- Dried coolant tracks

A small external leak can evaporate on a hot engine and leave only dried residue.

Use a bright light and inspect when cold and again after a controlled pressure test.

---

# 10. Cooling-System Pressure Test

**SERVICE-FAMILY - 2012 ACCENT 1.6 GDI**

Hyundai service information specifies a cooling-system pressure test of approximately:

```text
93.16 - 122.58 kPa
0.95 - 1.25 kg/cm²
13.51 - 17.78 psi
```

Procedure summary:

1. Allow engine to cool completely.
2. Remove the radiator cap only when safe.
3. Fill coolant appropriately.
4. Install a cooling-system pressure tester.
5. Pressurize only to the specified test range.
6. Inspect for leaks and pressure loss.
7. Check for engine oil in coolant and coolant in engine oil.

Source:

- https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Engine%2C%20Cooling%20and%20Exhaust/Cooling%20System/Radiator/Testing%20and%20Inspection/

### Interpretation

A pressure drop means the system is losing pressure somewhere. It does not by itself identify the head gasket.

If no external leak appears, investigate internal leakage.

---

# 11. Radiator-Cap Test

**SERVICE-FAMILY - 2012 ACCENT 1.6 GDI**

Hyundai uses the same approximate pressure range for radiator-cap testing:

```text
93.16 - 122.58 kPa
13.51 - 17.78 psi
```

A leaking cap can cause coolant loss or boiling behavior that imitates a deeper engine problem.

Source:

- https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Engine%2C%20Cooling%20and%20Exhaust/Cooling%20System/Radiator%20Cap/Testing%20and%20Inspection/

---

# 12. Compression Test

See `COMPRESSION_LEAKDOWN_MECHANICAL_HEALTH.md` for the full procedure.

**SERVICE-FAMILY - 2013 ACCENT 1.6 GDI**

Hyundai gives:

```text
Standard:
177.79 psi / 1225.83 kPa

Minimum:
156.46 psi / 1078.73 kPa

Maximum difference between cylinders:
14 psi / 98 kPa

Reference cranking speed:
200 - 250 rpm
```

The test is performed with a fully charged battery, warm engine, injectors and ignition disabled, spark plugs removed, and throttle wide open.

Source:

- https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Engine%2C%20Cooling%20and%20Exhaust/Engine/Tune-up%20and%20Engine%20Performance%20Checks/Compression%20Check/Testing%20and%20Inspection/

### Head-gasket patterns

#### Two adjacent low cylinders

This pattern can suggest:

- Gasket leakage between cylinders
- Head crack
- Timing issue
- Valve problem affecting both cylinders

Do not skip leak-down.

#### One low cylinder

Possible causes include:

- Burned or leaking valve
- Tight valve clearance
- Ring or bore damage
- Head gasket at that cylinder
- Crack

#### All cylinders low

Look first at:

- Low cranking speed
- Battery state
- Test procedure
- Throttle position
- Mechanical timing
- Broad engine wear

A head gasket is not automatically the leading cause.

---

# 13. Wet Compression Test

**SERVICE-FAMILY - 2013 ACCENT 1.6 GDI**

Hyundai instructs that if compression is low, add a small amount of oil to the affected cylinder and repeat the test.

Interpretation:

```text
COMPRESSION RISES SIGNIFICANTLY
        -> rings / cylinder bore more likely

COMPRESSION STAYS LOW
        -> valve leakage / gasket leakage / other top-end issue more likely
```

This is a directional test, not final proof.

Source:

- https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Engine%2C%20Cooling%20and%20Exhaust/Engine/Tune-up%20and%20Engine%20Performance%20Checks/Compression%20Check/Testing%20and%20Inspection/

---

# 14. Cylinder Leak-Down Test

**GENERAL DIAGNOSTIC PRACTICE**

Leak-down testing is one of the strongest ways to determine where a cylinder is losing pressure.

The piston must be positioned at TDC on the compression stroke so both valves are closed.

Listen and observe where the test air escapes.

| Evidence | Likely leakage path |
|---|---|
| Air at intake | Intake valve |
| Air at tailpipe | Exhaust valve |
| Air at oil fill / crankcase | Rings, piston, bore |
| Bubbles in cooling system | Combustion chamber to coolant path |
| Air entering neighboring cylinder | Inter-cylinder gasket breach or crack |

### Strong head-gasket evidence

Leak-down air producing repeatable bubbles in the cooling system is much stronger evidence than white exhaust vapor alone.

### Safety

Do not remove a hot radiator cap to watch for bubbles.

---

# 15. Combustion-Gas Chemical Test

**GENERAL DIAGNOSTIC PRACTICE**

A combustion-leak tester samples gas above the coolant and uses chemical fluid that reacts to combustion gases.

A positive test can support a combustion-to-coolant leak diagnosis.

### Limitations

A negative test does not completely rule out:

- Very small intermittent leaks
- Leaks that appear only under load
- Leaks that occur only at high temperature
- Coolant-to-cylinder leaks without major combustion-gas transfer

Use this test as part of a body of evidence.

---

# 16. Cold-Start Misfire as a Clue

A small coolant leak into one cylinder can produce a distinctive pattern:

```text
VEHICLE SITS
     ↓
SMALL AMOUNT OF COOLANT ENTERS CYLINDER
     ↓
COLD START
     ↓
ONE CYLINDER MISFIRES
     ↓
COOLANT CLEARS
     ↓
MISFIRE IMPROVES
```

Supporting evidence can include:

- Repeated same-cylinder cold misfire
- Falling coolant level
- Unusually clean plug on that cylinder
- Borescope evidence
- Positive pressure or leak-down test

Do not confuse this with an injector leaking fuel overnight, weak ignition, valve-clearance issues, or carbon-related cold-start behavior.

---

# 17. Borescope Inspection

**GENERAL DIAGNOSTIC PRACTICE**

A borescope through the spark-plug hole can reveal:

- Coolant droplets
- Unusually clean piston crown
- Washed combustion chamber
- Rust-colored deposits
- Piston damage
- Valve damage where visible
- Cylinder-wall scoring

### Compare cylinders

The value is often in comparison.

If three pistons have similar carbon deposits and one appears dramatically steam-cleaned, that difference matters.

It is not automatic proof of a head gasket, but it strengthens the case when paired with coolant loss and pressure/leak-down evidence.

---

# 18. Spark-Plug Evidence

Remove and compare all four spark plugs.

Look for:

- One plug unusually white or clean
- Deposits unlike neighboring cylinders
- Wetness after an overnight sit
- Coolant-like residue
- Oil fouling
- Fuel fouling

Do not diagnose from plug color alone.

Use plug evidence together with compression, leak-down, coolant loss, and borescope findings.

---

# 19. Oil and Coolant Cross-Contamination

Check both fluids.

## Engine oil

Look for:

- Rising oil level
- Full-crankcase emulsion
- Coolant droplets
- Abnormal viscosity

## Coolant

Look for:

- Oil film
- Sludge
- Brown contamination not explained by old coolant/rust

### Important distinction

```text
MILKY FILLER CAP ONLY
        ≠
CONFIRMED COOLANT IN CRANKCASE
```

Cold-weather condensation can create cap residue.

Drain-oil evidence is much stronger.

---

# 20. White Exhaust Vapor

Water vapor from a gasoline engine is normal during warm-up, especially in cool or humid weather.

Concern increases when vapor is:

- Dense
- Persistent after full warm-up
- Accompanied by coolant loss
- Sweet-smelling
- Associated with cold-start misfire
- Associated with cooling-system pressure abnormalities

Again:

```text
WHITE VAPOR
    ≠
HEAD GASKET PROOF
```

---

# 21. Overheating and Cylinder-Head Damage

A severe overheat can damage:

- Cylinder-head flatness
- Head gasket sealing
- Valve seats
- Valve guides
- Plastic cooling-system components
- Oil condition
- Catalyst if misfire follows

After a serious overheat, do not merely refill coolant and assume the event is finished.

Investigate why it overheated and whether the engine sustained secondary damage.

---

# 22. Cylinder-Head Flatness

**SERVICE-FAMILY - 2012 ACCENT 1.6 GDI**

Hyundai specifies cylinder-head gasket-surface flatness as:

```text
Total area:
less than 0.05 mm / 0.0020 in

Within a 100 mm x 100 mm section:
less than 0.02 mm / 0.0008 in
```

Hyundai also instructs inspection of the combustion chambers, intake ports, exhaust ports, and block-contact surface for cracks. If cracked, the service procedure calls for cylinder-head replacement.

Source:

- https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Engine%2C%20Cooling%20and%20Exhaust/Engine/Cylinder%20Head%20Assembly/Service%20and%20Repair/Repair%20Procedures/Part%201%200F%202/

### Do not guess machining limits

Exact allowable material-removal/resurfacing limits for the 2014 head are **UNKNOWN** in this repository until a directly verified service source is obtained.

A machine shop must evaluate:

- Flatness
- Surface finish
- Crack integrity
- Valve-seat condition
- Cam journal alignment
- Minimum head dimensions if specified by Hyundai

---

# 23. Cylinder-Block Deck Flatness

**SERVICE-FAMILY - 2013 ACCENT 1.6 GDI**

Hyundai gives the same nominal flatness targets for the block deck:

```text
Total area:
less than 0.05 mm / 0.0020 in

100 mm x 100 mm section:
less than 0.02 mm / 0.0008 in
```

Source:

- https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Engine%2C%20Cooling%20and%20Exhaust/Engine/Service%20and%20Repair/Overhaul/Repair%20Procedures/

A new head gasket cannot compensate for a seriously distorted sealing surface.

---

# 24. Head-Gasket Construction and Installation Rules

**SERVICE-FAMILY - 2013 ACCENT 1.6 GDI**

Hyundai service information states:

- The cylinder-head gasket is a metal gasket.
- Do not bend or damage its sealing surfaces.
- Always use a new cylinder-head gasket.
- Always use new cylinder-head bolts.
- Hardened sealant must be removed from mating surfaces before assembly.
- Hyundai specifies sealant application at defined areas of the block/head-gasket interface during assembly.

Source:

- https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Engine%2C%20Cooling%20and%20Exhaust/Engine/Cylinder%20Head%20Assembly/Service%20and%20Repair/Repair%20Procedures/Part%202/

---

# 25. Cylinder-Head Bolt Tightening

**SERVICE-FAMILY - 2013 ACCENT 1.6 GDI**

Hyundai specifies:

```text
10 cylinder-head bolts

Initial torque:
29.4 N·m / 21.7 lb-ft

Then:
+90°
+90°
```

Tighten in Hyundai's specified sequence and in several passes.

Hyundai explicitly instructs:

```text
ALWAYS USE NEW CYLINDER-HEAD BOLTS
```

Source:

- https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Engine%2C%20Cooling%20and%20Exhaust/Engine/Cylinder%20Head%20Assembly/Service%20and%20Repair/Repair%20Procedures/Part%202/

### Important

The torque-angle sequence is highly sensitive to:

- Correct fastener identity
- Correct washers
- Correct sequence
- Correct surface preparation
- Correct lubrication state where specified
- Correct angle measurement

Do not reuse an old bolt because it visually appears undamaged.

---

# 26. GDI Safety During Cylinder-Head Work

Cylinder-head removal on this engine intersects the gasoline direct-injection system.

**SERVICE-FAMILY - 2012/2013 ACCENT 1.6 GDI**

Hyundai warns that the high-pressure pump, high-pressure pipe, fuel rail, and injectors can retain dangerous fuel pressure after shutdown.

Do not begin opening the high-pressure fuel system immediately after the engine stops.

Proper residual-pressure release and GDI procedures are required.

Sources:

- https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Powertrain%20Management/Fuel%20Delivery%20and%20Air%20Induction/Fuel%20Supply%20Line/Service%20and%20Repair/
- https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Engine%2C%20Cooling%20and%20Exhaust/Engine/Cylinder%20Head%20Assembly/Service%20and%20Repair/Repair%20Procedures/Part%201%200F%202/

See `GDI_FUEL_SYSTEM.md`.

---

# 27. Timing Risk During Cylinder-Head Work

Cylinder-head service intersects:

- Timing chain
- Chain tensioner
- Guides
- Intake CVVT phaser
- Exhaust CVVT phaser
- Camshafts
- Crankshaft TDC position

Mechanical timing must be restored correctly before cranking the engine.

See `TIMING_CVVT.md`.

A no-start or zero/low compression after head work should immediately raise questions about mechanical timing before parts are replaced elsewhere.

---

# 28. When a Head-Gasket Diagnosis Is Strong

Confidence becomes high when multiple independent forms of evidence agree.

Example:

```text
UNEXPLAINED COOLANT LOSS
        +
COLD-START MISFIRE CYLINDER 2
        +
CYLINDER 2 STEAM-CLEANED ON BORESCOPE
        +
LEAK-DOWN BUBBLES IN COOLANT
        +
POSITIVE COMBUSTION-GAS TEST
        =
STRONG INTERNAL COMBUSTION-TO-COOLANT CASE
```

Compare that with:

```text
WHITE VAPOR ON A COLD MORNING
        =
NOT ENOUGH EVIDENCE
```

---

# 29. False Head-Gasket Diagnoses to Avoid

## Thermostat stuck closed

Can cause overheating without head-gasket failure.

## Cooling fan failure

Can produce low-speed/idle overheating.

## Radiator restriction

Can produce heat rejection problems under load.

## Bad radiator cap

Can reduce boiling margin or lose coolant.

## External coolant leak

Can cause low coolant and overheating with no internal breach.

## Air pocket after coolant service

Can create heater changes, temperature spikes, and bubbles.

## Tight valve clearance

Can cause compression loss and misfire.

## Mechanical timing error

Can lower compression across multiple cylinders.

## Leaking injector

Can cause cold-start misfire and a wet cylinder without coolant.

## Short-trip condensation

Can create milky filler-cap residue.

---

# 30. Post-Overheat Inspection Checklist

After any serious overheating event:

1. Allow engine to cool fully.
2. Record the event in `NOMAD_SERVICE_LOG.md`.
3. Check coolant level.
4. Check engine oil level and appearance.
5. Inspect for external coolant leakage.
6. Inspect water-pump/belt condition.
7. Confirm cooling-fan operation.
8. Scan for DTCs and preserve freeze-frame data.
9. Pressure-test cooling system if coolant was lost.
10. Watch for recurring reservoir pressurization.
11. Watch for cold-start misfire over subsequent starts.
12. Perform compression/leak-down testing if evidence points internal.
13. Do not keep repeatedly overheating the engine while "testing."

Repeated overheating can turn a small cooling fault into major engine damage.

---

# 31. Nomad / Remote-Road Decision Rules

When far from services, preservation matters more than making the next campsite.

## Continue only after diagnosis when

- Temperature has fully returned to normal
- Cause was identified and corrected
- Coolant level remains stable
- No active leak exists
- No combustion-to-coolant evidence exists
- No repeated misfire exists

## Tow / recover when

- Coolant repeatedly disappears
- Reservoir repeatedly vents coolant
- Overheating returns
- Compression is materially abnormal and leak-down implicates coolant
- Oil and coolant are mixing
- A cylinder may contain liquid
- Engine develops severe knocking
- Cooling system cannot hold pressure and the leak is internal or inaccessible

---

# 32. AI / RAG Diagnostic Rules

An AI using this repository must follow these rules:

1. Never diagnose a head gasket from white exhaust vapor alone.
2. Never diagnose a head gasket from milky filler-cap residue alone.
3. Always distinguish external coolant loss from internal loss.
4. Always verify cooling-system basics before engine teardown.
5. Use compression pattern, not merely one absolute number.
6. Use leak-down to localize pressure loss.
7. Treat bubbles during a properly performed leak-down test as stronger evidence than ordinary reservoir bubbling.
8. Treat service-family specifications as supporting, not exact 2014 values.
9. Never open a hot radiator cap.
10. Never recommend repeated overheating as a diagnostic method.
11. Never open the GDI high-pressure fuel system casually.
12. Do not reuse cylinder-head bolts when following the same-engine Hyundai procedure.
13. If exact 2014 service data conflicts with this document, exact 2014 Hyundai data wins.
14. Preserve uncertainty explicitly.

---

# 33. Diagnostic Evidence Record

```yaml
head_gasket_diagnostic:
  date:
  odometer_miles:
  ambient_temperature:
  complaint:

  overheating_history:
    overheated: false
    estimated_duration:
    steam_observed: false
    coolant_loss_observed: false

  coolant:
    level_cold:
    unexplained_loss: false
    external_leak_found: false
    oil_contamination_visible: false

  engine_oil:
    level:
    rising_level: false
    coolant_contamination_visible: false
    filler_cap_emulsion_only: false

  startup:
    cold_start_misfire: false
    affected_cylinder:
    clears_after_seconds:

  exhaust:
    persistent_white_vapor_hot: false
    sweet_odor: false

  cooling_pressure_test:
    starting_pressure_psi:
    ending_pressure_psi:
    duration_minutes:
    external_leak_found:

  compression_psi:
    cylinder_1:
    cylinder_2:
    cylinder_3:
    cylinder_4:
    cranking_rpm:

  wet_compression_psi:
    cylinder_1:
    cylinder_2:
    cylinder_3:
    cylinder_4:

  leakdown:
    cylinder_1:
      percent:
      intake_noise: false
      exhaust_noise: false
      crankcase_noise: false
      coolant_bubbles: false
    cylinder_2:
      percent:
      intake_noise: false
      exhaust_noise: false
      crankcase_noise: false
      coolant_bubbles: false
    cylinder_3:
      percent:
      intake_noise: false
      exhaust_noise: false
      crankcase_noise: false
      coolant_bubbles: false
    cylinder_4:
      percent:
      intake_noise: false
      exhaust_noise: false
      crankcase_noise: false
      coolant_bubbles: false

  combustion_gas_test:
    performed: false
    result:

  borescope:
    cylinder_1:
    cylinder_2:
    cylinder_3:
    cylinder_4:

  spark_plug_comparison:
    cylinder_1:
    cylinder_2:
    cylinder_3:
    cylinder_4:

  mechanical_timing_verified: false
  valve_clearance_verified: false

  conclusion:
  confidence:
  next_test:
```

---

# 34. Quick Diagnostic Matrix

| Pattern | More likely direction |
|---|---|
| Coolant loss + visible external leak | Repair external cooling leak first |
| Two adjacent low cylinders | Gasket between cylinders, crack, timing/valve issue |
| One low cylinder, wet test improves | Rings/bore direction |
| One low cylinder, wet test unchanged | Valve/gasket/top-end direction |
| Leak-down bubbles in coolant | Combustion-to-coolant path strongly suspected |
| Cold-start misfire + coolant loss + steam-cleaned cylinder | Internal coolant leak strongly suspected |
| Milky residue only under cap | Condensation possible, gather more evidence |
| Persistent white exhaust hot + coolant loss | Internal coolant entry more suspicious |
| Immediate hard cooling-system pressurization cold | Combustion-gas intrusion possible |
| Overheats only at idle | Check fan/airflow before condemning head gasket |
| Overheats highway and idle | Check coolant level, thermostat, pump, radiator, internal leak |
| Repeated reservoir overflow with no external cause | Investigate combustion pressure entering coolant |

---

# 35. Core Doctrine

```text
OVERHEAT / COOLANT LOSS / MISFIRE
             ↓
RULE OUT EXTERNAL COOLING FAULTS
             ↓
PRESSURE TEST
             ↓
COMPRESSION
             ↓
LEAK-DOWN
             ↓
COMBUSTION-GAS TEST
             ↓
BORESCOPE / PLUG EVIDENCE
             ↓
VERIFY TIMING + VALVE CLEARANCE
             ↓
PROVE THE FAILURE PATH
             ↓
ONLY THEN REMOVE THE HEAD
```

A cylinder-head teardown is expensive, invasive, and capable of creating new faults if performed unnecessarily.

The purpose of diagnosis is not to make the symptoms fit a feared failure. It is to make the failure prove itself.

---

# 36. Sources

## Exact 2014 Hyundai / parts references

- 2014 Hyundai Accent owner manual overheating procedure:
  https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/?srch=overheating

- 2014 Accent cylinder-head parts catalog:
  https://www.hyundaipartsdeal.com/parts-list/2014-hyundai-accent/engine/cylinder_head.html

- 2014 Accent cylinder-head gasket listing:
  https://www.hyundaipartsdeal.com/oem-2014-hyundai-accent-cylinder_head_gasket.html

## Same-generation / same-engine Hyundai service references

- 2013 Accent compression test:
  https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Engine%2C%20Cooling%20and%20Exhaust/Engine/Tune-up%20and%20Engine%20Performance%20Checks/Compression%20Check/Testing%20and%20Inspection/

- 2013 Accent cylinder-head installation:
  https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Engine%2C%20Cooling%20and%20Exhaust/Engine/Cylinder%20Head%20Assembly/Service%20and%20Repair/Repair%20Procedures/Part%202/

- 2012 Accent cylinder-head inspection/removal:
  https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Engine%2C%20Cooling%20and%20Exhaust/Engine/Cylinder%20Head%20Assembly/Service%20and%20Repair/Repair%20Procedures/Part%201%200F%202/

- 2013 Accent block-deck inspection:
  https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Engine%2C%20Cooling%20and%20Exhaust/Engine/Service%20and%20Repair/Overhaul/Repair%20Procedures/

- 2012 Accent cooling-system pressure test:
  https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Engine%2C%20Cooling%20and%20Exhaust/Cooling%20System/Radiator/Testing%20and%20Inspection/

- 2012 Accent radiator-cap test:
  https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Engine%2C%20Cooling%20and%20Exhaust/Cooling%20System/Radiator%20Cap/Testing%20and%20Inspection/

- 2013 Accent GDI fuel-line safety/service:
  https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Powertrain%20Management/Fuel%20Delivery%20and%20Air%20Induction/Fuel%20Supply%20Line/Service%20and%20Repair/

---

## Status

- Exact 2014 hardware identity: **VERIFIED**
- Exact 2014 owner overheating safety procedure: **VERIFIED**
- Exact 2014 cylinder-head machining limits: **UNKNOWN**
- Same-generation head/block flatness data: **SERVICE-FAMILY SUPPORT**
- Same-generation compression data: **SERVICE-FAMILY SUPPORT**
- Same-generation head-bolt torque-angle procedure: **SERVICE-FAMILY SUPPORT**
- Head-gasket diagnosis should always rely on converging evidence, not a single symptom.
