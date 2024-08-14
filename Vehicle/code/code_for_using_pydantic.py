from __future__ import annotations

from datetime import date
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


class CategoryEnum(Enum):
    municipalServices = 'municipalServices'
    nonTracked = 'nonTracked'
    private = 'private'
    public = 'public'
    specialUsage = 'specialUsage'
    tracked = 'tracked'


class DeviceBatteryStatus(Enum):
    connected = 'connected'
    disconnected = 'disconnected'


class EmergencyVehicleType(Enum):
    policeCar = 'policeCar'
    policeMotorcycle = 'policeMotorcycle'
    policeVan = 'policeVan'
    policeSWAT = 'policeSWAT'
    fireEngine = 'fireEngine'
    waterTender = 'waterTender'
    airAmbulance = 'airAmbulance'
    ambulance = 'ambulance'
    motorcycleAmbulance = 'motorcycleAmbulance'
    rescueVehicle = 'rescueVehicle'
    hazardousMaterialsApparatus = 'hazardousMaterialsApparatus'
    towTruck = 'towTruck'


class FeatureEnum(Enum):
    abs = 'abs'
    airbag = 'airbag'
    alarm = 'alarm'
    backCamera = 'backCamera'
    disabledRamp = 'disabledRamp'
    gps = 'gps'
    internetConnection = 'internetConnection'
    overspeed = 'overspeed'
    proximitySensor = 'proximitySensor'
    wifi = 'wifi'


class Heading(Enum):
    number__1 = -1


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


class Type6(Enum):
    Point = 'Point'


