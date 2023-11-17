<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
实体流量观测    
======<!-- /10-Header -->    
<!-- 15-License -->    
[开放许可](https://github.com/smart-data-models//dataModel.Transportation/blob/master/TrafficFlowObserved/LICENSE.md)    
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
全球描述：**对某时某地交通流量状况的观测。    
版本： 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## 属性列表    
<sup><sub>[*] 如果属性中没有类型，是因为它可能有多个类型或不同的格式/模式</sub></sup>。    
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国家。例如，西班牙  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: 街道地址所在的地点，以及该地点所在的区域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: 地点所在的地区，以及该地区位于哪个国家  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: 地区是一种行政区划，在一些国家由地方政府管理      
	- `postOfficeBoxNumber[string]`: 用于邮政信箱地址的邮政信箱号码。例如：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: 邮政编码。例如：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: 街道地址  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `alternateName[string]`: 该项目的替代名称  - `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `averageGapDistance[number]`: 连续车辆之间的平均间距  . Model: [https://schema.org/Number](https://schema.org/Number)- `averageHeadwayTime[number]`: 平均通行时间。超车时间是指连续两辆车之间的时间间隔。  . Model: [https://schema.org/Number](https://schema.org/Number)- `averageVehicleLength[number]`: 观测期间过境车辆的平均长度    
    平均长度  . Model: [https://schema.org/Number](https://schema.org/Number)- `averageVehicleSpeed[number]`: 观测期间过境车辆的平均速度  . Model: [https://schema.org/Number](https://schema.org/Number)- `congested[boolean]`: 标记观测期间所指车道是否发生交通拥堵。没有该属性表示没有交通拥堵  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `dateObserved[string]`: 以 ISO8601 UTC 格式表示的观测日期和时间。它可以用一个特定的时间瞬间或一个 ISO8601 时间间隔来表示。由于 Orion Context Broker 不支持日期时间间隔，因此可以使用两个不同的属性：dateObservedFrom "和 "dateObservedTo"。[日期时间](https://schema.org/DateTime) 或以[文本](https://schema.org/Text) 表示的 ISO8601 时间间隔  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateObservedFrom[date-time]`: 观察期开始日期和时间。参见 `dateObserved` 。  . Model: [https://schema.org/Datetime](https://schema.org/Datetime)- `dateObservedTo[date-time]`: 观察期结束日期和时间。请参阅 "观察日期"。  . Model: [https://schema.org/Datetime](https://schema.org/Datetime)- `description[string]`: 项目描述  - `id[*]`: 实体的唯一标识符  - `intensity[number]`: 观测期间检测到的车辆总数  . Model: [https://schema.org/Number](https://schema.org/Number)- `laneDirection[string]`: 该观测值所指车道的通常行驶方向。该属性在观测值未引用任何路段时非常有用，可用于了解所观测交通流的行驶方向。枚举：前进、后退"。有关这些值的语义说明，请参阅 RoadSegment。  . Model: [https://schema.org/Text](https://schema.org/Text)- `laneId[number]`: 车道标识符。车道识别使用基于 [OpenStreetMap](http://wiki.openstreetmap.org/wiki/Forward_%26_backward,_left_%26_right) 的 RoadSegment 实体所定义的约定。  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `name[string]`: 该项目的名称  - `occupancy[number]`: 车辆占用观察车道的观察时间比例  . Model: [https://schema.org/Number](https://schema.org/Number)- `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `refRoadSegment[uri]`: 观测对象所在的相关路段。指向 "路段 "类型实体的引用  . Model: [https://schema.org/URL](https://schema.org/URL)- `reversedLane[boolean]`: 标记在观察期间车道上的交通是否逆向。没有该属性表示车道没有逆转  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `type[string]`: NGSI 实体类型。必须是 TrafficFlowObserved  - `vehicleSubType[string]`: 它允许指定 "车辆类型 "的子类型，例如，如果 "车辆类型 "设置为 "货车"，则 "车辆子类型 "可以是 "OGV1 "或 "OGV2"，以传达有关车辆确切类型的更多信息。  - `vehicleType[string]`: 从结构特征角度看的车辆类型。枚举:'农用车、自行车、公共汽车、小客车、汽车、大篷车、电车、油罐车、带大篷车的汽车、带拖车的汽车、货车、轻便摩托车、摩托车、带侧车的摩托车、摩托车、拖车、面包车、建筑或维护车辆、手推车、垃圾车、清扫机、清洁车'。  . Model: [https://schema.org/Text](https://schema.org/Text)<!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
所需属性    
- `dateObserved`  - `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
该实体主要负责汽车和智能城市垂直细分市场以及相关的物联网应用。    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## 属性的数据模型描述    
按字母顺序排列（点击查看详情）    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
TrafficFlowObserved:      
  description: An observation of traffic flow conditions at a certain place and time.      
  properties:      
    address:      
      description: The mailing address      
      properties:      
        addressCountry:      
          description: 'The country. For example, Spain'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressCountry      
            type: Property      
        addressLocality:      
          description: 'The locality in which the street address is, and which is in the region'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressLocality      
            type: Property      
        addressRegion:      
          description: 'The region in which the locality is, and which is in the country'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressRegion      
            type: Property      
        district:      
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government'      
          type: string      
          x-ngsi:      
            type: Property      
        postOfficeBoxNumber:      
          description: 'The post office box number for PO box addresses. For example, 03578'      
          type: string      
          x-ngsi:      
            model: https://schema.org/postOfficeBoxNumber      
            type: Property      
        postalCode:      
          description: 'The postal code. For example, 24004'      
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
    areaServed:      
      description: The geographic area where a service or offered item is provided      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    averageGapDistance:      
      description: Average gap distance between consecutive vehicles      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: meter (m)      
    averageHeadwayTime:      
      description: Average headway time. Headway time is the time ellapsed between two consecutive vehicles      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: second (s)      
    averageVehicleLength:      
      description: |-      
        Average length of the vehicles transiting during      
            the observation period      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: meter (m)      
    averageVehicleSpeed:      
      description: Average speed of the vehicles transiting during the observation period      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: Kilometer per hour (Km/h)      
    congested:      
      description: ' Flags whether there was a traffic congestion during the observation period in the referred lane. The absence of this attribute means no traffic congestion'      
      type: boolean      
      x-ngsi:      
        model: https://schema.org/Boolean      
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
    dateObserved:      
      description: 'The date and time of this observation in ISO8601 UTC format. It can be represented by an specific time instant or by an ISO8601 interval. As a workaround for the lack of support of Orion Context Broker for datetime intervals, it can be used two separate attributes: `dateObservedFrom`, `dateObservedTo`. [DateTime](https://schema.org/DateTime) or an ISO8601 interval represented as [Text](https://schema.org/Text)'      
      type: string      
      x-ngsi:      
        model: https://schema.org/DateTime      
        type: Property      
    dateObservedFrom:      
      description: Observation period start date and time. See `dateObserved`      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/Datetime      
        type: Property      
    dateObservedTo:      
      description: Observation period end date and time. See `dateObserved`      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/Datetime      
        type: Property      
    description:      
      description: A description of this item      
      type: string      
      x-ngsi:      
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
        type: Property      
    intensity:      
      description: Total number of vehicles detected during this observation period      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    laneDirection:      
      description: 'Usual direction of travel in the lane referred by this observation. This attribute is useful when the observation is not referencing any road segment, allowing to know the direction of travel of the traffic flow observed. Enum:forward, backward''. See RoadSegment for a description of the semantics of these values'      
      enum:      
        - forward      
        - backward      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    laneId:      
      description: 'Lane identifier. Lane identification is done using the conventions defined by RoadSegment entity which are based on [OpenStreetMap](http://wiki.openstreetmap.org/wiki/Forward_%26_backward,_left_%26_right)'      
      minimum: 1      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    location:      
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'      
      oneOf:      
        - description: Geojson reference to the item. Point      
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
          title: GeoJSON Point      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. LineString      
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
          title: GeoJSON LineString      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. Polygon      
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
          title: GeoJSON Polygon      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiPoint      
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
          title: GeoJSON MultiPoint      
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
          title: GeoJSON MultiPolygon      
          type: object      
          x-ngsi:      
            type: GeoProperty      
      x-ngsi:      
        type: GeoProperty      
    name:      
      description: The name of this item      
      type: string      
      x-ngsi:      
        type: Property      
    occupancy:      
      description: Fraction of the observation time where a vehicle has been occupying the observed lane      
      maximum: 1      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
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
          type: Property      
      type: array      
      x-ngsi:      
        type: Property      
    refRoadSegment:      
      description: Concerned road segment on which the observation has been made. Reference to an entity of type RoadSegment      
      format: uri      
      type: string      
      x-ngsi:      
        model: https://schema.org/URL      
        type: Relationship      
    reversedLane:      
      description: Flags whether traffic in the lane was reversed during the observation period. The absence of this attribute means no lane reversion      
      type: boolean      
      x-ngsi:      
        model: https://schema.org/Boolean      
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
      type: string      
      x-ngsi:      
        type: Property      
    type:      
      description: NGSI Entity type. It has to be TrafficFlowObserved      
      enum:      
        - TrafficFlowObserved      
      type: string      
      x-ngsi:      
        type: Property      
    vehicleSubType:      
      description: 'It allows to specify a sub type of `vehicleType`, eg if the `vehicleType` is set to `Lorry` the `vehicleSubType` may be `OGV1` or `OGV2` to convey more information about the exact type of vehicle'      
      type: string      
      x-ngsi:      
        type: Property      
    vehicleType:      
      description: 'Type of vehicle from the point of view of its structural characteristics. Enum:''agriculturalVehicle, bicycle, bus, minibus, car, caravan, tram, tanker, carWithCaravan, carWithTrailer, lorry, moped, motorcycle, motorcycleWithSideCar, motorscooter, trailer, van, constructionOrMaintenanceVehicle, trolley, binTrolley, sweepingMachine, cleaningTrolley'''      
      enum:      
        - agriculturalVehicle      
        - bicycle      
        - bus      
        - minibus      
        - car      
        - caravan      
        - tram      
        - tanker      
        - carWithCaravan      
        - carWithTrailer      
        - lorry      
        - moped      
        - motorcycle      
        - motorcycleWithSideCar      
        - motorscooter      
        - trailer      
        - van      
        - constructionOrMaintenanceVehicle      
        - trolley      
        - binTrolley      
        - sweepingMachine      
        - cleaningTrolley      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
  required:      
    - id      
    - type      
    - dateObserved      
  type: object      
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.Transportation/blob/master/TrafficFlowObserved/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.Transportation/TrafficFlowObserved/schema.json      
  x-model-tags: ""      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## 有效载荷示例    
#### TrafficFlowObserved NGSI-v2 key-values 示例    
下面是一个以 JSON-LD 格式作为键值的 TrafficFlowObserved 示例。当使用 "options=keyValues "时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "TrafficFlowObserved-Valladolid-osm-60821110",  
  "type": "TrafficFlowObserved",  
  "laneId": 1,  
  "address": {  
    "streetAddress": "Avenida de Salamanca",  
    "addressLocality": "Valladolid",  
    "addressCountry": "ES"  
  },  
  "location": {  
    "type": "LineString",  
    "coordinates": [  
      [  
        -4.73735395519672,  
        41.6538181849672  
      ],  
      [  
        -4.73414858659993,  
        41.6600594193478  
      ],  
      [  
        -4.73447575302641,  
        41.659585195093  
      ]  
    ]  
  },  
  "dateObserved": "2016-12-07T11:10:00/2016-12-07T11:15:00",  
  "dateObservedFrom": "2016-12-07T11:10:00Z",  
  "dateObservedTo": "2016-12-07T11:15:00Z",  
  "averageHeadwayTime": 0.5,  
  "intensity": 197,  
  "occupancy": 0.76,  
  "averageVehicleSpeed": 52.6,  
  "averageVehicleLength": 9.87,  
  "reversedLane": false,  
  "laneDirection": "forward"  
}  
```  
</details>    
#### TrafficFlowObserved NGSI-v2 normalized 示例    
以下是以 JSON-LD 格式规范化的 TrafficFlowObserved 示例。当不使用选项时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "TrafficFlowObserved-Valladolid-osm-60821110",  
  "type": "TrafficFlowObserved",  
  "dateObserved": {  
    "type": "DateTime",  
    "value": "2016-12-07T11:10:00/2016-12-07T11:15:00"  
  },  
  "laneDirection": {  
    "type": "Text",  
    "value": "forward"  
  },  
  "dateObservedFrom": {  
    "type": "DateTime",  
    "value": "2016-12-07T11:10:00Z"  
  },  
  "averageVehicleLength": {  
    "type": "Number",  
    "value": 9.87  
  },  
  "averageHeadwayTime": {  
    "type": "Number",  
    "value": 0.5  
  },  
  "occupancy": {  
    "type": "Number",  
    "value": 0.76  
  },  
  "reversedLane": {  
    "type": "Boolean",  
    "value": false  
  },  
  "dateObservedTo": {  
    "type": "DateTime",  
    "value": "2016-12-07T11:15:00Z"  
  },  
  "intensity": {  
    "type": "Number",  
    "value": 197  
  },  
  "laneId": {  
    "type": "Boolean",  
    "value": true  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "LineString",  
      "coordinates": [  
        [  
          -4.73735395519672,  
          41.6538181849672  
        ],  
        [  
          -4.73414858659993,  
          41.6600594193478  
        ],  
        [  
          -4.73447575302641,  
          41.659585195093  
        ]  
      ]  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "addressLocality": "Valladolid",  
      "addressCountry": "ES",  
      "streetAddress": "Avenida de Salamanca"  
    }  
  },  
  "averageVehicleSpeed": {  
    "type": "Number",  
    "value": 52.6  
  }  
}  
```  
</details>    
#### TrafficFlowObserved NGSI-LD key-values 示例    
下面是一个以 JSON-LD 格式作为键值的 TrafficFlowObserved 示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:TrafficFlowObserved:TrafficFlowObserved-Valladolid-osm-60821110",  
  "type": "TrafficFlowObserved",  
  "address": {  
    "addressCountry": "ES",  
    "addressLocality": "Valladolid",  
    "streetAddress": "Avenida de Salamanca",  
    "type": "PostalAddress"  
  },  
  "averageHeadwayTime": 0.5,  
  "averageVehicleLength": 9.87,  
  "averageVehicleSpeed": 52.6,  
  "dateObserved": "2016-12-07T11:10:00/2016-12-07T11:15:00",  
  "dateObservedFrom": "2016-12-07T11:10:00Z",  
  "dateObservedTo": "2016-12-07T11:15:00Z",  
  "intensity": 197,  
  "laneDirection": "forward",  
  "laneId": 1,  
  "location": {  
    "coordinates": [  
      [  
        -4.73735395519672,  
        41.6538181849672  
      ],  
      [  
        -4.73414858659993,  
        41.6600594193478  
      ],  
      [  
        -4.73447575302641,  
        41.659585195093  
      ]  
    ],  
    "type": "LineString"  
  },  
  "occupancy": 0.76,  
  "reversedLane": false,  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Transportation/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### TrafficFlowObserved NGSI-LD normalized 示例    
以下是以 JSON-LD 格式规范化的 TrafficFlowObserved 示例。当不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:TrafficFlowObserved:TrafficFlowObserved-Valladolid-osm-60821110",  
  "type": "TrafficFlowObserved",  
  "address": {  
    "type": "Property",  
    "value": {  
      "addressLocality": "Valladolid",  
      "addressCountry": "ES",  
      "streetAddress": "Avenida de Salamanca"  
    }  
  },  
  "averageHeadwayTime": {  
    "type": "Property",  
    "value": 0.5  
  },  
  "averageVehicleLength": {  
    "type": "Property",  
    "value": 9.87  
  },  
  "averageVehicleSpeed": {  
    "type": "Property",  
    "value": 52.6  
  },  
  "dateObserved": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2016-12-07T11:10:00"  
    }  
  },  
  "dateObservedFrom": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2016-12-07T11:10:00Z"  
    }  
  },  
  "dateObservedTo": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2016-12-07T11:15:00Z"  
    }  
  },  
  "intensity": {  
    "type": "Property",  
    "value": 197  
  },  
  "laneDirection": {  
    "type": "Property",  
    "value": "forward"  
  },  
  "laneId": {  
    "type": "Property",  
    "value": 1  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "LineString",  
      "coordinates": [  
        [  
          -4.73735395519672,  
          41.6538181849672  
        ],  
        [  
          -4.73414858659993,  
          41.6600594193478  
        ],  
        [  
          -4.73447575302641,  
          41.659585195093  
        ]  
      ]  
    }  
  },  
  "occupancy": {  
    "type": "Property",  
    "value": 0.76  
  },  
  "reversedLane": {  
    "type": "Property",  
    "value": false  
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Transportation/master/context.jsonld"  
  ]  
}  
```  
</details><!-- /80-Examples -->    
<!-- 90-FooterNotes -->    
<!-- /90-FooterNotes -->    
<!-- 95-Units -->    
请参阅 [FAQ 10](https://smartdatamodels.org/index.php/faqs/)，获取如何处理幅度单位的答案。    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
