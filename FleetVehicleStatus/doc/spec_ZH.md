<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体。车队车辆状态  
=========<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.Transportation/blob/master/FleetVehicleStatus/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全局描述。**该实体包含对通用车队车辆状态的统一描述。该实体主要与运输和物流的垂直领域相关，但也可用于许多其他相关的物联网应用。  
版本：0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

##属性列表  

<sup><sub>[*] 如果一个属性中没有一个类型，是因为它可能有几种类型或不同的格式/模式</sub></sup>。  
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: 这个项目的一个替代名称  - `areaServed[string]`: 提供服务或提供项目的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `bearing[number]`: 车队车辆的当前方位，以相对于北方的度数表示。该属性的时间戳元素应表明获得该读数的时间。  - `currentOperative[object]`: 描述为Schema.org人的车辆的当前操作人员（如司机）。  . Model: [https://schema.org/Person](https://schema.org/Person)- `currentStatus[string]`: 对车辆当前状态的描述，例如，枚举："已部署、已完成、已终止、已服务、已开始  - `dataProvider[string]`: 一串识别统一数据实体提供者的字符。  - `dateCreated[string]`: 实体创建时间戳。这通常会由存储平台分配。  - `dateModified[string]`: 实体最后一次修改的时间戳。这通常会由存储平台分配。  - `description[string]`: 对这个项目的描述  - `fleetVehicle[*]`: 对该状态实体相关的FleetVehicle实体的引用。  - `fleetVehicleOperation[*]`: 对该状态实体相关的FleetVehicleOperation实体的引用。  - `id[*]`: 实体的唯一标识符  - `inRestrictedArea[boolean]`: 表示在状态更新时，车辆是否已知处于限制区域。  - `lastFuellingAmount[number]`: 在最后一次加油时添加到车辆的燃料水平。该属性的时间戳元素应表明车辆何时加过油。要记录的数据单位是升  - `lastKnownPosition[*]`: 对该项目的Geojson引用。它可以是点、线字符串、多边形、多点、多线字符串或多多边形。  - `lastKnownPositionUpdatedAt[string]`: 车队车辆的最后一次已知位置更新的时间戳。  - `location[*]`: 对该项目的Geojson引用。它可以是点、线字符串、多边形、多点、多线字符串或多多边形。  - `mileageFromOdometer[number]`: 根据车载里程表，车队车辆行驶的总距离，单位是公里（单位代码KMT）或英里（单位代码SMI）。参见Schema.org Vehicle/ mileageFromOdometer。时间戳元素记录里程表读数的时间。  - `name[string]`: 这个项目的名称。  - `owner[array]`: 一个包含JSON编码的字符序列的列表，引用所有者的唯一Ids。  - `restFuelAmount[number]`: 车辆最后一次休息（即停车）时记录的燃料水平。该属性的时间戳元素应表明车辆最后一次休息的时间。要记录的数据单位是升。  - `seeAlso[*]`: 指向有关该项目的其他资源的URI列表  - `source[string]`: 提供实体数据原始来源的一连串字符，作为一个URL。建议为源提供者的完全合格域名，或源对象的URL。  - `speed[number]`: 车队车辆的当前速度（公里/小时）。该属性的时间戳元素应表明何时获得该读数  - `type[string]`: NGSI实体标识符。它必须是FleetVehicleStatus。  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
这个数据模型来自原始项目GSMA物联网项目，https://www.gsma.com/iot/iot-big-data/。有一些小的调整，以满足智能数据模型的要求。  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 数据模型的属性描述  
按字母顺序排列（点击查看详情）。  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
FleetVehicleStatus:    
  description: 'This entity contains a harmonised description of the status of a generic fleet vehicle. This entity is primarily associated with the vertical segment of the transport and logistics but may also be used many other related IoT applications.'    
  properties:    
    address:    
      description: 'The mailing address'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/addressCountry'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/addressLocality'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/addressRegion'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    bearing:    
      description: 'The current bearing of the fleet vehicle in degrees relative to North. The timestamp element of the attribute should indicate when the reading was obtained.'    
      type: number    
      x-ngsi:    
        type: Property    
    currentOperative:    
      description: 'The current operative (e.g. driver) of the vehicle described as a Schema.org  person'    
      properties:    
        givenName:    
          type: string    
        jobTitle:    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/Person    
        type: Property    
    currentStatus:    
      description: 'A description of the current status of the vehicle e.g. Enum:''deployed, finished, terminated, servicing, starting'''    
      enum:    
        - deployed    
        - finished    
        - servicing    
        - starting    
        - terminated    
      type: string    
      x-ngsi:    
        type: Property    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    fleetVehicle:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Reference to the FleetVehicle entity to which this status entity relates.'    
      x-ngsi:    
        type: Relationship    
    fleetVehicleOperation:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Reference to the FleetVehicleOperation entity to which this status entity relates.'    
      x-ngsi:    
        type: Relationship    
    id:    
      anyOf: &fleetvehiclestatus_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      x-ngsi:    
        type: Property    
    inRestrictedArea:    
      description: 'Indicates if the vehicle is known to be in a restricted area at the time of the status update.'    
      type: boolean    
      x-ngsi:    
        type: Property    
    lastFuellingAmount:    
      description: 'The level of fuel added to the vehicle at the last fuelling. The timestamp element of the attribute should indicate when the vehicle was fuelled. Data to be recorded in Litres'    
      type: number    
      x-ngsi:    
        type: Property    
        units: litres    
    lastKnownPosition:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf: &fleetvehiclestatus_-_properties_-_location_-_oneof    
        - description: 'GeoProperty. Geojson reference to the item. Point'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                type: number    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - Point    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Point'    
          type: object    
        - description: 'GeoProperty. Geojson reference to the item. LineString'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - LineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON LineString'    
          type: object    
        - description: 'GeoProperty. Geojson reference to the item. Polygon'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
            type:    
              enum:    
                - Polygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Polygon'    
          type: object    
        - description: 'GeoProperty. Geojson reference to the item. MultiPoint'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPoint    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPoint'    
          type: object    
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiLineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiLineString'    
          type: object    
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
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
            type:    
              enum:    
                - MultiPolygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPolygon'    
          type: object    
      x-ngsi:    
        type: GeoProperty    
    lastKnownPositionUpdatedAt:    
      description: 'The timestamp of the last known position update for the fleet vehicle.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf: *fleetvehiclestatus_-_properties_-_location_-_oneof    
      x-ngsi:    
        type: GeoProperty    
    mileageFromOdometer:    
      description: 'The total distance the fleet vehicle has travelled according to the on-board odometer in kilometres (unitCode KMT) or miles (unitCode SMI). See also Schema.org Vehicle/ mileageFromOdometer. The timestamp element records when the odometer reading was taken.'    
      type: number    
      x-ngsi:    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *fleetvehiclestatus_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    restFuelAmount:    
      description: 'The level of fuel recorded when the vehicle was last at rest (i.e. stopped). The timestamp element of the attribute should indicate when the vehicle was last at rest. Data to be recorded in Litres.'    
      type: number    
      x-ngsi:    
        type: Property    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    speed:    
      description: 'The current speed of the fleet vehicle (km/h). The timestamp element of the attribute should indicate when the reading was obtained'    
      type: number    
      x-ngsi:    
        type: Property    
        units: km/h    
    type:    
      description: 'NGSI Entity identifier. It has to be FleetVehicleStatus'    
      enum:    
        - FleetVehicleStatus    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Transportation/blob/master/FleetVehicleStatus/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Transportation/FleetVehicleStatus/schema.json    
  x-model-tags: GSMA    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ＃＃＃＃有效载荷的例子  
#### FleetVehicleStatus NGSI-v2 关键值示例  
下面是一个JSON-LD格式的FleetVehicleStatus的例子，作为关键值。当使用`options=keyValues`时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:FleetVehicleStatus:16ea1c5c-5aa6-11e8-8144-4b82063ca31c",  
  "type": "FleetVehicleStatus",  
  "source": "https://source.example.com",  
  "dataProvider": "https://provider.example.com",  
  "fleetVehicle": "urn:ngsi-ld:FleetVehicle:84c6a3a8-5aa6-11e8-bedc-27e105edd16f",  
  "fleetVehicleOperation": "urn:ngsi-ld:FleetVehicleOperation:a4f0a07a-5aa6-11e8-b70f-4b9d36e53d7b",  
  "restFuelAmount": 28,  
  "lastFuellingAmount": 95,  
  "currentStatus": "finished",  
  "currentOperative": {  
    "givenName": "John Smith",  
    "jobTitle": "Ambulance Operator"  
  },  
  "speed": 60,  
  "unitCode": "KMH",  
  "bearing": 80,  
  "lastKnownPosition": {  
    "type": "Point",  
    "coordinates": [  
      -104.99404,  
      39.75621  
    ]  
  },  
  "lastKnownPositionUpdatedAt": "2016-08-28T10:18:16Z",  
  "inRestrictedArea": true,  
  "mileageFromOdometer": 18756  
}  
```  
</details>  
#### FleetVehicleStatus NGSI-v2规范化示例  
下面是一个JSON-LD格式的FleetVehicleStatus规范化的例子。当不使用选项时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:FleetVehicleStatus:16ea1c5c-5aa6-11e8-8144-4b82063ca31c",  
  "type": "FleetVehicleStatus",  
  "source": {  
    "type": "URL",  
    "value": "https://source.example.com"  
  },  
  "dataProvider": {  
    "type": "URL",  
    "value": "https://provider.example.com"  
  },  
  "fleetVehicle": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:FleetVehicle:84c6a3a8-5aa6-11e8-bedc-27e105edd16f"  
  },  
  "fleetVehicleOperation": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:FleetVehicleOperation:a4f0a07a-5aa6-11e8-b70f-4b9d36e53d7b"  
  },  
  "restFuelAmount": {  
    "type": "Number",  
    "value": 28  
  },  
  "lastFuellingAmount": {  
    "type": "Number",  
    "value": 95  
  },  
  "currentStatus": {  
    "type": "Text",  
    "value": "finished"  
  },  
  "currentOperative": {  
    "type": "StructuredValue",  
    "value": {  
      "givenName": "John Smith",  
      "jobTitle": "Ambulance Operator"  
    }  
  },  
  "speed": {  
    "type": "Number",  
    "value": 60  
  },  
  "bearing": {  
    "type": "Number",  
    "value": 80  
  },  
  "lastKnownPosition": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -104.99404,  
        39.75621  
      ]  
    }  
  },  
  "lastKnownPositionUpdatedAt": {  
    "type": "DateTime",  
    "value": "2016-08-28T10:18:16Z"  
  },  
  "inRestrictedArea": {  
    "type": "Boolean",  
    "value": true  
  },  
  "mileageFromOdometer": {  
    "type": "Number",  
    "value": 18756  
  }  
}  
```  
</details>  
#### FleetVehicleStatus NGSI-LD关键值示例  
这里是一个JSON-LD格式的FleetVehicleStatus的例子，作为关键值。当使用`options=keyValues`时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:FleetVehicleStatus:16ea1c5c-5aa6-11e8-8144-4b82063ca31c",  
    "type": "FleetVehicleStatus",  
    "bearing": 80,  
    "currentOperative": {  
        "givenName": "John Smith",  
        "jobTitle": "Ambulance Operator"  
    },  
    "currentStatus": "finished",  
    "dataProvider": "https://provider.example.com",  
    "fleetVehicle": "urn:ngsi-ld:FleetVehicle:84c6a3a8-5aa6-11e8-bedc-27e105edd16f",  
    "fleetVehicleOperation": "urn:ngsi-ld:FleetVehicleOperation:a4f0a07a-5aa6-11e8-b70f-4b9d36e53d7b",  
    "inRestrictedArea": true,  
    "lastFuellingAmount": 95,  
    "lastKnownPosition": {  
        "type": "Point",  
        "coordinates": [  
            -104.99404,  
            39.75621  
        ]  
    },  
    "lastKnownPositionUpdatedAt": "2016-08-28T10:18:16Z",  
    "mileageFromOdometer": 18756,  
    "restFuelAmount": 28,  
    "source": "https://source.example.com",  
    "speed": 60,  
    "unitCode": "KMH",  
    "@context": [  
        "https://smart-data-models.github.io/dataModel.Transportation/FleetVehicleStatus/context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Transportation/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### FleetVehicleStatus NGSI-LD规范化示例  
下面是一个JSON-LD格式的FleetVehicleStatus规范化的例子。当不使用选项时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:FleetVehicleStatus:16ea1c5c-5aa6-11e8-8144-4b82063ca31c",  
    "type": "FleetVehicleStatus",  
    "bearing": {  
        "type": "Property",  
        "value": 80,  
        "unitCode": "DD",  
        "observedAt": "2016-08-22T10:18:16Z"  
    },  
    "currentOperative": {  
        "type": "Property",  
        "value": {  
            "givenName": "John Smith",  
            "jobTitle": "Ambulance Operator",  
            "@type": "https://schema.org/Person"  
        }  
    },  
    "currentStatus": {  
        "type": "Property",  
        "value": "finished"  
    },  
    "dataProvider": {  
        "type": "Property",  
        "value": "https://provider.example.com"  
    },  
    "fleetVehicle": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:FleetVehicle:84c6a3a8-5aa6-11e8-bedc-27e105edd16f"  
    },  
    "fleetVehicleOperation": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:FleetVehicleOperation:a4f0a07a-5aa6-11e8-b70f-4b9d36e53d7b"  
    },  
    "inRestrictedArea": {  
        "type": "Property",  
        "value": true  
    },  
    "lastFuellingAmount": {  
        "type": "Property",  
        "value": 95,  
        "unitCode": "LTR",  
        "observedAt": "2016-08-22T10:18:16Z"  
    },  
    "lastKnownPosition": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                -104.99404,  
                39.75621  
            ]  
        }  
    },  
    "lastKnownPositionUpdatedAt": {  
        "type": "Property",  
        "value": "2016-08-28T10:18:16Z"  
    },  
    "mileageFromOdometer": {  
        "type": "Property",  
        "value": 18756,  
        "unitCode": "SMI",  
        "observedAt": "2016-08-22T10:18:16Z"  
    },  
    "restFuelAmount": {  
        "type": "Property",  
        "value": 28,  
        "unitCode": "LTR",  
        "observedAt": "2016-08-22T10:18:16Z"  
    },  
    "source": {  
        "type": "Property",  
        "value": "https://source.example.com"  
    },  
    "speed": {  
        "type": "Property",  
        "value": 60,  
        "unitCode": "KMH",  
        "observedAt": "2016-08-22T10:18:16Z"  
    },  
    "@context": [  
        "https://smart-data-models.github.io/dataModel.Transportation/FleetVehicleStatus/context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Transportation/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
参见[常见问题10](https://smartdatamodels.org/index.php/faqs/)，以获得关于如何处理量级单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
