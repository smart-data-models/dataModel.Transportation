# dataModel.Transportation
These data models describe the main entities involved with smart applications that deal with transportation issues. This set of entities is primarily associated with the Automotive and Smart City vertical segments and related IoT applications.
When feasible, references to existing schema.org entity types and attributes are included.
These models have been devised to be as generic as possible, thus allowing to deal with different scenarios
- Traffic flow monitoring - Private Vehicles. - Public Vehicles (Buses, Trains, etc.). - Municipal Vehicles (pick up lorries, cleaning units, ...) - Special Vehicles (ambulances, fire brigades, ...)

### List of data models

The following entity types are available:
- [BikeHireDockingStation](https://github.com/smart-data-models/dataModel.Transportation/blob/master/BikeHireDockingStation/README.md). -> Many cities provide a bike hiring system for citizens. These can hire a bike base on different types of subscriptions. A bike hire docking station where subscribed users can hire and return a bike. It provides data about its main features and availability of bikes and free slots.

- [CrowdFlowObserved](https://github.com/smart-data-models/dataModel.Transportation/blob/master/CrowdFlowObserved/README.md). -> An observation related to the movement of people at a certain place and time.

- [EVChargingStation](https://github.com/smart-data-models/dataModel.Transportation/blob/master/EVChargingStation/README.md). -> A public charging station supplying energy to electrical vehicles. The charge time depends on the maximum power output of the station, the number of vehicles currently charging and the current battery level.

- [Road](https://github.com/smart-data-models/dataModel.Transportation/blob/master/Road/README.md). -> This entity contains a harmonised geographic and contextual description of a road. Roads are made up of one or more RoadSegment entities. Road segments are usually used to model the different carriageways of highways, for instance. The presence of dedicated bicycle lanes should be modelled using road segments as well. Road segments also play an important role when modelling roads with heterogeneous segments, for instance segments on which speed limits are different. This entity is primarily associated with the Automotive and Smart City vertical segments and related IoT applications. This data model has been developed in cooperation with mobile operators and the GSMA.

- [RoadSegment](https://github.com/smart-data-models/dataModel.Transportation/blob/master/RoadSegment/README.md). This entity contains a harmonised geographic and contextual description of a
road segment. A collection of road segments are used to describe a Road.
Road segments can include several lanes. This data model allows to convey
road segments made up of heterogeneous lanes (different in their usage,
speed, height, etc.). Lanes are identified by using integer numbers between
1 and n, being number 1 the lane to the right when going forwards. The
forward direction is the direction denoted by the vector which goes from the
segment"s start point to the segment"s end point. This is the same
convention as the one used by OpenStreetMap. This entity is primarily
associated with the Automotive and Smart City vertical segments and related
IoT applications. This data model has been developed in cooperation with
mobile operators and the GSMA.


- [TrafficFlowObserved](https://github.com/smart-data-models/dataModel.Transportation/blob/master/TrafficFlowObserved/README.md). TrafficFlowObserved

- [Vehicle](https://github.com/smart-data-models/dataModel.Transportation/blob/master/Vehicle/README.md). This entity models a particular vehicle model, including all properties
which are common to multiple vehicle instances belonging to such model.


- [VehicleModel](https://github.com/smart-data-models/dataModel.Transportation/blob/master/VehicleModel/README.md). This entity models a particular vehicle model, including all properties
which are common to multiple vehicle instances belonging to such model.




### Incubated data models
The list of incubated (on development) data models are:

  - [FleetVehicleOperation_incubated](https://github.com/smart-data-models/dataModel.Transportation/tree/master/FleetVehicleOperation_incubated)

  - [FleetVehicleStatus_incubated](https://github.com/smart-data-models/dataModel.Transportation/tree/master/FleetVehicleStatus_incubated)


### Contributors
[Link](https://github.com/smart-data-models/dataModel.Transportation/blob/master/CONTRIBUTORS.yaml) to the 5 current contributors of the data models of this Subject.


### Contribution
You can raise an [issue](https://github.com/smart-data-models/dataModel.Transportation/issues) or submit your [PR](https://github.com/smart-data-models/dataModel.Transportation/pulls) on existing data models


