# Diagnostic Trouble Code Index — 2014 Hyundai Accent SE

> **Vehicle focus:** U.S.-market 2014 Hyundai Accent SE, 1.6L Gamma GDI, 6-speed automatic, FWD  
> **Purpose:** Fast routing from a scan-tool code to the correct diagnostic workflow.  
> **Rule:** A DTC identifies a condition the control module detected. It does **not** automatically identify a failed part.

---

## 1. Core Doctrine

```text
DTC
 ↓
PRESERVE THE EVIDENCE
 ↓
IDENTIFY THE REPORTING MODULE
 ↓
CHECK VOLTAGE / POWER / GROUNDS
 ↓
CLASSIFY THE CODE
 ↓
FOLLOW THE CORRECT SYSTEM GUIDE
 ↓
TEST THE CIRCUIT / COMPONENT / MECHANICAL SYSTEM
 ↓
ISOLATE ROOT CAUSE
 ↓
REPAIR
 ↓
VERIFY UNDER ENABLE CONDITIONS
 ↓
RESCAN ALL MODULES
```

Never use this logic:

```text
P0xxx CODE
   ↓
GOOGLE PART NAME
   ↓
BUY PART
```

A sensor code can be caused by wiring, connector damage, low voltage, bad grounds, shared-reference faults, mechanical problems, fluid problems, software calibration, another failed component, or the sensor itself.

---

## 2. DTC Format

SAE J2012 uses five-character Diagnostic Trouble Codes.

Example:

```text
P0301
││└── specific fault index
│└─── code family / subsystem
└──── system family
```

### First character

| Prefix | General area |
|---|---|
| `P` | Powertrain |
| `B` | Body |
| `C` | Chassis |
| `U` | Network communication |

SAE J2012 assigns `P0`, `C0`, `B0`, and `U0` families to standardized areas and also defines manufacturer-controlled and extended ranges. Do **not** assume every non-zero second character means the same thing across every family. Always verify the exact code definition for the reporting module and vehicle.

**Primary standards references:**

- SAE J2012 historical public copy: https://ptacts.uspto.gov/ptacts/public-informations/petitions/1532543/download-documents?artifactId=LxtzK1g8Pp1TwzB8NAVFIyZd6qbjMbs9ZGsiPl3T-bZWf0_AFDk7DNg
- California OBD regulation referencing SAE J2012 code use: https://www3.epa.gov/region9/CA-Air-SIP/California%20Code%20of%20Regulations/Title%2013%2C%20Division%203%2C%20Chapter%201%2C%20Article%202%2C%20Section%201971.1.pdf

---

## 3. Record More Than the Code

Before clearing anything, record:

- exact DTC
- reporting module
- current / stored / pending / permanent status if shown
- freeze-frame data
- engine speed
- coolant temperature
- vehicle speed
- calculated load
- fuel trims
- MAP
- intake-air temperature
- throttle command and actual position if relevant
- fuel pressure if available
- transmission temperature if relevant
- system voltage
- mileage
- warning lights
- symptoms
- weather / ambient temperature
- whether the fault happened cold, hot, at idle, cruising, accelerating, braking, or after refueling
- recent repairs, battery disconnects, jump starts, underbody impacts, water exposure, or wiring work

A screenshot of the scan-tool screen is often more useful than a handwritten code alone.

---

## 4. Reporting Module Matters

The same code number can appear in more than one Hyundai module.

A useful same-generation example is `C1616`.

Hyundai service information shows `C1616` being used by:

- ABS/ESC for CAN bus-off
- TPMS for CAN communication failure
- EPS/MDPS for CAN bus-off

Therefore:

```text
"C1616"
   ≠
COMPLETE DIAGNOSIS
```

Record:

```text
MODULE + CODE + STATUS
```

Example:

```text
ABS/ESC — C1616 — CURRENT
```

Same-generation references:

- ABS/ESC C1616: https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/A%20L%20L%20%20Diagnostic%20Trouble%20Codes%20%28%20DTC%20%29/Testing%20and%20Inspection/C%20Code%20Charts/C1616/Brake/General%20Information/
- TPMS C1616: https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/A%20L%20L%20%20Diagnostic%20Trouble%20Codes%20%28%20DTC%20%29/Testing%20and%20Inspection/C%20Code%20Charts/C1616/TPMS/General%20Information/
- EPS C1616: https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/A%20L%20L%20%20Diagnostic%20Trouble%20Codes%20%28%20DTC%20%29/Testing%20and%20Inspection/C%20Code%20Charts/C1616/Steering/General%20Information/

