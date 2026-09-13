---
title: "2014 Hyundai Accent SE — Vehicle Baseline"
vehicle_make: Hyundai
vehicle_model: Accent
model_year: 2014
market: United States
trim: SE
body_style: five-door hatchback
generation: RB
engine_family: Gamma 1.6 GDI
engine_code: G4FD
transmission: six-speed automatic
transmission_control: SHIFTRONIC
layout: front-engine, front-wheel-drive
status: living_reference
last_reviewed: 2026-09-13
---

# 2014 Hyundai Accent SE — Vehicle Baseline

> **Purpose:** Canonical identity and architecture file for this repository.
>
> Other repair documents should reference this file for basic vehicle identity rather than repeatedly inventing or re-deriving specifications.
>
> **Accuracy rule:** This document distinguishes factory-confirmed 2014 U.S.-market information from owner-specific configuration and secondary-source identifiers.

---

# 1. Target Vehicle

This repository is centered on a:

| Field | Value | Confidence |
|---|---|---|
| Make | Hyundai | **VERIFIED — HYUNDAI** |
| Model | Accent | **VERIFIED — HYUNDAI** |
| Model year | 2014 | **VERIFIED — OWNER / REPOSITORY SCOPE** |
| Market | United States | **VERIFIED — OWNER / REPOSITORY SCOPE** |
| Trim | SE | **VERIFIED — OWNER / REPOSITORY SCOPE** |
| Body | Five-door hatchback | **VERIFIED — HYUNDAI + OWNER** |
| Transmission | Six-speed automatic | **VERIFIED — OWNER; factory configuration supported by Hyundai** |
| Drivetrain | Front-wheel drive | **VEHICLE ARCHITECTURE** |
| Engine | 1.6 L Gamma GDI inline-four | **VERIFIED — HYUNDAI** |
| Engine code | G4FD | **VERIFIED — PARTS-CATALOG EVIDENCE; confirm against vehicle/build data when needed** |

The 2014 U.S. Accent lineup consisted of the four-door GLS, five-door GS, and five-door SE. Hyundai describes the SE as the sporty five-door trim.

Primary Hyundai source:

- Hyundai Newsroom — *Hyundai Accent Keeps Building on a Proven Formula* (2014 model information):
  https://www.hyundainews.com/releases/1756

---

# 2. Vehicle-Specific Identification Record

Fill this section from the physical vehicle before ordering expensive or configuration-sensitive parts.

```text
VIN: ______________________________________________

Build date: ________________________________________

Current odometer: __________________________________

Exterior color/code: _______________________________

Interior trim/code: _________________________________

Engine number: _____________________________________

Transmission identification: ________________________

Tire brand/model currently installed: ______________

Tire size currently installed: ______________________

Battery brand/model/date: ___________________________
```

## Why the VIN matters

Within a single model year there can be:

- production-date changes
- supplier changes
- revised part numbers
- superseded components
- market-specific equipment
- transmission differences
- option-package differences

For parts ordering, use the VIN whenever possible instead of relying only on `2014 Hyundai Accent`.

---

# 3. Engine Baseline

## Factory-confirmed engine architecture

Hyundai identifies the 2014 U.S. Accent engine as an all-aluminum **1.6-liter Gamma four-cylinder** with Gasoline Direct Injection.

| Specification | Factory information |
|---|---:|
| Configuration | Inline 4-cylinder |
| Displacement class | 1.6 L |
| Fuel delivery | Gasoline Direct Injection (GDI) |
| Cylinder head | DOHC |
| Valve timing | Dual Continuously Variable Valve Timing (D-CVVT) |
| Rated horsepower | 138 hp @ 6,300 rpm |
| Rated torque | 123 lb-ft @ 4,850 rpm |
| Throttle | Electronic throttle control |
| Cam drive | Roller timing chain |
| Block construction | Aluminum |
| Induction | Naturally aspirated |

Hyundai also lists:

- variable induction system
- offset crankshaft design
- Alternator Management System
- anti-friction coatings
- hydraulic engine mounts

### Timing drive

This engine uses a **timing chain**, not a normal scheduled-replacement timing belt.

That does **not** mean the timing system can never wear or fail. Chain stretch, tensioner, guide, oil-pressure, cam-phaser, or correlation faults still require diagnosis if symptoms or DTCs appear.

---

# 4. Engine Code: G4FD

The U.S.-market 1.6 L Gamma GDI engine used in this generation is identified in Hyundai parts-catalog data as **G4FD**.

Evidence example:

- A 2014 HMA-market Accent parts-catalog record lists an engine number beginning `G4FD`.

Secondary catalog reference:

- PartSouq Hyundai catalog example:
  https://ftp.gforceparts.com/en/catalog/genuine/vehicle?c=Hyundai&q=KMHCT4AE7EU690122

