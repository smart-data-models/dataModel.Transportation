<!-- 10-Header -->
  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

实体: Vehicle  
===============
<!-- /10-Header -->
  
<!-- 15-License -->
  

[开放许可证](https://github.com/smart-data-models//dataModel.Transportation/blob/master/Vehicle/LICENSE.md)  

[自动生成的文档](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->
  
<!-- 20-Description -->
  

Global description: **该实体模拟一种特定的车辆型号，包括所有属于此型号的多个车辆实例的共同属性。**  

version: 0.2.2  
<!-- /20-Description -->
  
<!-- 30-PropertiesList -->
  


## 属性列表  


<sup><sub>[*] 如果一个属性中没有指定类型，那是因为它可能有多种类型或不同的格式/模式</sub></sup>  
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)  
	- `addressCountry[string]`: 该国。例如，西班牙  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: 该街道地址所在的地区，以及该地区所在的区域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: 该地所在的地区，也是该国所在的地区  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: 区是某些国家的一种行政区划，由当地政府管理  
	- `postOfficeBoxNumber[string]`: 邮政信箱的邮政信箱号码。例如，03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: 邮政编码。例如，24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: 街道地址  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
	- `streetNr[string]`: 公共街道上特定房产的识别号码  
- `alternateName[string]`: 该物品的另一个名称  
- `annotations[array]`: 关于该项的注释  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `areaServed[string]`: 提供服务或项目的区域  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `battery[number]`: 电动车辆中电池剩余的当前百分比，或连接到车辆的设备  
- `bearing[number]`: 提供以真北为基准，顺时针方向测量的车辆GPS角度。与GTFS实时信息-位置（https://developers.google.com/transit/gtfs-realtime/reference#message-position）中的'bearing'字段相同。  . Model: [https://schema.org/Number](https://schema.org/Number)  
- `cargoWeight[number]`: 车辆货物的当前重量  . Model: [https://schema.org/Number](https://schema.org/Number)  
- `category[array]`: 从外部视角的车辆类别。这与由 `vehicleType` 属性表示的车辆类型（汽车、卡车等）不同。枚举：'municipalServices, nonTracked, private, public, specialUsage, tracked'。被跟踪的车辆是指其位置由远程系统永久跟踪的车辆。或者任何应用程序需要的其他车辆。它们结合GPS接收器和网络连接，定期更新报告位置（位置、速度、方向...）  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `color[string]`: 产品的颜色  . Model: [https://schema.org/color](https://schema.org/color)  
- `currentTripCount[number]`: 该观察对应的车辆在给定营运日的行程当前计数  . Model: [https://schema.org/Number](https://schema.org/Number)  
- `dataProvider[string]`: 识别和谐数据实体提供者的字符序列  
- `dateCreated[date-time]`: 实体创建时间戳。这通常由存储平台分配  
- `dateFirstUsed[date]`: 车辆首次使用的时间戳  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)  
- `dateModified[date-time]`: 实体最后修改的时间戳。这通常由存储平台分配  
- `dateVehicleFirstRegistered[date]`: 车辆首次向相关公共机构登记的日期  . Model: [https://schema.org/dateVehicleFirstRegistered](https://schema.org/dateVehicleFirstRegistered)  
- `description[string]`: 对此项的描述  
- `deviceBatteryStatus[string]`: 提供报告设备的电池充电状态。枚举：'已连接，已断开'  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `deviceSimNumber[string]`: 提供车辆内设备的SIM卡号码  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `emergencyVehicleType[string]`: 对应此观察的紧急车辆类型。枚举：'警车，警用摩托车，警用面包车，特警队，消防车，水罐车，空中救护车，救护车，摩托车救护车，救援车辆，危险品车，拖车'  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `feature[array]`: 车辆整合的功能。枚举：' abs, airbag, alarm, backCamera, disabledRamp, gps, internetConnection, overspeed, proximitySensor, wifi'。或者应用程序所需的其他功能。为了表示功能的多个实例，可以使用以下语法： `<功能>,<出现次数>`。例如，一辆车有4个安全气囊，将被表示为 `airbag,4`  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `fleetVehicleId[string]`: 该车辆在其所属车队中的标识符  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `fuelEfficiency[number]`: 每单位燃料消耗所行进的距离，通常用公里每升（公里/升）表示  . Model: [https://schema.org/Number](https://schema.org/Number)  
- `fuelFilled[number]`: 本观察对应车辆所加油量（升）  . Model: [https://schema.org/Number](https://schema.org/Number)  
- `fuelType[string]`: 该观察对应的车辆的发动机或发动机适用的燃料类型  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `heading[*]`: 表示车辆的行进方向，以十进制度为单位，范围为0 <= `heading` < 360，相对于真北顺时针计数。如果车辆静止（即`speed`属性的值为`0`），则`heading`属性的值必须等于`-1`。  . Model: [https://schema.org/Number](https://schema.org/Number)  
- `id[*]`: 实体的唯一标识符  
- `ignitionStatus[boolean]`: 提供车辆的点火状态。True 表示已点火  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)  
- `image[uri]`: 该物品的图像  . Model: [https://schema.org/URL](https://schema.org/URL)  
- `license_plate[string]`: 提供车辆的车牌号码。SameAs：GTFS实时信息中VehicleDescriptor（https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor）的license_plate字段。  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `location[*]`: GeoJSON指向该项的引用。它可以是Point、LineString、Polygon、MultiPoint、MultiLineString或MultiPolygon  
- `mileageFromOdometer[number]`: 该车辆自初始生产以来行驶的总距离，以其里程表读数为准  . Model: [https://schema.org/mileageFromOdometer](https://schema.org/mileageFromOdometer)  
- `municipalityInfo[object]`: 与此观察相对应的市政信息  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `cityId[string]`: 与此观测相对应的城市ID  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `cityName[string]`: 与此观测相对应的城市名称  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `district[string]`: 与此观测相对应的区名称  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `stateName[string]`: 该观察结果对应的州名称  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `ulbName[string]`: 与该观察相对应的城市地方机构名称  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `wardId[string]`: 与此观察相对应的病房ID  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `wardName[string]`: 与此观察相对应的病房名称  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `wardNum[number]`: 与此观察相对应的病房编号  . Model: [https://schema.org/Number](https://schema.org/Number)    
	- `zoneId[string]`: 与此观测相对应的区域ID  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `zoneName[string]`: 对应此观测的区域名称  . Model: [https://schema.org/Text](https://schema.org/Text)    
- `name[string]`: 该物品的名称  
- `observationDateTime[date-time]`: 最近报告的观测时间  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)  
- `owner[array]`: 包含对所有者唯一Id的JSON编码字符序列的列表  
- `previousLocation[*]`: 对项目的Geojson引用。它可以是点、线字符串、多边形、多点、多线字符串或多多边形  
- `purchaseDate[date-time]`: 该物品（例如车辆）被当前所有者购买的日期  . Model: [https://schema.org/purchaseDate](https://schema.org/purchaseDate)  
- `refVehicleModel[*]`: 对VehicleModel的引用  . Model: [https://schema.org/URL](https://schema.org/URL)  
- `reportId[string]`: 为此观察对应的问题、报告、反馈或事务分配的唯一ID  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `seeAlso[*]`: 关于该项目的附加资源的URI列表  
- `serviceOnDuty[boolean]`: 本次观察对应的紧急车辆所提供的服务性质。若紧急车辆对应本次观察正在处理/服务紧急呼叫任务，则为True，否则为False。  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)  
- `serviceProvided[array]`: 车辆能够提供的服务或其被分配的服务。枚举：'auxiliaryServices, cargoTransport, construction, fairground, garbageCollection, goodsSelling, maintenance, parksAndGardens, roadSignalling, specialTransport, streetCleaning, streetLighting, urbanTransit, wasteContainerCleaning'。或者任何特定应用程序所需的其他值。  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `serviceStatus[string]`: 车辆状态（从提供的服务角度来看，因此不适用于私人车辆）。 
`停车`：车辆已停车，目前不提供任何服务。 
`行驶中`：车辆正在执行任务。可以添加逗号分隔的修饰符来指示车辆当前正在执行哪个任务。例如，`行驶中，垃圾收集`可以用来表示车辆正在行驶中并执行垃圾收集任务。 
`故障`：车辆正在经历暂时的故障。 
`不提供服务`：车辆在道路上但不执行任何任务，可能正在前往其停车区域。 
枚举：`故障，行驶中，不提供服务，停车`  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)  
- `source[string]`: 一个字符序列，给出实体数据的原始来源作为URL。建议为源提供者的全限定域名，或源对象的URL。  
- `speed[*]`: 表示车辆当前速度的水平分量的大小，以公里每小时为单位指定。如果提供，速度属性的值必须是非负实数。 `-1` 可以在速度由于某种原因暂时未知时使用  . Model: [https://schema.org/Number](https://schema.org/Number)  
- `tripNetWeightCollected[number]`: 该观察对应的车辆在行程结束时收集的净重量  . Model: [https://schema.org/Number](https://schema.org/Number)  
- `type[string]`: NGSI 实体类型。它必须是车辆  
- `vehicleAltitude[string]`: 使用GPS获取车辆的当前海拔高度  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `vehicleConfiguration[string]`: 一段简短的文本，指示车辆的配置，例如“5门掀背车ST 2.5手动变速箱225马力”或“限量版”  . Model: [https://schema.org/vehicleConfiguration](https://schema.org/vehicleConfiguration)  
- `vehicleIdentificationNumber[string]`: 车辆识别号码（VIN）是汽车行业用来识别个别机动车辆的唯一序列号  . Model: [https://schema.org/vehicleIdentificationNumber](https://schema.org/vehicleIdentificationNumber)  
- `vehiclePlateIdentifier[string]`:  用于官方识别目的的车辆注册板上的标识符或代码，附着在车辆上。注册标识符是数字或字母数字的，并且在发行机构的区域内是唯一的。规范性引用：DATEXII `vehicleRegistrationPlateIdentifier`  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `vehicleRunningStatus[string]`: 提供报告设备的电池充电状态。枚举：'运行，等待，停止'  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `vehicleSpecialUsage[string]`: 指示该车辆是否用于特殊用途，例如商业租赁、驾驶学校或出租车。许多国家的法律要求在出售汽车时披露此信息。枚举：'救护车，消防队，军事，警察，校车，出租车，垃圾管理'  . Model: [https://schema.org/vehicleSpecialUsage](https://schema.org/vehicleSpecialUsage)  
- `vehicleTrackerDevice[string]`: 该观察对应车辆上GPS设备或跟踪设备的安装状态  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `vehicleType[string]`: 从其结构特征的角度来看的车辆类型。这与车辆类别不同。枚举：'农业车辆、任何车辆、半挂车、自行车、手推车、公共汽车、汽车、拖车、汽车或轻型车辆、带拖车的汽车、带拖车的汽车、清洁手推车、建筑或维护车辆、四轮驱动车、高边车、卡车、小型巴士、轻便摩托车、摩托车、带侧车的摩托车、摩托脚踏车、扫街机、油罐车、三轮车、拖车、有轨电车、两轮车、手推车、货车、无催化转换器的车辆、带拖车的车辆、带拖车的车辆、带有偶数注册牌的车辆、带有奇数注册牌的车辆、其他'。以下值由_VehicleTypeEnum_和_VehicleTypeEnum2_定义，[DATEX 2版本2.3](http://d2docs.ndwcloud.nu/_static/umlmodel/v2.3/index.htm)并为其他用途扩展。  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `wardId[string]`: 与此观察相对应的实体的区域编号  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `wardName[string]`: 该观察对应的实体的行政区划名称  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `zoneName[string]`: 该观测对应实体的区域名称  . Model: [https://schema.org/Text](https://schema.org/Text)  
<!-- /30-PropertiesList -->
  
<!-- 35-RequiredProperties -->
  

必需属性  
- `类别`  
- `id`  
- `位置`  
- `类型`  
- `车辆类型`  
<!-- /35-RequiredProperties -->
  
<!-- 40-NotesYaml -->
  
<!-- /40-NotesYaml -->
  
<!-- 50-DataModelHeader -->
  

## 数据模型属性描述  

按字母顺序排序（点击查看详情）  
<!-- /50-DataModelHeader -->
  
<!-- 60-ModelYaml -->
  
<details><summary><strong>full yaml details</strong></summary>    

```yaml  
Vehicle:    
  description: This entity models a particular vehicle model, including all properties which are common to multiple vehicle instances belonging to such model.    
  properties:    
    address:    
      description: The mailing address    
      properties:    
        addressCountry:    
          description: The country. For example, Spain    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressCountry    
            type: Property    
        addressLocality:    
          description: The locality in which the street address is, and which is in the region    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressLocality    
            type: Property    
        addressRegion:    
          description: The region in which the locality is, and which is in the country    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressRegion    
            type: Property    
        district:    
          description: A district is a type of administrative division that, in some countries, is managed by the local government    
          type: string    
          x-ngsi:    
            type: Property    
        postOfficeBoxNumber:    
          description: The post office box number for PO box addresses. For example, 03578    
          type: string    
          x-ngsi:    
            model: https://schema.org/postOfficeBoxNumber    
            type: Property    
        postalCode:    
          description: The postal code. For example, 24004    
          type: string    
          x-ngsi:    
            model: https://schema.org/https://schema.org/postalCode    
            type: Property    
        streetAddress:    
          description: The street address    
          type: string    
          x-ngsi:    
            model: https://schema.org/streetAddress    
            type: Property    
        streetNr:    
          description: Number identifying a specific property on a public street    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: An alternative name for this item    
      type: string    
      x-ngsi:    
        type: Property    
    annotations:    
      description: Annotations about the item    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    battery:    
      description: The current percentage of battery left in case of an electric vehicle, or a device connected to the vehicle    
      maximum: 1    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    bearing:    
      description: Gives the vehicle GPS angle measured in a clockwise direction from the True North. SameAs 'bearing' field from GTFS Realtime message-Position(https://developers.google.com/transit/gtfs-realtime/reference#message-position)    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    cargoWeight:    
      description: Current weight of the vehicle's cargo    
      exclusiveMinimum: 0    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Kilograms    
    category:    
      description: Vehicle category(ies) from an external point of view. This is different than the vehicle type (car, lorry, etc.) represented by the `vehicleType` property. Enum:'municipalServices, nonTracked, private, public, specialUsage, tracked'. Tracked vehicles are those vehicles which position is permanently tracked by a remote system. Or any other needed by an application They incorporate a GPS receiver together with a network connection to periodically update a reported position (location, speed, heading ...)    
      items:    
        enum:    
          - municipalServices    
          - nonTracked    
          - private    
          - public    
          - specialUsage    
          - tracked    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    color:    
      description: The color of the product    
      type: string    
      x-ngsi:    
        model: https://schema.org/color    
        type: Property    
    currentTripCount:    
      description: The current count of trips made by the vehicle corresponding to this observation on the given day of operation    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    dataProvider:    
      description: A sequence of characters identifying the provider of the harmonised data entity    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: Entity creation timestamp. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateFirstUsed:    
      description: Timestamp which denotes when the vehicle was first used    
      format: date    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateVehicleFirstRegistered:    
      description: The date of the first registration of the vehicle with the respective public authorities    
      format: date    
      type: string    
      x-ngsi:    
        model: https://schema.org/dateVehicleFirstRegistered    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    deviceBatteryStatus:    
      description: Gives the Battery charging status of the reporting device. Enum:'connected, disconnected'    
      enum:    
        - connected    
        - disconnected    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    deviceSimNumber:    
      description: Gives the SIM number of the device in the vehicle    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    emergencyVehicleType:    
      description: Type of emergency vehicle corresponding to this observation. Enum:'policeCar, policeMotorcycle, policeVan, policeSWAT, fireEngine, waterTender, airAmbulance, ambulance, motorcycleAmbulance, rescueVehicle, hazardousMaterialsApparatus, towTruck    
      enum:    
        - policeCar    
        - policeMotorcycle    
        - policeVan    
        - policeSWAT    
        - fireEngine    
        - waterTender    
        - airAmbulance    
        - ambulance    
        - motorcycleAmbulance    
        - rescueVehicle    
        - hazardousMaterialsApparatus    
        - towTruck    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    feature:    
      description: 'Feature(s) incorporated by the vehicle. Enum:'' abs, airbag, alarm, backCamera, disabledRamp, gps, internetConnection, overspeed, proximitySensor, wifi''. Or any other needed by the application. In order to represent multiple instances of a feature it can be used the following syntax: `<feature>,<occurences>`. For example, a car with 4 airbags will be represented by `airbag,4`'    
      items:    
        enum:    
          - abs    
          - airbag    
          - alarm    
          - backCamera    
          - disabledRamp    
          - gps    
          - internetConnection    
          - overspeed    
          - proximitySensor    
          - wifi    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    fleetVehicleId:    
      description: The identifier of the vehicle in the context of the fleet of vehicles to which it belongs    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    fuelEfficiency:    
      description: The distance traveled per unit of fuel used, commonly in kilometers per liter (km/L)    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fuelFilled:    
      description: Amount of fuel filled in liters to the vehicle corresponding to this observation    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fuelType:    
      description: The type of fuel suitable for the engine or engines of the vehicle corresponding to this observation    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    heading:    
      description: Denotes the direction of travel of the vehicle and is specified in decimal degrees, where 0 <= `heading` < 360, counting clockwise relative to the true north. If the vehicle is stationary (i.e. the value of the `speed` attribute is `0`), then the value of the heading attribute must be equal to `-1`    
      oneOf:    
        - exclusiveMaximum: 360    
          maximum: 360    
          minimum: 0    
          type: number    
        - enum:    
            - -1    
          type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Degree    
    id:    
      anyOf:    
        - description: Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
          x-ngsi:    
            type: Property    
        - description: Identifier format of any NGSI entity    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      description: Unique identifier of the entity    
      x-ngsi:    
        type: Relationship    
    ignitionStatus:    
      description: Gives the ignition status of the vehicle. True means ignited    
      type: boolean    
      x-ngsi:    
        model: https://schema.org/Boolean    
        type: Property    
    image:    
      description: An image of the item    
      format: uri    
      type: string    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Property    
    license_plate:    
      description: 'Gives the License Plate number of the vehicle. SameAs: license_plate field from GTFS Realtime message-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)'''    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    location:    
      description: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon    
      oneOf:    
        - description: Geojson reference to the item. Point    
          properties:    
            bbox:    
              description: BBox of the  Point    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the Point    
              items:    
                type: number    
              minItems: 2    
              type: array    
              x-ngsi:    
                type: Property    
            type:    
              enum:    
                - Point    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON Point    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. LineString    
          properties:    
            bbox:    
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the LineString    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
              x-ngsi:    
                type: Property    
            type:    
              enum:    
                - LineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON LineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. Polygon    
          properties:    
            bbox:    
              description: BBox coordinates of the Polygon    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the Polygon    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
            type:    
              enum:    
                - Polygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON Polygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiPoint    
          properties:    
            bbox:    
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the MulitPoint    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
            type:    
              enum:    
                - MultiPoint    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiPoint    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
          properties:    
            bbox:    
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the MultiLineString    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
            type:    
              enum:    
                - MultiLineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiLineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              description: Coordinates of the MultiPolygon    
              items:    
                items:    
                  items:    
                    items:    
                      type: number    
                    minItems: 2    
                    type: array    
                  minItems: 4    
                  type: array    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
            type:    
              enum:    
                - MultiPolygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiPolygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
      x-ngsi:    
        type: GeoProperty    
    mileageFromOdometer:    
      description: The total distance travelled by the particular vehicle since its initial production, as read from its odometer    
      type: number    
      x-ngsi:    
        model: https://schema.org/mileageFromOdometer    
        type: Property    
    municipalityInfo:    
      description: Municipality information corresponding to this observation    
      properties:    
        cityId:    
          description: City ID corresponding to this observation    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        cityName:    
          description: City name corresponding to this observation    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        district:    
          description: District name corresponding to this observation    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        stateName:    
          description: Name of the state corresponding to this observation    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        ulbName:    
          description: Name of the Urban Local Body corresponding to this observation    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        wardId:    
          description: Ward ID corresponding to this observation    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        wardName:    
          description: Ward name corresponding to this observation    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        wardNum:    
          description: Ward number corresponding to this observation    
          type: number    
          x-ngsi:    
            model: https://schema.org/Number    
            type: Property    
        zoneId:    
          description: Zone ID corresponding to this observation    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        zoneName:    
          description: Zone name corresponding to this observation    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
      type: object    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    observationDateTime:    
      description: Last reported time of observation    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf:    
          - description: Identifier format of any NGSI entity    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
            x-ngsi:    
              type: Property    
          - description: Identifier format of any NGSI entity    
            format: uri    
            type: string    
            x-ngsi:    
              type: Property    
        description: Unique identifier of the entity    
        x-ngsi:    
          type: Relationship    
      type: array    
      x-ngsi:    
        type: Property    
    previousLocation:    
      description: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon    
      oneOf:    
        - description: Geojson reference to the item. Point    
          properties:    
            bbox:    
              description: BBox of the  Point    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the Point    
              items:    
                type: number    
              minItems: 2    
              type: array    
              x-ngsi:    
                type: Property    
            type:    
              enum:    
                - Point    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON Point    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. LineString    
          properties:    
            bbox:    
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the LineString    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
              x-ngsi:    
                type: Property    
            type:    
              enum:    
                - LineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON LineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. Polygon    
          properties:    
            bbox:    
              description: BBox coordinates of the Polygon    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the Polygon    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
            type:    
              enum:    
                - Polygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON Polygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiPoint    
          properties:    
            bbox:    
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the MulitPoint    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
            type:    
              enum:    
                - MultiPoint    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiPoint    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
          properties:    
            bbox:    
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the MultiLineString    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
            type:    
              enum:    
                - MultiLineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiLineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              description: Coordinates of the MultiPolygon    
              items:    
                items:    
                  items:    
                    items:    
                      type: number    
                    minItems: 2    
                    type: array    
                  minItems: 4    
                  type: array    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
            type:    
              enum:    
                - MultiPolygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiPolygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
      x-ngsi:    
        type: GeoProperty    
    purchaseDate:    
      description: The date the item e.g. vehicle was purchased by the current owner    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/purchaseDate    
        type: Property    
    refVehicleModel:    
      anyOf:    
        - description: Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
          x-ngsi:    
            type: Property    
        - description: Identifier format of any NGSI entity    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      description: Reference to a VehicleModel    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Relationship    
    reportId:    
      description: Unique Id assigned for the issue or report or feedback or transaction corresponding to this observation    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    seeAlso:    
      description: list of uri pointing to additional resources about the item    
      oneOf:    
        - items:    
            format: uri    
            type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      x-ngsi:    
        type: Property    
    serviceOnDuty:    
      description: Nature of service provided by emergency vehicle corresponding to this observation. True indicates the emergency vehicle corresponding to this observation is attending to/ servicing to an emergency call of duty and is False otherwise    
      type: boolean    
      x-ngsi:    
        model: https://schema.org/Boolean    
        type: Property    
    serviceProvided:    
      description: Service(s) the vehicle is capable of providing or it is assigned to. Enum:'auxiliaryServices, cargoTransport, construction, fairground, garbageCollection, goodsSelling, maintenance, parksAndGardens, roadSignalling, specialTransport, streetCleaning, streetLighting, urbanTransit, wasteContainerCleaning'. Or any other value needed by an specific application    
      items:    
        enum:    
          - auxiliaryServices    
          - cargoTransport    
          - construction    
          - fairground    
          - garbageCollection    
          - goodsSelling    
          - maintenance    
          - parksAndGardens    
          - roadSignalling    
          - specialTransport    
          - streetCleaning    
          - streetLighting    
          - urbanTransit    
          - wasteContainerCleaning    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    serviceStatus:    
      description: 'Vehicle status (from the point of view of the service provided, so it could not apply to private vehicles). `parked` : Vehicle is parked and not providing any service at the moment. `onRoute` : Vehicle is performing a mission. A comma-separated modifier(s) can be added to indicate what mission is currently delivering the vehicle. For instance `onRoute,garbageCollection` can be used to denote that the vehicle is on route and in a garbage collection mission. ''broken'' : Vehicle is suffering a temporary breakdown. `outOfService` : Vehicle is on the road but not performing any mission, probably going to its parking area. Enum:''broken, onRoute, outOfService, parked'''    
      enum:    
        - broken    
        - onRoute    
        - outOfService    
        - parked    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    source:    
      description: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object    
      type: string    
      x-ngsi:    
        type: Property    
    speed:    
      description: Denotes the magnitude of the horizontal component of the vehicle's current velocity and is specified in Kilometers per Hour. If provided, the value of the speed attribute must be a non-negative real number. `-1` MAY be used if speed is transiently unknown for some reason    
      oneOf:    
        - minimum: 0    
          type: number    
        - maximum: -1    
          minimum: -1    
          type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Km/h    
    tripNetWeightCollected:    
      description: The net weight collected by the vehicle corresponding to this observation at the end of the trip    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be Vehicle    
      enum:    
        - Vehicle    
      type: string    
      x-ngsi:    
        type: Property    
    vehicleAltitude:    
      description: Gives the current altitude of the vehicle using GPS    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    vehicleConfiguration:    
      description: A short text indicating the configuration of the vehicle, e.g. '5dr hatchback ST 2.5 MT 225 hp' or 'limited edition'    
      type: string    
      x-ngsi:    
        model: https://schema.org/vehicleConfiguration    
        type: Property    
    vehicleIdentificationNumber:    
      description: The Vehicle Identification Number (VIN) is a unique serial number used by the automotive industry to identify individual motor vehicles    
      type: string    
      x-ngsi:    
        model: https://schema.org/vehicleIdentificationNumber    
        type: Property    
    vehiclePlateIdentifier:    
      description: ' An identifier or code displayed on a vehicle registration plate attached to the vehicle used for official identification purposes. The registration identifier is numeric or alphanumeric and is unique within the issuing authority''s region. Normative References: DATEXII `vehicleRegistrationPlateIdentifier`'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    vehicleRunningStatus:    
      description: Gives the Battery charging status of the reporting device. Enum:'running, waiting, stopped'    
      enum:    
        - running    
        - stopped    
        - waiting    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    vehicleSpecialUsage:    
      description: Indicates whether the vehicle is been used for special purposes, like commercial rental, driving school, or as a taxi. The legislation in many countries requires this information to be revealed when offering a car for sale. Enum:'ambulance, fireBrigade, military, police, schoolTransportation, taxi, trashManagement'    
      enum:    
        - ambulance    
        - fireBrigade    
        - military    
        - police    
        - schoolTransportation    
        - taxi    
        - trashManagement    
      type: string    
      x-ngsi:    
        model: https://schema.org/vehicleSpecialUsage    
        type: Property    
    vehicleTrackerDevice:    
      description: Installation status of the GPS device or the tracking device fitted to the vehicle corresponding to this observation    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    vehicleType:    
      description: Type of vehicle from the point of view of its structural characteristics. This is different than the vehicle category . Enum:'agriculturalVehicle, anyVehicle, articulatedVehicle, bicycle, binTrolley, bus, car, caravan, carOrLightVehicle, carWithCaravan, carWithTrailer, cleaningTrolley, constructionOrMaintenanceVehicle, fourWheelDrive, highSidedVehicle, lorry, minibus, moped, motorcycle, motorcycleWithSideCar, motorscooter, sweepingMachine, tanker, threeWheeledVehicle, trailer, tram, twoWheeledVehicle, trolley, van, vehicleWithoutCatalyticConverter, vehicleWithCaravan, vehicleWithTrailer, withEvenNumberedRegistrationPlates, withOddNumberedRegistrationPlates, other'. The following values defined by _VehicleTypeEnum_ and _VehicleTypeEnum2_, [DATEX 2 version 2.3](http://d2docs.ndwcloud.nu/_static/umlmodel/v2.3/index.htm) and extended for other uses    
      enum:    
        - agriculturalVehicle    
        - ambulance    
        - anyVehicle    
        - articulatedVehicle    
        - autorickshaw    
        - bicycle    
        - binTrolley    
        - BRT mini bus·    
        - BRT bus    
        - bus    
        - car    
        - caravan    
        - carOrLightVehicle    
        - carWithCaravan    
        - carWithTrailer    
        - cleaningTrolley    
        - compactor    
        - constructionOrMaintenanceVehicle    
        - dumper    
        - e-bike    
        - e-moped    
        - e-scooter    
        - e-motorcycle    
        - fireTender    
        - fourWheelDrive    
        - highSidedVehicle    
        - hopper    
        - lorry    
        - minibus    
        - moped    
        - motorcycle    
        - motorcycleWithSideCar    
        - motorscooter    
        - policeVan    
        - publicMotor    
        - sweepingMachine    
        - tanker    
        - tempo    
        - threeWheeledVehicle    
        - tipper    
        - trailer    
        - tram    
        - trolley    
        - twoWheeledVehicle    
        - van    
        - vehicleWithoutCatalyticConverter    
        - vehicleWithCaravan    
        - vehicleWithTrailer    
        - withEvenNumberedRegistrationPlates    
        - withOddNumberedRegistrationPlates    
        - pilotVessel    
        - passengerVessel    
        - cargoVessel    
        - tug    
        - militaryVessel    
        - sailingVessel    
        - vessel    
        - other    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    wardId:    
      description: Ward ID of the entity corresponding to this observation    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    wardName:    
      description: Ward name of the entity corresponding to this observation    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    zoneName:    
      description: Zone name of the entity corresponding to this observation    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
  required:    
    - id    
    - type    
    - vehicleType    
    - category    
    - location    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms...    
  x-license-url: https://github.com/smart-data-models/dataModel.Transportation/blob/master/Vehicle/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Transportation/Vehicle/schema.json    
  x-model-tags: IUDX, SEDIMARK    
  x-version: 0.2.2    
```  
</details>    
<!-- /60-ModelYaml -->
  
<!-- 70-MiddleNotes -->
  
<!-- /70-MiddleNotes -->
  
<!-- 80-Examples -->
  

## 示例有效载荷  

#### 车辆NGSI-v2键值示例  

这是JSON格式的车辆示例，以键值对的形式呈现。当使用`options=keyValues`时，这与NGSI-v2兼容，并返回个体实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    

```json  

{  
  "id": "vehicle:WasteManagement:1",  
  "type": "Vehicle",  
  "vehicleType": "lorry",  
  "battery": 0.81,  
  "category": [  
    "municipalServices"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -3.164485591715449,  
      40.62785133667262  
    ]  
  },  
  "name": "C Recogida 1",  
  "speed": 50,  
  "cargoWeight": 314,  
  "serviceStatus": "onRoute",  
  "serviceProvided": [  
    "garbageCollection",  
    "wasteContainerCleaning"  
  ],  
  "areaServed": "Centro",  
  "refVehicleModel": "vehiclemodel:econic",  
  "vehiclePlateIdentifier": "3456ABC",  
  "bearing": 43,  
  "fuelEfficiency": 13,  
  "fuelType": "Petrol",  
  "fuelFilled": 6,  
  "tripNetWeightCollected": 12,  
  "vehicleTrackerDevice": "Installed",  
  "wardId": "4",  
  "license_plate": "KA052134",  
  "currentTripCount": 1,  
  "reportId": "21645",  
  "zoneName": "South Zone",  
  "vehicleAltitude": "600",  
  "deviceSimNumber": "9942142573",  
  "wardName": "Kempegowda Ward",  
  "deviceBatteryStatus": "connected",  
  "ignitionStatus": true,  
  "vehicleRunningStatus": "running",  
  "observationDateTime": "2021-03-11T15:51:02+05:30",  
  "serviceOnDuty": false,  
  "emergencyVehicleType": "ambulance",  
  "municipalityInfo": {  
    "district": "Bangalore Urban",  
    "ulbName": "BMC",  
    "cityId": "23",  
    "wardId": "23",  
    "stateName": "Karnataka",  
    "cityName": "Bangalore",  
    "zoneName": "South",  
    "wardName": "Bangalore Urban",  
    "zoneId": "2",  
    "wardNum": 4  
  }  
}  
```  
</details>  

#### 车辆NGSI-v2标准化示例  

这是一个以JSON格式标准化的车辆示例。当不使用选项时，它与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    

```json  

{  
  "id": "vehicle:WasteManagement:1",  
  "type": "Vehicle",  
  "category": {  
    "type": "StructuredValue",  
    "value": [  
      "municipalServices"  
    ]  
  },  
  "vehicleType": {  
    "type": "Text",  
    "value": "lorry"  
  },  
  "battery": {  
    "type": "Number",  
    "value": 0.81  
  },  
  "name": {  
    "type": "Text",  
    "value": "C Recogida 1"  
  },  
  "vehiclePlateIdentifier": {  
    "type": "Text",  
    "value": "3456ABC"  
  },  
  "refVehicleModel": {  
    "type": "Text",  
    "value": "vehiclemodel:econic"  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -3.164485591715449,  
        40.62785133667262  
      ]  
    },  
    "metadata": {  
      "timestamp": {  
        "type": "DateTime",  
        "value": "2018-09-27T12:00:00"  
      }  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Centro"  
  },  
  "serviceStatus": {  
    "type": "Text",  
    "value": "onRoute"  
  },  
  "cargoWeight": {  
    "type": "Number",  
    "value": 314  
  },  
  "speed": {  
    "type": "Number",  
    "value": 50,  
    "metadata": {  
      "timestamp": {  
        "type": "DateTime",  
        "value": "2018-09-27T12:00:00"  
      }  
    }  
  },  
  "serviceProvided": {  
    "type": "StructuredValue",  
    "value": [  
      "garbageCollection",  
      "wasteContainerCleaning"  
    ]  
  },  
  "bearing": {  
    "type": "Number",  
    "value": 43  
  },  
  "fuelEfficiency": {  
    "type": "Number",  
    "value": 13  
  },  
  "fuelType": {  
    "type": "Text",  
    "value": "Petrol"  
  },  
  "fuelFilled": {  
    "type": "Number",  
    "value": 6  
  },  
  "tripNetWeightCollected": {  
    "type": "Number",  
    "value": 12  
  },  
  "vehicleTrackerDevice": {  
    "type": "Text",  
    "value": "Installed"  
  },  
  "wardId": {  
    "type": "Text",  
    "value": "4"  
  },  
  "license_plate": {  
    "type": "Text",  
    "value": "KA052134"  
  },  
  "currentTripCount": {  
    "type": "Boolean",  
    "value": true  
  },  
  "reportId": {  
    "type": "Text",  
    "value": "21645"  
  },  
  "zoneName": {  
    "type": "Text",  
    "value": "South Zone"  
  },  
  "vehicleAltitude": {  
    "type": "Text",  
    "value": "600"  
  },  
  "deviceSimNumber": {  
    "type": "Text",  
    "value": "9942142573"  
  },  
  "wardName": {  
    "type": "Text",  
    "value": "Kempegowda Ward"  
  },  
  "deviceBatteryStatus": {  
    "type": "Text",  
    "value": "connected"  
  },  
  "ignitionStatus": {  
    "type": "Boolean",  
    "value": true  
  },  
  "vehicleRunningStatus": {  
    "type": "Text",  
    "value": "running"  
  },  
  "observationDateTime": {  
    "type": "DateTime",  
    "value": "2021-03-11T15:51:02+05:30"  
  },  
  "serviceOnDuty": {  
    "type": "Boolean",  
    "value": false  
  },  
  "emergencyVehicleType": {  
    "type": "Text",  
    "value": "ambulance"  
  },  
  "municipalityInfo": {  
    "type": "StructuredValue",  
    "value": {  
      "district": "Bangalore Urban",  
      "ulbName": "BMC",  
      "cityId": "23",  
      "wardId": "23",  
      "stateName": "Karnataka",  
      "cityName": "Bangalore",  
      "zoneName": "South",  
      "wardName": "Bangalore Urban",  
      "zoneId": "2",  
      "wardNum": 4  
    }  
  }  
}  
```  
</details>  

#### 车辆NGSI-LD键值示例  

这是一个JSON-LD格式的车辆示例，以键值对的形式呈现。当使用`options=keyValues`时，它与NGSI-LD兼容，并返回个体实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    

```json  

{  
  "id": "urn:ngsi-ld:Vehicle:vehicle:WasteManagement:1",  
  "type": "Vehicle",  
  "areaServed": "Centro",  
  "battery": 0.81,  
  "bearing": 43,  
  "cargoWeight": 314,  
  "category": [  
    "municipalServices"  
  ],  
  "currentTripCount": 1,  
  "deviceBatteryStatus": "connected",  
  "deviceSimNumber": "9942142573",  
  "emergencyVehicleType": "ambulance",  
  "fuelEfficiency": 13,  
  "fuelFilled": 6,  
  "fuelType": "Petrol",  
  "ignitionStatus": true,  
  "license_plate": "KA052134",  
  "location": {  
    "coordinates": [  
      -3.164485591715449,  
      40.62785133667262  
    ],  
    "type": "Point"  
  },  
  "municipalityInfo": {  
    "district": "Bangalore Urban",  
    "ulbName": "BMC",  
    "cityId": "23",  
    "wardId": "23",  
    "stateName": "Karnataka",  
    "cityName": "Bangalore",  
    "zoneName": "South",  
    "wardName": "Bangalore Urban",  
    "zoneId": "2",  
    "wardNum": 4  
  },  
  "name": "C Recogida 1",  
  "observationDateTime": "2021-03-11T15:51:02+05:30",  
  "refVehicleModel": "urn:ngsi-ld:VehicleModel:vehiclemodel:econic",  
  "reportId": "21645",  
  "serviceOnDuty": false,  
  "serviceProvided": [  
    "garbageCollection",  
    "wasteContainerCleaning"  
  ],  
  "serviceStatus": "onRoute",  
  "speed": 50,  
  "tripNetWeightCollected": 12,  
  "vehicleAltitude": "600",  
  "vehiclePlateIdentifier": "3456ABC",  
  "vehicleRunningStatus": "running",  
  "vehicleTrackerDevice": "Installed",  
  "vehicleType": "lorry",  
  "wardId": "4",  
  "wardName": "Kempegowda Ward",  
  "zoneName": "South Zone",  
  "@context": [  
    "https://smart-data-models.github.io/dataModel.Transportation/context.jsonld"  
  ]  
}  
```  
</details>  

#### 车辆NGSI-LD标准化示例  

这是一个以JSON-LD格式标准化的车辆示例。当不使用选项时，它与NGSI-LD兼容，并返回个体实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    

```json  

{  
  "id": "urn:ngsi-ld:Vehicle:vehicle:WasteManagement:1",  
  "type": "Vehicle",  
  "areaServed": {  
    "type": "Property",  
    "value": "Centro"  
  },  
  "battery": {  
    "type": "Property",  
    "value": 0.81,  
    "observedAt": "2021-03-11T15:51:02+05:30"  
  },  
  "bearing": {  
    "type": "Property",  
    "value": 43  
  },  
  "cargoWeight": {  
    "type": "Property",  
    "value": 314  
  },  
  "category": {  
    "type": "Property",  
    "value": [  
      "municipalServices"  
    ]  
  },  
  "currentTripCount": {  
    "type": "Property",  
    "value": 1  
  },  
  "deviceBatteryStatus": {  
    "type": "Property",  
    "value": "Connected"  
  },  
  "deviceSimNumber": {  
    "type": "Property",  
    "value": "9942142573"  
  },  
  "emergencyVehicleType": {  
    "type": "Property",  
    "value": "ambulance"  
  },  
  "fuelEfficiency": {  
    "type": "Property",  
    "value": 13  
  },  
  "fuelFilled": {  
    "type": "Property",  
    "value": 6  
  },  
  "fuelType": {  
    "type": "Property",  
    "value": "Petrol"  
  },  
  "ignitionStatus": {  
    "type": "Property",  
    "value": true  
  },  
  "license_plate": {  
    "type": "Property",  
    "value": "KA052134"  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -3.164485591715449,  
        40.62785133667262  
      ]  
    },  
    "observedAt": "2018-09-27T12:00:00Z"  
  },  
  "municipalityInfo": {  
    "type": "Property",  
    "value": {  
      "district": "Bangalore Urban",  
      "ulbName": "BMC",  
      "cityId": "23",  
      "wardId": "23",  
      "stateName": "Karnataka",  
      "cityName": "Bangalore",  
      "zoneName": "South",  
      "wardName": "Bangalore Urban",  
      "zoneId": "2",  
      "wardNum": 4  
    }  
  },  
  "name": {  
    "type": "Property",  
    "value": "C Recogida 1"  
  },  
  "observationDateTime": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2021-03-11T15:51:02+05:30"  
    }  
  },  
  "refVehicleModel": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:VehicleModel:vehiclemodel:econic"  
  },  
  "reportId": {  
    "type": "Property",  
    "value": "21645"  
  },  
  "serviceOnDuty": {  
    "type": "Property",  
    "value": false  
  },  
  "serviceProvided": {  
    "type": "Property",  
    "value": [  
      "garbageCollection",  
      "wasteContainerCleaning"  
    ]  
  },  
  "serviceStatus": {  
    "type": "Property",  
    "value": "onRoute"  
  },  
  "speed": {  
    "type": "Property",  
    "value": 50,  
    "observedAt": "2018-09-27T12:00:00Z"  
  },  
  "tripNetWeightCollected": {  
    "type": "Property",  
    "value": 12  
  },  
  "vehicleAltitude": {  
    "type": "Property",  
    "value": 600  
  },  
  "vehiclePlateIdentifier": {  
    "type": "Property",  
    "value": "3456ABC"  
  },  
  "vehicleRunningStatus": {  
    "type": "Property",  
    "value": "running"  
  },  
  "vehicleTrackerDevice": {  
    "type": "Property",  
    "value": "Installed"  
  },  
  "vehicleType": {  
    "type": "Property",  
    "value": "lorry"  
  },  
  "wardId": {  
    "type": "Property",  
    "value": "4"  
  },  
  "wardName": {  
    "type": "Property",  
    "value": "Kempegowda Ward"  
  },  
  "zoneName": {  
    "type": "Property",  
    "value": "South Zone"  
  },  
  "@context": [  
    "https://smart-data-models.github.io/dataModel.Transportation/context.jsonld"  
  ]  
}  
```  
</details><!-- /80-Examples -->
  
<!-- 90-FooterNotes -->
  
<!-- /90-FooterNotes -->
  
<!-- 95-Units -->
  

See [FAQ 10](https://smartdatamodels.org/index.php/faqs/) to get an answer on how to deal with magnitude units  
<!-- /95-Units -->
  
<!-- 97-LastFooter -->
  
---  

[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->
  
