# 2014 Hyundai Accent SE — Exhaust, Catalytic Converter & Oxygen Sensor Diagnostics

> **Purpose:** Offline-first reference for diagnosing the exhaust system, catalytic converter, upstream/downstream oxygen sensing, exhaust leaks, catalyst-efficiency faults, heater-circuit faults, sulfur/overheat symptoms, and misfire-related catalyst damage on a U.S.-market 2014 Hyundai Accent SE 1.6 L GDI.
>
> **Core rule:** An oxygen-sensor code does **not** automatically mean the oxygen sensor has failed. A sensor may be accurately reporting a mixture, exhaust, wiring, heater, or catalyst problem.

---

## 1. Vehicle Scope

Primary vehicle:

- U.S.-market 2014 Hyundai Accent SE five-door
- 1.6 L Gamma GDI inline-four
- Single cylinder bank: **Bank 1 only**
- Front/upstream heated oxygen sensor: **Bank 1 Sensor 1 (B1S1)**
- Rear/downstream heated oxygen sensor: **Bank 1 Sensor 2 (B1S2)**
- Manifold-integrated catalytic converter

Related repository files:

- `ENGINE_OVERVIEW.md`
- `MISFIRE.md`
- `FUEL_TRIM_DIAGNOSTICS.md`
- `IGNITION.md`
- `GDI_FUEL_SYSTEM.md`
- `AIR_INTAKE_THROTTLE_MAP.md`
- `WIRING_AND_CONNECTOR_DIAGNOSTICS.md`
- `ROADSIDE_DIAGNOSTIC_TRIAGE.md`

---

# 2. Confidence / Provenance Tags

This document uses these tags:

- **VERIFIED — 2014 PARTS DATA**: exact 2014 Accent catalog evidence
- **VERIFIED — 2014 OWNER MANUAL**: exact 2014 Hyundai owner documentation
- **CORROBORATED — SAME ENGINE / SERVICE FAMILY**: nearby-year Accent or same 1.6 GDI Hyundai service information
- **GENERAL DIAGNOSTIC PRACTICE**: accepted diagnostic method, not a Hyundai-specific specification
- **UNKNOWN**: not yet verified closely enough to publish as a number or exact 2014 specification

Unknown is preferable to a confident wrong answer.

---

# 3. Hardware Architecture

## 3.1 Exhaust manifold and catalyst

**VERIFIED — 2014 PARTS DATA**

The 2014 Accent 1.6 GDI catalog identifies the exhaust manifold/catalyst as a combined assembly:

```text
Exhaust manifold + catalytic converter
OEM assembly: 28510-2BEF1
```

The catalyst is integrated into the manifold assembly rather than being treated as a casually separable insert.

Source:

- https://www.hyundaipartsdeal.com/parts-list/2014-hyundai-accent/engine/exhaust_manifold.html
- https://www.hyundaipartsdeal.com/genuine/hyundai-manifold-catalytic-a~28510-2bef1.html

## 3.2 Oxygen sensors

**VERIFIED — 2014 PARTS DATA**

The 2014 catalog lists two oxygen sensors:

```text
Front / upstream sensor:
39210-2B210

Rear / downstream sensor:
39210-2B220
```

Always VIN-check before purchase because catalog supersessions and emissions-package differences can exist.

Source:

- https://www.hyundaipartsdeal.com/oem-2014-hyundai-accent-oxygen_sensor.html

## 3.3 Sensor type

**CORROBORATED — SAME ENGINE / SERVICE FAMILY**

Same-generation Gamma 1.6 GDI Hyundai service data identifies:

```text
B1S1 / front HO2S:
zirconia linear type

B1S2 / rear HO2S:
zirconia binary type
```

This is an important distinction. Do not treat the upstream linear sensor as if it were an old-school narrowband sensor whose only useful interpretation is simple 0.1–0.9 V switching.

Source:

- https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Powertrain%20Management/Specifications/

---

# 4. What Each Sensor Does

