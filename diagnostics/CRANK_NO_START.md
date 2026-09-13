# 2014 Hyundai Accent SE — Cranks but Will Not Start

> **Purpose:** A source-aware, offline diagnostic workflow for a 2014 Hyundai Accent SE that **cranks normally but does not start**.
>
> **Core rule:** A crank/no-start is not a diagnosis. It is a symptom. Separate the problem into **engine-speed signal, ignition, fuel, air, and mechanical timing/compression** before replacing parts.

---

## 1. Scope

This guide is intended primarily for a U.S.-market 2014 Hyundai Accent SE five-door with the 1.6 L GDI engine and six-speed automatic transmission configuration documented elsewhere in this repository.

Related files:

- `../specs/VEHICLE_BASELINE.md`
- `../specs/FUSES_AND_RELAYS.md`
- `../specs/FLUIDS_AND_CAPACITIES.md`
- `OBD2_GUIDE.md`
- `NO_CRANK.md`
- `../guides/ROADSIDE_DIAGNOSTIC_TRIAGE.md`

---

# 2. Define the Symptom Correctly

## Crank/no-start means

The starter rotates the engine at approximately normal cranking speed, but the engine does not begin running on its own.

This is different from:

- **No crank:** starter does not rotate the engine.
- **Slow crank:** starter rotates the engine abnormally slowly.
- **Starts then dies:** engine fires and runs briefly, then stops.
- **Intermittent stall:** engine was already running and then shut off.

Misclassifying the symptom sends diagnosis down the wrong branch.

---

# 3. Hyundai Owner-Manual First Checks

Hyundai's 2014 Accent owner documentation gives a short factory roadside sequence for an engine that **turns over normally but does not start**:

1. Check the fuel level.
2. With ignition in LOCK/OFF, inspect ignition-coil and spark-plug connections.
3. Reconnect any loose or disconnected connectors.
4. If the engine still will not start, seek qualified service.

Hyundai also specifies that normal starting should be attempted **without depressing the accelerator**, whether the engine is cold or warm.

Do not crank continuously for more than **10 seconds** per attempt. Hyundai instructs waiting approximately **5–10 seconds** before another attempt.

Primary owner-manual sources:

- https://manualzz.com/doc/53857913/hyundai-2014-accent-owner-manual
- https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual

---

# 4. Safety Stop Conditions

Stop diagnosis and do not continue repeated cranking if any of these are present:

- Strong raw-fuel smell combined with suspected leak
- Visible fuel leak
- Smoke from wiring or electrical components
- Severe mechanical clunking, grinding, or impact noises while cranking
- Engine suddenly cranks much faster than normal after a mechanical event
- Evidence of coolant or oil entering cylinders
- Battery cables become dangerously hot
- Starter remains engaged after key release

Repeated cranking can overheat the starter, discharge the battery, wash oil from cylinder walls, and load the catalytic converter with unburned fuel.

---

# 5. Master Diagnostic Tree

```text
ENGINE CRANKS NORMALLY BUT WILL NOT START
                ↓
        Preserve evidence first
                ↓
        Scan all available DTCs
                ↓
      Observe RPM while cranking
        ┌────────┴────────┐
      0 RPM           RPM present
        ↓                  ↓
CKP signal / wiring     Check spark
ECU power / grounds       ↓
mechanical trigger   Spark on all cylinders?
                         ┌──────┴──────┐
                        NO            YES
                        ↓              ↓
                 Ignition/CKP/CMP    Fuel / injector
                 ECU power/grounds   / air / mechanical
                                         ↓
                              Fuel delivery plausible?
                                  ┌──────┴──────┐
                                 NO            YES
                                 ↓              ↓
                         Low/high pressure   Compression /
                         pump/control        cam-crank timing
```

The branches are not perfectly independent. A single failed crankshaft-position signal, ECU power problem, or mechanical timing failure can suppress both spark and injector operation.

---

# 6. Step Zero: Preserve Evidence

Before clearing codes or disconnecting the battery, record:

- Stored DTCs
- Pending DTCs
- Permanent DTCs
- Freeze-frame data
- Engine RPM while cranking
- Module/system voltage while cranking
- Coolant temperature
- Fuel-related PIDs if supported
- Security/immobilizer indicators
- Whether the problem is cold-only, hot-only, or random
- Fuel level
- Recent repairs or electrical work
- Whether the engine stalled suddenly before becoming a no-start

Do not clear codes merely to see whether they return.

---

# 7. Step One: Verify Adequate Cranking Speed and Voltage

A starter can rotate the engine yet still crank too slowly for reliable starting.

Check:

- Battery state of charge
- Battery terminals
- Engine/chassis grounds
- Cranking voltage behavior
- Whether the cranking sound is normal for this vehicle

If cranking is clearly slow, diagnose the battery/starter/cable problem first using `NO_CRANK.md` principles.

Low voltage can create misleading sensor, communication, immobilizer, and ECU faults.

---

# 8. Step Two: Watch OBD Engine RPM While Cranking

This is one of the fastest useful tests.

Connect an OBD-II scanner and monitor engine RPM while the starter turns the engine.

## If RPM is present

The ECU is receiving at least some engine-speed information.

That makes a total loss of crankshaft-position input less likely, though it does **not** prove the signal is perfect.

Proceed to spark and fuel checks.

## If RPM stays at 0 while the engine is physically cranking

Prioritize:

- Crankshaft-position sensor circuit
- Crankshaft-position sensor connector
- Sensor wiring damage
- ECU power/ground
- Trigger wheel / reluctor issue
- Mechanical timing or engine-speed signal problem

A crankshaft-position sensor is fundamental to engine speed/timing calculations; crank/cam sensor faults can produce intermittent or heat-related crank/no-start problems.

General technical background:

- SAE crankshaft-position sensor timing paper: https://saemobilus.sae.org/papers/application-a-crankshaft-position-sensor-control-engine-timing-780213
- Diagnostic discussion: https://www.underhoodservice.com/crankshaft-and-camshaft-position-sensor-diagnosis/

### Important

`0 RPM` is a diagnostic clue, not automatic permission to buy a crankshaft sensor.

A wiring fault, connector problem, ECU supply problem, poor ground, damaged trigger wheel, or mechanical issue can create the same symptom.

---

# 9. Step Three: Read Relevant DTC Families

Useful code families may include:

## Crank/cam synchronization

- `P0335` family — crankshaft-position circuit
- `P0340` family — camshaft-position circuit
- Correlation/timing-related codes

## Ignition / misfire

- `P0300`
- `P0301`–`P0304`
- ignition-coil circuit codes

## Fuel pressure / delivery

- fuel-pressure regulator/control codes
- rail-pressure sensor codes
- low-pressure pump related codes

## Electronic throttle / air control

- throttle actuator codes
- throttle-position correlation codes

## ECU / voltage / communication

- low-voltage codes
- U-codes
- ECU power-supply faults

Do not diagnose from the code title alone. Use the code to choose a circuit or system to test.

---

# 10. Step Four: Check the Relevant Fuses and Relays

For this 2014 Accent configuration, first electrical checks for a crank/no-start include the circuits documented in `../specs/FUSES_AND_RELAYS.md`.

High-value engine-bay circuits include:

| Circuit | Rating | Role |
|---|---:|---|
| ECU 1 | 30A | ECU / engine-control feed |
| ECU 2 | 10A | ECM/PCM feed |
| F/PUMP | 15A | Fuel-pump relay circuit |
| INJECTOR | 15A | Injector/engine-control related feed |
| SENSOR | 10A | Engine-control sensors/solenoids related feed |
| IGN COIL | 15A | Ignition coils 1–4 |

Also inspect the engine-control/main relay and fuel-pump relay where applicable.

A fuse that looks good visually should still be electrically tested.

A good fuse does **not** prove usable voltage reaches the component under load.

---

# 11. Step Five: Verify Spark Safely

