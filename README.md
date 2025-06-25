# dataModel.Transportation
These data models describe the main entities involved with smart applications that deal with transportation issues. This set of entities is primarily associated with the Automotive and Smart City vertical segments and related IoT applications.
When feasible, references to existing schema.org entity types and attributes are included.
These models have been devised to be as generic as possible, thus allowing to deal with different scenarios
- Traffic flow monitoring - Private Vehicles. - Public Vehicles (Buses, Trains, etc.). - Municipal Vehicles (pick up lorries, cleaning units, ...) - Special Vehicles (ambulances, fire brigades, ...)

### List of data models

The following entity types are available:
- [AnonymousCommuterId](https://github.com/smart-data-models/dataModel.Transportation/blob/master/AnonymousCommuterId/README.md). Anonymized identifier for flow monitoring. Includes an origin and destiny property to map its path.

- [AnprFlowObserved](https://github.com/smart-data-models/dataModel.Transportation/blob/master/AnprFlowObserved/README.md). The data model represents an observation linked to the passing of a vehicle at a certain location and at a given time. This Data Model is based on the [dataModel.Transportation/ItemFlowObserved], extended with ANPR specific properties and links to the observation images.

- [APDSObservation](https://github.com/smart-data-models/dataModel.Transportation/blob/master/APDSObservation/README.md). This entity models a particular observation of a set of ANPR camera. The Observation might be done with several ANPR cameras, but is limited to the observation of ONE vehicle. It implements the APDS data model https://www.allianceforparkingdatastandards.org/

- [BikeHireDockingStation](https://github.com/smart-data-models/dataModel.Transportation/blob/master/BikeHireDockingStation/README.md). Bike Hire Docking Station

- [BikeLane](https://github.com/smart-data-models/dataModel.Transportation/blob/master/BikeLane/README.md). A generic bike lane schema

- [CityWork](https://github.com/smart-data-models/dataModel.Transportation/blob/master/CityWork/README.md). The Data Model is a contextual description of urban works carried out on a road axis and which can impact individual (Cars, motorcycle, bicycles, .…) or common transport (Tram, Bus, subway). It contains a geographic representation making it possible to locate its work from a specific JSON Object and at a more global level (Road segment, Road, District, ...) in order to assess the potential impacts on the circulation. A GeoJSON object may represent a region of space (a Geometry), a spatially-bounded entity (a Feature), or a list of features (a Feature Collection). refer to the document [geojson](https://tools.ietf.org/pdf/draft-ietf-geojson-03.pdf) for more information about the modeling and the possible value.

- [CrowdFlowObserved](https://github.com/smart-data-models/dataModel.Transportation/blob/master/CrowdFlowObserved/README.md). CrowdFlowObserved

- [EVChargingStation](https://github.com/smart-data-models/dataModel.Transportation/blob/master/EVChargingStation/README.md). EV Charging Station

- [FareCollectionSystem](https://github.com/smart-data-models/dataModel.Transportation/blob/master/FareCollectionSystem/README.md). A public transit fare collection system Data Model

- [FleetVehicle](https://github.com/smart-data-models/dataModel.Transportation/blob/master/FleetVehicle/README.md). This entity contains a harmonised description of a generic fleet vehicle such as a delivery vehicle, an ambulance or a postal vehicle. This entity is primarily associated with the vertical segment of the transport and logistics but may also be used many other related IoT applications.

- [FleetVehicleOperation](https://github.com/smart-data-models/dataModel.Transportation/blob/master/FleetVehicleOperation/README.md). This entity contains a harmonised description of a generic fleet vehicle operation such as a delivery, or a postal collection. This entity is primarily associated with the vertical segment of the transport and logistics but may also be used many other related IoT applications.

- [FleetVehicleStatus](https://github.com/smart-data-models/dataModel.Transportation/blob/master/FleetVehicleStatus/README.md). This entity contains a harmonised description of the status of a generic fleet vehicle. This entity is primarily associated with the vertical segment of the transport and logistics but may also be used many other related IoT applications.

- [ItemFlowObserved](https://github.com/smart-data-models/dataModel.Transportation/blob/master/ItemFlowObserved/README.md). The data model intended to measure an observation linked to the movement of an item at a certain location and over a given period. This Data Model proposes an evolution of two Data Model by merging them and integrating all the attributes of the initial version of [TrafficFlowObserved] and [CrowFlowObserved] and by extension any type of item that we want to analyze the movements. Attributes `vehicleType` and `vehicleSubType` are removed from the initial data Model in order to become generic `itemType` and `itemSubType` of possible values. (people, Type of vehicle, Type of boat, Type of plane, ...).

- [RestrictedTrafficArea](https://github.com/smart-data-models/dataModel.Transportation/blob/master/RestrictedTrafficArea/README.md). An area of a city in which the traffic generated by cars or any other kind of vehicles is subjected to limitation.

- [RestrictionException](https://github.com/smart-data-models/dataModel.Transportation/blob/master/RestrictionException/README.md). A Restriction Exception represents a particular case that specialise restriction reported in a Restricted Traffic Areas; for instance it could describe particular permissions applied to specific kind vehicles

- [Road](https://github.com/smart-data-models/dataModel.Transportation/blob/master/Road/README.md). This entity contains a harmonised geographic and contextual description of a road.

- [RoadAccident](https://github.com/smart-data-models/dataModel.Transportation/blob/master/RoadAccident/README.md). A road accident description with causes and aftermath. First version developed in Synchronicity project

- [RoadSegment](https://github.com/smart-data-models/dataModel.Transportation/blob/master/RoadSegment/README.md). This entity contains a harmonised geographic and contextual description of a road segment. A collection of road segments are used to describe a Road.

- [SpecialRestriction](https://github.com/smart-data-models/dataModel.Transportation/blob/master/SpecialRestriction/README.md). A Special Restriction represents a particular case that specialise restriction reported in a Restricted Traffic Areas; for instance it could describe particular restrictions applied to specific kind vehicles

- [TrafficFlowObserved](https://github.com/smart-data-models/dataModel.Transportation/blob/master/TrafficFlowObserved/README.md). An observation of traffic flow conditions at a certain place and time.

- [TrafficViolation](https://github.com/smart-data-models/dataModel.Transportation/blob/master/TrafficViolation/README.md). A Data Model for Traffic Violations registered and E-Challans generated in Cities.

- [TransportStation](https://github.com/smart-data-models/dataModel.Transportation/blob/master/TransportStation/README.md). The data model is a general description of urban stations (Metro, Bus, Tram, Heliport, ...) according to the GFTS standard https://developers.google.com/transit/gtfs/reference/#stopstxt, as well the detailed description of these (means of access, platform, assistance, ...).

- [Vehicle](https://github.com/smart-data-models/dataModel.Transportation/blob/master/Vehicle/README.md). This entity models a particular vehicle model, including all properties which are common to multiple vehicle instances belonging to such model.

- [VehicleFault](https://github.com/smart-data-models/dataModel.Transportation/blob/master/VehicleFault/README.md). This entity contains a harmonised description of a Vehicle Fault. This entity is primarily associated with the Automotive vertical segment but might also be relevant to Industry, Smart City, Agriculture and related IoT applications.

- [VehicleModel](https://github.com/smart-data-models/dataModel.Transportation/blob/master/VehicleModel/README.md). This entity models a particular vehicle model, including all properties which are common to multiple vehicle instances belonging to such model.

## Mock Server

You can simulate and test the Road API using a hosted mock server built directly from the OpenAPI spec. This is helpful for exploring the API behavior, validating request and response formats, or developing client-side integrations—without setting up a backend. The mock server uses schema and example data to generate dynamic, realistic responses.

<a href="https://beeceptor.com/openapi-mock-server/?utm_source=github&utm_campaign=smart-data-models&url=https://raw.githubusercontent.com/smart-data-models/dataModel.Transportation/083e3bf77d2fffca4bfadee6ba895f4efb8a5c9e/Road/swagger.yaml" target="_blank"><img src="https://cdn.beeceptor.com/assets/images/buttons/mock-openapi-with-beeceptor.png" alt="Mock These APIs Instantly" style="height: 60px;"></a>


### Contributors
[Link](https://github.com/smart-data-models/dataModel.Transportation/blob/master/CONTRIBUTORS.yaml) to the 20 current contributors of the data models of this Subject.


### Contribution
You can raise an [issue](https://github.com/smart-data-models/dataModel.Transportation/issues) or submit your [PR](https://github.com/smart-data-models/dataModel.Transportation/pulls) on existing data models


