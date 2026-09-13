# 2014 Hyundai Accent SE — Ignition System

> **Purpose:** Offline, source-aware ignition-system reference for the U.S.-market 2014 Hyundai Accent SE 1.6 L Gamma GDI engine. Designed for field diagnosis, maintenance, and AI/RAG retrieval.
>
> **Core rule:** A misfire or ignition-related DTC identifies a system or cylinder to investigate. It does **not** automatically prove that a coil or spark plug is defective.

---

## 1. Scope

This document covers:

- Coil-on-plug ignition architecture
- Spark plugs
- Ignition-coil power and ECU triggering
- Ignition-system fuses and supply paths
- Spark testing
- Coil-swap testing
- Spark-plug inspection
- Hot and load-related ignition failures
- Ignition-related DTCs
- No-spark diagnosis
- Misfire diagnosis
- Connector and wiring faults
- Service intervals
- Field / nomad troubleshooting
- AI reasoning rules

Related repository files:

- `ENGINE_OVERVIEW.md`
- `../diagnostics/MISFIRE.md`
- `../diagnostics/CRANK_NO_START.md`
- `../diagnostics/OBD2_GUIDE.md`
- `../specs/FUSES_AND_RELAYS.md`
- `../maintenance/MAINTENANCE_SCHEDULE.md`
- `../maintenance/NOMAD_SERVICE_LOG.md`

---

# 2. Source and Confidence Labels

This repository separates evidence by source quality.

- **VERIFIED — 2014 HYUNDAI OWNER MANUAL:** Explicitly stated in Hyundai's 2014 Accent owner's documentation.
- **CORROBORATED — 2014 OEM PARTS CATALOG:** Supported by 2014 Hyundai parts-catalog fitment data.
- **ADJACENT-YEAR HYUNDAI SERVICE FAMILY:** Hyundai service information for the same 1.6 L Gamma GDI platform in a nearby model year. Useful, but not silently promoted to exact 2014 VIN-specific factory data.
- **VERIFIED — STANDARD:** Defined by a recognized industry standard.
- **GENERAL DIAGNOSTIC PRACTICE:** Broadly accepted automotive diagnostic method, not a Hyundai-specific specification.
- **PROVISIONAL:** Plausible but not yet verified strongly enough for a hard specification.

**Repository principle:** Unknown is preferable to a confident wrong answer.

---

# 3. System Architecture

The 2014 Accent 1.6 L Gamma GDI uses a **coil-on-plug** ignition system.

Each cylinder has its own ignition coil mounted directly over its spark plug.

Conceptually:

```text
BATTERY / CHARGING SYSTEM
          ↓
IGNITION / ECU POWER DISTRIBUTION
          ↓
IGN COIL FUSE / ENGINE CONTROL FEEDS
          ↓
FOUR INDIVIDUAL COILS
          ↓
FOUR SPARK PLUGS
          ↓
COMBUSTION
```

The ECM/PCM determines when each coil should fire using engine-position and operating data such as:

- Crankshaft-position signal
- Camshaft-position signal
- Engine speed
- Load
- Coolant temperature
- Intake/manifold data
- Knock feedback
- Other engine-control inputs

An ignition failure can therefore originate from:

- Coil
- Spark plug
- Coil connector
- Coil power feed
- Coil control circuit
- ECM/PCM power or ground
- Crank/cam synchronization failure
- Low system voltage
- Mechanical engine fault that imitates ignition misfire

---

# 4. Factory / Catalog Hardware Identification

## Ignition coils

2014 Hyundai parts-catalog data lists:

```text
Ignition coil assembly: 27301-2B100
Quantity: 4
```

**Confidence:** CORROBORATED — 2014 OEM PARTS CATALOG

This part number appears for the 2014 Accent DOHC-GDI application.

### Important rule

Always verify replacement parts by VIN before purchase.

Catalog supersessions can occur, and a later replacement number may supersede the original number.

## Spark plugs

2014 Hyundai parts-catalog data lists:

```text
Spark plug assembly: 18846-10060
Quantity: 4
```

**Confidence:** CORROBORATED — 2014 OEM PARTS CATALOG

