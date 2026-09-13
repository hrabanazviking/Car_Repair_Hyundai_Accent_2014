# 2014 Hyundai Accent SE — Misfire Diagnosis

> **Purpose:** A practical, source-aware diagnostic guide for engine misfires on a U.S.-market 2014 Hyundai Accent SE with the 1.6 L GDI engine. Designed for roadside use, workshop use, and offline AI/RAG retrieval.
>
> **Primary rule:** A misfire code identifies a combustion problem. It does **not** automatically identify the failed part.

---

## 1. Scope

This document focuses on:

- `P0300` — Random/multiple-cylinder misfire detected
- `P0301` — Cylinder 1 misfire detected
- `P0302` — Cylinder 2 misfire detected
- `P0303` — Cylinder 3 misfire detected
- `P0304` — Cylinder 4 misfire detected

It also covers related symptoms when no code is yet stored.

Related repository files:

- `OBD2_GUIDE.md`
- `CRANK_NO_START.md`
- `../guides/ROADSIDE_DIAGNOSTIC_TRIAGE.md`
- `../specs/FUSES_AND_RELAYS.md`
- `../maintenance/MAINTENANCE_SCHEDULE.md`
- `../maintenance/NOMAD_SERVICE_LOG.md`

SAE J2012 defines standardized OBD diagnostic trouble-code formats and code descriptions. Hyundai's 2014 Accent owner's manual also warns that engine malfunction/misfire can damage the catalytic converter.

---

# 2. Immediate Safety / Catalyst Protection

## If the MIL/check-engine light is blinking or flashing

Treat this as **urgent**.

A severe active misfire can send unburned fuel into the catalytic converter and overheat/damage it.

Hyundai specifically warns not to continue operating the vehicle when there are signs of engine malfunction such as misfire or noticeable loss of performance.

### Immediate action

1. Reduce throttle/load.
2. Avoid hard acceleration.
3. Avoid high RPM.
4. Move to a safe place.
5. Stop driving if the engine is shaking severely, power is badly reduced, or the MIL is blinking continuously.
6. Diagnose before resuming normal driving.

A catalytic converter can be far more expensive than an ignition coil or spark plug.

---

# 3. What a Misfire Actually Means

A cylinder must receive all of the following correctly:

1. Air
2. Fuel
3. Compression
4. Ignition energy
5. Correct ignition timing
6. Correct valve/cam timing

A failure in any of those areas can create a misfire.

For the 1.6 L GDI Accent, possible misfire causes include:

- Spark plug fault
- Ignition coil fault
- Coil connector/wiring fault
- Injector fault
- Injector wiring/control fault
- Fuel-pressure problem
- Intake/vacuum leak
- Mechanical compression loss
- Valve sealing problem
- Cam/crank timing problem
- Carbon/deposit-related airflow problem
- Low system voltage
- ECU power/ground problem
- Contaminated/poor-quality fuel
- Overly rich or lean mixture
- Sensor input problem

Do not treat `P030X` as a parts-order command.

---

# 4. Misfire Code Reference

| Code | Meaning | First interpretation |
|---|---|---|
| `P0300` | Random/multiple-cylinder misfire | Shared cause more likely than one isolated component |
| `P0301` | Cylinder 1 misfire | Focus diagnosis on cylinder 1, but still check shared causes |
| `P0302` | Cylinder 2 misfire | Focus diagnosis on cylinder 2, but still check shared causes |
| `P0303` | Cylinder 3 misfire | Focus diagnosis on cylinder 3, but still check shared causes |
| `P0304` | Cylinder 4 misfire | Focus diagnosis on cylinder 4, but still check shared causes |

A cylinder-specific code can still be caused by a shared fuel, voltage, or mechanical problem that happens to affect one cylinder first.

---

# 5. Preserve Evidence Before Clearing Codes

Before disconnecting the battery, swapping parts, or clearing DTCs, record:

- Stored codes
- Pending codes
- Permanent codes
- Freeze-frame data
- Engine RPM
- Coolant temperature
- Intake-air temperature
- Short-term fuel trim (STFT)
- Long-term fuel trim (LTFT)
- Calculated load
- MAP value, if available
- System/module voltage
- Fuel-pressure data, if available
- Whether the engine was cold or hot
- Vehicle speed when the fault occurred
- Whether fault occurred under acceleration, cruise, idle, or deceleration
- Fuel level
- Recent refueling history
- Recent repairs