---

# 5. First-Pass Triage by Code Pattern

## One isolated code

Usually begin with the circuit or system named by the code.

## Many unrelated codes at once

Check first:

1. battery state
2. charging voltage
3. battery terminals
4. engine / body / transmission grounds
5. main fuses
6. shared sensor 5V reference
7. CAN network health

A low-voltage event can generate a forest of misleading codes.

See:

- `diagnostics/CHARGING_SYSTEM.md`
- `electrical/BATTERY_STARTER_ALTERNATOR.md`
- `electrical/GROUND_POINTS.md`
- `electrical/CAN_NETWORK_DIAGNOSTICS.md`

## Multiple sensor circuit codes

Suspect a shared power, reference, or ground before replacing multiple sensors.

See:

- `electrical/WIRING_AND_CONNECTOR_DIAGNOSTICS.md`
- `electrical/GROUND_POINTS.md`

## Misfire + catalyst code

Repair the misfire first.

A catalyst can be damaged by prolonged misfire, and catalyst-monitor data can be invalid while combustion is abnormal.

See:

- `diagnostics/MISFIRE.md`
- `engine/EXHAUST_CATALYST_O2_SENSORS.md`

## Timing code + oil concern

Check oil level, condition, pressure, OCV circuit, and mechanical timing before condemning a cam phaser.

See:

- `engine/TIMING_CVVT.md`
- `engine/LUBRICATION_SYSTEM.md`

## U-codes + weak battery / recent jump start

Resolve voltage stability first, then clear and recheck communication faults.

See:

- `electrical/CAN_NETWORK_DIAGNOSTICS.md`
- `diagnostics/CHARGING_SYSTEM.md`

---

# 6. Master Powertrain DTC Routing Index

This is a **curated Accent-focused index**, not an exhaustive SAE code database.

Status labels used here:

- **EXACT / APPLICABLE:** Direct Hyundai source explicitly applies to Accent RB or the exact same-generation Accent.
- **SERVICE-FAMILY:** Same-generation or same-engine Hyundai service data used as supporting evidence.
- **GENERIC:** Standardized SAE/OBD meaning. Vehicle-specific testing is still required.

---

## 6.1 Timing / CVVT / Oil-Control Codes

| Code | Meaning / diagnostic direction | Route |
|---|---|---|
| `P0011` | Intake CVVT target-versus-actual performance fault | `engine/TIMING_CVVT.md` |
| `P0014` | Exhaust CVVT target-versus-actual performance fault | `engine/TIMING_CVVT.md` |
| `P0016` | Crankshaft / intake cam correlation | `engine/TIMING_CVVT.md` |
| `P0017` | Crankshaft / exhaust cam correlation | `engine/TIMING_CVVT.md` |
| `P0075` | Intake oil-control valve circuit | `engine/TIMING_CVVT.md` |
| `P0076` | Intake OCV circuit low | `engine/TIMING_CVVT.md` |
| `P0077` | Intake OCV circuit high | `engine/TIMING_CVVT.md` |
| `P0078` | Exhaust OCV circuit | `engine/TIMING_CVVT.md` |
| `P0079` | Exhaust OCV circuit low | `engine/TIMING_CVVT.md` |
| `P0080` | Exhaust OCV circuit high | `engine/TIMING_CVVT.md` |

Same-generation Hyundai P0011 diagnostics explicitly begin with engine-oil level, oil contamination, OCV-filter contamination, and oil-path restriction before component replacement.

Sources:

- P0011 overview: https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/A%20L%20L%20%20Diagnostic%20Trouble%20Codes%20%28%20DTC%20%29/Testing%20and%20Inspection/P%20Code%20Charts/P0011/General%20Information/
- P0011 system inspection: https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/A%20L%20L%20%20Diagnostic%20Trouble%20Codes%20%28%20DTC%20%29/Testing%20and%20Inspection/P%20Code%20Charts/P0011/System%20Inspection/
- P0075 OCV inspection: https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/A%20L%20L%20%20Diagnostic%20Trouble%20Codes%20%28%20DTC%20%29/Testing%20and%20Inspection/P%20Code%20Charts/P0075/Component%20Inspection/

