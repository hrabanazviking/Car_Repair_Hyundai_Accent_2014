# 2014 Hyundai Accent SE — Maintenance Schedule

> **Purpose:** A practical, source-aware maintenance schedule for a U.S.-market 2014 Hyundai Accent SE, organized for offline use by both humans and AI assistants.
>
> **Primary rule:** When Hyundai specifies both mileage and time, service is due at **whichever comes first**.

---

## 1. Scope

This document is intended for the 2014 Hyundai Accent SE five-door, especially the 1.6 L GDI engine and six-speed automatic transmission configuration documented elsewhere in this repository.

Related files:

- `../specs/VEHICLE_BASELINE.md`
- `../specs/FLUIDS_AND_CAPACITIES.md`
- `../specs/FUSES_AND_RELAYS.md`
- `../guides/ROADSIDE_DIAGNOSTIC_TRIAGE.md`

This schedule is based primarily on Hyundai's 2014 Accent owner documentation and Hyundai's 2014 Accent Quick Reference Guide.

---

# 2. Normal vs. Severe Service

Hyundai distinguishes between **normal usage** and **severe usage**.

Use the severe schedule when the vehicle is regularly operated under one or more severe conditions.

## Hyundai severe-use conditions

Severe conditions include:

- Repeated trips shorter than about 5 miles (8 km) in normal temperatures
- Repeated trips shorter than about 10 miles (16 km) in freezing temperatures
- Extensive idling
- Long periods of low-speed operation
- Rough roads
- Dusty roads
- Muddy roads
- Unpaved roads
- Gravel roads
- Salt-covered roads
- Very cold-weather operation
- Sandy areas
- Heavy traffic in temperatures above 90°F / 32°C
- Frequent uphill, downhill, or mountain driving
- Trailer towing
- Camper or roof-rack use
- Commercial/taxi/patrol-type use
- Frequent stop-and-go driving
- Sustained extremely high-speed driving

### Practical interpretation for camping / nomad use

Vehicle-based camping can easily become severe service if it includes:

- Primitive-camping access roads
- Gravel forest roads
- Dusty BLM/National Forest roads
- Long idling periods for heating, cooling, charging, or waiting
- Repeated short supply trips
- Mountain passes
- Winter salt
- Desert heat
- Slow driving on rough roads

**Practical repository default:** If primitive camping or nomad travel regularly exposes the car to dust, gravel, rough roads, extended idling, repeated short trips, mountain roads, or severe temperatures, use the **severe-service engine-oil schedule** and inspect affected components more often.

Do not classify every highway road trip as severe merely because it is long-distance. Steady highway driving at normal speeds is generally comparatively easy on the powertrain.

---

# 3. High-Level Maintenance Table

