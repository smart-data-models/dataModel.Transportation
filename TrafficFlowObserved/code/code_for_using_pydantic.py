from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import (
    AnyUrl,
    AwareDatetime,
    BaseModel,
    Field,
    RootModel,
    confloat,
    constr,
)


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


class LaneDirection(Enum):
    forward = 'forward'
    backward = 'backward'


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


class Type6(Enum):
    TrafficFlowObserved = 'TrafficFlowObserved'


class VehicleType(Enum):
    agriculturalVehicle = 'agriculturalVehicle'
    bicycle = 'bicycle'
    bus = 'bus'
    minibus = 'minibus'
    car = 'car'
    caravan = 'caravan'
    tram = 'tram'
    tanker = 'tanker'
    carWithCaravan = 'carWithCaravan'
    carWithTrailer = 'carWithTrailer'
    lorry = 'lorry'
    moped = 'moped'
    motorcycle = 'motorcycle'
    motorcycleWithSideCar = 'motorcycleWithSideCar'
    motorscooter = 'motorscooter'
    trailer = 'trailer'
    van = 'van'
    constructionOrMaintenanceVehicle = 'constructionOrMaintenanceVehicle'
    trolley = 'trolley'
    binTrolley = 'binTrolley'
    sweepingMachine = 'sweepingMachine'
    cleaningTrolley = 'cleaningTrolley'


class TrafficFlowObserved(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    averageGapDistance: Optional[confloat(ge=0.0)] = Field(
        None, description='Average gap distance between consecutive vehicles'
    )
    averageHeadwayTime: Optional[confloat(ge=0.0)] = Field(
        None,
        description='Average headway time. Headway time is the time ellapsed between two consecutive vehicles',
    )
    averageVehicleLength: Optional[confloat(ge=0.0)] = Field(
        None,
        description='Average length of the vehicles transiting during\\n    the observation period',
    )
    averageVehicleSpeed: Optional[confloat(ge=0.0)] = Field(
        None,
        description='Average speed of the vehicles transiting during the observation period',
    )
    congested: Optional[bool] = Field(
        None,
        description=' Flags whether there was a traffic congestion during the observation period in the referred lane. The absence of this attribute means no traffic congestion',
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
    dateObserved: Optional[str] = Field(
        None,
        description='The date and time of this observation in ISO8601 UTC format. It can be represented by an specific time instant or by an ISO8601 interval. As a workaround for the lack of support of Orion Context Broker for datetime intervals, it can be used two separate attributes: `dateObservedFrom`, `dateObservedTo`. [DateTime](https://schema.org/DateTime) or an ISO8601 interval represented as [Text](https://schema.org/Text)',
    )
    dateObservedFrom: Optional[AwareDatetime] = Field(
        None, description='Observation period start date and time. See `dateObserved`'
    )
    dateObservedTo: Optional[AwareDatetime] = Field(
        None, description='Observation period end date and time. See `dateObserved`'
    )
    description: Optional[str] = Field(None, description='A description of this item')
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
    intensity: Optional[confloat(ge=0.0)] = Field(
        None,
        description='Total number of vehicles detected during this observation period',
    )
    laneDirection: Optional[LaneDirection] = Field(
        None,
        description="Usual direction of travel in the lane referred by this observation. This attribute is useful when the observation is not referencing any road segment, allowing to know the direction of travel of the traffic flow observed. Enum:forward, backward'. See RoadSegment for a description of the semantics of these values",
    )
    laneId: Optional[confloat(ge=1.0)] = Field(
        None,
        description='Lane identifier. Lane identification is done using the conventions defined by RoadSegment entity which are based on [OpenStreetMap](http://wiki.openstreetmap.org/wiki/Forward_%26_backward,_left_%26_right)',
    )
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    name: Optional[str] = Field(None, description='The name of this item')
    occupancy: Optional[confloat(ge=0.0, le=1.0)] = Field(
        None,
        description='Fraction of the observation time where a vehicle has been occupying the observed lane',
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
    refRoadSegment: Optional[AnyUrl] = Field(
        None,
        description='Concerned road segment on which the observation has been made. Reference to an entity of type RoadSegment',
    )
    reversedLane: Optional[bool] = Field(
        None,
        description='Flags whether traffic in the lane was reversed during the observation period. The absence of this attribute means no lane reversion',
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    type: Optional[Type6] = Field(
        None, description='NGSI Entity type. It has to be TrafficFlowObserved'
    )
    vehicleSubType: Optional[str] = Field(
        None,
        description='It allows to specify a sub type of `vehicleType`, eg if the `vehicleType` is set to `Lorry` the `vehicleSubType` may be `OGV1` or `OGV2` to convey more information about the exact type of vehicle',
    )
    vehicleType: Optional[VehicleType] = Field(
        None,
        description="Type of vehicle from the point of view of its structural characteristics. Enum:'agriculturalVehicle, bicycle, bus, minibus, car, caravan, tram, tanker, carWithCaravan, carWithTrailer, lorry, moped, motorcycle, motorcycleWithSideCar, motorscooter, trailer, van, constructionOrMaintenanceVehicle, trolley, binTrolley, sweepingMachine, cleaningTrolley'",
    )
