# Student Teams

- [Student Teams](#student-teams)
  - [Great Northern Concrete Toboggan Competition (2026)](#great-northern-concrete-toboggan-competition-2026)
    - [Awards](#awards)
      - [**3rd** Overall (Out of 18)](#3rd-overall-out-of-18)
      - [**1st** Braking Performance](#1st-braking-performance)
      - [**1st** Overall Performance](#1st-overall-performance)
      - [**1st** Student Fabrication](#1st-student-fabrication)
      - [**2nd** Steering Performance](#2nd-steering-performance)
    - [Overall Design](#overall-design)
    - [Skiis](#skiis)
    - [Steering](#steering)
    - [Brakes](#brakes)
  - [Formula SAE Motorsports (Chief Electrical Engineer) (2023)](#formula-sae-motorsports-chief-electrical-engineer-2023)
    - [Battery Module Design](#battery-module-design)
      - [Custom Fuse Design and Testing](#custom-fuse-design-and-testing)
      - [Battery Module M2](#battery-module-m2)
      - [Battery Module M3](#battery-module-m3)
    - [BMS Design](#bms-design)
      - [Distributed BMS Prototype in a night (3/2/2023)](#distributed-bms-prototype-in-a-night-322023)
      - [Final BMS Design](#final-bms-design)
    - [Vehicle Design](#vehicle-design)
      - [Full System Design](#full-system-design)
      - [Contactor Controller \& HV\<-\>LV Board](#contactor-controller--hv-lv-board)
      - [Shutdown Circuit](#shutdown-circuit)
      - [Power Distribution Board](#power-distribution-board)
      - [Full Harnessing Diagram](#full-harnessing-diagram)
    - [Electromechanical Packaging](#electromechanical-packaging)
  - [Robotics](#robotics)
    - [Robot In One Night (2022)](#robot-in-one-night-2022)
    - [PID Steering Correction](#pid-steering-correction)
    - [First Robotics League (2021)](#first-robotics-league-2021)
      - [As Team Captain](#as-team-captain)
      - [As Team Member](#as-team-member)

## Great Northern Concrete Toboggan Competition (2026)

### Awards

#### **3rd** Overall (Out of 18)

#### **1st** Braking Performance

#### **1st** Overall Performance 

#### **1st** Student Fabrication 

#### **2nd** Steering Performance

### Overall Design

### Skiis 

### Steering

### Brakes


## Formula SAE Motorsports (Chief Electrical Engineer) (2023)

I stepped up to the role of Chief Electrical Engineer at the start of 2023. What we had so far was essentially a chassis with suspension design. Over the course of 5 months I designed, iterated and tested an entire electric vehicle system.

<img src="images/fsae/car-photo.jpg" alt="Formula SAE Vehicle" width="800">


### Battery Module Design

#### Custom Fuse Design and Testing

I initially took on the challenge of designing custom battery packs because I believed I could design something cheaper and higher performing than what was offered to most FSAE teams off the shelf. One of the first challenges to solve was cell level fusing.

I designed nickel fuses for P42A 27100 battery cells, that I lasercut and then characterized through a series of fuse blowing tests.

<img src="images/fsae/fuse-design.png" alt="Fuse Design" width="200">

<img src="images/fsae/fuse-test-setup.jpg" alt="Fuse Testing Setup" width="300"> 
<img src="images/fsae/fuse-thermal.png" alt="Fuse Test Thermal" width="300">

<img src="images/fsae/fuse-test-results.png" alt="Fuse Test Results" width="500">

The graphs above correlate to the maximum current tests I ran. The fuse pulled 825 Amps from a Marine lead acid battery and blew in roughly 80ms. I plotted and filtered the data using Python.

#### Battery Module M2

The first and second iteration of the battery pack was designed for extremely tight space constraints while still providing the performance required to excel in the competition.

<img src="images/fsae/m2-spot-welding.jpg" alt="Battery M2 Welding" width="640">

<img src="images/fsae/m2-taped.png" alt="Battery M2 CAD" width="400">

<img src="images/fsae/m2-assembled.png" alt="Battery M2 ASM" width="400">

#### Battery Module M3

This pack was my redesign with a higher prioritization of manufacturability, safety and structural strength.

16s 6p battery pack, capable of 15.5kW peak output (270 amps peak at 57.6 Volts). This battery pack is much faster to manufacture than my previous design. It includes flame retardant, thermal potting which ensures thermal homogeneity within the pack as well as added structural and vibration dampening benefits.

<img src="images/fsae/m3-photo.jpg" alt="Battery M3 Assembly" width="800">

<img src="images/fsae/m3-asm-cells.jpg" alt="Battery M3 Cells" width="800">

<img src="images/fsae/m3-cad-exploded.png" alt="Battery M3 Exploded" width="800">

<img src="models/Module_M3.obj" alt="Battery M3 3D Model" width="800">

### BMS Design

#### Distributed BMS Prototype in a night (3/2/2023)

I realized our BMS didn't have the proper Galvanic isolation between modules, so I started figuring out how to make one from scratch. I whipped up a plan for distributed and isolated balancing system using off the shelf balancing ICs (bq7 series). From conception to prototype in about 12 hours.

<img src="images/bms-prototype.jpg" alt="BMS Prototype" width="800">

<img src="images/bms-schematic.png" alt="BMS Schematic" width="800">

#### Final BMS Design

Assembling these boards greatly improved my SMT soldering skills.

<img src="images/bms-pcb-front.png" alt="BMS PCB Front" width="800">

<img src="images/bms-pcb-back.png" alt="BMS PCB Back" width="800">

<img src="images/bms-installed.png" alt="BMS Installed" width="800">

### Vehicle Design

The battery pack was one of the first components I designed on the car, and I was given all the mechanical constraints and preferred specs when I joined the team. Designing the entire electrical system architecture with only the rule book as my constraints was much more difficult.

<img src="images/accumulator-assembly.png" alt="Accumulator Assembly" width="800">

#### Full System Design

Below is one of my first sketches of the full system design. I used Altium and draw.io to iterate through and communicate system architecture decisions.

<img src="images/system-architecture-sketch.png" alt="System Architecture Sketch" width="800">

<img src="images/system-architecture.png" alt="System Architecture Diagram" width="800">

<img src="images/ecu-system.png" alt="ECU System" width="800">

#### Contactor Controller & HV<->LV Board

This board was designed to control three contactors. Two high voltage bus contactors and one precharge that allowed for the HV bus to slow charge through a resistor before closing the main contactor.

<img src="images/contactor-controller.png" alt="Contactor Controller" width="800">

<img src="images/hvlv-board.png" alt="HVLV Board" width="800">

#### Shutdown Circuit

This system is designed to shutdown power to the main contactors on the car whenever there is a critical fault with our main components or an operator uses a shutdown button.

<img src="images/shutdown-circuit.png" alt="Shutdown Circuit" width="800">

#### Power Distribution Board

<img src="images/power-distribution.png" alt="Power Distribution Board" width="800">

#### Full Harnessing Diagram

This was a diagram I did containing every connection and pin throughout the car.

<img src="images/harness-diagram.png" alt="Harness Diagram" width="800">

<img src="images/harness-detail.png" alt="Harness Detail" width="800">

### Electromechanical Packaging

<img src="images/packaging-overview.png" alt="Packaging Overview" width="800">

<img src="images/packaging-assembly.png" alt="Packaging Assembly" width="800">

**Contactor Assembly:** With precharge circuit, galvanically isolated voltage measurement, DCDC, main fuse, current sensors. All fasteners were also insulated.

<img src="images/contactor-assy.png" alt="Contactor Assembly" width="800">

**HV Box:** Designed with the goal of making competition inspection easy. Houses the capacitance discharge circuit, current sensor and voltage taps.

<img src="images/hv-box.png" alt="HV Box" width="800">

---

## Robotics 

### Robot In One Night (2022)

I designed, printed, programmed and built this little bottle cap stacking mecanum robot in one night for a college competition.

<img src="models/robot-one-night.glb" alt="Robot Model" width="800">

**Rack and pinion mechanism in action:**

<img src="images/rack-pinion.gif" alt="Rack and Pinion" width="800">

### PID Steering Correction

<img src="images/pid-steering.gif" alt="PID Steering Demo" width="800">

### First Robotics League (2021)

#### As Team Captain

During my senior year of high school (2020 COVID), I led a team in remotely creating an almost fully 3D printed Robot. We built the robot with less than half the budget the team is usually allotted. I slept with 3D printers running 24/7 for a couple months.

<img src="images/frc-senior-1.png" alt="FRC Senior Bot 1" width="800">

<img src="images/frc-senior-2.png" alt="FRC Senior Bot 2" width="800">

<img src="images/frc-senior-test-1.gif" alt="FRC Senior Test 1" width="800">

<img src="images/frc-senior-test-2.gif" alt="FRC Senior Test 2" width="800">

<img src="images/frc-senior-complete.png" alt="FRC Senior Complete" width="800">

Together we were able to build 5 large mechanisms in separate homes and then bring those together in mine for a full robot.

<img src="images/frc-mechanisms.png" alt="FRC Mechanisms" width="800">

<img src="images/frc-mechanism-test.gif" alt="FRC Mechanism Test" width="800">

<img src="images/frc-assembly.png" alt="FRC Assembly" width="800">

#### As Team Member

Junior year of high school, this robot taught me to CAD. I designed the chassis, the roller intake and did the full 1200 part assembly for my team.

<img src="models/frc-junior-full.glb" alt="FRC Junior Model" width="800">

<img src="images/frc-junior-1.png" alt="FRC Junior Photo 1" width="800">

<img src="images/frc-junior-2.png" alt="FRC Junior Photo 2" width="800">

<img src="images/frc-junior-3.png" alt="FRC Junior Photo 3" width="800">

**Embedded tank drive:**

<img src="images/tank-drive.png" alt="Tank Drive Photo" width="800">

<img src="models/tank-drive.glb" alt="Tank Drive Model" width="800">

**Roller Intake:**

<img src="models/roller-intake.glb" alt="Roller Intake Model" width="800">