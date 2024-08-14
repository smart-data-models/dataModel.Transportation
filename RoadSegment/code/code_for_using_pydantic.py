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


class AllowedVehicleTypeEnum(Enum):
    agriculturalVehicle = 'agriculturalVehicle'
    bicycle = 'bicycle'
    bus = 'bus'
    car = 'car'
    caravan = 'caravan'
    carWithCaravan = 'carWithCaravan'
    carWithTrailer = 'carWithTrailer'
    constructionOrMaintenanceVehicle = 'constructionOrMaintenanceVehicle'
    lorry = 'lorry'
    moped = 'moped'
    motorcycle = 'motorcycle'
    motorcycleWithSideCar = 'motorcycleWithSideCar'
    motorscooter = 'motorscooter'
    tanker = 'tanker'
    trailer = 'trailer'
    van = 'van'
    anyVehicle = 'anyVehicle'


class CategoryEnum(Enum):
    oneway = 'oneway'
    toll = 'toll'
    link = 'link'


class CyclePathPlacement(Enum):
    BOTH = 'BOTH'
    LEFT = 'LEFT'
    NOT_AVAILABLE = 'NOT_AVAILABLE'
    RIGHT = 'RIGHT'


class Type(Enum):
    Point = 'Point'


class EndPoint(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[float] = Field(..., min_length=2)
    type: Type


class Coordinate(RootModel[List[float]]):
    root: List[float]


class Type1(Enum):
    LineString = 'LineString'


class EndPoint1(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[Coordinate] = Field(..., min_length=2)
    type: Type1


class Type2(Enum):
    Polygon = 'Polygon'


class EndPoint2(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type2


class Type3(Enum):
    MultiPoint = 'MultiPoint'


class EndPoint3(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[float]]
    type: Type3


class Type4(Enum):
    MultiLineString = 'MultiLineString'


class EndPoint4(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type4


class Type5(Enum):
    MultiPolygon = 'MultiPolygon'


class EndPoint5(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[List[Coordinate]]]
    type: Type5


class LaneDirection(Enum):
    BACKWARD = 'BACKWARD'
    FORWARD = 'FORWARD'
    INBOUND = 'INBOUND'
    LEFT = 'LEFT'
    OUTBOUND = 'OUTBOUND'
    RIGHT = 'RIGHT'


class LaneInfo(BaseModel):
    laneDirection: Optional[LaneDirection] = Field(
        None,
        description="Describes the direction in which vehicles are plying on the lane corresponding to this observation. Enum:'FORWARD, BACKWARD, INBOUND, OUTBOUND, RIGHT, LEFT'",
    )
    laneId: Optional[float] = Field(
        None,
        description='Unique identification number of the lane corresponding to this observation',
    )


class LaneUsageEnum(Enum):
    forward = 'forward'
    backward = 'backward'


class Type6(Enum):
    Point = 'Point'


class Location(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[float] = Field(..., min_length=2)
    type: Type6


class Type7(Enum):
    LineString = 'LineString'


class Location1(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[Coordinate] = Field(..., min_length=2)
    type: Type7


class Type8(Enum):
    Polygon = 'Polygon'


class Location2(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type8


class Type9(Enum):
    MultiPoint = 'MultiPoint'


class Location3(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[float]]
    type: Type9


class Type10(Enum):
    MultiLineString = 'MultiLineString'


class Location4(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type10


class Type11(Enum):
    MultiPolygon = 'MultiPolygon'


class Location5(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[List[Coordinate]]]
    type: Type11


class MunicipalityInfo(BaseModel):
    cityId: Optional[str] = Field(
        None, description='City ID corresponding to this observation'
    )
    cityName: Optional[str] = Field(
        None, description='City name corresponding to this observation'
    )
    district: Optional[str] = Field(
        None, description='District name corresponding to this observation'
    )
    stateName: Optional[str] = Field(
        None, description='Name of the state corresponding to this observation'
    )
    ulbName: Optional[str] = Field(
        None,
        description='Name of the Urban Local Body corresponding to this observation',
    )
    wardId: Optional[str] = Field(
        None, description='Ward ID corresponding to this observation'
    )
    wardName: Optional[str] = Field(
        None, description='Ward name corresponding to this observation'
    )
    wardNum: Optional[float] = Field(
        None, description='Ward number corresponding to this observation'
    )
    zoneId: Optional[str] = Field(
        None, description='Zone ID corresponding to this observation'
    )
    zoneName: Optional[str] = Field(
        None, description='Zone name corresponding to this observation'
    )


class RoadClass(Enum):
    MAJOR_DISTRICT_ROAD = 'MAJOR_DISTRICT_ROAD'
    MAJOR_CITY_ROAD = 'MAJOR_CITY_ROAD'
    MINOR_CITY_ROAD = 'MINOR_CITY_ROAD'
    NATIONAL_HIGHWAY = 'NATIONAL_HIGHWAY'
    OTHER_DISTRICT_ROAD = 'OTHER_DISTRICT_ROAD'
    OTHER_PUBLIC_ROAD = 'OTHER_PUBLIC_ROAD'
    PORT_ROAD = 'PORT_ROAD'
    PRIVATE_ROAD = 'PRIVATE_ROAD'
    SERVICE_ROAD = 'SERVICE_ROAD'
    STATE_HIGHWAY = 'STATE_HIGHWAY'


class RoadWork(Enum):
    COLLAPSE = 'COLLAPSE'
    DERAILMENT = 'DERAILMENT'
    FIRE = 'FIRE'
    FLOOD = 'FLOOD'
    GASLEAK = 'GASLEAK'
    LANDSLIDE = 'LANDSLIDE'
    OTHER = 'OTHER'
    POWERCUT = 'POWERCUT'
    ROCKFALL = 'ROCKFALL'
    SAGGING = 'SAGGING'
    WATERLEAK = 'WATERLEAK'


class Type12(Enum):
    Point = 'Point'


class StartPoint(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[float] = Field(..., min_length=2)
    type: Type12


class Type13(Enum):
    LineString = 'LineString'


class StartPoint1(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[Coordinate] = Field(..., min_length=2)
    type: Type13


class Type14(Enum):
    Polygon = 'Polygon'


class StartPoint2(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type14


class Type15(Enum):
    MultiPoint = 'MultiPoint'


class StartPoint3(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[float]]
    type: Type15


class Type16(Enum):
    MultiLineString = 'MultiLineString'


class StartPoint4(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type16


class Type17(Enum):
    MultiPolygon = 'MultiPolygon'


class StartPoint5(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[List[Coordinate]]]
    type: Type17


class StatusEnum(Enum):
    open = 'open'
    closed = 'closed'
    limited = 'limited'


class Type18(Enum):
    RoadSegment = 'RoadSegment'


class RoadSegment(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    agency_name: Optional[str] = Field(
        None,
        description="The agency_name field contains the full name of the agency or organisation responsible for maintenance of the entity under consideration. SameAs: 'agency_name' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)",
    )
    allowedVehicleType: Optional[List[AllowedVehicleTypeEnum]] = Field(
        None,
        description="Vehicle type(s) allowed to transit through this road segment. Enum:'agriculturalVehicle, bicycle, bus, car, caravan, carWithCaravan, carWithTrailer, constructionOrMaintenanceVehicle, lorry, moped, motorcycle, motorcycleWithSideCar, motorscooter, tanker, trailer, van, anyVehicle'. Allowed values: The following values defined by _VehicleTypeEnum_, [DATEX 2 version 2.3](http://d2docs.ndwcloud.nu/):",
    )
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    annotations: Optional[List[str]] = Field(
        None, description='Annotations about the item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    bridgeCount: Optional[float] = Field(
        None,
        description='Number of bridges in the road segment corresponding to this observation. Takes 0 (zero) as the value when the road segment has no bridges',
    )
    carriagewayLength: Optional[float] = Field(
        None,
        description='Total length of the carriage way of the road segment corresponding to this observation',
    )
    carriagewayWidth: Optional[float] = Field(
        None,
        description='Total width of the carriage way of the road segment corresponding to this observation',
    )
    category: Optional[List[CategoryEnum]] = Field(
        None,
        description="Allows to convey extra characteristics of a road segment. Enum:'oneway, toll, link'.  `oneway`: Flags whether the road segment can only be used in one direction. If not present it means road segment can be used in both directions (forwards and backwards). See also [http://wiki.openstreetmap.org/wiki/Key:oneway](http://wiki.openstreetmap.org/wiki/Key:oneway). `toll` : Flags whether the road segment is under toll fees. `link` : Flags whether this road segment is an auxiliary link segment for exiting or entering a road. See [https://wiki.openstreetmap.org/wiki/Tag:highway%3Dmotorway_link](https://wiki.openstreetmap.org/wiki/Tag:highway%3Dmotorway_link). Any other value meaningful to an application",
    )
    color: Optional[str] = Field(None, description='The color of the product')
    culvertCount: Optional[float] = Field(
        None,
        description='Number of culverts prevalent in the trace of the road corresponding to this observation',
    )
    cyclePathLeftHeight: Optional[float] = Field(
        None,
        description='Height of the cycle track on the left edge of the road corresponding to this observation',
    )
    cyclePathLeftWidth: Optional[float] = Field(
        None,
        description='Width of the cycle track on the left edge of the road corresponding to this observation',
    )
    cyclePathMaterial: Optional[str] = Field(
        None,
        description='Construction material used for laying the cycle path on the sides of the road corresponding to this observation',
    )
    cyclePathPlacement: Optional[CyclePathPlacement] = Field(
        None,
        description="Describes the placement of cycle track along the road segment corresponding to this observation. Enum:' ['RIGHT, LEFT, BOTH, NOT_AVAILABLE'",
    )
    cyclePathRightHeight: Optional[float] = Field(
        None,
        description='Height of the cycle track on the right edge of the road corresponding to this observation',
    )
    cyclePathRightWidth: Optional[float] = Field(
        None,
        description='Width of the cycle track on the right edge of the road corresponding to this observation',
    )
    dataDescriptor: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='URI pointing to the data-descriptor entity')
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
    endKilometer: Optional[confloat(ge=0.0)] = Field(
        None,
        description="The kilometer number (measured from the road's start point) where this road segment ends. ",
    )
    endPoint: Optional[
        Union[EndPoint, EndPoint1, EndPoint2, EndPoint3, EndPoint4, EndPoint5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
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
    image: Optional[AnyUrl] = Field(None, description='An image of the item')
    laneInfo: Optional[LaneInfo] = Field(
        None,
        description='Describes the aspects of lanes of the road corresponding to this observation',
    )
    laneUsage: Optional[List[LaneUsageEnum]] = Field(
        None,
        description='This attribute can be used to convey specific parameters describing each lane. It must contain a string per road segment lane. The element 0 of the array must contain the information of lane 1, and so on. Format of the referred string must be: <lane_direction>, <lane_minimumAllowedSpeed>, <lane_maximumAllowedSpeed>, <lane_maximumAllowedHeight>, <lane_maximumAllowedWeight>. <lane_direction> is a text string with the following allowed values: `forward`. The lane is currently used in the `forwards` direction. `backward`. The lane is currently used in the `backwards` direction. The only mandatory parameter is `lane_direction`. If not specified, the rest of parameters can be assumed to be equal to those specified at entity level',
    )
    length: Optional[confloat(ge=0.0)] = Field(
        None, description='Total length of this road segment in kilometers'
    )
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    maximumAllowedHeight: Optional[confloat(ge=0.0)] = Field(
        None,
        description='Maximum allowed height for vehicles transiting this road segment',
    )
    maximumAllowedSpeed: Optional[confloat(ge=0.0)] = Field(
        None,
        description='Maximum allowed speed plying the road segment. More restrictive limits might be applied to specific vehicle types (trucks, caravans, etc.)',
    )
    maximumAllowedWeight: Optional[confloat(ge=0.0)] = Field(
        None,
        description='Maximum allowed weight for vehicles transiting this road segment',
    )
    maximumAllowedWidth: Optional[float] = Field(
        None,
        description='Maximum allowed width for vehicles using the entity corresponding to this observation',
    )
    medianHeight: Optional[float] = Field(
        None,
        description='Height of the median or central reservation in the road corresponding to this observation',
    )
    medianLength: Optional[float] = Field(
        None,
        description='Length of the median or central reservation in the road corresponding to this observation',
    )
    medianWidth: Optional[float] = Field(
        None,
        description='Width of the median or central reservation in the road corresponding to this observation',
    )
    minimumAllowedSpeed: Optional[confloat(ge=0.0)] = Field(
        None, description='Minimum allowed speed while transiting this road segment'
    )
    municipalityInfo: Optional[MunicipalityInfo] = Field(
        None, description='Municipality information corresponding to this observation'
    )
    name: Optional[str] = Field(None, description='The name of this item')
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
    pedestrianPathLeftHeight: Optional[float] = Field(
        None,
        description='Height of the walkway placed on the left edge of the road corresponding to this observation',
    )
    pedestrianPathLeftWidth: Optional[float] = Field(
        None,
        description='Width of the walkway placed on the left edge of the road corresponding to this observation',
    )
    pedestrianPathMaterial: Optional[str] = Field(
        None,
        description='Construction material used for laying the walkway / footpath on the sides of the road corresponding to this observation',
    )
    pedestrianPathPlacement: Optional[str] = Field(
        None,
        description="Describes the presence and placement of pedestrian along the road segment corresponding to this observation. Enum:'RIGHT, LEFT, BOTH, NOT_AVAILABLE'",
    )
    pedestrianPathRightHeight: Optional[float] = Field(
        None,
        description='Height of the walkway placed on the right edge of the road corresponding to this observation',
    )
    pedestrianPathRightWidth: Optional[float] = Field(
        None,
        description='Width of the walkway placed on the right edge of the road corresponding to this observation',
    )
    refRoad: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Road to which this road segment belongs to')
    rightOfWayWidth: Optional[float] = Field(
        None,
        description="Right of Way (RoW) is the total land area available for the roadway. Its width accommodates for carriages way + other necessities + future extension, along the road's alignment",
    )
    roadClass: Optional[RoadClass] = Field(
        None,
        description='The type of road corresponding to this observation. Enum: [OTHER_PUBLIC_ROAD, PRIVATE_ROAD, MINOR_CITY_ROAD, MAJOR_DISTRICT_ROAD, MAJOR_CITY_ROAD, NATIONAL_HIGHWAY, SERVICE_ROAD, STATE_HIGHWAY, OTHER_DISTRICT_ROAD, PORT_ROAD]',
    )
    roadDirection: Optional[str] = Field(
        None,
        description="Represents the direction the road is heading to. Enum:' ['N, S, E, W'. The values N,S,E,W represent North,South,East,West respectively",
    )
    roadId: Optional[str] = Field(
        None,
        description='Unique internal representation of the road corresponding to this observation',
    )
    roadMaterial: Optional[str] = Field(
        None,
        description='The construction material used for laying the carriageway corresponding to this observation. For eg. concrete, earthen, tar etc',
    )
    roadName: Optional[str] = Field(
        None, description='The name of the road corresponding to this observation'
    )
    roadWork: Optional[RoadWork] = Field(
        None,
        description="Reasons for the road work in case of urgent intervention. A combination of these values. Enum:'COLLAPSE, DERAILMENT, FIRE, FLOOD, GASLEAK, LANDSLIDE, OTHER, POWERCUT, ROCKFALL, SAGGING, WATERLEAK'",
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    startKilometer: Optional[confloat(ge=0.0)] = Field(
        None,
        description="The kilometer number (measured from the road's start point) where this road segment starts. ",
    )
    startPoint: Optional[
        Union[
            StartPoint, StartPoint1, StartPoint2, StartPoint3, StartPoint4, StartPoint5
        ]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    status: Optional[List[StatusEnum]] = Field(
        None,
        description='Specific driving conditions on the roadsegment. Use statusDescription for additional information. Enum: ‘open, closed, limited’.  `open`: the roadsegment can be used in full intended capacity, `closed`: no traffic is possible, e.g. due to roadworks, an open bridge or lock, or any other event preventing traffic. `limited`: traffic is possible, but not in the full capacity',
    )
    statusDescription: Optional[str] = Field(
        None, description='Additional information to the status attribute'
    )
    totalCyclePathWidth: Optional[float] = Field(
        None,
        description='Total width of the cycle track present in the road corresponding to this observation',
    )
    totalLaneNumber: Optional[confloat(ge=1.0)] = Field(
        None, description='Total number of lanes offered by this road segment'
    )
    totalPedestrianPathLength: Optional[float] = Field(
        None,
        description='Total length of the walkway present in the road corresponding to this observation',
    )
    totalPedestrianPathWidth: Optional[float] = Field(
        None,
        description='Total width of the walkway present in the road corresponding to this observation',
    )
    type: Optional[Type18] = Field(
        None, description='NGSI Entity type. It has to be RoadSegment'
    )
    width: Optional[confloat(ge=0.0)] = Field(None, description="Road's segment width.")
