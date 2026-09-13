# 2014 Hyundai Accent SE — Cooling System

> **Purpose:** Component-level reference for the cooling system of a U.S.-market 2014 Hyundai Accent SE with the 1.6 L Gamma GDI engine. Designed for offline field use by humans and AI/RAG systems.
>
> **Core rule:** Overheating is a **system problem to diagnose**, not a thermostat-replacement command.

---

## 1. Scope

This document maps the physical cooling system and explains how its parts interact:

- Coolant pump / water pump
- Thermostat / water-temperature-control assembly
- Radiator
- Electric cooling fan and shroud
- Radiator cap and reservoir
- Upper/lower radiator hoses
- Heater circuit
- Engine Coolant Temperature (ECT) sensor
- Coolant flow and air bleeding
- Pressure testing
- Leak diagnosis
- Component-level failure patterns

Related files:

- `../diagnostics/OVERHEATING.md`
- `../specs/FLUIDS_AND_CAPACITIES.md`
- `../maintenance/MAINTENANCE_SCHEDULE.md`
- `../maintenance/PRE_TRIP_INSPECTION.md`
- `ENGINE_OVERVIEW.md`

`OVERHEATING.md` is the emergency/triage guide. This file explains the **hardware and system behavior behind the symptom**.

---

# 2. Source and Confidence Hierarchy

Confidence labels used here:

- **VERIFIED — 2014 OE CATALOG:** 2014 Accent hardware or part identity shown in Hyundai OE catalog data.
- **VERIFIED — OWNER MANUAL:** 2014 Hyundai Accent owner documentation.
- **SERVICE-FAMILY — SAME GENERATION:** Same-generation Accent 1.6 L Hyundai service data, useful for procedures/specifications but not promoted to exact VIN-specific 2014 fact without confirmation.
- **GENERAL DIAGNOSTIC PRACTICE:** Accepted cooling-system diagnostic method.
- **OWNER-SPECIFIC:** Must be confirmed from the exact vehicle, label, VIN, build date, or installed part.

When exact service specifications matter, prefer:

1. Exact VIN/build-specific Hyundai service information
2. Physical label/installed part on this vehicle
3. 2014 Hyundai owner documentation
4. Same-generation Hyundai service data
5. Trusted general diagnostic practice

---

# 3. System Architecture

The 1.6 L Gamma GDI engine uses a conventional liquid-cooling system with forced circulation and an electric radiator fan.

Simplified heat path:

```text
COMBUSTION / ENGINE METAL
          ↓
       COOLANT
          ↓
      WATER PUMP
          ↓
 ENGINE BLOCK / CYLINDER HEAD
          ↓
      THERMOSTAT
       ↙       ↘
 BYPASS/HEATER   RADIATOR
                    ↓
               ELECTRIC FAN
                    ↓
             HEAT TO AMBIENT AIR
```

The thermostat controls when significant radiator flow begins. The pump provides circulation. The radiator rejects heat. The electric fan supplies airflow when vehicle speed alone is insufficient.

The heater core is also part of the coolant circuit and can provide useful diagnostic clues.

---

# 4. 2014 OE Hardware Map

The 2014 Hyundai Accent 1.6 L Gamma GDI parts catalog identifies the following cooling-system hardware.

> **Verify VIN/build date before ordering. Part supersessions and production changes can occur.**

| Component | 2014 OE catalog example | Notes |
|---|---|---|
| Coolant pump assembly | `25100-2B700` | Belt-driven mechanical pump |
| Water-pump gasket | `25124-2B000` | Replace when servicing pump as applicable |
| Coolant-pump pulley | `25221-2B700` | Driven by accessory belt |
| Thermostat assembly | `25500-2B000` | Located in water-temperature-control circuit |
| ECT sensor | `39220-38030` | Engine coolant temperature input to ECM |
| Radiator, 6AT example | `25310-1R150` | Catalog distinguishes automatic/manual applications |
| Radiator cap | `25330-1R000` | Production/build applicability must be checked |
| Radiator reservoir cap | `25440-1R000` | Reservoir component |
| Upper radiator hose | `25411-1R250` | Main hot-side radiator hose |
| Lower radiator hose | `25412-1R000` | Main return-side radiator hose |
| Cooling fan | `25231-1R390` | Electric radiator fan |
| Fan/shroud assembly | `25350-...` variants | Production-date/configuration dependent |
| Cooling-fan resistor | `25385-1M000` | Supports staged fan operation on applicable configuration |