Use a proper spark tester where possible.

Do not hold coils, plug wires, test leads, or spark plugs by hand while cranking.

## No spark on all cylinders

Prioritize shared causes:

- Crankshaft-position input
- Camshaft-position input / synchronization
- ECU power/ground
- `IGN COIL` fuse
- Main/engine-control relay
- Immobilizer/security authorization
- Wiring harness damage
- Mechanical timing problem severe enough to disrupt synchronization

Do not replace four coils because all four lack spark.

## Spark missing on one cylinder only

That is usually **not** the reason an otherwise healthy four-cylinder engine will not start at all.

Investigate the individual coil, plug, connector, wiring, or cylinder fault separately.

## Spark appears weak or inconsistent

Do not judge spark solely by color in open air.

Use proper test equipment and compare cylinders.

---

# 12. Step Six: Fuel System — Understand the Two-Stage GDI System

The Accent's GDI fuel system uses:

1. A low-pressure supply side from the tank
2. An engine-driven high-pressure pump feeding the direct-injection rail

The high-pressure side is hazardous.

## GDI high-pressure safety

**Never loosen a high-pressure fuel pipe to check whether fuel is present.**

**Never search for a high-pressure leak with your hand.**

Hyundai service information warns that high-pressure fuel can remain in the system after shutdown and that residual pressure must be released before opening high-pressure components.

Service references for the same 1.6 L Accent GDI architecture:

- High-pressure pump: https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Powertrain%20Management/Fuel%20Delivery%20and%20Air%20Induction/Fuel%20Pump/Service%20and%20Repair/High%20Pressure%20Fuel%20Pump/
- Residual-pressure release: https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Maintenance/Filters/Fuel%20Filter/Fuel%20Pressure%20Release/Service%20and%20Repair/

Those service references are for the closely related 2013 1.6 L Accent GDI architecture and should be treated as **supporting technical evidence**, not a substitute for VIN-specific 2014 service information.

---

# 13. Low-Pressure Fuel-Supply Checks

Start non-invasively.

Check:

- Actual fuel level
- `F/PUMP` fuse
- Fuel-pump relay/control
- Pump electrical power/ground
- Relevant DTCs
- Whether low-pressure fuel data is available through enhanced diagnostics

Do not trust the fuel gauge blindly if there is reason to suspect sender or gauge error.

A pump sound by itself does not prove correct pressure or flow.

A silent pump does not prove the pump itself is defective; the relay, fuse, power, ground, ECU command, or wiring may be at fault.

---

# 14. High-Pressure GDI Diagnosis

When scan data supports rail-pressure monitoring, compare:

- Commanded/target pressure if available
- Actual rail pressure
- Pressure behavior during cranking

If pressure is not building appropriately, possible causes include:

- In-tank supply problem
- High-pressure pump problem
- Pressure-control valve issue
- Rail-pressure sensor/circuit issue
- Electrical supply/control problem
- Fuel contamination
- Mechanical drive issue at the high-pressure pump

The GDI high-pressure system can operate at very high pressure. Older port-injection habits such as cracking a line open are inappropriate and dangerous.

---

# 15. Step Seven: Injector Operation

If spark is present and fuel pressure is plausible, determine whether the ECU is actually commanding injection.

Possible test approaches include:

- Scan-tool injector-related data when supported
- Proper electrical testing
- Oscilloscope testing by an experienced technician

Do not apply arbitrary battery voltage directly to GDI injectors.

Direct injectors are ECU-driven devices and should not be treated like simple 12 V lamps or generic solenoids.

If all injectors appear inactive, look for a shared cause:

- ECU power/ground
- `INJECTOR` fuse
- crank/cam synchronization
- immobilizer/security logic
- harness fault
- ECU control issue

---

# 16. Step Eight: Air and Electronic Throttle

The engine also requires sufficient air.

Inspect for:

- Major intake tube collapse or disconnection
- Severe obstruction
- Throttle-body connector problem
- Electronic-throttle DTCs
- Damaged wiring

