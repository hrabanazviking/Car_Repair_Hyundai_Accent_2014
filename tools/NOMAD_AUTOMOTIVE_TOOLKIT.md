# Nomad Automotive Toolkit

**Vehicle focus:** U.S.-market 2014 Hyundai Accent SE five-door, 1.6L Gamma GDI, 6-speed automatic, FWD  
**Purpose:** Build a compact, evidence-driven field toolkit for diagnosis, roadside stabilization, tire service, electrical checks, basic maintenance, and conservative recovery while living or traveling from the vehicle.  
**Rule:** A mobile toolkit should increase the chance of a safe diagnosis or safe exit. It should not encourage roadside work that requires a lift, press, refrigerant equipment, high-pressure GDI tooling, or other shop-level controls.

> **Unknown is preferable to a confident wrong answer. Verify the physical vehicle before depending on a size, connector, spare part, or lifting point in a remote location.**

---

## 1. Toolkit philosophy

The best field kit is not the largest kit. It is the smallest set of tools that can reliably answer these questions:

1. **Is the car safe to move?**
2. **Is the failure electrical, mechanical, fluid-related, tire-related, or control-related?**
3. **Can the problem be safely stabilized here?**
4. **Can the car reach pavement or professional help without creating a larger failure?**
5. **What evidence should be preserved before parts are replaced?**

The field workflow is:

```text
GET SAFE
  ↓
OBSERVE
  ↓
SCAN / MEASURE
  ↓
ISOLATE THE SYSTEM
  ↓
STABILIZE ONLY IF SAFE
  ↓
VERIFY
  ↓
MOVE ONLY AS FAR AS JUSTIFIED
  ↓
PERMANENT REPAIR
  ↓
LOG WHAT HAPPENED
```

A toolkit that cannot measure voltage, tire pressure, torque, or fault data is mostly a box of guessing tools.

---

# 2. Exact 2014 Hyundai factory anchors

The 2014 Accent owner's manual identifies the factory emergency tire-change equipment as:

- jack
- jack handle
- wheel-lug-nut wrench

These are stored in the luggage compartment under the luggage-box cover when the vehicle is equipped with the spare-tire setup.

Hyundai states that the factory jack is for **emergency tire changing only**. The car must be on firm, level ground, with the parking brake fully applied, the automatic transmission in `P`, and the wheel diagonally opposite the lift point blocked.

Hyundai also explicitly warns:

- do not place any part of the body under a vehicle supported only by the jack;
- use vehicle support stands if work beneath the vehicle is required;
- do not run the engine while the vehicle is on the jack;
- use only the designated jacking positions;
- do not use the bumper or arbitrary underbody areas as jack points.

### Exact wheel data

| Item | 2014 SE value |
|---|---:|
| Main tire size | `P195/50R16` |
| Wheel size | `6.0Jx16` |
| Cold pressure, front | `33 psi / 230 kPa` |
| Cold pressure, rear | `33 psi / 230 kPa` |
| Compact spare, if equipped | `T125/80D15` |
| Compact spare pressure | `60 psi / 420 kPa` |
| Compact spare maximum speed | `50 mph / 80 km/h` |
| Wheel-lug torque | `65-79 lb-ft / 88-107 N·m` |

### Factory fuse service rule

Hyundai requires a blown fuse to be replaced with a fuse of the **same rating**. The 2014 manual identifies a fuse-removal tool in the engine-compartment fuse panel.

Never install a larger fuse because the correct one keeps blowing. A fuse that blows repeatedly is evidence of a circuit fault.

Sources:

- https://www.manualslib.com/manual/1067849/Hyundai-2014-Accent.html
- https://manualzz.com/doc/53857913/hyundai-2014-accent-owner-manual
- https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/?srch=fuses

---

# 3. 21 mm lug-tool note

The 2014 parts catalog lists Hyundai wheel nut `52950-14140` as a valid Accent wheel nut. An OEM cross-reference for that exact Hyundai part number lists:

- thread: `M12 x 1.5`
- spanner size: `21 mm`

This is useful corroborating evidence for carrying a **21 mm six-point wheel socket**, but it is not being promoted to exact factory-owner-manual status.

**Field rule:** physically test the 21 mm socket on all installed wheel nuts before relying on it for remote travel. Aftermarket or replacement wheel nuts may differ.

Sources:

- https://www.hyundaipartsdeal.com/oem-2014-hyundai-accent-lug_nuts.html
- https://www.niparts.com/OEM/CB4CA1/KIA/5295014140.html

---

# 4. Tier A: must-carry field kit

These tools provide the greatest safety and diagnostic value per unit of storage space.

## 4.1 Tire and wheel kit

### Carry

- verified wheel-lug socket, **21 mm corroborated for factory nut 52950-14140**
- 1/2-inch breaker bar
- torque wrench that comfortably covers `65-79 lb-ft / 88-107 N·m`
- accurate tire-pressure gauge
- 12-volt or battery-powered tire inflator
- valve caps
- valve-core tool
- spare valve cores in a sealed container
- tread-depth gauge
- tire marking chalk or paint marker
- tire plug kit for **temporary mobility only**
- pliers for removing a puncturing object only after the repair plan is ready
- compact spare, if the vehicle is equipped for one
- factory jack and handle
- at least two solid wheel chocks

### Why these belong in the car

Tire problems are common, visible, and often field-manageable. They are also easy to make worse by driving on them.

The torque wrench is not optional in a serious field kit. "Tight enough" is not a specification.

### Never

- use the torque wrench as the breaker bar unless its manufacturer specifically permits that use;
- crawl underneath a vehicle supported only by the factory jack;
- plug a sidewall or shoulder injury as a permanent repair;
- keep driving on a tire with exposed cords, a bulge, major sidewall cut, separated tread, or repeated pressure loss.

Cross-reference:

- [`../tires-wheels/TIRES_WHEELS.md`](../tires-wheels/TIRES_WHEELS.md)
- [`../roadside/RECOVERY_TOWING_JACKING.md`](../roadside/RECOVERY_TOWING_JACKING.md)

---

## 4.2 Electrical and starting kit

### Carry

- digital multimeter
- 12-volt test light
- OBD-II scan tool
- lithium jump pack or equivalent portable booster
- compact jumper cables as a backup if storage permits
- fuse puller
- spare automotive blade fuses matching the ratings actually used in this car
- electrical-contact cleaner suitable for automotive connectors
- small brass or nylon cleaning brush
- heat-shrink tubing assortment
- quality crimp connectors
- quality crimping tool
- wire stripper
- short lengths of automotive primary wire in a few useful gauges
- electrical tape
- self-fusing silicone tape
- small alligator-jumper leads
- spare common-size nuts, washers, and electrical fasteners only when their use is known

### Multimeter minimum functions

The meter should reliably measure:

- DC voltage
- resistance
- continuity

Useful additions:

- min/max capture
- frequency
- duty cycle
- DC current with a properly fused input

A clamp meter capable of measuring DC current is useful but not mandatory for the minimal kit.

### Electrical field doctrine

```text
NO-CRANK / LOW VOLTAGE / WARNING LIGHTS
                ↓
CHECK BATTERY VOLTAGE
                ↓
CHECK TERMINALS
                ↓
CHECK LOADED VOLTAGE DROP
                ↓
CHECK FUSES
                ↓
SCAN MODULES
                ↓
ONLY THEN CONDEMN COMPONENTS
```

Never use an oversized fuse, foil, wire, or another improvised conductor as a fuse substitute.

Cross-reference:

- [`../electrical/BATTERY_STARTER_ALTERNATOR.md`](../electrical/BATTERY_STARTER_ALTERNATOR.md)
- [`../electrical/GROUND_POINTS.md`](../electrical/GROUND_POINTS.md)
- [`../electrical/WIRING_AND_CONNECTOR_DIAGNOSTICS.md`](../electrical/WIRING_AND_CONNECTOR_DIAGNOSTICS.md)
- [`../diagnostics/OBD2_GUIDE.md`](../diagnostics/OBD2_GUIDE.md)

---

## 4.3 General hand tools

A compact metric set provides far more value than a large mixed SAE/metric collection on this vehicle.

### Carry

- 1/4-inch metric socket set
- 3/8-inch metric socket set
- selected 1/2-inch sockets for high-torque work
- extensions in several lengths
- universal joint or wobble extension
- 1/4-inch ratchet
- 3/8-inch ratchet
- 1/2-inch breaker bar
- combination metric wrench set
- adjustable wrench for non-critical utility use
- locking pliers
- regular slip-joint pliers
- needle-nose pliers
- diagonal cutters
- pick set
- flat and Phillips screwdrivers
- trim-removal tools
- small pry tool
- hook/pick for hose and O-ring inspection, used carefully
- telescoping magnet
- inspection mirror
- compact flashlight
- headlamp

