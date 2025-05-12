# 5e d6 (working title)

Release 0



An in-progress fantasy miniatures wargame. 

5e d6 is licensed under the Creative Commons Attribution 4.0 International License. 

>  This work includes material from the System Reference Document 5.2 (“SRD 5.2”) by Wizards of the Coast LLC, available at https://www.dndbeyond.com/srd. The SRD 5.2 is licensed under the Creative Commons Attribution 4.0 International License, available at https://creativecommons.org/licenses/by/4.0/legalcode.

# Playing the game

The game is divided into rounds, and each round has two phases in this order: Movement and Combat. 

During each round, each figure has a chance to move and a chance to attack. 

Once the Combat phase is complete, start a new round.

Each roll a die to see who is the Lead Player for round 1. Then alternate Lead Player in subsequent rounds. The Lead Player gets to go first in the case of some ties. 

# Movement Phase

Players move the figures they control, starting with those with the lowest Speed, then the next lowest Speed, and so on until all figures have had the chance to move. 

When figures from different forces have the same Speed, the Lead Player moves their figures first.

Players can move figures they control with the same Speed in any order. 

*For example, Bob has two Speed 6 elves and a Speed 5 dwarf. Anne has a Speed 5 dwarf. Bob is the Lead Player. Bob moves his dwarf first. Then Anne moves her dwarf. Then Bob moves his two elves, in either order.*

Figures can move up to their Speed in inches. They do not have to move at all. Turning on the spot takes no movement. 

Figures can move through allies, but cannot end their turn with their base overlapping an ally’s base. They cannot move through enemies. 

**Tight spaces:** Figures can move through tight spaces that are at least as wide as half their height, but must end their turn in open space. 

**Preparing to shoot:** A creature that wants to shoot a bow or gun in the Combat Phase must spend half its Speed in movement preparing to shoot. 

**Prone:** A creature that is prone cannot move willingly. When it would otherwise be able to move, a prone creature can spend half its Speed in movement to stand up. 

*For example, Bob's elf has Speed 6 so he would normally be able to move it up to 6 inches. But the elf is prone. The elf spends 3" worth of movement standing up from prone. Bob could move the elf 3", but he wants the elf to shoot her bow later. So instead of moving the elf at all, he spends the movement preparing the elf to shoot.*

## Movement Actions

A figure can take one action per round, either a movement action in the Movement Phase or a combat action in the Combat Phase. 

A figure's profile may have other actions. Any figure can take any of the movement actions listed below: 

* **Dash:** The figure may move an additional distance in inches up to its Speed. 

* **Disengage:** The creature’s movement this phase does not provoke opportunity attacks. 

* **Dodge:** Until the end of the round, attacks against the creature are made with disadvantage and the creature has advantage on Reflex saves. 

## Threatened spaces and opportunity attacks

A figure threatens the space within 1” of the rim of its base. 

When one figure moves out of another figure’s threatened space, the second figure can immediately make an opportunity attack against the moving figure. This is a single melee attack, made with a melee weapon of the second figure's choice (among those they are equipped with). 

This is a reaction (each figure usually only gets one reaction per phase).

Forced movement and teleportation do not trigger an opportunity attack.

## Figures

A figure’s base size is based on their size: 

* 20mm: Tiny

* 20mm–25mm: Small

* 25mm–32mm: Medium

* 40mm: Large

* 60mm: Huge

* 80mm: Gargantuan

# Combat Phase

Make attacks with figures, starting with those with the highest Fight, then the next highest Fight, and so on until all figures have had the chance to attack. 

When figures from different forces have the same Fight, the Lead Player attacks with their figures first.

## Attacking

As their combat action, a creature can make a number of attacks equal to their Attack stat. 

Each attack can be with the same or a different weapon, among those the figure is equipped with.

For each attack, choose a target within range (ranged weapon) or reach (melee weapon). If not listed, a melee weapon’s reach is 1”. 

