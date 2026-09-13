# 2014 Hyundai Accent SE — OBD-II Diagnostic Guide

> **Purpose:** A practical, source-aware guide to using OBD-II diagnostics on a U.S.-market 2014 Hyundai Accent SE. It is written for both human field use and retrieval by an offline AI assistant/RAG system.
>
> **Core rule:** A diagnostic trouble code is **evidence**, not a parts order.

---

## 1. Scope

This document explains how to use generic OBD-II data intelligently on the 2014 Hyundai Accent SE, including:

- Diagnostic Trouble Codes (DTCs)
- Stored, pending, and permanent codes
- Freeze-frame data
- Readiness monitors
- Live Parameter IDs (PIDs)
- Fuel trims
- Misfire-related diagnosis
- Mode $06 monitor test results
- Clearing codes and what information is lost
- Generic versus Hyundai-enhanced diagnostics
- OBD connector basics
- AI-friendly diagnostic recording

Related repository files:

- `../guides/ROADSIDE_DIAGNOSTIC_TRIAGE.md`
- `../specs/FUSES_AND_RELAYS.md`
- `../specs/VEHICLE_BASELINE.md`
- `../maintenance/NOMAD_SERVICE_LOG.md`

---

# 2. What OBD-II Actually Is

OBD-II is a standardized emissions-related diagnostic interface used by the vehicle to report information to external diagnostic equipment.

The standards behind the system include SAE J1979 for diagnostic services/data exchange and SAE J2012 for standardized diagnostic trouble-code definitions and formats.

For a 2014 U.S.-market passenger car, the generic OBD-II interface communicates through CAN.

Generic OBD-II is extremely useful, but it does **not** expose every diagnostic function in every vehicle module.

A basic generic scanner may primarily access emissions-related powertrain data, while a Hyundai-capable enhanced scanner may additionally communicate with systems such as:

- ABS
- Airbag/SRS
- Transmission control
- Electric power steering / MDPS
- Body control module
- TPMS
- Other manufacturer-specific controllers

Therefore:

```text
NO GENERIC OBD CODE
        ≠
NO VEHICLE FAULT
```

A steering, ABS, airbag, body-electrical, or network fault may require enhanced module access.

---

# 3. OBD-II Connector Basics

The vehicle has a standardized 16-pin diagnostic connector.

Important standardized pins include:

| Pin | Function |
|---|---|
| 4 | Chassis ground |
| 5 | Signal ground |
| 6 | CAN High |
| 14 | CAN Low |
| 16 | Battery positive power |

## If the scanner will not power on

Check:

1. Ignition/key position.
2. Scanner condition.
3. OBD connector damage.
4. Power at pin 16.
5. Grounds at pins 4 and 5.
6. Related fuses.

See `../specs/FUSES_AND_RELAYS.md` for vehicle fuse information.

## Safety

Never short OBD connector pins together.

Do not probe terminals carelessly with oversized meter probes that can spread or damage connector contacts.

---

# 4. SAE Diagnostic Service Modes

Classic generic OBD-II diagnostic services are commonly described as "modes."

| Service / Mode | Primary purpose |
|---|---|
| Mode $01 | Current powertrain diagnostic data / live data |
| Mode $02 | Freeze-frame data |
| Mode $03 | Confirmed emission-related DTCs |
| Mode $04 | Clear/reset emission-related diagnostic information |
| Mode $05 | Oxygen-sensor test results on older implementations |
| Mode $06 | On-board monitor test results |
| Mode $07 | Pending DTCs from current/recent driving cycle |
| Mode $08 | Control of supported on-board system/test/component |
| Mode $09 | Vehicle information such as VIN/calibration data where supported |
| Mode $0A | Permanent emission-related DTCs |

Modern scan tools usually hide these mode numbers behind friendly menus.

The important point is that different data types come from different services and have different diagnostic meanings.

---

# 5. Diagnostic Trouble Code Structure

A familiar OBD-II code looks like:

```text
P0302
```

The first letter identifies the broad system family:

| Prefix | System family |
|---|---|
| P | Powertrain |
| B | Body |
| C | Chassis |
| U | Network / communication |

The remaining characters identify the code allocation and specific fault.

Do not rely on oversimplified internet rules such as "0 always means generic and 1 always means manufacturer-specific" for every possible modern code range. SAE J2012 defines both standardized and manufacturer-reserved ranges, and newer formats have expanded over time.

For practical field use:

- `P0xxx` contains many familiar standardized powertrain codes.
- `P1xxx` commonly contains manufacturer-specific powertrain codes.
- Other ranges can contain a mixture depending on the code family and applicable standard revision.

