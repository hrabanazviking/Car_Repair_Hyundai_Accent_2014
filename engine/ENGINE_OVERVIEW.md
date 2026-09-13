# 2014 Hyundai Accent SE — Engine Overview

> **Purpose:** Canonical engine-system overview for a U.S.-market 2014 Hyundai Accent SE. This file maps the engine as an interacting system so that humans and offline AI assistants can reason across ignition, fuel, airflow, timing, lubrication, cooling, emissions, and diagnostics without treating each component in isolation.
>
> **Core rule:** Diagnose systems by relationships. A symptom in one subsystem can be caused by another subsystem upstream or downstream.

---

## 1. Scope

This document applies primarily to the U.S.-market 2014 Hyundai Accent SE five-door with the 1.6 L gasoline direct-injection engine.

Hyundai's official 2014 U.S. product information identifies the engine as the **1.6-liter Gamma GDI DOHC inline-four with Dual CVVT**.

The engine is commonly identified in Hyundai/Kia technical and vehicle data as **G4FD**. Because Hyundai's 2014 U.S. press material describes the engine by family and specification rather than printing the G4FD code explicitly, this repository records the engine code with a separate confidence label.

### Engine identity

| Attribute | Value | Confidence |
|---|---|---|
| Engine family | Gamma | VERIFIED — HYUNDAI |
| Displacement | 1.6 L / 1,591 cc class | VERIFIED — HYUNDAI / CORROBORATED |
| Configuration | Inline four-cylinder | VERIFIED — HYUNDAI |
| Cylinder head | DOHC, four valves per cylinder architecture | VERIFIED — HYUNDAI / SERVICE FAMILY |
| Fuel system | Gasoline Direct Injection (GDI) | VERIFIED — HYUNDAI |
| Variable valve timing | Dual CVVT, intake and exhaust | VERIFIED — HYUNDAI |
| Throttle | Electronic throttle control | VERIFIED — HYUNDAI |
| Cam drive | Roller timing chain | VERIFIED — HYUNDAI |
| Block construction | Aluminum | VERIFIED — HYUNDAI |
| Output | 138 hp @ 6,300 rpm | VERIFIED — HYUNDAI |
| Torque | 123 lb-ft @ 4,850 rpm | VERIFIED — HYUNDAI |
| Common engine code | G4FD | CORROBORATED — VEHICLE/SERVICE DATA |
| Firing order | 1-3-4-2 | CORROBORATED — ADJACENT-YEAR HYUNDAI SERVICE DATA |

### Primary Hyundai source

- Hyundai Newsroom, **"Hyundai Accent Keeps Building on a Proven Formula"**: https://www.hyundainews.com/releases/1756

### Corroborating technical sources

- Operation CHARM, 2013 Hyundai Accent L4-1.6L service information: https://charm.li/Hyundai/2013/Accent%20L4-1.6L/
- 2013 firing-order specification: https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Powertrain%20Management/Tune-up%20and%20Engine%20Performance%20Checks/Firing%20Order/Specifications/

---

# 2. High-Level Engine System Map

```text
                         DRIVER REQUEST
                               │
                               ▼
                    ELECTRONIC THROTTLE
                               │
                               ▼
AIR FILTER → INTAKE DUCT → THROTTLE BODY → INTAKE MANIFOLD
                                             │
                                             ├── MAP / IAT DATA
                                             ├── PCV FLOW
                                             └── EVAP PURGE FLOW
                                             │
                                             ▼
                                       CYLINDER AIR
                                             │
                                             ▼
LOW-PRESSURE FUEL → HIGH-PRESSURE PUMP → FUEL RAIL → GDI INJECTORS
                                             │
                                             ▼
                                      AIR + FUEL MIX
                                             │
                                             ▼
                                   COIL-ON-PLUG IGNITION
                                             │
                                             ▼
                                         COMBUSTION
                                             │
                         ┌───────────────────┼───────────────────┐
                         ▼                   ▼                   ▼
                      TORQUE             EXHAUST               HEAT
                         │                   │                   │
                         ▼                   ▼                   ▼
                    TRANSMISSION      O2/A-F SENSORS       COOLING SYSTEM
                                             │
                                             ▼
                                      CATALYTIC CONVERTER

ENGINE POSITION / CONTROL LOOP:

CRANK SENSOR ─┐
CAM SENSOR ───┼→ ECM/PCM → IGNITION TIMING
MAP / IAT ────┤          → INJECTOR CONTROL
ECT ──────────┤          → THROTTLE CONTROL
O2/A-F ───────┤          → CVVT CONTROL
KNOCK ────────┤          → FUEL TRIM
PEDAL ────────┘          → FAN / EVAP / LOAD MANAGEMENT
```

