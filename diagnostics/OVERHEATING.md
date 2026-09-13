# 2014 Hyundai Accent SE — Overheating Diagnosis and Emergency Guide

> **Purpose:** Offline-first diagnosis and emergency response for overheating, coolant loss, cooling-fan failure, circulation faults, and repeated high-temperature events on a U.S.-market 2014 Hyundai Accent SE 1.6 L GDI.
>
> **Primary rule:** Overheating is not a condition to "drive through." The first objective is to prevent engine damage; diagnosis comes second.

Related files:

- `../specs/VEHICLE_BASELINE.md`
- `../specs/FLUIDS_AND_CAPACITIES.md`
- `../specs/FUSES_AND_RELAYS.md`
- `../maintenance/MAINTENANCE_SCHEDULE.md`
- `../maintenance/PRE_TRIP_INSPECTION.md`
- `OBD2_GUIDE.md`
- `CRANK_NO_START.md`

---

# 1. Factory Emergency Threshold

**VERIFIED — HYUNDAI OWNER'S MANUAL**

The 2014 Hyundai Accent owner's manual states that the engine-coolant-temperature warning light illuminates when coolant temperature exceeds approximately:

```text
257 ± 4.5°F
125 ± 2.5°C
```

Hyundai warns not to continue driving with an overheated engine because engine damage can result.

This value is an **overheat warning threshold**, not a normal operating-temperature target.

Do not invent a precise "normal" ECT value for this vehicle unless a Hyundai service specification is available. Use temperature trend, thermostat/fan behavior, ambient conditions, operating load, and verified service data together.

Primary owner-manual source:

- https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/?srch=overheating

---

# 2. Immediate Response — Hyundai Procedure

If the temperature gauge indicates overheating, power drops, or loud pinging/knocking occurs:

1. **Move off the road and stop as soon as safely possible.**
2. Put the automatic transmission in **Park**.
3. Set the parking brake.
4. Turn the air conditioning **OFF**.
5. Look for steam or coolant escaping.

## If steam is coming from under the hood or coolant is pouring out

**SHUT THE ENGINE OFF.**

Do not open the hood until steaming or heavy coolant discharge has stopped.

## If there is no steam and no visible coolant loss

Hyundai's owner procedure permits leaving the engine running briefly while checking whether the cooling fan operates.

If the cooling fan is **not operating while the engine is overheating**, shut the engine off.

## Never remove the radiator cap while hot

The cooling system is pressurized. Hot coolant can erupt from the filler neck and cause severe burns.

Wait until the engine and cooling system have cooled sufficiently before opening a pressure cap or adding coolant.

---

# 3. Hard STOP / NO-DRIVE Conditions

Shut the engine off and do not continue driving if any of the following is present:

- Steam from the hood
- Coolant visibly pouring or spraying out
- Temperature continues climbing rapidly
- Coolant warning light / severe overheat indication remains present
- Cooling fan does not operate during an active overheat condition
- Broken or missing accessory/drive belt affecting coolant circulation
- Major radiator or hose rupture
- Repeated overheating immediately after cooldown/refill
- Loud mechanical knocking associated with overheating
- Coolant contaminated with significant engine oil
- Engine oil appears heavily contaminated with coolant
- Severe loss of power accompanied by overheating
- Cylinder misfire or rough operation develops after a severe overheat
- Cooling system cannot retain coolant

A tow is cheaper than a cylinder head, catalytic converter, or engine.

---

# 4. Master Overheating Decision Tree

```text
ENGINE TEMPERATURE ABNORMAL
        ↓
Steam or active coolant loss?
   ├── YES → SHUT ENGINE OFF → cool → find leak / tow as needed
   └── NO
        ↓
Cooling fan operating during overheat?
   ├── NO → shut engine off → fuse/relay/fan/control diagnosis
   └── YES
        ↓
Coolant level low after full cooldown?
   ├── YES → locate leak / air entry / consumption cause
   └── NO
        ↓
Cabin heater output behavior?
   ├── Suddenly cold while ECT rises → circulation loss / low coolant / air pocket suspect
   └── Still hot
        ↓
Overheats mostly at idle/low speed?
   ├── YES → airflow/fan problem rises in probability
   └── NO
        ↓
Overheats mostly at highway/load?
   ├── YES → circulation / thermostat / radiator / combustion-gas issue rises
   └── NO
        ↓
Pressure test / thermostat / pump / radiator / combustion-gas diagnosis
```

