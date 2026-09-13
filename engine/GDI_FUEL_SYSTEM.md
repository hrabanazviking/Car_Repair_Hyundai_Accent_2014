# 2014 Hyundai Accent SE - GDI Fuel System

> **Purpose:** Source-aware, field-oriented reference for the gasoline direct-injection fuel system used in the U.S.-market 2014 Hyundai Accent SE 1.6 L Gamma GDI engine. Designed for offline use by humans and AI/RAG systems.
>
> **Core rule:** Separate the **low-pressure supply side** from the **high-pressure GDI side** before diagnosing anything. Never open a GDI high-pressure connection casually.

---

## 1. Scope

This document covers:

- Fuel tank and in-tank pump
- Low-pressure supply line
- High-pressure mechanical pump
- Fuel-pressure control valve
- High-pressure pipe
- Fuel rail / delivery pipe
- Rail-pressure sensor
- Four direct injectors
- Fuel-pressure diagnosis
- Crank/no-start diagnosis
- Hot-start and restart problems
- Injector leakage and imbalance clues
- Electrical feeds and fuses
- Residual-pressure safety
- Field-use decision logic
- AI reasoning rules

Related files:

- `ENGINE_OVERVIEW.md`
- `IGNITION.md`
- `../diagnostics/CRANK_NO_START.md`
- `../diagnostics/MISFIRE.md`
- `../diagnostics/FUEL_TRIM_DIAGNOSTICS.md`
- `../specs/FUSES_AND_RELAYS.md`
- `../specs/FLUIDS_AND_CAPACITIES.md`

---

# 2. Confidence Labels

This file intentionally separates exact 2014 information from adjacent-year Gamma 1.6 GDI service information.

- **VERIFIED - 2014 PARTS CATALOG:** Confirmed in 2014 Accent OE parts-catalog data.
- **VERIFIED - 2014 OWNER MANUAL:** Confirmed in the 2014 Accent owner's manual.
- **SERVICE-FAMILY - 2012/2013 GAMMA 1.6 GDI:** Hyundai service information for the same closely related Gamma 1.6 GDI engine family in adjacent model years.
- **GENERAL DIAGNOSTIC PRACTICE:** Accepted diagnostic method, not claimed as a Hyundai factory specification.
- **OWNER-SPECIFIC / VIN-VERIFY:** Must be confirmed on the exact vehicle before purchasing parts or performing specification-critical service.

Unknown is preferable to a confident wrong answer.

---

# 3. System Architecture

The fuel path is:

```text
FUEL TANK
   ↓
IN-TANK ELECTRIC LOW-PRESSURE PUMP
   ↓
LOW-PRESSURE SUPPLY LINE
   ↓
MECHANICAL HIGH-PRESSURE FUEL PUMP
   ↓
HIGH-PRESSURE PIPE
   ↓
FUEL RAIL / DELIVERY PIPE
   ↓
FOUR DIRECT INJECTORS
   ↓
COMBUSTION CHAMBERS
```

Control and feedback path:

```text
RAIL PRESSURE SENSOR
        ↓
       ECM
        ↓
FUEL PRESSURE CONTROL VALVE
        ↓
HIGH-PRESSURE PUMP OUTPUT
```

The low-pressure electric pump supplies fuel to the engine-mounted high-pressure pump.

The high-pressure pump then raises fuel pressure to direct-injection levels and feeds the rail.

The ECM uses rail-pressure feedback to regulate commanded pressure through the fuel-pressure control valve.

---

# 4. 2014 Accent GDI Hardware Confirmed by OE Catalog

> **VERIFIED - 2014 PARTS CATALOG**

2014 Hyundai Accent 1.6 GDI catalog data identifies the following hardware family:

| Component | OE catalog evidence |
|---|---|
| High-pressure fuel pump | `35320-2B140` listed for applicable 2014 Accent configurations |
| Fuel rail / delivery pipe | `35340-2B100` |
| Rail / high-pressure sensor | `35342-2B100`, superseded in catalog by later number |
| Fuel injector | `35310-2B130`, quantity 4 |
| Injector clip | `35309-2B110`, quantity 4 |
| High-pressure fuel-pump roller tappet | `35325-2G700` family listing |

