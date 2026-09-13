# 2014 Hyundai Accent SE — Emergency Field Repairs

> **Purpose:** Offline-first field guide for stabilizing common roadside failures on a U.S.-market 2014 Hyundai Accent SE without turning a small problem into an engine, brake, fuel-system, electrical, or personal-safety disaster.
>
> **Core rule:** A field repair is a **temporary risk-control measure**, not permission to ignore the underlying fault.

---

## 1. Vehicle Scope

Primary vehicle:

- U.S.-market 2014 Hyundai Accent SE five-door
- 1.6 L Gamma GDI gasoline engine
- Six-speed automatic transmission
- Front-wheel drive
- Motor Driven Power Steering (MDPS)
- P195/50R16 road tires on the SE configuration
- Compact spare or Tire Mobility Kit depending on vehicle equipment

Related repository files:

- `../guides/ROADSIDE_DIAGNOSTIC_TRIAGE.md`
- `../maintenance/PRE_TRIP_INSPECTION.md`
- `../maintenance/NOMAD_SERVICE_LOG.md`
- `../diagnostics/NO_CRANK.md`
- `../diagnostics/CRANK_NO_START.md`
- `../diagnostics/OVERHEATING.md`
- `../diagnostics/CHARGING_SYSTEM.md`
- `../engine/COOLING_SYSTEM.md`
- `../engine/GDI_FUEL_SYSTEM.md`
- `../electrical/BATTERY_STARTER_ALTERNATOR.md`
- `../brakes/BRAKE_SYSTEM.md`
- `../suspension-steering/STEERING_SUSPENSION.md`
- `../specs/FUSES_AND_RELAYS.md`
- `../specs/FLUIDS_AND_CAPACITIES.md`

---

# 2. Confidence Labels

- **VERIFIED — 2014 OWNER MANUAL:** Directly supported by the 2014 Hyundai Accent owner's manual.
- **VERIFIED — HYUNDAI:** Supported by Hyundai official model information.
- **VERIFIED — STANDARD / GOVERNMENT:** Supported by an applicable safety standard or government source.
- **SERVICE-FAMILY REFERENCE:** Hyundai service information from an adjacent model year or closely related Accent 1.6 GDI system. Useful, but not automatically exact for every 2014 build.
- **GENERAL FIELD PRACTICE:** Broad automotive field practice, not a Hyundai-specific factory instruction.
- **OWNER-SPECIFIC:** Must be confirmed on the actual vehicle before relying on it.

---

# 3. First Priority: Do Not Become the Second Emergency

Before touching the car:

1. Move as far from traffic as safely possible.
2. Turn on hazard flashers.
3. Put the transmission in **P** and apply the parking brake when parked.
4. Choose firm, stable ground before using a jack.
5. Keep people away from the traffic side of the vehicle.
6. Do not work beneath a vehicle supported only by the factory jack.
7. If the shoulder, slope, mud, ice, traffic, darkness, fire risk, or weather makes the repair unsafe, call for recovery instead.

### High-value roadside visibility gear

Carry:

- Reflective vest
- LED flashlight/headlamp
- Reflective triangles or approved emergency markers
- Work gloves
- Eye protection
- Fire extinguisher rated for automotive electrical/fuel fires

Do **not** place yourself in a traffic lane to deploy equipment.

---

# 4. Hard NO-GO / DO-NOT-IMPROVISE Conditions

Do not drive the vehicle merely because it can still move.

## Stop and recover the vehicle if any of these occur

- Brake fluid is leaking.
- Brake pedal falls abnormally far or braking is substantially reduced.
- Fuel is visibly leaking or spraying.
- A GDI high-pressure fuel component is damaged.
- Electrical wiring is smoking, melting, or repeatedly blowing a major fuse.
- Engine oil-pressure warning remains on while the engine is running.
- Engine has severe knocking, hammering, grinding, or sudden mechanical noise.
- Coolant is pouring out.
- Steam is escaping from the engine compartment.
- Water-pump drive belt is broken or missing.
- Steering has uncontrolled play, binding, or loss of directional control.
- Tie rod, ball joint, wheel bearing/hub, control arm, strut mounting, or wheel is visibly loose or structurally damaged.
- Tire has a sidewall rupture, exposed cord, major bulge, broken bead, or wheel damage and no safe spare is available.
- A wheel stud/nut failure prevents the wheel from being secured correctly.
- Automatic-transmission fluid is leaking substantially.
- A fire has occurred or fuel has contacted an ignition source.