This tree ranks possibilities. It does not prove a failed component by itself.

---

# 5. First Evidence to Record

Before clearing codes or disturbing the cooling system, record:

- Outside temperature
- Vehicle speed when overheating began
- Whether A/C was on
- Engine load / uphill / mountain driving
- Whether overheating occurred at idle, low speed, highway speed, or all conditions
- ECT reading from OBD-II if available
- Whether the radiator/cooling fan was running
- Whether cabin heat remained hot or suddenly became cold
- Coolant reservoir level after full cooldown
- Visible leaks
- Steam location
- Sweet coolant odor
- Recent cooling-system work
- Recent coolant top-offs
- DTCs, pending codes, and freeze-frame data
- Whether the engine began running rough or misfiring

Pattern matters enormously in overheating diagnosis.

---

# 6. Coolant Safety and Correct Fluid

See `../specs/FLUIDS_AND_CAPACITIES.md` for the repository's canonical coolant specification.

The 2014 Accent manual specifies:

- Ethylene-glycol-based coolant
- Compatible with aluminum engine/radiator components
- Deionized or soft water when dilution is required
- Antifreeze concentration between **35% and 60%**

A quality compatible **50/50 premix** is a practical field choice.

Do not mix unknown coolant chemistries merely because the colors appear similar.

Coolant color is not a reliable specification.

---

# 7. Important Capacity Warning

Hyundai's 2014 manual contains an apparent unit inconsistency for cooling-system capacity, listing:

```text
4.7 US qt (5.3 L)
```

Those values are not mathematically equivalent.

Therefore:

- Do not use that printed pair as an instruction to blindly pour a fixed quantity into an emptied system.
- Use the correct fill/bleed procedure.
- Establish the final level by the specified cold reservoir/radiator condition after air is removed.
- Recheck after full heat-up and complete cooldown.

The repository intentionally preserves this source conflict instead of silently "correcting" Hyundai's text.

---

# 8. Common Cause Families

Overheating usually belongs to one or more of these categories:

## A. Coolant quantity problem

Examples:

- Hose leak
- Radiator leak
- Reservoir leak
- Pressure-cap sealing problem
- Water-pump leak
- Heater-core leak
- Internal engine leak
- Previous service left system underfilled

## B. Airflow problem

Examples:

- Cooling fan not running
- Cooling fan running too slowly
- Fan electrical fault
- Fan relay/fuse/control problem
- Radiator/condenser externally blocked by debris

## C. Coolant-circulation problem

Examples:

- Thermostat stuck closed or not opening sufficiently
- Water-pump impeller/circulation problem
- Air pocket
- Restricted radiator
- Collapsed/restricted hose

## D. Combustion-gas / internal engine problem

Examples:

- Head-gasket leakage
- Warped/damaged cylinder head after severe overheat
- Cracked component

## E. False or misleading temperature information

Examples:

- ECT sensor/circuit problem
- Connector/wiring fault
- Scan data implausible compared with actual engine condition

Never jump directly from "overheating" to "head gasket."

---

# 9. Cooling-Fan Diagnosis

The repository's fuse reference identifies the following relevant engine-bay circuit:

```text
C/FAN — 40A
```

The 2014 fuse/relay information also identifies cooling-fan relay positions and fan-control-related feeds.

See `../specs/FUSES_AND_RELAYS.md` for the complete table and the rule that the **physical fuse-box lid on the actual car outranks the generic printed table**.

## If fan does not run during an actual overheat condition

Check logically:

1. Correct fuse(s)
2. Relevant relays
3. Fan electrical connector
4. Fan motor power and ground
5. Relay command/control
6. Wiring damage
7. ECU/temperature-input plausibility

Do not condemn the fan motor merely because it is not spinning.

```text
FAN NOT RUNNING
    ↓
FUSE POWER?
    ↓
RELAY INPUT / COMMAND?
    ↓
POWER AT FAN?
    ↓
GROUND GOOD?
    ↓
FAN MOTOR FUNCTION?
```

### Important safety rule

An electric cooling fan can start unexpectedly when the control system commands it.

Keep hands, hair, clothing, test leads, and tools away from the fan blades and belts whenever the system is energized.

---

# 10. Overheats at Idle but Improves While Driving

