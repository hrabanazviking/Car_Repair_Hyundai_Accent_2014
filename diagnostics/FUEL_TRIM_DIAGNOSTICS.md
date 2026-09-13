# 2014 Hyundai Accent SE — Fuel Trim Diagnostics

> **Purpose:** A practical, source-aware guide to diagnosing lean/rich conditions with Short-Term Fuel Trim (STFT), Long-Term Fuel Trim (LTFT), MAP, IAT, oxygen/A/F feedback, purge behavior, fuel pressure data, and related OBD-II evidence on a U.S.-market 2014 Hyundai Accent SE 1.6 L GDI.
>
> **Core rule:** Fuel trim is the ECU describing the **correction it is making**, not naming the failed part.

---

## 1. Scope

This document focuses on fuel-control diagnosis for the 2014 Hyundai Accent SE with the 1.6 L GDI engine.

Related repository files:

- `OBD2_GUIDE.md`
- `MISFIRE.md`
- `CRANK_NO_START.md`
- `CHARGING_SYSTEM.md`
- `../specs/FLUIDS_AND_CAPACITIES.md`
- `../specs/VEHICLE_BASELINE.md`
- `../guides/ROADSIDE_DIAGNOSTIC_TRIAGE.md`

This guide is intended for:

- Generic OBD-II scan tools
- Hyundai-capable enhanced scanners
- Human diagnosis
- Offline AI/RAG retrieval

---

# 2. Important Accent-Specific Architecture

The Gamma 1.6 L GDI engine used in this generation of Accent uses a **speed-density** strategy centered around a Manifold Absolute Pressure sensor (MAP) and Intake Air Temperature sensor (IAT), rather than relying on a conventional MAF sensor as the primary airflow-measurement device.

Hyundai service information for the closely related 2012–2013 Accent 1.6 L documents:

- MAP sensor mounted on the intake/surge tank
- IAT sensing integrated with the MAP assembly
- Electronic throttle control (ETC)
- Upstream linear oxygen/A/F sensing
- Downstream oxygen sensing
- Purge Control Solenoid Valve (PCSV)
- Positive Crankcase Ventilation (PCV) system
- GDI high-pressure fuel system
- Rail pressure sensor
- Fuel pressure control valve

### Diagnostic consequence

Generic advice such as:

```text
P0171 → clean the MAF sensor
```

is not a good default for this vehicle.

For this Accent, think instead about:

- unmetered / unexpected air entering the manifold
- MAP plausibility
- IAT plausibility
- throttle position / commanded airflow
- purge flow
- PCV flow
- fuel delivery and rail pressure
- injector behavior
- exhaust leaks affecting feedback
- upstream A/F sensor feedback

### Sources

- Hyundai/Accent service information mirror — intake manifold and sensor layout: https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Engine%2C%20Cooling%20and%20Exhaust/Engine/Intake%20Manifold/Service%20and%20Repair/Repair%20Procedures/
- Hyundai/Accent service information mirror — MAP sensor description: https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Powertrain%20Management/Computers%20and%20Control%20Systems/Sensors%20and%20Switches%20-%20Computers%20and%20Control%20Systems/Manifold%20Pressure%2FVacuum%20Sensor/Description%20and%20Operation/

---

# 3. What Fuel Trim Means

The engine control module continuously adjusts injector delivery to keep combustion near the commanded air/fuel target when operating in closed loop.

Two commonly exposed OBD-II values are:

- **STFT — Short-Term Fuel Trim**
- **LTFT — Long-Term Fuel Trim**

## STFT

STFT is the fast correction.

It reacts relatively quickly to feedback from the upstream oxygen/A/F sensing system.

Examples:

```text
STFT +8%
```

means the ECU is currently adding fuel relative to its base calculation.

```text
STFT -8%
```

means the ECU is currently subtracting fuel.

## LTFT

LTFT is the slower learned/adaptive correction.

It represents a longer-term adjustment learned by the ECU as conditions persist.

Bosch diagnostic documentation describes LTFT as the ECU's steady long-term correction and notes that it changes more slowly than STFT.

Source:

- Bosch Global OBD-II operator documentation: https://cdr.boschdiagnostics.com/pro/sites/pro/files/tech_1a_global_obd_ii_operators_manual.pdf