Source:

- https://www.hyundaipartsdeal.com/parts-list/2014-hyundai-accent/engine/engine_cooling_system.html
- https://www.hyundaipartsdeal.com/parts-list/2014-hyundai-accent/engine/coolant_pump.html
- https://www.hyundaipartsdeal.com/parts-list/2014-hyundai-accent/engine/coolant_pipe_hose.html

---

# 5. Coolant Pump / Water Pump

## Function

The pump circulates coolant through the engine, heater circuit, thermostat path, and radiator.

Same-generation Hyundai service data shows this pump is mechanically driven through the accessory-belt/pulley system rather than by a standalone electric motor.

That matters diagnostically:

```text
BROKEN / SLIPPING DRIVE BELT
        ↓
REDUCED OR LOST WATER-PUMP DRIVE
        ↓
COOLANT CIRCULATION FAILURE
        ↓
RAPID OVERHEATING
```

The 2014 owner manual explicitly tells the driver to check the **water-pump drive belt** during an overheating event.

## Failure clues

Possible pump-related evidence:

- Coolant leak near pump
- Bearing growl or grinding
- Pulley wobble
- Sluggish or rough bearing feel with belt removed
- Repeated overheating despite adequate coolant
- Poor heater output combined with overheating
- Little evidence of circulation after proper warm-up

Same-generation Hyundai service data says to inspect the pump for:

- cracks/damage/wear
- bearing noise or sluggish rotation
- coolant leakage from the pump/weep area

A tiny trace of weeping at the bleed/weep hole can occur, but persistent coolant leakage indicates seal failure.

## Service-family fastener values

Same-generation Accent 1.6 L service data lists:

```text
Water-pump pulley bolts: 9.8–11.8 N·m
                         7.2–8.7 lb-ft

Water-pump mounting bolts: 9.8–11.8 N·m
                           7.2–8.7 lb-ft
```

**SERVICE-FAMILY — SAME GENERATION. Verify exact 2014 service information before critical assembly work.**

Source:

https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Engine%2C%20Cooling%20and%20Exhaust/Engine/Water%20Pump/Service%20and%20Repair/

---

# 6. Thermostat

## Function

The thermostat controls coolant flow to the radiator based on temperature.

When cold:

- radiator flow is restricted
- engine warms faster

As temperature rises:

- thermostat opens progressively
- radiator flow increases

## Failure modes

### Stuck closed / restricted

Likely pattern:

- rapid temperature rise
- radiator may remain unusually cool while engine overheats
- heater may initially be hot
- pressure can rise quickly

### Stuck open

Likely pattern:

- very slow warm-up
- weak cabin heat in cold weather
- coolant temperature may stay below expected operating range
- possible `P0128`

### Intermittent / partial opening

Can create inconsistent temperature behavior, especially under climbing, highway load, or hot-weather conditions.

## Service-family thermostat specification

Same-generation Hyundai service data for the Accent 1.6 L shows approximately:

```text
Initial valve opening: ~82°C / 180°F
Full opening:          ~95°C / 203°F
```

Treat these as **SERVICE-FAMILY — SAME GENERATION**, not exact VIN-verified 2014 shop-manual values.

Source:

https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/A%20L%20L%20%20Diagnostic%20Trouble%20Codes%20%28%20DTC%20%29/Testing%20and%20Inspection/P%20Code%20Charts/P0128/Component%20Inspection/

---

# 7. Radiator

The radiator transfers coolant heat to outside air.

The 2014 OE catalog distinguishes radiator configuration by transmission, including a specific 6AT radiator listing.

Possible radiator faults:

- external fin blockage from dust, insects, mud, leaves, or debris
- bent/crushed fins
- internal restriction
- leaking plastic tank/seam
- drain-plug leak
- hose-neck damage
- external impact from primitive-road debris

## Primitive-road importance

After dusty or muddy roads, inspect the **front airflow stack**:

```text
GRILLE
  ↓
A/C CONDENSER
  ↓
RADIATOR
```

Mud or plant matter packed into the condenser/radiator face can reduce airflow even when the fan works correctly.

Do not blast delicate fins at close range with extreme pressure.

---

# 8. Electric Cooling Fan

The radiator fan provides airflow when natural ram-air flow is insufficient.

