# 2014 Hyundai Accent SE — Accessory Drive Belt

> **Purpose:** Offline-first field and service reference for the accessory drive system on a U.S.-market 2014 Hyundai Accent SE 5-door with the 1.6 L Gamma GDI engine.
>
> **Core rule:** A drive-belt problem can simultaneously become a **cooling-system problem and a charging-system problem**. If the belt that drives the water pump is broken or missing, **stop the engine**.

---

## 1. Scope

This guide covers:

- V-ribbed accessory drive belt
- Crankshaft pulley / damper
- Water-pump pulley
- Alternator pulley and alternator mounting/adjustment
- Drive-belt idler
- A/C compressor drive load where equipped
- Belt tension and alignment
- Belt wear, cracking, glazing, fraying, contamination, chirp, squeal and slap
- Idler, alternator, water-pump and A/C pulley/bearing faults
- Charging and overheating consequences of belt failure
- Roadside triage
- Post-repair verification

Related repository files:

- `COOLING_SYSTEM.md`
- `LUBRICATION_SYSTEM.md`
- `../diagnostics/OVERHEATING.md`
- `../diagnostics/CHARGING_SYSTEM.md`
- `../electrical/BATTERY_STARTER_ALTERNATOR.md`
- `../roadside/EMERGENCY_FIELD_REPAIRS.md`
- `../maintenance/MAINTENANCE_SCHEDULE.md`
- `../specs/TORQUE_SPECS.md`

---

# 2. Source Confidence Tags

Use these tags throughout this document:

- **VERIFIED — 2014 OWNER MANUAL**: exact model-year Hyundai owner documentation.
- **VERIFIED — 2014 PARTS CATALOG**: 2014 Accent OE parts-catalog evidence.
- **SERVICE-FAMILY — 2012/2013 ACCENT 1.6 GDI**: same-generation / same-engine service information used as supporting data pending exact 2014 workshop confirmation.
- **GENERAL DIAGNOSTIC PRACTICE**: broadly accepted mechanical diagnosis, not a Hyundai-specific specification.
- **UNKNOWN**: exact 2014 value or detail has not yet been verified.

When exact 2014 guidance conflicts with adjacent-year service-family information, **the exact 2014 source wins**.

---

# 3. Verified 2014 Hardware

## 3.1 Water pump and belt-drive hardware

**VERIFIED — 2014 PARTS CATALOG**

The 2014 Accent 1.6 L Gamma GDI coolant-pump catalog shows:

| Part | OE catalog reference |
|---|---|
| Water-pump assembly | `25100-2B700` |
| Water-pump pulley | `25221-2B700` |
| Drive-belt idler | `25286-2B010` |
| V-ribbed belt option | `25212-2B020` |
| V-ribbed belt option | `25212-2B030` |

The belt entries are production/configuration dependent. **Do not order solely by this table. Verify VIN, installed belt, build date and A/C configuration.**

Source:

- https://www.hyundaipartsdeal.com/parts-list/2014-hyundai-accent/engine/coolant_pump.html

The same catalog page lists both belt choices during 2014 production, including overlapping production windows. That is strong evidence that **VIN/build configuration matters**.

---

# 4. System Architecture

## 4.1 Belt-driven functions

Same-generation Gamma 1.6 service information shows a V-ribbed drive belt routed through the accessory system and tensioned by alternator adjustment, with different routing diagrams for vehicles **with A/C** and **without A/C**.

**SERVICE-FAMILY — 2012/2013 ACCENT 1.6 GDI**

The system includes at minimum:

```text
CRANKSHAFT PULLEY
        ↓
V-RIBBED DRIVE BELT
        ↓
WATER PUMP
ALTERNATOR
DRIVE-BELT IDLER
A/C COMPRESSOR (when equipped / in routing path)
```

This Accent uses **MDPS electric power steering**, so there is no hydraulic power-steering pump belt in the 2014 SE configuration.

### Important consequence

A thrown or broken accessory belt can cause:

```text
BELT FAILURE
    ↓
WATER PUMP STOPS / LOSES DRIVE
    ↓
COOLANT CIRCULATION FAILS
    ↓
ENGINE OVERHEATS
```

and simultaneously:

```text
BELT FAILURE
    ↓
ALTERNATOR STOPS
    ↓
BATTERY / CHARGING WARNING
    ↓
VEHICLE RUNS ON BATTERY ONLY
    ↓
SYSTEM VOLTAGE EVENTUALLY COLLAPSES
```

If the A/C compressor is belt-driven in the installed routing, A/C operation is also lost.

---

# 5. Hyundai's Emergency Rule

**VERIFIED — 2014 OWNER MANUAL**

Hyundai's exact 2014 overheating procedure says to check whether the **water-pump drive belt is missing**, verify that it is tight if present, and:

> If the water-pump drive belt is broken or engine coolant is leaking out, stop the engine immediately.

Source:

- https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/?srch=overheating

Therefore:

```text
BROKEN / MISSING WATER-PUMP DRIVE BELT
                 ↓
             STOP ENGINE
                 ↓
             DO NOT LIMP
                 ↓
      REPAIR OR RECOVER VEHICLE
```

A few more miles can turn a belt replacement into a cylinder-head or complete-engine repair.

---

# 6. Maintenance Interval

**VERIFIED — 2014 OWNER MANUAL**

Hyundai specifies:

```text
Drive belt:
First inspection: 60,000 mi / 96,000 km or 72 months
Then inspect every: 15,000 mi / 24,000 km or 24 months
```

Hyundai also says the drive belt should be replaced when:

- Cracks occur
- Tension becomes excessively reduced

Source:

- https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/33

The 2014 Quick Reference Guide independently repeats the same inspection schedule.

Source:

- https://www.carmanualsonline.info/hyundai-accent-2014-quick-reference-guide/?srch=belt

### Source conflict preserved

Older same-generation service text says some small rib-side cracks may be acceptable if no rib chunks are missing.

However, the exact 2014 owner manual says to replace the belt when cracks occur.

Repository rule:

> **For this 2014 vehicle, use the exact 2014 owner-manual guidance. Cracking moves the belt into the replacement category.**

---

# 7. Belt Tension

## 7.1 Same-generation factory-family values

**SERVICE-FAMILY — 2012/2013 ACCENT 1.6 GDI**

Hyundai service information specifies measured belt tension of approximately:

```text
NEW BELT:
882.6–980.7 N
90–100 kgf
198.4–220.5 lbf

USED BELT:
637.4–735.5 N
65–75 kgf
143.3–165.3 lbf
```

If the engine has run for five minutes or more, Hyundai says to treat the belt as a **used belt** for tension adjustment.

Source:

- https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Starting%20and%20Charging/Charging%20System/Testing%20and%20Inspection/Component%20Tests%20and%20General%20Diagnostics/

### Adjustment architecture

Same-generation service information describes:

1. Loosen alternator mounting bolts.
2. Use the alternator adjusting bolt to change tension.
3. Recheck belt tension.
4. Tighten through/mounting bolts after adjustment.

This is **not** an automatic spring-tensioner procedure.

### Important

Hyundai warns:

```text
TOO LOOSE
→ belt slip / squeal / poor accessory drive

TOO TIGHT
→ alternator-bearing damage
→ water-pump-bearing damage
```

Tighter is **not** automatically better.

---

# 8. Same-Family Fastener References

**SERVICE-FAMILY — 2012/2013 ACCENT 1.6 GDI**

| Fastener / component | Torque |
|---|---:|
| Water-pump pulley bolts | 9.8–11.8 N·m / 7.2–8.7 lb-ft |
| Drive-belt idler | 42.2–53.9 N·m / 31.1–39.8 lb-ft |
| Alternator M8 mounting bolt | 19.6–26.5 N·m / 14.5–19.5 lb-ft |
| Alternator M10 mounting bolt | 29.4–41.2 N·m / 21.7–30.4 lb-ft |
| Crankshaft pulley bolt | 127.5–137.3 N·m / 94.0–101.3 lb-ft |

Source:

- https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Engine%2C%20Cooling%20and%20Exhaust/Engine/Timing%20Components/Timing%20Chain/Service%20and%20Repair/Repair%20Procedures/Part%202/

These values are useful supporting data but remain tagged **SERVICE-FAMILY** until an exact 2014 service procedure is obtained.

---

# 9. Inspection Procedure

## Engine OFF inspection

Do not put hands, clothing, hair or tools near the belt while the engine is running.