The ECM/PCM is the central coordinator, but it can only make good decisions from good inputs and usable mechanical hardware.

---

# 3. Mechanical Architecture

The Gamma 1.6 GDI is an aluminum inline-four engine with double overhead camshafts.

Key mechanical features include:

- Aluminum cylinder block
- Aluminum cylinder head
- Four-cylinder inline layout
- DOHC valvetrain
- Four-valve-per-cylinder architecture
- Intake and exhaust camshaft phasing
- Roller timing chain
- Hydraulic timing-chain tensioner
- Chain guides
- Offset crankshaft design
- Low-friction valvetrain coatings

Hyundai specifically promoted the Gamma engine's offset-crankshaft and friction-reduction measures as part of its efficiency strategy.

### Why this matters diagnostically

Mechanical condition sets the foundation for every electronic system.

A perfect spark, perfect injector pulse, and perfect sensor signal cannot compensate for:

- low compression
- incorrect cam timing
- burned valve
- damaged piston/ring condition
- timing-chain jump
- severe valve-clearance error

When electrical and fuel checks look correct but the engine still runs poorly or will not start, return to mechanical fundamentals.

---

# 4. Firing Order

Adjacent-year Hyundai Accent 1.6 L service information specifies:

```text
1 → 3 → 4 → 2
```

This repository treats that as strongly applicable to the same Gamma 1.6 GDI family used in the 2014 U.S. Accent.

## Important cylinder-numbering rule

Do not infer cylinder physical location from a generic inline-four diagram.

Before cylinder-specific mechanical work, confirm the exact numbering orientation from a Hyundai service diagram or physical engine identification reference.

The firing order and cylinder numbering are separate facts.

---

# 5. Timing Chain System

Hyundai uses a **roller timing chain**, not a scheduled timing belt, on this engine.

The timing system includes:

- crankshaft sprocket
- timing chain
- fixed guide
- tensioner arm
- hydraulic chain tensioner
- intake CVVT sprocket
- exhaust CVVT sprocket
- timing-chain cover

Adjacent-year Hyundai service information shows chain timing indexed between the crankshaft sprocket and both CVVT sprockets.

## What the timing chain does

The chain keeps the crankshaft and camshafts synchronized.

If mechanical timing shifts, symptoms can include:

- crank/no-start
- low compression
- rough running
- loss of power
- cam/crank correlation codes
- abnormal mechanical noise
- poor idle
- abnormal exhaust behavior

## Timing-chain diagnostic clues

Investigate mechanical timing when there is:

- sudden no-start with normal cranking speed
- cam/crank correlation DTCs
- abnormal chain rattle
- multiple-cylinder misfire with otherwise plausible ignition/fuel
- unexpectedly low compression across several cylinders
- evidence that cam timing no longer follows commanded CVVT behavior

Do not assume that "timing chain" means "lifetime part that can never fail."

It means the chain is not a routine scheduled-replacement item like a conventional timing belt.

Lubrication condition, tensioner function, guide wear, contamination, and mechanical damage still matter.

---

# 6. Dual CVVT

The engine uses **Dual Continuously Variable Valve Timing** on both intake and exhaust camshafts.

Hyundai states that this helps:

- improve volumetric efficiency
- reduce pumping losses
- improve fuel economy
- reduce hydrocarbon emissions
- improve performance

The ECM adjusts camshaft phase using oil-controlled actuators/valves and feedback from camshaft/crankshaft position sensors.

## CVVT depends on engine oil