2014 catalog data confirms:

- electric cooling fan
- fan shroud
- applicable fan resistor

Same-generation Hyundai documentation shows low/high cooling-fan relay logic.

## Pattern recognition

### Overheats at idle or in traffic, improves at speed

Strongly investigate:

- fan motor
- fan relay(s)
- fan fuse/feed
- fan resistor where equipped
- wiring/connector
- ECM command path
- ECT input plausibility

### Overheats at highway speed too

Do **not** assume fan is the main cause. At speed, airflow is already substantial.

Look harder at:

- low coolant
- thermostat restriction
- water-pump/circulation problem
- radiator restriction
- combustion-gas intrusion
- severe external blockage

## Electrical references already in this repository

See `../specs/FUSES_AND_RELAYS.md`.

Important circuit:

```text
C/FAN — 40A engine-compartment fuse
```

Fan relay/control configuration may vary by build. Use the physical fuse-box lid diagram and exact vehicle wiring where possible.

---

# 9. Engine Coolant Temperature Sensor

The ECT sensor reports coolant temperature to the ECM.

Same-generation Hyundai service information describes it as a thermistor supplied through the ECM. Its signal is used for functions including:

- fuel injection control
- ignition timing
- idle-speed strategy
- cooling-fan control

This means a bad ECT signal can create more than a temperature-display problem.

Possible consequences include:

- incorrect fan operation
- poor cold starting
- rich/lean behavior
- abnormal idle
- implausible OBD coolant data
- temperature-related DTCs such as P0115/P0116 family faults

## Plausibility test

Before cold start after sitting overnight:

```text
ECT ≈ ambient temperature
IAT ≈ ambient temperature
```

They do not need to be numerically identical, but large unexplained differences are suspicious.

As the engine warms:

- ECT should rise smoothly
- sudden jumps/dropouts suggest circuit or sensor trouble

Source:

https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/A%20L%20L%20%20Diagnostic%20Trouble%20Codes%20%28%20DTC%20%29/Testing%20and%20Inspection/P%20Code%20Charts/P0116/General%20Information/

---

# 10. Radiator Cap and System Pressure

The radiator cap is a pressure-control component, not just a lid.

Pressurizing the system raises the coolant boiling point. A cap that cannot hold pressure can contribute to:

- coolant loss
- boiling at lower-than-intended temperature
- reservoir overflow
- recurrent overheating

A cap that does not recover coolant correctly as the engine cools can also disturb system level.

## Service-family pressure test

Same-generation Hyundai data uses approximately:

```text
93–123 kPa
13.5–17.8 psi
```

for radiator-cap/system pressure testing.

**SERVICE-FAMILY — SAME GENERATION. Do not treat this as an exact 2014 VIN-specific specification without verification.**

Sources:

- https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Engine%2C%20Cooling%20and%20Exhaust/Cooling%20System/Radiator%20Cap/Testing%20and%20Inspection/
- https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Engine%2C%20Cooling%20and%20Exhaust/Cooling%20System/Radiator/Testing%20and%20Inspection/

Never remove the cap when the system is hot or pressurized.

---

# 11. Reservoir

The reservoir provides expansion volume and a visible coolant-level reference.

Hyundai's owner documentation directs the owner to monitor coolant level and add coolant to the reservoir when appropriate.

## Important interpretation

A full reservoir does **not** always prove the radiator/engine itself is full.

Possible reasons include:

- failed radiator cap recovery function
- blocked overflow hose
- trapped air
- internal pressure pushing coolant out
- leak that prevents proper vacuum recovery while cooling

If overheating occurs and the engine is fully cold, inspect the entire system rather than assuming the reservoir alone tells the whole story.

---

# 12. Heater Core as a Diagnostic Window

The heater core uses hot engine coolant to heat cabin air.

Because of that, cabin heat can reveal circulation changes.

## Useful pattern

```text
ENGINE TEMPERATURE RISING
        +
HEATER WAS HOT
        ↓
HEATER SUDDENLY GOES COLD
```

Treat this as a serious clue for:

- low coolant
- air pocket
- coolant-flow interruption
- pump/circulation failure

It does **not** identify one failed part by itself, but it raises concern that coolant may no longer be reaching the heater core properly.

---

# 13. Upper and Lower Radiator Hoses

Inspect for:

- swelling
- cracking
- soft/mushy sections
- hardened/brittle sections
- abrasion
- oil contamination
- clamp damage
- leaks at hose necks
- collapse under operating conditions

After rough-road travel, inspect for contact damage from displaced shields, debris, or loose components.

A collapsed lower hose can restrict coolant return under pump suction.

---

# 14. Coolant Type

See `../specs/FLUIDS_AND_CAPACITIES.md` for the canonical fluid specification.

2014 Hyundai guidance requires an **ethylene-glycol-based coolant suitable for aluminum engine/radiator components**.

Hyundai specifies a coolant concentration between approximately:

```text
35% minimum antifreeze
60% maximum antifreeze
```

A correct 50/50 premix is a practical field choice and avoids water-quality and mixing errors.

Do not mix random coolant chemistries merely because their colors look similar.

Color is not a chemical specification.

---

# 15. Capacity — Source Conflict Must Be Preserved

Hyundai documentation around this engine family contains inconsistent unit conversions.

The service-family source lists **5.3 L**, but nearby source text also presents conflicting US-quart conversions.

Therefore this repository does **not** use a single blindly converted quart value as the final fill instruction.

Field rule:

```text
DRAIN
  ↓
REFILL SLOWLY
  ↓
BLEED AIR CORRECTLY
  ↓
RUN / COOL / RECHECK
  ↓
FINAL LEVEL BY SYSTEM PROCEDURE
```

See `../specs/FLUIDS_AND_CAPACITIES.md` for the full source-conflict note.

---

# 16. Refilling and Bleeding

Air trapped in the cooling system can mimic or cause overheating.

Same-generation Hyundai service procedure includes:

1. Work only with engine/radiator cool.
2. Drain as required.
3. Refill slowly.
4. Compress/squeeze upper and lower hoses to help release trapped air.
5. Run engine to normal temperature.
6. Allow cooling fan to cycle multiple times.
7. Shut down and cool completely.
8. Recheck radiator/system level.
9. Refill reservoir to the correct mark.
10. Repeat until level stabilizes.
11. Recheck over the following 2–3 days after a coolant change.

This is **SERVICE-FAMILY — SAME GENERATION** procedure guidance.

Source:

https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Engine%2C%20Cooling%20and%20Exhaust/Cooling%20System/Service%20and%20Repair/

## Do not shortcut bleeding

Symptoms of trapped air can include:

- heater alternates hot/cold
- gurgling
- unstable coolant level
- temperature swings
- reservoir level changes after cooldown

---

# 17. Pressure Testing

A cooling-system pressure test can reveal leaks that are difficult to see cold and unpressurized.

Inspect while pressurized for:

- radiator seams
- hose connections
- pump leak/weep area
- thermostat housing/control assembly
- reservoir/overflow hose
- heater hoses
- engine exterior

Also inspect for:

- engine oil in coolant
- coolant contamination in engine oil

Never exceed the correct system test pressure.

Do not pressure-test a hot system.

---

# 18. Cooling-System Diagnostic Pattern Table

| Pattern | Highest-priority areas to investigate |
|---|---|
| Overheats at idle, improves at speed | Fan, relays, resistor, fan power/ground, ECT command logic, airflow blockage |
| Overheats at speed and idle | Low coolant, thermostat, pump, radiator restriction, combustion-gas intrusion |
| Heater suddenly goes cold while ECT rises | Low coolant, air pocket, circulation loss |
| Very slow warm-up / weak winter heat | Thermostat stuck open, ECT plausibility |
| Coolant pushed into/through reservoir | Overpressure, cap fault, overheating, combustion-gas intrusion |
| Repeated coolant loss with no obvious puddle | Cap/recovery fault, small hot leak, heater core, pump, internal leak |
| Sweet smell inside cabin / wet carpet / fogging | Heater-core or heater-hose leak |
| Temperature spikes after coolant service | Trapped air / incomplete bleeding |
| Overheat begins after belt problem | Verify water-pump drive immediately |
| Fan never runs | Fuse, relays, fan motor, resistor, wiring, ECT signal, ECM command |
| Fan runs constantly from cold | ECT circuit plausibility, fail-safe strategy, relay/control issue |
| Temperature normal cruising but rises climbing mountains | Cooling capacity, coolant level, radiator flow, pump/thermostat, load |

---

# 19. Head-Gasket / Internal-Leak Warning Pattern

Do not declare a head gasket failed from one symptom.