**Always decode the complete code from a trustworthy source.**

---

# 6. Stored / Confirmed Codes

A confirmed or stored code means the diagnostic system has met the criteria required to record the fault as confirmed.

A stored code does not prove that:

- The named component itself is defective.
- The fault is currently active.
- Replacing the named sensor will fix the vehicle.

Example:

```text
P0335 — Crankshaft Position Sensor "A" Circuit
```

Possible root causes can include:

- Failed sensor
- Open circuit
- Short circuit
- Damaged connector
- Wiring damage
- Poor power or ground where applicable
- Reluctor/tone-wheel problem
- Mechanical timing issue
- ECU/PCM connection problem
- Severe low-voltage condition

The correct mental model is:

```text
CODE → SYSTEM/CIRCUIT TO INVESTIGATE
```

not:

```text
CODE → PART TO BUY
```

---

# 7. Pending Codes

A pending code means the OBD system has detected a fault condition but the criteria for a confirmed code may not yet be complete.

Pending codes are especially useful for intermittent problems.

Examples:

- A misfire occurred once but has not yet repeated enough to mature into a confirmed code.
- A sensor reading temporarily failed a monitor.
- An emissions monitor saw suspicious behavior during the current or previous driving cycle.

## Practical rule

**Always read pending codes before clearing anything.**

A pending code may be the only electronic breadcrumb left by an intermittent problem.

---

# 8. Permanent DTCs

Permanent Diagnostic Trouble Codes are stored in nonvolatile memory.

On vehicles supporting them, a permanent DTC cannot simply be erased by:

- Using a scan tool to clear codes
- Disconnecting the battery
- Removing ECU power

The OBD system itself clears the permanent code only after the underlying fault has been corrected and the relevant monitor has run successfully under the required conditions.

For a 2014 vehicle, permanent DTC capability should be expected.

## Why this is useful

A vehicle may show:

```text
MIL OFF
Stored codes: none
Permanent code: P0xxx
```

That can mean:

- A fault existed previously.
- Someone cleared the ordinary diagnostic memory.
- The monitor has not yet completed enough successful testing to erase the permanent record.

It does **not** automatically mean the fault is still active.

### AI rule

When a permanent code exists but no current/pending fault is present:

1. Identify what monitor must verify the repair.
2. Check readiness state.
3. Check whether the vehicle has had sufficient normal operation since repair/code clearing.
4. Do not recommend replacing a component solely because the permanent code remains.

---

# 9. Freeze-Frame Data

Freeze frame is a snapshot of operating conditions when a qualifying fault was detected.

Depending on what the ECU and scanner support, freeze frame may contain values such as:

- Engine RPM
- Vehicle speed
- Engine coolant temperature
- Calculated engine load
- Fuel trims
- Intake-air temperature
- MAP data
- Throttle position
- Fuel-system status
- System voltage

Freeze frame can often be more diagnostically useful than the DTC itself.

## Example

Suppose a code appears for a lean condition.

Freeze frame A:

```text
RPM: 720
Vehicle speed: 0 mph
Load: low
STFT: +24%
LTFT: +18%
```

This pattern may point toward a problem most severe at idle, such as unmetered air or a vacuum/intake leak.

Freeze frame B:

```text
RPM: 3100
Vehicle speed: 68 mph
Load: high
STFT: +23%
LTFT: +17%
```

A lean condition that appears under load can lead diagnosis toward different possibilities, such as fuel-delivery limitations.

Same DTC family, different evidence.

## Rule

**Record freeze frame before clearing codes.**

---

# 10. Readiness Monitors

OBD-II continuously or periodically tests emissions-related systems.

Readiness status tells you whether required monitors have completed their diagnostic checks since memory was last reset.

Common monitor categories include items such as:

- Misfire
- Fuel system
- Comprehensive components
- Catalyst
- Evaporative emissions system
- Oxygen / air-fuel sensor related monitoring
- Oxygen-sensor heater monitoring

Exact monitor names shown depend on scanner and vehicle support.

## Ready / Complete

The monitor has completed its required diagnostic evaluation.

## Not Ready / Incomplete

The monitor has not yet completed since the last reset or conditions required to run it have not occurred.

## Unsupported

The vehicle does not use that monitor.

Do not confuse **unsupported** with **not ready**.

---

# 11. Why Clearing Codes Resets Evidence

Using Mode $04 / the scan tool's "Clear Codes" function can erase or reset important diagnostic information, including ordinary DTC memory and readiness information.

Disconnecting the battery may also reset portions of OBD diagnostic state.

After a reset, monitors need normal vehicle operation under appropriate conditions before they become ready again.

Therefore:

**Do not clear codes before recording:**

- Confirmed codes
- Pending codes
- Permanent codes
- Freeze frame
- Readiness status
- Relevant live data

## Bad diagnostic habit

```text
CHECK ENGINE LIGHT
↓
CLEAR CODES
↓
WAIT TO SEE WHAT RETURNS
```

This throws evidence into the void.

## Better habit

```text
SCAN
↓
SAVE EVERYTHING
↓
DIAGNOSE
↓
REPAIR
↓
CLEAR ONLY WHEN USEFUL
↓
VERIFY MONITORS / DRIVE
```

---

# 12. When Clearing Codes Is Appropriate

Code clearing can be appropriate after:

- Evidence has been fully recorded.
- A repair has been completed.
- You deliberately want to evaluate whether a fault returns.
- A diagnostic procedure specifically calls for resetting learned diagnostic state.

After clearing:

1. Start the vehicle.
2. Confirm no immediate fault returns.
3. Observe live data.
4. Drive normally and safely.
5. Recheck pending codes.
6. Recheck readiness.
7. Recheck permanent codes later.

Do not promise that a specific universal "drive cycle" will make every monitor complete. Monitor enabling conditions vary.

---

# 13. Current Live Data / PIDs

Mode $01 provides current standardized powertrain data where supported.

Useful PIDs include:

- Engine RPM
- Vehicle speed
- Engine coolant temperature (ECT)
- Intake-air temperature (IAT)
- Calculated load
- Short-term fuel trim (STFT)
- Long-term fuel trim (LTFT)
- Manifold absolute pressure (MAP)
- Throttle position / relative throttle values where supported
- Fuel-system status
- Control-module voltage on scanners that expose it
- Oxygen/A/F sensor data where supported
- Fuel-pressure data where available

Not every PID is supported by every vehicle.

A blank PID does not necessarily mean a failed sensor. It may simply be unsupported through generic OBD.

---

# 14. Build a Baseline While the Car Is Healthy

One of the most powerful things you can do is record normal live data while the vehicle is running correctly.

Create baseline snapshots for:

### Warm idle

Record:

- RPM
- ECT
- IAT
- STFT
- LTFT
- MAP
- System voltage if available
- Engine load

### Steady cruise

At a safe steady road speed, record:

- RPM
- Vehicle speed
- STFT
- LTFT
- MAP/load
- ECT
- System voltage

### Cold start

Record:

- Initial ECT
- Initial IAT
- RPM behavior
- Time until warm

When a future fault occurs, compare against **this car's own healthy baseline**.

That is often more valuable than an internet "normal value" from a different vehicle.

---

# 15. Engine Coolant Temperature (ECT)

ECT is useful for diagnosing:

- Cold-start behavior
- Thermostat problems
- Cooling-system behavior
- Sensor plausibility
- Fuel-enrichment problems

## Cold-engine plausibility test

After the car has sat long enough to become fully cold, ECT and IAT should generally be reasonably close to ambient temperature.

If:

```text
Outside temperature ≈ 55°F
IAT ≈ 57°F
ECT = 180°F before starting
```

then the ECT signal is implausible.

Do not immediately replace the sensor. Investigate:

- Sensor
- Connector
- Wiring
- Reference/ground circuits
- Scanner interpretation

---

# 16. RPM While Cranking

RPM is one of the fastest crank/no-start checks available.

If the starter physically cranks the engine but generic OBD shows:

```text
RPM = 0
```

investigate:

- Crankshaft position signal
- Sensor wiring/connectors
- ECU power/ground
- Related timing/signal issues

If RPM is present, the ECU is receiving at least enough crank-speed information to calculate RPM.

This does **not** prove the crank sensor waveform or cam/crank correlation is perfect.

See the future `CRANK_NO_START.md` diagnostic document for deeper procedure.

---

# 17. Fuel-System Status

Generic OBD can report whether fuel control is operating in states such as open loop or closed loop.

## Open loop

The ECU is not currently using normal closed-loop exhaust feedback for mixture correction.

This can be normal during conditions such as:

- Initial cold start
- Certain high-load conditions
- Some fault states

## Closed loop

The ECU is adjusting fueling using exhaust feedback.

A warm engine that never enters expected closed-loop control deserves investigation, but exact behavior depends on conditions and sensor strategy.

---

# 18. Short-Term Fuel Trim (STFT)

STFT is the ECU's rapid mixture correction.

General interpretation:

```text
Positive STFT → ECU is adding fuel
Negative STFT → ECU is subtracting fuel
```

Examples:

```text
STFT +15%
```

means the ECU is currently adding substantially more fuel than the base calculation.

```text
STFT -15%
```