class PreviousLocation(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[float] = Field(..., min_length=2)
    type: Type6


class Type7(Enum):
    LineString = 'LineString'


class PreviousLocation1(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[Coordinate] = Field(..., min_length=2)
    type: Type7


class Type8(Enum):
    Polygon = 'Polygon'


class PreviousLocation2(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type8


class Type9(Enum):
    MultiPoint = 'MultiPoint'


class PreviousLocation3(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[float]]
    type: Type9


class Type10(Enum):
    MultiLineString = 'MultiLineString'


class PreviousLocation4(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type10


class Type11(Enum):
    MultiPolygon = 'MultiPolygon'


class PreviousLocation5(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[List[Coordinate]]]
    type: Type11


class ServiceProvidedEnum(Enum):
    auxiliaryServices = 'auxiliaryServices'
    cargoTransport = 'cargoTransport'
    construction = 'construction'
    fairground = 'fairground'
    garbageCollection = 'garbageCollection'
    goodsSelling = 'goodsSelling'
    maintenance = 'maintenance'
    parksAndGardens = 'parksAndGardens'
    roadSignalling = 'roadSignalling'
    specialTransport = 'specialTransport'
    streetCleaning = 'streetCleaning'
    streetLighting = 'streetLighting'
    urbanTransit = 'urbanTransit'
    wasteContainerCleaning = 'wasteContainerCleaning'


class ServiceStatus(Enum):
    broken = 'broken'
    onRoute = 'onRoute'
    outOfService = 'outOfService'
    parked = 'parked'


class Type12(Enum):
    Vehicle = 'Vehicle'


class VehicleRunningStatus(Enum):
    running = 'running'
    stopped = 'stopped'
    waiting = 'waiting'


class VehicleSpecialUsage(Enum):
    ambulance = 'ambulance'
    fireBrigade = 'fireBrigade'
    military = 'military'
    police = 'police'
    schoolTransportation = 'schoolTransportation'
    taxi = 'taxi'
    trashManagement = 'trashManagement'


class VehicleType(Enum):
    agriculturalVehicle = 'agriculturalVehicle'
    ambulance = 'ambulance'
    anyVehicle = 'anyVehicle'
    articulatedVehicle = 'articulatedVehicle'
    autorickshaw = 'autorickshaw'
    bicycle = 'bicycle'
    binTrolley = 'binTrolley'
    BRT_mini_bus_ = 'BRT mini bus·'
    BRT_bus = 'BRT bus'
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
    e_bike = 'e-bike'
    e_moped = 'e-moped'
    e_scooter = 'e-scooter'
    e_motorcycle = 'e-motorcycle'
    fireTender = 'fireTender'
    fourWheelDrive = 'fourWheelDrive'
    highSidedVehicle = 'highSidedVehicle'
    hopper = 'hopper'
    lorry = 'lorry'
    minibus = 'minibus'
    moped = 'moped'
    motorcycle = 'motorcycle'
    motorcycleWithSideCar = 'motorcycleWithSideCar'
    motorscooter = 'motorscooter'
    policeVan = 'policeVan'
    publicMotor = 'publicMotor'
    sweepingMachine = 'sweepingMachine'
    tanker = 'tanker'
    tempo = 'tempo'
    threeWheeledVehicle = 'threeWheeledVehicle'
    tipper = 'tipper'
    trailer = 'trailer'
    tram = 'tram'
    trolley = 'trolley'
    twoWheeledVehicle = 'twoWheeledVehicle'
    van = 'van'
    vehicleWithoutCatalyticConverter = 'vehicleWithoutCatalyticConverter'
    vehicleWithCaravan = 'vehicleWithCaravan'
    vehicleWithTrailer = 'vehicleWithTrailer'
    withEvenNumberedRegistrationPlates = 'withEvenNumberedRegistrationPlates'
    withOddNumberedRegistrationPlates = 'withOddNumberedRegistrationPlates'
    pilotVessel = 'pilotVessel'
    passengerVessel = 'passengerVessel'
    cargoVessel = 'cargoVessel'
    tug = 'tug'
    militaryVessel = 'militaryVessel'
    sailingVessel = 'sailingVessel'
    vessel = 'vessel'
    other = 'other'


class Vehicle(BaseModel):
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
    battery: Optional[confloat(ge=0.0, le=1.0)] = Field(
        None,
        description='The current percentage of battery left in case of an electric vehicle, or a device connected to the vehicle',
    )
    bearing: Optional[float] = Field(
        None,
        description="Gives the vehicle GPS angle measured in a clockwise direction from the True North. SameAs 'bearing' field from GTFS Realtime message-Position(https://developers.google.com/transit/gtfs-realtime/reference#message-position)",
    )
    cargoWeight: Optional[confloat(ge=0.0, gt=0.0)] = Field(
        None, description="Current weight of the vehicle's cargo"
    )
    category: Optional[List[CategoryEnum]] = Field(
        None,
        description="Vehicle category(ies) from an external point of view. This is different than the vehicle type (car, lorry, etc.) represented by the `vehicleType` property. Enum:'municipalServices, nonTracked, private, public, specialUsage, tracked'. Tracked vehicles are those vehicles which position is permanently tracked by a remote system. Or any other needed by an application They incorporate a GPS receiver together with a network connection to periodically update a reported position (location, speed, heading ...)",
    )
    color: Optional[str] = Field(None, description='The color of the product')
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
    dateFirstUsed: Optional[date] = Field(
        None, description='Timestamp which denotes when the vehicle was first used'
    )
    dateModified: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp of the last modification of the entity. This will usually be allocated by the storage platform',
    )
    dateVehicleFirstRegistered: Optional[date] = Field(
        None,
        description='The date of the first registration of the vehicle with the respective public authorities',
    )
    description: Optional[str] = Field(None, description='A description of this item')
    deviceBatteryStatus: Optional[DeviceBatteryStatus] = Field(
        None,
        description="Gives the Battery charging status of the reporting device. Enum:'connected, disconnected'",
    )
    deviceSimNumber: Optional[str] = Field(
        None, description='Gives the SIM number of the device in the vehicle'
    )
    emergencyVehicleType: Optional[EmergencyVehicleType] = Field(
        None,
        description="Type of emergency vehicle corresponding to this observation. Enum:'policeCar, policeMotorcycle, policeVan, policeSWAT, fireEngine, waterTender, airAmbulance, ambulance, motorcycleAmbulance, rescueVehicle, hazardousMaterialsApparatus, towTruck",
    )
    feature: Optional[List[FeatureEnum]] = Field(
        None,
        description="Feature(s) incorporated by the vehicle. Enum:' abs, airbag, alarm, backCamera, disabledRamp, gps, internetConnection, overspeed, proximitySensor, wifi'. Or any other needed by the application. In order to represent multiple instances of a feature it can be used the following syntax: `<feature>,<occurences>`. For example, a car with 4 airbags will be represented by `airbag,4`",
    )
    fleetVehicleId: Optional[str] = Field(
        None,
        description='The identifier of the vehicle in the context of the fleet of vehicles to which it belongs',
    )
    fuelEfficiency: Optional[float] = Field(
        None,
        description='The distance traveled per unit of fuel used, commonly in kilometers per liter (km/L)',
    )
    fuelFilled: Optional[float] = Field(
        None,
        description='Amount of fuel filled in liters to the vehicle corresponding to this observation',
    )
    fuelType: Optional[str] = Field(
        None,
        description='The type of fuel suitable for the engine or engines of the vehicle corresponding to this observation',
    )
    heading: Optional[Union[confloat(ge=0.0, le=360.0, lt=360.0), Heading]] = Field(
        None,
        description='Denotes the direction of travel of the vehicle and is specified in decimal degrees, where 0 <= `heading` < 360, counting clockwise relative to the true north. If the vehicle is stationary (i.e. the value of the `speed` attribute is `0`), then the value of the heading attribute must be equal to `-1`',
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
    ignitionStatus: Optional[bool] = Field(
        None, description='Gives the ignition status of the vehicle. True means ignited'
    )
    image: Optional[AnyUrl] = Field(None, description='An image of the item')
    license_plate: Optional[str] = Field(
        None,
        description="Gives the License Plate number of the vehicle. SameAs: license_plate field from GTFS Realtime message-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)'",
    )
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    mileageFromOdometer: Optional[float] = Field(
        None,
        description='The total distance travelled by the particular vehicle since its initial production, as read from its odometer',
    )
    municipalityInfo: Optional[MunicipalityInfo] = Field(
        None, description='Municipality information corresponding to this observation'
    )
    name: Optional[str] = Field(None, description='The name of this item')
    observationDateTime: Optional[AwareDatetime] = Field(
        None, description='Last reported time of observation'
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
    previousLocation: Optional[
        Union[
            PreviousLocation,
            PreviousLocation1,
            PreviousLocation2,
            PreviousLocation3,
            PreviousLocation4,
            PreviousLocation5,
        ]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    purchaseDate: Optional[AwareDatetime] = Field(
        None,
        description='The date the item e.g. vehicle was purchased by the current owner',
    )
    refVehicleModel: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Reference to a VehicleModel')
    reportId: Optional[str] = Field(
        None,
        description='Unique Id assigned for the issue or report or feedback or transaction corresponding to this observation',
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    serviceOnDuty: Optional[bool] = Field(
        None,
        description='Nature of service provided by emergency vehicle corresponding to this observation. True indicates the emergency vehicle corresponding to this observation is attending to/ servicing to an emergency call of duty and is False otherwise',
    )
    serviceProvided: Optional[List[ServiceProvidedEnum]] = Field(
        None,
        description="Service(s) the vehicle is capable of providing or it is assigned to. Enum:'auxiliaryServices, cargoTransport, construction, fairground, garbageCollection, goodsSelling, maintenance, parksAndGardens, roadSignalling, specialTransport, streetCleaning, streetLighting, urbanTransit, wasteContainerCleaning'. Or any other value needed by an specific application",
    )
    serviceStatus: Optional[ServiceStatus] = Field(
        None,
        description="Vehicle status (from the point of view of the service provided, so it could not apply to private vehicles). `parked` : Vehicle is parked and not providing any service at the moment. `onRoute` : Vehicle is performing a mission. A comma-separated modifier(s) can be added to indicate what mission is currently delivering the vehicle. For instance `onRoute,garbageCollection` can be used to denote that the vehicle is on route and in a garbage collection mission. 'broken' : Vehicle is suffering a temporary breakdown. `outOfService` : Vehicle is on the road but not performing any mission, probably going to its parking area. Enum:'broken, onRoute, outOfService, parked'",
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    speed: Optional[Union[confloat(ge=0.0), confloat(ge=-1.0, le=-1.0)]] = Field(
        None,
        description="Denotes the magnitude of the horizontal component of the vehicle's current velocity and is specified in Kilometers per Hour. If provided, the value of the speed attribute must be a non-negative real number. `-1` MAY be used if speed is transiently unknown for some reason",
    )
    tripNetWeightCollected: Optional[float] = Field(
        None,
        description='The net weight collected by the vehicle corresponding to this observation at the end of the trip',
    )
    type: Optional[Type12] = Field(
        None, description='NGSI Entity type. It has to be Vehicle'
    )
    vehicleAltitude: Optional[str] = Field(
        None, description='Gives the current altitude of the vehicle using GPS'
    )
    vehicleConfiguration: Optional[str] = Field(
        None,
        description="A short text indicating the configuration of the vehicle, e.g. '5dr hatchback ST 2.5 MT 225 hp' or 'limited edition'",
    )
    vehicleIdentificationNumber: Optional[str] = Field(
        None,
        description='The Vehicle Identification Number (VIN) is a unique serial number used by the automotive industry to identify individual motor vehicles',
    )
    vehiclePlateIdentifier: Optional[str] = Field(
        None,
        description=" An identifier or code displayed on a vehicle registration plate attached to the vehicle used for official identification purposes. The registration identifier is numeric or alphanumeric and is unique within the issuing authority's region. Normative References: DATEXII `vehicleRegistrationPlateIdentifier`",
    )
    vehicleRunningStatus: Optional[VehicleRunningStatus] = Field(
        None,
        description="Gives the Battery charging status of the reporting device. Enum:'running, waiting, stopped'",
    )
    vehicleSpecialUsage: Optional[VehicleSpecialUsage] = Field(
        None,
        description="Indicates whether the vehicle is been used for special purposes, like commercial rental, driving school, or as a taxi. The legislation in many countries requires this information to be revealed when offering a car for sale. Enum:'ambulance, fireBrigade, military, police, schoolTransportation, taxi, trashManagement'",
    )
    vehicleTrackerDevice: Optional[str] = Field(
        None,
        description='Installation status of the GPS device or the tracking device fitted to the vehicle corresponding to this observation',
    )
    vehicleType: Optional[VehicleType] = Field(
        None,
        description="Type of vehicle from the point of view of its structural characteristics. This is different than the vehicle category . Enum:'agriculturalVehicle, anyVehicle, articulatedVehicle, bicycle, binTrolley, bus, car, caravan, carOrLightVehicle, carWithCaravan, carWithTrailer, cleaningTrolley, constructionOrMaintenanceVehicle, fourWheelDrive, highSidedVehicle, lorry, minibus, moped, motorcycle, motorcycleWithSideCar, motorscooter, sweepingMachine, tanker, threeWheeledVehicle, trailer, tram, twoWheeledVehicle, trolley, van, vehicleWithoutCatalyticConverter, vehicleWithCaravan, vehicleWithTrailer, withEvenNumberedRegistrationPlates, withOddNumberedRegistrationPlates, other'. The following values defined by _VehicleTypeEnum_ and _VehicleTypeEnum2_, [DATEX 2 version 2.3](http://d2docs.ndwcloud.nu/_static/umlmodel/v2.3/index.htm) and extended for other uses",
    )
    wardId: Optional[str] = Field(
        None, description='Ward ID of the entity corresponding to this observation'
    )
    wardName: Optional[str] = Field(
        None, description='Ward name of the entity corresponding to this observation'
    )
    zoneName: Optional[str] = Field(
        None, description='Zone name of the entity corresponding to this observation'
    )