---

## 6.2 GDI Fuel-Pressure Codes

| Code family | Diagnostic direction | Route |
|---|---|---|
| `P008x` | Fuel-pressure regulation / regulator circuits | `engine/GDI_FUEL_SYSTEM.md` |
| `P0191` | Fuel rail pressure sensor range / performance | `engine/GDI_FUEL_SYSTEM.md` |

Same-generation service information describes the high-pressure fuel system as ECM-controlled using fuel-rail pressure feedback.

Example:

- P0092: https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/A%20L%20L%20%20Diagnostic%20Trouble%20Codes%20%28%20DTC%20%29/Testing%20and%20Inspection/P%20Code%20Charts/P0092/General%20Information/
- P0191: https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/A%20L%20L%20%20Diagnostic%20Trouble%20Codes%20%28%20DTC%20%29/Testing%20and%20Inspection/P%20Code%20Charts/P0191/Component%20Inspection/

**Safety:** Never crack open a GDI high-pressure line merely to “see if fuel comes out.”

---

## 6.3 Air / MAP / IAT / Throttle Codes

| Code family | Diagnostic direction | Route |
|---|---|---|
| `P010x` | MAP / manifold-pressure plausibility or circuit | `engine/AIR_INTAKE_THROTTLE_MAP.md` |
| `P011x` | Intake-air-temperature circuit / plausibility | `engine/AIR_INTAKE_THROTTLE_MAP.md` |
| `P012x` | Throttle / accelerator sensor family | `engine/AIR_INTAKE_THROTTLE_MAP.md` |
| `P022x` | Throttle-position / pedal-position family | `engine/AIR_INTAKE_THROTTLE_MAP.md` |
| `P2118` | Throttle actuator motor current range / performance | `engine/AIR_INTAKE_THROTTLE_MAP.md` |

Same-generation Hyundai information shows the electronic throttle body includes the actuator and TPS feedback, while accelerator-pedal sensors provide driver-demand input.

P2118 source:

https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/A%20L%20L%20%20Diagnostic%20Trouble%20Codes%20%28%20DTC%20%29/Testing%20and%20Inspection/P%20Code%20Charts/P2118/General%20Information/

P0222 example:

https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/A%20L%20L%20%20Diagnostic%20Trouble%20Codes%20%28%20DTC%20%29/Testing%20and%20Inspection/P%20Code%20Charts/P0222/General%20Information/

**Important:** This Gamma GDI uses MAP/IAT speed-density logic. Do not default to generic “clean the MAF” advice.

---

## 6.4 Fuel-Trim Codes

| Code | Meaning / direction | Route |
|---|---|---|
| `P0171` | System too lean | `diagnostics/FUEL_TRIM_DIAGNOSTICS.md` |
| `P0172` | System too rich | `diagnostics/FUEL_TRIM_DIAGNOSTICS.md` |
| `P2188` | System too rich at idle, Bank 1 | `diagnostics/FUEL_TRIM_DIAGNOSTICS.md` |
| `P2192` | System too rich at higher load, Bank 1 | `diagnostics/FUEL_TRIM_DIAGNOSTICS.md` |

Investigate:

- vacuum leaks
- PCV flow
- EVAP purge leakage
- MAP plausibility
- fuel pressure
- injector leakage / restriction
- exhaust leaks
- oxygen-sensor feedback
- misfire
- engine mechanical condition

Hyundai issued a bulletin for certain 2012–2013 Accent RB 1.6 GDI A/T vehicles for P2192 that involved ECM software rather than a mechanical failure. This is an excellent reminder that calibration can be part of the diagnostic tree.

Source:

https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Technical%20Service%20Bulletins/All%20Technical%20Service%20Bulletins/Engine%20Controls%20-%20MIL%20ON%2C%20DTC%20P2192%20Set/

---

## 6.5 Misfire Codes