| Item | Normal Usage | Severe Usage | Notes |
|---|---:|---:|---|
| Engine oil & filter | 7,500 mi / 12 months | 3,750 mi / 6 months | Whichever comes first |
| Tire rotation | 7,500 mi | 7,500 mi | Inspect tires at rotation |
| Battery condition | Inspect every 7,500 mi | Same baseline; inspect more often in extreme climate | Clean terminals as needed |
| Engine air filter | Inspect every 7,500 mi; replace every 30,000 mi | Replace more frequently in dust/sand | Primitive roads may shorten life substantially |
| Cabin / climate filter | Replace every 15,000 mi | More frequently in dust/sand | Also inspect if HVAC airflow drops |
| A/C refrigerant/system | Inspect every 15,000 mi | Same baseline | Refrigerant charge is not routine DIY top-off |
| Brake hoses & lines | Inspect every 15,000 mi | Same baseline, plus more corrosion checks where salted | Safety-critical |
| Front brake discs/pads/calipers | Inspect every 15,000 mi | More frequently under listed severe conditions | Mountain driving increases wear |
| Rear brake discs/pads | Inspect every 15,000 mi | More frequently under listed severe conditions | SE uses rear discs |
| Drive shafts & CV boots | Inspect every 15,000 mi | Every 7,500 mi / 6 months under applicable severe use | Rough/gravel roads matter |
| Exhaust pipe & muffler | Inspect every 15,000 mi | Same baseline; inspect after impacts | Rust/road damage important |
| Steering gear/linkage/boots/ball joints | Inspect every 15,000 mi | More frequently; Hyundai QRG summarizes 7,500 mi / 6 mo for severe use | Rough roads matter |
| Suspension mounting bolts | Inspect every 15,000 mi | Same baseline | Recheck after severe impacts/repairs |
| Brake fluid | Inspect every 30,000 mi | Same baseline | Condition matters, not just level |
| Fuel lines/hoses/connections | Inspect every 30,000 mi | Same baseline | GDI fuel safety applies |
| Fuel filter | Inspect periodically / around 30,000-mi schedule points | Replace more readily if restriction symptoms occur | Hyundai treats it as largely maintenance-free unless symptoms/fuel-quality issues arise |
| Fuel tank air filter | Inspect about every 30,000 mi where equipped | Same baseline | Availability/configuration may vary |
| Parking brake | Inspect every 30,000 mi | More frequently | Important if frequently parking on slopes |
| Vapor hose & fuel filler cap | Inspect every 30,000 mi | Same baseline | EVAP-related |
| Valve clearance | Inspect every 60,000 mi / 72 months | Same baseline | Especially if abnormal valve noise or drivability symptoms |
| Drive belt | First inspect 60,000 mi / 72 months; then every 15,000 mi / 24 months | Same baseline | Replace if cracked/damaged or tension inadequate |
| Spark plugs, iridium | See conflict note below | More frequently under applicable severe use | Conservative repository interval: 97,500 mi |
| Engine coolant | First replace 120,000 mi / 120 months; then every 30,000 mi / 24 months | Same baseline | Time is critical on an older vehicle |
| Automatic transmission fluid | No routine service under normal schedule | Replace every 60,000 mi under applicable severe conditions | Use correct SP-IV/SP-4 specification |

---

# 4. Engine Oil and Filter

## Normal service

**Replace every 7,500 miles or 12 months, whichever comes first.**

## Severe service

**Replace every 3,750 miles or 6 months, whichever comes first.**

Severe conditions apply broadly to the engine-oil interval. Hyundai's severe-use chart applies the shortened interval to conditions A through K.

### Between changes

Check oil level regularly.

Recommended practical habits:

- Check before a long trip.
- Check after long high-speed highway travel.
- Check more frequently if oil consumption develops.
- Check after any leak is discovered.
- Check after engine work.

Never assume that a modern synthetic oil makes the factory service interval irrelevant.

See `../specs/FLUIDS_AND_CAPACITIES.md` for oil specification and capacity.

---

# 5. Tires

## Rotation

**Every 7,500 miles.**

At each rotation inspect:

- Tread depth
- Uneven wear
- Cuts
- Cracks
- Bulges
- Embedded objects
- Sidewall damage
- Wheel damage
- Lug/stud condition

Uneven wear can point to:

- Alignment error
- Worn suspension components
- Incorrect tire pressure
- Bent wheel or suspension component
- Driving pattern

Check inflation monthly and before long trips.

Always use the vehicle's tire-pressure placard as the primary inflation reference, not the maximum pressure molded into the tire sidewall.

---

# 6. Engine Air Filter

## Normal

- Inspect every **7,500 miles**.
- Replace every **30,000 miles**.

## Severe dust / sand

Replace **more frequently**.

For a car used on dusty primitive-camping roads, visual inspection is more valuable than blindly waiting for 30,000 miles.

Inspect sooner if:

- The car follows other vehicles on dusty roads.
- Dust is visible inside the airbox downstream of the filter.
- Fuel economy or performance changes.
- The filter is physically damaged or saturated.

Do not blow high-pressure compressed air through a disposable filter unless the filter manufacturer explicitly permits it.

---

# 7. Cabin / Climate-Control Air Filter

## Normal

Replace every **15,000 miles**.

## Severe dust or sand

Replace more frequently.

Earlier replacement may be useful if:

- HVAC airflow drops.
- Dust or odor increases.
- The blower becomes noisy.
- The car spends significant time on dirt roads.

---

# 8. Brakes

Hyundai calls for routine brake-system inspection.

## Every 15,000 miles

Inspect:

- Front brake discs
- Front pads
- Calipers
- Rear brake discs/pads on the SE
- Brake hoses and lines

## Every 30,000 miles

Inspect:

- Brake fluid
- Parking brake

## Inspect more frequently when

- Driving mountain roads
- Using brakes heavily
- Traveling rough/gravel/salted roads
- Carrying heavy loads
- Braking feel changes

### Stop and repair immediately if

- Pedal becomes abnormally soft
- Pedal sinks
- Brake fluid leaks
- Braking force drops
- Strong pulling begins under braking
- Grinding begins

Do not extend pad life until metal-to-metal contact. Rotors cost more than pads.

---

# 9. Drive Shafts and CV Boots

## Normal

Inspect every **15,000 miles**.

## Severe use

Hyundai specifies inspection every **7,500 miles / 6 months** under applicable severe conditions.

Look for:

- Split CV boots
- Grease thrown around the wheel well
- Loose clamps
- Clicking on turns
- Vibration under acceleration

A torn boot caught early can be dramatically cheaper than waiting for the joint to fail.

---

# 10. Steering and Suspension

## Normal

Inspect every **15,000 miles**:

- Steering gear/linkage
- Steering boots
- Lower ball joints
- Upper ball-joint-related components where applicable
- Suspension mounting bolts

## Severe / rough-road use

Inspect steering and joint components more often.

Hyundai's 2014 Quick Reference Guide summarizes severe steering/joint inspection at **7,500 miles or 6 months**.

Primitive road travel makes this especially useful.

Inspect after a hard impact with:

- Pothole
- Rock
- Curb
- Deep rut
- Road debris

Watch for:

- New clunk
- Steering looseness
- Pulling
- Uneven tire wear
- Steering-wheel position changing while driving straight

---

# 11. Exhaust System

Inspect at least every **15,000 miles** and after any suspected underbody impact.

Look for:

- Leaks
- Loose shields
- Broken hangers
- Rust perforation
- Impact damage

**Exhaust fumes entering the cabin are a safety emergency.**

Do not sleep in an idling vehicle.

---

# 12. Fuel System

## Every 30,000 miles

Inspect as applicable:

- Fuel lines
- Fuel hoses
- Connections
- Fuel tank air filter
- Vapor hose
- Fuel filler cap
- Fuel filter condition/function

Hyundai describes the fuel filter and fuel-tank air filter as largely maintenance-free but recommends periodic inspection depending on fuel quality.

Replace or diagnose the fuel filter regardless of scheduled mileage if symptoms suggest restriction, such as:

- Hard starting
- Surging
- Power loss
- Fuel-flow restriction symptoms

### GDI warning

This engine uses gasoline direct injection.

Do not open high-pressure fuel lines casually.

See the GDI safety section in `../guides/ROADSIDE_DIAGNOSTIC_TRIAGE.md`.

---

# 13. Spark Plugs — Source Conflict

There is a documented discrepancy between Hyundai maintenance sources for the 2014 Accent.

## 2014 owner's manual

The owner's manual maintenance schedule lists:

**Replace iridium-plated spark plugs every 97,500 miles (156,000 km).**

## 2014 Quick Reference Guide

The Quick Reference Guide summarizes:

**Replace iridium-coated spark plugs at 105,000 miles.**

## Repository policy

Use **97,500 miles** as the conservative maintenance target unless the exact vehicle's original glovebox documentation or Hyundai VIN-specific service information establishes otherwise.

Severe-use guidance says to replace spark plugs **more frequently** under applicable conditions, particularly extensive idling and towing/camper-type use.

### Replace/inspect earlier if

- Persistent misfire develops
- Plug fouling is suspected
- Coil boots are contaminated with oil/coolant
- Plug damage is found
- Gap has eroded excessively

Do not guess spark-plug gap or torque. Store those values only in source-verified specification files.