## Important

Do not use engine code alone to order every component. Production date and VIN can still affect fitment.

Recommended notation throughout this repository:

```text
Engine family: Hyundai/Kia Gamma
Engine: 1.6 L GDI DOHC I4
Common engine code: G4FD
```

---

# 5. Fuel-System Architecture

The engine uses **Gasoline Direct Injection**.

A GDI system has both low-pressure fuel delivery and a mechanically driven high-pressure side supplying the fuel rail/injectors.

## Safety consequence

High-pressure GDI plumbing must never be treated like an old low-pressure port-injection system.

Do **not**:

- loosen a high-pressure pipe to check whether fuel exists
- search for a high-pressure leak with fingers
- reuse a component when the applicable service procedure specifies replacement
- open the system without verified depressurization procedures

Detailed fuel-pressure values and service procedures belong in:

`engine/GDI_FUEL_SYSTEM.md`

---

# 6. Transmission Baseline

Hyundai offered both six-speed manual and six-speed automatic transaxles in the 2014 Accent.

This repository's target car uses the **six-speed automatic**.

Factory-described automatic features include:

- six forward speeds
- SHIFTRONIC manual-selection capability
- Active ECO system
- Hillstart Assist Control

## Transmission identity caution

Do not assume a transmission-fluid specification, fill procedure, fluid temperature, or internal transmission code solely from generic internet listings.

These values must be verified before service and will live in dedicated files.

```text
Transmission type: 6-speed automatic transaxle
Exact transmission code: TO BE VIN/BUILD VERIFIED
Fluid specification: TO BE SOURCE VERIFIED
Fluid level procedure: TO BE SOURCE VERIFIED
```

---

# 7. Drivetrain Layout

```text
ENGINE
  ↓
6-SPEED TRANSAXLE
  ↓
FRONT DIFFERENTIAL
  ↓
LEFT + RIGHT FRONT HALF-SHAFTS
  ↓
FRONT WHEELS
```

Architecture:

- transverse front-mounted engine
- front-wheel drive
- front half-shafts/CV joints
- no rear drive shaft
- no rear differential

For noise diagnosis, remember that wheel bearings, CV joints, tires, brakes, engine/transmission mounts, and transaxle components can imitate one another.

---

# 8. Steering

Hyundai specifies **column-mounted Motor Driven Power Steering (MDPS)**.

The SE receives a sportier steering calibration than other Accent trims.

| Item | Baseline |
|---|---|
| Assist type | Electric / motor-driven power steering |
| Assist location | Column mounted |
| Hydraulic power-steering fluid | **None for the MDPS assist system** |
| SE calibration | Sport-tuned |
| Published turning diameter | 34.1 ft |

## Diagnostic consequence

There is no conventional hydraulic steering pump/reservoir to top off.

Loss of steering assist should trigger checks of:

- system voltage
- charging system
- related fuses
- connectors and grounds
- MDPS diagnostic codes
- mechanical steering condition

before expensive steering components are replaced.

---

# 9. Suspension Architecture

Hyundai describes the 2014 Accent suspension as:

## Front

- MacPherson strut
- coil spring
- twin-tube gas shock/strut damping

## Rear

- torsion axle
- coil springs
- monotube shock absorbers

Simplified layout:

```text
FRONT
MacPherson strut suspension
        │
  driven front wheels

REAR
torsion-beam / torsion-axle layout
        │
   non-driven rear wheels
```

This architecture matters for diagnosing:

- clunks
- wandering
- uneven tire wear
- wheel-bearing noise
- strut/shock leakage
- bushing wear
- alignment problems

Exact alignment values belong in a later source-verified specification file.

---

# 10. Wheels and Tires — SE Factory Configuration

Hyundai lists the following as standard on the 2014 five-door SE:

| Item | Factory configuration |
|---|---|
| Wheel | 16-inch alloy |
| Tire size | **195/50R16** |
| Tire-pressure monitoring | TPMS |

## Tire-pressure warning

**Tire size is not tire pressure.**

The correct cold inflation pressure for the individual vehicle should be taken from the driver's-door certification/tire placard, not from the tire sidewall maximum.

A dedicated tire file should record:

- door-placard pressure
- spare-tire specification
- wheel torque
- compatible tire sizes
- load limits
- rotation pattern

---

# 11. Brake-System Baseline

Hyundai lists the SE with **rear disc brakes**, distinguishing it from configurations that used rear drums.

Standard safety/braking systems include:

- Anti-lock Braking System (ABS)
- Electronic Brake-force Distribution (EBD)
- Brake Assist
- Electronic Stability Control (ESC)
- Traction Control System (TCS)
- Vehicle Stability Management (VSM)