Do not force the electronic throttle plate aggressively by hand unless the service procedure specifically permits it.

A completely blocked intake is uncommon, but a disturbed connector or intake assembly after service is very plausible.

---

# 17. Step Nine: Mechanical Compression and Timing

If engine-speed signal, spark, fuel pressure, injection, and air all appear plausible, move toward mechanical testing.

Possible tests:

- Compression test
- Relative-compression test
- Leak-down test
- Cam/crank correlation
- Mechanical timing inspection

## Clues pointing toward mechanical problems

- Engine suddenly cranks faster than normal
- Cranking cadence sounds unusually even
- Very low compression on all cylinders
- Cam/crank correlation codes
- No-start began immediately after timing-system work
- Severe prior overheating
- Internal mechanical noise

The 1.6 L engine uses a timing chain, but a chain system is not magically immune to tensioner, guide, phaser, or timing faults.

Do not assume "timing chain means lifetime and impossible to fail."

---

# 18. Compression Pattern Interpretation

## Low compression on all cylinders

Possible causes include:

- Incorrect valve timing
- Washed cylinders after excessive failed start attempts
- Major mechanical wear/damage
- Testing procedure error

## One cylinder very low

Possible causes include:

- Valve sealing problem
- Piston/ring damage
- Head-gasket issue localized to that cylinder

One low cylinder alone usually does not create a total no-start unless the remaining cylinders are also compromised or another fault exists.

---

# 19. Hot No-Start vs Cold No-Start

Temperature patterns are valuable evidence.

## Starts cold, will not restart hot

Possible causes include:

- Heat-sensitive crankshaft/camshaft sensor
- Electrical connection that opens with heat
- Fuel-pressure control problem
- Ignition component heat failure
- Excessive voltage drop when hot

## Hard/no start only when cold

Possible causes include:

- Weak battery/cranking speed
- Incorrect coolant-temperature input
- Fuel-pressure bleed-down
- Injector leakage
- ignition weakness
- compression issue that worsens when cold

Record coolant-temperature PID before first start attempt. An obviously implausible value can be diagnostically important.

---

# 20. Starts With Accelerator Input Only

Hyundai specifies normal starting **without depressing the accelerator**.

If the engine consistently requires pedal input to start, treat that as a symptom rather than a normal workaround.

Possible areas to investigate:

- Throttle/airflow issue
- Mixture problem
- Fuel-pressure issue
- Injector leakage
- Sensor input error
- Carbon/deposit-related airflow behavior

Do not normalize a workaround until the underlying cause is understood.

---

# 21. Suspected Flooding

Repeated unsuccessful cranking can leave excessive fuel in the cylinders on some failure modes.

Clues may include:

- Strong fuel odor from exhaust
- Wet spark plugs
- Initial firing that worsens after repeated attempts

Because throttle and fueling strategy are ECU-controlled, do not assume an old carbureted-engine "pedal pumping" procedure applies.

The 2014 Accent owner manual instructs normal starting without depressing the accelerator.

If flooding is strongly suspected, stop repeated cranking and diagnose why combustion is not occurring.

---

# 22. Immobilizer / Security Clues

A security/immobilizer problem can allow cranking while preventing normal engine operation on some configurations.

Check:

- Immobilizer/security indicator behavior
- Related DTCs with an enhanced scan tool
- Key/transponder issues
- Relevant `SENSOR`/immobilizer-related electrical feeds documented in the fuse guide

Do not assume every crank/no-start with no spark is an immobilizer problem.

Verify actual system behavior and codes.

---

# 23. If the Engine Stalled Suddenly and Now Will Not Restart

The pre-failure event changes diagnostic priority.

## Sudden clean shutoff, like key switched off

Prioritize:

- crankshaft-position signal
- ECU power/ground
- main relay
- ignition feed
- fuel-pump power/control

## Lost power gradually before dying

Prioritize:

- fuel supply
- charging-system voltage
- exhaust restriction
- overheating/mechanical problem

## Bucked/misfired before dying

Prioritize:

- ignition
- fuel pressure
- crank/cam synchronization
- mechanical timing

---

# 24. Roadside Diagnostic Sequence

A practical low-tool sequence:

```text
1. Confirm actual fuel level
2. Record warning lights and security indicator
3. Scan stored + pending codes
4. Watch RPM while cranking
5. Check system voltage during cranking
6. Inspect ECU / F-PUMP / INJECTOR / SENSOR / IGN COIL fuses
7. Inspect obvious connectors and wiring
8. Verify spark with a proper tester
9. Evaluate fuel-pressure data if scanner supports it
10. If spark + fuel control appear plausible, consider compression/timing
```

Avoid dismantling the high-pressure GDI fuel system roadside.

---

# 25. Symptom Matrix

| Observation | Higher-priority suspects |
|---|---|
| 0 RPM on scan tool while cranking | CKP circuit, wiring, ECU power/ground, trigger issue |
| RPM present, no spark anywhere | shared ignition control, CKP/CMP sync, ECU power, immobilizer, IGN COIL circuit |
| Spark present, fuel pressure absent | low-pressure pump/control, high-pressure pump/control, fuel-pressure sensing |
| Spark + plausible fuel pressure, no injector command | ECU power/control, synchronization, immobilizer, injector circuit |
| Spark + fuel + injector command, no start | compression, mechanical timing, excessive/insufficient fueling, air |
| Starts cold, no-start hot | heat-sensitive sensor/wiring, fuel pressure, voltage, ignition |
| Starts hot, poor/no cold start | battery, ECT input, fuel bleed-down, injector leak, compression |
| Cranks suddenly much faster than usual | compression/timing problem |
| Multiple unrelated electrical codes | battery/system voltage, grounds, ECU supply, network fault |

---

# 26. What Not to Do

Do **not**:

- Replace the crankshaft sensor solely because RPM is 0 without checking wiring/power/grounds.
- Replace the fuel pump because you cannot hear it.
- Replace all ignition coils because there is no spark anywhere.
- Crack open a GDI high-pressure line to look for fuel.
- Apply 12 V directly to GDI injectors.
- Clear codes before recording them.
- Disconnect the battery before preserving freeze-frame evidence unless safety requires it.
- Keep cranking endlessly.
- Use starting fluid casually on a GDI engine.
- Push-start or tow-start the automatic transmission vehicle.

---

# 27. AI Diagnostic Rules

An AI using this document should:

1. First verify that the symptom is truly crank/no-start.
2. Ask for or inspect **cranking RPM** early.
3. Preserve DTC/freeze-frame evidence before suggesting code clearing.
4. Rank shared-system failures above simultaneous failure of many individual components.
5. Distinguish **low-pressure fuel supply** from **high-pressure GDI rail pressure**.
6. Never recommend opening a high-pressure fuel line as a diagnostic shortcut.
7. Never treat a DTC as proof a named component has failed.
8. Separate verified measurements from assumptions.
9. Escalate toward compression/timing only after basic electrical, spark, and fuel evidence is considered.
10. Surface safety-critical findings first.

---

# 28. AI Prompt Template

```text
Vehicle: 2014 Hyundai Accent SE 1.6L GDI automatic
Symptom: cranks normally but will not start
Mileage: _____
Cold / warm / hot engine: _____
Fuel level: _____
Stored DTCs: _____
Pending DTCs: _____
Permanent DTCs: _____
Freeze frame: _____
Battery voltage engine off: _____
Voltage while cranking: _____
RPM while cranking: _____
Spark test result: _____
Fuel pressure data: _____
Injector command evidence: _____
Security/immobilizer indicator: _____
Recent repair work: _____
Recent stall/event before no-start: _____
Unusual noises/smells: _____

Rank the likely causes by probability and diagnostic leverage.
For each likely cause, give the safest next test that distinguishes it from the others.
Do not recommend replacing parts without a confirming test.
Do not recommend opening the high-pressure GDI fuel system as a roadside test.
```

---