### Why this matters

A code like `P0302` is much more useful when accompanied by:

```text
P0302
Coolant: fully warm
RPM: 2,700
Load: high
Vehicle speed: 58 mph
Fuel trims: near normal
Symptom: stumble only under acceleration
```

That pattern points in a different direction than:

```text
P0302
Coolant: cold
RPM: 850
Load: low
Fuel trims: strongly positive
Symptom: rough idle only for first 60 seconds
```

---

# 6. First Classification: One Cylinder or Many?

## One-cylinder pattern

Examples:

- Only `P0302`
- Consistent miss on one cylinder
- Roughness remains localized

Most likely categories:

- Coil
- Plug
- Injector
- Injector wiring
- Local intake leak
- Compression/valve problem

## Multi-cylinder/random pattern

Examples:

- `P0300`
- `P0300` plus several `P030X` codes
- Several cylinders begin misfiring together

Prioritize shared causes:

- Low fuel pressure
- Bad fuel
- Air leak
- Charging/voltage problem
- ECU/ground issue
- Shared power feed
- Cam/crank timing issue
- Major intake problem
- Sensor input fault

A simultaneous four-cylinder coil failure is much less likely than a shared system problem.

---

# 7. Master Diagnostic Tree

```text
MISFIRE / P030X
      ↓
MIL flashing?
      ↓
YES → reduce load / stop driving / protect catalyst
      ↓
NO or safely stopped
      ↓
Record codes + freeze frame + live data
      ↓
One cylinder or multiple?
      ↓
ONE CYLINDER
      ├── Coil swap test
      ├── Plug inspection
      ├── Injector / wiring check
      ├── Local intake leak
      └── Compression / mechanical test

MULTIPLE / RANDOM
      ├── Battery/charging voltage
      ├── Fuel pressure / fuel quality
      ├── Intake / vacuum leak
      ├── Shared fuses / grounds / ECU feed
      ├── Sensor plausibility
      └── Cam/crank timing / mechanical condition
```

---

# 8. Single-Cylinder Misfire Workflow

Suppose the vehicle has `P0302`.

Use this sequence:

```text
P0302
  ↓
Inspect cylinder-2 coil connector/wiring
  ↓
Swap coil with another cylinder
  ↓
Clear codes only after recording evidence
  ↓
Road-test / reproduce symptom
  ↓
Did the misfire move?
```

## If the misfire moves with the coil

Example:

```text
Before swap: P0302
Swap coil 2 ↔ coil 3
After test: P0303
```

The moved coil becomes a **strong suspect**.

This is much better evidence than replacing all four coils.

## If the misfire stays on the original cylinder

Continue diagnosis:

1. Inspect spark plug.
2. Inspect coil boot and plug well.
3. Check injector command/wiring.
4. Compare injector behavior where appropriate.
5. Check compression.
6. Check for local intake leak.
7. Consider valve/mechanical condition.

---

# 9. Ignition Coil Diagnosis

The Accent uses coil-on-plug ignition.

## Inspect first

Engine OFF and cool enough to work safely:

- Connector fully seated
- Broken connector lock
- Corrosion
- Oil or water in plug well
- Cracked coil housing
- Burn/carbon tracking marks
- Damaged coil boot
- Chafed wiring

## Coil swap test

For a single-cylinder misfire:

1. Record original DTC.
2. Mark the suspect coil.
3. Move it to a different cylinder.
4. Move the known-good coil from that cylinder into the suspect cylinder.
5. Reconnect everything correctly.
6. Re-test.

### Interpretation

```text
Misfire follows coil → coil strongly implicated
Misfire stays cylinder → coil less likely; continue diagnosis
```

A coil-swap test is not absolute proof if the problem is intermittent, but it is high-value evidence.

---

# 10. Spark Plug Diagnosis

A bad or fouled plug can misfire under:

- Cold start
- Heavy load
- High cylinder pressure
- Acceleration
- Wet/fuel-fouled conditions

