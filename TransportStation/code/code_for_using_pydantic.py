from __future__ import annotations

from datetime import date, time
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


class CurrencyAcceptedEnum(Enum):
    EUR = 'EUR'
    USD = 'USD'


class Dimension(BaseModel):
    depth: Optional[confloat(ge=0.0)] = Field(None, description='Depth of the Station')
    height: Optional[confloat(ge=0.0)] = Field(
        None, description='Height of the Station'
    )
    width: Optional[confloat(ge=0.0)] = Field(None, description='Width of the Station')


class InstallationMode(Enum):
    aerial = 'aerial'
    ground = 'ground'
    underGround = 'underGround'
    underSea = 'underSea'


class PlatformTypeEnum(Enum):
    lateral = 'lateral'
    central = 'central'


class Inventory(BaseModel):
    PlatformType: Optional[List[PlatformTypeEnum]] = Field(
        None, description='Type of platforms available'
    )
    nbOfIOPoint: Optional[confloat(ge=0.0)] = Field(
        None, description='Number of input output points'
    )
    nbOfLane: Optional[confloat(ge=0.0)] = Field(
        None, description='Number of Lane in the station'
    )
    nbOfPlatform: Optional[confloat(ge=0.0)] = Field(
        None, description='Number of platform'
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


class LocationType(Enum):
    number_0 = 0
    number_1 = 1
    number_2 = 2
    number_3 = 3
    number_4 = 4


class DayOfWeek(Enum):
    Monday = 'Monday'
    Tuesday = 'Tuesday'
    Wednesday = 'Wednesday'
    Thursday = 'Thursday'
    Friday = 'Friday'
    Saturday = 'Saturday'
    Sunday = 'Sunday'
    PublicHolidays = 'PublicHolidays'


class DayOfWeek1(Enum):
    https___schema_org_Monday = 'https://schema.org/Monday'
    https___schema_org_Tuesday = 'https://schema.org/Tuesday'
    https___schema_org_Wednesday = 'https://schema.org/Wednesday'
    https___schema_org_Thursday = 'https://schema.org/Thursday'
    https___schema_org_Friday = 'https://schema.org/Friday'
    https___schema_org_Saturday = 'https://schema.org/Saturday'
    https___schema_org_Sunday = 'https://schema.org/Sunday'
    https___schema_org_PublicHolidays = 'https://schema.org/PublicHolidays'


class OpeningHoursSpecificationItem(BaseModel):
    closes: Optional[time] = Field(
        None,
        description=' \\tThe closing hour of the place or service on the given day(s) of the week',
    )
    dayOfWeek: Optional[Union[DayOfWeek, DayOfWeek1]] = Field(
        None,
        description='The day of the week for which these opening hours are valid. URLs from GoodRelations (http://purl.org/goodrelations/v1) are used (for Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday plus a special entry for PublicHolidays)',
    )
    opens: Optional[time] = Field(
        None,
        description='The opening hour of the place or service on the given day(s) of the week',
    )
    validFrom: Optional[Union[date, AwareDatetime]] = Field(
        None,
        description='The date when the item becomes valid. A date value in the form CCYY-MM-DD or a combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm] in ISO 8601 date format',
    )
    validThrough: Optional[Union[date, AwareDatetime]] = Field(
        None,
        description='The date after when the item is not valid. For example the end of an offer, salary period, or a period of opening hours. A date value in the form CCYY-MM-DD or a combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm] in ISO 8601 date format',
    )


class PaymentAcceptedEnum(Enum):
    Cash = 'Cash'
    CreditCard = 'CreditCard'
    CryptoCurrency = 'CryptoCurrency'
    other = 'other'


class Services(BaseModel):
    defibrillator: Optional[bool] = Field(
        None, description='Attribute to indicate if there are defibrillators'
    )
    emergencyPhone: Optional[bool] = Field(
        None,
        description='Attribute to indicate if there are emergency phones available',
    )
    informationBoardDevice: Optional[bool] = Field(
        None,
        description='Attribute to indicate if there are information boards for users',
    )
    interactiveDevice: Optional[bool] = Field(
        None,
        description='Attribute to indicate if there are interactive devices (i.e. kiosks) for users',
    )
    messageDevice: Optional[bool] = Field(
        None,
        description='Attribute to indicate if there are devices for sharing messages with the users',
    )
    purchaseDevice: Optional[bool] = Field(
        None,
        description='Attribute to indicate if there are machines for ticket purchase',
    )
    restBench: Optional[bool] = Field(
        None,
        description='Attribute to indicate if the station has benches to sit on for resting',
    )
    shelters: Optional[bool] = Field(
        None,
        description='Attribute to indicate if there are shelter for users (i.e. rain)',
    )
    timetableDevice: Optional[bool] = Field(
        None,
        description='Attribute to indicate if there are boards or devices showing the time table of the station',
    )
    voiceDevice: Optional[bool] = Field(
        None,
        description='Attribute to indicate if there are PA systems or other voice devices ',
    )
    wheelChairAccessible: Optional[bool] = Field(
        None,
        description='Attribute to indicate if there are facilities for wheelchair users',
    )


class StationType(Enum):
    aerialLift = 'aerialLift'
    bus = 'bus'
    cableTram = 'cableTram'
    ferry = 'ferry'
    funicular = 'funicular'
    monorail = 'monorail'
    rail = 'rail'
    subway = 'subway'
    train = 'train'
    tram = 'tram'
    trolleybus = 'trolleybus'


class StationConnectedItem(BaseModel):
    linesConnected: Optional[List[str]] = Field(
        None, description='Identifiers of the connected lines to the station'
    )
    stationType: Optional[StationType] = Field(
        None, description='Type of transport station connected to'
    )


class StationTypeEnum(Enum):
    aerialLift = 'aerialLift'
    bus = 'bus'
    cableTram = 'cableTram'
    ferry = 'ferry'
    funicular = 'funicular'
    monorail = 'monorail'
    rail = 'rail'
    subway = 'subway'
    trolleybus = 'trolleybus'
    tram = 'tram'


class Type6(Enum):
    TransportStation = 'TransportStation'


class WheelChairAccessible(Enum):
    number_0 = 0
    number_1 = 1
    number_2 = 2


class TransportStation(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    architect: Optional[str] = Field(
        None, description='Architect that designed the station'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    commissioningDate: Optional[AwareDatetime] = Field(
        None, description='Commissioning date of the station'
    )
    constructionDate: Optional[AwareDatetime] = Field(
        None, description='Construction date of the station'
    )
    contactPoint: Optional[ContactPoint] = Field(
        None, description='The details to contact with the item'
    )
    contractingAuthority: Optional[str] = Field(
        None, description='Name of the contracting authority'
    )
    contractingCompany: Optional[str] = Field(
        None,
        description='Name of the contracting company responsible for the exploitation of the station',
    )
    currencyAccepted: Optional[List[CurrencyAcceptedEnum]] = Field(
        None, description='Accepted currencies for making payments in the Station'
    )
    dataProvider: Optional[str] = Field(
        None,
        description='A sequence of characters identifying the provider of the harmonised data entity',
    )
    dateCreated: Optional[AwareDatetime] = Field(
        None,
        description='Entity creation timestamp. This will usually be allocated by the storage platform',
    )
    dateLastReported: Optional[AwareDatetime] = Field(
        None,
        description='A timestamp which denotes the last time when the device successfully reported data. Date and time in an ISO8601 UTC format',
    )
    dateModified: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp of the last modification of the entity. This will usually be allocated by the storage platform',
    )
    description: Optional[str] = Field(None, description='A description of this item')
    dimension: Optional[Dimension] = Field(
        None,
        description='Global dimension. The format is structured by a sub-property of 3 items. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **MTR** represents Meters',
    )
    featuredArtist: Optional[
        List[
            Optional[
                Union[
                    Union[
                        constr(
                            pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                            min_length=1,
                            max_length=256,
                        ),
                        AnyUrl,
                    ],
                    str,
                ]
            ]
        ]
    ] = Field(None, description='Featured artists in the station')
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
    installationMode: Optional[InstallationMode] = Field(
        None,
        description="Location  relative to the ground reference. Enum:'aerial, ground, underGround, underSea'",
    )
    inventory: Optional[Inventory] = Field(
        None,
        description='General data mapping only for `locationType` = 0, 1, 3, 4. The format is structured by a sub-property of 4 items',
    )
    levelId: Optional[float] = Field(
        None,
        description='Floor on which the location is located. Numerical index associated with the floor. Indicates the relative position of this stage in relation to the others. The index 0 indicates the ground floor. The floors above ground level are indicated by positive indices, and the underground stages by negative indices',
    )
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    locationType: Optional[LocationType] = Field(
        None,
        description="Link to the GTFS standard repository describing the different location [Location Type]. 0 Stop or platform (place where users get on or off in a public transport vehicle). 1 Station (area or physical structure comprising one or more platforms). 2 Entrance or Exit (place where users can enter / exit a station from the street). 3 Generic intersection (location in a station that doesn't correspond to any other `location_type` value). 4 Boarding area of a specific location on a platform where users can get on / off in a vehicle",
    )
    name: Optional[str] = Field(None, description='The name of this item')
    openingHoursSpecification: Optional[List[OpeningHoursSpecificationItem]] = Field(
        None,
        description='A structured value providing information about the opening hours of a place or a certain service inside a place',
        min_length=1,
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
    parentStation: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(
        None,
        description="Link to the GTFS standard repository describing the different link between Station and Platform [Parent STATION]. Case '1' location_type = 0 (Stop / platform ), the parent_station field contains the ID of a station. Case '2' location_type = 1  (Station), this field must be empty. Case '3' location_type = 2 (Input / output) or location_type = 3 (generic intersection), the parent_station field contains the ID of a station location_type = 1. Case '4' location_type = 4 (boarding area), the parent_station field contains the ID of a platform",
    )
    paymentAccepted: Optional[List[PaymentAcceptedEnum]] = Field(
        None, description='Accepted methods of payment in the Station'
    )
    platformCode: Optional[float] = Field(
        None,
        description='Platform identifier for a platform type stop `location_type` = 0 when the stop is in a station',
    )
    refPointOfInterest: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(
        None,
        description='A reference to a point of interest associated to this observation',
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    services: Optional[Services] = Field(
        None, description='Object containing information bout the services included'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    stationConnected: Optional[List[StationConnectedItem]] = Field(
        None,
        description="Connections possible from this station. A structured value from 0 to N occurrences where each items is a string in the format `stationType` : [List of Lines connected, separated by a comma]. Enum:'aerialLift, bus, cableTram, ferry, funicular, monorail, rail, subway, train, tram, trolleybus'",
    )
    stationType: Optional[List[StationTypeEnum]] = Field(
        None,
        description="Type of transport station. Enum:'aerialLift, bus, cableTram, ferry, funicular, monorail, rail, subway, trolleybus, tram'",
    )
    type: Optional[Type6] = Field(
        None, description='NGSI Entity type. It has to be TransportStation'
    )
    webSite: Optional[str] = Field(
        None, description='Link to the official website for more information'
    )
    wheelChairAccessible: Optional[WheelChairAccessible] = Field(
        None,
        description='Access possible for Person with Reduced Mobility. For stops without parents 0 no information is available regarding the accessibility of the stop. 1 some vehicles at this stop can board a PMR user. 2 PRM user cannot board  at this stop. For a stop that is part of a station 0 the stop inherits the wheelchair_boarding behavior of the parent station, if it is filled in. 1 lanes provide wheelchair access to the stop / platform  from outside the station. 2 no lane provides wheelchair access to the stop / platform from outside the station. For station inputs / outputs 0 the station entry inherits the wheelchair_boarding behavior of the main station, if specified. 1 the station entrance is wheelchair accessible. 2 no wheelchair accessible route connects the station entrance to the stops / platforms',
    )
    zoneId: Optional[str] = Field(None, description='Pricing zone of the station')