---

# 4. Positive and Negative Trim

A useful mental model:

```text
POSITIVE trim = ECU adds fuel
NEGATIVE trim = ECU removes fuel
```

Therefore:

## Positive trim can indicate

- Extra air entering the engine
- Too little fuel being delivered
- Incorrect MAP/IAT information
- Exhaust feedback falsely indicating lean
- Purge/PCV air-flow problems

## Negative trim can indicate

- Excess fuel entering the engine
- Injector leakage
- Excessive commanded/delivered fuel pressure
- Purge system supplying too much vapor
- Incorrect temperature/load information
- Upstream feedback falsely indicating rich

Do not translate positive trim directly into “vacuum leak” or negative trim directly into “bad injector.”

---

# 5. Combined Fuel Correction

For practical diagnosis, consider both STFT and LTFT together.

A useful approximation is:

```text
TOTAL CORRECTION ≈ STFT + LTFT
```

Example:

```text
STFT = +7%
LTFT = +11%

Approximate total correction = +18%
```

This does not mean the engine is literally receiving exactly 18% more fuel under every condition. It is a practical diagnostic shorthand for understanding the direction and magnitude of adaptive correction.

---

# 6. What Is “Normal”?

There is no single universal trim number that proves an engine is healthy.

Trim behavior varies with:

- Engine temperature
- Load
- RPM
- Altitude
- Fuel composition
- Purge operation
- Electrical load
- ECU calibration
- Driving history

Bosch diagnostic documentation gives **±10% at warm idle** as an expected generic reference range for LTFT in its Global OBD guide.

For field diagnosis, this repository uses the following **general diagnostic heuristic**, not a Hyundai factory pass/fail specification:

| Combined / persistent behavior | General interpretation |
|---|---|
| Around 0%, small movement | Often normal |
| Within roughly ±5% | Generally very good |
| Around ±5–10% | Usually plausible; evaluate context |
| Persistently beyond roughly ±10% | Worth investigating |
| Around ±15–20% or more | Strong evidence of a significant correction problem |

### Important

These are **diagnostic heuristics**, not Hyundai DTC thresholds.

Do not condemn a component because a trim number briefly crosses one of these values.

---

# 7. Closed Loop vs. Open Loop

Fuel trims are most useful when the engine is in a valid **closed-loop** operating state.

During open loop, the ECU may not be using oxygen/A/F feedback in the normal adaptive way.

Open-loop operation may occur during conditions such as:

- Cold start
- Heavy acceleration
- Certain fault states
- Deceleration fuel cut
- Other calibration-specific operating modes

Before interpreting trims, record:

- Fuel-system status
- Coolant temperature
- RPM
- Load
- Vehicle speed
- Whether the engine is fully warm

Do not interpret a cold-start trim snapshot as if it were a stabilized warm-idle reading.

---

# 8. The Most Useful Test: Idle vs. Raised RPM

One of the strongest low-tool fuel-trim tests is to compare correction at:

1. Warm stabilized idle
2. Approximately 2,000–2,500 RPM with no load, briefly and safely

Record:

- STFT
- LTFT
- MAP
- RPM
- ECT
- IAT
- upstream A/F/O2 data if supported

## Pattern A — Very positive at idle, much better at 2,000–2,500 RPM

Example:

```text
Warm idle:
STFT +12
LTFT +14
Approx total +26

2500 RPM:
STFT +2
LTFT +10
Approx total +12
```

This pattern strongly suggests a problem whose effect is largest when manifold vacuum is high and airflow is low.

Investigate:

- Intake manifold leak
- Vacuum hose leak
- PCV hose/system leak
- Brake-booster vacuum leak
- Throttle-body/intake gasket leak
- Purge valve flowing when it should not

A Ford diagnostic bulletin documents this same general principle: a vacuum leak's percentage effect tends to decrease as engine airflow rises.

Source:

- Ford fuel-trim vacuum-leak diagnostic bulletin mirror: https://www.aa1car.com/library/ford_tsb_04-17-4.pdf

This is used here as **general diagnostic methodology**, not as a Hyundai calibration specification.

---

# 9. Pattern B — Positive at Idle and Still Positive at Raised RPM / Load

Example:

```text
Idle total correction: +18%
2500 RPM total correction: +20%
```

Because the correction does not substantially improve as airflow increases, investigate causes that affect the mixture across a wider operating range.

Possible causes include:

- Low fuel delivery
- Rail-pressure problem
- Restricted fuel supply
- Injector flow restriction
- MAP bias
- Incorrect IAT or ECT information
- Upstream A/F sensor bias
- Exhaust leak ahead of the upstream sensor
- Fuel quality issue

For the GDI Accent, do not open high-pressure fuel fittings as a roadside diagnostic test.

Use scan data and the proper Hyundai test procedure.

---

# 10. Pattern C — Normal Idle, Positive Under Load

If trim is reasonable at idle but becomes strongly positive as load rises, suspect a problem that emerges when fuel demand or airflow increases.

Possible causes:

- Insufficient fuel delivery under load
- High-pressure GDI supply problem
- Fuel-pressure control issue
- Injector flow limitation
- MAP/load calculation problem
- Exhaust/A/F feedback issue

Also review:

- Misfire data
- Rail-pressure commanded vs. actual, if enhanced data is available
- Battery/charging voltage

A weak electrical system can disturb multiple control systems and should be ruled out before chasing complex fuel faults.

---

# 11. Pattern D — Strongly Negative Trim

Persistent negative trim means the ECU is subtracting fuel.

Investigate:

- Leaking injector
- Fuel-pressure control fault
- Excess purge-vapor flow
- Incorrect coolant-temperature signal
- Incorrect MAP/IAT/load information
- Upstream A/F sensor bias
- Contaminated fuel
- Combustion/misfire conditions confusing feedback

### Rich-code context

Common generic rich-system codes include:

```text
P0172 — System Too Rich, Bank 1
```

The 1.6 L inline-four has one cylinder bank for this purpose: **Bank 1**.

Do not search for a nonexistent Bank 2 on this engine.

---

# 12. P0171 — System Too Lean, Bank 1

`P0171` does not mean:

```text
replace oxygen sensor
```

or:

```text
replace fuel pump
```

It means the control system has reached calibration-defined lean correction criteria.

Potential causes include:

- Intake/vacuum leak
- PCV leak
- Purge valve leaking/open at an inappropriate time
- Low fuel delivery
- High-pressure fuel-system problem
- Restricted injector(s)
- MAP/IAT bias
- Exhaust leak ahead of upstream sensor
- Upstream A/F sensor bias
- Fuel quality issue

Older Hyundai service information likewise treats the air/fuel control system as a whole, including intake, exhaust, evaporative system, injectors, fuel pressure, and pump rather than treating `P0171` as a single-component code.

Source:

- Hyundai Accent service information mirror, P0171 background: https://charm.li/Hyundai/2003/Accent%20L4-1.6L/Repair%20and%20Diagnosis/A%20L%20L%20%20Diagnostic%20Trouble%20Codes%20%28%20DTC%20%29/Testing%20and%20Inspection/P%20Code%20Charts/P0171/

Use the older Hyundai page only for the **system-level diagnostic concept**, not for 2014 thresholds or hardware specifications.

---

# 13. P0172 — System Too Rich, Bank 1

Potential causes include:

- Excess fuel pressure / control problem
- Injector leakage
- Purge vapor entering excessively
- Incorrect ECT/IAT/MAP data
- Upstream A/F sensor bias
- Restricted intake airflow
- Fuel contamination / incorrect fuel composition

Inspect evidence before replacing parts.

---

# 14. MAP Sensor: High-Value Cross-Check

The Accent's MAP sensor is particularly important because it is part of the engine's airflow/load calculation.

## Key-on, engine-off plausibility

With the engine off and ignition on, MAP should be reasonably close to local barometric pressure.

It will vary with altitude and weather.

If MAP reports an implausible atmospheric pressure before startup, suspect:

- MAP sensor bias
- Sensor wiring/reference problem
- Ground problem
- Scan-tool decoding issue

## Warm idle plausibility

At warm idle, manifold pressure should be substantially below atmospheric pressure because the engine is producing manifold vacuum.

Bosch generic OBD documentation notes approximately **40 kPa at warm idle near sea level** as a typical generic reference.