## Upstream B1S1

Primary jobs:

- Measures exhaust oxygen before the catalyst
- Provides mixture feedback to the ECM
- Supports closed-loop air/fuel control
- Helps the ECM correct fueling

A B1S1 problem may affect:

- STFT / LTFT
- fuel economy
- idle quality
- emissions
- drivability
- catalyst loading

## Downstream B1S2

Primary jobs:

- Measures oxygen after the catalyst
- Helps the ECM evaluate catalyst oxygen-storage/conversion behavior
- Participates in catalyst-monitor logic

Same-engine Hyundai diagnostic information states that the front sensor is used for air/fuel control while the rear sensor is used to monitor the front sensor and catalyst operation.

Source:

- https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/A%20L%20L%20%20Diagnostic%20Trouble%20Codes%20%28%20DTC%20%29/Testing%20and%20Inspection/P%20Code%20Charts/P0038/General%20Information/

---

# 5. Heater Circuits

Both sensors are heated so they can reach useful operating temperature faster.

Same-generation Hyundai service information describes the heater strategy as:

```text
main relay supplies heater voltage
ECM controls the heater ground/duty cycle
```

Therefore a heater DTC does not automatically prove the sensing element itself is bad.

Possible heater-fault causes include:

- open heater element
- shorted heater element
- blown fuse/shared power problem
- relay/power-feed problem
- open or high-resistance wiring
- short-to-ground
- short-to-power
- connector corrosion
- ECM driver/control issue

Relevant code families may include:

```text
P0030 / P0031 / P0032 — upstream heater family
P0036 / P0037 / P0038 — downstream heater family
P0135 — B1S1 heater family
P0141 — B1S2 heater family
```

Code support and naming should always be confirmed with the actual scan tool/service data for the vehicle.

---

# 6. Sensor Installation / Handling

**CORROBORATED — SAME ENGINE / SERVICE FAMILY**

Same-generation Accent service data gives heated oxygen-sensor installation torque:

```text
39.2–49.1 N·m
28.9–36.2 lb-ft
```

Source:

- https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Powertrain%20Management/Computers%20and%20Control%20Systems/Sensors%20and%20Switches%20-%20Computers%20and%20Control%20Systems/Oxygen%20Sensor/Service%20and%20Repair/

Hyundai also warns:

- Do not contaminate the sensing element or connector with cleaner, spray, or grease.
- Do not allow sensor wiring to contact the hot exhaust system.
- A dropped sensor may be internally damaged even if it looks intact.

Treat these as service-family rules pending exact 2014 shop-manual confirmation.

---

# 7. Catalyst Function

**CORROBORATED — SAME ENGINE / SERVICE FAMILY**

Hyundai describes the gasoline catalytic converter as a three-way catalyst that reduces:

- hydrocarbons (HC)
- carbon monoxide (CO)
- oxides of nitrogen (NOx)

The catalyst also stores/release oxygen as part of the chemistry used by the ECM to evaluate catalyst efficiency.

Source:

- https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Powertrain%20Management/Emission%20Control%20Systems/Catalytic%20Converter/Description%20and%20Operation/

---

# 8. Catalyst Heat Is a Safety Issue

**VERIFIED — 2014 OWNER MANUAL**

Hyundai warns that the exhaust and catalyst become extremely hot and can ignite combustible material under the vehicle.

Do not park, idle, or drive over:

- dry grass
- leaves
- paper
- vegetation
- other combustible debris

Hyundai also warns not to operate the vehicle with obvious engine malfunction such as misfire or noticeable power loss because catalyst damage can result.

Source:

- https://manuals.plus/m/28181eb364b39dbbb16f909d42f8e060859e68749899494eb6c5fca29f35b8b1

**CORROBORATED — HYUNDAI SERVICE SAFETY**

Hyundai service information notes catalyst temperatures can exceed approximately:

```text
537°C / 1000°F
```

This is a burn and fire hazard.

Source:

- https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Powertrain%20Management/Fuel%20Delivery%20and%20Air%20Induction/Service%20Precautions/Fuel%20System%20Safety%20Precautions/

---

# 9. Misfire and Catalyst Damage

**VERIFIED — 2014 OWNER MANUAL**

Hyundai specifically warns that:

- Very low fuel can cause misfire and catalyst damage.
- Driving with an illuminated or blinking MIL may risk catalyst damage.
- Misfire or noticeable performance loss should not be ignored.

Source:

- https://manualzz.com/doc/53857913/hyundai-2014-accent-owner-manual
- https://www.dezosmanuals.com/wp-content/uploads/2021/07/2014-Hyundai-Accent-OM.pdf

Why severe misfire is dangerous:

```text
MISFIRE
  ↓
unburned fuel + oxygen enter catalyst
  ↓
oxidation occurs inside catalyst
  ↓
very high catalyst temperature
  ↓
substrate can melt / crack / collapse
  ↓
exhaust restriction and permanent catalyst damage
```

If the MIL is flashing and the engine is misfiring severely, reduce load and stop driving as soon as safely possible.

See `../diagnostics/MISFIRE.md`.

---

# 10. P0420 Is Not Automatically “Buy a Catalyst”

P0420 means the ECM has judged catalyst efficiency below its calibrated threshold.

The ECM does this by comparing upstream and downstream oxygen-sensor behavior under specific monitor conditions.

A healthy catalyst generally smooths oxygen fluctuations downstream.

If downstream activity increasingly resembles upstream activity, catalyst oxygen-storage/conversion performance may be reduced.

However, before condemning the catalyst, investigate:

- active or historical misfire
- rich operation
- lean operation
- oil burning
- coolant entering combustion
- exhaust leaks
- upstream sensor bias
- downstream sensor bias
- heater faults
- wiring faults
- sensor contamination
- incorrect/non-OE catalyst
- physical catalyst damage

Same-GDI-engine Hyundai P0420 diagnostic information specifically instructs technicians to check for exhaust leakage near the HO2S/catalyst and inspect the rear sensor and catalyst for damage, overheating discoloration, cracks, noise, or incorrect parts.

Source:

- https://charm.li/Hyundai/2012/Veloster%20L4-1.6L/Repair%20and%20Diagnosis/A%20L%20L%20%20Diagnostic%20Trouble%20Codes%20%28%20DTC%20%29/Testing%20and%20Inspection/P%20Code%20Charts/P0420/System%20Inspection/
- https://charm.li/Hyundai/2012/Veloster%20L4-1.6L/Repair%20and%20Diagnosis/A%20L%20L%20%20Diagnostic%20Trouble%20Codes%20%28%20DTC%20%29/Testing%20and%20Inspection/P%20Code%20Charts/P0420/Component%20Inspection/

---

# 11. Exhaust Leaks Can Fool Oxygen-Sensor Diagnostics

An exhaust leak can change sensor readings even when the sensor itself is healthy.

Potential leak points include:

- manifold gasket
- manifold/catalyst cracks
- sensor threads/bungs
- manifold-to-front-pipe connection
- pipe flanges
- flex section
- damaged pipe

A leak upstream of or near an oxygen sensor can introduce outside air and create misleading lean/oxygen readings.

Before replacing a sensor for implausible lean behavior, inspect for:

- ticking on cold start
- black soot around joints
- loose hardware
- damaged gaskets
- visible cracks
- exhaust odor in engine bay
- noise that changes as parts heat and expand

---

# 12. Upstream Sensor Diagnosis

## Common symptom patterns

Possible B1S1-related symptoms:

- poor fuel economy
- unstable fuel trims
- hesitation
- rough idle
- emissions codes
- mixture-control codes
- slow closed-loop entry

But these symptoms can also be caused by:

- vacuum leak
- PCV fault
- EVAP purge fault
- injector fault
- GDI pressure problem
- MAP/IAT error
- ignition misfire
- exhaust leak

### Rule