Because CVVT uses engine oil hydraulically, poor oil condition can create valve-timing symptoms.

Possible contributing factors include:

- low oil level
- incorrect viscosity
- dirty/sludged oil
- restricted oil passage
- failed oil-control valve
- wiring fault
- failed cam position sensor
- mechanical phaser problem
- chain/timing problem

### Diagnostic lesson

A cam-timing DTC is not automatically a failed camshaft sensor.

```text
CAM TIMING CODE
      ↓
CHECK OIL LEVEL / CONDITION
      ↓
CHECK RELATED DTCs
      ↓
CHECK COMMAND VS. ACTUAL CAM DATA IF AVAILABLE
      ↓
CHECK OIL-CONTROL VALVE / WIRING
      ↓
CHECK CAM / CRANK SENSING
      ↓
CHECK MECHANICAL TIMING
```

---

# 7. Valve Clearance

The valvetrain uses measured mechanical clearance that Hyundai specifies for inspection at scheduled intervals.

Adjacent-year service data for the same 1.6 L engine family lists cold inspection at about 20°C / 68°F.

The 2014 maintenance schedule in this repository calls for valve-clearance inspection at **60,000 miles / 72 months**.

See:

- `../maintenance/MAINTENANCE_SCHEDULE.md`

## Why valve clearance matters

Too little clearance can contribute to:

- valve not fully seating
- low compression
- hot-running valve
- burned valve over time
- hot misfire

Too much clearance can contribute to:

- valvetrain noise
- altered valve lift/duration behavior
- accelerated wear

Do not adjust clearance from generic numbers. Use verified service specifications and procedure.

---

# 8. Gasoline Direct Injection (GDI)

The engine uses direct fuel injection into the combustion chamber.

This differs fundamentally from older port-injection systems.

The fuel system has two pressure stages:

```text
FUEL TANK
   ↓
LOW-PRESSURE ELECTRIC PUMP
   ↓
SUPPLY LINE
   ↓
ENGINE-DRIVEN HIGH-PRESSURE PUMP
   ↓
HIGH-PRESSURE RAIL
   ↓
GDI INJECTORS
   ↓
COMBUSTION CHAMBERS
```

## Why Hyundai used GDI

Hyundai states that direct injection improves control of fuel delivery and contributes to:

- power
- fuel economy
- emissions performance

## GDI safety

The high-pressure side is hazardous.

Never:

- loosen a high-pressure line to see whether fuel is present
- search for a pressurized leak with fingers
- crack an injector fitting while cranking
- treat the high-pressure rail like an old carbureted fuel line

High-pressure gasoline can penetrate skin.

Use proper depressurization procedures before opening the high-pressure system.

See:

- `../diagnostics/CRANK_NO_START.md`
- future `GDI_FUEL_SYSTEM.md`

---

# 9. Low-Pressure Fuel Supply

The in-tank electric pump supplies fuel to the engine-driven high-pressure pump.

Relevant engine-bay electrical circuits already documented in this repository include:

- `F/PUMP` 15A
- fuel-pump relay
- ECU feeds
- injector circuit

See:

- `../specs/FUSES_AND_RELAYS.md`

## Diagnostic distinction

A no-start can result from failure on either side:

```text
LOW-PRESSURE FAILURE
→ high-pressure pump may be starved

HIGH-PRESSURE FAILURE
→ low-pressure pump may still run normally
```

Do not conclude that audible pump operation proves correct rail pressure.

---

# 10. High-Pressure Fuel Pump

The mechanical high-pressure pump is driven by the engine and raises fuel pressure for direct injection.

Its performance depends on:

- adequate low-pressure fuel supply
- mechanical drive
- control valve operation where applicable
- electrical control
- rail-pressure sensing
- correct ECM command

Possible symptoms of high-pressure fuel-system problems include:

- extended crank
- crank/no-start
- hesitation under load
- lean operation
- loss of power
- fuel-pressure DTCs
- unstable rail pressure

Exact pressure specifications must come from verified Hyundai service information before being used as pass/fail values.

---

# 11. Injectors

Each cylinder has a dedicated GDI injector.

