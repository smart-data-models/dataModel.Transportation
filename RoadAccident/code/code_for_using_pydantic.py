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


class AccidentDescriptionEnum(Enum):
    field_0 = 0
    field_1 = 1
    field_2 = 2
    field_3 = 3
    field_4 = 4
    field_5 = 5
    field_6 = 6
    field_7 = 7
    field_8 = 8
    field_9 = 9
    field_10 = 10
    field_11 = 11
    field_12 = 12
    field_13 = 13
    field_14 = 14
    field_15 = 15
    field_16 = 16
    field_17 = 17
    field_18 = 18
    field_19 = 19
    field_20 = 20
    field_21 = 21
    field_22 = 22
    field_23 = 23
    field_24 = 24
    field_25 = 25
    field_26 = 26
    field_27 = 27
    field_28 = 28
    field_29 = 29
    field_30 = 30
    field_31 = 31
    field_32 = 32
    field_33 = 33
    field_34 = 34
    field_35 = 35
    field_36 = 36
    field_37 = 37
    field_38 = 38
    field_39 = 39
    field_40 = 40
    field_41 = 41
    field_42 = 42
    field_43 = 43
    field_44 = 44
    field_45 = 45
    field_46 = 46
    field_47 = 47
    field_48 = 48
    field_49 = 49
    field_50 = 50
    field_51 = 51
    field_52 = 52
    field_53 = 53
    field_54 = 54
    field_55 = 55
    field_56 = 56
    field_57 = 57
    field_58 = 58
    field_59 = 59
    field_60 = 60
    field_61 = 61
    field_62 = 62
    field_63 = 63
    field_64 = 64
    field_65 = 65
    field_66 = 66
    field_67 = 67
    field_68 = 68
    field_69 = 69
    field_70 = 70
    field_71 = 71
    field_72 = 72
    field_73 = 73
    field_74 = 74
    field_75 = 75
    field_76 = 76
    field_77 = 77
    field_78 = 78
    field_79 = 79
    field_80 = 80
    field_81 = 81
    field_82 = 82
    field_83 = 83
    field_84 = 84
    field_85 = 85
    field_86 = 86
    field_87 = 87
    field_88 = 88
    field_89 = 89


class AccidentLocation(Enum):
    field_0 = 0
    field_1 = 1
    field_2 = 2
    field_3 = 3
    field_4 = 4
    field_5 = 5
    field_6 = 6
    field_7 = 7
    field_8 = 8
    field_9 = 9


class Weekday(Enum):
    Monday = 'Monday'
    Tuesday = 'Tuesday'
    Wednesday = 'Wednesday'
    Thursday = 'Thursday'
    Friday = 'Friday'
    Saturday = 'Saturday'
    Sunday = 'Sunday'


class AccidentStatisticalDate(BaseModel):
    hour: Optional[int] = None
    quarter: Optional[int] = None
    weekday: Optional[Weekday] = Field(None, description='Week days')
    year: Optional[int] = None


class AccidentTypeEnum(Enum):
    field_1 = 1
    field_2 = 2
    field_3 = 3
    field_4 = 4
    field_5 = 5
    field_6 = 6
    field_7 = 7
    field_8 = 8
    field_9 = 9
    field_10 = 10
    field_11 = 11
    field_12 = 12


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


class RoadIntersection(Enum):
    field_1 = 1
    field_2 = 2
    field_3 = 3
    field_4 = 4
    field_5 = 5
    field_6 = 6
    field_7 = 7
    field_8 = 8
    field_9 = 9
    field_10 = 10
    field_11 = 11
    field_12 = 12


class RoadPaving(Enum):
    field_1 = 1
    field_2 = 2
    field_3 = 3


class RoadSign(Enum):
    field_1 = 1
    field_2 = 2
    field_3 = 3
    field_4 = 4
    field_5 = 5


class RoadSurface(Enum):
    field_1 = 1
    field_2 = 2
    field_3 = 3
    field_4 = 4
    field_5 = 5


class RoadTrunk(Enum):
    field_1 = 1
    field_2 = 2
    field_3 = 3
    field_4 = 4
    field_5 = 5
    field_6 = 6
    field_7 = 7
    field_8 = 8
    field_9 = 9
    field_10 = 10
    field_11 = 11
    field_12 = 12
    field_15 = 15