This pattern strongly increases suspicion of **insufficient airflow at low road speed**.

Possible causes:

- Cooling fan inoperative
- Intermittent fan
- Weak fan motor
- Relay/control fault
- Electrical voltage problem
- Debris obstructing radiator/condenser airflow

Why the pattern matters:

```text
LOW ROAD SPEED
→ little natural airflow
→ fan becomes critical

HIGHER ROAD SPEED
→ ram airflow through radiator increases
→ symptom may improve
```

This pattern is suggestive, not absolute proof of a fan problem.

---

# 11. Overheats Mainly at Highway Speed / High Load

If temperature is acceptable at idle but rises on sustained highway driving, mountain climbs, or heavy load, prioritize checks for:

- Low coolant
- Restricted coolant flow
- Thermostat not opening sufficiently
- Radiator internal restriction
- Water-pump/circulation weakness
- Collapsing/restricted hose
- Combustion-gas intrusion
- Severe external radiator blockage

A functioning fan does not rule out a cooling-system problem under load.

---

# 12. Heater Behavior as a Diagnostic Clue

The cabin heater uses engine coolant as its heat source.

## Heater remains strongly hot while engine temperature rises

Coolant is likely still circulating through at least the heater circuit.

This does not prove the entire cooling system is healthy.

## Heater suddenly turns cold while ECT climbs

Treat this as an important warning sign.

Possible causes include:

- Coolant level has fallen below the heater circuit
- Large air pocket
- Coolant circulation has stopped or become severely impaired
- Water-pump/circulation problem

If the heater suddenly goes cold **and** engine temperature is rapidly rising, do not use continued driving as a diagnostic experiment.

Stop safely and shut down as appropriate.

---

# 13. Thermostat Clues

Possible thermostat-related patterns include:

### Stuck closed / insufficient opening

- Engine warms rapidly toward overheat
- Upper/lower hose temperature pattern may be abnormal
- Highway/load overheating can occur
- Fan operation may be normal but unable to compensate for poor circulation

### Stuck open

Usually causes slow warm-up or low operating temperature rather than overheating.

Do not diagnose a thermostat solely by touching a hose with a bare hand.

Hot cooling-system components can cause burns, and hose temperature alone is imperfect evidence.

Use controlled temperature observation, scan data, infrared measurement where appropriate, and verified service procedures.

---

# 14. Water-Pump / Circulation Clues

Possible clues include:

- Coolant leak near pump area
- Bearing noise
- Repeated overheating despite adequate coolant and working fan
- Poor heater output combined with high ECT
- Circulation behavior inconsistent with thermostat state

A water pump can fail mechanically without producing an obvious external leak.

Conversely, overheating does not prove the pump has failed.

---

# 15. Radiator Problems

## External restriction

Look for:

- Leaves
- Insects
- Mud
- Dust accumulation
- Bent fins
- Debris trapped between condenser and radiator

For a primitive-camping vehicle, dust and vegetation can accumulate faster than in ordinary paved-road use.

Do not blast delicate fins with a pressure washer at close range.

## Internal restriction

Possible clues:

- Repeated overheating under load
- Uneven radiator temperature distribution
- Old/contaminated coolant history
- Cooling system otherwise appears functional

Thermal imaging or careful infrared temperature comparison can assist diagnosis, but interpretation requires context.

---

# 16. Low Coolant — Find the Reason

Coolant is not normally "used up" like gasoline.

If the level repeatedly drops, find the cause.

Inspect when fully cool:

- Reservoir and cap
- Radiator area
- Upper/lower hoses
- Hose junctions
- Thermostat housing area
- Water-pump area
- Heater hoses
- Underbody for dried coolant tracks
- Passenger compartment for heater-core clues

Dried coolant may leave crusty or colored residue even when the leak is not actively wet.

Do not keep topping up indefinitely without diagnosing repeated coolant loss.

---

# 17. Cooling-System Pressure Test

A pressure test is useful for finding leaks that may appear only when the system is pressurized.

General procedure concept:

```text
ENGINE COLD
   ↓
INSTALL CORRECT TESTER / ADAPTER
   ↓
PRESSURIZE ONLY TO VERIFIED SYSTEM LIMIT
   ↓
WATCH FOR PRESSURE LOSS
   ↓
INSPECT FOR EXTERNAL LEAKS
```

**Do not invent a pressure value.**