| Code | Meaning | Route |
|---|---|---|
| `P0300` | Random / multiple-cylinder misfire | `diagnostics/MISFIRE.md` |
| `P0301` | Cylinder 1 misfire | `diagnostics/MISFIRE.md` |
| `P0302` | Cylinder 2 misfire | `diagnostics/MISFIRE.md` |
| `P0303` | Cylinder 3 misfire | `diagnostics/MISFIRE.md` |
| `P0304` | Cylinder 4 misfire | `diagnostics/MISFIRE.md` |

Do not stop at spark plugs.

Use:

```text
spark
fuel
injector command
air
compression
valve clearance
timing
wiring
```

Same-generation Hyundai P0301 service information includes spark-plug inspection and compression testing as part of the diagnostic tree.

Source:

https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/A%20L%20L%20%20Diagnostic%20Trouble%20Codes%20%28%20DTC%20%29/Testing%20and%20Inspection/P%20Code%20Charts/P0301/System%20Inspection/

**Flashing MIL / severe misfire:** Reduce engine load and stop driving when continued operation risks catalyst damage.

---

## 6.6 Catalyst / Oxygen-Sensor Codes

| Code / family | Diagnostic direction | Route |
|---|---|---|
| `P0420` | Catalyst efficiency below threshold | `engine/EXHAUST_CATALYST_O2_SENSORS.md` |
| `P003x` | O2 / A/F sensor heater circuits | `engine/EXHAUST_CATALYST_O2_SENSORS.md` |
| `P013x` | Oxygen-sensor circuit / response family | `engine/EXHAUST_CATALYST_O2_SENSORS.md` |

Rule:

```text
P0420
  ≠
AUTOMATIC CATALYTIC-CONVERTER REPLACEMENT
```

Before condemning the catalyst, check:

- active misfire
- rich running
- oil burning
- coolant contamination
- exhaust leaks
- sensor wiring
- sensor response
- physical catalyst damage

---

## 6.7 EVAP Codes

| Code | Direction | Route |
|---|---|---|
| `P0441` | Incorrect purge flow | `engine/EVAP_PURGE_SYSTEM.md` |
| `P0442` | Small EVAP leak | `engine/EVAP_PURGE_SYSTEM.md` |
| `P0446` | Vent-control fault | `engine/EVAP_PURGE_SYSTEM.md` |
| `P0455` | Large EVAP leak | `engine/EVAP_PURGE_SYSTEM.md` |
| `P0456` | Very small EVAP leak | `engine/EVAP_PURGE_SYSTEM.md` |
| `P2422` | Vent valve stuck closed / vent restriction | `engine/EVAP_PURGE_SYSTEM.md` |

Same-generation Hyundai P0456 information describes the charcoal canister, purge valve, fuel-tank pressure sensor, and vacuum-decay leak test.

Source:

https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/A%20L%20L%20%20Diagnostic%20Trouble%20Codes%20%28%20DTC%20%29/Testing%20and%20Inspection/P%20Code%20Charts/P0456/General%20Information/

Supplemental Hyundai EVAP diagnostic reference:

https://charm.li/Hyundai/2010/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Powertrain%20Management/Computers%20and%20Control%20Systems/Technical%20Service%20Bulletins/All%20Technical%20Service%20Bulletins/Emissions%20-%20Supplemental%20EVAP%20System%20Diagnostics/

---

## 6.8 Cooling-System / Thermostat Code

| Code | Meaning | Route |
|---|---|---|
| `P0128` | Coolant temperature below thermostat regulating temperature | `engine/COOLING_SYSTEM.md` |

Same-generation Hyundai service information checks thermostat condition and opening temperature as part of P0128 diagnosis.

Source:

https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/A%20L%20L%20%20Diagnostic%20Trouble%20Codes%20%28%20DTC%20%29/Testing%20and%20Inspection/P%20Code%20Charts/P0128/Component%20Inspection/

Do not confuse P0128 with an overheating code. It usually indicates the engine is warming too slowly or the reported temperature is implausibly low under the monitor conditions.

---

# 7. Automatic-Transmission DTC Index

Route transmission codes to:

`transmission/SIX_SPEED_AUTOMATIC.md`