Repository target:

```text
Front brakes: disc
Rear brakes: disc on SE
ABS: yes
EBD: yes
Brake Assist: yes
ESC/TCS: yes
```

Exact rotor thickness, discard limits, pad limits, caliper torque values, and brake-fluid specification must be verified separately before repair.

---

# 12. Body and Dimensions

Factory-published 2014 five-door information:

| Measurement | Value |
|---|---:|
| Wheelbase | **101.2 in** |
| Five-door overall length | **162 in** |
| Cargo volume, rear seats up | **21.2 cu ft** |
| Aerodynamic drag coefficient | **0.30 Cd** |
| Published turning diameter | **34.1 ft** |

The rear seat uses a 60/40 split-folding design.

## Nomad-build caution

Removing seats, adding a sleeping platform, carrying tools, batteries, water, camping equipment, or other cargo changes real-world vehicle mass and axle loading.

Do not use cargo volume as a substitute for payload capacity.

Vehicle loading should eventually be documented from:

- driver's-door certification label
- GVWR
- front GAWR
- rear GAWR
- actual scale weights when loaded

Suggested future file:

`specs/WEIGHT_PAYLOAD_AND_NOMAD_LOADOUT.md`

---

# 13. Factory SE Equipment Relevant to Diagnostics

The five-door SE adds or includes equipment that can matter during electrical troubleshooting:

- cruise control
- steering-wheel audio controls
- Bluetooth hands-free system
- driver's auto-up power window
- heated power mirrors
- mirror-integrated turn signals
- projector headlights
- LED accent lighting
- headlamp welcome/escort function
- front fog lights
- rear wiper
- rear defroster with timer
- remote keyless entry
- roof-mounted antenna
- six-speaker audio system
- USB/auxiliary inputs

This matters when tracking:

- parasitic draws
- fuse assignments
- switch failures
- body-control behavior
- lighting faults
- wiring damage

---

# 14. Safety-System Baseline

Hyundai's 2014 U.S. Accent documentation identifies these standard systems:

- six airbags
- front airbags
- front seat-mounted side-impact airbags
- side-curtain airbags covering front/rear occupants
- active front head restraints
- ABS
- EBD
- Brake Assist
- ESC
- TCS
- VSM
- TPMS

## Airbag/SRS warning

Airbag and pretensioner circuits require special handling.

Never probe an SRS squib circuit casually with ordinary test equipment. Follow proper SRS service precautions before disconnecting connectors or removing seats/components containing airbags or pretensioners.

---

# 15. OBD-II / Electronic Diagnostics

The vehicle is OBD-II equipped and uses networked electronic control modules.

Useful diagnostic categories include:

```text
Pxxxx = powertrain-related DTCs
Bxxxx = body-related DTCs
Cxxxx = chassis-related DTCs
Uxxxx = network/communication DTCs
```

A basic emissions-code reader may expose only part of the diagnostic picture.

For serious troubleshooting, use a scanner capable of communicating with as many Hyundai modules as possible, such as:

- ECM/PCM
- transmission control functions
- ABS/ESC
- SRS
- MDPS
- body/electrical modules where supported

See:

`guides/ROADSIDE_DIAGNOSTIC_TRIAGE.md`

---

# 16. Historical Factory Fuel-Economy Rating

Hyundai's original 2014 model announcement listed:

| Transmission | City | Highway |
|---|---:|---:|
| 6-speed automatic | 27 mpg | 37 mpg |
| 6-speed manual | 27 mpg | 38 mpg |

These are **historical EPA-estimated ratings published by Hyundai for the model introduction**, not a promise of present-day real-world mileage.

Actual fuel economy varies with:

- speed
- temperature
- wind
- tire pressure
- tire model
- cargo weight
- road grade
- engine condition
- alignment
- driving behavior
- accessory use

For repair diagnosis, a sudden sustained fuel-economy change can be useful evidence when considered with fuel trims, tire pressure, brake drag, sensor data, and maintenance condition.

---

# 17. What Is NOT Yet Canonical

The following are intentionally **not** declared as verified factory service specifications in this baseline file:

- engine-oil viscosity
- engine-oil capacity
- coolant capacity
- coolant chemistry/specification
- automatic-transmission fluid specification
- automatic-transmission fill quantity
- brake-fluid specification
- refrigerant quantity
- spark-plug manufacturer/part number
- spark-plug gap
- battery group size
- alternator rated amperage
- fuel-tank capacity
- fuel-pressure values
- compression pressure
- valve clearances
- torque specifications
- alignment specifications
- rotor thickness limits
- wheel-lug torque
- jack/support points
- fuse/relay map

Those values are too consequential to populate from memory or random aggregator sites.