Again, verify by VIN and current Hyundai catalog before purchase.

Do not assume that every aftermarket cross-reference preserves the correct:

- Heat range
- Reach
- Thread
- Seat style
- Electrode design
- Resistor characteristics

Hyundai's 2014 owner's manual instructs that replacement plugs must have the **correct heat range**.

---

# 5. Spark-Plug Maintenance Interval

The 2014 Hyundai owner documentation specifies iridium spark-plug replacement at approximately:

```text
97,500 miles
```

A separate Hyundai Quick Reference Guide for the model year has been observed listing a later interval.

The repository currently uses **97,500 miles as the conservative service target** until exact VIN/build documentation resolves the conflict.

See:

- `../maintenance/MAINTENANCE_SCHEDULE.md`

Severe-service use can justify earlier inspection where drivability symptoms exist.

---

# 6. Service-Family Spark-Plug Data

Adjacent-year Hyundai service information for the same 1.6 L Gamma GDI platform gives:

```text
Spark plug gap:
0.9–1.0 mm
0.0354–0.0394 in
```

**Confidence:** ADJACENT-YEAR HYUNDAI SERVICE FAMILY

This is highly useful as a technical reference, but it is intentionally **not labeled exact 2014 VIN-specific factory specification** in this repository.

## Do not aggressively re-gap fine-wire iridium plugs

Fine-wire iridium/platinum plugs can be damaged by careless bending or prying against the center electrode.

Best practice:

1. Verify the plug part number.
2. Verify the manufacturer's supplied gap.
3. Measure gently if needed.
4. Replace a damaged or badly out-of-spec plug rather than abusing the electrode.

---

# 7. Ignition-Coil Service-Family Data

Adjacent-year Hyundai service information for the same engine family lists:

```text
Ignition coil primary resistance:
0.75 ohm ±15%
```

and ignition-coil retaining-bolt torque:

```text
9.8–11.8 N·m
7.2–8.7 lb-ft
```

**Confidence:** ADJACENT-YEAR HYUNDAI SERVICE FAMILY

## Important limitation of resistance testing

A coil that measures within resistance specification can still fail:

- Under high cylinder pressure
- When hot
- During acceleration
- Intermittently
- Because of internal insulation breakdown
- Because of connector or control-circuit faults

Therefore:

```text
RESISTANCE IN RANGE
        ≠
COIL PROVEN GOOD
```

Dynamic behavior matters.

---

# 8. Ignition Power Supply

The engine-compartment fuse box includes an ignition-coil circuit identified in this repository as:

```text
IGN COIL — 15A
```

The engine also depends on ECU/PCM power feeds and related ignition circuits.

See:

- `../specs/FUSES_AND_RELAYS.md`

If **all four cylinders lose spark**, prioritize shared causes before suspecting four simultaneous coil failures.

Shared causes may include:

- IGN COIL fuse
- ECU/PCM power supply
- Engine-control relay/main power
- Crankshaft-position signal loss
- Cam/crank synchronization problem
- System-voltage collapse
- ECM/PCM ground problem
- Wiring-harness damage

---

# 9. The Most Important Diagnostic Distinction

## One-cylinder ignition problem

Typical suspects:

- One coil
- One spark plug
- One coil connector
- One coil-control wire
- One injector
- One cylinder mechanical fault

## All-cylinder / multiple-cylinder ignition problem

Typical suspects:

- Shared power feed
- Shared ground / ECU issue
- Crank/cam signal loss
- Low voltage
- Fuel-system problem
- Mechanical timing
- Severe intake or fueling problem

This distinction prevents replacing four coils for one shared system fault.

---

# 10. Misfire DTCs

Common standardized misfire DTCs include:

```text
P0300 — Random / multiple-cylinder misfire
P0301 — Cylinder 1 misfire
P0302 — Cylinder 2 misfire
P0303 — Cylinder 3 misfire
P0304 — Cylinder 4 misfire
```

Ignition-primary/secondary circuit codes can also exist in the `P035x` family depending on what the ECM detects and what the vehicle implementation supports.