---

# 14. Valve Clearance

Inspect every **60,000 miles / 72 months**.

Inspection becomes more important if there is:

- Persistent valvetrain ticking
- Compression imbalance
- Rough running
- Hard starting
- Unexplained power loss

Do not adjust valve clearance without verified specifications and procedures.

---

# 15. Accessory Drive Belt

## First inspection

**60,000 miles / 72 months**

## Thereafter

**Every 15,000 miles / 24 months**

Inspect for:

- Cracks
- Fraying
- Missing ribs
- Contamination
- Glazing
- Abnormal tension
- Pulley misalignment
- Bearing noise

Hyundai states that the belt should be replaced when cracks occur or tension is reduced excessively.

For an older vehicle, belt age matters even if mileage is low.

---

# 16. Engine Coolant

## Factory interval

First replacement:

**120,000 miles / 120 months**

Thereafter:

**Every 30,000 miles / 24 months**

### Age matters

A 2014 vehicle has already exceeded the original 120-month time threshold by 2026.

If coolant replacement history is unknown, treat coolant service status as **UNKNOWN**, not automatically "good because mileage is low."

Verify coolant condition/history and use the correct coolant specification.

See `../specs/FLUIDS_AND_CAPACITIES.md`.

---

# 17. Automatic Transmission Fluid

## Normal usage

Hyundai's normal schedule states:

**No check / no scheduled service required** for the automatic-transmission fluid.

## Severe usage

Replace every:

**60,000 miles (96,000 km)**

under applicable severe conditions, including certain combinations of:

- Short trips
- Rough/dusty roads
- Sandy areas
- Hot heavy traffic
- Mountain driving
- Commercial-type operation

### Repository practical policy

For a vehicle entering regular primitive-road, mountain, hot-weather, or stop-and-go nomad use, do not assume "lifetime fluid" means literally forever.

Use only the verified Hyundai SP-IV / SP-4 specification documented in `../specs/FLUIDS_AND_CAPACITIES.md`.

Do not use universal ATF unless its manufacturer explicitly documents compatibility with the required Hyundai specification.

Do not perform an aggressive power flush merely because the transmission is old. Service strategy should consider history, condition, symptoms, and correct procedures.

---

# 18. Fuel Additive Guidance

Hyundai's 2014 schedule recommends fuel additive at the oil-service cadence **if TOP TIER Detergent Gasoline is not available**.

Do not stack multiple fuel additives together.

Do not treat aftermarket additives as a cure for mechanical faults.

---

# 19. Owner Checks Between Scheduled Services

Hyundai also specifies owner-level checks outside the main mileage schedule.

## While driving

Pay attention to:

- New exhaust sounds
- Exhaust smell in the cabin
- Steering-wheel vibration
- Increased steering effort
- Steering looseness
- Vehicle pulling to one side
- Unusual braking noises
- Increased brake-pedal travel
- Hard brake pedal
- Transmission slipping or changed behavior
- Parking-brake operation
- Fluid leaks

Water dripping from the air-conditioning system during/after use can be normal condensation.

## At least monthly

Check:

- Engine coolant reservoir level
- Exterior lights
- Brake lights
- Turn signals
- Hazard lights
- Tire pressures, including spare if equipped

## At least twice per year

Check:

- Radiator hoses
- Heater hoses
- A/C hoses for visible damage/leaks
- Washer spray
- Wiper operation
- Headlight aim
- Muffler/exhaust pipes/shields/clamps
- Seat belts
- Tire wear
- Wheel-lug condition

## At least once per year

- Clean body and door drain holes
- Lubricate door hinges/checks
- Lubricate hood hinges
- Lubricate door/hood locks and latches
- Lubricate door weatherstrips appropriately
- Check A/C operation
- Inspect automatic-transmission linkage/controls as applicable
- Clean battery and terminals
- Check brake-fluid level

---

# 20. Primitive-Camping / Nomad Inspection Routine

This is a **repository recommendation**, not a separate Hyundai factory schedule.

It translates Hyundai's severe-use categories into an easy travel routine.