Hyundai explicitly warns to keep hair, hands and clothing away from moving fans and drive belts.

### Inspect the belt for

- Cracks
- Missing rib material
- Frayed cords
- Shredded edges
- Polished/glazed surface
- Embedded debris
- Oil saturation
- Coolant contamination
- Uneven rib wear
- Transverse splits
- Belt riding off-center
- Rubber dust around pulleys
- Sections that appear stretched or narrowed

### Inspect pulleys for

- Bent pulley flanges
- Wobble
- Rust or debris packed into grooves
- Damaged ribs
- Misalignment
- Bearing roughness
- Side play
- Seized or sticky rotation

### Inspect nearby components for leaks

A belt should not be continually exposed to:

- Engine oil
- Coolant
- Powertrain-fluid spray
- Road chemicals

If a belt is contaminated, find and repair the leak rather than simply cleaning the belt and pretending the cause is gone.

---

# 10. Noise Diagnosis

Noise is a pattern clue, not a component verdict.

## Squeal

Common pattern:

```text
HIGH-PITCHED SQUEAL
       ↓
slip under load
       ↓
possible causes:
low tension
wet / contaminated belt
glazed belt
high accessory drag
misalignment
```

Squeal that appears during:

- Cold start
- Heavy electrical load
- A/C engagement
- Rapid acceleration

can help identify when accessory load is provoking the slip.

Do **not** automatically tighten the belt harder. A dragging alternator, water pump, idler or A/C compressor can create the same symptom.

## Chirp

A repetitive chirp that follows engine speed often suggests:

- Pulley misalignment
- Rib tracking error
- Damaged rib
- Foreign material in a groove
- Slight pulley wobble

## Growl / rumble / grinding

Suspect a rotating component before condemning the belt itself:

- Idler bearing
- Alternator bearing
- Water-pump bearing
- A/C compressor pulley/clutch bearing

## Slap / flutter

Possible causes:

- Insufficient tension
- Belt damage
- Pulley eccentricity
- Accessory drag variation
- Incorrect belt/application

---

# 11. Belt Tracking and Alignment

A belt that repeatedly walks sideways, frays one edge or throws itself off is usually telling you something.

Investigate:

- Incorrect belt width/application
- Bent bracket
- Loose alternator mounting
- Idler misalignment
- Water-pump pulley wobble
- Crank pulley/damper damage
- A/C pulley alignment
- Pulley bearing failure
- Debris in pulley grooves

Do not install belt after belt onto a system that is visibly misaligned.

---

# 12. Pulley and Bearing Diagnosis

With the engine **off**, belt removed and components cool enough to touch:

1. Rotate accessible pulleys by hand.
2. Feel for roughness, notchiness, seizure or grinding.
3. Check for excessive radial or axial play.
4. Inspect pulley faces and grooves.
5. Verify the accessory is not cocked on its bracket.

### Water pump

Red flags:

- Rough bearing
- Pulley wobble
- Coolant trace around pump
- Grinding
- Recurrent belt walk

A failing water-pump bearing can become both a belt problem and a cooling-system failure.

### Alternator

Red flags:

- Rough/noisy bearings
- Pulley resistance inconsistent with normal alternator drag
- Charging warning
- Heat/discoloration
- Belt dust around pulley

### Idler

Red flags:

- Dry bearing hiss
- Gravelly rotation
- Side play
- Visible wobble

### A/C compressor / pulley

If noise changes immediately when A/C is commanded on or off, investigate the compressor-clutch/pulley load path.

Do not assume the compressor itself is seized until pulley/clutch behavior is isolated.

---

# 13. Charging-Warning + Overheating Pattern

This symptom pair is especially important:

```text
BATTERY / CHARGING WARNING
            +
TEMPERATURE RISING
            ↓
CHECK ACCESSORY BELT IMMEDIATELY
```

A single belt-drive fault can explain both systems at once.

This pattern is much stronger evidence for a belt/accessory-drive failure than either warning by itself.

---

# 14. Belt Failure While Driving

## Immediate response

If you hear a sudden slap, bang, squeal or shredding noise and then notice:

- Charging light
- Rising coolant temperature
- A/C loss
- Rubber smell
- Pieces of belt

then:

```text
SIGNAL / GET SAFE
      ↓
STOP VEHICLE
      ↓
SHUT ENGINE OFF
      ↓
OPEN HOOD ONLY WHEN SAFE
      ↓
VISUALLY VERIFY BELT CONDITION
```

If the belt is broken, missing or off the water-pump pulley:

> **Do not restart merely to “see if it will make it.”**

The engine may restart and run perfectly for a short time while silently cooking itself.

---

# 15. Roadside Belt Replacement: Decision Rule

A field belt replacement is reasonable only when all of these are true:

- Correct replacement belt is available.
- Correct routing is known.
- No pulley is seized.
- No pulley/bracket is visibly misaligned or broken.
- Water pump turns acceptably and is not leaking badly.
- Alternator pulley/bearing is not seized.
- Idler is healthy.
- A/C pulley/compressor path is not mechanically locked.
- Belt can be tensioned correctly.
- No tools/body parts need to enter unsafe moving zones.

If the original belt failed because an accessory seized, installing another belt can destroy the new belt immediately.

### Before installing a new belt

```text
WHY DID THE OLD BELT FAIL?
         ↓
AGED / CRACKED?
CONTAMINATED?
MISALIGNED?
SEIZED PULLEY?
FAILED BEARING?
INCORRECT TENSION?
```

Do not skip this question.

---

# 16. Belt Installation Principles

**SERVICE-FAMILY — same-generation Hyundai**

Hyundai instructs that when installing the V-ribbed belt:

- All pulley grooves must be correctly engaged by belt ribs.
- Belt tension must be measured/adjusted.
- New and used belts have different tension targets.

After installation:

1. Confirm every rib is seated.
2. Confirm no rib hangs over a pulley edge.
3. Adjust tension.
4. Tighten mounting hardware.
5. Rotate/check system as appropriate.
6. Start engine and observe tracking from a safe distance.
7. Shut engine off.
8. Reinspect tracking and tension.
9. Verify charging system.
10. Verify coolant temperature remains normal.

---

# 17. Belt Dressing and Spray Products

**GENERAL DIAGNOSTIC PRACTICE**

Do not use belt dressing as a substitute for diagnosis.

Sprays can temporarily change friction and noise while hiding:

- Low tension
- Contamination
- Misalignment
- Pulley damage
- Bearing drag

A quiet belt is not necessarily a healthy belt.

---

# 18. Oil or Coolant on the Belt

If the belt is contaminated:

```text
CONTAMINATED BELT
       ↓
FIND LEAK SOURCE
       ↓
REPAIR LEAK
       ↓
CLEAN PULLEYS
       ↓
REPLACE DAMAGED / SATURATED BELT
       ↓
VERIFY TRACKING + TENSION
```

Possible nearby sources include:

- Water pump / cooling-system leakage
- Timing-cover / front-engine oil leakage
- Rocker-cover leakage migrating downward
- Oil spilled during service

Do not repeatedly replace belts while ignoring the leak.

---

# 19. Crankshaft Pulley / Damper Clues

A damaged crank pulley can mimic an ordinary belt problem.

Investigate if there is:

- Visible pulley wobble
- Belt walking sideways
- Repeated edge wear
- Rhythmic chirp
- Rubber deterioration in the damper area
- Sudden change in accessory tracking

Do not place hands near a suspected wobbling pulley while the engine is running.

---

# 20. Water-Pump Consequences

The water pump is not merely another accessory.

If belt drive to the pump is lost:

- Coolant circulation is lost or severely reduced.
- Engine temperature can rise rapidly.
- Head-gasket / cylinder-head damage becomes possible.

The exact 2014 owner manual therefore makes a broken water-pump drive belt an **immediate stop-engine condition**.

Cross-reference:

- `COOLING_SYSTEM.md`
- `CYLINDER_HEAD_HEAD_GASKET.md`

---

# 21. Alternator Consequences

If the belt slips badly or stops driving the alternator:

- Battery warning may illuminate.
- System voltage may fall.
- ABS/ESC/MDPS and other modules can set secondary low-voltage faults.
- Steering assist may become abnormal as voltage drops.
- The engine may eventually stall once battery energy is exhausted.

Do not diagnose a pile of low-voltage DTCs until charging/belt drive is corrected.

Cross-reference:

- `../diagnostics/CHARGING_SYSTEM.md`
- `../electrical/BATTERY_STARTER_ALTERNATOR.md`

---

# 22. A/C-Related Noise Branch

If a belt noise appears mainly when A/C engages:

```text
A/C ON → NOISE APPEARS
        ↓
CHECK:
compressor load
clutch/pulley bearing
belt tension
belt contamination
idler
alignment
```

If noise exists equally with A/C on and off, broaden the search to all rotating accessories.

---

# 23. Symptom Matrix

| Symptom | Higher-probability areas to inspect |
|---|---|
| Cold-start squeal | belt tension, glazing, contamination, accessory drag |
| Squeal with electrical load | alternator load + belt tension |
| Squeal when A/C engages | compressor/clutch load, tension, belt condition |
| Repetitive chirp | alignment, pulley groove/rib, wobble |
| Belt frays one edge | pulley misalignment / bent bracket / wobble |
| Belt jumps off | severe misalignment, seized accessory, incorrect belt, pulley failure |
| Battery light + rising temperature | accessory belt / shared drive failure |
| Grinding at belt side | idler, water pump, alternator, compressor pulley bearing |
| Coolant leak + pulley wobble | water-pump failure likely |
| Belt dust | slip, misalignment, pulley damage, wrong tension |
| Belt repeatedly loosens | adjuster/mounting fault, belt stretch, bracket movement |

This table ranks inspection direction only. It does not replace testing.

---

# 24. Do Not Do These Things

```text
DO NOT:

• drive with a broken/missing water-pump drive belt
• reach near a moving belt
• tighten the belt blindly to cure every squeal
• pry against fragile housings/connectors
• install a replacement belt over a seized pulley
• ignore belt edge wear
• spray belt dressing and call the problem repaired
• assume a charging warning automatically means alternator failure
• assume overheating automatically means thermostat/head gasket
• order a belt without checking VIN/configuration/build fit
```

---

# 25. Nomad / Remote-Road Strategy

For remote travel, belt reliability deserves more attention than it gets in ordinary city use.

Before a remote-road leg:

1. Inspect belt condition.
2. Verify tension.
3. Look for fresh belt dust.
4. Look for coolant around water pump.
5. Listen for idler/alternator/water-pump bearing noise.
6. Confirm charging voltage is normal.
7. Confirm coolant level is correct.

### Reasonable spare strategy

Consider carrying:

- Correct VIN-verified spare V-ribbed belt
- Compact belt-routing reference
- Tools required to loosen/tension alternator mounting
- Flashlight/headlamp
- Gloves

A spare belt is useful only if the pulley system is mechanically healthy enough to accept it.

---

# 26. Post-Rough-Road Inspection

After unusually rough gravel, mud, debris or underbody contact:

- Check belt for stones/debris.
- Check pulley grooves.
- Verify undercovers have not shifted into the belt path.
- Inspect nearby wiring and hoses.
- Listen for a new chirp or scrape.
- Look for coolant or oil contamination.

The belt system is exposed to engine movement and road debris, and small tracking changes can become large failures later.

---

# 27. AI / RAG Diagnostic Rules

An AI using this file must follow these rules:

1. **Never recommend continued driving with a broken/missing water-pump drive belt.**
2. Treat **battery warning + rising temperature** as a strong shared-belt clue.
3. Do not condemn the alternator before verifying belt drive and tension.
4. Do not condemn the water pump solely because the engine overheats.
5. Do not cure every squeal by increasing belt tension.
6. Consider accessory bearing drag when belts repeatedly fail.
7. Treat edge wear as an alignment clue.
8. Treat contamination as evidence of another leak/failure.
9. Use exact 2014 owner-manual maintenance guidance over adjacent-year conflict.
10. Tag belt part numbers as VIN/configuration dependent.
11. Never invent routing details if exact installed configuration is unknown.
12. Do not present SERVICE-FAMILY values as exact 2014 factory specifications.

### Preferred AI reasoning chain

```text
BELT SYMPTOM
     ↓
SAFE TO RUN ENGINE?
     ↓
VISUAL CONDITION
     ↓
TENSION
     ↓
ALIGNMENT
     ↓
PULLEY / BEARING HEALTH
     ↓
WATER-PUMP DRIVE PRESENT?
     ↓
ALTERNATOR DRIVE PRESENT?
     ↓
A/C LOAD EFFECT?
     ↓
ROOT CAUSE
     ↓
REPAIR
     ↓
VERIFY CHARGING + COOLING
```