**VIN-VERIFY RULE:** Do not order solely from this table. Hyundai part numbers can supersede and production-date splits can exist. Confirm fitment by VIN before purchase.

Sources:

- https://www.hyundaipartsdeal.com/parts-list/2014-hyundai-accent/engine/throttle_body_injector.html
- https://www.hyundaipartsdeal.com/oem-2014-hyundai-accent-fuel_rail.html
- https://www.hyundaipartsdeal.com/oem-2014-hyundai-accent-fuel_injector.html

---

# 5. Low-Pressure Side

The low-pressure side includes:

- Fuel tank
- In-tank electric fuel pump
- Pump electrical circuit
- Fuel feed line
- Connections to the engine-mounted high-pressure pump

The low-pressure pump must provide enough fuel volume and pressure for the mechanical high-pressure pump to work correctly.

A failed high-pressure pump is not the only possible cause of low rail pressure.

If the low-pressure supply is weak, restricted, aerated, electrically underpowered, or empty, the high-pressure side can also fail to meet its target.

## Adjacent-year low-side pressure reference

> **SERVICE-FAMILY - 2013 GAMMA 1.6 GDI**

Hyundai service information for the 2013 Accent 1.6 GDI lists low-side fuel pressure at idle as:

```text
429-469 kPa
4.38-4.79 kgf/cm²
62.3-68.1 psi
```

It also states that after shutdown, gauge pressure should hold for about five minutes during the specified test.

This is a strong service-family reference, but it is not labeled here as a confirmed exact 2014 VIN-specific specification until an exact 2014 Hyundai service source is obtained.

Source:

- https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Powertrain%20Management/Fuel%20Delivery%20and%20Air%20Induction/Fuel%20Pump/Fuel%20Pressure/Testing%20and%20Inspection/

---

# 6. High-Pressure GDI Side

The high-pressure side includes:

- Mechanical high-pressure fuel pump
- Fuel-pressure control valve
- High-pressure metal pipe
- Fuel rail / delivery pipe
- Rail-pressure sensor
- Four direct injectors

This side operates at pressures far above ordinary port-injection systems.

## Service-family pressure range

> **SERVICE-FAMILY - 2012 GAMMA 1.6 GDI**

Hyundai diagnostic information for this engine family describes ECM-controlled high-side fuel pressure on the order of:

```text
40-150 bar
approximately 580-2175 psi
```

The ECM controls the fuel-pressure regulator / fuel-pressure control valve using feedback from the fuel-rail pressure sensor.

This range is useful for understanding system scale and diagnostic behavior. It is not a substitute for exact 2014 commanded-versus-actual specifications for a specific test condition.

Source:

- https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/A%20L%20L%20%20Diagnostic%20Trouble%20Codes%20%28%20DTC%20%29/Testing%20and%20Inspection/P%20Code%20Charts/P0092/General%20Information/

---

# 7. High-Pressure Pump Drive

> **SERVICE-FAMILY - 2013 GAMMA 1.6 GDI**

The high-pressure pump is mechanically driven through a **roller tappet** at the cylinder head.

Hyundai service instructions require the roller tappet to be placed at its lowest position before high-pressure-pump installation because pump spring force can otherwise damage the mounting hardware or cylinder-head surface.

This confirms that high-pressure output depends on mechanical engine rotation, not merely an electric pump command.

Diagnostic implication:

```text
ENGINE NOT ROTATING
      ↓
NO MECHANICAL HPFP STROKE
      ↓
NO NORMAL GDI RAIL PRESSURE BUILD
```

Mechanical cam/tappet/pump problems can therefore imitate electrical fuel-pressure faults.

Source:

- https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Powertrain%20Management/Fuel%20Delivery%20and%20Air%20Induction/Fuel%20Pump/Service%20and%20Repair/High%20Pressure%20Fuel%20Pump/

---

# 8. CRITICAL GDI SAFETY WALL

## Do not open the high-pressure side casually