Range and reach are measured from any point on the edge of attacker’s base.

**To-hit roll:** Roll 1d6 per attack. The target number is the attacker’s Fight score minus the target’s Armor. Any die result that is equal or below the target number is a hit. 

*For example, a hobgoblin with Fight 5 makes one attack against a guard with Armor 1.* 

*The target number is 4 (5 minus 1). If the result of the die roll is 1, 2, 3 or 4, the attack hits.* 

Each hit does one Damage, unless otherwise specified. 

### Ranged attacks

Targets must be within range and line of sight. 

**Block:** Count each bit of cover, concealment or other model between the shooter and the target, other than those adjacent to the shooter. 

Make one block check for each, working from the shooter towards the target. If the target is mounted, the mount blocks too. Then if the target is in melee, make a final block check. 

On a 1–2, the shot hits that cover or model instead, or just misses in the case of concealment. Work from the shooter towards the target. 

**Close Combat Ranged Attacks:** An attacker that is threatened by an enemy suffers disadvantage on their ranged attack. 

**Long Range Attacks:** Ranged attacks have a short and long range listed (in the form 6”/12”, where the former is the short range and the latter the long range). Treat an attacker at long range's Fight score as one lower (Fight 5 becomes 4, for example) for the purpose of calculating the target number for attacks. 

### Melee attacks

Targets must be within reach. If the attacker does not have line of sight to the target, they attack with disadvantage. 

**Flanking:** When the target of a melee attack is flanked (the attacker and their ally are both within reach of the target, and are on opposite sides of the target), treat the attacker’s Fight score as one higher (Fight 5 becomes 6, for example) for the purpose of calculating the target number for attacks. 

## Damage

Each time a creature is hit, they risk taking a wound. The number of wounds they risk is equal to the attack's Damage. Normally an attack does 1 Damage; the attacker's profile will say if some of their attacks do more Damage. 

**To-wound roll:** The attacker rolls 1d6 per point of Damage per hit. 

Compare the Strength of the attack to the Toughness of the target to find the target number. 

Every result that is equal to or below this number is a wound. 

When a value has a slash, like "1/3", it means if the attacker rolls a 1, they reroll the die. Only if the result of the reroll is the second number is there a wound.

*For example, Bob's orc hits with an attack that does 2 Damage. The orc has Str 2 and the target has Tough 7, in other words the target number is "1/3". Bob rolls 2 dice. One is a "1", so he rerolls it. The reroll is a 3, so the target takes 1 wound.*

|               | Strength |       |       |       |       |       |       |       |       |        |
| ------------- | -------- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ------ |
| **Toughness** | **1**    | **2** | **3** | **4** | **5** | **6** | **7** | **8** | **9** | **10** |
| **1**         | 3        | 4     | 4     | 5     | 5     | 6     | 6     | 6     | 6     | 6      |
| **2**         | 2        | 3     | 4     | 4     | 5     | 5     | 6     | 6     | 6     | 6      |
| **3**         | 2        | 2     | 3     | 4     | 4     | 5     | 5     | 6     | 6     | 6      |
| **4**         | 1        | 2     | 2     | 3     | 4     | 4     | 5     | 5     | 6     | 6      |
| **5**         | 1        | 1     | 2     | 2     | 3     | 4     | 4     | 5     | 5     | 6      |
| **6**         | 1/3      | 1     | 1     | 2     | 2     | 3     | 4     | 4     | 5     | 5      |
| **7**         | 1/3      | 1/3   | 1     | 1     | 2     | 2     | 3     | 4     | 4     | 5      |
| **8**         | 1/2      | 1/3   | 1/3   | 1     | 1     | 2     | 2     | 3     | 4     | 4      |
| **9**         | 1/2      | 1/2   | 1/3   | 1/3   | 1     | 1     | 2     | 2     | 3     | 4      |
| **10**        | 1/1      | 1/2   | 1/2   | 1/3   | 1/3   | 1     | 1     | 2     | 2     | 3      |