---

# 28. Field Incident Log Template

```yaml
accessory_drive_incident:
  date: UNKNOWN
  odometer_miles: UNKNOWN
  engine_temp_state: UNKNOWN
  weather: UNKNOWN
  road_surface: UNKNOWN

  symptoms:
    squeal: false
    chirp: false
    grinding: false
    belt_slapping: false
    charging_warning: false
    overheating: false
    ac_loss: false
    rubber_smell: false

  belt:
    present: UNKNOWN
    intact: UNKNOWN
    cracks: UNKNOWN
    fraying: UNKNOWN
    glazing: UNKNOWN
    chunks_missing: UNKNOWN
    oil_contamination: UNKNOWN
    coolant_contamination: UNKNOWN
    edge_wear: UNKNOWN
    tracking_centered: UNKNOWN
    tension_status: UNKNOWN

  pulleys:
    crank_wobble: UNKNOWN
    water_pump_roughness: UNKNOWN
    water_pump_play: UNKNOWN
    alternator_roughness: UNKNOWN
    idler_roughness: UNKNOWN
    ac_pulley_roughness: UNKNOWN

  charging:
    battery_voltage_engine_off: UNKNOWN
    system_voltage_engine_running: UNKNOWN

  cooling:
    coolant_level: UNKNOWN
    water_pump_leak_visible: UNKNOWN
    temp_normal_after_repair: UNKNOWN

  repair:
    root_cause: UNKNOWN
    belt_part_number: UNKNOWN
    belt_replaced: false
    pulley_replaced: false
    accessory_repaired: false
    tension_verified: false

  verification:
    belt_tracks_correctly: UNKNOWN
    no_abnormal_noise: UNKNOWN
    charging_normal: UNKNOWN
    coolant_temp_normal: UNKNOWN
    recheck_after_drive: UNKNOWN
```

---

# 29. Source List

## Exact 2014 sources

Hyundai Accent 2014 Owner's Manual, drive-belt maintenance and overheating procedure:

- https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/33
- https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/?srch=overheating
- https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/?srch=service+interval

2014 Accent Quick Reference Guide:

- https://www.carmanualsonline.info/hyundai-accent-2014-quick-reference-guide/?srch=belt

2014 OE parts catalog, coolant pump / belt / idler:

- https://www.hyundaipartsdeal.com/parts-list/2014-hyundai-accent/engine/coolant_pump.html

2014 OE parts catalog, alternator:

- https://www.hyundaipartsdeal.com/parts-list/2014-hyundai-accent/engine/alternator.html

## Same-generation service-family sources

Gamma 1.4/1.6 drive-belt inspection, tension and adjustment:

- https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Starting%20and%20Charging/Charging%20System/Testing%20and%20Inspection/Component%20Tests%20and%20General%20Diagnostics/

Timing-chain service procedure containing water-pump pulley, idler, alternator and drive-belt installation data:

- https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Engine%2C%20Cooling%20and%20Exhaust/Engine/Timing%20Components/Timing%20Chain/Service%20and%20Repair/Repair%20Procedures/Part%202/

Normal-service drive-belt inspection entry:

- https://charm.li/Hyundai/2013/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Maintenance/Service%20Intervals/Normal%20Service/60000%20MI%20or%2096000%20KM/

---

# 30. Core Doctrine

```text
SQUEAL IS NOT A BELT DIAGNOSIS
CHARGING LIGHT IS NOT AN ALTERNATOR DIAGNOSIS
OVERHEATING IS NOT A THERMOSTAT DIAGNOSIS

CHECK THE SHARED MECHANICAL DRIVE
```

And for roadside use:

```text
BROKEN BELT
   ↓
WATER PUMP LOST?
   ↓
YES
   ↓
STOP ENGINE
   ↓
FIND WHY THE BELT FAILED
   ↓
REPAIR ROOT CAUSE
   ↓
INSTALL / TENSION CORRECTLY
   ↓
VERIFY CHARGING + COOLING
```

**Unknown is preferable to a confident wrong answer.**
