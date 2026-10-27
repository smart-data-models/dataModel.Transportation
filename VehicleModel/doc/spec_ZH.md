<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：VehicleModel  
===============<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models/dataModel.Transportation/blob/master/VehicleModel/LICENSE.md)  
[自动生成的文档](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全局描述：**此实体建模特定的车辆型号，包括属于该型号的多个车辆实例共有的所有属性。**  
version: 0.0.3  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 属性列表  

<sup><sub>[*] 如果属性中没有类型，则可能是因为它有多种类型或不同的格式/模式</sub></sup>  
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国家。例如，西班牙  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 街道地址所在的城镇，该城镇位于该区域内  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 城镇所在的区域，该区域位于该国家内  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 区是一种行政区划类型，在某些国家由地方政府管理    
	- `postOfficeBoxNumber[string]`: 邮政信箱地址的邮政信箱号码。例如，03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 邮政编码。例如，24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 街道地址  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 标识公共街道上特定属性的编号    
- `alternateName[string]`: 此项目的替代名称  - `annotations[array]`: 关于该项目的注释  . Model: [https://schema.org/Text](https://schema.org/Text)- `areaServed[string]`: 提供服务或商品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `brandName[string]`: 车辆品牌名称  . Model: [https://schema.org/brand](https://schema.org/brand)- `cargoVolume[number]`: 可用于货物或行李的可用容积。对于汽车，这通常指行李箱容积。如果只提供一个值（类型为 Number），则表示最大容积。  . Model: [https://schema.org/cargoVolume](https://schema.org/cargoVolume)- `color[string]`: 产品的颜色  . Model: [https://schema.org/color](https://schema.org/color)- `dataProvider[string]`: 标识协调数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。这通常由存储平台分配。  - `dateModified[date-time]`: 实体上次修改的时间戳。这通常由存储平台分配  - `depth[number]`: 车辆深度  . Model: [https://schema.org/depth](https://schema.org/depth)- `description[string]`: 此项目的描述  - `fuelConsumption[number]`: 给定车辆行驶特定距离或持续时间所消耗的燃料或能量量。对于内燃机，以每 100 公里升数表示；对于电动汽车（燃料类型为电动），以每 100 公里千瓦时表示。  . Model: [https://schema.org/fuelConsumption](https://schema.org/fuelConsumption)- `fuelType[string]`: 适用于车辆发动机的燃料类型。枚举值：'autogas, biodiesel, cng, diesel, electric, ethanol, gasoline, hybrid_electric_diesel, hybrid_electric_petrol, hydrogen, lpg, petrol, petrol(unleaded), petrol(leaded), other'  . Model: [https://schema.org/fuelType](https://schema.org/fuelType)- `height[number]`: 车辆高度  . Model: [https://schema.org/height](https://schema.org/height)- `id[*]`: 实体的唯一标识符  - `image[uri]`: 该项目的图片  . Model: [https://schema.org/URL](https://schema.org/URL)- `location[*]`: 项目的 Geojson 引用。它可以是 Point、LineString、Polygon、MultiPoint、MultiLineString 或 MultiPolygon  - `manufacturerName[string]`: 车辆制造商名称  . Model: [https://schema.org/Text](https://schema.org/Text)- `modelName[string]`: 车辆型号名称  . Model: [https://schema.org/model](https://schema.org/model)- `name[string]`: 此项目的名称  - `owner[array]`: 一个包含 JSON 编码字符序列的列表，该序列引用所有者（一个或多个）的唯一 ID  - `seeAlso[*]`: 指向有关该项目的其他资源的 URI 列表。  - `source[string]`: 以 URL 形式提供实体数据原始来源的字符序列。建议使用来源提供者的完全限定域名，或指向来源对象的 URL  - `tractionBatteryCapacity[number]`: 完全或部分由电力驱动的车辆（纯电动、插电式混合动力或混合动力汽车）的牵引电池可用能量容量。例如，可以结合油耗估算续航里程。  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: NGSI 实体类型。必须是 VehicleModel。  - `url[uri]`: 提供此车辆型号描述的 URL  . Model: [https://schema.org/URL](https://schema.org/URL)- `vehicleEngine[string]`: 车辆发动机信息  . Model: [https://schema.org/vehicleEngine](https://schema.org/vehicleEngine)- `vehicleModelDate[date-time]`: 车辆型号的发布日期（通常用于区分同一品牌和型号的不同版本）  . Model: [https://schema.org/vehicleModelDate](https://schema.org/vehicleModelDate)- `vehicleType[string]`: 从结构特征角度划分的车辆类型。这与车辆类别不同。枚举值：'agriculturalVehicle, anyVehicle, articulatedVehicle, bicycle, binTrolley, bus, car, caravan, carOrLightVehicle, carWithCaravan, carWithTrailer, cleaningTrolley, constructionOrMaintenanceVehicle, fourWheelDrive, highSidedVehicle, lorry, minibus, moped, motorcycle, motorcycleWithSideCar, motorscooter, sweepingMachine, tanker, threeWheeledVehicle, trailer, tram, twoWheeledVehicle, trolley, van, vehicleWithoutCatalyticConverter, vehicleWithCaravan, vehicleWithTrailer, withEvenNumberedRegistrationPlates, withOddNumberedRegistrationPlates, other'。以下值由 _VehicleTypeEnum_ 和 _VehicleTypeEnum2_ 定义，[DATEX 2 版本 2.3](http://d2docs.ndwcloud.nu/_static/umlmodel/v2.3/index.htm)  . Model: [https://schema.org/Text](https://schema.org/Text)- `weight[number]`: 车辆重量  . Model: [https://schema.org/weight](https://schema.org/weight)- `width[number]`: 车辆宽度  . Model: [https://schema.org/width](https://schema.org/width)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必填属性  
- `brandName`  - `id`  - `manufacturerName`  - `modelName`  - `name`  - `type`  - `vehicleType`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## 属性的数据模型描述  
按字母顺序排序（点击查看详情）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
VehicleModel:    
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
        description: Eventy element in the annotations    
        type: string    
        x-ngsi:    
          type: Property    
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
    brandName:    
      description: Vehicle's brand name    
      type: string    
      x-ngsi:    
        model: https://schema.org/brand    
        type: Property    
    cargoVolume:    
      description: The available volume for cargo or luggage. For automobiles, this is usually the trunk volume. If only a single value is provided (type Number) it will refer to the maximum volume    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/cargoVolume    
        type: Property    
        units: Liters    
    color:    
      description: The color of the product    
      type: string    
      x-ngsi:    
        model: https://schema.org/color    
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
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    depth:    
      description: Vehicle's depth    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/depth    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    fuelConsumption:    
      description: The amount of fuel or energy consumed for traveling a particular distance or temporal duration with the given vehicle. For combustion engines it is expressed in liters per 100 km, for electric vehicles (fuelType electric) in kilowatt hours per 100 km    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/fuelConsumption    
        type: Property    
        units: liters per 100 kilometer or kilowatt hour per 100 kilometer    
    fuelType:    
      description: The type of fuel suitable for the engine or engines of the vehicle. Enum:'autogas, biodiesel, cng, diesel, electric, ethanol, gasoline, hybrid_electric_diesel, hybrid_electric_petrol, hydrogen, lpg, petrol, petrol(unleaded), petrol(leaded), other'    
      enum:    
        - autogas    
        - biodiesel    
        - cng    
        - diesel    
        - electric    
        - ethanol    
        - gasoline    
        - hybrid_electric_diesel    
        - hybrid_electric_petrol    
        - hydrogen    
        - lpg    
        - petrol    
        - petrol(unleaded)    
        - petrol(leaded)    
        - other    
      type: string    
      x-ngsi:    
        model: https://schema.org/fuelType    
        type: Property    
    height:    
      description: Vehicle's height    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/height    
        type: Property    
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
    image:    
      description: An image of the item    
      format: uri    
      type: string    
      x-ngsi:    
        model: https://schema.org/URL    
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
    manufacturerName:    
      description: Vehicle's manufacturer name    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    modelName:    
      description: Vehicle's model name    
      type: string    
      x-ngsi:    
        model: https://schema.org/model    
        type: Property    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
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
    source:    
      description: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object    
      type: string    
      x-ngsi:    
        type: Property    
    tractionBatteryCapacity:    
      description: Usable energy capacity of the traction battery of vehicles fully or partly powered by electricity (battery electric, plug-in hybrid or hybrid vehicles). Allows, for instance, estimating the driving range together with fuelConsumption    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: kilowatt hour    
    type:    
      description: NGSI Entity type. It has to be VehicleModel    
      enum:    
        - VehicleModel    
      type: string    
      x-ngsi:    
        type: Property    
    url:    
      description: URL which provides a description of this vehicle model    
      format: uri    
      type: string    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Property    
    vehicleEngine:    
      description: Information about the engine or engines of the vehicle    
      type: string    
      x-ngsi:    
        model: https://schema.org/vehicleEngine    
        type: Property    
    vehicleModelDate:    
      description: The release date of a vehicle model (often used to differentiate versions of the same make and model)    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/vehicleModelDate    
        type: Property    
    vehicleType:    
      description: Type of vehicle from the point of view of its structural characteristics. This is different than the vehicle category . Enum:'agriculturalVehicle, anyVehicle, articulatedVehicle, bicycle, binTrolley, bus, car, caravan, carOrLightVehicle, carWithCaravan, carWithTrailer, cleaningTrolley, constructionOrMaintenanceVehicle, fourWheelDrive, highSidedVehicle, lorry, minibus, moped, motorcycle, motorcycleWithSideCar, motorscooter, sweepingMachine, tanker, threeWheeledVehicle, trailer, tram, twoWheeledVehicle, trolley, van, vehicleWithoutCatalyticConverter, vehicleWithCaravan, vehicleWithTrailer, withEvenNumberedRegistrationPlates, withOddNumberedRegistrationPlates, other'. The following values defined by _VehicleTypeEnum_ and _VehicleTypeEnum2_, [DATEX 2 version 2.3](http://d2docs.ndwcloud.nu/_static/umlmodel/v2.3/index.htm)    
      enum:    
        - agriculturalVehicle    
        - bicycle    
        - binTrolley    
        - bus    
        - car    
        - caravan    
        - carWithCaravan    
        - carWithTrailer    
        - cleaningTrolley    
        - constructionOrMaintenanceVehicle    
        - lorry    
        - minibus    
        - moped    
        - motorcycle    
        - motorcycleWithSideCar    
        - motorscooter    
        - sweepingMachine    
        - tanker    
        - trailer    
        - tram    
        - van    
        - trolley    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    weight:    
      description: Vehicle's weight    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/weight    
        type: Property    
    width:    
      description: Vehicle's width    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/width    
        type: Property    
  required:    
    - id    
    - name    
    - type    
    - vehicleType    
    - brandName    
    - modelName    
    - manufacturerName    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program    
  x-license-url: https://github.com/smart-data-models/dataModel.Transportation/blob/master/VehicleModel/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Transportation/VehicleModel/schema.json    
  x-model-tags: ''    
  x-version: 0.0.3    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 示例载荷    
#### VehicleModel NGSI-v2 键值对示例  
这是键值对形式的 JSON-LD 格式的 VehicleModel 示例。当使用 `options=keyValues` 时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "vehiclemodel:buzz",  
  "type": "VehicleModel",  
  "name": "VW-IDBuzz",  
  "brandName": "Volkswagen",  
  "modelName": "ID. Buzz",  
  "manufacturerName": "Volkswagen",  
  "vehicleType": "car",  
  "fuelType": "electric",  
  "fuelConsumption": 20.7,  
  "tractionBatteryCapacity": 79  
}  
```  
</details>  
#### VehicleModel NGSI-v2 规范化示例  
这是规范化后的 JSON-LD 格式的 VehicleModel 示例。当不使用 `options` 时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "vehiclemodel:buzz",  
  "type": "VehicleModel",  
  "name": {  
    "type": "Text",  
    "value": "VW-IDBuzz"  
  },  
  "brandName": {  
    "type": "Text",  
    "value": "Volkswagen"  
  },  
  "modelName": {  
    "type": "Text",  
    "value": "ID. Buzz"  
  },  
  "manufacturerName": {  
    "type": "Text",  
    "value": "Volkswagen"  
  },  
  "vehicleType": {  
    "type": "Text",  
    "value": "car"  
  },  
  "fuelType": {  
    "type": "Text",  
    "value": "electric"  
  },  
  "fuelConsumption": {  
    "type": "Number",  
    "value": 20.7  
  },  
  "tractionBatteryCapacity": {  
    "type": "Number",  
    "value": 79  
  }  
}  
```  
</details>  
#### VehicleModel NGSI-LD 键值对示例  
这是键值对形式的 JSON-LD 格式的 VehicleModel 示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:VehicleModel:vehiclemodel:buzz",  
  "type": "VehicleModel",  
  "name": "VW-IDBuzz",  
  "brandName": "Volkswagen",  
  "modelName": "ID. Buzz",  
  "manufacturerName": "Volkswagen",  
  "vehicleType": "car",  
  "fuelType": "electric",  
  "fuelConsumption": 20.7,  
  "tractionBatteryCapacity": 79,  
  "@context": [  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Transportation/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### VehicleModel NGSI-LD 规范化示例  
这是规范化后的 JSON-LD 格式的 VehicleModel 示例。当不使用 `options` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:VehicleModel:vehiclemodel:buzz",  
    "type": "VehicleModel",  
    "name": {  
        "type": "Property",  
        "value": "VW-IDBuzz"  
    },  
    "brandName": {  
        "type": "Property",  
        "value": "Volkswagen"  
    },  
    "modelName": {  
        "type": "Property",  
        "value": "ID. Buzz"  
    },  
    "manufacturerName": {  
        "type": "Property",  
        "value": "Volkswagen"  
    },  
    "vehicleType": {  
        "type": "Property",  
        "value": "car"  
    },  
    "fuelType": {  
        "type": "Property",  
        "value": "electric"  
    },  
    "fuelConsumption": {  
        "type": "Property",  
        "value": 20.7  
    },  
    "tractionBatteryCapacity": {  
        "type": "Property",  
        "value": 79  
    },  
    "@context": [  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Transportation/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
请参阅 [常见问题 10](https://smartdatamodels.org/index.php/faqs/)，了解如何处理数量单位的答案  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