Always decode the **complete exact code** with a trustworthy source.

Do not infer a failed coil solely from a `P030x` code.

---

# 11. Coil-Swap Test

The coil-swap test is one of the highest-value ignition diagnostics for a single-cylinder misfire.

Example:

```text
P0302
Cylinder 2 misfire
```

Procedure concept:

1. Record all DTCs, freeze frame, and current symptoms.
2. Mark the original coil locations.
3. Move the suspected cylinder-2 coil to another cylinder, for example cylinder 3.
4. Move cylinder 3's coil to cylinder 2.
5. Reassemble correctly.
6. Run or drive only under safe conditions needed to reproduce the fault.
7. Re-scan.

Interpretation:

```text
P0302 becomes P0303
        ↓
MISFIRE FOLLOWED COIL
        ↓
COIL STRONGLY SUSPECTED
```

If the misfire stays on cylinder 2:

```text
P0302 stays P0302
        ↓
COIL NOT YET CONDEMNED,
BUT LOOK ELSEWHERE
        ↓
plug / injector / compression /
wiring / intake / mechanical
```

## Only change one diagnostic variable at a time

Do not simultaneously swap:

- Coil
- Plug
- Injector

If three things move at once, the result becomes ambiguous.

---

# 12. Spark-Plug Swap Test

If a coil swap does not move the misfire, a plug swap can be the next controlled test.

Example:

```text
Misfire stays cylinder 2 after coil swap
        ↓
Inspect plug 2
        ↓
Swap plug 2 with plug 3 if appropriate
        ↓
Misfire moves to cylinder 3?
```

If yes, the plug becomes strongly suspect.

Do not swap a plug that is:

- Cracked
- Oil-soaked due to a serious leak
- Mechanically damaged
- Severely fouled
- Missing electrode material
- Obviously unsafe to reinstall

Replace it instead.

---

# 13. Spark-Plug Inspection

A removed plug is a combustion witness.

Inspect:

- Center electrode
- Ground electrode
- Ceramic insulator
- Thread condition
- Crush washer / seat
- Oil contamination
- Fuel wetness
- Heavy carbon
- Ash deposits
- Abnormal erosion
- Cracks
- Tracking marks

## Possible interpretations

### Wet with fuel

May suggest:

- Fuel is entering the cylinder
- Ignition is absent or weak
- Engine is flooded

But a wet plug alone does not prove a bad coil.

### Dry after repeated cranking

May suggest:

- Fuel-delivery problem
- Injector not operating
- Injector control problem

But modern GDI behavior requires cautious interpretation.

### Oil-fouled

May suggest:

- Valve-cover / plug-well oil leakage externally
- Internal oil consumption if electrode end is oil-fouled
- Ring / valve-guide / mechanical issue

Determine **where** the oil is located.

Oil in the plug well is not the same diagnosis as oil on the firing tip.

### Heavy black carbon

Possible contributors:

- Repeated short trips
- Rich operation
- Weak ignition
- Long-term idling
- Plug too cold for the application
- Persistent misfire

### White / overheated appearance

Possible contributors:

- Excessive combustion temperature
- Incorrect plug heat range
- Lean condition
- Abnormal ignition / combustion

Do not diagnose mixture from plug color alone on a modern closed-loop GDI engine.

---

# 14. Spark Test Safety

Ignition systems generate high voltage.

Never:

- Hold a coil or plug with your hand while cranking
- Allow spark near spilled fuel or fuel vapor
- Perform uncontrolled spark testing near an open GDI fuel system
- Rest a loose spark plug where it can fall into moving components
- Crank continuously for long periods

Adjacent-year Hyundai service procedure disables fuel injection before the spark test and limits cranking to roughly **5–10 seconds**.

**Confidence:** ADJACENT-YEAR HYUNDAI SERVICE FAMILY

## Preferred field method

A proper spark tester is safer and more repeatable than casually holding a removed plug against the engine.

If following a Hyundai-style removed-plug test:

- Disable fuel injection by the verified service method.
- Secure the plug properly.
- Ground the plug body securely.
- Keep hands and flammable material away.
- Limit cranking time.