### Never perform these roadside improvisations

- Clamp or crimp a brake hose to keep driving.
- Patch a brake line with rubber hose.
- Substitute power-steering fluid anywhere; this vehicle uses electric MDPS.
- Patch or splice a high-pressure GDI fuel pipe.
- Loosen a GDI high-pressure line to "check for fuel."
- Wrap a leaking fuel line with tape and continue driving.
- Bridge a blown fuse with foil, wire, a coin, or a higher-amperage fuse.
- Defeat a relay or safety circuit with an uncontrolled jumper wire.
- Weld, strap, or wire a broken steering or suspension joint into place for road use.
- Crawl beneath the vehicle with only the factory jack supporting it.
- Dynamically yank the vehicle from an unverified factory tow eye with a kinetic recovery rope.

A tow is cheaper than an engine, transmission, collision, fire, or hospital visit.

---

# 5. Roadside Decision Ladder

```text
FAILURE OCCURS
    ↓
GET OUT OF TRAFFIC / STABILIZE SCENE
    ↓
IS THERE FIRE, FUEL, BRAKE, STEERING,
WHEEL, STRUCTURAL, OIL-PRESSURE,
OR SEVERE-OVERHEAT RISK?
    ├─ YES → SHUT DOWN / RECOVER VEHICLE
    └─ NO
         ↓
PRESERVE CODES / FREEZE FRAME / SYMPTOMS
         ↓
CAN THE FAULT BE SAFELY STABILIZED
WITHOUT BYPASSING A SAFETY SYSTEM?
    ├─ NO → RECOVER VEHICLE
    └─ YES
         ↓
MAKE MINIMAL TEMPORARY REPAIR
         ↓
RECHECK / SHORT LOW-RISK TEST
         ↓
DRIVE ONLY TO SAFETY OR REPAIR,
NOT BACK TO NORMAL USE
```

---

# 6. Dead Battery / No-Crank Field Response

See:

- `../diagnostics/NO_CRANK.md`
- `../diagnostics/CHARGING_SYSTEM.md`
- `../electrical/BATTERY_STARTER_ALTERNATOR.md`

## Before jump-starting

Check for:

- Cracked battery case
- Leaking electrolyte
- Swollen or frozen battery
- Melted terminals
- Heavy cable damage
- Strong electrical-burning smell

Do not jump a visibly damaged or frozen battery.

## Hyundai jump-start sequence

**VERIFIED — 2014 OWNER MANUAL**

Hyundai specifies a **12-volt** booster source.

1. Turn off unnecessary electrical loads.
2. Positive cable to discharged-battery positive.
3. Other positive cable end to booster-battery positive.
4. Negative cable to booster-battery negative.
5. Final negative connection to a solid stationary metallic engine/body ground away from the discharged battery and moving parts.
6. Do not allow the vehicles to touch.
7. Hyundai instructs starting the donor/booster vehicle and running it around 2,000 rpm before attempting the discharged vehicle when using another vehicle as the source.

Source:

- 2014 Hyundai Accent Owner's Manual, emergency jump-start section: https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/?srch=charging

### Automatic transmission rule

The automatic-transmission Accent **cannot be push-started**.

Do not attempt bump-starting or tow-starting.

## If the jump works

Do not assume the battery was the root cause.

Possible causes include:

- Battery discharged by lights/accessories
- Weak battery
- Loose/corroded terminal
- Bad ground
- Alternator/charging fault
- Belt problem
- Parasitic draw

If the charging warning lamp remains illuminated, diagnose before depending on the car for remote travel.

---

# 7. Loose or Corroded Battery Terminal

**GENERAL FIELD PRACTICE**

A visibly loose battery clamp can create:

- Intermittent no-crank
- Rapid clicking
- Instrument resets
- Low-voltage DTCs
- Charging irregularities
- MDPS assist problems

Field stabilization is reasonable if:

- Battery case is intact.
- Terminal is not melted.
- Cable is not broken internally or badly corroded.
- Clamp can be mechanically secured normally.

Clean only enough corrosion to restore a sound connection, protect eyes and skin, then tighten the terminal correctly.

Do not hammer a clamp onto a battery post or force a damaged terminal to fit.

