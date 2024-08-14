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


class CategoryEnum(Enum):
    barrierAccess = 'barrierAccess'
    forBikes = 'forBikes'
    forCustomers = 'forCustomers'
    forDisabled = 'forDisabled'
    forElectricalVehicles = 'forElectricalVehicles'
    forEmployees = 'forEmployees'
    forMembers = 'forMembers'
    forPedestrian = 'forPedestrian'
    forVisitors = 'forVisitors'
    forResidents = 'forResidents'
    forStudents = 'forStudents'
    gateAccess = 'gateAccess'
    guarded = 'guarded'
    onlyElectricalVehicles = 'onlyElectricalVehicles'
    onlyPedestrian = 'onlyPedestrian'
    onlyResident = 'onlyResident'
    onlyResidents = 'onlyResidents'
    onlyWithPermit = 'onlyWithPermit'
    private = 'private'
    public = 'public'
    publicPrivate = 'publicPrivate'


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


class NotAllowedVehicleTypeEnum(Enum):
    anyVehicle = 'anyVehicle'
    agriculturalVehicle = 'agriculturalVehicle'
    bicycle = 'bicycle'
    bus = 'bus'
    car = 'car'
    caravan = 'caravan'
    carWithCaravan = 'carWithCaravan'
    carWithTrailer = 'carWithTrailer'
    constructionOrMaintenanceVehicle = 'constructionOrMaintenanceVehicle'
    dieselCarEuro0 = 'dieselCarEuro0'
    dieselCarEuro1 = 'dieselCarEuro1'
    dieselCarEuro2 = 'dieselCarEuro2'
    dieselCarEuro3 = 'dieselCarEuro3'
    dieselCarEuro4 = 'dieselCarEuro4'
    dieselCarEuro5a = 'dieselCarEuro5a'
    dieselCarEuro5b = 'dieselCarEuro5b'
    dieselCarEuro6 = 'dieselCarEuro6'
    freightTransportVehicle = 'freightTransportVehicle'
    lorry = 'lorry'
    moped = 'moped'
    motorcycle = 'motorcycle'
    motorcycleWithSideCar = 'motorcycleWithSideCar'
    motorscooter = 'motorscooter'
    petrolCarEuro0 = 'petrolCarEuro0'
    petrolCarEuro1 = 'petrolCarEuro1'
    petrolCarEuro2 = 'petrolCarEuro2'
    petrolCarEuro3 = 'petrolCarEuro3'
    petrolCarEuro4 = 'petrolCarEuro4'
    petrolCarEuro5 = 'petrolCarEuro5'
    petrolCarEuro6 = 'petrolCarEuro6'
    tanker = 'tanker'
    trailer = 'trailer'
    van = 'van'


class SecurityEnum(Enum):
    bollard = 'bollard'
    camera = 'camera'
    cctv = 'cctv'
    dog = 'dog'
    externalSecurity = 'externalSecurity'
    fencesareaSeperatedFromSurroundings = 'fencesareaSeperatedFromSurroundings'
    floodLight = 'floodLight'
    guard24hours = 'guard24hours'
    lighting = 'lighting'
    patrolled = 'patrolled'
    securityStaff = 'securityStaff'


class Type6(Enum):
    RestrictedTrafficArea = 'RestrictedTrafficArea'


class RestrictedTrafficArea(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    category: Optional[List[CategoryEnum]] = Field(
        None,
        description="Restricted traffic area's category(ies). The purpose of this field is to allow to tag, generally speaking, restricted traffic area entities. Particularities and detailed descriptions should be found under the corresponding specific attributes",
        min_length=1,
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
    notAllowedVehicleType: Optional[List[NotAllowedVehicleTypeEnum]] = Field(
        None,
        description='Vehicle type(s) not allowed to cross the restricted traffic area',
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
    regulation: Optional[AnyUrl] = Field(
        None,
        description='A URL pointing to the regulation for the specific restricted traffic area',
    )
    restrictionExceptions: Optional[
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
        description='Individual vehicle type allowed to cross the restricted traffic area in a specific time slot',
    )
    restrictionValidityHours: Optional[str] = Field(
        None,
        description='Days of the week and hours in which the traffic restriction is active',
    )
    security: Optional[List[SecurityEnum]] = Field(
        None,
        description='Security aspects provided by this restricted traffic area',
        min_length=1,
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    specialRestrictions: Optional[
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
        description='Individual vehicle type not allowed to cross the restricted traffic area in a specific time slot',
    )
    type: Optional[Type6] = Field(
        None, description='NGSI Entity type. It has to be RestrictedTrafficArea'
    )
    validityEndDate: Optional[AwareDatetime] = Field(
        None, description='The date at which the restriction is dismissed'
    )
    validityStartDate: Optional[AwareDatetime] = Field(
        None, description='The date from which the restriction is applied'
    )