```text
UPSTREAM O2 CODE
      ≠
BAD UPSTREAM O2 SENSOR
```

Use sensor data together with:

- STFT
- LTFT
- MAP
- IAT
- ECT
- RPM/load
- misfire counters if available
- fuel-pressure data

See `../diagnostics/FUEL_TRIM_DIAGNOSTICS.md`.

---

# 13. Downstream Sensor Diagnosis

The downstream sensor primarily observes catalyst output.

Same-engine Hyundai service data explains that a healthy catalyst smooths oxygen fluctuations so B1S2 normally has less amplitude/activity than the upstream sensor.

If the catalyst loses oxygen-storage capability due to aging, poisoning, overheating, or misfire damage, downstream activity may begin to resemble upstream activity.

Source:

- https://charm.li/Hyundai/2012/Veloster%20L4-1.6L/Repair%20and%20Diagnosis/A%20L%20L%20%20Diagnostic%20Trouble%20Codes%20%28%20DTC%20%29/Testing%20and%20Inspection/P%20Code%20Charts/P2271/General%20Information/

Do not use one idle screenshot to condemn a catalyst.

Catalyst monitoring depends on:

- full operating temperature
- closed-loop control
- monitor enable conditions
- stable sensor heaters
- absence of interfering faults

---

# 14. P013x / Sensor Circuit Logic

A sensor-circuit DTC can represent:

- open signal wire
- short to ground
- short to voltage
- high resistance
- bad sensor ground/reference
- failed heater
- failed sensing element
- connector contamination/corrosion
- harness heat damage
- exhaust leak producing implausible data

For downstream sensor codes in particular, same-GDI-engine Hyundai documentation warns that heater-circuit faults can sometimes contribute to signal-code diagnosis, so heater operation should not be ignored.

Source:

- https://charm.li/Hyundai/2012/Veloster%20L4-1.6L/Repair%20and%20Diagnosis/A%20L%20L%20%20Diagnostic%20Trouble%20Codes%20%28%20DTC%20%29/Testing%20and%20Inspection/P%20Code%20Charts/P0138/General%20Information/
- https://charm.li/Hyundai/2012/Veloster%20L4-1.6L/Repair%20and%20Diagnosis/A%20L%20L%20%20Diagnostic%20Trouble%20Codes%20%28%20DTC%20%29/Testing%20and%20Inspection/P%20Code%20Charts/P0136/General%20Information/

---

# 15. Catalyst Damage Patterns

## Overheating / melted substrate

Possible causes:

- prolonged severe misfire
- excessively rich mixture
- leaking injector
- ignition failure
- repeated failed start attempts with fuel entering exhaust

Possible symptoms:

- major power loss under load
- exhaust glowing unusually hot
- sulfur/hot-metal smell
- rattling substrate
- restriction that worsens with RPM/load

## Poisoning / contamination

Possible contributors:

- sustained oil burning
- coolant burning
- inappropriate chemical contamination

## Physical damage

Possible causes:

- road impact
- underbody strike
- severe thermal shock
- internal substrate breakup

Nomad use increases the importance of post-impact inspection because the Accent has limited ground clearance.

---

# 16. Restricted Catalyst / Exhaust

A physically restricted exhaust can create:

- poor acceleration
- inability to rev freely under load
- excessive exhaust-manifold heat
- high engine load for a given performance level
- worsening power loss as RPM rises

Possible confirmation methods include:

- exhaust backpressure measurement with proper equipment
- intake-vacuum behavior on engines/procedures where applicable
- comparing engine behavior before/after professionally verified exhaust testing
- temperature/thermal pattern assessment by a trained technician

Do not casually remove an oxygen sensor and drive around as a “backpressure test.” Hot exhaust exiting the sensor port can damage wiring, components, or people.

---

# 17. Sulfur / Rotten-Egg Smell

A sulfur smell can be associated with unusual catalyst chemistry, rich operation, fuel composition, or catalyst overload.