---

# 8. Flat Tire — Compact Spare

**VERIFIED — 2014 OWNER MANUAL**

The 2014 manual lists the compact spare, if equipped, as:

```text
T125/80D15
Cold pressure: 60 psi / 420 kPa
Maximum speed: 50 mph / 80 km/h
Temporary use only
```

The manual warns that the compact spare has a smaller diameter and reduces ground clearance.

Sources:

- Compact spare instructions: https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/?srch=tire+size
- Tire/wheel specifications: https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/?srch=wheel+torque

## Safe wheel-change procedure

1. Stop on firm, level, non-slippery ground away from traffic.
2. Shift to **P**.
3. Apply parking brake.
4. Turn on hazards.
5. Chock a wheel diagonally opposite the wheel being changed if safe and practical.
6. Loosen wheel nuts slightly before lifting.
7. Use only the designated jacking point.
8. Lift only high enough to remove/install the wheel.
9. Never place any part of your body beneath the vehicle while it is supported by the factory jack.
10. Install the wheel and snug nuts in a cross/star pattern.
11. Lower the vehicle.
12. Tighten evenly.
13. Verify torque with a torque wrench as soon as practical.

### Wheel-nut torque

**VERIFIED — 2014 OWNER MANUAL**

```text
65–79 lb-ft
88–107 N·m
```

Do not stand on the wrench or add a pipe to the factory lug wrench.

## After installing compact spare

- Confirm **60 psi cold**.
- Stay below **50 mph**.
- Avoid potholes, rocks, ruts, deep gravel, and abrupt maneuvers.
- Restore a normal wheel/tire as soon as possible.
- Remember that the compact spare further reduces the Accent's already modest ground clearance.

NHTSA also recommends treating spare tires as emergency equipment rather than replacements for worn regular tires and inspecting tires for damage, inflation loss, bulges, cracks, and irregular wear.

Government source:

- NHTSA TireWise: https://www.nhtsa.gov/vehicle-safety/tires

---

# 9. Tire Mobility Kit — If Equipped

Some 2014 Accents were supplied with Hyundai's Tire Mobility Kit instead of a compact spare.

**VERIFIED — 2014 OWNER MANUAL**

Hyundai describes the kit as a temporary repair for many tread-area punctures caused by nails or similar objects.

Factory limitations include:

- **Do not use it for tire sidewall damage.**
- One sealant bottle is intended for one tire.
- Maximum post-repair speed: **50 mph / 80 km/h**.
- Hyundai lists up to **120 miles / 200 km** of cautious temporary travel after a successful seal, solely to reach repair/service.
- Tire should be professionally inspected/repaired or replaced as soon as possible.

Source:

- 2014 Accent Tire Mobility Kit section: https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/?srch=tire+replacement

### Do not use sealant when

- Sidewall is cut or punctured.
- Tire has separated or shredded.
- Bead has unseated.
- Wheel is bent/cracked.
- Two or more tires are flat and only one sealant bottle is available.
- Tire has been driven flat long enough to damage the carcass.

---

# 10. Blown Fuse

See `../specs/FUSES_AND_RELAYS.md`.

## Safe temporary field action

**VERIFIED — 2014 OWNER MANUAL**

1. Turn ignition and affected loads off.
2. Identify the correct fuse using the panel label and repository reference.
3. Remove the suspected fuse.
4. Confirm it is open/blown.
5. Replace it only with **the same amperage rating**.
6. Reinstall fuse-panel covers securely against moisture.

Source:

- 2014 Accent fuse replacement: https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/2/?srch=fuse

## If the new fuse blows again

Stop replacing fuses.

A repeated fuse failure means the circuit likely still has:

- Short to ground
- Damaged wiring
- Failed motor/component
- Water intrusion
- Pinched harness
- Internal component fault

Repeatedly feeding the circuit more fuses does not repair the fault.

### Never substitute

- Higher-amperage fuse
- Foil
- Wire
- Coin
- Metal object

### Bolted multi-fuse caution

Hyundai warns against disassembling/reassembling the bolted multi-fuse casually and specifies disconnecting the negative battery terminal before multi-fuse removal.

---

# 11. Cooling-System Leak / Overheating

See:

- `../diagnostics/OVERHEATING.md`
- `../engine/COOLING_SYSTEM.md`
- `../specs/FLUIDS_AND_CAPACITIES.md`