Hyundai issued multiple Accent RB bulletins for transmission-sensor and range-switch codes. These are valuable because they show that Hyundai expects targeted sensor / harness / switch diagnosis rather than automatic complete-transmission replacement.

---

## 7.1 Range / Inhibitor Switch

| Code | Hyundai description |
|---|---|
| `P0705` | Range switch sensor circuit |
| `P0706` | Range switch range / performance |
| `P0707` | Range switch open circuit |
| `P0708` | Range switch short circuit or multiple inputs |

Possible symptoms include:

- MIL
- incorrect / missing gear indication
- fail-safe operation
- intermittent no-crank in Park or Neutral

Hyundai TSB 19-AT-024H explicitly applies to 2012–2017 Accent RB.

Source:

https://static.nhtsa.gov/odi/tsbs/2019/MC-10169380-9999.pdf

---

## 7.2 Transmission-Fluid Temperature Sensor

| Code | Hyundai description |
|---|---|
| `P0711` | Transmission fluid temperature sensor rationality / range |
| `P0712` | Transmission fluid temperature sensor circuit low |
| `P0713` | Transmission fluid temperature sensor circuit high |

Hyundai TSB 20-AT-014H explicitly applies to 2012–2017 Accent RB.

Source:

https://static.nhtsa.gov/odi/tsbs/2020/MC-10174799-0001.pdf

---

## 7.3 Input / Output Speed Sensors

| Code | Direction |
|---|---|
| `P0717` | Input / turbine speed sensor no signal |
| `P0721` | Output speed sensor range / performance |
| `P0722` | Output speed sensor no signal |

Hyundai transmission bulletin coverage includes 2012–2017 Accent RB 1.6L.

Source:

https://static.nhtsa.gov/odi/tsbs/2020/MC-10173548-0001.pdf

Rule:

```text
SPEED-SENSOR CODE
      ≠
BAD TRANSMISSION
```

Check sensor, harness, connector, power / ground, debris / physical damage where applicable, and live-data behavior before escalating.

---

# 8. Chassis Codes

A basic code reader may not access ABS, ESC, MDPS/EPS, or TPMS. An enhanced scanner may be required.

---

## 8.1 CAN Timeout from ABS/ESC

| Code | Same-generation Hyundai meaning | Route |
|---|---|---|
| `C1612` | ABS/ESC CAN timeout waiting for TCM message | `electrical/CAN_NETWORK_DIAGNOSTICS.md` |
| `C1687` | ABS/ESC CAN timeout waiting for MDPS/EPS message | `electrical/CAN_NETWORK_DIAGNOSTICS.md` |
| `C1616` | CAN bus-off, module context required | `electrical/CAN_NETWORK_DIAGNOSTICS.md` |

Sources:

- C1612: https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/A%20L%20L%20%20Diagnostic%20Trouble%20Codes%20%28%20DTC%20%29/Testing%20and%20Inspection/C%20Code%20Charts/C1612/General%20Information/
- C1687: https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/A%20L%20L%20%20Diagnostic%20Trouble%20Codes%20%28%20DTC%20%29/Testing%20and%20Inspection/C%20Code%20Charts/C1687/General%20Information/

If ABS reports a timeout waiting for another module, do not automatically replace the ABS module.

Ask:

```text
WHO REPORTED THE CODE?
WHO IS MISSING?
IS THE MISSING MODULE POWERED?
IS ITS GROUND GOOD?
IS THE NETWORK HEALTHY?
```

---

# 9. U-Code / Network Index

Route all network faults first to:

`electrical/CAN_NETWORK_DIAGNOSTICS.md`

Example:

| Code | General meaning | First questions |
|---|---|---|
| `U0101` | Lost communication with TCM | Is TCM powered? Grounded? Visible on network? |

A communication code tells you one module could not hear another module. It does **not** prove the silent module itself is defective.

Older Hyundai documentation shows the diagnostic concept clearly for U0101: the ECM detects missing TCM messages on the CAN line.

Supporting reference:

https://charm.li/Hyundai/2008/Accent%20L4-1.6L/Repair%20and%20Diagnosis/A%20L%20L%20%20Diagnostic%20Trouble%20Codes%20%28%20DTC%20%29/Testing%20and%20Inspection/U%20Code%20Charts/U0101/