The exact cap/system test pressure must come from verified Hyundai service information or the correct cap specification before testing.

Never exceed the system's rated pressure.

---

# 18. Air Pockets After Cooling-System Service

Air trapped in a cooling system can cause:

- Temperature spikes
- Inconsistent heater output
- Gurgling
- Reservoir-level changes after cooldown
- Apparent intermittent overheating

Suspect trapped air especially when overheating begins immediately after:

- Coolant replacement
- Hose replacement
- Thermostat replacement
- Water-pump work
- Radiator work
- Any procedure that drained the system

Use the correct bleed/fill method. Do not assume that filling the reservoir once removes all air from the system.

---

# 19. Head-Gasket / Internal Leak Clues

No single roadside symptom proves a head-gasket failure.

Possible clues become more meaningful when several appear together:

- Repeated unexplained coolant loss
- Cooling system pressurizes unusually quickly from cold
- Persistent bubbles/combustion gas in coolant under appropriate test conditions
- White exhaust vapor after full warm-up that is abnormal for weather conditions
- Sweet exhaust odor
- Misfire after startup associated with coolant entry
- Oil/coolant contamination
- Recurrent overheating with no external leak
- Compression/leak-down abnormalities

Useful confirmatory tests may include:

- Cooling-system pressure test
- Combustion-gas/block test
- Compression test
- Cylinder leak-down test
- Borescope inspection
- Spark-plug comparison

Do not replace a head gasket based only on white vapor on a cold morning.

---

# 20. Oil and Coolant Cross-Contamination

## Suspicious coolant contamination

Watch for:

- Oil film or sludge in coolant
- Persistent contamination that returns after cleaning

## Suspicious oil contamination

Watch for:

- Milky/emulsified oil beyond ordinary condensation patterns
- Oil level inexplicably rising
- Coolant loss combined with abnormal oil appearance

Short-trip condensation under an oil cap can resemble light mayonnaise-like residue and is not, by itself, proof of coolant contamination.

Interpret all evidence together.

---

# 21. OBD-II Temperature Diagnosis

Useful PIDs include:

- Engine Coolant Temperature (ECT)
- Intake Air Temperature (IAT)
- Vehicle speed
- Engine RPM
- Calculated load
- System voltage

## Cold-soak plausibility test

After the vehicle has been parked long enough to reach ambient temperature, ECT and IAT should generally be reasonably close to ambient temperature.

If ECT reports an implausible value before startup, investigate sensor/circuit plausibility before assuming the engine is truly overheating.

Do not require ECT and IAT to match exactly. Sensor location, heat soak, and environment can create differences.

---

# 22. Relevant Diagnostic Trouble Codes

Cooling-system diagnosis may encounter generic codes such as:

- `P0115` — Engine Coolant Temperature circuit
- `P0116` — Engine Coolant Temperature range/performance
- `P0117` — Engine Coolant Temperature circuit low input
- `P0118` — Engine Coolant Temperature circuit high input
- `P0128` — Coolant thermostat / temperature below regulating temperature

A code describes a detected condition or circuit behavior.

It does **not** prove that the named sensor or thermostat itself is the failed part.

Wiring, connectors, coolant level, mechanical conditions, and system voltage can influence faults.

---

# 23. Safe Cooldown and Refill Logic

If coolant was lost but the cause is not catastrophic:

```text
STOP ENGINE IF REQUIRED
   ↓
ALLOW FULL COOL-DOWN
   ↓
VERIFY NO DANGEROUS PRESSURE
   ↓
INSPECT FOR MAJOR LEAK
   ↓
ADD CORRECT COOLANT ONLY WHEN SAFE
   ↓
START / OBSERVE
   ↓
VERIFY FAN + TEMPERATURE TREND
   ↓
RECHECK AFTER COMPLETE COOL-DOWN
```

Hyundai's owner procedure states that after the engine returns to normal temperature, lost coolant may be carefully added to the reservoir to approximately the halfway mark.

A refill is not a repair if coolant escaped because of a leak.

---

# 24. Water as Emergency Coolant

Correct coolant is strongly preferred.

If stranded in an emergency where compatible coolant is unavailable and freezing conditions are not present, plain clean water may sometimes be used temporarily to prevent operating a dry engine **only as an emergency measure**, provided the cooling system is otherwise safe to fill.

Risks of water-only operation include:

- Reduced corrosion protection
- Reduced boiling-margin performance
- No freeze protection
- Mineral deposits if poor-quality water is used

Restore the correct coolant mixture as soon as practical.

Do not add cold water to a dangerously overheated, pressurized engine.

---

# 25. Can I Drive After an Overheat?

Use a conservative decision.

## Possible short cautious movement to safety only if ALL are true

- Engine has fully cooled
- No steam
- No significant active leak
- Coolant level restored correctly
- Cooling fan functions
- Temperature remains stable during observation
- Engine runs normally
- No knocking
- No major misfire
- No oil/coolant cross-contamination clue
- Safe destination is close

Continuously monitor temperature.

## Tow / do not drive if ANY are true

- Overheat repeats
- Coolant drains out
- Fan does not operate when required
- Temperature climbs rapidly
- Severe knocking
- Engine runs badly after overheating
- Suspected belt/pump failure
- Significant internal-leak evidence
- Remote terrain would make a second failure dangerous

For remote-country travel, the threshold for choosing a tow or recovery should be lower than in town.

---

# 26. Primitive-Road / Nomad Cooling-System Checks

Before entering remote areas:

- Confirm coolant level when cold
- Inspect for old dried coolant residue
- Inspect visible hoses
- Check radiator/condenser face for blockage
- Confirm fan operation history is normal
- Check OBD-II for pending cooling-system codes
- Carry compatible premixed coolant
- Carry water separately for drinking and emergency mechanical use

After dusty or vegetation-heavy roads:

- Inspect radiator/condenser airflow path
- Look for grass, seeds, leaves, mud, and insects
- Inspect lower-front area for impact damage
- Check beneath the car for new leaks after parking

After any underbody/front-end strike, inspect for cooling-system damage before driving far from services.

---

# 27. Overheating Symptom Matrix

| Pattern | Higher-priority suspects |
|---|---|
| Overheats at idle, improves while moving | Cooling fan / airflow / fan electrical control |
| Overheats at highway speed or climbing | Coolant flow, thermostat, radiator restriction, pump, low coolant, internal leak |
| Heater suddenly goes cold as ECT rises | Low coolant, air pocket, circulation loss |
| Overheats immediately after coolant service | Air pocket / underfill / service error / leak |
| Coolant continually disappears | External leak or internal leak |
| Fan never operates during real overheat | Fuse/relay/wiring/fan/control/ECT input |
| Temperature reading implausible from cold start | ECT sensor/circuit/data plausibility problem |
| Repeated bubbling/pressure from cold | Combustion-gas intrusion becomes a concern |
| Overheat plus white exhaust and startup misfire | Internal coolant leak becomes a concern |
| Temperature rises only with A/C / low speed | Fan/airflow or marginal cooling capacity |

This matrix ranks diagnostic direction; it does not replace testing.

---

# 28. Minimum Roadside Tool Kit for Cooling Diagnosis

Useful items:

- OBD-II scanner with live ECT
- Digital multimeter
- Flashlight/headlamp
- Gloves
- Eye protection
- Compatible premixed coolant
- Funnel
- Shop towels
- Basic metric hand tools
- Inspection mirror

Useful additions:

- Infrared thermometer
- Cooling-system pressure tester with correct adapter
- Combustion-gas/block tester

Do not perform pressure-cap or pressurized-system work while the system is dangerously hot.

---

# 29. AI Diagnostic Rules

An AI assistant using this file should:

1. Treat active overheating as a potential engine-damage emergency.
2. Ask whether there is steam or active coolant loss before suggesting continued operation.
3. Distinguish idle-only overheating from highway/load overheating.
4. Ask whether the cooling fan operates.
5. Ask whether cabin heat remained hot or went cold.
6. Ask for OBD ECT when safely available.
7. Never instruct the user to remove a hot radiator cap.
8. Never assume a thermostat, water pump, fan, or head gasket has failed without tests.
9. Treat repeated coolant loss as a fault requiring explanation.
10. Preserve the Hyundai 125 ± 2.5°C warning threshold as an emergency threshold, not a normal target.
11. Do not invent Hyundai-specific pressure, thermostat-opening, or fan-command specifications.
12. Prefer towing when repeat overheating occurs in remote terrain.

---

# 30. AI Prompt Template