## Hyundai emergency sequence

**VERIFIED — 2014 OWNER MANUAL**

If overheating occurs:

1. Pull off safely.
2. Shift to **P** and set the parking brake.
3. Turn A/C off.
4. If steam or coolant is escaping, stop the engine.
5. Do not open the hood until severe steaming has subsided enough to approach safely.
6. Never remove the radiator cap while hot.
7. If there is no visible coolant loss or steam, Hyundai says to check whether the cooling fan is operating.
8. If the fan is not operating, shut the engine off.
9. Check the water-pump drive belt.
10. If the water-pump drive belt is broken or coolant is leaking out, **stop the engine immediately**.

Source:

- 2014 Accent overheating section: https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/?srch=engine+coolant

## Minor hose seep after full cooldown

**GENERAL FIELD PRACTICE**

A tiny external seep from a conventional low-pressure hose connection can sometimes be stabilized temporarily by:

- Correcting a displaced hose if undamaged
- Tightening a loose serviceable clamp without crushing the fitting
- Replacing a failed clamp with a correctly sized clamp

A hose that is split, oil-soaked, ballooned, hardened, shredded, or leaking near a molded connection should be replaced rather than trusted.

### Emergency hose patch

A temporary external hose patch using self-fusing silicone repair tape and/or a proper sleeve/clamp arrangement is an **emergency-only technique**, not a normal repair.

Use it only when:

- Engine is completely cool.
- Leak is on a conventional coolant hose, not a fuel/brake/ATF line.
- Hose has not burst catastrophically.
- Repair is being used solely to reach immediate safety/service.
- Coolant temperature and level can be watched continuously.

If temperature begins climbing again, shut down.

## Coolant top-up

Hyundai specifies ethylene-glycol coolant suitable for aluminum components, using deionized/soft water, with the final mixture kept between roughly **35% and 60% antifreeze**.

Source:

- 2014 Accent coolant specification: https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/?srch=Coolant

For routine travel, carry correct premixed coolant rather than depending on roadside water.

---

# 12. Broken or Missing Water-Pump / Alternator Drive Belt

**VERIFIED — 2014 OWNER MANUAL**

Hyundai's overheating instructions specifically say:

- Check whether the water-pump drive belt is missing.
- If the water-pump drive belt is broken, **stop the engine immediately**.

Source:

- https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/?srch=engine+coolant

Same-generation Accent service information also shows the alternator drive belt being removed before the water-pump pulley and pump during engine service, corroborating the importance of the belt-driven accessory path.

Service-family reference:

- https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Engine%2C%20Cooling%20and%20Exhaust/Engine/Timing%20Components/Timing%20Chain/Service%20and%20Repair/Repair%20Procedures/Part%201%20of%202/

### Field rule

Do not run the engine "just a few more miles" with a broken/missing belt when water-pump operation is lost.

A spare belt is useful only if:

- The correct belt is carried.
- The cause of the belt failure is understood.
- Pulleys spin correctly.
- No seized accessory or damaged tension/idler component caused the failure.
- Installation can be performed safely and correctly.

Installing another belt onto a seized pulley can immediately destroy the replacement belt.

---

# 13. Loose Electrical Connector or Ground

**GENERAL FIELD PRACTICE**

A connector that has clearly worked loose may sometimes be reseated safely if:

- Ignition is off.
- Connector is cool.
- Pins are not burned, green with severe corrosion, spread, bent, or melted.
- Locking mechanism still functions.
- Wiring insulation is intact.

Examples where a simple reseat may restore operation:

- Ignition coil connector
- Sensor connector
- Battery terminal
- Accessible chassis/engine ground connection

Do not force mismatched connectors together.

Do not repeatedly unplug live modules simply to see what happens.

Preserve DTCs before disconnecting the battery.

---

# 14. Damaged Wiring

## Temporary insulation repair

**GENERAL FIELD PRACTICE**

If only the insulation is abraded and the conductor is intact, a temporary weather-resistant electrical insulation repair may be reasonable after the circuit is powered down.

If conductor strands are broken, burned, green/corroded, shorted, or carrying high current, proper wire repair is required.

### Never make a casual roadside splice in

