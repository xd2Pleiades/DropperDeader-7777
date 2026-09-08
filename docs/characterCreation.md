# Character Creation

## Overview

Character Creation is divided into two primary panels:

* **Left Panel:** Persistent Character Information
* **Right Panel:** Character Life Simulation

The left panel displays the character's current state and accumulated information.

The right panel progresses the character through their life, presenting decisions and random events that shape the
character over time.

---

# Left Panel — Character Information

The Left Panel contains the character's persistent information.

## SSA Registration

Contains the character's official registration information.

* SSA Registration Number
* Full Name
* Date of Birth
* Place of Birth
* Planet
* Region
* District
* Microdistrict
* Citizenship / Registration Status

---

## Health

Contains the character's current and historical health information.

* General Health
* Physical Health
    * Physical Build
        * Limb by Limb breakdown
            * Organ by Organ breakdown
* Mental Health
* Conditions
* Injuries
* Health History
* Genetic Disposition

---

## Personality

Contains the character's current personality profile.

* Core Personality Traits
* Temperament
* Behavioral Tendencies
* Personality Development
* Preferences
* Dislikes

Personality may change as a result of:

* Player decisions
* Random Events
* Relationships
* Education
* Employment
* Other life experiences

---

## Traits & Skills

Contains the character's abilities and personal characteristics.

### Traits

Examples include:

* Ambitious
* Introverted
* Extroverted
* Creative
* Analytical
* Compassionate
* Risk-Taking

### Skills

Examples include:

* Communication
* Engineering
* Medicine
* Mathematics
* Athletics
* Cooking
* Programming

### Hobbies

Examples include:

* Music
* Sports
* Reading
* Art
* Gaming
* Science
* Travel

Traits, skills, and hobbies may develop or change during the life simulation.

---

## Relations

Contains the character's relationships with other individuals.

* Parents
* Siblings
* Extended Family
* Friends
* Partners
* Children
* Colleagues
* Other Significant Relationships

Relationships may be created, strengthened, weakened, or lost through life events.

---

## Inventory

Contains the character's possessions and financial information.

### Finances

* Cash
* Bank Balance
* Income
* Savings
* Debt
* Other Financial Assets

### Items

* Personal Items
* Tools
* Electronics
* Collectibles
* Important Objects

### Clothing

* Everyday Clothing
* Formal Clothing
* Work Clothing
* Seasonal Clothing
* Special Clothing

Inventory may change as a result of purchases, employment, gifts, losses, and random events.

---

## Background

Contains the character's accumulated life history.

* Family Background
* Education
* Employment History
* Major Life Events
* Achievements
* Failures
* Important Experiences
* Other Background Information

The Background should function as a summary of the character's life rather than a duplicate of the other tabs.

---

# Right Panel — Life Simulation

The Right Panel controls the progression of the character through their life.

The simulation is **age-based** rather than divided into predefined life stages.

The character begins at their generated Date of Birth and progresses through increasing ages.

---

## Age Progression

The simulation advances the character's age over time.

Each age may introduce:

* Decisions
* Opportunities
* Relationships
* Education
* Employment
* Financial changes
* Personality changes
* Random Events

Not every age needs to contain an event.

The purpose of the simulation is to create a believable life history without requiring the player to make a decision for
every single year.

---

# Random Events

Random Events are the primary mechanism for generating unexpected experiences during the character's life.

Events should be influenced by the character's existing state where appropriate.

Potential factors include:

* Age
* Personality
* Traits
* Skills
* Hobbies
* Health
* Education
* Employment
* Finances
* Relationships
* Previous Events
* Location
* Other Character Data

---

## Number of Random Events

The player should receive a limited number of Random Events during each applicable period of the simulation.

The number of events should be:

**1–3 Random Events**

The exact number is randomly determined.

This is intentionally limited to prevent the character creation process from becoming overwhelming.

### Example

```text
Random Events Available: 2
```

The player is then presented with two events.

```text
Event 1
────────────────────────
Your character joined a
local sports club at age 14.

[Accept]
```

```text
Event 2
────────────────────────
Your character received an
unexpected financial gift.

[Accept]
```

Once the available events have been resolved, the simulation continues.

---

# Event Selection

Random Events should not necessarily be completely random.

The event generator may use the character's existing information to determine which events are appropriate.

For example:

```text
Character:
- Age: 24
- Trait: Ambitious
- Skill: Engineering
- Hobby: Robotics
- Education: Technical
```

This character may have a higher chance of receiving events related to:

* Career opportunities
* Engineering projects
* Professional networking
* Technical competitions
* Further education
* Entrepreneurship

The event system should therefore support **weighted and conditional events**.

---

# Event Outcomes

Events may modify one or more aspects of the character.

Possible outcomes include:

* Personality changes
* Trait changes
* Skill increases/decreases
* New hobbies
* Relationship changes
* Health changes
* Financial changes
* Inventory changes
* Education changes
* Employment changes
* New background entries
* New opportunities
* Future event modifiers

An event may also have no significant mechanical effect and exist primarily to enrich the character's history.

---

# Event History

Resolved events should be recorded in the character's Background.

Each recorded event should contain, where appropriate:

* Age
* Event Name
* Description
* Outcome
* Significant Changes

Example:

```text
Age 17 — Technical Competition

Participated in a regional engineering competition.

Outcome:
- Engineering +2
- Met Alex
- Added "Engineering Competition" to Background
```

---

# Character Creation Flow

The overall character creation process should follow this general structure:

```text
Generate Character
       │
       ▼
Generate SSA Registration
       │
       ▼
Generate Basic Character Information
       │
       ▼
Generate Initial Traits / Personality
       │
       ▼
Generate Origin
       │
       ▼
Begin Age Progression
       │
       ▼
     Age +
       │
       ▼
Determine Relevant Events
       │
       ▼
Generate 1–3 Random Events
       │
       ▼
Player Resolves Events
       │
       ▼
Apply Outcomes
       │
       ▼
Update Character Information
       │
       ▼
     Age +
       │
       ▼
Repeat
       │
       ▼
Character Complete
```

---

# Design Principle

The character sheet and life simulation should remain separate concepts.

### Left Panel

> **Who is this character?**

Displays the character's current state.

### Right Panel

> **What happens to this character?**

Controls the progression of their life and presents decisions and events.

The Right Panel changes the character.

The Left Panel reflects those changes.

This separation should remain consistent as additional character systems are introduced.