### Six-point versus twelve-point

Prefer six-point sockets for stubborn high-load hex fasteners because they place load closer to the flats rather than the corners.

Do not force the wrong-size tool onto a fastener. One rounded bolt can turn a roadside repair into a recovery call.

---

## 4.4 Safety and visibility kit

### Carry

- reflective safety vest
- reflective warning triangles or other legal roadside warning devices
- nitrile gloves
- heavier work gloves
- safety glasses
- kneeling pad
- compact first-aid kit
- fire extinguisher suitable for automotive use and mounted so it cannot become a projectile
- absorbent pads
- shop towels
- heavy trash bags
- small drain or catch container
- hand cleaner

### Night-work rule

A headlamp is one of the highest-value tools in a field kit because it leaves both hands free. Keep a backup light separate from the primary one.

---

# 5. Tier B: high-value nomad additions

These are not mandatory for every driver, but they make sense for repeated primitive-road travel and long distances from a workshop.

## 5.1 Recovery and terrain tools

### Carry when traveling primitive roads

- traction boards
- compact shovel
- folding saw only if legal and useful for route clearing, not for vehicle repair
- wheel chocks
- work gloves
- recovery blanket or damper for appropriate static recovery operations
- soft shackles for **verified rated recovery points only**
- tow strap intended for steady towing, if an appropriate rated connection is available
- kinetic recovery rope only for a future **verified rated kinetic recovery point**, never for the factory Accent tow eye

### Factory tow-eye rule

Hyundai's factory emergency towing hook is not a rated snatch-recovery point. The owner-manual recovery guidance prohibits jerking the hook and prohibits using the hook to pull the vehicle from mud or sand when the vehicle cannot free itself.

Therefore:

```text
FACTORY TOW EYE
      +
KINETIC ROPE
      =
DO NOT CONNECT
```

Use traction boards, digging, underbody clearance, and conservative self-recovery first.

Cross-reference:

- [`../roadside/RECOVERY_TOWING_JACKING.md`](../roadside/RECOVERY_TOWING_JACKING.md)

---

## 5.2 Supplemental lifting equipment

A compact **2-ton bottle jack** can be useful, but capacity alone does not make a lift safe.

Carry it only with:

- a stable base plate for soft ground
- a suitable saddle or adapter for the intended contact point
- rated support stands if any underbody work is contemplated

### Critical rule

The factory jacking points and bottle-jack contact geometry are not automatically interchangeable.

Never assume a narrow bottle-jack saddle is safe against a pinch weld or an arbitrary suspension/subframe surface.

If the correct lifting geometry is not known, use the factory jack for the tire change or recover the vehicle to a controlled workspace.

### Under-car work

No body part goes beneath the vehicle until it is supported by appropriately rated stands on stable ground.

---

## 5.3 Inspection and diagnostic additions

Useful compact additions include:

- USB or handheld borescope
- mechanic's stethoscope
- infrared thermometer
- spark tester designed for modern ignition systems
- compression tester
- vacuum gauge if appropriate adapters are available
- battery conductance tester
- DC clamp meter
- small inspection camera with side-view mirror attachment
- portable battery charger when shore power is available

### Borescope value

A borescope can inspect:

- cylinder condition through a spark-plug hole
- coolant or oil traces in cylinders
- piston crown differences
- inaccessible connector damage
- hidden fluid leaks
- under-dash routing

It is an evidence tool, not a verdict machine.

Cross-reference:

- [`../engine/COMPRESSION_LEAKDOWN_MECHANICAL_HEALTH.md`](../engine/COMPRESSION_LEAKDOWN_MECHANICAL_HEALTH.md)
- [`../engine/CYLINDER_HEAD_HEAD_GASKET.md`](../engine/CYLINDER_HEAD_HEAD_GASKET.md)

---

# 6. Fluids and consumables

Carry only fluids that can be safely stored and that have a realistic field purpose.

## High-value fluids

- correct engine oil for top-off
- premixed compatible coolant in a sealed bottle
- windshield-washer fluid
- small sealed brake-fluid container only if there is a specific maintenance need and storage is safe