- Airbag/SRS wiring
- ABS wheel-speed harness without correct repair technique
- GDI injector/high-current driver wiring
- Starter B+ cable
- Alternator B+ cable
- Main battery cable
- High-current fuse link
- Any melted harness section

A harness that has overheated enough to melt insulation should be treated as a fire risk until the root cause is identified.

---

# 15. Minor Exhaust Damage

**GENERAL FIELD PRACTICE**

Possible low-risk temporary actions:

- Secure a loose heat shield if the original fastener location is intact and the repair cannot contact moving/hot components.
- Remove only a completely detached piece that is already separated and creating a road hazard, if this can be done safely with the exhaust cold.

Do not crawl under a hot exhaust or jack-supported vehicle.

## Do not continue driving if

- Exhaust is hanging low enough to catch the road.
- Exhaust is contacting a tire, fuel line, brake line, CV boot, wiring, or plastic body component.
- Exhaust gas can enter the passenger compartment.
- Catalytic converter is glowing or there is evidence of severe overheating.
- A major exhaust restriction causes power loss or extreme heat.

Never sleep in the vehicle with the engine running. Carbon monoxide can accumulate even when the exhaust appears intact.

---

# 16. Loose Splash Shield / Undertray

**GENERAL FIELD PRACTICE**

A partially detached plastic splash shield can become a road hazard or be pulled into rotating components.

Safe temporary actions may include:

- Reinstalling intact original clips/fasteners.
- Using suitable temporary mechanical fasteners in existing noncritical mounting holes.
- Removing a severely damaged loose plastic panel only if it can be done without going under an unsafe vehicle and without exposing or disturbing critical components.

Do not attach anything to:

- Brake lines
- Fuel lines
- CV axles
- Steering components
- Exhaust
- Suspension springs
- Cooling fan
- Drive belt/pulleys

Zip ties are useful organizers, not structural suspension hardware.

---

# 17. Brake Drag / Hot Wheel

See `../brakes/BRAKE_SYSTEM.md`.

A wheel that is much hotter than the others after normal driving may indicate:

- Sticking caliper piston
- Seized slide pin
- Parking-brake mechanism/cable not releasing
- Restricted brake hose
- Wheel-bearing problem

## Field response

1. Stop safely.
2. Do not touch rotor/caliper immediately; severe burns are possible.
3. Look for smoke, odor, discoloration, or obvious fluid leakage.
4. Allow the assembly to cool naturally.
5. Verify the parking brake is fully released.

### Do not

- Pour water onto a very hot rotor.
- Clamp a brake hose.
- Open a bleeder merely to make the wheel roll and then continue normal travel.
- Disconnect the parking-brake system and assume the car is repaired.

If the brake binds again, smokes, or substantially affects vehicle motion, recover the vehicle.

---

# 18. Steering / Suspension / Wheel Impact

After a pothole, rut, rock, curb strike, or primitive-road impact, stop and inspect before continuing.

Check:

- Tire sidewalls
- Wheel lip/cracks
- Wheel position in arch
- Steering wheel centering
- Tie rods
- Control arm area
- Ball-joint area
- Strut body/spring
- CV boots
- Fluid leaks beneath engine/transmission
- Exhaust and underbody contact

## Stop driving for

- New visible wheel tilt
- Tire rubbing body/suspension
- Steering wheel dramatically off-center after impact
- Severe pull
- Clunk plus steering looseness
- Broken spring
- Bent tie rod/control arm
- Ball-joint or hub play
- Cracked wheel
- Sidewall bulge/cut

The Accent is a low-clearance FWD economy car. A road that requires more ground clearance is not made suitable by adding more throttle.

---

# 19. Stuck in Mud, Sand, Snow, or Loose Gravel

## First rule

Stop digging holes with the driven wheels.

Excessive wheelspin can:

- Bury the front suspension/subframe
- Overheat tires
- Damage the road/trail
- Heat the transmission
- Reduce the usefulness of traction boards

## Low-risk self-recovery sequence

1. Stop wheelspin.
2. Inspect what is actually holding the car.
3. Clear loose material from immediately ahead/behind the driven tires if safe/legal.
4. Straighten the front wheels when possible.
5. Place traction boards correctly.
6. Use gentle throttle.
7. Stop if the car begins resting on its underbody.

### Recovery-point warning

Do **not** assume the factory threaded tow eye is rated for a high-energy kinetic recovery pull.