They will be added only after source verification.

---

# 18. Source Confidence System

Use these labels throughout the repository.

### `VERIFIED — HYUNDAI`
Directly supported by Hyundai documentation.

### `VERIFIED — STANDARD`
Defined by a relevant automotive or diagnostic standard.

### `VERIFIED — PARTS CATALOG`
Supported by manufacturer-linked or OEM parts-catalog data but not yet confirmed against the individual vehicle.

### `VERIFIED — OWNER`
Physically known or directly reported for this specific car.

### `VERIFIED — MULTIPLE SOURCES`
Supported independently by multiple reliable sources.

### `GENERAL DIAGNOSTIC PRACTICE`
Widely accepted automotive diagnostic methodology rather than a Hyundai-specific specification.

### `PROVISIONAL`
Useful working information that still requires stronger verification.

### `UNKNOWN`
Not yet established. **Unknown is preferable to a confident wrong answer.**

---

# 19. AI Retrieval Rules

An AI using this repository should follow these rules:

1. Treat this file as the canonical identity file for the target car.
2. Prefer a dedicated subsystem/specification file if it contains a newer, source-verified value.
3. Do not infer an exact service specification from another Hyundai/Kia model merely because it uses a related engine or transmission.
4. Do not transform `PROVISIONAL` information into a fact.
5. Do not transform a DTC into a parts order.
6. Distinguish **vehicle architecture** from **individual component condition**.
7. State when VIN/build-date verification is needed.
8. For safety-critical procedures, prefer factory information and clearly flag uncertainty.

Suggested AI response format:

```text
Vehicle identity:
Relevant verified facts:
Observed symptoms/data:
Likely causes ranked:
Tests that distinguish causes:
Safety concerns:
Required exact specifications:
Source confidence:
```

---

# 20. Core Architecture Summary

```text
2014 HYUNDAI ACCENT SE — U.S. FIVE-DOOR
│
├── ENGINE
│   └── Gamma 1.6 L GDI DOHC I4
│       ├── GDI
│       ├── Dual CVVT
│       ├── electronic throttle
│       └── timing chain
│
├── TRANSMISSION
│   └── 6-speed automatic transaxle
│       └── SHIFTRONIC
│
├── DRIVE
│   └── Front-wheel drive
│
├── STEERING
│   └── Column-mounted MDPS
│       └── SE sport calibration
│
├── FRONT SUSPENSION
│   └── MacPherson strut
│
├── REAR SUSPENSION
│   └── Torsion axle
│
├── BRAKES
│   ├── Front disc
│   ├── Rear disc (SE)
│   ├── ABS
│   ├── EBD
│   └── Brake Assist
│
├── STABILITY
│   ├── ESC
│   ├── TCS
│   └── VSM
│
└── FACTORY SE WHEELS
    └── 16-in alloy / 195/50R16
```

---

# 21. Primary Sources

## Hyundai Motor America / Hyundai Newsroom

**2014 Accent model announcement and technical overview**

https://www.hyundainews.com/releases/1756

This source supports, among other things:

- 2014 trim structure
- SE five-door configuration
- engine architecture
- GDI
- Dual CVVT
- timing chain
- electronic throttle control
- horsepower and torque
- six-speed manual/automatic availability
- SHIFTRONIC
- Active ECO
- wheelbase and five-door length
- cargo volume
- aerodynamic coefficient
- suspension architecture
- MDPS
- turning diameter
- SE 16-inch wheels and 195/50R16 tires
- SE rear disc brakes
- safety/stability systems

## Secondary parts-catalog evidence

**2014 HMA-market Accent example showing G4FD-series engine number**

https://ftp.gforceparts.com/en/catalog/genuine/vehicle?c=Hyundai&q=KMHCT4AE7EU690122

Use parts-catalog information as supporting evidence, not as a substitute for checking the target vehicle VIN/build date when fitment matters.

---

# 22. Planned Companion Specifications

Build next:

```text
specs/
├── VEHICLE_BASELINE.md              ← YOU ARE HERE
├── FLUIDS_AND_CAPACITIES.md
├── TORQUE_SPECS.md
├── FUSES_AND_RELAYS.md
├── WEIGHT_PAYLOAD_AND_NOMAD_LOADOUT.md
└── PARTS_AND_CONSUMABLES.md
```

Subsystem documents should link back to this baseline.

---

## Document Status

- **Scope:** 2014 U.S.-market Hyundai Accent SE five-door
- **Target transmission:** six-speed automatic
- **Primary source:** Hyundai Motor America
- **Design goal:** offline human + AI/RAG reference
- **Exact repair specifications:** intentionally deferred to source-specific documents
- **Copyright approach:** original organization and explanatory text; factual specifications cited to sources
