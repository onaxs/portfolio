---
title: "Formula SAE — Electrical System"
thumbnail: "content/fsae/images/fsae_car_coverphoto.jpg"
caption: "Chief Electrical Engineer, 2022–23"
section: project
tags: [competitive]
employer: Cooper FSAE
date_start: 2022-09
date_end: 2023-05
order: 1
visible: true
---

# Formula SAE — Electrical System

I stepped up to the role of Chief Electrical Engineer at the start of 2023. What we had so far was essentially a chassis with suspension design. Over the course of 5 months I designed, iterated and tested an entire electric vehicle system.

<img src="content/fsae/images/fsae_car_coverphoto.jpg" alt="Formula SAE Vehicle" width="800">

## Battery Module Design

### Custom Fuse Design and Testing

I initially took on the challenge of designing custom battery packs because I believed I could design something cheaper and higher performing than what was offered to most FSAE teams off the shelf. One of the first challenges to solve was cell level fusing.

I designed nickel fuses for P42A 27100 battery cells, that I lasercut and then characterized through a series of fuse blowing tests.

<img src="content/fsae/images/fuse-design.png" alt="Fuse Design" width="200">

<img src="content/fsae/images/fuse-test-setup.jpg" alt="Fuse Testing Setup" width="300">
<img src="content/fsae/images/fuse-thermal.png" alt="Fuse Test Thermal" width="300">

<img src="content/fsae/images/fuse-test-results.png" alt="Fuse Test Results" width="500">

The graphs above correlate to the maximum current tests I ran. The fuse pulled 825 Amps from a Marine lead acid battery and blew in roughly 80ms. I plotted and filtered the data using Python.

### Battery Module M2

The first and second iteration of the battery pack was designed for extremely tight space constraints while still providing the performance required to excel in the competition.

<img src="content/fsae/images/m2-spot-welding.jpg" alt="Battery M2 Welding" width="640">

<img src="content/fsae/images/m2-taped.png" alt="Battery M2 CAD" width="400">

<img src="content/fsae/images/m2-assembled.png" alt="Battery M2 Assembly" width="400">

### Battery Module M3

This pack was my redesign with a higher prioritization of manufacturability, safety and structural strength.

16s 6p battery pack, capable of 15.5kW peak output (270 amps peak at 57.6 Volts). This battery pack is much faster to manufacture than my previous design. It includes flame retardant, thermal potting which ensures thermal homogeneity within the pack as well as added structural and vibration dampening benefits.

<img src="content/fsae/images/m3-photo.jpg" alt="Battery M3 Assembly" width="800">

<img src="content/fsae/images/m3-asm-cells.jpg" alt="Battery M3 Cells" width="800">

<img src="content/fsae/images/m3-cad-exploded.png" alt="Battery M3 Exploded" width="800">

<img src="content/fsae/Module_M3.glb" alt="Battery M3 3D Model" width="800">

## BMS Design

### Distributed BMS Prototype in a Night

I realized our BMS didn't have the proper Galvanic isolation between modules, so I started figuring out how to make one from scratch. I whipped up a plan for distributed and isolated balancing system using off the shelf balancing ICs (bq7 series). From conception to prototype in about 12 hours.

<img src="content/fsae/images/bms-in-night.jpg" alt="BMS Prototype" width="800">

<img src="content/fsae/images/bms-in-night-schem.png" alt="BMS Schematic" width="800">

### Final BMS Design

Assembling these boards greatly improved my SMT soldering skills.

<img src="content/fsae/images/bms-eda-ss.png" alt="BMS EDA" width="800">

## Vehicle Design

The battery pack was one of the first components I designed on the car, and I was given all the mechanical constraints and preferred specs when I joined the team. Designing the entire electrical system architecture with only the rule book as my constraints was much more difficult.

<img src="content/fsae/images/accumulator-asm-1.png" alt="Accumulator Assembly" width="800">

### Full System Design

<img src="content/fsae/images/altium-system-schematic.png" alt="System Architecture Diagram" width="800">

<img src="content/fsae/images/drawio-system.png" alt="Draw.io System Diagram" width="800">

### Contactor Controller & HV↔LV Board

This board was designed to control three contactors. Two high voltage bus contactors and one precharge that allowed for the HV bus to slow charge through a resistor before closing the main contactor.

<img src="content/fsae/images/PCB-PC.png" alt="Precharge PCB" width="800">

<img src="content/fsae/images/PCB-HVLV.png" alt="HVLV Board" width="800">

### Shutdown Circuit

This system is designed to shutdown power to the main contactors on the car whenever there is a critical fault with our main components or an operator uses a shutdown button.

<img src="content/fsae/images/PCB-SDC.png" alt="Shutdown Circuit PCB" width="800">

### Power Distribution Board

<img src="content/fsae/images/PCB-PDU.png" alt="Power Distribution Board" width="800">

### Full Harnessing Diagram

<img src="content/fsae/images/mcu-breakout-diagram.png" alt="MCU Breakout Diagram" width="800">

## Electromechanical Packaging

<img src="content/fsae/images/accum-shelf-asm.png" alt="Accumulator Shelf Assembly" width="800">

<img src="content/fsae/images/accumulator-asm-3.png" alt="Accumulator Assembly" width="800">

<img src="content/fsae/images/SDC-TSMP-busbar_box.png" alt="SDC TSMP Busbar Box" width="800">