Injector faults may include:

- electrical open/short
- connector fault
- restricted flow
- leaking injector
- poor spray pattern
- mechanical sticking
- contamination

### Single-cylinder misfire logic

A cylinder-specific injector fault may produce:

- one-cylinder misfire
- unusual plug appearance
- local fuel-trim behavior that is difficult to see globally
- rough idle
- hard starting

Do not condemn an injector before checking ignition and mechanical condition.

See:

- `../diagnostics/MISFIRE.md`

---

# 12. Ignition System

The engine uses **coil-on-plug ignition**.

Each cylinder has its own ignition coil mounted directly over the spark plug.

Relevant electrical protection includes the engine-bay `IGN COIL` fuse documented elsewhere in the repository.

## Advantages of coil-on-plug

- no distributor
- no conventional spark-plug wires
- individual-cylinder ignition control
- easier cylinder-to-cylinder diagnostic comparison

## Common ignition diagnostic methods

- scan misfire counters/codes
- inspect coil connector
- inspect plug
- swap one coil to another cylinder
- observe whether the misfire follows

A coil swap is powerful because it turns a suspect component into a controlled experiment.

See:

- `../diagnostics/MISFIRE.md`

---

# 13. Spark Plugs

The 2014 maintenance documentation specifies iridium-type plugs, with a source conflict in published Hyundai materials regarding replacement mileage.

This repository conservatively uses the lower verified interval while documenting the conflict.

See:

- `../maintenance/MAINTENANCE_SCHEDULE.md`

Spark-plug condition can reveal evidence of:

- oil consumption
- rich mixture
- lean/hot operation
- coolant contamination
- weak ignition
- cylinder-specific fuel problem

Do not diagnose an engine from plug color alone.

---

# 14. Airflow Measurement — MAP/IAT Speed-Density Strategy

This engine uses a **Manifold Absolute Pressure (MAP)** sensor strategy together with intake-air-temperature data rather than relying on a conventional hot-wire MAF sensor as the primary airflow meter.

That means the ECM estimates air mass from values including:

- manifold pressure
- intake-air temperature
- engine speed
- throttle position
- engine volumetric behavior

### Important repository rule

Generic advice to "clean the MAF" does not belong at the top of the diagnostic tree for this Accent.

Instead examine:

- MAP plausibility
- IAT plausibility
- throttle position
- intake leaks
- PCV flow
- EVAP purge flow
- engine mechanical condition

See:

- `../diagnostics/FUEL_TRIM_DIAGNOSTICS.md`

---

# 15. Electronic Throttle Control

Hyundai uses an electronically controlled throttle body.

The accelerator pedal is an electronic input rather than a direct mechanical cable pulling the throttle plate.

The system includes concepts such as:

- accelerator-pedal position sensing
- throttle-position sensing
- throttle actuator motor
- ECM torque control

The ECM can coordinate throttle behavior with:

- transmission operation
- traction/stability control
- idle control
- air-conditioning load
- engine protection

## Possible symptoms of throttle-system problems

- limited throttle response
- limp/fail-safe behavior
- unstable idle
- throttle-related DTCs
- reduced engine power

Do not manually force an electronic throttle plate unless the service procedure allows it.

---

# 16. Intake Manifold / Variable Induction

Hyundai's 2014 product information identifies a **variable induction system** as part of the Gamma engine's efficiency strategy.

The intake system can therefore affect performance through more than a simple open tube.

Possible intake-related problems include:

- vacuum leak
- damaged intake duct
- loose clamp
- manifold leak
- variable-intake actuator/solenoid problem
- PCV leak
- purge-flow fault

These problems may interact strongly with fuel trims.

---

# 17. PCV System

The Positive Crankcase Ventilation system routes crankcase vapors back into the intake for combustion.

The PCV system influences:

- crankcase pressure
- oil-vapor handling
- idle airflow
- fuel trims

A stuck-open or leaking PCV path can act like an intake leak.

Possible clues include:

- lean fuel trims at idle
- rough idle
- whistling
- abnormal crankcase vacuum
- oil-consumption changes