This is **not a Hyundai specification**.

Altitude, cam timing, engine load, A/C operation, and other conditions affect MAP.

## Snap-throttle behavior

When the throttle is opened quickly, manifold pressure should move toward atmospheric pressure.

A MAP reading that is physically implausible or sluggish can distort load calculation and fuel control.

---

# 15. IAT and ECT Plausibility

Before a cold start after the car has sat long enough to fully heat-soak to ambient conditions:

```text
IAT ≈ ambient temperature
ECT ≈ ambient temperature
```

They need not match perfectly.

But a large implausible difference can indicate:

- Temperature sensor bias
- Wiring issue
- Connector issue
- Scan-data problem

A false cold ECT reading can command unnecessary enrichment.

A false hot reading can distort cold-start fueling and other strategies.

---

# 16. Purge Control Solenoid Valve (PCSV)

The Accent's evaporative-emissions system includes a Purge Control Solenoid Valve.

If purge flow occurs when the ECU does not expect it, the engine can receive additional fuel vapor and/or airflow.

Possible symptoms can include:

- Rough idle
- Hard restart after refueling
- Rich or lean correction depending on conditions
- EVAP-related DTCs
- Fuel-trim changes when purge command changes

### Diagnostic principle

Compare fuel-trim behavior with purge command/data where supported.

Do not assume the purge valve is bad solely because a trim problem exists.

Inspect hoses and system integrity as well.

---

# 17. PCV System

The PCV system connects the crankcase to intake vacuum.

A damaged hose, incorrect connection, stuck valve, or leak can create an intake-air path that affects fuel trim.

Inspect for:

- Split hose
- Loose connection
- Collapsed hose
- Oil saturation/deterioration
- Abnormal crankcase vacuum behavior

Do not clamp or disable PCV as a permanent repair.

---

# 18. Exhaust Leaks Can Mimic Lean Operation

An exhaust leak ahead of the upstream oxygen/A/F sensor can allow outside oxygen into the exhaust stream.

The ECU may interpret that oxygen as lean combustion and add fuel.

Therefore:

```text
POSITIVE FUEL TRIM
      ≠
INTAKE LEAK ONLY
```

Inspect for:

- Exhaust manifold leak
- Gasket leak
- Cracked exhaust component
- Loose sensor bung
- Damage after underbody/rough-road impact

This is particularly relevant for a vehicle used on primitive roads.

---

# 19. Misfire Can Corrupt Fuel-Trim Interpretation

A misfiring cylinder may send unburned oxygen into the exhaust.

The upstream sensor can interpret the excess oxygen as a lean condition even when fuel delivery is not actually insufficient.

Therefore:

```text
MISFIRE + POSITIVE TRIM
```

must not automatically be diagnosed as a fuel-pressure problem or intake leak.

Check `MISFIRE.md` first when active misfire codes or counters are present.

---

# 20. GDI Fuel Pressure

This Accent uses Gasoline Direct Injection.

Fuel diagnosis may involve both:

- Low-pressure supply side
- High-pressure GDI side

Enhanced Hyundai scan data may expose useful values such as:

- Commanded rail pressure
- Actual rail pressure
- Fuel-pressure control parameters

## Critical safety rule

**Never loosen a high-pressure GDI line to “see whether fuel comes out.”**

High-pressure gasoline can penetrate skin and can ignite.

Use scan data and validated service procedures.

If invasive pressure-system work is required, follow the proper Hyundai pressure-release and service procedure.

---

# 21. Upstream vs. Downstream Oxygen/A/F Data

The upstream sensor is primarily involved in mixture feedback.

The downstream sensor is primarily used for catalyst monitoring.

Do not treat both sensors as interchangeable diagnostic signals.

The upstream sensor on this engine generation is documented as a **linear zirconia sensor**, while the downstream sensor is a binary zirconia sensor in related Hyundai service information.

Source:

- Hyundai Accent powertrain-management specifications mirror: https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Powertrain%20Management/Specifications/

### Diagnostic rule

Do not apply old-school narrowband `0.1–0.9 V switching` rules to every upstream A/F sensor PID without verifying how the scanner represents that sensor.

Many scan tools translate or expose wideband/linear A/F data differently.

Use:

- Lambda
- Equivalence ratio
- A/F current
- Manufacturer-enhanced data

when available and properly identified.

---

# 22. A Practical Fuel-Trim Capture Procedure

For a warm running engine with no immediate safety problem:

## Step 1 — Preserve codes

Record:

- Stored DTCs
- Pending DTCs
- Permanent DTCs
- Freeze frame

## Step 2 — Verify operating state

Record:

- Closed/open loop status
- ECT
- IAT
- Battery/system voltage

## Step 3 — Warm idle snapshot

Record:

- RPM
- STFT Bank 1
- LTFT Bank 1
- MAP
- Throttle position / commanded throttle if available
- Upstream A/F/O2 data
- Purge command if available
- Fuel pressure / rail pressure if available

Let idle stabilize before judging a single number.

## Step 4 — Brief raised-RPM snapshot

Hold approximately 2,000–2,500 RPM briefly in Park/Neutral under safe conditions.

Record the same PIDs.

Do not hold high RPM unnecessarily.

## Step 5 — Compare patterns

Ask:

```text
Did correction improve substantially as RPM/airflow increased?
```

If yes:

```text
Investigate vacuum / intake / PCV / purge-type faults first
```

If no:

```text
Investigate fuel delivery, sensor bias, exhaust feedback, or broader mixture-control faults
```

---

# 23. Diagnostic Pattern Matrix

| Fuel-trim pattern | Higher-probability directions |
|---|---|
| Positive mainly at idle, improves at 2500 RPM | Intake/vacuum/PCV/purge leak |
| Positive idle and 2500 RPM | Fuel delivery, injector restriction, sensor bias, exhaust leak |
| Normal idle, positive with load | Fuel-delivery limitation, rail-pressure problem, load-calculation issue |
| Negative mainly at idle | Purge/injector leak, sensor bias, localized rich condition |
| Negative across most conditions | Excess fuel pressure/delivery, sensor bias, purge issue |
| Wildly oscillating with misfire | Diagnose misfire first |
| Trims strange after battery disconnect | Adaptation may be relearning; inspect only if persistent |
| Multiple unrelated codes + trim issues | Check charging voltage and grounds first |

This matrix is a prioritization tool, not proof.

---

# 24. Fuel Trim After Battery Disconnect / Code Clear

Clearing diagnostic memory or disconnecting battery power can erase learned adaptation.

Immediately afterward:

- LTFT may reset or change substantially.
- Idle behavior may temporarily differ.
- Readiness monitors reset.
- The ECU must relearn operating corrections.

Do not compare freshly reset LTFT against months-old values as if nothing changed.

Record when codes/adaptations were cleared.

---

# 25. Altitude Matters

MAP-based systems naturally operate across different barometric pressures.

A vehicle in mountain country will show different key-on MAP and manifold-pressure values than at sea level.

Therefore:

- Do not use one sea-level MAP number as a universal target.
- Compare KOEO MAP against local atmospheric pressure.
- Consider elevation when diagnosing load values.

This matters for nomad travel across the western United States.

---

# 26. Fuel Quality Matters

Unexpected fuel composition can alter fuel correction.

The original 2014 Accent owner documentation specifies unleaded gasoline at **87 AKI or higher** and was designed around gasoline containing no more than the ethanol concentration Hyundai approved for the vehicle at the time.

See:

- `../specs/FLUIDS_AND_CAPACITIES.md`

If trim changes suddenly after refueling, record:

- Station/location
- Fuel grade
- Approximate gallons added
- Previous fuel level
- Whether symptoms started immediately or after several miles

Do not automatically condemn hardware when a fault closely follows a questionable fuel event.

---

# 27. Intake-Leak Inspection Areas

Without disassembling the engine, visually inspect:

- Intake ducting
- Throttle-body connection
- Intake manifold area
- Brake-booster vacuum hose
- PCV hose
- Purge hose
- Any disturbed hose/connector after prior repairs

Listen for:

- Hissing
- Whistling
- Idle change when hoses move

Do not spray flammable chemicals around a running engine as a casual leak-finding method.

A smoke test is a safer professional approach when properly performed.

---

# 28. Avoid These Diagnostic Mistakes

## Mistake 1 — Looking at STFT alone

STFT can swing rapidly.