For the 2014 Accent, exact module-specific service information outranks this older example.

---

# 10. Body Codes

`B` codes may involve systems such as:

- SRS / airbags
- HVAC
- lighting
- body electronics
- door / lock circuits
- cluster-related functions

This repo does not yet maintain a complete 2014 Accent body-code database.

For an unknown B-code:

1. record the reporting module
2. record the complete code and any suffix
3. check battery voltage
4. verify module power / ground
5. inspect related fuses and connectors
6. obtain exact 2014 Hyundai module-specific diagnostic information before replacing parts

**SRS warning:** Do not probe airbag squib / inflator circuits with ordinary test equipment unless the exact service procedure explicitly permits it.

---

# 11. Code-Type Logic

The wording of a DTC often tells you what kind of test should come first.

## Circuit low

Possible causes include:

- short to ground
- open power feed
- high resistance
- sensor internally pulling signal low
- bad reference voltage
- connector corrosion

## Circuit high

Possible causes include:

- short to voltage
- open ground
- open signal wire with pull-up behavior
- sensor internal fault

## Range / performance / rationality

The circuit may be electrically intact while the signal is physically implausible.

Investigate:

- mechanical condition
- fluid / pressure
- sensor bias
- wiring resistance
- incorrect installation
- correlation with other sensors

## Correlation

Compare two signals that should agree.

Examples:

- crank vs cam
- dual TPS tracks
- dual accelerator-pedal tracks
- command vs actual position

## No signal

Do not automatically replace the sensor.

Check:

- power
- ground
- signal circuit
- connector
- damaged reluctor / target
- mechanical rotation
- module input

## Timeout / lost communication

Check:

- system voltage
- module power
- module ground
- CAN wiring
- connector integrity
- network termination / topology
- whether the module is actually awake

---

# 12. DTC Priority Rules

When several codes are present, use this order unless exact Hyundai service information says otherwise.

## Priority 1 — Immediate safety / engine-damage risks

Examples:

- active oil-pressure warning
- severe overheating
- flashing MIL / severe misfire
- brake hydraulic warning
- major steering-control failure
- severe fuel leak

Stop driving when the condition itself is unsafe, regardless of DTC priority.

## Priority 2 — Power / ground / voltage

Low voltage can corrupt diagnostics across several modules.

## Priority 3 — Network communication

Restore missing modules before trusting downstream codes that depend on their data.

## Priority 4 — Primary sensor / actuator circuit faults

Fix known electrical faults before chasing rationality codes caused by missing inputs.

## Priority 5 — Performance / rationality / emissions codes

Interpret these after the enabling systems are healthy.

---

# 13. Freeze-Frame Strategy

Freeze-frame information can preserve the conditions present when the fault set.

Record especially:

```text
RPM
vehicle speed
coolant temp
intake temp
MAP
load
STFT
LTFT
throttle
system voltage
fuel pressure if available
```

Examples:

### Lean at idle only

Think first about:

- vacuum leak
- PCV
- purge leak

### Lean under load

Think more about:

- fuel delivery
- fuel pressure
- injector flow
- exhaust-sensor plausibility

### Misfire only cold

Consider:

- plug / coil moisture
- injector behavior
- compression / valve clearance
- coolant intrusion

### Timing fault only hot

Consider:

- oil viscosity / pressure
- sticking OCV
- phaser leakage
- wiring affected by heat

---

# 14. Pending, Stored, and Permanent Codes

See the detailed discussion in:

`diagnostics/OBD2_GUIDE.md`

General rules:

- **Pending:** monitor detected a fault but confirmation criteria may not yet be complete.
- **Stored / confirmed:** monitor criteria were met sufficiently to store the fault.
- **Permanent:** emissions-related code retained until the vehicle proves through successful monitor operation that the fault is corrected.

Do not repeatedly clear codes during diagnosis. Clearing can erase freeze frame, reset readiness monitors, and destroy useful evidence.

---

# 15. Verification After Repair

A repair is not complete because the MIL went out.

Use:

```text
REPAIR
  ↓
CLEAR ONLY WHEN APPROPRIATE
  ↓
OPERATE UNDER CODE ENABLE CONDITIONS
  ↓
RESCAN
  ↓
CHECK LIVE DATA
  ↓
CHECK PENDING CODES
  ↓
CHECK READINESS
  ↓
VERIFY SYMPTOM IS GONE
```