Do not block the PCV system as a permanent repair.

---

# 18. EVAP Purge System

The evaporative-emissions system stores fuel vapors and meters them into the engine through a purge valve.

A purge valve that flows when it should not can introduce additional fuel vapor/air into the intake.

Possible symptoms include:

- hard start after refueling
- rough idle
- rich or lean trim disturbance depending on conditions
- EVAP DTCs

The `SENSOR` engine-bay fuse protects multiple engine-control devices including purge-related circuitry according to the 2014 fuse documentation.

See:

- `../specs/FUSES_AND_RELAYS.md`
- `../diagnostics/FUEL_TRIM_DIAGNOSTICS.md`

---

# 19. Crankshaft Position Sensor

The crankshaft-position signal is fundamental to:

- engine-speed calculation
- spark timing
- injector synchronization
- misfire monitoring

During crank/no-start diagnosis, OBD cranking RPM is a useful first clue.

```text
ENGINE PHYSICALLY CRANKING
+ OBD RPM = 0
      ↓
INVESTIGATE CRANK SIGNAL / CIRCUIT / ECU POWER
```

However, visible RPM does not prove the waveform is perfect.

See:

- `../diagnostics/CRANK_NO_START.md`

---

# 20. Camshaft Position Sensors

Camshaft-position information allows the ECM to determine engine phase and coordinate:

- injection timing
- ignition strategy
- CVVT control
- cam/crank correlation

Possible cam-signal symptoms include:

- extended crank
- no-start
- rough running
- correlation DTCs
- CVVT-related faults

A cam sensor code can also result from incorrect mechanical timing.

Always consider both electrical and mechanical causes.

---

# 21. MAP and Intake-Air-Temperature Sensors

MAP provides manifold-pressure information.

IAT provides intake-air-temperature information.

Together with RPM and other inputs they help the ECM estimate incoming air mass.

## Plausibility checks

Key-on engine-off MAP should broadly resemble local atmospheric pressure after accounting for altitude and sensor/scanner units.

Cold-soaked IAT should broadly resemble ambient air temperature.

A wildly implausible sensor value can cause fueling errors even without an obvious circuit failure.

See:

- `../diagnostics/FUEL_TRIM_DIAGNOSTICS.md`

---

# 22. Engine Coolant Temperature Sensor

ECT strongly affects:

- cold-start enrichment
- warm-up strategy
- fan control
- fueling
- ignition strategy
- readiness-monitor behavior

A false ECT reading can mimic a fuel or starting problem.

Examples:

```text
COLD ENGINE
ECT SCANNER VALUE = VERY HOT
→ possible sensor/circuit bias

HOT ENGINE
ECT SCANNER VALUE = EXTREMELY COLD
→ possible sensor/circuit bias
```

Compare ECT to ambient temperature after an overnight cold soak.

See:

- `../diagnostics/OVERHEATING.md`

---

# 23. Knock Sensor

The knock sensor allows the ECM to detect combustion knock and adjust ignition timing.

Knock-related behavior can be influenced by:

- fuel quality
- engine temperature
- carbon deposits
- mechanical noise
- sensor/circuit problems

Do not interpret a knock-related code as proof that the engine itself is physically knocking apart.

Likewise, a mechanical engine noise should not be dismissed simply because there is no knock-sensor code.

---

# 24. Oxygen / Air-Fuel Feedback

The exhaust system uses oxygen/air-fuel feedback so the ECM can correct mixture and monitor catalyst performance.

These sensors influence:

- closed-loop fuel control
- STFT
- LTFT
- catalyst monitoring

A sensor can report a lean exhaust because the engine truly is lean, but also because:

- an exhaust leak adds oxygen
- a misfire sends oxygen downstream
- the sensor is biased

Therefore:

```text
LEAN SENSOR READING
      ≠
AUTOMATICALLY BAD O2 SENSOR
```

See:

- `../diagnostics/FUEL_TRIM_DIAGNOSTICS.md`
- `../diagnostics/MISFIRE.md`

---

# 25. Lubrication System

Engine oil performs several jobs simultaneously:

- bearing lubrication
- piston/ring lubrication
- valvetrain lubrication
- timing-chain lubrication
- hydraulic timing-chain tensioner supply
- CVVT hydraulic control
- heat removal
- contamination suspension

This is why low or degraded oil can produce symptoms far beyond simple bearing wear.

Possible oil-related secondary symptoms include:

- CVVT faults
- chain/tensioner noise
- abnormal valvetrain noise
- oil-pressure warning

See:

- `../specs/FLUIDS_AND_CAPACITIES.md`
- `../maintenance/MAINTENANCE_SCHEDULE.md`

## Oil-pressure warning

If the oil-pressure warning remains illuminated while the engine is running, shut the engine down and investigate.

Do not continue driving merely because the dipstick shows oil present.

Oil level and oil pressure are different things.

---

# 26. Cooling System

The cooling system manages combustion and friction heat using:

- coolant
- engine coolant passages
- water pump
- thermostat
- radiator
- electric cooling fan
- reservoir
- hoses
- heater core
- ECT sensing

Adjacent-year Hyundai service information lists a system capacity around **5.3 L**, but Hyundai source material contains an inconsistent US-quart conversion. This repository preserves that source conflict instead of silently correcting it.

See:

- `../specs/FLUIDS_AND_CAPACITIES.md`
- `../diagnostics/OVERHEATING.md`

## Diagnostic patterns

```text
OVERHEATS AT IDLE
BUT IMPROVES WITH ROAD SPEED
→ airflow / cooling-fan branch

OVERHEATS UNDER LOAD / HIGHWAY
→ flow / coolant / thermostat / radiator / pump branch

HEATER TURNS COLD WHILE ECT RISES
→ low coolant / air / circulation branch
```

---

# 27. Catalytic Converter and Misfire Risk

The catalytic converter depends on correct combustion upstream.

A severe misfire can send unburned fuel into the catalyst and overheat it.

Hyundai warns against continued driving with a known misfire because catalyst damage can result.

See:

- `../diagnostics/MISFIRE.md`

A flashing MIL should therefore be treated as an urgent drivability condition rather than ignored until convenient.

---

# 28. Engine Electrical Power Feeds

Important engine-related fuses documented for the 2014 Accent include:

| Fuse | Rating | General function |
|---|---:|---|
| ECU 1 | 30A | Main ECU/engine-control feed |
| ECU 2 | 10A | ECM/PCM feed |
| F/PUMP | 15A | Fuel-pump circuit |
| INJECTOR | 15A | Injector / engine-control circuit |
| SENSOR | 10A | Engine-control sensors/actuators |
| IGN COIL | 15A | Ignition coils |
| C/FAN | 40A | Cooling fan circuit |

See:

- `../specs/FUSES_AND_RELAYS.md`

## Diagnostic implication

A single lost common power feed can create several simultaneous symptoms.

Example:

```text
NO SPARK ON ALL CYLINDERS
+ NO INJECTOR ACTIVITY
+ MULTIPLE SENSOR CODES
        ↓
CHECK COMMON POWER / GROUND / ECU FEEDS
BEFORE REPLACING MULTIPLE COMPONENTS
```

---

# 29. Common Symptom-to-System Map

| Symptom | High-value systems to investigate first |
|---|---|
| No crank | Battery, cables/grounds, starter, range switch, start relay, fuses |
| Cranks but will not start | Crank/cam signal, spark, low/high fuel pressure, injectors, compression/timing |
| One-cylinder misfire | Coil, plug, injector, compression, wiring |
| Multiple-cylinder misfire | Fuel delivery, intake leak, shared ignition/power, timing, low voltage |
| Lean at idle, improves at 2500 rpm | Intake/PCV/purge leak |
| Lean at idle and cruise | Fuel delivery, injector flow, sensor bias, exhaust leak |
| Poor hot restart | Fuel pressure, injector leakage, purge, sensor heat failure |
| Extended cold crank | Fuel pressure, ECT plausibility, ignition, injector behavior |
| Rattle on startup | Oil level/pressure, timing-chain tensioner/chain, mechanical inspection |
| Cam correlation codes | Oil/CVVT, sensors/wiring, mechanical timing |
| Overheats at idle | Fan/airflow branch |
| Overheats under sustained load | Coolant flow/thermostat/radiator/pump branch |
| Battery/steering/code storm | Charging system / low voltage |