Do not diagnose the catalyst by smell alone.

Check:

- active misfire
- fuel trims
- injector leakage
- GDI rail/control faults
- oxygen sensor plausibility
- catalyst temperature symptoms
- fuel quality

A strong sulfur smell plus loss of power, extreme heat, or a flashing MIL deserves immediate attention.

---

# 18. Sensor Contamination

Sensor response may be harmed by contamination from:

- oil burning
- coolant burning
- silicone-containing products
- unsuitable sprays/grease on the sensor element
- severe rich operation and deposits

If a contaminated sensor is found, diagnose **why it became contaminated** before simply installing another one.

Example:

```text
OIL-CONTAMINATED HO2S
       ↓
WHY IS OIL REACHING EXHAUST?
       ↓
PCV / rings / valve seals /
internal engine condition
```

---

# 19. Electrical Testing Workflow

## Heater-code workflow

```text
HEATER DTC
   ↓
VERIFY BATTERY / CHARGING VOLTAGE
   ↓
CHECK RELATED FUSE / RELAY POWER
   ↓
CHECK SENSOR CONNECTOR
   ↓
VERIFY HEATER POWER WITH CIRCUIT ACTIVE
   ↓
VERIFY ECM-CONTROLLED GROUND SIDE
   ↓
CHECK HEATER RESISTANCE AGAINST EXACT SPEC
   ↓
ISOLATE SENSOR VS HARNESS VS CONTROL
```

Exact 2014 heater-resistance specifications remain **UNKNOWN** until a readable authoritative 2014 specification is sourced.

Do not invent resistance numbers from adjacent models.

## Signal-code workflow

```text
SIGNAL DTC
   ↓
PRESERVE FREEZE FRAME
   ↓
CHECK HEATER DTCs
   ↓
CHECK CONNECTOR / HARNESS
   ↓
CHECK EXHAUST LEAKS
   ↓
COMPARE SENSOR DATA TO ENGINE CONDITION
   ↓
FORCE / OBSERVE CONTROLLED RICH-LEAN RESPONSE
   ↓
ONLY THEN CONDEMN SENSOR
```

---

# 20. Wiring Heat-Damage Inspection

Oxygen-sensor wiring lives in one of the hottest environments on the car.

Inspect for:

- melted loom
- hardened insulation
- wiring contacting manifold/catalyst
- missing clips/brackets
- pulled terminals
- corrosion
- previous poor splices
- road-debris damage underneath

Hyundai specifically warns that sensor/wiring contact with exhaust components can damage the sensor or harness.

---

# 21. Roadside / Remote-Country Decision Rules

## STOP / DO NOT CONTINUE DRIVING

- flashing MIL with severe misfire
- glowing red exhaust/catalyst
- smoke or fire risk beneath vehicle
- dramatic power loss with suspected blocked catalyst
- exhaust component hanging low enough to strike road
- exhaust entering passenger compartment
- fuel leak

## CAUTION / SHORT DISTANCE ONLY AFTER ASSESSMENT

- steady MIL with otherwise normal operation
- known downstream O2 heater fault without drivability symptoms
- minor exhaust rattle with secure hardware and no leak into cabin

A steady MIL is not permission to ignore the car indefinitely.

---

# 22. Carbon Monoxide Safety

Exhaust contains carbon monoxide.

Never:

- sleep in the car with the engine running
- idle for long periods in enclosed or partially enclosed spaces
- ignore an exhaust leak beneath or near the cabin
- assume an odorless cabin means CO is absent

If exhaust intrusion is suspected, ventilate, shut the engine off when safe, and repair the leak before using the vehicle as sleeping shelter.

---

# 23. After an Underbody Impact

After striking a rut, rock, stump, road debris, or high center:

1. Stop safely.
2. Inspect exhaust pipes and hangers.
3. Look for crushed pipe sections.
4. Check sensor wiring.
5. Look for fresh dents around the catalyst/manifold area.
6. Check for new rattles.
7. Verify nothing is touching plastic, fuel/brake lines, or body panels.
8. Recheck after the next heat cycle.