> **SERVICE-FAMILY - HYUNDAI WARNING**

Hyundai warns that removing the following shortly after engine shutdown can cause injury from highly pressurized fuel:

- High-pressure fuel pump
- High-pressure fuel pipe
- Fuel rail / delivery pipe
- Injectors

Fuel can penetrate skin and cause serious injury.

### Never use these field methods

Do **not**:

- Crack a high-pressure line to "see if fuel comes out"
- Loosen an injector line during cranking
- Put a finger near a suspected high-pressure leak
- Search for a pinhole leak with bare skin
- Reuse a high-pressure pipe where Hyundai specifies replacement
- Apply an ordinary low-pressure fuel gauge directly to the high-pressure rail
- Disconnect high-pressure components immediately after shutdown

If high-pressure fuel injection into skin is suspected, treat it as a medical emergency even if the external wound appears small.

---

# 9. Hyundai Residual-Pressure Release Logic

> **SERVICE-FAMILY - 2013 GAMMA 1.6 GDI**

Hyundai's service procedure includes deliberate depressurization before opening the fuel system.

The service-family procedure includes:

1. Ignition OFF.
2. Disconnect battery negative.
3. Access and disconnect the in-tank fuel-pump electrical connection.
4. Disconnect the electrical connector at the high-pressure pump as specified in that procedure.
5. Reconnect the battery.
6. Run the engine long enough to reduce low- and high-side pressure. Hyundai's referenced procedure allows roughly 20 seconds and notes the engine may stop sooner.
7. Turn the engine off.
8. Cover connections with absorbent material before opening them because residual fuel may remain.
9. Reassemble fully.
10. Start and inspect carefully for leaks.
11. Clear any DTCs created by intentionally disconnecting fuel-system components.

**Important:** Use the exact service procedure for the exact vehicle before physically opening the high-pressure system. This summary explains the concept and is not a substitute for the factory procedure.

Source:

- https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Maintenance/Filters/Fuel%20Filter/Fuel%20Pressure%20Release/Service%20and%20Repair/

---

# 10. Fuel-System Electrical Feeds

From the repository's 2014 Hyundai fuse mapping:

## Engine compartment

| Circuit | Rating | Relevance |
|---|---:|---|
| F/PUMP | 15A | Fuel-pump relay / low-side supply |
| INJECTOR | 15A | Injector and related engine-control feed |
| ECU 1 | 30A | Main engine-control feed |
| ECU 2 | 10A | ECM/PCM feed |
| SENSOR | 10A | Engine sensors / controls including relevant management circuits |

See `../specs/FUSES_AND_RELAYS.md` for the complete source-aware table.

A good fuse proves only that the fuse element is intact.

It does **not** prove:

- Relay command
- Usable voltage at the pump
- Ground integrity
- Connector integrity
- Pump output under load
- Injector command
- Rail-pressure control

---

# 11. Fuel-System Diagnostic Hierarchy

For a crank/no-start or severe fuel-delivery problem:

```text
CRANKS BUT WILL NOT START
        ↓
READ DTCs + FREEZE FRAME
        ↓
DOES SCANNER SHOW CRANKING RPM?
        ↓ YES
VERIFY SYSTEM VOLTAGE
        ↓
CHECK LOW-PRESSURE PUMP CIRCUIT
        ↓
VERIFY LOW-SIDE SUPPLY
        ↓
COMPARE COMMANDED VS ACTUAL RAIL PRESSURE
        ↓
RAIL PRESSURE BUILDS?
   ├─ NO → low-side supply / HPFP / FPCV / sensor / mechanical drive / wiring
   └─ YES → injector command / ignition / compression / timing / other cause
```

Do not jump directly from "no start" to "bad fuel pump."

---

# 12. Low-Side vs High-Side Fault Separation

## Suspect low-side supply when

- No pump activity is detected when it should be commanded
- Low-side pressure is below specification
- Low-side pressure collapses under load
- Pump voltage is low under load
- F/PUMP fuse or relay circuit is faulty
- Fuel level is genuinely very low
- Supply line is restricted or damaged
- Rail pressure fails because the high-pressure pump is being starved