Unless a recovery point is explicitly verified for dynamic loads, treat the tow eye as a towing/loading point rather than a kinetic-rope recovery anchor.

A slow controlled pull is fundamentally different from a kinetic snatch.

---

# 20. Automatic-Transmission Towing

See `../transmission/SIX_SPEED_AUTOMATIC.md`.

**VERIFIED — 2014 OWNER MANUAL**

If the automatic Accent must be emergency-towed with all four wheels on the ground:

- Tow from the front.
- Transmission in **N**.
- Steering unlocked.
- Driver must operate steering/brakes.
- Maximum approximately **10 mph / 15 km/h**.
- Maximum distance approximately **1 mile / 1.5 km**.

If automatic-transmission fluid is leaking, Hyundai says a **flatbed or towing dolly must be used**.

Source:

- 2014 Accent towing section: https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/?srch=emergency+release

For ordinary roadside recovery, a flatbed is the preferred low-risk choice.

---

# 21. Oil Leak

## Small seep versus active loss

A slightly damp gasket area is different from oil actively dripping or spraying.

Field decision:

```text
MINOR SEEP
→ verify dipstick level
→ document
→ monitor
→ repair soon

ACTIVE LEAK
→ determine rate/source
→ if level falling rapidly, stop engine

OIL-PRESSURE WARNING WHILE RUNNING
→ stop engine immediately
```

Do not continue driving solely because spare oil is available.

Adding oil does not repair a leak that can empty the crankcase faster than it is being monitored.

Do not use random stop-leak products as a substitute for diagnosis.

---

# 22. Fuel Leak / Raw Fuel Smell

See `../engine/GDI_FUEL_SYSTEM.md`.

## Hard rule

A visible fuel leak is **not a field-patch-and-drive problem**.

Actions:

1. Shut engine off.
2. Keep ignition sources away.
3. Do not smoke or create sparks.
4. Do not repeatedly cycle ignition/fuel pump.
5. Do not touch a suspected GDI high-pressure leak with your hand.
6. Recover the vehicle.

GDI fuel can operate at pressures high enough to penetrate skin.

Never use tape, epoxy, hose, or clamps to repair a high-pressure fuel pipe.

---

# 23. Temporary Repair Kit for Nomad Use

A compact field kit can include:

### Safety

- Reflective vest
- Reflective triangles
- LED headlamp + spare batteries
- Work gloves
- Eye protection
- Automotive fire extinguisher

### Tire / wheel

- Accurate tire-pressure gauge
- 12 V inflator
- Tire plug kit for appropriate **tread-area punctures only**, if the operator understands its limitations
- Spare valve cores and valve-core tool
- Compact spare checked at 60 psi, if equipped
- 21 mm wheel tool if confirmed for the installed lug nuts
- Torque wrench capable of 65–79 lb-ft
- Wheel chock

### Electrical

- Digital multimeter
- OBD-II scanner
- Quality jumper cables or appropriate booster pack
- Exact spare blade fuses
- Fuse puller
- Electrical tape
- Heat-shrink / proper crimp repair supplies for noncritical wiring
- Small wire brush / terminal cleaning tool

### Cooling

- Correct premixed coolant
- Funnel
- Self-fusing silicone repair tape for emergency conventional-hose stabilization
- A few appropriate hose clamps
- Shop towels

### General

- Basic metric socket/wrench set
- Pliers
- Screwdrivers
- Utility knife
- Flashlight mirror
- Mechanic wire for noncritical securing tasks
- Zip ties for nonstructural items
- Nitrile gloves
- Absorbent pads
- Trash bags
- Pen/marker
- Paper copy or offline copy of this repository

### Recovery

- Traction boards
- Soft shackles only where an appropriate rated attachment point exists
- Tow equipment only when attachment points and ratings are known

Do not let recovery gear encourage entry onto roads the Accent cannot safely clear.

---

# 24. Things Worth Carrying as Actual Spare Parts

For long-distance remote travel, compact low-cost spares may be more useful than carrying large assemblies.

Consider only after confirming exact fitment:

- Common blade fuses
- Known-good relay(s) where interchange is verified
- Correct accessory/drive belt
- One ignition coil
- One or two correct spark plugs
- Spare valve cores/caps
- Common hose clamps
- Correct oil and coolant
- Replacement headlight/brake bulbs where applicable