Inspect plugs for:

- Cracked ceramic
- Heavy carbon deposits
- Oil fouling
- Fuel wetness
- Damaged electrode
- Abnormal erosion
- Evidence of overheating
- Deposits inconsistent between cylinders

Compare all four plugs rather than looking at one in isolation.

## Important

Do not invent a plug gap or torque value from memory.

Use a verified Hyundai/plug-manufacturer specification before installing or adjusting plugs.

The maintenance schedule in this repository records Hyundai's conflicting published replacement intervals and uses the conservative figure there.

---

# 11. Wet vs. Dry Plug Clues

A plug can provide clues, but not absolute proof.

## Plug unusually wet with fuel smell

Possible explanations:

- Cylinder receives fuel but fails to ignite
- Weak/no spark
- Excessive fuel delivery
- Repeated unsuccessful starts

## Plug unusually dry compared with others

Possible explanations:

- Injector not delivering fuel
- Injector circuit/control fault
- Severe local intake/air issue

## Plug oily

Possible explanations:

- Oil entering combustion chamber
- Mechanical wear
- Valve-seal/ring-related issue

Do not diagnose solely by plug appearance.

---

# 12. Injector / GDI Misfire Diagnosis

The 2014 Accent uses gasoline direct injection.

## Safety

The high-pressure fuel system can retain dangerous pressure.

Never:

- loosen high-pressure fuel fittings just to check whether fuel is present
- place a hand over a suspected high-pressure leak
- crack injector lines during roadside diagnosis

High-pressure fuel can penetrate skin.

## Safer diagnostic tools

Prefer:

- OBD fuel-pressure data where available
- Injector electrical tests using proper procedures
- Cylinder contribution/misfire data where supported
- Professional scan-tool commands where supported
- Proper service-information-guided testing

## A single-cylinder injector problem may involve

- Electrical connector
- Open/short in wiring
- ECU driver issue
- Restricted injector
- Leaking injector
- Mechanical injector fault

Do not conclude "bad injector" until ignition and compression have been considered.

---

# 13. Compression / Mechanical Misfire

If coil and plug tests do not move the misfire, mechanical testing becomes important.

Possible causes:

- Burned/leaking valve
- Valve not seating correctly
- Ring/cylinder sealing problem
- Head-gasket problem
- Mechanical timing issue
- Cam/valvetrain problem

Useful tests include:

- Compression test
- Relative compression test
- Leak-down test
- Cam/crank correlation analysis

## Relative comparison matters

A cylinder that is substantially lower than the others deserves investigation even if an absolute compression number seems superficially plausible.

Do not publish a Hyundai-specific compression threshold in this repository until it is verified from an authoritative service source.

---

# 14. Vacuum / Intake Leak Misfire

A vacuum/intake leak may cause:

- Rough idle
- Lean fuel trims
- `P0300`
- One-cylinder misfire if leak is localized near one runner
- Improvement as engine speed/load increases

Possible leak locations include:

- Intake ducting
- Intake-manifold gasket
- PCV-related hoses
- EVAP purge plumbing
- Brake-booster vacuum line
- Other vacuum connections

## Fuel-trim clue

General diagnostic pattern:

```text
Large positive trims at idle
↓
Trims improve substantially at higher RPM/load
↓
Vacuum/intake leak becomes more plausible
```

Fuel trims are clues, not standalone verdicts.

---

# 15. Fuel-Pressure / Shared Fuel Problem

When multiple cylinders misfire, evaluate fuel supply.

Possible causes:

- Low tank level
- Contaminated fuel
- Low-pressure fuel-delivery issue
- High-pressure GDI issue
- Electrical supply fault to fuel system
- Fuel-pressure sensor/control problem

Hyundai warns that operating with an extremely low fuel level can contribute to misfire and catalytic-converter damage.

If the misfire began immediately after refueling, note:

- Station/location
- Fuel grade
- Approximate gallons added
- Whether water/contamination is suspected
- Whether symptoms appeared immediately or after several miles

Do not casually add fuel-system chemicals as a diagnostic substitute.

---

# 16. Fuel Trim Interpretation

Fuel trims are especially useful once the engine is running steadily enough to produce meaningful data.