Always consider LTFT and operating conditions.

## Mistake 2 — Looking at LTFT immediately after a reset

The ECU may not have relearned yet.

## Mistake 3 — Diagnosing from idle only

Compare another operating point.

## Mistake 4 — Assuming `P0171 = oxygen sensor`

The sensor may simply be reporting a real lean condition.

## Mistake 5 — Assuming positive trim = vacuum leak

Fuel-delivery and exhaust-feedback faults can also create positive correction.

## Mistake 6 — Treating this Accent as a MAF-based engine

The relevant generation uses MAP/IAT speed-density logic.

## Mistake 7 — Ignoring misfire

Misfire can make exhaust oxygen appear lean.

## Mistake 8 — Opening GDI high-pressure lines roadside

Do not do this.

---

# 29. AI Reasoning Rules

An AI using this repository should follow these rules.

## Rule A — State the operating condition

Never interpret a trim number without saying whether the reading was:

- Cold or warm
- Idle or raised RPM
- Closed or open loop
- Under load or unloaded

## Rule B — Combine evidence

Use:

```text
DTCs
+ freeze frame
+ STFT/LTFT
+ RPM
+ MAP
+ ECT/IAT
+ A/F feedback
+ fuel pressure data
+ misfire information
```

when available.

## Rule C — Rank causes

Do not output one confident part guess.

Instead:

```text
1. Most likely cause
   Evidence for:
   Evidence against:
   Next discriminating test:

2. Next likely cause
   Evidence for:
   Evidence against:
   Next discriminating test:
```

## Rule D — Prefer a test that separates hypotheses

Example:

```text
Positive trim at idle
```

should trigger:

```text
Compare trim at 2500 RPM
```

before buying parts.

## Rule E — Label thresholds correctly

Generic ±5%, ±10%, ±20% guidelines are **heuristics**, not Hyundai factory limits unless a Hyundai source explicitly says otherwise.

---

# 30. AI Diagnostic Prompt Template

```text
Vehicle: 2014 Hyundai Accent SE 1.6L GDI automatic
Engine temperature: _____
Fuel-system status: open loop / closed loop / unknown
RPM: _____
STFT Bank 1: _____ %
LTFT Bank 1: _____ %
MAP: _____ kPa
IAT: _____
ECT: _____
System voltage: _____
Upstream A/F or lambda: _____
Purge command: _____
Rail pressure actual: _____
Rail pressure commanded: _____
Misfire codes/counters: _____
Stored codes: _____
Pending codes: _____
Freeze frame: _____
Symptoms: _____
Recent refueling/repairs: _____

Compare idle and raised-RPM data if both are provided. Rank causes by evidence. Distinguish intake-air, purge/PCV, fuel-delivery, sensor-bias, exhaust-leak, and misfire possibilities. Do not recommend replacing a component until you identify a test that would distinguish it from competing causes.
```

---

# 31. Field Log Template

```markdown
## Fuel Trim Diagnostic Session

**Date:**
**Mileage:**
**Elevation / location:**
**Fuel level:**
**Recent refueling:**
**ECT:**
**IAT:**
**Closed loop:** yes / no
**System voltage:**

### Idle
- RPM:
- STFT B1:
- LTFT B1:
- Approx total correction:
- MAP:
- Upstream A/F / lambda:
- Purge command:
- Rail pressure commanded:
- Rail pressure actual:

### 2000–2500 RPM
- RPM:
- STFT B1:
- LTFT B1:
- Approx total correction:
- MAP:
- Upstream A/F / lambda:
- Purge command:
- Rail pressure commanded:
- Rail pressure actual:

### DTCs
- Stored:
- Pending:
- Permanent:

### Misfire data


### Interpretation


### Next discriminating test


### Repair / outcome

```

---

# 32. Machine-Readable Summary

