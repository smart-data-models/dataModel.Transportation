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


class FuelType(Enum):
    autogas = 'autogas'
    biodiesel = 'biodiesel'
    cng = 'cng'
    diesel = 'diesel'
    electric = 'electric'
    ethanol = 'ethanol'
    gasoline = 'gasoline'
    hybrid_electric_diesel = 'hybrid_electric_diesel'
    hybrid_electric_petrol = 'hybrid_electric_petrol'
    hydrogen = 'hydrogen'
    lpg = 'lpg'
    petrol = 'petrol'
    petrol_unleaded_ = 'petrol(unleaded)'
    petrol_leaded_ = 'petrol(leaded)'
    other = 'other'


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
    VehicleModel = 'VehicleModel'


class VehicleType(Enum):
    agriculturalVehicle = 'agriculturalVehicle'
    bicycle = 'bicycle'
    binTrolley = 'binTrolley'
    bus = 'bus'
    car = 'car'
    caravan = 'caravan'
    carWithCaravan = 'carWithCaravan'
    carWithTrailer = 'carWithTrailer'
    cleaningTrolley = 'cleaningTrolley'
    constructionOrMaintenanceVehicle = 'constructionOrMaintenanceVehicle'
    lorry = 'lorry'
    minibus = 'minibus'
    moped = 'moped'
    motorcycle = 'motorcycle'
    motorcycleWithSideCar = 'motorcycleWithSideCar'
    motorscooter = 'motorscooter'
    sweepingMachine = 'sweepingMachine'
    tanker = 'tanker'
    trailer = 'trailer'
    tram = 'tram'
    van = 'van'
    trolley = 'trolley'


class VehicleModel(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
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
    brandName: Optional[str] = Field(None, description="Vehicle's brand name")
    cargoVolume: Optional[confloat(ge=0.0)] = Field(
        None,
        description='The available volume for cargo or luggage. For automobiles, this is usually the trunk volume. If only a single value is provided (type Number) it will refer to the maximum volume',
    )
    color: Optional[str] = Field(None, description='The color of the product')
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
    depth: Optional[confloat(ge=0.0)] = Field(None, description="Vehicle's depth")
    description: Optional[str] = Field(None, description='A description of this item')
    fuelConsumption: Optional[confloat(ge=0.0)] = Field(
        None,
        description='The amount of fuel consumed for traveling a particular distance or temporal duration with the given vehicle (e.g. liters per 100 km)',
    )
    fuelType: Optional[FuelType] = Field(
        None,
        description="The type of fuel suitable for the engine or engines of the vehicle. Enum:'autogas, biodiesel, ethanol, cng, diesel, electric, gasoline, hybrid electric/diesel, hybrid electric/petrol, hydrogen, lpg, petrol, petrol(unleaded), petrol(leaded), other'",
    )
    height: Optional[confloat(ge=0.0)] = Field(None, description="Vehicle's height")
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
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    manufacturerName: Optional[str] = Field(
        None, description="Vehicle's manufacturer name"
    )
    modelName: Optional[str] = Field(None, description="Vehicle's model name")
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
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    type: Optional[Type6] = Field(
        None, description='NGSI Entity type. It has to be VehicleModel'
    )
    url: Optional[AnyUrl] = Field(
        None, description='URL which provides a description of this vehicle model'
    )
    vehicleEngine: Optional[str] = Field(
        None, description='Information about the engine or engines of the vehicle'
    )
    vehicleModelDate: Optional[AwareDatetime] = Field(
        None,
        description='The release date of a vehicle model (often used to differentiate versions of the same make and model)',
    )
    vehicleType: Optional[VehicleType] = Field(
        None,
        description="Type of vehicle from the point of view of its structural characteristics. This is different than the vehicle category . Enum:'agriculturalVehicle, anyVehicle, articulatedVehicle, bicycle, binTrolley, bus, car, caravan, carOrLightVehicle, carWithCaravan, carWithTrailer, cleaningTrolley, constructionOrMaintenanceVehicle, fourWheelDrive, highSidedVehicle, lorry, minibus, moped, motorcycle, motorcycleWithSideCar, motorscooter, sweepingMachine, tanker, threeWheeledVehicle, trailer, tram, twoWheeledVehicle, trolley, van, vehicleWithoutCatalyticConverter, vehicleWithCaravan, vehicleWithTrailer, withEvenNumberedRegistrationPlates, withOddNumberedRegistrationPlates, other'. The following values defined by _VehicleTypeEnum_ and _VehicleTypeEnum2_, [DATEX 2 version 2.3](http://d2docs.ndwcloud.nu/_static/umlmodel/v2.3/index.htm)",
    )
    weight: Optional[confloat(ge=0.0)] = Field(None, description="Vehicle's weigth")
    width: Optional[confloat(ge=0.0)] = Field(None, description="Vehicle's width")