means it is subtracting fuel.

STFT moves quickly and should be interpreted as a trend rather than one frozen number.

---

# 19. Long-Term Fuel Trim (LTFT)

LTFT represents learned longer-term correction.

General interpretation:

```text
Positive LTFT → learned tendency to add fuel
Negative LTFT → learned tendency to remove fuel
```

STFT and LTFT should be considered together.

Example:

```text
STFT +3%
LTFT +17%
```

The instantaneous correction looks small, but the ECU has already learned a substantial positive correction.

---

# 20. Fuel Trim Diagnostic Heuristics

The following are **general diagnostic heuristics, not Hyundai factory pass/fail specifications**.

On a healthy fully warmed gasoline engine under stable conditions, combined correction near zero is generally desirable.

A rough field heuristic:

- Around ±5%: often unremarkable
- Around ±10%: worth context and trend analysis
- Around ±20% or more: strong evidence that something is abnormal

Do not diagnose solely from these thresholds.

Fuel trims vary with:

- Idle versus cruise
- Temperature
- Electrical load
- Fuel composition
- Altitude
- Recent ECU reset
- Sensor strategy

---

# 21. Fuel Trim Pattern Recognition

## Strong positive correction mainly at idle

Possible areas to investigate:

- Intake/vacuum leak
- PCV-related air leak
- Intake manifold sealing
- Purge-flow problem

Why:

A fixed amount of unmetered air has a larger percentage effect when total airflow is small at idle.

## Strong positive correction at idle AND cruise/load

Possible areas include:

- Fuel supply limitation
- Incorrect pressure signal/control
- Injector delivery problem
- Air measurement/load calculation problem
- Exhaust feedback bias

## Strong negative correction

Possible areas include:

- Excess fuel delivery
- Leaking injector
- Purge valve flow when it should be closed
- Incorrect pressure/control
- Sensor bias causing ECU to command too much fuel

These are starting points, not verdicts.

---

# 22. MAP Data

The Accent's load calculations can make manifold absolute pressure useful for diagnosis.

MAP should respond logically to throttle/load changes.

Typical qualitative pattern:

- Closed throttle / idle: manifold pressure lower than atmospheric pressure
- Throttle opens / load rises: manifold pressure rises toward atmospheric pressure

Actual values depend heavily on:

- Altitude
- Weather
- Engine load
- Engine condition

Do not use a sea-level MAP number as a universal specification in the mountains.

A useful trick is comparing key-on/engine-off MAP to local atmospheric pressure, then comparing the running value.

---

# 23. Intake Air Temperature (IAT)

After a long cold soak, IAT should generally be reasonably consistent with ambient conditions.

After the engine compartment becomes heat-soaked, stationary IAT can rise well above outdoor air temperature.

Therefore a hot parked IAT reading is not automatically a failed sensor.

Context matters.

---

# 24. Control-Module / System Voltage

Some scanners expose ECU voltage.

Use it to spot:

- Low cranking voltage
- Charging failure
- Intermittent electrical problems
- Voltage drops that coincide with multiple codes

But use a digital multimeter at the battery for accurate electrical diagnosis.

OBD voltage is useful evidence, not a calibrated substitute for direct measurement.

---

# 25. Multiple Codes: Diagnose Relationships

Do not treat each DTC as an independent broken part.

Example:

```text
P010x air/load code
P0171 lean code
P0300 random misfire
```

These may share a single root cause.

Another example:

```text
Multiple sensor circuit-low codes
U-codes
Throttle code
Transmission communication code
```

Check system voltage, shared powers, grounds, and network health before buying several sensors.

## AI rule

When multiple codes appear:

1. Group by shared circuit/system.
2. Identify common power/ground/reference/network dependencies.
3. Identify which code is likely primary and which may be downstream effects.
4. Rank shared-cause hypotheses before independent-component failures.

---

# 26. Misfire Codes

Common generic codes include:

| Code | Meaning |
|---|---|
| P0300 | Random/multiple-cylinder misfire detected |
| P0301 | Cylinder 1 misfire detected |
| P0302 | Cylinder 2 misfire detected |
| P0303 | Cylinder 3 misfire detected |
| P0304 | Cylinder 4 misfire detected |

A cylinder-specific misfire does not automatically mean a failed ignition coil.

Possible causes include:

- Ignition coil
- Spark plug
- Injector
- Injector circuit
- Compression problem
- Valve problem
- Local intake leak
- Wiring/connector issue

### Useful isolation strategy

For a persistent single-cylinder misfire, after recording evidence:

1. Inspect plug/coil connector.
2. Swap the suspected ignition coil with another cylinder when appropriate.
3. Re-test.
4. If the misfire moves, the coil becomes a strong suspect.
5. If it stays, continue diagnosis rather than buying another coil.

---

# 27. Flashing MIL / Check Engine Light

A flashing malfunction indicator lamp commonly indicates a severe active misfire with potential catalytic-converter damage.

When the MIL flashes:

- Reduce engine load.
- Avoid hard acceleration.
- Stop driving as soon as safely practical if severe misfire continues.
- Diagnose promptly.

A flashing MIL should not be treated like an ordinary steady check-engine light.

---

# 28. Mode $06 — On-Board Monitor Test Results

Mode $06 can expose the numerical results of on-board monitor tests.

This can be extremely useful because it may show a component or system moving toward a failure threshold **before** a normal DTC becomes confirmed.

Depending on vehicle/scanner support, Mode $06 may provide results related to monitors such as:

- Catalyst
- Misfire
- Oxygen/A/F sensing
- EVAP
- Other non-continuously monitored systems

## Critical warning

Raw Mode $06 data is easy to misinterpret.

Values can require:

- Correct Test ID / Monitor ID interpretation
- Manufacturer-specific mapping
- Correct units
- Scaling
- Minimum/maximum limits

Do not look at a raw hexadecimal or numerical value and guess what it means.

A good scan tool will decode the test name, value, limit, and units where known.

### AI rule

Do not interpret Mode $06 numerically unless the following are known:

```text
monitor/test identity
value
units/scaling
minimum/maximum or pass/fail threshold
vehicle applicability
```

If any of these are unknown, state that the data cannot yet be interpreted reliably.

---

# 29. Mode $08 — Active Tests

Mode $08 or manufacturer-specific bidirectional diagnostics can command supported components or tests.

Possible enhanced-tool functions might include activating pumps, valves, fans, solenoids, or other outputs.

These functions can be diagnostically powerful, but they are not harmless buttons.

Do not command a component unless you understand:

- What will move or activate
- What prerequisites are required
- Whether the engine should be running
- Whether fluid pressure or temperature creates risk

A cheap generic reader may not support useful active tests at all.

---

# 30. Mode $09 — Vehicle Information

Mode $09 can provide supported identification data such as:

- VIN
- Calibration identification
- Calibration verification information

Availability depends on vehicle and scanner.

This information can help confirm that the scan tool is actually talking to the expected ECU/vehicle.

---

# 31. Generic Scanner vs. Enhanced Hyundai Scanner

## Generic OBD-II reader

Good for:

- Powertrain DTCs
- Pending codes
- Permanent codes
- Freeze frame
- Readiness
- Generic live PIDs
- Basic emissions diagnosis

## Enhanced Hyundai-capable scanner

Potentially adds access to:

- ABS codes and data
- SRS/airbag codes
- MDPS steering faults
- Transmission-specific information
- Body controller information
- Manufacturer-specific PIDs
- Bidirectional tests
- Adaptations / service functions depending on tool

When a warning lamp is not the engine MIL, a generic scanner showing "no codes" should not end diagnosis.

---

# 32. Cheap Bluetooth/Wi-Fi OBD Adapters

Low-cost adapters can be very useful, but quality varies enormously.

Potential problems include:

- Communication dropouts
- Incorrectly reported PIDs
- Slow polling
- Poor CAN handling
- Firmware clones
- Excessive sleep-current draw if left connected
- Apps that mistranslate codes

## Practical rule

If a reading seems impossible:

1. Verify it with another PID.
2. Restart the connection.
3. Cross-check with another app/tool if available.
4. Verify critical electrical values with a multimeter.

Do not base a costly repair on one suspicious value from an unknown adapter.

---

# 33. Do Not Leave Unknown Adapters Connected Forever

Some OBD dongles continue drawing power with the ignition off.

For a vehicle that may sit at primitive camps for days, this matters.

Unless the device is specifically designed and verified for low-power sleep:

- Remove it when diagnostics are finished.
- Especially remove it before extended parking.

A diagnostic tool should not become the cause of the next dead-battery diagnosis.

---

# 34. Code Priority

When many DTCs exist, prioritize them approximately like this:

## Priority 1 — safety / damaging conditions

- Severe misfire
- Critical voltage/power faults
- Conditions related to overheating or unsafe drivability

## Priority 2 — codes likely to be primary causes

Examples:

- Power supply/reference faults
- Crank/cam signal faults
- Major air/fuel measurement faults

## Priority 3 — likely secondary/resulting codes

Examples can include:

- Misfire codes caused by a broader fueling problem
- Catalyst-efficiency codes following long-term misfire
- Communication faults caused by low voltage

