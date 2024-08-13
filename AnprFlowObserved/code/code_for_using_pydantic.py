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


class Brand(BaseModel):
    confidence: Optional[confloat(ge=0.0, le=1.0)] = Field(
        None, description='Confidence level of the detection'
    )
    name: Optional[str] = Field(None, description='Brand name identified')


class Color(BaseModel):
    confidence: Optional[confloat(ge=0.0, le=1.0)] = Field(
        None, description='Confidence level of the detection'
    )
    name: Optional[str] = Field(None, description='Color name')


class Country(BaseModel):
    code: Optional[str] = Field(
        None, description='Country code according to ISO 3166-1 alpha-2'
    )
    confidence: Optional[confloat(ge=0.0, le=1.0)] = Field(
        None, description='Confidence level of the detection'
    )


class Direction(Enum):
    away = 'away'
    towards = 'towards'


class Type6(Enum):
    Point = 'Point'


class Coordinates(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[float] = Field(..., min_length=2)
    type: Type6


class Type7(Enum):
    LineString = 'LineString'


class Coordinates1(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[Coordinate] = Field(..., min_length=2)
    type: Type7


class Type8(Enum):
    Polygon = 'Polygon'


class Coordinates2(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type8


class Type9(Enum):
    MultiPoint = 'MultiPoint'


class Coordinates3(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[float]]
    type: Type9


class Type10(Enum):
    MultiLineString = 'MultiLineString'


class Coordinates4(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type10


class Type11(Enum):
    MultiPolygon = 'MultiPolygon'


class Coordinates5(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[List[Coordinate]]]
    type: Type11


class LicensePlate(BaseModel):
    confidence: Optional[confloat(ge=0.0, le=1.0)] = Field(
        None, description='Confidence level of the detection'
    )
    coordinates: Optional[
        Union[
            Coordinates,
            Coordinates1,
            Coordinates2,
            Coordinates3,
            Coordinates4,
            Coordinates5,
        ]
    ] = Field(
        None,
        description='Sequence of position points describing this location, expressed in coordinate system',
    )
    identifier: Optional[str] = Field(None, description='License plate identifier')


class Model(BaseModel):
    confidence: Optional[confloat(ge=0.0, le=1.0)] = Field(
        None, description='Confidence level of the detection'
    )
    name: Optional[str] = Field(None, description='Model name')


class ObservedVehicle(BaseModel):
    brand: Optional[Brand] = Field(
        None, description='Detected brand of the observed vehicle'
    )
    color: Optional[Color] = Field(
        None, description='Detected color of the observed vehicle'
    )
    country: Optional[Country] = Field(
        None, description='Detected country of the observed vehicle'
    )
    direction: Optional[Direction] = Field(
        None, description='Detected direction of the observed vehicle'
    )
    licensePlate: Optional[LicensePlate] = Field(
        None, description='Detected license plate of the observed vehicle'
    )
    model: Optional[Model] = Field(
        None, description='Detected brand model of the observed vehicle'
    )
    speed: Optional[confloat(ge=0.0)] = Field(
        None, description='Detected speed of the observed vehicle'
    )


class ImageType(Enum):
    plate = 'plate'
    overview = 'overview'
    anpr = 'anpr'


class RefImage(BaseModel):
    contentType: Optional[str] = Field(
        None, description='Content type according to IANA Media Types'
    )
    imageType: Optional[ImageType] = Field(None, description='Type of image')
    url: Optional[AnyUrl] = Field(None, description='URL referencing to the image')


class Type12(Enum):
    AnprFlowObserved = 'AnprFlowObserved'


class AnprFlowObserved(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
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
    dateObserved: Optional[AwareDatetime] = Field(
        None, description='Date of the observed entity defined by the user'
    )
    dateReceived: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp when the observation has been received by the platform',
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
    laneId: Optional[str] = Field(
        None,
        description='Lane identifier. Lane identification provided by the observer',
    )
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    name: Optional[str] = Field(None, description='The name of this item')
    observedBy: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(
        None, description='The entity or device which has reported this observation'
    )
    observedVehicle: Optional[ObservedVehicle] = Field(
        None, description='Information about the observed vehicle'
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
    refImages: Optional[List[RefImage]] = Field(
        None, description='Array of multiple objects that refer to images'
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    type: Optional[Type12] = Field(
        None, description='NGSI Entity type. It has to be AnprFlowObserved'
    )
    vehiclePlateNotRead: Optional[bool] = Field(
        None, description='Indicates if a license could not be read'
    )
    zonesServed: Optional[List[str]] = Field(
        None,
        description='Array of zones that are able to receive or read the observations',
    )