Automatic-transmission fluid is useful as an emergency spare only if the user understands the correct fill/check procedure. Do not treat SP-IV ATF as a generic roadside pour-in fluid.

Cross-reference exact specifications before buying:

- [`../specs/FLUIDS_AND_CAPACITIES.md`](../specs/FLUIDS_AND_CAPACITIES.md)

## Useful consumables

- nitrile gloves
- shop towels
- absorbent pads
- zip ties
- stainless safety wire for non-critical temporary retention only
- assorted hose clamps for low-pressure hose applications only
- vacuum hose of verified compatible size
- electrical wire
- crimp terminals
- heat shrink
- spare blade fuses
- spare valve caps and cores
- thread-cleaning brush
- penetrating oil
- silicone lubricant where material-compatible
- anti-seize only where the specific procedure allows it

### Do not improvise these systems

Never field-patch or improvise:

- brake hydraulic lines
- brake hoses
- high-pressure GDI fuel lines
- steering or suspension structural joints
- SRS/airbag circuits
- high-current fusible links
- refrigerant lines

---

# 7. Spare parts worth considering

A nomad kit should not become a parts warehouse. Carry parts that are small, inexpensive, commonly useful, and unlikely to degrade in storage.

Possible candidates:

- selected spare blade fuses matching the vehicle
- one or two known-good relays only after verifying exact application
- spare exterior bulbs if applicable to the installed lamp assemblies
- valve caps and valve cores
- spare drain-plug gasket
- spare oil filter for planned remote oil service
- spare engine air filter for extended dusty travel
- spare cabin filter if desired
- known-correct accessory belt only after VIN/build verification

Potential parts that should be purchased only after exact VIN/build verification:

- accessory drive belt
- sensors
- ignition coils
- spark plugs
- relays
- oxygen sensors
- fuel-system parts
- TPMS components

Do not carry expensive electronic parts merely because they could fail. Diagnosis should come before parts replacement.

---

# 8. Scan tool requirements

A basic OBD-II reader should at minimum support:

- stored DTCs
- pending DTCs
- permanent DTCs when available
- freeze-frame data
- readiness monitors
- live engine data
- clearing codes only after evidence is saved

High-value live PIDs include:

- engine RPM
- coolant temperature
- intake-air temperature
- MAP
- calculated load
- throttle position
- commanded throttle where supported
- short-term fuel trim
- long-term fuel trim
- upstream and downstream oxygen / air-fuel sensor data as exposed by the ECM
- system voltage

A more advanced Hyundai-capable tool may provide ABS, ESC, MDPS, transmission, TPMS, body-module, and manufacturer-specific information. That is valuable, but the basic reader remains useful as a small field tool.

Cross-reference:

- [`../diagnostics/OBD2_GUIDE.md`](../diagnostics/OBD2_GUIDE.md)
- [`../electrical/CAN_NETWORK_DIAGNOSTICS.md`](../electrical/CAN_NETWORK_DIAGNOSTICS.md)

---

# 9. What belongs in a shop, not the car

These tools are too large, specialized, dangerous, or procedure-sensitive to justify routine nomad storage.

## Usually shop-only

- hydraulic floor jack
- full-height jack stands if storage makes them impractical, unless under-car work is planned
- vehicle lift
- hydraulic press
- coil-spring compressor
- wheel-bearing press tooling
- alignment rack
- tire mounting and balancing machine
- refrigerant recovery/recharge machine
- A/C manifold equipment unless the user is properly trained and legally permitted to service refrigerant
- GDI high-pressure fuel test equipment unless the exact procedure and pressure-rated equipment are known
- injector bench equipment
- cylinder-head resurfacing equipment
- valve-seat grinding equipment
- crankshaft micrometers and full engine-machining tools
- engine hoist
- transmission jack
- welding equipment
- oscilloscope larger than a practical portable diagnostic unit

### Rule

If the safe procedure requires a level concrete floor, a press, a lift, a refrigerant recovery station, machine-shop measurement, or high-pressure fuel tooling, the correct field decision is often **diagnose, document, and transport**.

---

# 10. Tool storage inside a nomad Accent

Tools become dangerous during a collision if they are not restrained.

## Storage priorities