## Suspect high-side generation/control when

- Low-side supply is verified healthy
- Rail pressure remains too low compared with command
- High-pressure control DTCs are present
- Rail-pressure sensor data are implausible
- High-pressure pump control valve circuit faults are present
- Mechanical pump/tappet problems are suspected

## Suspect injector-side problems when

- Rail pressure is available but one cylinder misfires
- One cylinder repeatedly shows a fuel-related imbalance
- Plug appearance suggests one cylinder is wet or abnormally dry
- Injector electrical DTCs exist
- Compression and ignition test healthy
- Hot restart or residual-pressure behavior suggests leakage

---

# 13. Commanded vs Actual Rail Pressure

Where the scan tool exposes both values, compare:

- Desired / commanded fuel-rail pressure
- Actual measured rail pressure
- Engine RPM
- Battery/module voltage
- Throttle/load
- Fuel trims
- Relevant fuel-pressure-control duty or command, if supported

## Pattern A - Command rises, actual stays low

Possible causes:

- Weak low-pressure supply
- Weak mechanical high-pressure pump
- Fuel-pressure control valve fault
- High-pressure leak
- Injector leakage
- Mechanical pump-drive problem
- Rail-pressure sensor under-reporting
- Wiring/control fault

## Pattern B - Actual pressure appears implausibly high/low and does not behave naturally

Possible causes:

- Rail-pressure sensor fault
- Sensor power/reference problem
- Sensor ground problem
- Signal wiring fault
- Connector damage

## Pattern C - Command and actual track well

Look elsewhere before condemning fuel-pressure hardware.

---

# 14. Useful Fuel-System DTC Families

Exact supported DTCs vary by calibration and scan-tool capability, but common GDI diagnostic families include:

- `P0087` - fuel rail/system pressure too low
- `P0088` - fuel rail/system pressure too high
- `P0090/P0091/P0092` - fuel-pressure regulator/control circuit family
- `P0190-P0193` - fuel-rail pressure sensor circuit/range family
- `P0201-P0204` - injector circuit cylinder-specific family
- `P0300-P0304` - random / cylinder-specific misfire
- Lean/rich fuel-trim codes where mixture control is affected

**Rule:** Decode the exact code from a trustworthy current database. Do not assume a code names the failed part.

---

# 15. Hot-Start / Hot-Soak No-Start Logic

A hot engine that starts normally cold but becomes difficult to restart hot can point toward:

- Injector leakage
- Rail-pressure decay
- Fuel-vapor or supply issue
- Heat-sensitive high-pressure pump/control fault
- Heat-sensitive crank/cam signal fault
- Ignition-coil failure
- Sensor bias under heat

Do not assume "hot no-start = fuel."

Use evidence:

```text
HOT NO-START
   ↓
CRANKING RPM PRESENT?
   ↓
RAIL PRESSURE BUILDS?
   ↓
SPARK PRESENT?
   ↓
PLUGS WET OR DRY?
   ↓
COMPARE COLD VS HOT DATA
```

---

# 16. Injector Leakage Clues

Possible injector-leak clues include:

- Difficult hot restart
- One cylinder repeatedly rich
- Fuel odor at exhaust after restart
- One wet/fuel-fouled spark plug
- Rail pressure decays faster than expected after shutdown
- Oil level rising unexpectedly
- Engine oil smelling strongly of gasoline
- Rich fuel trims after restart

None of these proves an injector leak by itself.

A leaking high-pressure pump, purge problem, sensor bias, or other fueling fault can produce overlapping symptoms.

## Important oil-dilution warning

If gasoline contamination of the crankcase is suspected:

- Avoid unnecessary running.
- Confirm the fuel-system fault.
- Correct the source.
- Replace contaminated engine oil and filter before returning the engine to normal service.

Fuel-thinned oil can reduce lubrication protection.

---

# 17. Injector Imbalance Without a Dedicated Balance Test

If an enhanced scan tool does not offer Hyundai injector-balance testing, use comparative evidence:

- Cylinder-specific misfire counters
- Coil swap result
- Spark-plug appearance
- Compression result
- Injector electrical integrity
- Fuel trims
- Relative cylinder contribution where available
- Borescope evidence where appropriate

A cylinder-specific misfire that does not follow the coil or plug and has healthy compression increases suspicion of injector or localized intake/mechanical problems.

Do not replace an injector solely because a misfire stayed on one cylinder.

---

# 18. Rail-Pressure Sensor

> **VERIFIED - 2014 PARTS CATALOG / SERVICE-FAMILY FUNCTION**

The 2014 Accent catalog includes a high-pressure / rail-pressure sensor on the delivery pipe.

Hyundai service information for the same engine family instructs technicians to inspect rail-pressure-sensor output with a scan tool across engine speeds.

This means the sensor should be diagnosed as a **signal system**, not merely by resistance guessing.

Check:

- Reference voltage where applicable
- Ground
- Signal integrity
- Connector fit
- Harness damage
- Plausibility compared with commanded pressure and engine behavior

Source:

- https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Powertrain%20Management/Computers%20and%20Control%20Systems/Fuel%20Pressure%20Sensor/Service%20and%20Repair/

---

# 19. High-Pressure Pump Service-Family Hardware Rules

> **SERVICE-FAMILY - 2013 GAMMA 1.6 GDI**

Hyundai service information specifies several important one-time-use and installation practices around the high-pressure system.

Examples include:

- Do not reuse the high-pressure fuel pipe.
- Do not reuse specified high-pressure-pump mounting bolts.
- Install the high-pressure pump only with the roller tappet positioned correctly.
- Tighten the two pump mounting bolts incrementally and evenly.
- Confirm the low-pressure quick connector is fully latched.
- Inspect carefully for fuel leakage after assembly.

Service-family torque references:

| Item | Adjacent-year Hyundai value |
|---|---:|
| High-pressure fuel-pump mounting bolts | 12.8-14.7 N·m / 9.4-10.9 lb-ft |
| High-pressure fuel-pipe nuts | 26.5-32.4 N·m / 19.5-23.9 lb-ft |
| Delivery-pipe mounting bolts | 18.6-23.5 N·m / 13.7-17.4 lb-ft |

These values are **not promoted here to exact 2014 VIN-specific torque specifications** until exact 2014 Hyundai service information is verified.

Sources:

- https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Powertrain%20Management/Fuel%20Delivery%20and%20Air%20Induction/Fuel%20Pump/Service%20and%20Repair/High%20Pressure%20Fuel%20Pump/
- https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Powertrain%20Management/Fuel%20Delivery%20and%20Air%20Induction/Fuel%20Supply%20Line/Service%20and%20Repair/

---

# 20. Injector Seals and One-Time-Use Parts

> **SERVICE-FAMILY - 2013 GAMMA 1.6 GDI**

Hyundai specifies replacement of several injector-related sealing/retaining pieces when the injector/rail assembly is serviced.

Service-family warnings include not reusing items such as:

- Injector fixing clip
- Injector O-ring
- Support disc
- Rubber washer
- Combustion seal
- Specified mounting bolt(s)

Direct-injection injector sealing is not equivalent to casually reinstalling an old port-injection O-ring.

If an injector is removed, use the exact current Hyundai parts/procedure for the VIN and repair operation.

---

# 21. Fuel Leak Decision Tree

```text
SMELL RAW FUEL / SEE WETNESS
          ↓
SHUT ENGINE OFF
          ↓
NO SMOKING / NO FLAME / NO SPARK SOURCE
          ↓
DO NOT TOUCH SUSPECTED HIGH-PRESSURE SPRAY
          ↓
IDENTIFY LOW-SIDE VS HIGH-SIDE AREA FROM SAFE DISTANCE
          ↓
HIGH-PRESSURE SYSTEM SUSPECTED?
          ├─ YES → TOW / PROPER SERVICE PROCEDURE
          └─ NO  → REPAIR ONLY IF SAFE AND COMPETENT
```

A fuel leak is a fire hazard.

Do not continue driving simply because the leak appears small.

---

# 22. Crank-No-Start Fuel Checklist

