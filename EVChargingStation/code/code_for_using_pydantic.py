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


class AcceptedPaymentMethodEnum(Enum):
    ByBankTransferInAdvance = 'ByBankTransferInAdvance'
    ByInvoice = 'ByInvoice'
    Cash = 'Cash'
    CheckInAdvance = 'CheckInAdvance'
    COD = 'COD'
    DirectDebit = 'DirectDebit'
    GoogleCheckout = 'GoogleCheckout'
    PayPal = 'PayPal'
    PaySwarm = 'PaySwarm'


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
    bicycle = 'bicycle'
    bus = 'bus'
    car = 'car'
    caravan = 'caravan'
    motorcycle = 'motorcycle'
    motorscooter = 'motorscooter'
    truck = 'truck'


class ChargeTypeEnum(Enum):
    annualPayment = 'annualPayment'
    flat = 'flat'
    free = 'free'
    monthlyPayment = 'monthlyPayment'
    other = 'other'


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


class SocketTypeEnum(Enum):
    Caravan_Mains_Socket = 'Caravan_Mains_Socket'
    CHAdeMO = 'CHAdeMO'
    CCS_SAE = 'CCS/SAE'
    Dual_CHAdeMO = 'Dual_CHAdeMO'
    Dual_J_1772 = 'Dual_J-1772'
    Dual_Mennekes = 'Dual_Mennekes'
    J_1772 = 'J-1772'
    Mennekes = 'Mennekes'
    Other = 'Other'
    Tesla = 'Tesla'
    Type2 = 'Type2'
    Type3 = 'Type3'
    Wall_Euro = 'Wall_Euro'


class Status(Enum):
    almostEmpty = 'almostEmpty'
    almostFull = 'almostFull'
    empty = 'empty'
    full = 'full'
    outOfService = 'outOfService'
    withIncidence = 'withIncidence'
    working = 'working'


class Type6(Enum):
    EVChargingStation = 'EVChargingStation'


class VehicleType(Enum):
    agriculturalVehicle = 'agriculturalVehicle'
    ambulance = 'ambulance'
    articulatedVehicle = 'articulatedVehicle'
    autorickshaw = 'autorickshaw'
    bicycle = 'bicycle'
    binTrolley = 'binTrolley'
    BRT_bus = 'BRT bus'
    BRT_minibus = 'BRT minibus'
    bus = 'bus'
    car = 'car'
    caravan = 'caravan'
    carOrLightVehicle = 'carOrLightVehicle'
    carWithCaravan = 'carWithCaravan'
    carWithTrailer = 'carWithTrailer'
    cleaningTrolley = 'cleaningTrolley'
    compactor = 'compactor'
    constructionOrMaintenanceVehicle = 'constructionOrMaintenanceVehicle'
    dumper = 'dumper'
    e_moped = 'e-moped'
    e_scooter = 'e-scooter'
    e_motorcycle = 'e-motorcycle'
    fire_tender = 'fire tender'
    fourWheelDrive = 'fourWheelDrive'
    highSidedVehicle = 'highSidedVehicle'
    hopper = 'hopper'
    lorry = 'lorry'
    minibus = 'minibus'
    moped = 'moped'
    motorcycle = 'motorcycle'
    motorcycleWithSideCar = 'motorcycleWithSideCar'
    motorscooter = 'motorscooter'
    police_van = 'police van'
    sweepingMachine = 'sweepingMachine'
    tanker = 'tanker'
    tempo = 'tempo'
    threeWheeledVehicle = 'threeWheeledVehicle'
    tipper = 'tipper'
    trailer = 'trailer'
    tram = 'tram'
    twoWheeledVehicle = 'twoWheeledVehicle'
    trolley = 'trolley'
    van = 'van'