---

# 15. Why a Visible Spark Does Not Always Prove the Coil Is Good

A spark can jump easily in open air but fail inside the engine where cylinder pressure is much higher.

Therefore:

```text
SPARK VISIBLE IN AIR
        ≠
SPARK PROVEN STRONG UNDER LOAD
```

A marginal coil or worn plug may behave normally:

- At idle
- When cold
- In the shop

but fail:

- Under hard acceleration
- On steep grades
- At high engine load
- When hot
- With a wide plug gap

This is why symptom reproduction and controlled component swapping are so valuable.

---

# 16. Load-Related Misfire

Pattern:

```text
Idle smooth
Cruise acceptable
Hard acceleration → stumble / misfire
```

Ignition possibilities include:

- Weak coil
- Excessive plug gap
- Worn plug electrodes
- Cracked insulator
- Coil-boot leakage
- High-voltage tracking

But also consider:

- Fuel-pressure deficiency
- Injector flow problem
- Mechanical compression problem

Do not assume every load misfire is ignition.

---

# 17. Hot-Only Misfire

Pattern:

```text
Cold engine normal
        ↓
Fully warm / heat-soaked
        ↓
misfire appears
```

Possible ignition causes:

- Coil internal breakdown when hot
- Connector terminal expansion / poor contact
- Heat-damaged wiring

Possible non-ignition causes:

- Injector fault
- Crank/cam sensor heat failure
- Fuel-pressure issue
- Mechanical problem

A hot-only coil failure may pass a cold resistance test.

---

# 18. Cold-Start Misfire

Possible ignition causes:

- Worn or fouled spark plug
- Weak coil
- Moisture contamination
- Cracked insulator or boot

Also consider:

- GDI injector leakage
- Intake-valve deposits
- Compression leakage that improves as parts warm
- Coolant-temperature sensor bias
- Intake-air leak
- Fuel-quality problem

See:

- `../diagnostics/MISFIRE.md`
- `../diagnostics/FUEL_TRIM_DIAGNOSTICS.md`

---

# 19. Moisture-Related Misfire

If misfire appears after:

- Heavy rain
- Engine washing
- High humidity
- Deep splash exposure

inspect:

- Coil connectors
- Coil boots
- Spark-plug wells
- Harness seals
- Water intrusion
- Cracks / carbon tracking

Do not spray water on the ignition system as a crude diagnostic technique around a running engine.

---

# 20. Coil Connector Inspection

Inspect for:

- Broken locking tab
- Partially seated connector
- Backed-out terminal
- Corrosion
- Bent terminal
- Heat damage
- Oil contamination
- Harness chafing
- Rodent damage
- Previous poor repairs

A visually perfect connector can still have poor terminal tension.

When a problem is intermittent, a careful harness movement test while observing live data may help, but avoid pulling, piercing, or shorting wires.

---

# 21. No Spark on One Cylinder

Diagnostic sequence:

```text
ONE CYLINDER HAS NO / WEAK SPARK
            ↓
Inspect plug and coil physically
            ↓
Swap coil with known-good cylinder
            ↓
Does fault move?
   ├─ YES → coil strongly suspected
   └─ NO
        ↓
Swap / inspect plug if appropriate
        ↓
Still same cylinder?
        ↓
Check coil power
        ↓
Check coil control circuit / connector
        ↓
Check injector / compression / mechanical fault
```

Do not jump directly from "no spark seen" to "bad ECM."

---

# 22. No Spark on All Cylinders

When all four cylinders appear affected, look for a shared cause.

```text
NO SPARK — ALL CYLINDERS
        ↓
Battery / system voltage healthy?
        ↓
IGN COIL fuse / ECU feeds intact?
        ↓
Engine RPM visible while cranking?
        ↓
Crank/cam DTCs?
        ↓
ECM/PCM powered and communicating?
        ↓
Shared wiring / main relay / ground issue?
        ↓
Mechanical timing / synchronization issue?
```

## RPM while cranking

If the scan tool shows **zero engine RPM while the engine is physically cranking**, prioritize crankshaft-position sensing, wiring, synchronization, and ECU-input diagnosis.