Do not purchase parts solely from generic year/make/model listings when VIN, engine, trim, or production-date differences matter.

---

# 25. After Any Field Repair

Before moving:

1. Remove tools from engine bay and under vehicle.
2. Verify caps and covers are installed.
3. Verify no wires/hoses can reach belts, fan, exhaust, axle, or steering components.
4. Recheck fluid levels where applicable.
5. Check for leaks.
6. Scan for DTCs if relevant.
7. Start and idle while watching/listening.
8. Recheck repair.
9. Move only a short distance at low speed initially.
10. Stop and inspect again.

## A successful temporary repair means

```text
SAFE ENOUGH TO REACH
A SAFER PLACE OR PROPER REPAIR
```

It does **not** mean:

```text
RETURN TO NORMAL REMOTE TRAVEL
```

Log the event in `../maintenance/NOMAD_SERVICE_LOG.md`.

---

# 26. Emergency Severity Classes

| Class | Meaning | Action |
|---|---|---|
| GREEN | Cosmetic/noncritical issue, vehicle control unaffected | Secure/monitor |
| YELLOW | Temporary repair possible, but permanent repair required soon | Stabilize, drive cautiously to service |
| ORANGE | Vehicle may move but continued operation risks major damage | Move only if required for immediate safety; otherwise recover |
| RED | Fire, fuel, brake, steering, wheel, severe overheating, oil-pressure, structural risk | Shut down / do not drive |

The classification depends on the actual symptom, not merely the name of the failed part.

---

# 27. AI Diagnostic Rules

When an AI assistant uses this document:

1. **Scene safety comes before mechanical diagnosis.**
2. Ask whether the vehicle is in traffic or another immediately dangerous location.
3. Identify RED conditions before suggesting tests.
4. Never recommend bypassing a brake, steering, fuel, airbag, or major electrical safety system to keep moving.
5. Never recommend opening GDI high-pressure fuel lines for roadside diagnosis.
6. Never recommend removing a hot radiator cap.
7. Never recommend getting beneath a car supported only by the factory jack.
8. Never assume a tow eye is a rated kinetic-recovery point.
9. Preserve DTCs/freeze frame before battery disconnect or code clearing when possible.
10. Treat a temporary repair as temporary.
11. Prefer controlled recovery over escalating mechanical damage.
12. Clearly label Hyundai-specific facts versus general field practice.
13. Do not invent torque values, fluid specifications, wire colors, fuse ratings, pressure values, or part numbers.
14. Use related repository system guides for deeper diagnosis.
15. If evidence is insufficient, say **UNKNOWN** and identify the next safe test.

---

# 28. AI Prompt Template

```text
Vehicle: 2014 Hyundai Accent SE 5-door, 1.6 GDI, 6-speed automatic
Location type: highway / city / gravel / forest road / campsite / other
Immediate traffic danger: yes/no
Engine running: yes/no
Cranks: yes/no
Warning lights:
Smoke/steam: yes/no
Fuel smell/leak: yes/no
Coolant leak: yes/no
Oil leak: yes/no
Brake problem: yes/no
Steering problem: yes/no
Tire/wheel damage: yes/no
Electrical burning smell: yes/no
Recent impact or rough road: yes/no
DTCs:
Freeze frame:
Battery voltage:
Coolant temperature:
Observed symptom:
Tools available:
Spare parts available:

Classify the situation GREEN/YELLOW/ORANGE/RED.
First identify any DO-NOT-DRIVE condition.
Then give the minimum safe diagnostic sequence.
Separate factory-verified facts from general field practice.
Do not recommend bypassing safety systems.
```

---

# 29. Field Incident Record

```markdown
## Roadside Incident
Date:
Time:
Odometer:
Location / road type:
Weather:
Ambient temperature:
Vehicle speed when failure began:
Road condition:

### Symptoms
Warning lights:
Noise:
Smell:
Leak:
Smoke/steam:
Handling change:

### Electronic evidence
Stored DTCs:
Pending DTCs:
Permanent DTCs:
Freeze frame:
Battery voltage:
ECT:
Other live data:

### Inspection
Tires/wheels:
Underbody:
Engine bay:
Fluid levels:
Belts:
Fuses:
Connectors:

### Field action
Temporary repair performed:
Parts/material used:
Safety classification:
Test performed:
Result:

### Follow-up
Vehicle driven after repair? yes/no
Distance driven:
Permanent repair required:
Permanent repair completed:
Notes:
```

