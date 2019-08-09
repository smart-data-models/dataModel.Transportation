[![Status badge](https://img.shields.io/badge/status-draft-red.svg)](RELEASE_NOTES)
[![Build badge](https://img.shields.io/travis/smart-data-models/dataModel.Transportation.svg "Travis build status")](https://travis-ci.org/smart-data-models/dataModel.Transportation/)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
# Transportation Harmonized Data Models

These data models describe the main entities involved with smart applications
that deal with transportation issues. This set of entities is primarily
associated with the Automotive and Smart City vertical segments and related IoT
applications.

When feasible, references to existing schema.org entity types and attributes are
included.

These models have been devised to be as generic as possible, thus allowing to
deal with different scenarios:

-   Traffic flow monitoring
-   Private Vehicles.
-   Public Vehicles (Buses, Trains, etc.).
-   Municipal Vehicles (pick up lorries, cleaning units, ...)
-   Special Vehicles (ambulances, fire brigades, ...)

The main entities identified are:

-   [TrafficFlowObserved](./TrafficFlowObserved/doc/spec.md). It represents an
    observation about flow of traffic.
-   [CrowdFlowObserved](./CrowdFlowObserved/doc/spec.md). It represents an
    observation related to the movement of people at a certain place and time.
-   [BikeHireDockingStation](./Bike/BikeHireDockingStation/doc/spec.md). It
    represents an a bike hire docking station where subscribed users can hire
    and return a bike.
-   [EVChargingStation](./EVChargingStation/doc/spec.md). It represents a
    public charging station supplying energy to electrical vehicles.
-   [Road](./Road/doc/spec.md). It contains a harmonised geographic and
    contextual description of a Road.
-   [RoadSegment](./RoadSegment/doc/spec.md). It contains a harmonised
    geographic and contextual description of a road segment.
-   [Vehicle](./Vehicle/Vehicle/doc/spec.md). It represents a vehicle with all
    its individual characteristics.
-   [VehicleModel](./Vehicle/VehicleModel/doc/spec.md). It represents a model
    of vehicle, capturing its static properties such as dimensions, materials or
    features.