See:

- `../diagnostics/CRANK_NO_START.md`

---

# 23. Ignition Coil Power Test

General diagnostic method:

1. Identify the correct coil power terminal from trustworthy wiring information.
2. Verify appropriate voltage with the ignition state required by the circuit.
3. Compare the suspect coil connector with a known-good cylinder.
4. If power is missing on all coils, trace the shared feed.
5. If power is missing on only one coil, inspect that branch of the harness.

Do not guess connector pin functions.

Do not short a coil-control circuit to battery positive or ground.

ECM driver circuits can be damaged by careless testing.

---

# 24. Coil-Control Signal

The ECM commands ignition timing electronically.

A conventional multimeter may not reveal a brief pulsed control signal clearly.

Advanced diagnosis can use:

- Oscilloscope
- Appropriate ignition probe
- Logic-safe test equipment designed for automotive control circuits

Do not use an incandescent test light on sensitive ECM trigger circuits unless the service procedure explicitly allows it.

---

# 25. Low Voltage and False Ignition Symptoms

Low battery or charging voltage can cause:

- Weak cranking
- Unstable ECU operation
- Multiple misleading DTCs
- Weak ignition performance
- Communication faults
- Apparent random misfires

Before diagnosing multiple simultaneous electrical failures:

```text
VERIFY SYSTEM VOLTAGE FIRST
```

See:

- `../diagnostics/CHARGING_SYSTEM.md`
- `../electrical/BATTERY_STARTER_ALTERNATOR.md`

---

# 26. Spark Plug Removal Rules

Before removal:

1. Work with a suitably cool engine unless the exact service procedure specifies otherwise.
2. Blow or clean loose debris away from plug wells before removing plugs.
3. Remove coils carefully.
4. Do not allow dirt to fall into the cylinder.
5. Use the correct plug socket.
6. Keep plugs indexed by cylinder during diagnosis.

Adjacent-year Hyundai service data uses a **16 mm spark-plug wrench/socket** for this engine family.

**Confidence:** ADJACENT-YEAR HYUNDAI SERVICE FAMILY

---

# 27. Spark Plug Installation Rules

Use only a verified correct plug.

General best practice:

- Start threads by hand.
- Never force a plug into an aluminum cylinder head.
- If resistance appears before the plug seats, stop and inspect.
- Do not cross-thread.
- Keep plug and seat clean.
- Follow the verified torque for the exact plug/application.

## Important repository limitation

This document intentionally does **not** publish a hard 2014 spark-plug installation torque until a sufficiently authoritative exact-application source is locked down.

Several nearby Hyundai applications provide plausible values, but they are not treated as exact merely because they are close.

This is an example of the repository's rule:

```text
UNKNOWN EXACT TORQUE
        >
CONFIDENTLY WRONG TORQUE
```

---

# 28. Do Not Automatically Use Anti-Seize

Modern spark plugs may have plated threads and manufacturer-specific torque assumptions.

Anti-seize can change thread friction and therefore change clamp load for a given torque.

Use anti-seize only if the spark-plug manufacturer or exact Hyundai service procedure specifically calls for it.

Do not automatically lubricate spark-plug threads.

---

# 29. Coil-Boot Compounds

A small amount of appropriate dielectric grease may sometimes be used on the inside lip of a coil boot where allowed by the component manufacturer.

Do not:

- Fill the boot with grease
- Coat electrical metal terminals indiscriminately
- Use random petroleum grease

Too much dielectric grease can interfere with proper seating.

---

# 30. Catalyst Protection

Hyundai warns that continued engine operation with a serious misfire can damage the catalytic converter.

Therefore:

```text
SEVERE MISFIRE
FLASHING MIL
RAW-FUEL SMELL
LOSS OF POWER
        ↓
STOP DRIVING HARD
        ↓
DIAGNOSE / TOW AS APPROPRIATE
```

Do not "drive it until it clears out" when the MIL is flashing and the engine is misfiring heavily.

Unburned fuel can overheat the catalyst.

---

# 31. Quick Diagnostic Matrix