Evidence becomes more concerning when multiple signs agree:

- unexplained coolant loss
- repeated pressurization from cold start
- continuous combustion-like bubbling
- coolant expelled repeatedly
- white exhaust vapor after full warm-up beyond normal condensation
- sweet exhaust smell
- cylinder-specific misfire after sitting
- coolant-contaminated plug
- hydrocarbons/combustion gas detected in cooling system
- compression/leak-down evidence
- coolant in oil or oil in coolant

The correct sequence is:

```text
SUSPICION
  ↓
COLLECT MULTIPLE INDEPENDENT CLUES
  ↓
PRESSURE / BLOCK / COMPRESSION / LEAK-DOWN TESTING AS APPROPRIATE
  ↓
CONFIRM BEFORE MAJOR REPAIR
```

---

# 20. Emergency Overheat Logic

For full emergency steps, use `../diagnostics/OVERHEATING.md`.

Hyundai's 2014 owner procedure says:

- stop safely
- turn A/C off
- if coolant is escaping or steam is present, shut engine off
- if no steam or visible coolant loss, verify cooling-fan operation
- if the fan is not running, shut engine off
- check the water-pump drive belt
- inspect for leaks
- do not remove radiator cap while hot

Source:

https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/?srch=overheating

---

# 21. Remote / Nomad Inspection Routine

Before remote travel:

- [ ] Coolant reservoir at correct cold level
- [ ] No coolant smell
- [ ] No fresh drips
- [ ] Upper/lower hoses visually sound
- [ ] Belt visually sound
- [ ] Radiator/condenser face not packed with debris
- [ ] No unresolved overheating history
- [ ] OBD ECT behaves plausibly
- [ ] Cooling fan known to operate normally

After rough/dusty travel:

- [ ] Inspect radiator/condenser airflow path
- [ ] Inspect lower front area for impacts
- [ ] Inspect hoses and clamps
- [ ] Look for fresh coolant traces
- [ ] Recheck reservoir when fully cold

Before desert or mountain travel:

- [ ] Confirm cooling system is already healthy
- [ ] Do not begin a remote grade with known coolant loss
- [ ] Carry correct premixed coolant
- [ ] Carry clean water for emergency non-radiator uses; do not contaminate cooling system casually
- [ ] Know the nearest safe turnaround/service point

---

# 22. AI Diagnostic Rules

An AI using this document should follow these rules:

1. **Never recommend opening the radiator cap on a hot engine.**
2. Separate **airflow problems** from **coolant-flow problems**.
3. Use idle-vs-road-speed behavior as evidence, not proof.
4. A full reservoir does not prove the engine/radiator is full.
5. Do not diagnose a thermostat solely from one temperature spike.
6. If the heater suddenly goes cold during rising ECT, raise urgency.
7. If the water-pump drive belt is broken or coolant is pouring out, recommend engine shutdown.
8. Do not invent exact fan-on temperatures unless sourced for the exact configuration.
9. Do not silently resolve factory unit conflicts.
10. Treat exact torque, thermostat, pressure, and part values as VIN/build-specific unless clearly verified.
11. For internal-leak suspicion, require multiple independent pieces of evidence.
12. After coolant service, consider trapped air before condemning major components.

---

# 23. Diagnostic Decision Tree

```text
TEMPERATURE ABNORMAL
      ↓
VERIFY ACTUAL ECT / WARNING CONDITION
      ↓
CHECK COOLANT LEVEL WHEN SAFE AND COLD
      ↓
VISIBLE LEAK?
  ├─ YES → locate leak / repair / bleed
  └─ NO
      ↓
OVERHEATS MOSTLY AT IDLE?
  ├─ YES → fan / airflow / control path
  └─ NO
      ↓
OVERHEATS UNDER LOAD / AT SPEED?
  ├─ YES → thermostat / pump / radiator / low coolant / internal leak
  └─ NO
      ↓
HEATER OUTPUT ABNORMAL?
      ↓
CHECK CIRCULATION / AIR POCKET
      ↓
PRESSURE TEST / SENSOR PLAUSIBILITY / DEEPER TESTING
      ↓
REPAIR ROOT CAUSE
      ↓
BLEED
      ↓
VERIFY FAN CYCLES + ROAD TEST + COLD LEVEL RECHECK
```

---

# 24. Machine-Readable Summary