## Positive trim

The ECU is generally adding fuel relative to its base calculation.

Possible causes:

- Unmetered air / vacuum leak
- Low fuel delivery
- Injector restriction
- Sensor error

## Negative trim

The ECU is generally subtracting fuel.

Possible causes:

- Excess fuel delivery
- Injector leakage
- Sensor bias
- Other rich condition

## Important

Do not use arbitrary universal percentages as hard failure limits.

Interpret:

- STFT
- LTFT
- idle vs. cruise behavior
- bank/cylinder context
- sensor plausibility

The Accent's inline-four has one cylinder bank, so bank-to-bank comparison is not available as it would be on a V-engine.

---

# 17. Cold-Start Misfire

If the engine misfires mainly when cold and smooths out as it warms:

Possible causes include:

- Weak ignition component
- Plug fouling
- Injector behavior
- Local intake leak
- Temperature-dependent sensor issue
- Valve/compression issue that changes with temperature
- Deposit-related airflow/combustion behavior

Record exactly how long the roughness lasts:

```text
5 seconds?
30 seconds?
2 minutes?
Until coolant reaches operating temperature?
```

Duration matters.

---

# 18. Hot-Only Misfire

A misfire that appears only after heat soak may involve:

- Ignition coil breaking down hot
- Connector/wiring expansion issue
- Injector problem
- Sensor fault
- Fuel-pressure problem
- Mechanical issue sensitive to heat

Do not let the engine cool before capturing codes/live data if the vehicle is safely stopped and testing can be performed safely.

Intermittent heat-related faults often hide once cooled.

---

# 19. Misfire Under Load / Acceleration

A misfire that appears mainly during acceleration or climbing often points toward faults that become visible under higher cylinder pressure/load.

Prioritize:

- Weak coil
- Worn/damaged spark plug
- Fuel-delivery limitation
- Injector restriction
- Low fuel pressure
- Mechanical compression problem

If fuel trims are normal and one cylinder consistently misfires only under load, ignition becomes especially worth testing.

---

# 20. Idle-Only Misfire

If roughness is strongest at idle but improves with RPM:

Consider:

- Vacuum/intake leak
- PCV-related leak
- Local runner leak
- Injector imbalance
- Valve/compression issue
- Deposits/airflow problem

Compare fuel trims at idle and at a steady elevated RPM when safe.

---

# 21. Random/Multiple Misfire With Low System Voltage

Low voltage can create misleading engine faults.

If several codes appear together, check:

- Battery condition
- Charging voltage
- Battery terminals
- Engine ground
- Chassis ground
- ECU power feeds
- `ECU`, `ECU 1`, `ECU 2`, `IGN COIL`, `INJECTOR`, and `SENSOR` circuits as appropriate

A failing charging system can make electronic diagnostics look much stranger than the underlying problem really is.

---

# 22. Relevant Fuse / Power Checks

From this repository's Hyundai fuse reference, useful engine-related circuits include:

- `IGN COIL` — 15 A
- `INJECTOR` — 15 A
- `SENSOR` — 10 A
- `ECU 2` — 10 A
- `ECU 1` — 30 A
- `F/PUMP` — 15 A

A blown fuse can indicate a short or failed load.

Do not repeatedly replace a fuse that blows again.

See `../specs/FUSES_AND_RELAYS.md`.

---

# 23. Carbon / Deposit Considerations on GDI

Direct-injection engines do not wash the intake valves with port-injected gasoline in the same way traditional port-injected engines do.

Over long service periods, intake-valve deposits can become one possible contributor to poor airflow, roughness, or misfire.

However:

- Deposits should not be assumed merely because the engine is GDI.
- Verify more common causes first.
- Do not pour cleaners into places they were not designed to go.
- Do not treat a chemical product as a substitute for diagnosis.

Deposit-related diagnosis may require inspection or professional cleaning methods.

---

# 24. Cylinder-Swap Strategy

The central diagnostic trick for a single-cylinder misfire is to move only one suspect component at a time.

Example:

```text
P0302
  ↓
Swap coil 2 ↔ coil 3
  ↓
P0303 appears
  ↓
Coil is strongly implicated
```