**Wounds:** Once a creature has taken wounds equal to or exceeding their Health, they are eliminated and removed from play. 

# Reactions

Each phase, each figure can take one reaction. A figure cannot take the same reaction in both phases. “Movement reactions” can only be taken during the movement phase; “combat reactions” can only be taken during the combat phase. 

Opportunity attacks (described above) are a movement reaction. Masteries (described below) are a combat reaction. 

## Weapon Masteries 

Figures that are equipped with a spear, blade, bludgeon or exotic weapon can use the Weapon Mastery associated with that weapon. Figures equipped with a shield can use Shield Mastery. Figures wielding two of the same hand weapon (two blades or two bludgeons, for example) can use Dual Wielding Mastery (as well as the mastery of their hand weapon, for example Blade Mastery if they are wielding two blades). 

Weapon Masteries are reactions, which means a figure can use at most one per phase. 

**Spear Mastery:** You attack first, regardless of Fight value. 

**Blade Mastery:** If a melee attack you make hits, make a melee attack with the same weapon against a creature that is within 1” of you. That attack is at Strength -2. 

**Bludgeon Mastery:** If an attack you make misses, you still do damage at Strength -2 (no other effects of your attack apply). 

**Dual Wielding Mastery:** Immediately make an attack with a light weapon against a target of your choice. 

**Shield Mastery:** Make an attacker reroll one hit against you. 

If you have a ranged weapon, you can only use a shield against melee attacks. If you have a great weapon, you can only use a shield against ranged attacks.

**Exotic Mastery:** If you hit a creature with this weapon, it falls prone. 

## Combat Maneuver

As their combat action, instead of attacking a figure can choose to perform a combat maneuver on a target within 1". A combat maneuver can only target a creature smaller than the user (as measured by base size):

**Grapple:** The target makes a saving throw. On a failure, they gain the grappled condition. 

**Shove:** The target makes a saving throw. On a failure, they are pushed 1”. 

**Trip:** The target makes a saving throw. On a failure, they fall prone. 

# Advantage and disadvantage

**Rolling with advantage** means rerolling any failures once and taking the second result. 

**Rolling with disadvantage** means rerolling any successes once and taking the second result. 

**Disadvantage and advantage from different sources** cancel each other out, so for example if you have advantage from two sources and disadvantage from one, you roll with advantage.

Even if you have multiple sources of advantage, you only ever reroll once. 

**When a figure has advantage or disadvantage on an attack,** the advantage applies to the to-hit roll, *not* to the to-wound roll. In other words, it applies to the roll that is compared to the attacker's Fight, not the roll that is compared to Strength vs Toughness. 

# Converting from 5e

5e d6 converts 5e into a miniatures game. Follow the rules below to convert any creature: 

| Attack/Save    | Fight/Save |
| -------------- | ---------- |
| +0 to +2       | 3          |
| +3 to +5       | 4          |
| +6 to +8       | 5          |
| +9 to +11      | 6          |
| +12 and higher | 7          |

 

| AC/DC         | Armor/Difficulty       | Armor |
| ------------- | ---------------------- | ----- |
| 6 to 10       | N/A – attacks auto-hit |       |
| 11 to 13      | 0                      | None  |
| 14 to 16      | 1                      | Light |
| 17 to 19      | 2                      | Heavy |
| 20 to 22      | 3                      |       |
| 23 and higher | 4                      |       |

 

**HP:** HP turns into Toughness *and* Health. Decide how much Health you want the figure to have, divide HP by that amount and use the new total to calculate Toughness. 

For example, an aboleth has 171 HP. I assign it 4 Health; 171 divided by 4 is 43: so I give it Toughness 8. 