---

# 30. Engine Diagnostic Hierarchy

Use this order when a symptom is broad or confusing:

```text
1. SAFETY
   ↓
2. BATTERY / SYSTEM VOLTAGE
   ↓
3. DTCs + FREEZE FRAME
   ↓
4. BASIC MECHANICAL CONDITION
   ↓
5. AIR
   ↓
6. FUEL
   ↓
7. IGNITION
   ↓
8. TIMING / SYNCHRONIZATION
   ↓
9. CONTROL / SENSOR PLAUSIBILITY
   ↓
10. VERIFY REPAIR
```

The exact sequence changes by symptom, but this prevents random part replacement.

---

# 31. Maintenance Relationships

The engine's subsystems interact strongly with maintenance.

| Maintenance item | Systems affected |
|---|---|
| Engine oil | bearings, chain, tensioner, CVVT, valvetrain |
| Air filter | airflow, MAP behavior, engine load |
| Spark plugs | ignition, misfire, catalyst protection |
| Coolant | temperature control, knock resistance, durability |
| Valve clearance | compression, idle, hot running |
| Drive belt | alternator, water-pump/accessory operation depending on configuration |
| Battery condition | cranking speed, module voltage, sensor plausibility |

See:

- `../maintenance/MAINTENANCE_SCHEDULE.md`

---

# 32. Primitive-Road / Nomad Considerations

For an Accent used for extended travel and primitive camping, engine stress may come less from mileage itself and more from environment.

Watch closely for:

- dust-loaded engine air filter
- damaged lower splash shielding
- underbody impacts
- radiator/condenser debris
- mud blocking airflow
- wiring/connector damage from debris
- long idling periods
- repeated short trips
- steep mountain climbs
- high ambient heat
- winter salt exposure

After severe rough-road travel, inspect the engine bay and underbody before assuming a new sound is "normal."

See:

- `../maintenance/PRE_TRIP_INSPECTION.md`

---

# 33. Engine Safety Rules

Never:

- open a hot pressurized cooling system
- loosen GDI high-pressure lines casually
- work beneath a car supported only by a jack
- substitute a larger fuse
- place hands near belts/fans on a running engine
- disconnect ignition coils by hand while using unsafe spark-testing methods
- ignore an oil-pressure warning
- continue driving a severe misfire

Electric cooling fans may start unexpectedly when commanded.

Keep hands, hair, clothing, and tools clear of rotating components.

---

# 34. AI Reasoning Rules for Engine Questions

An AI using this repository should:

1. Identify the symptom before naming a component.
2. Separate no-crank from crank/no-start.
3. Separate one-cylinder faults from shared-system faults.
4. Check system voltage early when many unrelated codes appear.
5. Use fuel trims as evidence, not as a verdict.
6. Treat GDI high-pressure work as hazardous.
7. Distinguish sensor reading from physical reality.
8. Consider mechanical timing when cam/crank correlation is abnormal.
9. Avoid telling the user to clean a MAF as the default airflow repair on this MAP-based engine.
10. Never invent an exact pressure, torque, clearance, or sensor value if the repository does not contain a verified specification.
11. Prefer a test that discriminates between two causes before recommending a part.
12. After repair, verify symptoms, codes, live data, and leaks.

---

# 35. Machine-Readable Engine Summary

