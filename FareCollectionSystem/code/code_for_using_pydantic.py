from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field, RootModel, constr


class Address(BaseModel):
    addressCountry: Optional[str] = Field(
        None, description='The country. For example, Spain'
    )
    addressLocality: Optional[str] = Field(
        None,
        description='The locality in which the street address is, and which is in the region',
    )
    addressRegion: Optional[str] = Field(
        None,
        description='The region in which the locality is, and which is in the country',
    )
    district: Optional[str] = Field(
        None,
        description='A district is a type of administrative division that, in some countries, is managed by the local government',
    )
    postOfficeBoxNumber: Optional[str] = Field(
        None,
        description='The post office box number for PO box addresses. For example, 03578',
    )
    postalCode: Optional[str] = Field(
        None, description='The postal code. For example, 24004'
    )
    streetAddress: Optional[str] = Field(None, description='The street address')
    streetNr: Optional[str] = Field(
        None, description='Number identifying a specific property on a public street'
    )


class EquipmentTypeCode(Enum):
    field_1B = '1B'
    field_42 = 42
    field_2 = 2
    field_8 = 8
    field_41 = 41


class Type(Enum):
    Point = 'Point'


class Location(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[float] = Field(..., min_length=2)
    type: Type


class Coordinate(RootModel[List[float]]):
    root: List[float]


class Type1(Enum):
    LineString = 'LineString'


class Location1(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[Coordinate] = Field(..., min_length=2)
    type: Type1


class Type2(Enum):
    Polygon = 'Polygon'


class Location2(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type2


class Type3(Enum):
    MultiPoint = 'MultiPoint'


class Location3(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[float]]
    type: Type3


class Type4(Enum):
    MultiLineString = 'MultiLineString'


class Location4(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type4


class Type5(Enum):
    MultiPolygon = 'MultiPolygon'


class Location5(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[List[Coordinate]]]
    type: Type5


class OccupancyLevel(Enum):
    Red = 'Red'
    Yellow = 'Yellow'
    Green = 'Green'


class Type6(Enum):
    FareCollectionSystem = 'FareCollectionSystem'


class FareCollectionSystem(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    cardId: Optional[str] = Field(
        None,
        description='Unique ticket Id of the transaction or Id of the smart card used in the transaction',
    )
    currentTripCount: Optional[float] = Field(
        None,
        description='The current count of trips made by the vehicle corresponding to this observation on the given day of operation',
    )
    dataProvider: Optional[str] = Field(
        None,
        description='A sequence of characters identifying the provider of the harmonised data entity',
    )
    dateCreated: Optional[AwareDatetime] = Field(
        None,
        description='Entity creation timestamp. This will usually be allocated by the storage platform',
    )
    dateModified: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp of the last modification of the entity. This will usually be allocated by the storage platform',
    )
    description: Optional[str] = Field(None, description='A description of this item')
    destinationStopCategory: Optional[str] = Field(
        None,
        description='Type of the destination bus stop corresponding to this observation',
    )
    destinationStopId: Optional[str] = Field(
        None,
        description='Unique Id of the bus stop at which the passenger deboards from the bus corresponding to this observation',
    )
    destinationStopName: Optional[str] = Field(
        None,
        description='The name of the destination bus stop corresponding to this observation',
    )
    direction_id: Optional[float] = Field(
        None,
        description="Indicates the direction of travel of the vehicle corresponding to this observation, can be referenced from the GTFS static feed trips.txt. SameAs: 'direction_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)",
    )
    entryAreaCode: Optional[str] = Field(
        None,
        description='Area code of the passenger boarding stop (used by the fare collection agency). For example, whether the stop is city-bus-service stop or brts stop or other service type stop etc',
    )
    equipmentCompanyCode: Optional[str] = Field(
        None,
        description='Company/Agency code for the transaction equipment (used by fare collection agency). For example, 103 - CBS (city bus service),102 - BRTS etc',
    )
    equipmentId: Optional[str] = Field(
        None, description='Unique Id of the equipment corresponding to this observation'
    )
    equipmentSequenceNumber: Optional[float] = Field(
        None, description='Sequence number for the given equipment'
    )
    equipmentStopId: Optional[str] = Field(
        None,
        description='Stop Id (BRTS) at which the equipment corresponding to this transaction is installed',
    )
    equipmentType: Optional[str] = Field(
        None,
        description='Type of equipment or the name of the equipment corresponding to this observation',
    )
    equipmentTypeCode: Optional[EquipmentTypeCode] = Field(
        None,
        description='Unique code indicating the type of equipment used in the transaction (used by fare collection agency).ENUM [1B, 42, 02, 08, 41] 1B - POS, 42 - HTT, 02- Mobile, 08- Fare Gate, 41- Pole Validator',
    )
    exitAreaCode: Optional[str] = Field(
        None,
        description='Area code of the passenger alighting stop (used by the fare collection agency). For example, whether the stop is city-bus-service stop or BRTS stop or other service type stop etc',
    )
    fareForAdult: Optional[float] = Field(
        None,
        description='The fare for an adult in the journey corresponding to this observation',
    )
    fareForChild: Optional[float] = Field(
        None,
        description='The fare for a child in the journey corresponding to this observation',
    )
    id: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Unique identifier of the entity')
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    name: Optional[str] = Field(None, description='The name of this item')
    observationDateTime: Optional[AwareDatetime] = Field(
        None, description='Last reported time of observation'
    )
    occupancyLevel: Optional[OccupancyLevel] = Field(
        None,
        description="Occupancy level in the public transit bus corresponding to this observation. 'Red' indicates the congestion level in the bus is HIGH, 'Yellow' indicates the congestion level in the bus is MODERATE and 'Green' indicates the congestion level in the bus is LOW",
    )
    originDestinationCode: Optional[str] = Field(
        None,
        description='The code for the origin and destination stops corresponding to this observation',
    )
    originStopCategory: Optional[str] = Field(
        None,
        description='Type of the origin bus stop corresponding to this observation',
    )
    originStopId: Optional[str] = Field(
        None,
        description='Unique Id of the bus stop at which the passenger boards into the bus corresponding to this observation',
    )
    originStopName: Optional[str] = Field(
        None,
        description='The name of the origin bus stop corresponding to this observation',
    )
    owner: Optional[
        List[
            Union[
                constr(
                    pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!,:\\\\]+$',
                    min_length=1,
                    max_length=256,
                ),
                AnyUrl,
            ]
        ]
    ] = Field(
        None,
        description='A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)',
    )
    passengerCount: Optional[float] = Field(
        None,
        description='Number of passengers travelling in the public transit bus corresponding to this observation. This count is computed based on the realtime ticketing transactions in the public transit bus',
    )
    route_id: Optional[str] = Field(
        None,
        description="Route Id assigned to the route on which the bus/vehicle corresponding to the bus in this observation is currently plying on. SameAs: 'route_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)",
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    shiftOfOperation: Optional[str] = Field(
        None,
        description="Shift of operation of the public transit vehicle operated by the fare collection agency/ public transit agency or the employee corresponding to this observation. Indicated as '1' when the vehicle operates in the first shift, '2' when the vehicle operates in the second shift and '3' when the vehicle operates in the third shift",
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    stage: Optional[float] = Field(
        None,
        description='Total number of stages from the origin bus stop to the destination bus stop',
    )
    ticketTypeCode: Optional[str] = Field(
        None, description='Unique ticket type code of the corresponding trip'
    )
    transactionDateTime: Optional[AwareDatetime] = Field(
        None,
        description='Date-time of the transaction corresponding to this observation',
    )
    transactionType: Optional[str] = Field(
        None,
        description='Type of the transaction corresponding to this observation. For Eg - Issue, ReIssue, Entry, Exit etc',
    )
    transactionTypeDescription: Optional[str] = Field(
        None,
        description='Description of the transaction type. Explanation of various transactionTypeId codes used in the data',
    )
    transactionVehicleNum: Optional[float] = Field(
        None,
        description='Code used by fare collection agency for the vehicle number corresponding to the transaction',
    )
    travelDistance: Optional[float] = Field(
        None,
        description='The distance between the origin bus stop and the destination bus stop corresponding to this observation',
    )
    trip_id: Optional[str] = Field(
        None,
        description="Trip Id/Trip name alloted to the bus corresponding to this observation, in consideration to the time of the day and the direction of the trip on the given routeId. SameAs: 'trip_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)",
    )
    type: Optional[Type6] = Field(
        None, description='NGSI entity type. It has to be FareCollectionSystem'
    )
    vehicle_label: Optional[str] = Field(
        None,
        description="User visible label, i.e., something that must be shown to the passenger to help identify the correct vehicle. SameAs: 'label' field from GTFS Realtime message-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)",
    )