| Symptom | Ignition possibilities | Other important possibilities |
|---|---|---|
| Single-cylinder misfire | Coil, plug, connector, control wire | Injector, compression, intake leak |
| Random/multiple misfire | Shared power, several worn plugs, low voltage | Fuel pressure, vacuum leak, timing, bad fuel |
| Misfire under load | Weak coil, excessive plug gap, worn plug | Fuel-pressure problem, compression |
| Hot-only misfire | Heat-sensitive coil/wiring | Injector, CKP/CMP, fuel pressure |
| Cold-only misfire | Plug/coil/moisture | Injector leakage, deposits, compression |
| No spark one cylinder | Coil, plug, connector/control | ECM driver, wiring, mechanical misdiagnosis |
| No spark all cylinders | Shared power, crank/cam input, ECU feed | Mechanical timing, system voltage |
| Starts rough after rain | Coil boot/connector moisture | Intake moisture, unrelated fault |
| P030x follows coil swap | Coil strongly suspected | — |
| P030x stays after coil swap | Plug/wiring or non-ignition cause | Injector/compression/intake |

---

# 32. Minimal Roadside Ignition Workflow

For a rough-running Accent away from a shop:

```text
1. Is MIL flashing?
   YES → reduce load / stop driving aggressively

2. Read stored + pending DTCs

3. Preserve freeze frame

4. Identify cylinder-specific vs random fault

5. Inspect coil connectors and obvious wiring

6. Check system voltage

7. If one-cylinder fault:
   controlled coil swap

8. If fault does not follow coil:
   inspect plug / consider plug swap

9. If still same cylinder:
   move to injector / compression / mechanical diagnosis
```

This sequence minimizes unnecessary parts replacement.

---

# 33. Nomad / Primitive-Road Considerations

Long-distance and primitive-road use can add ignition stressors:

- Dust
- Moisture
- Heat soak
- Vibration
- Long high-load climbs
- Repeated short trips
- Extended idling

Useful field inventory may include:

- OBD-II scanner
- Multimeter
- Correct coil-removal socket
- Correct spark-plug socket
- Extension and ratchet
- Torque wrench appropriate to low torque values
- Dielectric-safe electrical cleaner
- Clean shop towels
- Nitrile gloves

## Spare-coil strategy

A verified spare coil can be useful for remote travel, but only if:

- It is the correct part
- It is protected from impact/moisture
- It is not used as a substitute for diagnosis

A spare part is a tool, not proof of the failure.

---

# 34. AI Diagnostic Rules

When an AI assistant uses this file, it should follow these rules:

1. Never equate `P030x` directly with "bad coil."
2. Ask whether the misfire is cylinder-specific or random.
3. Preserve DTCs, pending codes, freeze frame, and live data before clearing.
4. Prefer one-variable-at-a-time swap testing.
5. If a misfire follows a coil, raise coil probability strongly.
6. If a misfire does not follow the coil, do not keep blaming the coil without new evidence.
7. Consider plugs, injectors, compression, intake leaks, wiring, and fuel pressure.
8. For all-cylinder no-spark, prioritize shared power, crank/cam input, ECU feeds, and system voltage.
9. Do not invent exact connector pinouts.
10. Do not invent exact spark-plug torque.
11. Treat adjacent-year Hyundai service values as adjacent-year evidence unless verified for the exact vehicle.
12. Treat visible open-air spark as incomplete evidence of performance under cylinder pressure.
13. Escalate severe/flashing-MIL misfire because of catalyst-damage risk.
14. Never recommend random wire-jumper testing on ECM-controlled ignition circuits.

---

# 35. AI Prompt Template

```text
Vehicle: 2014 Hyundai Accent SE 1.6 GDI
Mileage:
Ambient temperature:
Engine cold/warm/hot:
Symptom:
MIL steady/flashing/off:
Stored DTCs:
Pending DTCs:
Permanent DTCs:
Freeze frame:
Misfire cylinder(s):
Idle behavior:
Acceleration/load behavior:
System voltage:
Coil swap performed:
Result:
Plug swap performed:
Result:
Plug appearance:
Fuel trims:
Compression data if known:
Recent repairs:
Rain/water exposure:

Diagnose using evidence-first logic.
Do not assume a DTC names the failed part.
State what is known, unknown, and the next best discriminating test.
```