Exact priority depends on symptoms and evidence.

---

# 35. U-Codes / Network Codes

Codes beginning with `U` concern communication/network faults.

Do not automatically blame the module named in the code.

Possible causes include:

- Weak battery
- Charging-system failure
- Voltage drop
- Blown fuse
- Shared ground problem
- CAN wiring damage
- Connector fault
- One module pulling the network down
- Actual module failure

If many modules suddenly report communication faults at once, electrical supply and network integrity deserve early attention.

---

# 36. Low Voltage Can Create a Code Storm

One weak battery can make a modern car look haunted.

During low voltage you may see:

- U-codes
- Sensor voltage codes
- Throttle-related codes
- Steering warnings
- ABS warnings
- Transmission faults
- Strange instrument behavior

Therefore:

```text
MANY UNRELATED CODES
        ↓
CHECK BATTERY / CHARGING / GROUNDS EARLY
```

Do this before replacing a pile of unrelated electronic modules.

---

# 37. Basic Diagnostic Capture Procedure

Whenever a fault occurs:

## Step 1 — Do not clear anything

## Step 2 — Record symptoms

- Cold/warm/hot engine
- Speed
- Load
- Weather
- Fuel level
- Recent rough road / impact
- Recent service

## Step 3 — Scan

Record:

- Confirmed codes
- Pending codes
- Permanent codes
- Module source if known

## Step 4 — Record freeze frame

## Step 5 — Record readiness

## Step 6 — Record relevant live data

## Step 7 — Measure battery voltage directly if electrical behavior is suspicious

## Step 8 — Build hypotheses

## Step 9 — Perform tests that distinguish hypotheses

## Step 10 — Repair and verify

---

# 38. Diagnostic Snapshot Template

Use this block when saving a scan:

```markdown
## OBD Diagnostic Snapshot

**Date:**
**Mileage:**
**Engine cold/warm/hot:**
**Ambient temperature:**
**Fuel level:**
**Primary symptom:**

### Warning lamps

### Confirmed DTCs
- 

### Pending DTCs
- 

### Permanent DTCs
- 

### Freeze frame
- DTC that triggered frame:
- RPM:
- Vehicle speed:
- ECT:
- IAT:
- Calculated load:
- STFT:
- LTFT:
- MAP:
- Throttle:
- Voltage:
- Other:

### Readiness monitors
- Misfire:
- Fuel system:
- Comprehensive component:
- Catalyst:
- EVAP:
- O2/A/F sensor:
- Heater:
- Other:

### Warm idle live data
- RPM:
- ECT:
- IAT:
- STFT:
- LTFT:
- MAP:
- Load:
- Voltage:

### Cruise live data
- Speed:
- RPM:
- STFT:
- LTFT:
- MAP/load:
- ECT:

### Mode $06 findings

### Tests performed

### Result

### Ranked hypotheses
1.
2.
3.

### Repair

### Verification

```

Copy important events into `../maintenance/NOMAD_SERVICE_LOG.md`.

---

# 39. AI Diagnostic Reasoning Rules

An AI using this repository should follow these rules:

## Rule 1

Never say:

```text
Pxxxx means replace component X.
```

Instead say:

```text
Pxxxx indicates the ECU detected ______. Likely causes include ______. The next discriminating tests are ______.
```

## Rule 2

Rank causes by:

- Symptom compatibility
- Code relationships
- Freeze-frame conditions
- Live-data evidence
- Known electrical dependencies
- Recent maintenance/events

not by whichever part name appears in the DTC description.

## Rule 3

Separate:

- **Observed fact**
- **Measured value**
- **Code definition**
- **Diagnostic inference**
- **Unverified hypothesis**

## Rule 4

Never invent missing PID values or Hyundai-specific limits.

## Rule 5

If a PID is unsupported, do not treat that as a failed sensor.

## Rule 6

If codes were recently cleared, explicitly account for incomplete readiness and lost historical evidence.

## Rule 7

If several unrelated electronic systems fault at once, evaluate system voltage/power/ground/network causes early.

## Rule 8

A permanent DTC alone is not proof that the fault remains active.

---

# 40. Example AI Reasoning

Input:

```text
Vehicle cranks normally but does not start.
Confirmed codes: none.
Pending: P0335.
RPM while cranking: 0.
Battery voltage: normal.
```

Good reasoning:

```text
The combination of a pending crankshaft-position circuit code and 0 RPM
reported while the engine is physically cranking makes the crankshaft-position
signal path a high-priority area. Do not replace the sensor yet. Inspect the
sensor connector/wiring and verify signal/circuit integrity; also verify ECU
power/grounds and consider mechanical signal-wheel issues if electrical tests
pass.
```