---

# 30. Machine-Readable Summary

```yaml
vehicle:
  year: 2014
  make: Hyundai
  model: Accent
  trim: SE
  body: 5-door
  engine: 1.6L Gamma GDI
  transmission: 6-speed automatic

field_repair_philosophy:
  goal: "stabilize safely, diagnose, reach proper repair"
  temporary_repair_is_permanent: false
  preserve_diagnostic_evidence: true

red_no_drive:
  - brake_fluid_leak
  - major_braking_loss
  - fuel_leak
  - gdi_high_pressure_damage
  - electrical_smoke_or_melting
  - oil_pressure_warning_engine_running
  - severe_mechanical_noise
  - active_overheat_with_steam_or_major_coolant_loss
  - broken_water_pump_drive_belt
  - unsafe_steering
  - loose_or_structurally_damaged_wheel_or_suspension
  - unsafe_tire_without_replacement
  - major_atf_leak
  - fire

compact_spare:
  size: "T125/80D15"
  pressure_psi: 60
  max_speed_mph: 50
  temporary_only: true
  source: "2014 Hyundai Accent owner manual"

road_wheel:
  se_tire: "P195/50R16"
  lug_torque_lbft:
    min: 65
    max: 79
  lug_torque_nm:
    min: 88
    max: 107

jump_start:
  system_voltage: 12
  automatic_push_start_allowed: false
  final_negative_connection: "solid stationary metallic ground away from discharged battery"

cooling:
  broken_water_pump_belt_action: "stop engine immediately"
  hot_radiator_cap_removal_allowed: false
  normal_coolant: "ethylene-glycol based, aluminum-compatible"
  water_quality: "deionized or soft water"
  antifreeze_percent_range:
    min: 35
    max: 60

tire_mobility_kit_if_equipped:
  sidewall_repair_allowed: false
  max_speed_mph: 50
  max_temporary_distance_miles: 120

emergency_flat_tow_automatic:
  direction: "from front"
  transmission: "Neutral"
  max_speed_mph: 10
  max_distance_miles: 1
  if_atf_leaking: "flatbed or towing dolly"

prohibited_field_repairs:
  - brake_line_hose_bypass
  - gdi_high_pressure_fuel_patch
  - higher_amp_fuse_substitution
  - fuse_bypass_with_metal
  - steering_or_suspension_structural_improvisation
  - work_under_factory_jack_only
  - kinetic_recovery_from_unverified_tow_eye
```

---

# 31. Source Register

## 2014 Hyundai Accent Owner's Manual

Main manual mirror:

- https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/

Relevant searchable sections:

- Jump starting / charging: https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/?srch=charging
- Overheating / coolant: https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/?srch=engine+coolant
- Coolant specification: https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/?srch=Coolant
- Compact spare / tire size: https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/?srch=tire+size
- Wheel torque: https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/?srch=wheel+torque
- Tire Mobility Kit: https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/?srch=tire+replacement
- Fuse replacement: https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/2/?srch=fuse
- Emergency towing: https://www.carmanualsonline.info/hyundai-accent-2014-owner-s-manual/?srch=emergency+release

## NHTSA

- Tire safety / TireWise: https://www.nhtsa.gov/vehicle-safety/tires

## Hyundai service-family reference

- 2012 Accent 1.6L timing-chain procedure showing alternator belt / water-pump service relationship: https://charm.li/Hyundai/2012/Accent%20L4-1.6L/Repair%20and%20Diagnosis/Engine%2C%20Cooling%20and%20Exhaust/Engine/Timing%20Components/Timing%20Chain/Service%20and%20Repair/Repair%20Procedures/Part%201%20of%202/

---

# 32. Core Field Doctrine

```text
GET SAFE
   ↓
IDENTIFY RED CONDITIONS
   ↓
PRESERVE EVIDENCE
   ↓
STABILIZE ONLY WHAT CAN BE STABILIZED SAFELY
   ↓
TEST
   ↓
MOVE ONLY AS FAR AS THE TEMPORARY REPAIR JUSTIFIES
   ↓
PERMANENT REPAIR
   ↓
VERIFY
   ↓
LOG IT
```

**The best field repair is the one that prevents a roadside inconvenience from becoming a second failure.**