Before blaming the fuel system, preserve evidence.

## Scanner

- [ ] Stored DTCs
- [ ] Pending DTCs
- [ ] Permanent DTCs
- [ ] Freeze-frame data
- [ ] Cranking RPM
- [ ] Module voltage while cranking
- [ ] Fuel-rail pressure actual
- [ ] Fuel-rail pressure desired, if supported
- [ ] Injector-related DTCs

## Low side

- [ ] Fuel level credible
- [ ] F/PUMP fuse intact
- [ ] Pump circuit powered when commanded
- [ ] Pump ground good
- [ ] Low-side pressure tested if necessary

## High side

- [ ] Rail pressure increases during cranking
- [ ] Actual pressure plausibly follows command
- [ ] Rail-pressure sensor signal plausible
- [ ] High-pressure control circuit DTC-free or diagnosed

## Then branch outward

If pressure is adequate but the engine still does not start, test:

- Ignition
- Injector command
- Crank/cam synchronization
- Compression
- Mechanical timing

---

# 23. Fuel Trim Connections

Fuel-system faults can appear in fuel trims.

## Positive trim can come from

- Weak fuel supply
- Injector restriction
- Low rail pressure
- Unmetered air / intake leak
- Exhaust leak ahead of feedback sensor
- Sensor bias

## Negative trim can come from

- Leaking injector
- Excessive commanded fuel pressure
- Faulty pressure sensing
- EVAP purge fault
- Sensor bias

Fuel trims alone cannot tell you which subsystem is at fault.

See `../diagnostics/FUEL_TRIM_DIAGNOSTICS.md`.

---

# 24. Remote / Nomad Field Strategy

For remote travel, prioritize **non-invasive diagnosis**.

Useful field equipment:

- OBD-II scanner capable of live data
- Digital multimeter
- Fuse assortment of correct types/ratings
- Flashlight
- Fuel-resistant gloves
- Safety glasses
- Absorbent shop towels
- Fire extinguisher rated for flammable-liquid/electrical vehicle fires

Do not carry improvised equipment for opening GDI high-pressure lines roadside.

The safe field win is often:

```text
IDENTIFY THE FAILED SUBSYSTEM
        ↓
AVOID MAKING IT WORSE
        ↓
DECIDE DRIVE / TOW / REPAIR
```

not:

```text
DISASSEMBLE THE RAIL IN THE WOODS
```

---

# 25. Fuel Quality

> **VERIFIED - 2014 OWNER MANUAL**

The 2014 Accent is designed for unleaded gasoline of at least:

```text
87 AKI
91 RON
```

Hyundai also warns against indiscriminate use of unspecified fuel-system cleaning agents.

See `../specs/FLUIDS_AND_CAPACITIES.md` for the repository's complete fuel specification notes.

Owner's-manual source:

- https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/

---

# 26. AI Diagnostic Rules

An AI assistant using this file should follow these rules:

1. Never equate a fuel-pressure DTC with a failed fuel pump.
2. Separate low-pressure supply from high-pressure generation/control.
3. Preserve DTCs, freeze frame, and live data before clearing anything.
4. Ask whether rail pressure rises during cranking.
5. Ask whether desired and actual rail pressure agree where available.
6. Confirm system voltage before interpreting strange fuel-system behavior.
7. Treat GDI high-pressure components as hazardous.
8. Never instruct the user to crack a high-pressure line as a diagnostic shortcut.
9. Treat adjacent-year pressure/torque values as service-family references unless exact 2014 data is verified.
10. If rail pressure is normal, move to injector command, ignition, compression, and timing rather than continuing to blame fuel pressure.
11. If a raw-fuel leak is suspected, prioritize fire safety and towing over continued diagnosis.
12. Do not recommend parts purchases until testing isolates the fault.

---

# 27. Machine-Readable Summary