If the code remains `P0302`, next steps might include plug comparison, then injector/mechanical testing.

Do not swap coil and plug simultaneously if the objective is to determine which one caused the fault. Changing two variables destroys diagnostic clarity.

---

# 25. Do Not Shotgun Parts

Bad workflow:

```text
P0302
 ↓
Replace 4 coils
 ↓
Replace 4 plugs
 ↓
Replace injector
 ↓
Still misfires
```

Better workflow:

```text
P0302
 ↓
Record evidence
 ↓
Swap coil only
 ↓
Result?
 ↓
Inspect/test plug
 ↓
Result?
 ↓
Injector test
 ↓
Compression/mechanical test
```

Every step should answer a question.

---

# 26. Decision Matrix

| Pattern | First suspects to test |
|---|---|
| One-cylinder misfire | Coil, plug, injector, compression |
| Misfire moves with coil | Coil |
| Misfire remains after coil swap | Plug, injector, compression, local intake leak |
| Multiple cylinders misfire | Fuel supply, air leak, voltage, timing, shared power |
| Rough only at idle + positive trims | Vacuum/intake leak |
| Misfire mainly under load | Coil/plug/fuel delivery/compression |
| Cold-start-only | Ignition, injector, intake leak, mechanical/deposit issues |
| Hot-only | Heat-sensitive coil/sensor/injector/wiring |
| After refueling | Fuel quality/contamination |
| With charging warnings or many unrelated codes | System voltage/grounds |
| With cam/crank codes | Timing/sensor/correlation diagnosis before parts swapping |

---

# 27. Roadside Minimal Misfire Workflow

If stranded or remote:

```text
1. Is MIL blinking?
   YES → reduce load / stop driving

2. Read codes.

3. Record freeze frame.

4. Check battery/system voltage.

5. Inspect coil/injector connectors.

6. If one-cylinder code:
   swap coil with another cylinder.

7. Re-test only if safe.

8. If misfire moves → suspect coil.

9. If misfire stays → do not keep driving hard.
   Continue with plug/injector/compression diagnosis when tools/resources allow.
```

This workflow intentionally avoids opening the high-pressure GDI fuel system roadside.

---

# 28. When to Tow Instead of Drive

Strong reasons to stop driving include:

- MIL blinking continuously
- Severe shaking
- Major power loss
- Raw-fuel smell
- Backfiring
- Overheating
- Mechanical knocking
- Oil-pressure warning
- Misfire severe enough to make traffic operation unsafe

A short tow can protect the catalytic converter and engine.

---

# 29. After Repair: Verify, Don't Assume

After the suspected cause is repaired:

1. Ensure all connectors are fully seated.
2. Ensure tools/rags are removed from engine bay.
3. Start the engine.
4. Observe idle quality.
5. Check live misfire information if available.
6. Check fuel trims.
7. Road-test under the conditions that originally triggered the fault, if safe.
8. Re-scan for pending and stored codes.
9. Record the repair in `../maintenance/NOMAD_SERVICE_LOG.md`.

A successful repair must remove the symptom, not merely clear the code.

---

# 30. Diagnostic Incident Template

```markdown
## Misfire Incident

**Date:**
**Mileage:**
**Engine cold/warm/hot:**
**Fuel level:**
**Recent refueling:**

### Symptoms
- [ ] Rough idle
- [ ] Hesitation
- [ ] Misfire under load
- [ ] Cold-only
- [ ] Hot-only
- [ ] MIL steady
- [ ] MIL flashing

### Codes
Stored:
Pending:
Permanent:

### Freeze frame
RPM:
Vehicle speed:
Coolant temperature:
Calculated load:
STFT:
LTFT:
System voltage:
Fuel pressure data:
Other:

### Tests
Coil swap performed:
Result:

Spark plug inspection:
Result:

Injector/wiring test:
Result:

Compression/leak-down:
Result:

### Root cause

### Repair

### Verification

```

---

# 31. AI Reasoning Rules

When an AI assistant uses this document:

1. **Do not equate a `P030X` code with a failed coil.**
2. Ask whether the MIL is flashing before recommending further driving.
3. Preserve freeze-frame data before suggesting code clearing.
4. Prefer one-variable-at-a-time tests.
5. For a single-cylinder misfire, recommend coil-swap testing before buying parts when practical.
6. If the misfire does not follow the coil, widen diagnosis to plug, injector, compression, and local air leak.
7. For `P0300` or several cylinders, prioritize shared causes.
8. Never advise loosening GDI high-pressure lines as a casual fuel test.
9. Distinguish general diagnostic practice from Hyundai-specific specifications.
10. If exact plug torque, gap, compression spec, or injector spec is not verified, say **specification not yet verified**.
11. Use the vehicle's actual service history when available.
12. Rank likely causes, but explain what evidence would distinguish them.

---

# 32. Machine-Readable Summary

```yaml
vehicle:
  year: 2014
  make: Hyundai
  model: Accent
  trim: SE
  engine: 1.6L GDI inline-4

diagnostic_topic: misfire

codes:
  P0300: random_multiple_cylinder_misfire
  P0301: cylinder_1_misfire
  P0302: cylinder_2_misfire
  P0303: cylinder_3_misfire
  P0304: cylinder_4_misfire

critical_rule:
  flashing_mil:
    urgency: high
    reason: catalytic_converter_damage_risk
    action: reduce_load_and_stop_when_safe

single_cylinder_workflow:
  - preserve_diagnostic_evidence
  - inspect_connector_and_wiring
  - swap_ignition_coil_with_known_other_cylinder
  - reproduce_fault_if_safe
  - determine_whether_misfire_moves
  - inspect_test_spark_plug
  - inspect_test_injector
  - test_compression_mechanical_condition

multiple_cylinder_workflow:
  - verify_system_voltage
  - evaluate_fuel_supply
  - inspect_for_intake_vacuum_leaks
  - verify_shared_power_and_grounds
  - evaluate_sensor_plausibility
  - evaluate_cam_crank_timing

relevant_fuses:
  IGN_COIL_A: 15
  INJECTOR_A: 15
  SENSOR_A: 10
  ECU_2_A: 10
  ECU_1_A: 30
  F_PUMP_A: 15

gdi_safety:
  open_high_pressure_fuel_system_roadside: false
  loosen_line_to_check_for_fuel: false

ai_policy:
  dtc_is_not_failed_part: true
  preserve_freeze_frame_before_clear: true
  change_one_variable_at_a_time: true
  require_verified_exact_specs: true
```

---

# 33. Sources and Provenance

## Hyundai

- 2014 Hyundai Accent Owner's Manual: Hyundai's emissions warnings state that engine malfunction/misfire can lead to catalytic-converter damage and that low fuel operation can contribute to misfire.
- Searchable owner-manual mirror: https://manualzz.com/doc/53857913/hyundai-2014-accent-owner-manual

## Standards

- SAE J2012 — Diagnostic Trouble Code Definitions: https://saemobilus.sae.org/standards/j2012_202509-diagnostic-trouble-code-definitions

## Repository-internal source hierarchy

For exact component specifications:

1. VIN/build-specific Hyundai service information
2. Hyundai owner's/service documentation
3. OEM component-manufacturer documentation
4. Reputable professional diagnostic sources
5. Generic Internet references

When sources disagree, record the disagreement.

---

# 34. Core Philosophy

```text
MISFIRE
  ↓
PROTECT THE CATALYST
  ↓
PRESERVE EVIDENCE
  ↓
ONE CYLINDER OR MANY?
  ↓
MOVE / TEST ONE THING AT A TIME
  ↓
IGNITION → FUEL → AIR → COMPRESSION / TIMING
  ↓
IDENTIFY ROOT CAUSE
  ↓
REPAIR
  ↓
VERIFY
```

Not:

```text
P0302 → BUY FOUR COILS
```

---

## Document Status

- **Vehicle:** 2014 Hyundai Accent SE
- **Topic:** Misfire diagnostics
- **Status:** Initial field guide
- **Exact plug torque/gap:** intentionally omitted pending authoritative verification
- **Exact compression specification:** intentionally omitted pending authoritative verification
- **High-pressure GDI procedures:** intentionally limited to safe diagnostic boundaries
- **Copyright approach:** original diagnostic documentation; does not reproduce service-manual procedures verbatim