class Status(Enum):
    archived = 'archived'
    onGoing = 'onGoing'
    solved = 'solved'


class Type6(Enum):
    RoadAccident = 'RoadAccident'


class VehiclesInvolvedEnum(Enum):
    field_0 = 0
    field_1 = 1
    field_2 = 2
    field_3 = 3
    field_4 = 4
    field_5 = 5
    field_6 = 6
    field_7 = 7
    field_8 = 8
    field_9 = 9
    field_10 = 10
    field_11 = 11
    field_12 = 12
    field_13 = 13
    field_14 = 14
    field_15 = 15
    field_16 = 16
    field_17 = 17
    field_18 = 18
    field_19 = 19
    field_20 = 20
    field_21 = 21
    field_22 = 22
    field_23 = 23
    field_24 = 24


class WeakestSubject(Enum):
    field_0 = 0
    field_1 = 1
    field_2 = 2
    field_3 = 3
    field_4 = 4
    field_5 = 5
    field_6 = 6
    field_7 = 7
    field_8 = 8
    field_9 = 9
    field_10 = 10
    field_11 = 11
    field_12 = 12
    field_13 = 13
    field_14 = 14
    field_15 = 15
    field_16 = 16
    field_17 = 17
    field_18 = 18
    field_19 = 19
    field_20 = 20
    field_21 = 21
    field_22 = 22
    field_23 = 23
    field_24 = 24


class WeatherCondition(Enum):
    field_0 = 0
    field_1 = 1
    field_2 = 2
    field_3 = 3
    field_4 = 4
    field_5 = 5
    field_6 = 6
    field_7 = 7
    field_8 = 8
    field_9 = 9
    field_10 = 10
    field_11 = 11
    field_12 = 12
    field_13 = 13
    field_14 = 14
    field_15 = 15
    field_16 = 16
    field_17 = 17
    field_18 = 18
    field_19 = 19
    field_20 = 20
    field_21 = 21
    field_22 = 22
    field_23 = 23
    field_24 = 24
    field_25 = 25