Bad reasoning:

```text
P0335 = bad crank sensor. Replace it.
```

---

# 41. Example Fuel-Trim Reasoning

Input:

```text
Warm idle:
STFT +22%
LTFT +15%

2500 RPM no-load:
STFT +4%
LTFT +15%
```

Useful hypothesis:

The large short-term correction at idle that improves substantially with increased airflow is compatible with an air leak whose proportional effect is greatest at idle.

Next steps may include:

- Inspect intake plumbing
- Inspect PCV-related paths
- Check manifold sealing
- Evaluate purge flow
- Use a proper smoke test when available

Do not immediately buy an oxygen sensor.

---

# 42. Example Voltage / Network Reasoning

Input:

```text
ABS warning
MDPS warning
Transmission warning
Several U-codes
Engine cranks slowly
```

Priority:

1. Battery state and load capability
2. Battery terminals
3. Engine/chassis grounds
4. Charging system
5. Main fuses/power distribution
6. Only then chase individual network/module faults if voltage supply is healthy

This is more efficient than diagnosing three modules independently.

---

# 43. Readiness After Repair

After repairing an emissions-related problem:

1. Record the repair.
2. Clear ordinary codes only if appropriate.
3. Operate the vehicle normally.
4. Check pending codes periodically.
5. Check readiness monitors.
6. Check whether the permanent DTC eventually clears itself.

Do not force unsafe driving patterns just to complete a monitor.

A monitor may need very specific combinations of:

- Coolant temperature
- Ambient temperature
- Fuel level
- Speed
- Load
- Deceleration
- Time since start

Normal mixed driving is often the safest approach unless an authoritative vehicle-specific drive procedure is available.

---

# 44. OBD Before a Remote Trip

A useful remote-travel scan takes only a few minutes.

Before leaving pavement for an extended primitive-camping stay:

- Check confirmed DTCs
- Check pending DTCs
- Check permanent DTCs
- Confirm MIL status
- Check readiness for unusual recent resets
- Check ECT plausibility
- Check charging/system voltage if available
- Look at warm-idle fuel trims

A newly pending fault is worth investigating while parts stores and pavement are still nearby.

See `../maintenance/PRE_TRIP_INSPECTION.md`.

---

# 45. OBD After a Rough-Road Event

After a severe pothole, underbody strike, or rough trail, scan if any warning light or drivability change appears.

Look for:

- Pending powertrain faults
- Electrical faults caused by disturbed connectors
- Enhanced ABS/steering codes if a capable scanner is available

Also perform physical inspection. OBD cannot tell you that an exhaust hanger is bent or a tire sidewall is cut.

---

# 46. What OBD Cannot Diagnose by Itself

OBD does not replace physical inspection.

Examples:

- Worn wheel bearing with no electronic fault
- Torn CV boot
- Cracked suspension component
- Brake pad thickness
- Tire sidewall damage
- Oil leak
- Exhaust impact damage
- Loose wheel
- Mechanical engine wear with no monitor threshold exceeded

The scanner is one instrument in the toolkit, not an oracle.

---

# 47. Evidence Hierarchy

When diagnosing, weigh evidence approximately like this:

```text
PHYSICAL SAFETY CONDITION
        ↓
DIRECT MEASUREMENT / OBSERVATION
        ↓
DTC + FREEZE FRAME
        ↓
LIVE DATA TREND
        ↓
TARGETED ELECTRICAL / MECHANICAL TEST
        ↓
KNOWN PATTERN / SERVICE HISTORY
        ↓
INTERNET ANECDOTE
```

A forum post saying "mine was the sensor" is not stronger evidence than a failed wiring test on the actual car.

---

# 48. Suggested Future Diagnostic Files

This guide should remain the general OBD foundation. Specific symptom trees belong in separate files:

```text
diagnostics/
  OBD2_GUIDE.md
  NO_CRANK.md
  CRANK_NO_START.md
  MISFIRE.md
  OVERHEATING.md
  CHARGING_SYSTEM.md
  FUEL_TRIM_DIAGNOSTICS.md
  EVAP_DIAGNOSTICS.md
  SENSOR_PLAUSIBILITY.md
  NETWORK_U_CODES.md
```

Small focused documents improve offline retrieval accuracy.

---

# 49. Machine-Readable Summary

