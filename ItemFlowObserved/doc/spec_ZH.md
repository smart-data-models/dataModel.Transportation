<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体。项目流程观察（ItemFlowObserved  
==========================<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.Transportation/blob/master/ItemFlowObserved/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全局描述。**该数据模型旨在测量与某一地点和某一时期的物品移动有关的观察。这个数据模型提出了两个数据模型的演变，通过合并它们并整合[TrafficFlowObserved]和[CrowFlowObserved]的初始版本的所有属性，并延伸到我们想要分析运动的任何类型的项目。属性 "vehicleType "和 "vehicleSubType "被从初始数据模型中删除，以便成为可能值的通用 "itemType "和 "itemSubType"。(人、车辆类型、船只类型、飞机类型......)**。  
版本。  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

##属性列表  

<sup><sub>[*] 如果一个属性中没有一个类型，是因为它可能有几种类型或不同的格式/模式</sub></sup>。  
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: 这个项目的一个替代名称  - `areaServed[string]`: 提供服务或提供项目的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `averageGapDistance[number]`: 连续2个检测项目之间的平均间隙距离。单位代码（文本）使用[UN/CEFACT通用代码]（http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes）给出。例如，**MTR**代表米。  - `averageHeadwayTime[number]`: 平均头程时间。走头时间是指两个连续项目之间所经过的时间。单位代码（文本）使用[UN/CEFACT通用代码]（http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes）给出。例如，**SEC**代表秒。  - `averageLength[number]`: 观测期间检测到的过境物品的平均长度。单位代码（文本）使用[UN/CEFACT通用代码]（http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes）给出。例如，**MTR**代表米。  - `averageSpeed[number]`: 观测期间检测到的物品过境的平均速度。单位代码（文本）使用[UN/CEFACT通用代码]（http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes）给出。根据流量的类型，该值可以是**KMH** f（车辆、行人等）代表公里/小时（km/h）或**KNT**代表Knot（船）。  - `congested[boolean]`: 标志着在观察期间，在所指的人行道上是否有人群拥挤的情况。没有这个属性意味着没有人群拥堵。  - `dataProvider[string]`: 一串识别统一数据实体提供者的字符。  - `dateCreated[string]`: 实体创建时间戳。这通常会由存储平台分配。  - `dateModified[string]`: 实体最后一次修改的时间戳。这通常会由存储平台分配。  - `dateObserved[string]`: 由用户定义的被观察实体的日期。  - `dateObservedFrom[string]`: 观察期:开始日期和时间为ISO8601 UTC格式。  - `dateObservedTo[string]`: 观察期:结束日期和时间为ISO8601 UTC格式。  - `description[string]`: 对这个项目的描述  - `id[*]`: 实体的唯一标识符  - `intensity[number]`: 在这个观察期发现的物品总数  - `itemSubType[string]`: 对NGSI实体（Vehicle / BoatType / Person）现有 "子类型 "属性的标识符的引用，或对列出要计算的项目 "子类型 "的未来实体的引用。  - `itemType[string]`: 对NGSI实体（Vehicle / BoatType / Person）或未来实体的现有 "类型 "属性的标识符的引用，列出要计算的项目 "类型"。枚举：'人、船、车辆、游艇'  - `laneDirection[string]`: 该观察所涉及的车道上的通常行驶方向。这个属性在观察值没有引用任何路段时非常有用，可以知道所观察的交通流的行进方向。关于这些值的语义描述，见RoadSegment。  - `laneId[integer]`: 车道标识符。车道识别是使用RoadSegment实体定义的惯例来完成的，它是基于[OpenStreetMap](http://wiki.openstreetmap.org/wiki/Forward_%26_backward,_left_%26_right)。  - `location[*]`: 对该项目的Geojson引用。它可以是点、线字符串、多边形、多点、多线字符串或多多边形。  - `name[string]`: 这个项目的名称。  - `occupancy[number]`: 观察时间中，物品一直占据观察车道的部分。  - `owner[array]`: 一个包含JSON编码的字符序列的列表，引用所有者的唯一Ids。  - `refDevice[*]`: 用来获取本记录所表达的数据的设备或装置  - `refRoadSegment[*]`: 观察到的相关路段  - `reversedLane[boolean]`: 标志着该车道的交通在观察期间是否被逆转。没有这个属性意味着没有车道逆转。  - `seeAlso[*]`: 指向有关该项目的其他资源的URI列表  - `source[string]`: 一系列的字符，以URL的形式给出实体数据的原始来源。建议为源提供者的完全合格域名，或源对象的URL。  - `speedMax[number]`: 观测期间检测到的最大速度。单位代码（文本）使用[UN/CEFACT通用代码]（http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes）给出。根据流量的类型，该值可以是**KMH**（车辆、行人......）代表每小时公里数（km/h）或**KNT**代表节数（船）。  - `speedMin[number]`: 观测期间检测到的最小速度。单位代码（文本）使用[UN/CEFACT通用代码]（http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes）给出。根据流量的类型，该值可以是**KMH**（车辆、行人......）代表每小时公里数（km/h）或**KNT**代表节数（船）。  - `type[string]`: NGSI实体类型。它必须是ItemFlowObserved  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `dateObserved`  - `id`  - `laneId`  - `location`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 数据模型的属性描述  
按字母顺序排列（点击查看详情）。  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
ItemFlowObserved:    
  description: 'The data model intended to measure an observation linked to the movement of an item at a certain location and over a given period. This Data Model proposes an evolution of two Data Model by merging them and integrating all the attributes of the initial version of [TrafficFlowObserved] and [CrowFlowObserved] and by extension any type of item that we want to analyze the movements. Attributes `vehicleType` and `vehicleSubType` are removed from the initial data Model in order to become generic `itemType` and `itemSubType` of possible values. (people, Type of vehicle, Type of boat, Type of plane, ...).'    
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
    averageGapDistance:    
      description: 'Average gap distance between consecutive 2 detected items. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **MTR** represents Meter.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    averageHeadwayTime:    
      description: 'Average headway time. Head away time is the time elapsed between two consecutive items. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **SEC** represents Second.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    averageLength:    
      description: 'Average length of detected items transiting during the observation period. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . For instance, **MTR** represents Meter.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    averageSpeed:    
      description: 'Average speed of detected items transiting during the observation period. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . Depending the type of Flow, the value can be **KMH** f(vehicule, pedestrian, etc.) represents Kilometer per hour (km/h) or **KNT** represents Knot (Boat).'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    congested:    
      description: 'Flags whether there was a crowd congestion during the observation period in the referred walkway. The absence of this attribute means no crowd congestion'    
      type: boolean    
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
    dateObserved:    
      description: 'Date of the observed entity defined by the user.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateObservedFrom:    
      description: 'Observation period : Start date and time in an ISO8601 UTC format.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateObservedTo:    
      description: 'Observation period : End date and time in an ISO8601 UTC format.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &itemflowobserved_-_properties_-_owner_-_items_-_anyof    
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
    intensity:    
      description: 'Total number of items detected during this observation period'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    itemSubType:    
      description: 'Reference to an identifier of an existing ''subType'' attribute of an NGSI entity (Vehicle / BoatType / Person ) or of a future entity listing an item ''subType'' to be counted.'    
      type: string    
      x-ngsi:    
        type: Property    
    itemType:    
      description: 'Reference to an identifier of an existing ''Type'' attribute of an NGSI entity (Vehicle / BoatType / Person) or of a future entity listing an item ''Type'' to be counted. Enum:''people, ship, vehicle, yacht'''    
      enum:    
        - people    
        - ship    
        - vehicle    
        - yacht    
      type: string    
      x-ngsi:    
        type: Property    
    laneDirection:    
      description: 'Usual direction of travel in the lane referred by this observation. This attribute is useful when the observation is not referencing any road segment, allowing to know the direction of travel of the traffic flow observed. See RoadSegment for a description of the semantics of these values.'    
      enum:    
        - forward    
        - backward    
        - inbound    
        - outbound    
        - right    
        - left    
      type: string    
      x-ngsi:    
        type: Property    
    laneId:    
      description: 'Lane identifier. Lane identification is done using the conventions defined by RoadSegment entity which are based on [OpenStreetMap](http://wiki.openstreetmap.org/wiki/Forward_%26_backward,_left_%26_right).'    
      min: 1    
      type: integer    
      x-ngsi:    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'Geoproperty. Geojson reference to the item. Point'    
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
        - description: 'Geoproperty. Geojson reference to the item. LineString'    
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
        - description: 'Geoproperty. Geojson reference to the item. Polygon'    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiPoint'    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
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
        type: Geoproperty    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    occupancy:    
      description: 'Fraction of the observation time where a item has been occupying the observed lane'    
      maximum: 1    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *itemflowobserved_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    refDevice:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'The device or devices used to obtain the data expressed by this record'    
      x-ngsi:    
        type: Relationship    
    refRoadSegment:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Concerned road segment on which the observation has been made'    
      x-ngsi:    
        type: Relationship    
    reversedLane:    
      description: 'Flags whether traffic in the lane was reversed during the observation period. The absence of this attribute means no lane reversion'    
      type: boolean    
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
    speedMax:    
      description: 'Maximum speed detected during the observation period. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . Depending the type of Flow, the value can be **KMH** (vehicule, pedestrian, ...) represents Kilometer per hour (km/h) or **KNT** represents Knot (Boat).'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    speedMin:    
      description: 'Minimum speed detected during the observation period. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . Depending the type of Flow, the value can be **KMH** (vehicule, pedestrian, ...) represents Kilometer per hour (km/h) or **KNT** represents Knot (Boat).'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI Entity type. It has to be ItemFlowObserved'    
      enum:    
        - ItemFlowObserved    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - location    
    - dateObserved    
    - laneId    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Transportation/blob/master/ItemFlowObserved/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/data-models/Transportation/ItemFlowObserved/schema.json    
  x-model-tags: ""    
  x-version: ""    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ＃＃＃＃有效载荷的例子  
#### ItemFlowObserved NGSI-v2 key-values 示例  
这里是一个以JSON-LD格式作为key-values的ItemFlowObserved的例子。当使用`options=keyValues`时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "FlowObserved:BFO-NCE-MNCA-SP-001",  
  "type": "ItemFlowObserved",  
  "address": {  
    "addressCountry": "FR",  
    "addressLocality": "Nice",  
    "streetAddress": "Port Lympia"  
  },  
  "areaServed": "Nice Harbor",  
  "averageGapDistance": 35.28,  
  "averageHeadwayTime": 156,  
  "averageLength": 7.44,  
  "averageSpeed": 2.7,  
  "congested": false,  
  "dateObserved": "2020-03-20T16:30:00Z",  
  "dateObservedFrom": "2020-03-20T16:30:00Z",  
  "dateObservedTo": "2020-03-20T22:30:00Z",  
  "description": "Boat Flow Observed from Nice Harbor.",  
  "itemSubType": "monoHull",  
  "itemType": "yacht",  
  "intensity": 12,  
  "laneDirection": "outbound",  
  "laneId": 1,  
  "location": {  
    "coordinates": [  
      7.196545,  
      43.664809  
    ],  
    "type": "Point"  
  },  
  "maxSpeed": 3.8,  
  "minSpeed": 2.6,  
  "name": "BFO-NCE-MNCA-SP-001",  
  "occupancy": 0.1562,  
  "refDevice": "Device:BFO-NCE-MNCA-SP-001-Dev-02",  
  "reverseLane": false  
}  
```  
</details>  
#### ItemFlowObserved NGSI-v2 normalized 示例  
这里是一个以JSON-LD格式规范化的ItemFlowObserved的例子。当不使用选项时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "FlowObserved:BFO-NCE-MNCA-SP-001",  
  "type": "ItemFlowObserved",  
  "name": {  
    "type": "Text",  
    "value": "BFO-NCE-MNCA-SP-001"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Boat Flow Observed from Nice Harbor."  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        7.196545,  
        43.664809  
      ]  
    }  
  },  
  "address": {  
    "type": "PostalAddress",  
    "value": {  
      "streetAddress": "Port Lympia",  
      "addressLocality": "Nice",  
      "addressCountry": "FR"  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Nice Harbor"  
  },  
  "dateObserved": {  
    "type": "DateTime",  
    "value": "2020-03-20T16:30:00Z"  
  },  
  "dateObservedFrom": {  
    "type": "DateTime",  
    "value": "2020-03-20T16:30:00Z"  
  },  
  "dateObservedTo": {  
    "type": "DateTime",  
    "value": "2020-03-20T22:30:00Z"  
  },  
  "refDevice": {  
    "type": "Relationship",  
    "value": "Device:BFO-NCE-MNCA-SP-001-Dev-02"  
  },  
  "itemType": {  
    "type": "Text",  
    "value": "yacht"  
  },  
  "itemSubType": {  
    "type": "Text",  
    "value": "monoHull"  
  },  
  "laneId": {  
    "type": "Integer",  
    "value": 1  
  },  
  "laneDirection": {  
    "type": "Text",  
    "value": "outbound"  
  },  
  "reverseLane": {  
    "type": "Boolean",  
    "value": false  
  },  
  "intensity": {  
    "type": "Number",  
    "value": 12  
  },  
  "occupancy": {  
    "type": "Number",  
    "value": 0.1562  
  },  
  "congested": {  
    "type": "Boolean",  
    "value": false  
  },  
  "averageSpeed": {  
    "type": "Number",  
    "value": 2.7  
  },  
  "averageLength": {  
    "type": "Number",  
    "value": 7.44  
  },  
  "averageHeadwayTime": {  
    "type": "Number",  
    "value": 156  
  },  
  "averageGapDistance": {  
    "type": "Number",  
    "value": 35.28  
  },  
  "minSpeed": {  
    "type": "Number",  
    "value": 2.6  
  },  
  "maxSpeed": {  
    "type": "Number",  
    "value": 3.8  
  }  
}  
```  
</details>  
#### ItemFlowObserved NGSI-LD key-values 示例  
这里是一个以JSON-LD格式作为key-values的ItemFlowObserved的例子。当使用`options=keyValues`时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "itemFlowObserved:BFO-NCE-MNCA-SP-001",  
    "type": "ItemFlowObserved",  
    "address": {  
        "addressCountry": "FR",  
        "addressLocality": "Nice",  
        "streetAddress": "Port Lympia"  
    },  
    "areaServed": "Nice Harbor",  
    "averageGapDistance": 35.28,  
    "averageHeadwayTime": 156,  
    "averageLength": 7.44,  
    "averageSpeed": 2.7,  
    "congested": false,  
    "dateObserved": "2020-03-20T16:30:00Z",  
    "dateObservedFrom": "2020-03-20T16:30:00Z",  
    "dateObservedTo": "2020-03-20T22:30:00Z",  
    "description": "Boat Flow Observed from Nice Harbor.",  
    "intensity": 12,  
    "itemSubtype": "monoHull",  
    "itemType": "yacht",  
    "laneDirection": "outbound",  
    "laneId": 1,  
    "location": {  
        "coordinates": [  
            7.196545,  
            43.664809  
        ],  
        "type": "Point"  
    },  
    "maxSpeed": 3.8,  
    "minSpeed": 2.6,  
    "name": "BFO-NCE-MNCA-SP-001",  
    "occupancy": 0.1562,  
    "refDevice": "Device:BFO-NCE-MNCA-SP-001-Dev-02",  
    "reverseLane": false,  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Transportation/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### ItemFlowObserved NGSI-LD normalized Example  