class RoadAccident(BaseModel):
    accidentDate: Optional[AwareDatetime] = Field(
        None, description='Datetime of the accident'
    )
    accidentDescription: Optional[List[AccidentDescriptionEnum]] = Field(
        None,
        description='Description about this Road Accident as a combination of codified situation enlisted. 0: Unspecified circumstance; 1: Driver proceeded regularly without turning; 2: Driver proceeded with a distracted driving or undecided course; 3: Driver proceeded without maintaining a safe distance; 4: Driver proceeded without giving priority to the vehicle coming from the right; 5: Driver proceeded without respecting the stop; 6: Driver proceeded without respecting the signal to give precedence; 7: Driver proceeded against traffic; 8: Driver proceeded without respecting the traffic light or agent signals; 10: Driver proceeded without respecting the signs of prohibition of transit or access; 11: Driver proceeded with speeding; 12: Driver proceeded without respecting the speed limits; 13: Driver proceeded with the dazzling lights crossing other vehicles; 14: Driver turned right regularly; 15: It turned irregularly to the right; 16: Driver turned left regularly; 17: It turned irregularly to the left; 18: Driver passed at the intersection; 20: Driver proceeded regularly; 21: Driver proceeded with a distracted driving or undecided course; 22: Driver proceeded without maintaining a safe distance; 23: Driver proceeded with speeding; 24: Driver proceeded without respecting the speed limits; 25: It proceeded not near the right edge of the roadway; 26: Driver proceeded against traffic; 27: Driver proceeded without respecting the signs of prohibition of transit or access; 28: Driver proceeded with the dazzling lights crossing other vehicles; 29: Driver passed regularly; 30: It passed irregularly to the right; 31: Driver overtook on a curve, on a hill or with insufficient visibility; 32: It overtook a vehicle that was overtaking another; 33: Driver passed without observing the appropriate prohibition sign; 34: Maneuvered in relegation or conversion; 35: Driver maneuvered to get into the flow of circulation; 36: Maneuvering To turn left (private passage, distributor); 37: Driver maneuvered regularly to stop or stop; 38: Driver maneuvered irregularly to stop or stop; 39: It was joined by other irregular two-wheeled vehicles; 40: Driver proceeded regularly; 41: Driver proceeded with speeding; 42: Driver proceeded without respecting the speed limits; 43: Driver proceeded against traffic; 44: Driver passed the vehicle in gear; 45: Maneuvered; 46: Maneuvered without respecting traffic light or agent signals; 47: Driver came out of the driveway without precaution; 48: Driver stepped out of the lane and hit the pawn; 49: It did not give priority to the pedestrian on the appropriate crossings; 50: It overtook a vehicle stopped to allow the crossing; 51: Driver hit the pedestrian with the load; 52: Driver was passing a tram unevenly at the stop; 60: Driver proceeded regularly; 61: Driver proceeded with a distracted driving or undecided course; 62: Driver proceeded without maintaining a safe distance; 63: Driver proceeded against traffic; 64: Driver proceeded with speeding; 65: Driver proceeded without respecting the speed limits; 66: Driver proceeded without respecting the signs of prohibition of transit or access; 67: Driver was passing another vehicle in gear; 68: Driver imprudently crossed the level crossing; 70: Spill with spillage to avoid impact; 71: Listening with spillage for distracted driving; 72: List with over-speed spill; 73: Driver suddenly braked with consequence to the transported; 74: Fall of person from vehicle for: door opening; 75: Fall of person from vehicle for: descent from vehicle in motion; 76: Fall of person from vehicle due to: clinging or improperly placed; 80: Brake failure or failure; 81: Breakage or steering failure; 82: Tire burst or excessive wear; 83: Lack or insufficiency of headlights or position lights; 84: Lack or insufficiency of flashing lights or stopping light signals; 85: Breaking of trailer coupling parts; 86: Deficiency of dangerous goods transport equipment; 87: Deficiency of the adaptations prescribed to vehicles of physically handicapped people; 88: Wheel detachment; 89: Lack or insufficiency of visual devices for cycles',
    )
    accidentLocation: Optional[AccidentLocation] = Field(
        None,
        description='Brief description if the accident took place in a urban or extra-urban area. 0: Regional within the urban area 1: Urban road in the town 2: Provincial road within the town 3: State road within the village 4: Extra-urban road 5: Provincial 6: State road 7: Highway 8: Another way 9: Regional road',
    )
    accidentStatisticalDate: Optional[AccidentStatisticalDate] = Field(
        None,
        description='approximate datetime of the accident (often original accident data source reports only statistical attributes such as season, weekday and approximate hour',
    )
    accidentType: Optional[List[AccidentTypeEnum]] = Field(
        None,
        description='Quick classification this Road Accident. 1: Frontal collision; 2: Frontal-lateral collision; 3: Side crash; 4: Collision; 5: Pedestrian investment; 6: Impact with vehicle stopped or stopped; 7: Impact with parked vehicle; 8: Impact with obstacle; 9: Impact with train; 10: Spill, slip; 11: Accident due to sudden braking; 12: Accident due to falling from a vehicle;. ',
    )
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
    localId: Optional[str] = Field(
        None, description='Unique identifier from the source data set'
    )
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    name: Optional[str] = Field(None, description='The name of this item')
    numPassengersDead: Optional[confloat(ge=0.0)] = Field(
        None, description="Number of vehicle's passengers dead because the accident"
    )
    numPassengersInjured: Optional[confloat(ge=0.0)] = Field(
        None, description="Number of vehicle's passengers injured because the accident"
    )
    numPedestrianDead: Optional[confloat(ge=0.0)] = Field(
        None, description='Number of pedestrians dead because the accident'
    )
    numPedestrianInjured: Optional[confloat(ge=0.0)] = Field(
        None, description='Number of pedestrians injured because the accident'
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
    pedestriansInvolved: Optional[bool] = Field(
        None,
        description='Boolean to determine if pedestrians were involved in the accidents',
    )
    roadClass: Optional[str] = Field(
        None, description=' The classification of road where this accident took place'
    )
    roadIntersection: Optional[RoadIntersection] = Field(
        None,
        description='Brief description of the piece of the road where the accident took place.   1: Crossroad; 2: Roundabout; 3: Reported intersection; 4: Intersection with traffic light; 5: Intersection not reported; 6: Rail crossing; 7: Straight; 8: Curve; 9: Bump, bottleneck; 10: Slope; 11: Illuminated gallery; 12: Unlit gallery;',
    )
    roadPaving: Optional[RoadPaving] = Field(
        None,
        description='Road paving. 1: Paved road; 2: Rough paved road; 3: Unpaved road;',
    )
    roadSign: Optional[RoadSign] = Field(
        None,
        description='Brief description of the road sign where the accident took place. 1: Absent; 2: Vertical; 3: Horizontal; 4: Vertical and horizontal; 5: Temporary by construction site;',
    )
    roadSurface: Optional[RoadSurface] = Field(
        None,
        description='Brief description of the condition of the road during the accident. 1: Dry; 2: Wet; 3: Slippery; 4: frozen; 5: Snowcapped;',
    )
    roadTrunk: Optional[RoadTrunk] = Field(
        None,
        description='Brief description of type of trunk of the road where the accident took place. 1: Road branch; 2: Secondary branch; 3: Minor branch; 4: Junction branch; 5: Road junction; 6: Motorway left lane; 7: Highway carriageway right; 8: Motorway junction entrance; 9: Highway exit junction; 10: Highway junction trunk; 11: Highway station; 12: Other cases; 15: Extra urban road',
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    status: Optional[Status] = Field(
        None,
        description="Status of the Road Accident. Enum:'archived, onGoing, solved'",
    )
    totalDeadPeopleWithin24Hours: Optional[confloat(ge=0.0)] = Field(
        None, description='Number of people dead directly because the accident'
    )
    totalDeadPeopleWithin30Days: Optional[confloat(ge=0.0)] = Field(
        None, description='Number of people dead because the aftermath of the accident'
    )
    totalInjured: Optional[confloat(ge=0.0)] = Field(
        None,
        description='total number of people injured (not dead) because the accident',
    )
    type: Optional[Type6] = Field(
        None, description='NGSI Entity type. it has to be RoadAccident'
    )
    vehiclesInvolved: Optional[List[VehiclesInvolvedEnum]] = Field(
        None,
        description='List of the vehicles (and pedestrians) involved because the accident 0 : pedestrian 1 : bicycle 2 : agriculturalVehicle 3 : bus 4 : minibus 5 : car 6 : caravan 7 : tram 8 : tanker 9 : carWithCaravan 10 : carWithTrailer 11 : lorry 12 : moped 13 : tanker 14 : motorcycle 15 : motorcycleWithSideCar 16 : motorscooter 17 : trailer 18 : van 19 : caravan 20 : constructionOrMaintenanceVehicle 21 : trolley 22 : binTrolley 23 : sweepingMachine 24 : cleaningTrolley',
    )
    weakestSubject: Optional[WeakestSubject] = Field(
        None,
        description='vehicle that represent the weakest subject involved because the accident (usually pedestrian). 0 : pedestrian 1 : bicycle 2 : agriculturalVehicle 3 : bus 4 : minibus 5 : car 6 : caravan 7 : tram 8 : tanker 9 : carWithCaravan 10 : carWithTrailer 11 : lorry 12 : moped 13 : tanker 14 : motorcycle 15 : motorcycleWithSideCar 16 : motorscooter 17 : trailer 18 : van 19 : caravan 20 : constructionOrMaintenanceVehicle 21 : trolley 22 : binTrolley 23 : sweepingMachine 24 : cleaningTrolley',
    )
    weatherConditions: Optional[List[WeatherCondition]] = Field(
        None,
        description='Brief description of weather conditions during this Road Accident. 0 : clearNight 1 : sunnyDay 2 : slightlyCloudy 3 : partlyCloudy 4 : mist 5 : fog 6 : highClouds 7 : cloudy 8 : veryCloudy 9 : overcast 10 : lightRainShower 11 : drizzle 12 : lightRain 13 : heavyRainShower 14 : heavyRain 15 : sleetShower 16 : sleet 17 : hailShower 18 : hail 19 : shower 20 : lightSnow 21 : snow 22 : heavySnowShower 23 : heavySnow 24 : thunderShower 25 : thunder',
    )