---

# 36. Machine-Readable Summary

```yaml
vehicle:
  year: 2014
  make: Hyundai
  model: Accent
  trim: SE
  engine: 1.6L Gamma GDI

ignition:
  architecture: coil_on_plug
  coil_count: 4
  spark_plug_count: 4

catalog_parts:
  ignition_coil:
    part_number: "27301-2B100"
    confidence: corroborated_2014_oem_catalog
  spark_plug:
    part_number: "18846-10060"
    confidence: corroborated_2014_oem_catalog

service_family_values:
  spark_plug_gap:
    metric_mm: "0.9-1.0"
    imperial_in: "0.0354-0.0394"
    confidence: adjacent_year_hyundai_same_engine_family
  ignition_coil_primary_resistance_ohm:
    value: 0.75
    tolerance_percent: 15
    confidence: adjacent_year_hyundai_same_engine_family
  ignition_coil_bolt_torque:
    Nm: "9.8-11.8"
    lb_ft: "7.2-8.7"
    confidence: adjacent_year_hyundai_same_engine_family
  spark_plug_install_torque:
    value: unknown_exact_2014
    rule: do_not_guess

maintenance:
  spark_plug_repository_interval_miles: 97500
  interval_conflict_present: true

fuses:
  ignition_coil_fuse:
    label: "IGN COIL"
    amperage: 15

core_diagnostic_rules:
  - dtc_is_evidence_not_part_order
  - swap_one_component_at_a_time
  - if_misfire_follows_coil_raise_coil_probability
  - if_misfire_stays_check_plug_injector_compression_wiring
  - all_cylinder_no_spark_prioritize_shared_causes
  - verify_system_voltage
  - preserve_freeze_frame_before_clearing
  - severe_misfire_can_damage_catalyst
  - visible_open_air_spark_does_not_prove_loaded_performance
  - unknown_exact_spec_is_better_than_invented_spec
```

---

# 37. Sources

## 2014 Hyundai owner's manual

Searchable copy:

https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/

Relevant owner-manual points include:

- If the engine cranks normally but does not start, Hyundai instructs the owner to check ignition-coil and spark-plug connections.
- Replacement spark plugs must have the correct heat range.
- Maintenance information and spark-plug service interval.

## Adjacent-year Hyundai service information — same 1.6 L Gamma GDI family

Spark-plug / spark-test service information:

https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Powertrain%20Management/Tune-up%20and%20Engine%20Performance%20Checks/Spark%20Plug/Testing%20and%20Inspection/

Used in this document only with **ADJACENT-YEAR HYUNDAI SERVICE FAMILY** labeling for values including:

- Spark-plug gap
- Spark-test method
- Coil retaining-bolt torque

Adjacent ignition-system reference:

https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Powertrain%20Management/Ignition%20System/Testing%20and%20Inspection/

Used for corroboration of service-family coil resistance and testing concepts.

## 2014 Hyundai parts-catalog references

Ignition coil:

https://www.hyundaipartsdeal.com/oem-2014-hyundai-accent-ignition_coil.html

Spark plug:

https://www.hyundaipartsdeal.com/oem-2014-hyundai-accent-spark_plug.html

These are used for **catalog fitment / part-number corroboration**, not as a substitute for VIN-specific Hyundai service information.

---

# 38. Repository Doctrine

```text
MISFIRE
   ↓
PRESERVE EVIDENCE
   ↓
IDENTIFY CYLINDER PATTERN
   ↓
TEST ONE VARIABLE
   ↓
DID THE FAULT MOVE?
   ↓
YES → FOLLOW THE MOVED COMPONENT
NO  → INVESTIGATE THE ORIGINAL CYLINDER / SHARED SYSTEM
   ↓
REPAIR ROOT CAUSE
   ↓
VERIFY UNDER THE CONDITIONS THAT CAUSED THE FAULT
```

The ignition system should be diagnosed as a system, not as a shopping list.