```text
Vehicle: 2014 Hyundai Accent SE 1.6L GDI automatic
Symptom: overheating
Outside temperature: _____
Vehicle speed when it began: _____
Road condition / hill / load: _____
A/C on: yes/no
OBD coolant temperature: _____
Temperature trend: stable / slowly rising / rapidly rising
Steam present: yes/no
Visible coolant leak: yes/no
Coolant level when fully cold: _____
Cooling fan operating: yes/no/unknown
Cabin heater output during event: hot / became cold / unknown
Stored DTCs: _____
Pending DTCs: _____
Recent cooling-system work: _____
Recent coolant addition: _____
Engine runs normally afterward: yes/no
Oil appearance: _____
Coolant appearance: _____

First determine whether the engine should remain off or whether cautious observation is safe. Then rank likely causes. Do not recommend replacing a component until you describe a test that distinguishes it from competing causes.
```

---

# 31. Incident Log Template

```markdown
## Overheating Incident

**Date:**
**Mileage:**
**Outside temperature:**
**Road / terrain:**
**Speed:**
**Engine load / grade:**
**A/C:**

### First symptom


### Highest observed ECT


### Steam?
- [ ] Yes
- [ ] No

### Visible coolant leak?
- [ ] Yes
- [ ] No

### Fan operating?
- [ ] Yes
- [ ] No
- [ ] Unknown

### Heater behavior


### Cold coolant level afterward


### DTCs / freeze frame


### Repairs / tests performed


### Root cause


### Verification after repair

```

Copy the completed event into `../maintenance/NOMAD_SERVICE_LOG.md` or cross-reference it there.

---

# 32. Machine-Readable Summary

```yaml
vehicle:
  year: 2014
  make: Hyundai
  model: Accent
  trim: SE
  engine: 1.6L GDI
  transmission: 6-speed automatic

overheating:
  hyundai_warning_threshold:
    celsius: 125
    tolerance_celsius: 2.5
    fahrenheit: 257
    tolerance_fahrenheit: 4.5
  immediate_stop_if:
    - steam
    - major_coolant_loss
    - temperature_continues_rising
    - fan_inoperative_during_overheat
    - broken_required_drive_belt
    - repeated_overheat
    - severe_knocking
  primary_cause_families:
    - coolant_loss
    - airflow_failure
    - circulation_failure
    - internal_engine_leak
    - temperature_signal_fault
  fan_circuit:
    engine_bay_fuse: C/FAN
    fuse_rating_amps: 40
  coolant:
    base: ethylene_glycol
    aluminum_compatible: true
    minimum_antifreeze_percent: 35
    maximum_antifreeze_percent: 60
    practical_premix_percent: 50
  source_conflicts:
    coolant_capacity: "Owner manual lists 4.7 US qt (5.3 L), which is internally inconsistent"
```

---

# 33. Diagnostic Doctrine

```text
HOT ENGINE
   ↓
PROTECT ENGINE FIRST
   ↓
STEAM / LEAK / FAN STATUS
   ↓
COOL SAFELY
   ↓
PRESERVE EVIDENCE
   ↓
COOLANT QUANTITY
   ↓
AIRFLOW
   ↓
CIRCULATION
   ↓
PRESSURE / INTERNAL LEAK TESTS
   ↓
ROOT CAUSE
   ↓
REPAIR
   ↓
VERIFY UNDER CONTROLLED CONDITIONS
```

Not:

```text
GAUGE HOT
   ↓
ADD WATER WHILE SCALDING HOT
   ↓
KEEP DRIVING
   ↓
HOPE
```

---

## Document Status

- **Vehicle:** 2014 Hyundai Accent SE
- **Purpose:** Overheating emergency response and diagnosis
- **Status:** Initial field diagnostic guide
- **Primary vehicle-specific source:** 2014 Hyundai Accent owner's manual
- **Factory overheat-warning threshold:** Verified from Hyundai owner documentation
- **Coolant specification:** Cross-referenced to repository fluid guide
- **Cooling fan fuse:** Cross-referenced to repository fuse guide
- **Exact pressure-test limit:** Not yet added; requires verified Hyundai service specification
- **Exact thermostat opening specification:** Not yet added; requires verified Hyundai service specification
- **Exact fan command thresholds:** Not yet added; requires verified Hyundai service specification
- **Copyright approach:** Original diagnostic documentation; does not reproduce Hyundai service-manual text