```yaml
obd2:
  vehicle: "2014 Hyundai Accent SE"
  market: "US"
  connector:
    type: "SAE J1962 16-pin"
    important_pins:
      4: "chassis ground"
      5: "signal ground"
      6: "CAN High"
      14: "CAN Low"
      16: "battery positive"

  diagnostic_services:
    mode_01: "current powertrain/live data"
    mode_02: "freeze frame"
    mode_03: "confirmed emission-related DTCs"
    mode_04: "clear/reset emission-related diagnostic information"
    mode_06: "on-board monitor test results"
    mode_07: "pending DTCs"
    mode_09: "vehicle information"
    mode_0A: "permanent DTCs"

  dtc_states:
    confirmed: "fault matured to confirmed status"
    pending: "fault detected but confirmation criteria may not be complete"
    permanent: "nonvolatile emissions-related record cleared by OBD system after successful verification, not manually erased"

  evidence_preservation:
    before_clearing:
      - "confirmed codes"
      - "pending codes"
      - "permanent codes"
      - "freeze frame"
      - "readiness status"
      - "relevant live data"

  useful_live_data:
    - "RPM"
    - "vehicle speed"
    - "ECT"
    - "IAT"
    - "STFT"
    - "LTFT"
    - "MAP"
    - "calculated load"
    - "fuel-system status"
    - "system/control-module voltage when supported"

  fuel_trim_direction:
    positive: "ECU adding fuel"
    negative: "ECU subtracting fuel"

  generic_heuristic_not_factory_spec:
    trim_near_5_percent: "often unremarkable under stable warm conditions"
    trim_near_10_percent: "investigate context/trend"
    trim_near_20_percent: "strong abnormality indication"

  critical_rules:
    - "DTC is evidence, not a parts order"
    - "record freeze frame before clearing"
    - "unsupported PID does not equal failed sensor"
    - "permanent DTC alone does not prove active fault"
    - "multiple unrelated codes require voltage/power/ground/network consideration"
    - "Mode 06 raw values require correct identity, scaling, units, and limits"
```

---

# 50. Source and Standards Notes

Primary standards/background sources used for this document:

- SAE J1979 — E/E Diagnostic Test Modes / emissions-related OBD communication and services: https://saemobilus.sae.org/standards/j1979_202505-e-e-diagnostic-test-modes
- SAE J2012 — Diagnostic Trouble Code Definitions: https://saemobilus.sae.org/standards/j2012_202509-diagnostic-trouble-code-definitions
- SAE OBD-II diagnostic-messages/test-modes reference material: https://www.sae.org/images/books/toc_pdfs/R458.pdf
- U.S. EPA discussion of OBD readiness and Permanent DTC behavior: https://www.epa.gov/system/files/documents/2022-08/diesel-obd-im-readiness-14k-pounds-gwr-best-practices.pdf
- California Air Resources Board OBD readiness / Permanent DTC explanation: https://ww2.arb.ca.gov/es/node/35236

The SAE standards evolve over time. This 2014 vehicle implements the OBD requirements applicable to its model year; newer standard revisions are useful for terminology and current reference but should not be used to assume that a later-added PID or service is supported by this vehicle.

---

# 51. Repository Confidence Labels

Use the repository-wide labels consistently:

- **VERIFIED — STANDARD:** Defined by applicable OBD/SAE standard or regulation.
- **VERIFIED — HYUNDAI:** Confirmed by Hyundai documentation.
- **VERIFIED — MULTIPLE SOURCES:** Supported independently by reliable references.
- **GENERAL DIAGNOSTIC PRACTICE:** Widely used method, not a Hyundai-specific specification.
- **PROVISIONAL:** Plausible but awaiting authoritative confirmation.
- **OWNER OBSERVATION:** Specific observation from this individual vehicle.

Fuel-trim percentage heuristics in this document are **GENERAL DIAGNOSTIC PRACTICE**, not Hyundai service-manual limits.

---

# 52. Core Philosophy

```text
SCAN
  ↓
PRESERVE EVIDENCE
  ↓
UNDERSTAND THE CONDITIONS THAT SET THE CODE
  ↓
COMPARE LIVE DATA WITH PHYSICAL REALITY
  ↓
TEST THE SYSTEM
  ↓
ISOLATE THE ROOT CAUSE
  ↓
REPAIR
  ↓
VERIFY WITH DATA AND NORMAL OPERATION
```

The scanner does not tell you what part to replace.

It tells you where the car wants you to start asking better questions.

---

## Document Status

- **Vehicle:** 2014 Hyundai Accent SE
- **Document:** Generic OBD-II diagnostic foundation
- **Status:** Initial field/reference version
- **Architecture:** Human-readable + AI/RAG-friendly
- **Factory-specific PID thresholds:** Not invented
- **Enhanced Hyundai diagnostics:** To be expanded in dedicated module-specific documents
- **Copyright approach:** Original explanatory documentation based on standards, regulatory information, and general diagnostic practice