A dented pipe can restrict flow even if it does not leak.

---

# 24. Diagnostic Pattern Matrix

| Symptom | Higher-priority possibilities |
|---|---|
| P0420 only | catalyst efficiency, exhaust leak, rear sensor bias, prior misfire/rich damage |
| Upstream sensor code + fuel trim issue | B1S1 circuit, exhaust leak, fueling/air problem, MAP/IAT, PCV, EVAP |
| Downstream heater code | heater element, power feed, ECM ground control, harness/connector |
| Flashing MIL + sulfur/hot smell | severe misfire, catalyst overheating |
| Rattle inside catalyst | fractured substrate |
| Power falls off badly at higher load | exhaust restriction/catalyst collapse, fuel/ignition issues |
| Code appeared after underbody strike | harness, sensor, pipe/catalyst physical damage |
| Multiple O2/heater codes after voltage event | charging voltage, shared power, grounds, relay/fuse path |

---

# 25. Parts-Cannon Prevention

Do **not** automatically replace:

- B1S1 for a lean code
- B1S2 for P0420
- the catalyst because B1S2 moves
- both O2 sensors because one heater code exists
- the catalyst before fixing active misfire/rich operation

A new catalyst installed behind an unresolved misfire can be destroyed too.

---

# 26. AI / RAG Rules

An AI using this file should:

1. Identify whether the problem is **sensor, heater, mixture, exhaust leak, catalyst, or wiring** before naming a part.
2. Treat B1S1 and B1S2 as different diagnostic roles.
3. Remember the upstream sensor is a **linear zirconia type** in same-engine service data.
4. Never interpret the upstream sensor only as a simple narrowband 0–1 V switch.
5. Check active misfire before condemning a catalyst.
6. Check exhaust leaks before condemning an O2 sensor or catalyst.
7. Treat P0420 as a **system-efficiency judgment**, not a direct catalyst-part failure code.
8. Check sensor-heater circuits before condemning sensor signal behavior when heater DTCs coexist.
9. Verify system voltage early when multiple electrical codes appear together.
10. Never tell the user to drive with a flashing MIL and severe misfire.
11. Never recommend sleeping in the vehicle with the engine running.
12. Do not invent exact heater resistance, waveform thresholds, or 2014-specific catalyst efficiency limits.
13. Use exact 2014 part numbers only as catalog anchors, and still VIN-check before purchase.
14. After repair, clear codes only after evidence has been recorded, then complete an appropriate drive/monitor verification.

---

# 27. Core Diagnostic Flow

```text
MIL / O2 / CATALYST SYMPTOM
          ↓
PRESERVE DTC + FREEZE FRAME
          ↓
FLASHING MIL / SEVERE MISFIRE?
    ├─ YES → STOP LOAD / DIAGNOSE MISFIRE FIRST
    └─ NO
          ↓
VERIFY SYSTEM VOLTAGE
          ↓
CHECK EXHAUST LEAKS + PHYSICAL DAMAGE
          ↓
CLASSIFY:
B1S1 / B1S2 / HEATER / P0420 / RESTRICTION
          ↓
COMPARE SENSOR DATA TO ACTUAL ENGINE CONDITION
          ↓
CHECK WIRING + HEATER + FUEL TRIMS + MISFIRE HISTORY
          ↓
ONLY THEN CONDEMN SENSOR OR CATALYST
          ↓
REPAIR ROOT CAUSE
          ↓
VERIFY MONITORS / HOT OPERATION / ROAD TEST
```

---

# 28. Known Exact / Corroborated Values