## Before leaving pavement for a remote campsite

Check:

- Engine oil level
- Coolant level when engine is cold
- Tire pressure
- Tire sidewalls/tread
- Spare tire condition if equipped
- Visible leaks
- Battery security
- Underbody clearance hazards
- Brake feel
- Warning lights

## After a rough / gravel / muddy road

Inspect:

- Tires for cuts or punctures
- Wheels for dents
- CV boots
- Lower engine bay / splash shields
- Exhaust system
- Suspension for visible damage
- Fluid leaks
- Packed mud around cooling or brake components

## After heavy dust

Inspect sooner:

- Engine air filter
- Cabin air filter
- Radiator/condenser exterior airflow path

Do not blast delicate cooling fins with high-pressure water.

## Before a major highway run

Check:

- Oil
- Coolant
- Tires
- Lights
- Brakes
- Wipers/washer fluid
- Battery/charging behavior
- Any unresolved OBD-II codes

---

# 21. Unknown-History Catch-Up Strategy

For an older vehicle, maintenance history matters as much as odometer mileage.

If the history of an item cannot be established, mark it:

```text
STATUS: UNKNOWN
```

Do not silently assume it was serviced.

## High-priority history items to establish

- Last engine oil/filter change
- Coolant replacement date
- Automatic-transmission-fluid service history
- Spark-plug replacement history
- Brake service history
- Brake-fluid history
- Engine air-filter replacement
- Cabin filter replacement
- Drive-belt age/condition
- Battery age
- Tire age (DOT date code)

### Sensible catch-up principle

Do not replace everything blindly.

Use this order:

```text
VERIFY HISTORY
    ↓
INSPECT CONDITION
    ↓
IDENTIFY OVERDUE / UNKNOWN SAFETY ITEMS
    ↓
SERVICE SAFETY-CRITICAL ITEMS FIRST
    ↓
SERVICE FLUIDS / FILTERS
    ↓
ADDRESS WEAR ITEMS
    ↓
RECORD BASELINE
```

---

# 22. Maintenance Priority Levels

## PRIORITY 1 — Safety

Examples:

- Tires
- Brakes
- Steering
- Suspension damage
- Critical lights
- Fuel leaks

## PRIORITY 2 — Prevent catastrophic mechanical damage

Examples:

- Engine oil
- Cooling system
- Charging system
- Severe transmission-fluid issues
- Major fluid leaks

## PRIORITY 3 — Reliability

Examples:

- Battery condition
- Spark plugs
- Drive belt
- Filters
- Preventive electrical repairs

## PRIORITY 4 — Comfort / convenience

Examples:

- Cabin filter
- Non-safety cosmetic items
- Convenience accessories

When money or time is limited, prioritize by consequence of failure rather than by cosmetic annoyance.

---

# 23. Maintenance Log Template

```markdown
## Service Record

**Date:**
**Mileage:**
**Location / shop:**

### Work performed

- [ ] Engine oil
- [ ] Oil filter
- [ ] Tire rotation
- [ ] Engine air filter
- [ ] Cabin air filter
- [ ] Coolant
- [ ] Automatic transmission fluid
- [ ] Brake inspection
- [ ] Brake fluid
- [ ] Spark plugs
- [ ] Drive belt
- [ ] Battery
- [ ] Other

### Parts / fluids used


### Specifications


### Observations


### OBD-II codes before service


### OBD-II codes after service


### Next service due

**Mileage:**
**Date:**

### Receipts / part numbers


```

---

# 24. AI Maintenance Query Template

```text
Vehicle: 2014 Hyundai Accent SE 1.6L GDI automatic
Current mileage: _____
Current date: _____
Known maintenance history: _____
Unknown maintenance history: _____
Recent driving conditions: _____
Percent pavement vs gravel/dirt: _____
Frequent short trips: yes/no
Frequent idling: yes/no
Mountain driving: yes/no
Extreme heat/cold: yes/no
Recent symptoms or DTCs: _____

Using the repository maintenance schedule:
1. Determine whether recent use qualifies as severe service.
2. List maintenance that is due now.
3. Separate verified-due items from history-unknown items.
4. Prioritize safety-critical work first.
5. Do not invent service history.
6. Do not recommend parts replacement solely because of age unless the component is age-limited, visibly degraded, or due by time interval.
```

