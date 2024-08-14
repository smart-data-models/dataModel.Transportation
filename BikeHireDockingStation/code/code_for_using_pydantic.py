from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import (
    AnyUrl,
    AwareDatetime,
    BaseModel,
    EmailStr,
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


class ContactPoint(BaseModel):
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided. Supersedes serviceArea',
    )
    availabilityRestriction: Optional[
        Union[
            List[
                constr(
                    pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                    min_length=1,
                    max_length=256,
                )
            ],
            List[AnyUrl],
        ]
    ] = Field(
        None,
        description='This property links a contact point to information about when the contact point is not available. The details are provided using the Opening Hours Specification class',
    )
    availableLanguage: Optional[Union[str, List[str]]] = Field(
        None,
        description='A language someone may use with or at the item, service or place. Please use one of the language codes from the IETF BCP 47 standard. It is implemented the Text option but it could be also Language',
    )
    contactOption: Optional[Union[str, List[str]]] = Field(
        None,
        description='An option available on this contact point (e.g. a toll-free number or support for hearing-impaired callers)',
    )
    contactType: Optional[str] = Field(None, description='Contact type of this item')
    email: Optional[EmailStr] = Field(None, description='Email address of owner')
    faxNumber: Optional[str] = Field(None, description='The fax number')
    name: Optional[str] = Field(None, description='The name of this item')
    productSupported: Optional[str] = Field(
        None,
        description="The product or service this support contact point is related to (such as product support for a particular product line). This can be a specific product or product line (e.g. 'iPhone') or a general category of products or services (e.g. 'smartphones')",
    )
    telephone: Optional[str] = Field(None, description='Telephone of this contact')
    url: Optional[AnyUrl] = Field(
        None,
        description='URL which provides a description or further information about this item',
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


class Status(Enum):
    almostEmpty = 'almostEmpty'
    almostFull = 'almostFull'
    empty = 'empty'
    full = 'full'
    outOfService = 'outOfService'
    withIncidence = 'withIncidence'
    working = 'working'


class Type6(Enum):
    BikeHireDockingStation = 'BikeHireDockingStation'


class BikeHireDockingStation(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    agency_fare_url: Optional[str] = Field(
        None,
        description="URL of a web page that contains the details of the fares and also could allow to purchase tickets for that agency online. SameAs: 'agency_fare_url' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt) ",
    )
    agency_name: Optional[str] = Field(
        None,
        description="The agency_name field contains the full name of the transit agency. SameAs: 'agency_name' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)",
    )
    agency_url: Optional[AnyUrl] = Field(
        None,
        description="The agency_url field contains the URL of the transit agency. SameAs: 'agency_url' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)",
    )
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    availableBikeNumber: Optional[confloat(ge=0.0)] = Field(
        None,
        description='The number of bikes available in the bike hire docking station to be hired by users',
    )
    contactPoint: Optional[ContactPoint] = Field(
        None, description='The details to contact with the item'
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
    freeSlotNumber: Optional[confloat(ge=0.0)] = Field(
        None,
        description='The number of slots available for returning and parking bikes. It must lower or equal than `totalSlotNumber`',
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
    mediaURL: Optional[AnyUrl] = Field(
        None,
        description='URL providing further information of any image(s) or media of the complaint or place',
    )
    name: Optional[str] = Field(None, description='The name of this item')
    observationDateTime: Optional[AwareDatetime] = Field(
        None, description='Last reported time of observation'
    )
    openingHours: Optional[str] = Field(
        None, description='Opening hours of the docking station'
    )
    outOfServiceSlotNumber: Optional[confloat(ge=0.0)] = Field(
        None,
        description='The number of slots that are out of order and cannot be used to hire or park a bike. It must lower or equal than `totalSlotNumber`',
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
    provider: Optional[str] = Field(None, description='Bike hire service provider')
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    stationCode: Optional[str] = Field(
        None,
        description='The station number or station code of the bike hire docking station corresponding to the observation',
    )
    stationName: Optional[str] = Field(
        None,
        description='The name of the bike hire docking station corresponding to this observation',
    )
    status: Optional[Status] = Field(
        None,
        description="Status of the bike hire docking station. Enum:'working, outOfService, withIncidence, full, almostFull, empty, almostEmpty'. Or any other application specific",
    )
    totalSlotNumber: Optional[confloat(ge=0.0)] = Field(
        None,
        description='The total number of slots offered by this bike docking station',
    )
    type: Optional[Type6] = Field(
        None, description='NGSI Entity type. It has to be BikeHireDockingStation'
    )