Hyundai service procedures repeatedly require clearing the code, operating the vehicle under the DTC's enabling conditions, and rescanning to confirm that the fault does not return.

Hyundai readiness reference:

https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Powertrain%20Management/Computers%20and%20Control%20Systems/Testing%20and%20Inspection/Monitors%2C%20Trips%2C%20Drive%20Cycles%20and%20Readiness%20Codes/

---

# 16. Accent-Specific TSB-Aware Codes

Same-generation Hyundai bulletin indexes identify several code groups worth checking against current Hyundai service information before parts replacement:

```text
P0456 / P0461
P0128 / P0191 / P061B / P2188
P2192
P0705 / P0706 / P0707 / P0708
P0711 / P0712 / P0713
P0717 / P0721 / P0722
```

Same-generation TSB index:

https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Technical%20Service%20Bulletins/

A TSB does not prove that a particular car has that problem. It tells the diagnostician that Hyundai published known service information for the symptom / DTC family.

---

# 17. Cross-Reference Map

| Symptom / code family | Primary repo file |
|---|---|
| OBD basics, modes, freeze frame, readiness | `diagnostics/OBD2_GUIDE.md` |
| No crank | `diagnostics/NO_CRANK.md` |
| Crank / no start | `diagnostics/CRANK_NO_START.md` |
| Misfire | `diagnostics/MISFIRE.md` |
| Fuel trims | `diagnostics/FUEL_TRIM_DIAGNOSTICS.md` |
| Overheating | `diagnostics/OVERHEATING.md` |
| Charging / low voltage | `diagnostics/CHARGING_SYSTEM.md` |
| Battery / starter / alternator | `electrical/BATTERY_STARTER_ALTERNATOR.md` |
| Wiring / connectors | `electrical/WIRING_AND_CONNECTOR_DIAGNOSTICS.md` |
| Grounds | `electrical/GROUND_POINTS.md` |
| CAN / U-codes / communication | `electrical/CAN_NETWORK_DIAGNOSTICS.md` |
| Fuses / relays | `specs/FUSES_AND_RELAYS.md` |
| Timing / CVVT | `engine/TIMING_CVVT.md` |
| Lubrication | `engine/LUBRICATION_SYSTEM.md` |
| Ignition | `engine/IGNITION.md` |
| GDI fuel | `engine/GDI_FUEL_SYSTEM.md` |
| Cooling | `engine/COOLING_SYSTEM.md` |
| PCV | `engine/PCV_CRANKCASE_VENTILATION.md` |
| EVAP | `engine/EVAP_PURGE_SYSTEM.md` |
| Air / throttle / MAP / IAT | `engine/AIR_INTAKE_THROTTLE_MAP.md` |
| Catalyst / oxygen sensors | `engine/EXHAUST_CATALYST_O2_SENSORS.md` |
| Compression / leak-down | `engine/COMPRESSION_LEAKDOWN_MECHANICAL_HEALTH.md` |
| Valve clearance | `engine/VALVE_CLEARANCE_VALVETRAIN.md` |
| Head gasket / cylinder head | `engine/CYLINDER_HEAD_HEAD_GASKET.md` |
| Pistons / rings / bearings | `engine/PISTONS_RINGS_CYLINDERS_BOTTOM_END.md` |
| 6-speed automatic | `transmission/SIX_SPEED_AUTOMATIC.md` |
| Brakes / ABS / ESC | `brakes/BRAKE_SYSTEM.md` |
| Steering / suspension | `suspension-steering/STEERING_SUSPENSION.md` |
| Tires / TPMS | `tires-wheels/TIRES_WHEELS.md` |
| Roadside triage | `guides/ROADSIDE_DIAGNOSTIC_TRIAGE.md` |

---

# 18. AI / RAG Rules

An AI using this repository must obey these rules.

## Rule 1

Never translate:

```text
DTC NAME → REPLACE NAMED COMPONENT
```

Instead:

```text
DTC → DETECTED CONDITION → POSSIBLE CAUSES → TESTS → ROOT CAUSE
```

## Rule 2