---

# 25. Machine-Readable Summary

```yaml
vehicle:
  year: 2014
  make: Hyundai
  model: Accent
  trim: SE
  market: US

maintenance:
  engine_oil_filter:
    normal:
      miles: 7500
      months: 12
    severe:
      miles: 3750
      months: 6

  tire_rotation:
    miles: 7500

  engine_air_filter:
    inspect_miles: 7500
    replace_miles: 30000
    severe: "replace more frequently in dust/sand"

  cabin_air_filter:
    replace_miles: 15000
    severe: "replace more frequently in dust/sand"

  brakes:
    inspect_miles: 15000
    severe: "inspect more frequently under applicable severe conditions"

  drive_shafts_cv_boots:
    normal_inspect_miles: 15000
    severe_inspect_miles: 7500
    severe_inspect_months: 6

  steering_suspension:
    normal_inspect_miles: 15000
    severe_summary_miles: 7500
    severe_summary_months: 6

  brake_fluid:
    inspect_miles: 30000

  fuel_system:
    inspect_miles: 30000

  parking_brake:
    inspect_miles: 30000

  valve_clearance:
    inspect_miles: 60000
    inspect_months: 72

  drive_belt:
    first_inspect_miles: 60000
    first_inspect_months: 72
    subsequent_inspect_miles: 15000
    subsequent_inspect_months: 24

  spark_plugs:
    type: iridium
    repository_conservative_replace_miles: 97500
    source_conflict:
      owner_manual_miles: 97500
      quick_reference_guide_miles: 105000

  coolant:
    first_replace_miles: 120000
    first_replace_months: 120
    subsequent_replace_miles: 30000
    subsequent_replace_months: 24

  automatic_transmission_fluid:
    normal: "no scheduled service per original Hyundai normal schedule"
    severe_replace_miles: 60000
    required_spec: "Hyundai SP-IV / SP-4"
```

---

# 26. Source Notes

Primary references used to construct this file:

1. **2014 Hyundai Accent Owner's Manual — Maintenance section**
   - Scheduled maintenance
   - Severe-usage conditions
   - Owner maintenance checks
   - Normal maintenance schedule
   - Maintenance under severe usage conditions
   - Online reference: https://www.manualslib.com/manual/1067849/Hyundai-2014-Accent.html
   - Alternate searchable copy: https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/

2. **2014 Hyundai Accent Quick Reference Guide — Maintenance table**
   - Summarizes normal and severe intervals
   - Archived copy: https://www.dezosmanuals.com/wp-content/uploads/2021/07/2014-Hyundai-Accent-QRG.pdf

### Source conflict policy

Where two Hyundai-branded documents conflict:

1. Preserve both values.
2. Prefer the more detailed vehicle owner's manual unless VIN-specific factory information says otherwise.
3. For preventive maintenance, a modestly earlier interval is generally preferable to silently extending the interval.
4. Mark the conflict clearly for future review.

---

# 27. Repository Maintenance Philosophy

```text
KNOW THE INTERVAL
      ↓
KNOW THE DRIVING CONDITIONS
      ↓
VERIFY HISTORY
      ↓
INSPECT THE ACTUAL CAR
      ↓
SERVICE WHAT IS DUE
      ↓
RECORD WHAT WAS DONE
```

The odometer is only one clock.

**Time, heat, dust, corrosion, idling, road conditions, and maintenance history are clocks too.**

---

## Document Status

- **Vehicle:** 2014 Hyundai Accent SE
- **Purpose:** Preventive maintenance planning
- **Normal schedule:** Included
- **Severe schedule:** Included
- **Nomad / primitive-road interpretation:** Included as repository guidance
- **Source discrepancies:** Explicitly preserved
- **Exact repair procedures / torque values:** Deferred to dedicated source-verified documents