```yaml
vehicle:
  year: 2014
  model: Hyundai Accent SE
  engine: 1.6L Gamma GDI
  bank_count: 1

oxygen_sensors:
  front:
    location: Bank 1 Sensor 1
    oe_part_number: 39210-2B210
    source_confidence: VERIFIED_2014_PARTS_DATA
    service_family_type: zirconia_linear
  rear:
    location: Bank 1 Sensor 2
    oe_part_number: 39210-2B220
    source_confidence: VERIFIED_2014_PARTS_DATA
    service_family_type: zirconia_binary

catalyst:
  manifold_integrated: true
  oe_manifold_catalyst_assembly: 28510-2BEF1
  source_confidence: VERIFIED_2014_PARTS_DATA

service_family_specs:
  oxygen_sensor_install_torque:
    nm_min: 39.2
    nm_max: 49.1
    lbft_min: 28.9
    lbft_max: 36.2
    source_confidence: SAME_ENGINE_SERVICE_FAMILY
  catalyst_temperature_warning_reference:
    celsius_above: 537
    fahrenheit_above: 1000
    source_confidence: HYUNDAI_SERVICE_SAFETY_REFERENCE

unknown_exact_2014:
  - oxygen_sensor_heater_resistance
  - exact_sensor_signal_voltage_thresholds
  - exact_P0420_enable_conditions
  - exact_catalyst_efficiency_threshold
  - exact_exhaust_backpressure_limit
```

---

# 29. Sources

Primary / exact 2014 sources:

- Hyundai 2014 Accent owner manual mirror: https://manualzz.com/doc/53857913/hyundai-2014-accent-owner-manual
- Hyundai 2014 Accent owner manual PDF mirror: https://www.dezosmanuals.com/wp-content/uploads/2021/07/2014-Hyundai-Accent-OM.pdf
- 2014 Accent oxygen-sensor catalog: https://www.hyundaipartsdeal.com/oem-2014-hyundai-accent-oxygen_sensor.html
- 2014 Accent exhaust-manifold catalog: https://www.hyundaipartsdeal.com/parts-list/2014-hyundai-accent/engine/exhaust_manifold.html

Same-generation / same-engine supporting service information:

- 2012 Accent HO2S specifications: https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Powertrain%20Management/Specifications/
- 2012 Accent oxygen-sensor service: https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Powertrain%20Management/Computers%20and%20Control%20Systems/Sensors%20and%20Switches%20-%20Computers%20and%20Control%20Systems/Oxygen%20Sensor/Service%20and%20Repair/
- 2012 Accent catalyst description: https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Powertrain%20Management/Emission%20Control%20Systems/Catalytic%20Converter/Description%20and%20Operation/
- 2012 Veloster 1.6 GDI P0420 system inspection: https://charm.li/Hyundai/2012/Veloster%20L4-1.6L/Repair%20and%20Diagnosis/A%20L%20L%20%20Diagnostic%20Trouble%20Codes%20%28%20DTC%20%29/Testing%20and%20Inspection/P%20Code%20Charts/P0420/System%20Inspection/
- 2012 Veloster 1.6 GDI P0420 component inspection: https://charm.li/Hyundai/2012/Veloster%20L4-1.6L/Repair%20and%20Diagnosis/A%20L%20L%20%20Diagnostic%20Trouble%20Codes%20%28%20DTC%20%29/Testing%20and%20Inspection/P%20Code%20Charts/P0420/Component%20Inspection/
- 2012 Veloster 1.6 GDI rear-HO2S/catalyst behavior: https://charm.li/Hyundai/2012/Veloster%20L4-1.6L/Repair%20and%20Diagnosis/A%20L%20L%20%20Diagnostic%20Trouble%20Codes%20%28%20DTC%20%29/Testing%20and%20Inspection/P%20Code%20Charts/P2271/General%20Information/

---

## Final Principle

```text
OXYGEN SENSOR DATA
        ≠
OXYGEN SENSOR FAILURE

CATALYST CODE
        ≠
AUTOMATIC CATALYST REPLACEMENT

OBSERVE → VERIFY ENGINE CONDITION → CHECK LEAKS → CHECK WIRING/HEATERS → COMPARE SENSOR BEHAVIOR → REPAIR ROOT CAUSE → VERIFY
```