| HP   | Toughness |
| ---- | --------- |
| 4    | 1         |
| 9    | 2         |
| 12   | 3         |
| 15   | 4         |
| 20   | 5         |
| 26   | 6         |
| 33   | 7         |
| 43   | 8         |
| 56   | 9         |
| 73   | 10        |

 

**Damage:** Decide how much Damage you want the attack to do (normally 1). Divide the average damage in 5e by that much, then compare to the table below. 

For example, an aboleth does 19 damage with its tentacle. So it has Strength 8. 

| Damage | Strength |
| ------ | -------- |
| 3      | 1        |
| 4      | 2        |
| 5      | 3        |
| 7      | 4        |
| 9      | 5        |
| 11     | 6        |
| 14     | 7        |
| 19     | 8        |
| 24     | 9        |
| 32     | 10       |

 # Troops

| **Name**          | **Spd** | **Fight** | **Armor** | **Tough** | **Health** | **Attacks** | **Str** | **Fort** | **Ref** | **Will** | **Points** | **Atts**                                                     |
| ----------------- | ------- | --------- | --------- | --------- | ---------- | ----------- | ------- | -------- | ------- | -------- | ---------- | ------------------------------------------------------------ |
| **Dwarf**         | 5       | 4         | 0         | 7         | 1          | 1           | 3       | 3        | 3       | 3        | 8          | *Sturdy* No Speed penalty for heavy armor "<br />"**Hand Weapon** |
| **Elf**           | 6       | 4         | 0         | 4         | 1          | 2           | 3       | 3        | 3       | 3        | 8          | *Wilderness Stride* No penalty from difficult terrain caused by vegetation <br />**Hand Weapon** |
| **Goblin**        | 6       | 4         | 0         | 2         | 1          | 1           | 2       | 3        | 3       | 3        | 2          | *Climb, Pack Tactics* <br />**Hand Weapon**                  |
| **Halfling**      | 5       | 4         | 0         | 3         | 1          | 1           | 3       | 3        | 3       | 3        | 4          | *Sneak Attack* Weapon hits with advantage get +1 Str Movement reaction: *Nimble Escape* Disengage or Hide <br />**Hand Weapon** |
| **Human Levy**    | 6       | 4         | 0         | 3         | 1          | 1           | 2       | 3        | 3       | 3        | 2          | **Hand Weapon**                                              |
| **Human Soldier** | 6       | 4         | 0         | 4         | 1          | 1           | 3       | 3        | 3       | 3        | 4          | **Hand Weapon**                                              |
| **Orc**           | 6       | 4         | 0         | 3         | 1          | 1           | 5       | 4        | 3       | 2        | 4          | *Pack Tactics* <br />**Hand Weapon**                         |

* By default, soldiers begin with a **hand weapon** (costing no points). Choose its type: Blade, Bludgeon, Spear or Exotic. 

* A soldier with two **hand weapons** **of different types** can choose between their special effects (called “masteries”). A soldier with two **hand weapons of the same type** can make an extra attack with the second. 

| **Weapon**       | **Points**                     | **Strength modifier** | **Details**                      |
| ---------------- | ------------------------------ | --------------------- | -------------------------------- |
| **Great Weapon** | 2 (1 if replacing hand weapon) | +1                    | Blade, Bludgeon, Spear or Exotic |
| **Hand Weapon**  | 1                              |                       | Blade, Bludgeon, Spear or Exotic |
| **Daggers**      | 1 (0 if replacing hand weapon) | -1                    | Melee or ranged 2”/4”            |
| **Javelin**      | 1                              |                       | Ranged 4”/8”                     |
| **Bow**          | 3                              |                       | Ranged 12”/24”                   |

 

| **Armor**       | **Points**                     | **Details**                   |
| --------------- | ------------------------------ | ----------------------------- |
| **Light Armor** | 1                              | +1 Armor while worn           |
| **Heavy Armor** | 2 (1 if replacing light armor) | +2 Armor, -1 Speed while worn |
| **Shield**      | 1                              | Shield Mastery                |

 