```yaml
vehicle:
  year: 2014
  make: Hyundai
  model: Accent
  trim: SE
  market: US

engine:
  family: Gamma
  common_code: G4FD
  common_code_confidence: corroborated
  displacement_l: 1.6
  cylinders: 4
  arrangement: inline
  block_material: aluminum
  head: DOHC
  fuel_system: gasoline_direct_injection
  throttle: electronic
  valve_timing: dual_cvvt
  cam_drive: roller_timing_chain
  horsepower:
    value: 138
    rpm: 6300
  torque_lb_ft:
    value: 123
    rpm: 4850
  firing_order:
    value: "1-3-4-2"
    confidence: adjacent_year_service_family

air_metering:
  primary_strategy: speed_density
  map_sensor: true
  iat_sensor: true
  conventional_primary_maf: false

ignition:
  type: coil_on_plug
  cylinders: 4

fuel:
  stages:
    - low_pressure_in_tank_pump
    - engine_driven_high_pressure_pump
    - high_pressure_rail
    - gdi_injectors
  high_pressure_hazard: true

timing:
  chain: true
  intake_cvvt: true
  exhaust_cvvt: true
  hydraulic_tensioner: true

major_inputs:
  - crankshaft_position
  - camshaft_position
  - map
  - intake_air_temperature
  - engine_coolant_temperature
  - oxygen_air_fuel_feedback
  - throttle_position
  - accelerator_pedal_position
  - knock

major_outputs:
  - ignition_coils
  - injectors
  - electronic_throttle
  - cvvt_oil_control
  - purge_control
  - fuel_pump_control
  - cooling_fan_control

engine_fuses:
  ECU_1_A: 30
  ECU_2_A: 10
  F_PUMP_A: 15
  INJECTOR_A: 15
  SENSOR_A: 10
  IGN_COIL_A: 15
  C_FAN_A: 40

related_docs:
  - ../diagnostics/NO_CRANK.md
  - ../diagnostics/CRANK_NO_START.md
  - ../diagnostics/MISFIRE.md
  - ../diagnostics/OVERHEATING.md
  - ../diagnostics/CHARGING_SYSTEM.md
  - ../diagnostics/FUEL_TRIM_DIAGNOSTICS.md
  - ../electrical/BATTERY_STARTER_ALTERNATOR.md
  - ../specs/FLUIDS_AND_CAPACITIES.md
  - ../specs/FUSES_AND_RELAYS.md
  - ../maintenance/MAINTENANCE_SCHEDULE.md
```

---

# 36. Source Confidence Notes

### VERIFIED — HYUNDAI

The following are directly supported by Hyundai's official 2014 Accent U.S. material:

- Gamma engine family
- 1.6 L inline-four
- all-aluminum construction
- GDI
- Dual CVVT
- electronic throttle
- variable induction system
- offset crankshaft
- roller timing chain
- 138 hp @ 6,300 rpm
- 123 lb-ft @ 4,850 rpm

### CORROBORATED — ADJACENT-YEAR SERVICE FAMILY

The following are supported by 2013 Accent 1.6 L Hyundai service information and are highly relevant to the same engine family:

- firing order 1-3-4-2
- timing-chain architecture
- hydraulic chain tensioner
- intake/exhaust CVVT timing relationship
- valve-clearance service architecture
- cooling-system bleeding architecture

### CORROBORATED — ENGINE CODE

`G4FD` is strongly associated with the 2011–2014 Accent 1.6 GDI family in vehicle, parts, and technical data, but should still be confirmed against the exact vehicle/VIN before ordering code-specific internal engine parts.

---

# 37. Document Status

- **Vehicle:** 2014 Hyundai Accent SE
- **System:** Engine overview
- **Status:** Initial canonical engine map
- **Primary source:** Hyundai 2014 U.S. product information
- **Supporting sources:** Adjacent-year Hyundai service data and corroborated engine-code records
- **Purpose:** Human field reference + offline AI/RAG engine reasoning

---

# 38. Core Philosophy

```text
ENGINE SYMPTOM
     ↓
WHAT SYSTEM MUST BE WORKING FOR THIS SYMPTOM TO OCCUR?
     ↓
WHAT SHARED INPUTS / OUTPUTS CONNECT THOSE SYSTEMS?
     ↓
WHAT TEST MOST CLEANLY SEPARATES THE LIKELY CAUSES?
     ↓
TEST
     ↓
REPAIR ROOT CAUSE
     ↓
VERIFY THE WHOLE SYSTEM
```

The engine is not a bag of parts.

It is a network of mechanical, electrical, hydraulic, thermal, and combustion systems that continuously influence one another.