# 29. Diagnostic Incident Template

```markdown
## Crank/No-Start Incident

**Date:**
**Mileage:**
**Engine temperature:** cold / warm / hot
**Fuel level:**

### What happened before the failure?


### Cranking behavior
- [ ] Normal
- [ ] Slow
- [ ] Faster than normal
- [ ] Uneven

### System voltage
- Engine off:
- During crank:

### OBD-II
- Stored codes:
- Pending codes:
- Permanent codes:
- RPM while cranking:
- Coolant temperature:
- Rail/fuel pressure data:

### Spark


### Fuel


### Injector evidence


### Compression / mechanical findings


### Repairs performed


### Verification

```

---

# 30. Machine-Readable Summary

```yaml
vehicle:
  year: 2014
  make: Hyundai
  model: Accent
  trim: SE
  engine: 1.6L_GDI
  transmission: 6_speed_automatic

diagnostic_case:
  symptom: crank_no_start
  primary_branches:
    - cranking_speed_and_voltage
    - crankshaft_position_signal
    - ecu_power_and_ground
    - ignition_spark
    - low_pressure_fuel_supply
    - high_pressure_gdi_fuel
    - injector_control
    - air_and_throttle
    - compression
    - mechanical_timing
    - immobilizer

high_value_checks:
  - fuel_level
  - dtcs_before_clear
  - freeze_frame
  - rpm_while_cranking
  - voltage_while_cranking
  - ecu_fuses
  - ignition_coil_fuse
  - injector_fuse
  - sensor_fuse
  - fuel_pump_fuse
  - spark_test
  - fuel_pressure_scan_data

safety:
  gdi_high_pressure_line_opening: prohibited_as_diagnostic_shortcut
  direct_12v_to_gdi_injectors: prohibited
  continuous_cranking_over_10_seconds: avoid
  push_start_automatic: prohibited
```

---

# 31. Source / Confidence Notes

## VERIFIED — HYUNDAI OWNER DOCUMENTATION

- Normal starting is performed without depressing the accelerator.
- Starter engagement is limited to approximately 10 seconds per attempt.
- Hyundai's owner-level crank/no-start checks include fuel level and ignition-coil/spark-plug connections.

Sources:

- https://manualzz.com/doc/53857913/hyundai-2014-accent-owner-manual
- https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual

## VERIFIED — REPOSITORY HYUNDAI FUSE DATA

Relevant ECU, fuel-pump, injector, sensor, and ignition-coil circuits are documented in:

- `../specs/FUSES_AND_RELAYS.md`

## SUPPORTING SERVICE INFORMATION — CLOSELY RELATED 1.6 L ACCENT GDI

High-pressure fuel-system safety and architecture are supported by 2013 Accent 1.6 L service information:

- https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Powertrain%20Management/Fuel%20Delivery%20and%20Air%20Induction/Fuel%20Pump/Service%20and%20Repair/High%20Pressure%20Fuel%20Pump/
- https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Maintenance/Filters/Fuel%20Filter/Fuel%20Pressure%20Release/Service%20and%20Repair/

Exact 2014 VIN-specific service procedures and pressure specifications should be added only after authoritative verification.

---

# 32. Core Logic

```text
CRANKS
  ↓
RPM SIGNAL?
  ↓
SPARK?
  ↓
FUEL PRESSURE / INJECTION?
  ↓
AIR?
  ↓
COMPRESSION / TIMING?
  ↓
ROOT CAUSE
  ↓
REPAIR
  ↓
VERIFY HOT + COLD RESTART
```

Do not skip from **"cranks but won't start"** directly to **"buy a fuel pump."**

---

## Document Status

- **Vehicle:** 2014 Hyundai Accent SE
- **Topic:** Crank/no-start diagnosis
- **Status:** Initial field diagnostic guide
- **Factory owner guidance:** Included
- **GDI safety:** Included
- **VIN-specific fuel-pressure specifications:** Intentionally not guessed
- **Copyright approach:** Original diagnostic documentation with source-aware references