这里是一个以JSON-LD格式规范化的ItemFlowObserved的例子。当不使用选项时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "FlowObserved:BFO-NCE-MNCA-SP-001",  
    "type": "ItemFlowObserved",  
    "address": {  
        "type": "Property",  
        "value": {  
            "streetAddress": "Port Lympia",  
            "addressLocality": "Nice",  
            "addressCountry": "FR"  
        }  
    },  
    "areaServed": {  
        "type": "Property",  
        "value": "Nice Harbor"  
    },  
    "averageGapDistance": {  
        "type": "Property",  
        "value": 35.28,  
        "unitCode": "MTR"  
    },  
    "averageHeadwayTime": {  
        "type": "Property",  
        "value": 156,  
        "unitCode": "SEC"  
    },  
    "averageLength": {  
        "type": "Property",  
        "value": 7.44,  
        "unitCode": "MTR"  
    },  
    "averageSpeed": {  
        "type": "Property",  
        "value": 2.7,  
        "unitCode": "KNT"  
    },  
    "congested": {  
        "type": "Property",  
        "value": false  
    },  
    "dateObserved": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2020-03-20T16:30:00Z"  
        }  
    },  
    "dateObservedFrom": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2020-03-20T16:30:00Z"  
        }  
    },  
    "dateObservedTo": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2020-03-20T22:30:00Z"  
        }  
    },  
    "description": {  
        "type": "Property",  
        "value": "Boat Flow Observed from Nice Harbor."  
    },  
    "intensity": {  
        "type": "Property",  
        "value": 12  
    },  
    "itemSubType": {  
        "type": "Property",  
        "value": "monoHull"  
    },  
    "itemType": {  
        "type": "Property",  
        "value": "yatching"  
    },  
    "laneDirection": {  
        "type": "Property",  
        "value": "outbound"  
    },  
    "laneId": {  
        "type": "Property",  
        "value": 1  
    },  
    "location": {  
        "type": "Geoproperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                7.196545,  
                43.664809  
            ]  
        }  
    },  
    "maxSpeed": {  
        "type": "Property",  
        "value": 3.8,  
        "unitCode": "KNT"  
    },  
    "minSpeed": {  
        "type": "Property",  
        "value": 2.6,  
        "unitCode": "KNT"  
    },  
    "name": {  
        "type": "Property",  
        "value": "BFO-NCE-MNCA-SP-001"  
    },  
    "occupancy": {  
        "type": "Property",  
        "value": 0.1562  
    },  
    "refDevice": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Device:BFO-NCE-MNCA-SP-001-Dev-02"  
    },  
    "reverseLane": {  
        "type": "Property",  
        "value": false  
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
参见[常见问题10](https://smartdatamodels.org/index.php/faqs/)，以获得关于如何处理量级单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