```yaml
vehicle:
  year: 2014
  make: Hyundai
  model: Accent
  trim: SE
  market: US
  engine: Gamma 1.6 GDI

fuel_system:
  type: gasoline_direct_injection
  architecture:
    - fuel_tank
    - electric_low_pressure_pump
    - low_pressure_feed
    - mechanical_high_pressure_pump
    - fuel_pressure_control_valve
    - high_pressure_pipe
    - fuel_rail
    - rail_pressure_sensor
    - four_direct_injectors

low_side_reference:
  source_scope: 2013_same_engine_family
  idle_pressure_psi: "62.3-68.1"
  idle_pressure_kpa: "429-469"
  exact_2014_vin_verified: false

high_side_reference:
  source_scope: 2012_same_engine_family
  control_range_bar: "40-150"
  approximate_psi: "580-2175"
  exact_2014_vin_verified: false

confirmed_2014_catalog_parts:
  high_pressure_pump_family: "35320-2B140"
  fuel_rail: "35340-2B100"
  injector: "35310-2B130"
  injector_quantity: 4
  rail_pressure_sensor_family: "35342-2B100"

fuses:
  fuel_pump: "F/PUMP 15A"
  injectors: "INJECTOR 15A"
  ecu_main: "ECU 1 30A"
  ecu_secondary: "ECU 2 10A"
  sensor_feed: "SENSOR 10A"

safety:
  high_pressure_fuel_hazard: true
  release_residual_pressure_before_opening: true
  crack_high_pressure_line_for_testing: prohibited
  skin_contact_with_suspected_pressure_jet: prohibited
  tow_if_high_pressure_leak_suspected: true

diagnostic_order:
  - preserve_codes_and_freeze_frame
  - verify_cranking_rpm
  - verify_system_voltage
  - verify_low_pressure_supply
  - compare_commanded_and_actual_rail_pressure
  - evaluate_high_pressure_control
  - evaluate_injector_command
  - branch_to_ignition_compression_timing_if_pressure_ok
```

---

# 28. Source Notes

Primary references used for this file:

- 2014 Hyundai Accent owner's manual:
  - https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/
- 2014 Accent OE catalog, throttle body / injector / high-pressure fuel hardware:
  - https://www.hyundaipartsdeal.com/parts-list/2014-hyundai-accent/engine/throttle_body_injector.html
- 2014 Accent fuel rail catalog:
  - https://www.hyundaipartsdeal.com/oem-2014-hyundai-accent-fuel_rail.html
- 2014 Accent injector catalog:
  - https://www.hyundaipartsdeal.com/oem-2014-hyundai-accent-fuel_injector.html
- 2013 Accent 1.6 GDI fuel-pressure test:
  - https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Powertrain%20Management/Fuel%20Delivery%20and%20Air%20Induction/Fuel%20Pump/Fuel%20Pressure/Testing%20and%20Inspection/
- 2013 Accent 1.6 GDI residual-pressure release:
  - https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Maintenance/Filters/Fuel%20Filter/Fuel%20Pressure%20Release/Service%20and%20Repair/
- 2013 Accent 1.6 GDI high-pressure pump service:
  - https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Powertrain%20Management/Fuel%20Delivery%20and%20Air%20Induction/Fuel%20Pump/Service%20and%20Repair/High%20Pressure%20Fuel%20Pump/
- 2013 Accent 1.6 GDI fuel-supply / rail / injector service:
  - https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Powertrain%20Management/Fuel%20Delivery%20and%20Air%20Induction/Fuel%20Supply%20Line/Service%20and%20Repair/
- 2012 Accent 1.6 GDI fuel-pressure-control diagnostic description:
  - https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/A%20L%20L%20%20Diagnostic%20Trouble%20Codes%20%28%20DTC%20%29/Testing%20and%20Inspection/P%20Code%20Charts/P0092/General%20Information/

---

## Repository Principle

```text
FUEL PROBLEM
    ↓
SEPARATE LOW SIDE FROM HIGH SIDE
    ↓
MEASURE / OBSERVE / COMPARE COMMAND TO ACTUAL
    ↓
DO NOT OPEN HIGH-PRESSURE HARDWARE CASUALLY
    ↓
ISOLATE ROOT CAUSE
    ↓
REPAIR
    ↓
VERIFY PRESSURE + LEAK-FREE OPERATION
```