```yaml
vehicle:
  year: 2014
  make: Hyundai
  model: Accent
  trim: SE
  engine:
    family: Gamma
    displacement_l: 1.6
    induction: GDI

cooling_system:
  circulation: mechanical_belt_driven_pump
  radiator: present
  cooling_fan: electric
  thermostat: present
  reservoir: present
  heater_core: present
  ect_sensor: present

verified_2014_catalog_parts:
  coolant_pump: "25100-2B700"
  water_pump_gasket: "25124-2B000"
  water_pump_pulley: "25221-2B700"
  thermostat: "25500-2B000"
  ect_sensor: "39220-38030"
  radiator_6at_example: "25310-1R150"
  radiator_cap_example: "25330-1R000"
  upper_radiator_hose: "25411-1R250"
  lower_radiator_hose: "25412-1R000"
  cooling_fan: "25231-1R390"

service_family_reference:
  thermostat_initial_open_c: 82
  thermostat_full_open_c: 95
  radiator_cap_test_kpa:
    min: 93
    max: 123
  pump_pulley_torque_nm:
    min: 9.8
    max: 11.8
  pump_mount_torque_nm:
    min: 9.8
    max: 11.8
  confidence: "same-generation Hyundai service data; verify exact 2014 VIN/build"

coolant:
  chemistry: "ethylene-glycol based, suitable for aluminum cooling systems"
  antifreeze_percent:
    min: 35
    max: 60
  capacity_note: "Hyundai source unit conversions conflict; use proper refill/bleed/final-level procedure"

high_value_patterns:
  overheats_idle_improves_moving:
    investigate:
      - cooling_fan
      - relays
      - fan_resistor
      - wiring
      - ect_signal
      - airflow_blockage
  overheats_at_speed:
    investigate:
      - low_coolant
      - thermostat
      - water_pump
      - radiator_restriction
      - internal_leak
  heater_goes_cold_while_ect_rises:
    urgency: high
    investigate:
      - low_coolant
      - air_pocket
      - circulation_failure

safety:
  never_open_hot_radiator_cap: true
  broken_pump_drive_belt_shutdown: true
  active_major_coolant_leak_shutdown: true
```

---

# 25. Sources

## 2014 vehicle-specific

- Hyundai Accent 2014 Owner's Manual, overheating/coolant guidance:
  https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/

- 2014 Hyundai Accent Engine Cooling System OE catalog:
  https://www.hyundaipartsdeal.com/parts-list/2014-hyundai-accent/engine/engine_cooling_system.html

- 2014 Hyundai Accent Coolant Pump OE catalog:
  https://www.hyundaipartsdeal.com/parts-list/2014-hyundai-accent/engine/coolant_pump.html

- 2014 Hyundai Accent Coolant Pipe & Hose OE catalog:
  https://www.hyundaipartsdeal.com/parts-list/2014-hyundai-accent/engine/coolant_pipe_hose.html

## Same-generation Hyundai service-family references

- Cooling system refill/bleed procedure:
  https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Engine%2C%20Cooling%20and%20Exhaust/Cooling%20System/Service%20and%20Repair/

- Water pump service/inspection:
  https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Engine%2C%20Cooling%20and%20Exhaust/Engine/Water%20Pump/Service%20and%20Repair/

- Thermostat/P0128 inspection reference:
  https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/A%20L%20L%20%20Diagnostic%20Trouble%20Codes%20%28%20DTC%20%29/Testing%20and%20Inspection/P%20Code%20Charts/P0128/Component%20Inspection/

- Radiator pressure test:
  https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Engine%2C%20Cooling%20and%20Exhaust/Cooling%20System/Radiator/Testing%20and%20Inspection/

- Radiator-cap pressure test:
  https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Engine%2C%20Cooling%20and%20Exhaust/Cooling%20System/Radiator%20Cap/Testing%20and%20Inspection/

- ECT sensor description:
  https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/A%20L%20L%20%20Diagnostic%20Trouble%20Codes%20%28%20DTC%20%29/Testing%20and%20Inspection/P%20Code%20Charts/P0116/General%20Information/

---

## Repository Principle

```text
COOLING FAILURE
      ≠
THERMOSTAT FAILURE
```

The correct method is:

```text
OBSERVE → MEASURE → CLASSIFY AIRFLOW VS FLOW VS LEAK VS SENSOR → TEST → REPAIR → BLEED → VERIFY
```
