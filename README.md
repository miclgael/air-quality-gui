# AQI Pollutant Calculator (GUI)

> 💡 This simple python program was written for a first year comp-sci assignment and serves no real-world purpose. This is part 3 of a series, [part 1](https://github.com/miclgael/air-quality) and [part 2](https://github.com/miclgael/air-quality-fs) are available if interested.

This GUI version of the AQI calculator program was designed for use by Codetown council workers in various parts of the city to collect air quality information, which will be used to help make informed decisions for future changes in the town.

## Table of Contents

- [AQI Pollutant Calculator (GUI)](#aqi-pollutant-calculator-gui)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Example Usage](#example-usage)
  - [Walk-through Guide](#walk-through-guide)
  - [Calculation Details](#calculation-details)
  - [Acknowledgement](#acknowledgement)

## Installation

This program makes use of the `tkinter` package. Installation instructions for `tkinter` vary by operating system and are beyond the scope of this README. 

This program was designed to run optimally with `Python 3.8.2`

## Usage

To run the program, enter the following commands into your terminal prompt

1. Change to the directory where the application is installed with `cd /<PATH>/<TO>/<PROGRAM>/air-quality-gui`
2. Start the program with `python3 aqigui.py` 
3. Enter inputs into the fields provided. 

## Example Usage

```bash
$ python3 aqigui.py
```

![](images/AQIGUI_state0.png) <br>_The program in its default state_

![](images/AQIGUI_state1.png) <br>_The program producing a result_

![](images/AQIGUI_state2.png) <br>_The program resized for smaller screens_

![](images/AQIGUI_state_err.png) <br>_The program throwing an error_

## Walk-through Guide

The program presents the user with three (3) labelled fields in which to enter air quality measurements for a single site.

The program takes the given inputs to collect the amount of ozone (parts per hundred million), sulfur dioxide (parts per hundred million), and particles less than 2.5 micrometers diameter (micrograms per cubic metre).

Upon pressing the 'Calculate AQI' button, the program will output the air quality index (AQI) for that measurement (using the calculation below).

## Calculation Details

`AQI_pollutant = 100*(pollutant data reading)/standard`, where `pollutant data reading` is the value entered by the user for that pollutant and the standard value for each pollutant is given in the following table.

_The following table can be used to reference standard pollutant values:_

| Pollutant      | Standard value                                                  |
| -------------- | --------------------------------------------------------------- |
| Ozone          | 8.0 parts per hundred million                                   |
| Sulfur dioxide | 20 parts per hundred million                                    |
| Particles      | less than 2.5 micrometre diameter 25 micrograms per cubic metre |

## Acknowledgement

Thanks to **@dpaul4** for providing the AQI calculation algorithm

Colour palette generated with [Coolors.co](https://coolors.co/540d6e-ee4266-ffd23f-f3fcf0-1f271b)

