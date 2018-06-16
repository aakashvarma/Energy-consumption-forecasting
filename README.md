# Energy-consumption-forecasting

### DATASET
Link to the dataset is given below: https://archive.ics.uci.edu/ml/datasets/individual+household+electric+power+consumption

### Attribute Information:

1. date: Date in format dd/mm/yyyy 
2. time: time in format hh:mm:ss 
3. global_active_power: household global minute-averaged active power (in kilowatt) 
4. global_reactive_power: household global minute-averaged reactive power (in kilowatt) 
5. voltage: minute-averaged voltage (in volt) 
6. global_intensity: household global minute-averaged current intensity (in ampere) 
7. sub_metering_1: energy sub-metering No. 1 (in watt-hour of active energy). It corresponds to the kitchen, containing mainly a dishwasher, an oven and a microwave (hot plates are not electric but gas powered). 
8. sub_metering_2: energy sub-metering No. 2 (in watt-hour of active energy). It corresponds to the laundry room, containing a washing-machine, a tumble-drier, a refrigerator and a light. 
9. sub_metering_3: energy sub-metering No. 3 (in watt-hour of active energy). It corresponds to an electric water-heater and an air-conditioner.

### PROBLEM APPROACHED AND SOLUTION:
We consider the problem of power demand forecasting in residential micro-grids. In the last few years, the raising concern for greenhouse gas emissions, the growth in the electrical power demand, the diffusion of domestic generation plants based of renewables, and the integration of sensing and metering devices into power distribution grids has led to the deployment of several smart grids around the world.
Approaches using support vector machines, that perform one-step ahead predictions have been proposed in the literature. 

NOTICE: Not all predictions are very accurate. A hybrid approach, that is driven by the prediction interval, the target error, and its uncertainty, is then recommended.    