class EVChargingStation(BaseModel):
    acceptedPaymentMethod: Optional[List[AcceptedPaymentMethodEnum]] = Field(
        None,
        description="Type(s) of charge when using this station. Enum:'ByBankTransferInAdvance, ByInvoice, Cash, CheckInAdvance, COD, DirectDebit, GoogleCheckout, PayPal, PaySwarm'",
        min_length=1,
    )
    address: Optional[Address] = Field(None, description='The mailing address')
    allowedVehicleType: Optional[List[AllowedVehicleTypeEnum]] = Field(
        None,
        description="Vehicle type(s) which can be charged. Enum:'bicycle, bus, car, caravan, motorcycle, motorscooter, truck' ",
        min_length=1,
    )
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    amountCollected: Optional[float] = Field(
        None,
        description='Amount collected towards the service corresponding to this observation',
    )
    amperage: Optional[confloat(ge=0.0)] = Field(
        None, description='The total amperage offered by the charging station.'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    availableCapacity: Optional[confloat(ge=0.0)] = Field(
        None,
        description='The number of vehicles which currently can be charged. It must lower or equal than `capacity`',
    )
    capacity: Optional[confloat(ge=1.0)] = Field(
        None,
        description='The total number of vehicles which can be charged at the same time. The total number of sockets can be higher. ',
    )
    chargeType: Optional[List[ChargeTypeEnum]] = Field(
        None,
        description="Type(s) of charge when using this station. Enum:'annualPayment, flat, free, monthlyPayment, other'",
        min_length=1,
    )
    chargingUnitId: Optional[str] = Field(
        None,
        description='The Id of the charging point in the EV charging station corresponding to this observation',
    )
    contactPoint: Optional[ContactPoint] = Field(
        None, description='The details to contact with the item'
    )
    dataDescriptor: Optional[AnyUrl] = Field(
        None, description='URI pointing to the data-descriptor entity'
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
    endDateTime: Optional[AwareDatetime] = Field(
        None, description='Reported end time corresponding to this observation'
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
    network: Optional[str] = Field(
        None, description='The name of the Network, with that the operator cooperates. '
    )
    observationDateTime: Optional[AwareDatetime] = Field(
        None, description='Last reported time of observation'
    )
    openingHours: Optional[str] = Field(
        None, description='Opening hours of the charging station. '
    )
    operator: Optional[str] = Field(None, description="Charging station's operator. ")
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
    powerConsumption: Optional[float] = Field(
        None,
        description='Power consumed by the entity corresponding to this observation',
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    socketNumber: Optional[confloat(ge=1.0)] = Field(
        None, description='The total number of sockets offered by this charging station'
    )
    socketType: Optional[List[SocketTypeEnum]] = Field(
        None,
        description="The type of sockets offered by this station. Enum:'Caravan_Mains_Socket, CHAdeMO, CCS/SAE, Dual_CHAdeMO, Dual_J-1772, Dual_Mennekes, J-1772, Mennekes, Other, Tesla, Type2, Type3, Wall_Euro'",
        min_length=1,
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    startDateTime: Optional[AwareDatetime] = Field(
        None, description='Reported start time corresponding to this observation'
    )
    stationName: Optional[str] = Field(
        None,
        description='The name station corresponding to this observation. It can be the name of bike docking station, charging station, etc',
    )
    status: Optional[Status] = Field(
        None,
        description="Status of the charging station. Enum:'almostEmpty, almostFull, empty, full, outOfService, withIncidence, working'. Or any other application-specific",
    )
    taxAmountCollected: Optional[float] = Field(
        None,
        description='The amount of tax levied on the products, things and services which includes sales tax, value-added tax, service tax, Good and Service tax, customs duty, etc',
    )
    transactionId: Optional[str] = Field(
        None,
        description='Unique transaction Id of the entity corresponding to this observation',
    )
    transactionType: Optional[str] = Field(
        None,
        description='Type of the transaction based on the mode of payment (For eg. mobile/UPI, card, etc) or mode of service (For eg. Issue, ReIssue, Entry, Exit etc.) corresponding to this observation',
    )
    type: Optional[Type6] = Field(
        None, description='NGSI Entity type. It has to be EVChargingStation'
    )
    vehicleType: Optional[VehicleType] = Field(
        None,
        description="Type of vehicle from the point of view of its structural characteristics. This is different than the vehicle category . Enum:'agriculturalVehicle, ambulance, anyVehicle, articulatedVehicle, autorickshaw, bicycle, binTrolley, BRT bus, BRT minibus, bus, car, caravan, carOrLightVehicle, carWithCaravan, carWithTrailer, cleaningTrolley, compactor, constructionOrMaintenanceVehicle, dumper, e-moped, e-scooter, e-motorcycle,fire tender, fourWheelDrive, highSidedVehicle, hopper, lorry, minibus, moped, motorcycle, motorcycleWithSideCar, motorscooter, police van, sweepingMachine, tanker, tempo, threeWheeledVehicle, tipper, trailer, tram, twoWheeledVehicle, trolley, van, vehicleWithoutCatalyticConverter, vehicleWithCaravan, vehicleWithTrailer, withEvenNumberedRegistrationPlates, withOddNumberedRegistrationPlates, other'. The following values defined by _VehicleTypeEnum_ and _VehicleTypeEnum2_, [DATEX 2 version 2.3](http://d2docs.ndwcloud.nu/_static/umlmodel/v2.3/index.htm)",
    )
    voltage: Optional[confloat(ge=0.0)] = Field(
        None, description='The total voltage offered by the charging station'
    )