- place the heaviest tools low in the vehicle
- keep dense metal tools away from the sleeping area when practical
- restrain toolboxes so they cannot launch forward
- keep sharp tools sheathed
- keep liquids upright in secondary containment
- isolate oily rags from heat sources
- do not let metal tools bridge battery terminals
- protect lithium jump packs and batteries from excessive heat, crushing, and puncture
- store the fire extinguisher where it is quickly reachable but firmly secured

### Suggested zones

```text
LOW / HEAVY ZONE
  breaker bar
  sockets
  jack accessories
  chocks
  recovery hardware

FAST ACCESS ZONE
  headlamp
  gloves
  safety vest
  triangles
  OBD scanner
  tire gauge
  inflator
  multimeter

CLEAN DIAGNOSTIC ZONE
  scan tool
  meter leads
  borescope
  electrical connectors
  spare fuses

FLUID ZONE
  sealed secondary container
  engine oil
  coolant
  washer fluid
```

---

# 11. Minimum viable Accent nomad kit

If space is extremely limited, retain these first:

| Category | Minimum |
|---|---|
| Tire | pressure gauge, inflator, verified lug socket, breaker bar, torque wrench, factory jack, chocks |
| Electrical | multimeter, scan tool, fuse puller, correct spare fuses, jump pack |
| Hand tools | compact metric socket/wrench set, screwdrivers, pliers, cutters |
| Safety | headlamp, backup light, gloves, eye protection, reflective vest, warning triangles |
| Recovery | traction boards, compact shovel |
| Fluids | correct engine oil, compatible premixed coolant |
| Documentation | offline copies of this repository and vehicle records |

This is enough to solve or classify a surprisingly large percentage of roadside problems without carrying a complete shop.

---

# 12. Expanded primitive-road kit

For extended remote travel, add:

- 2-ton bottle jack with verified adapter/base strategy
- rated jack stands if underbody work is planned
- borescope
- DC clamp meter
- battery tester
- mechanic's stethoscope
- IR thermometer
- temporary tire repair kit
- spare engine air filter
- verified spare accessory belt
- additional electrical repair supplies
- recovery boards
- shovel
- static tow strap only for appropriate rated connections
- soft shackles only for verified rated points

The kinetic rope may be carried for future use with an appropriately engineered recovery point or with another vehicle whose recovery points are verified. It is **not** for the Accent factory tow eye.

---

# 13. Pre-departure tool inspection

Before a remote trip:

1. Verify the lug socket fits every wheel nut.
2. Confirm the breaker bar can loosen the installed lug nuts.
3. Verify the torque wrench covers `65-79 lb-ft`.
4. Check the tire gauge against another known-good gauge if possible.
5. Run the tire inflator and inspect its hose.
6. Check the compact spare for `60 psi` if equipped.
7. Charge the jump pack.
8. Test the multimeter on a known voltage source.
9. Confirm the OBD scanner communicates with the car.
10. Verify the fuse kit actually contains the ratings used by the car.
11. Confirm the jack, handle, chocks, and wheel tools are accessible without unloading the whole vehicle.
12. Check that liquids have not leaked.
13. Inspect recovery boards and shovel.
14. Check that the fire extinguisher and safety gear are accessible.
15. Confirm offline copies of the repair repository are current.

---

# 14. Maintenance of the toolkit itself

The toolkit is part of the vehicle reliability system.

## Monthly or before remote travel

- recharge jump pack
- check flashlight/headlamp batteries
- inspect inflator wiring and hose
- inspect meter leads for damaged insulation
- check spare fuses
- inspect tire plug cement and rubber components for age/drying
- check stored fluids for leakage
- inspect straps and shackles for cuts, abrasion, heat damage, corrosion, or chemical contamination
- inspect traction boards for cracks
- verify jack screw or hydraulic mechanism operates normally
- verify toolboxes remain securely restrained

Do not assume an emergency tool still works because it worked last year.

---

# 15. AI diagnostic rules for Runa / Aesir

When this file is used by an offline assistant, follow these rules:

1. **Ask what tools are actually present before recommending a test.**
2. Do not tell the user to crawl under a vehicle supported only by a jack.
3. Do not recommend a torque value unless a verified value is available.
4. Do not invent a socket size.
5. Treat `21 mm` for the factory-style wheel nut as corroborated, then require physical verification.
6. Preserve freeze frame and codes before clearing them.
7. Prefer voltage-drop testing over guessing at cables, starters, grounds, or alternators.
8. Prefer tire-pressure measurement over visual estimation.
9. Prefer torque measurement over "tight enough."
10. Never recommend a larger fuse to stop repeat fuse failure.
11. Never recommend kinetic recovery from the factory tow eye.
12. Never recommend under-car work without stable rated support stands.
13. Never recommend opening a hot pressurized cooling system.
14. Never recommend cracking a GDI high-pressure fuel line to "see if fuel comes out."
15. If the safe repair requires shop equipment, say so clearly.

---

# 16. Field incident record

Use a structured record so tool effectiveness can be improved over time.

```yaml
incident:
  date:
  odometer_miles:
  location_type: pavement|gravel|dirt|sand|mud|snow|camp
  symptom:
  vehicle_safe_to_move: unknown

initial_observations:
  warning_lights: []
  fluid_leak: unknown
  tire_damage: unknown
  smoke_or_steam: unknown
  abnormal_noise: unknown

measurements:
  battery_engine_off_v:
  battery_cranking_v:
  charging_v:
  tire_pressures_psi: {}
  dtcs: []
  freeze_frame_saved: false

field_tools_used: []
field_action:
  action_taken:
  temporary_or_permanent:
  distance_driven_after_repair_miles:

outcome:
  resolved: false
  tow_required: false
  shop_repair_required: false
  root_cause:

kit_review:
  tool_that_saved_trip:
  tool_missing:
  tool_carried_but_unnecessary:
  consumable_to_replace:
```

---

# 17. Cross-links

- [`../guides/ROADSIDE_DIAGNOSTIC_TRIAGE.md`](../guides/ROADSIDE_DIAGNOSTIC_TRIAGE.md)
- [`../roadside/EMERGENCY_FIELD_REPAIRS.md`](../roadside/EMERGENCY_FIELD_REPAIRS.md)
- [`../roadside/RECOVERY_TOWING_JACKING.md`](../roadside/RECOVERY_TOWING_JACKING.md)
- [`../maintenance/PRE_TRIP_INSPECTION.md`](../maintenance/PRE_TRIP_INSPECTION.md)
- [`../maintenance/NOMAD_SERVICE_LOG.md`](../maintenance/NOMAD_SERVICE_LOG.md)
- [`../specs/FLUIDS_AND_CAPACITIES.md`](../specs/FLUIDS_AND_CAPACITIES.md)
- [`../specs/FUSES_AND_RELAYS.md`](../specs/FUSES_AND_RELAYS.md)
- [`../specs/TORQUE_SPECS.md`](../specs/TORQUE_SPECS.md)
- [`../diagnostics/OBD2_GUIDE.md`](../diagnostics/OBD2_GUIDE.md)
- [`../electrical/BATTERY_STARTER_ALTERNATOR.md`](../electrical/BATTERY_STARTER_ALTERNATOR.md)
- [`../electrical/WIRING_AND_CONNECTOR_DIAGNOSTICS.md`](../electrical/WIRING_AND_CONNECTOR_DIAGNOSTICS.md)
- [`../tires-wheels/TIRES_WHEELS.md`](../tires-wheels/TIRES_WHEELS.md)

---

# 18. Source notes

## Exact 2014 owner-level sources

**2014 Hyundai Accent Owner's Manual, emergency jack/tool and wheel-service guidance**  
https://manualzz.com/doc/53857913/hyundai-2014-accent-owner-manual

**2014 Hyundai Accent Owner's Manual, alternate indexed copy**  
https://www.manualslib.com/manual/1067849/Hyundai-2014-Accent.html

**2014 Hyundai Accent fuse replacement guidance**  
https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/?srch=fuses

## Exact/corroborating parts sources

**2014 Accent wheel nuts, Hyundai parts catalog**  
https://www.hyundaipartsdeal.com/oem-2014-hyundai-accent-lug_nuts.html

**Hyundai 52950-14140 cross-reference showing M12 x 1.5 thread and 21 mm spanner size**  
https://www.niparts.com/OEM/CB4CA1/KIA/5295014140.html

---

# 19. Core rule

```text
THE BEST NOMAD TOOLKIT
IS NOT THE BIGGEST TOOLKIT.

IT IS THE KIT THAT LETS YOU:

GET SAFE
MEASURE
DIAGNOSE
STABILIZE
VERIFY
AND KNOW WHEN TO STOP.
```