```yaml
vehicle:
  year: 2014
  make: Hyundai
  model: Accent
  trim: SE
  engine: 1.6L_GDI_inline_4
  banks: 1

fuel_trim:
  stft:
    meaning: fast_feedback_correction
    positive: ecu_adding_fuel
    negative: ecu_removing_fuel
  ltft:
    meaning: learned_long_term_correction
    positive: ecu_adding_fuel
    negative: ecu_removing_fuel

architecture:
  airflow_strategy: speed_density
  primary_load_sensor: MAP
  intake_temperature_sensor: IAT
  conventional_primary_MAF: false
  electronic_throttle: true
  direct_injection: true
  purge_control_solenoid: true
  pcv_system: true

heuristics_not_factory_limits:
  excellent_trim: approximately_within_plus_minus_5_percent
  investigate_persistent: approximately_beyond_plus_minus_10_percent
  significant_correction: approximately_plus_minus_15_to_20_percent_or_more

pattern_logic:
  positive_idle_improves_with_rpm:
    investigate:
      - intake_vacuum_leak
      - pcv_leak
      - purge_leak
      - brake_booster_vacuum_leak
  positive_idle_and_rpm:
    investigate:
      - fuel_delivery
      - injector_flow
      - MAP_IAT_bias
      - upstream_AF_sensor_bias
      - pre_sensor_exhaust_leak
  normal_idle_positive_load:
    investigate:
      - fuel_delivery_under_load
      - rail_pressure_control
      - injector_flow
      - load_calculation
  negative_persistent:
    investigate:
      - injector_leak
      - excess_fuel_pressure
      - purge_vapor
      - sensor_bias

safety:
  high_pressure_GDI_lines:
    roadside_opening: prohibited
    reason: high_pressure_fuel_injection_fire_injury_risk

ai_rules:
  - interpret_trim_only_with_operating_condition
  - combine_STFT_and_LTFT
  - compare_idle_with_raised_rpm
  - diagnose_misfire_before_trusting_lean_trim
  - do_not_assume_MAF_fault
  - rank_causes_and_propose_discriminating_tests
  - label_generic_thresholds_as_heuristics
```

---

# 33. Source Notes

Primary technical references used for this document:

- Bosch Global OBD-II documentation — definitions and generic PID behavior: https://cdr.boschdiagnostics.com/pro/sites/pro/files/tech_1a_global_obd_ii_operators_manual.pdf
- Snap-on fuel-trim adaptation overview: https://www.snapon.com/EN/UK/Diagnostics/News-Centre/Technical-Focus-Archive/fuel-trim-adaptation
- Snap-on Global OBD documentation: https://www1.snapon.com/Files/Diagnostics/UserManuals/GlobalOBDVehicleCommunicationSoftwareManual_EAZ0025B43.pdf
- Hyundai Accent service-information mirror — 2012–2013 MAP/IAT, PCSV, ETC and intake architecture: https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Engine%2C%20Cooling%20and%20Exhaust/Engine/Intake%20Manifold/Service%20and%20Repair/Repair%20Procedures/
- Hyundai Accent service-information mirror — speed-density MAP description: https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Powertrain%20Management/Computers%20and%20Control%20Systems/Sensors%20and%20Switches%20-%20Computers%20and%20Control%20Systems/Manifold%20Pressure%2FVacuum%20Sensor/Description%20and%20Operation/
- Ford fuel-trim/vacuum-leak diagnostic methodology, used only as general diagnostic practice: https://www.aa1car.com/library/ford_tsb_04-17-4.pdf

When a generic diagnostic reference conflicts with VIN/build-specific Hyundai service information, **Hyundai vehicle-specific information wins**.

---

# 34. Core Diagnostic Philosophy

```text
TRIM TELLS YOU THE DIRECTION OF CORRECTION
              ↓
OPERATING PATTERN TELLS YOU WHERE TO LOOK
              ↓
TESTS SEPARATE THE POSSIBLE CAUSES
              ↓
ONLY THEN REPLACE A PART
```

Or, more compactly:

```text
DATA → PATTERN → HYPOTHESIS → TEST → ROOT CAUSE
```

Not:

```text
P0171 → BUY OXYGEN SENSOR
```

---

## Document Status

- **Vehicle:** 2014 Hyundai Accent SE 1.6 L GDI
- **Purpose:** Fuel-trim/live-data diagnosis
- **Status:** Initial source-aware diagnostic guide
- **Exact Hyundai DTC enable thresholds:** Not guessed
- **Fuel-trim percentage bands:** Explicitly labeled as general diagnostic heuristics
- **GDI invasive testing:** Intentionally excluded from roadside procedures