Always preserve the reporting module.

Bad:

```text
C1616
```

Better:

```text
ABS/ESC reports C1616 CAN Bus Off
```

## Rule 3

If many unrelated codes appear together, check battery / charging / grounds before diagnosing each one independently.

## Rule 4

Distinguish:

- circuit faults
- performance faults
- rationality faults
- mechanical faults
- communication faults

## Rule 5

Do not erase codes before recording freeze frame and status.

## Rule 6

A TSB is evidence of a known service pattern, not proof that the individual vehicle has that failure.

## Rule 7

Exact 2014 Hyundai data outranks adjacent-year data.

## Rule 8

Same-generation service data must stay labeled as supporting data when the exact 2014 source has not been recovered.

## Rule 9

Unknown is preferable to a confident wrong answer.

---

# 19. Diagnostic Record Template

```yaml
scan_event:
  date:
  mileage:
  engine_state: "KOEO | idle | driving | hot restart | cold start"
  ambient_temp:
  battery_voltage_koeo:
  charging_voltage:

codes:
  - module:
    code:
    description:
    status: "pending | stored | current | permanent"
    mil_requested:

freeze_frame:
  rpm:
  vehicle_speed:
  coolant_temp:
  intake_temp:
  map:
  calculated_load:
  stft:
  ltft:
  throttle_command:
  throttle_actual:
  system_voltage:
  fuel_pressure:

symptoms:
  -

recent_events:
  battery_disconnect: false
  jump_start: false
  wiring_work: false
  underbody_impact: false
  deep_water: false
  refueled_recently: false

initial_classification:
  safety_critical: false
  low_voltage_suspected: false
  network_suspected: false
  electrical_circuit: false
  mechanical: false
  emissions: false

next_test:
result:
root_cause:
repair:
verification:
```

---

# 20. Fast Field Algorithm

```text
SCAN ALL MODULES
      ↓
SAVE EVERYTHING
      ↓
ANY RED-LIGHT CONDITION?
      ├─ YES → STOP / MAKE SAFE
      └─ NO
          ↓
VOLTAGE HEALTHY?
      ├─ NO → FIX POWER FIRST
      └─ YES
          ↓
NETWORK CODE STORM?
      ├─ YES → CAN / MODULE POWER-GROUND
      └─ NO
          ↓
CLASSIFY PRIMARY CODE
      ↓
CIRCUIT / PERFORMANCE / CORRELATION / COMMUNICATION
      ↓
OPEN CORRECT REPO GUIDE
      ↓
TEST
      ↓
REPAIR ROOT CAUSE
      ↓
VERIFY
      ↓
LOG RESULT
```

---

# 21. Primary External Sources

- SAE J2012 public historical copy:  
  https://ptacts.uspto.gov/ptacts/public-informations/petitions/1532543/download-documents?artifactId=LxtzK1g8Pp1TwzB8NAVFIyZd6qbjMbs9ZGsiPl3T-bZWf0_AFDk7DNg

- California OBD regulation referencing SAE-defined and manufacturer-defined DTC use:  
  https://www3.epa.gov/region9/CA-Air-SIP/California%20Code%20of%20Regulations/Title%2013%2C%20Division%203%2C%20Chapter%201%2C%20Article%202%2C%20Section%201971.1.pdf

- Same-generation Accent DTC / TSB library:  
  https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Technical%20Service%20Bulletins/

- Hyundai TSB 20-AT-014H, P0711 / P0712 / P0713, includes 2012–2017 Accent RB:  
  https://static.nhtsa.gov/odi/tsbs/2020/MC-10174799-0001.pdf

- Hyundai TSB 19-AT-024H, P0705 / P0706 / P0707 / P0708, includes 2012–2017 Accent RB:  
  https://static.nhtsa.gov/odi/tsbs/2019/MC-10169380-9999.pdf

- Hyundai TSB covering P0717 / P0721 / P0722, includes 2012–2017 Accent RB 1.6L:  
  https://static.nhtsa.gov/odi/tsbs/2020/MC-10173548-0001.pdf

---

## Final Rule

```text
THE CODE IS THE WITNESS.
THE TESTS BUILD THE CASE.
THE ROOT CAUSE GETS THE REPAIR.
```
