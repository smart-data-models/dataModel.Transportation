<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体。票价采集系统  
=========<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.Transportation/blob/master/FareCollectionSystem/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全球描述。**一个公共交通的收费系统 数据模型**  
版本：0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

##属性列表  

<sup><sub>[*] 如果一个属性中没有一个类型，是因为它可能有几种类型或不同的格式/模式</sub></sup>。  
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: 这个项目的一个替代名称  - `areaServed[string]`: 提供服务或提供项目的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `cardId[string]`: 交易的唯一票据ID或交易中使用的智能卡的ID。  . Model: [https://schema.org/Text](https://schema.org/Text)- `currentTripCount[number]`: 与该观察点相对应的车辆在特定运行日的当前行程数。  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: 一串识别统一数据实体提供者的字符。  - `dateCreated[string]`: 实体创建时间戳。这通常会由存储平台分配。  - `dateModified[string]`: 实体最后一次修改的时间戳。这通常会由存储平台分配。  - `description[string]`: 对这个项目的描述  - `destinationStopCategory[string]`: 与该观察结果相对应的目的地巴士站的类型。  . Model: [https://schema.org/Text](https://schema.org/Text)- `destinationStopId[string]`: 与此观察相对应的乘客下车的巴士站的唯一标识。  . Model: [https://schema.org/Text](https://schema.org/Text)- `destinationStopName[string]`: 与该观察结果相对应的目的地巴士站的名称。  . Model: [https://schema.org/Text](https://schema.org/Text)- `direction_id[number]`: 表示与该观测值相对应的车辆行驶方向，可从GTFS静态资料trips.txt中引用。与此相同。来自GTFS实时消息-行程描述符的'方向_id'字段(https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)  . Model: [https://schema.org/Number](https://schema.org/Number)- `entryAreaCode[string]`: 乘客上车站点的地区代码（由收费机构使用）。例如，该站是城市巴士服务站还是BRTS站或其他服务类型的站等。  . Model: [https://schema.org/Text](https://schema.org/Text)- `equipmentCompanyCode[string]`: 交易设备的公司/机构代码（由收费机构使用）。例如，103-CBS（城市公交服务），102-BRTS等。  . Model: [https://schema.org/Text](https://schema.org/Text)- `equipmentId[string]`: 与此观察相对应的设备的唯一标识。  . Model: [https://schema.org/Text](https://schema.org/Text)- `equipmentSequenceNumber[number]`: 给定设备的序列号。  . Model: [https://schema.org/Number](https://schema.org/Number)- `equipmentStopId[string]`: 与此交易相对应的设备安装在哪个站点（BRTS）。  . Model: [https://schema.org/Text](https://schema.org/Text)- `equipmentType[string]`: 设备类型或与此观察对应的设备名称。  . Model: [https://schema.org/Text](https://schema.org/Text)- `equipmentTypeCode[string]`: 表示交易中使用的设备类型的唯一代码（由收费机构使用）。ENUM [1B, 42, 02, 08, 41] 1B - POS, 42 - HTT, 02- Mobile, 08- Fare Gate, 41- Pole Validator  . Model: [https://schema.org/Text](https://schema.org/Text)- `exitAreaCode[string]`: 乘客下车站的地区代码（由收费机构使用）。例如，该站是城市巴士服务站还是BRTS站或其他服务类型的站等。  . Model: [https://schema.org/Text](https://schema.org/Text)- `fareForAdult[number]`: 在与此观察相对应的旅程中，一个成年人的票价。  . Model: [https://schema.org/Number](https://schema.org/Number)- `fareForChild[number]`: 在与此观察相对应的旅程中，一个孩子的车费。  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: 实体的唯一标识符  - `location[*]`: 对该项目的Geojson引用。它可以是点、线字符串、多边形、多点、多线字符串或多多边形。  - `name[string]`: 这个项目的名称。  - `observationDateTime[string]`: 最后报告的观察时间。  . Model: [https://schema.org/Text](https://schema.org/Text)- `occupancyLevel[string]`: 与此观察相对应的公交车上的占用水平。红色 "表示公交车的拥挤程度高，"黄色 "表示公交车的拥挤程度中等，"绿色 "表示公交车的拥挤程度低。  . Model: [https://schema.org/Text](https://schema.org/Text)- `originDestinationCode[string]`: 与此观察相对应的起点和终点站的代码。  . Model: [https://schema.org/Text](https://schema.org/Text)- `originStopCategory[string]`: 与该观察点相对应的始发站类型。  . Model: [https://schema.org/Text](https://schema.org/Text)- `originStopId[string]`: 与此观察相对应的乘客上车的巴士站的唯一标识。  . Model: [https://schema.org/Text](https://schema.org/Text)- `originStopName[string]`: 与该观测点相对应的始发站名称。  . Model: [https://schema.org/Text](https://schema.org/Text)- `owner[array]`: 一个包含JSON编码的字符序列的列表，引用所有者的唯一Ids。  - `passengerCount[number]`: 与此观察相对应的公交车上的乘客数量。这个数字是根据公交车上的实时票务交易计算出来的。  . Model: [https://schema.org/Number](https://schema.org/Number)- `route_id[string]`: 分配给该观察中的公共汽车/车辆所对应的路线的路线标识，目前正在该路线上行驶。与此相同。GTFS实时消息-行程描述符中的'路线_ID'字段(https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)  . Model: [https://schema.org/Text](https://schema.org/Text)- `seeAlso[*]`: 指向有关该项目的其他资源的URI列表  - `shiftOfOperation[string]`: 由收费机构/公共交通机构或雇员运营的公共交通车辆的运营班次，与此观察相对应。当车辆在第一班运行时，表示为'1'，当车辆在第二班运行时，表示为'2'，当车辆在第三班运行时，表示为'3'。  . Model: [https://schema.org/Text](https://schema.org/Text)- `source[string]`: 提供实体数据原始来源的一连串字符，作为一个URL。建议为源提供者的完全合格域名，或源对象的URL。  - `stage[number]`: 从始发站到终点站的总台数。  . Model: [https://schema.org/Number](https://schema.org/Number)- `ticketTypeCode[string]`: 相应行程的唯一票种代码。  . Model: [https://schema.org/Text](https://schema.org/Text)- `transactionDateTime[string]`: 与此观察相对应的交易的日期-时间。  . Model: [https://schema.org/Text](https://schema.org/Text)- `transactionType[string]`: 与此观察相对应的交易类型。例如 - 发行、再发行、进入、退出等。  . Model: [https://schema.org/Text](https://schema.org/Text)- `transactionTypeDescription[string]`: 交易类型的描述。数据中使用的各种transactionTypeId代码的解释。  . Model: [https://schema.org/Text](https://schema.org/Text)- `transactionVehicleNum[number]`: 收费机构用于与交易相对应的车辆号码的代码。  . Model: [https://schema.org/Number](https://schema.org/Number)- `travelDistance[number]`: 与此观察相对应的始发站和终点站之间的距离。  . Model: [https://schema.org/Number](https://schema.org/Number)- `trip_id[string]`: 考虑到一天中的时间和给定路线上的行程方向，将行程标识/行程名称分配给与该观察结果相对应的巴士。与此相同。GTFS实时消息-行程描述符中的'trip_id'字段 (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: NGSI实体类型。它必须是FareCollectionSystem  - `vehicle_label[string]`: 用户可见的标签，即必须向乘客展示的东西，以帮助识别正确的车辆。与此相同。来自GTFS实时信息-车辆描述符的'标签'字段 (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)  . Model: [https://schema.org/Text](https://schema.org/Text)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 数据模型的属性描述  
按字母顺序排列（点击查看详情）。  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
FareCollectionSystem:    
  description: 'A public transit fare collection system Data Model'    
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
    cardId:    
      description: 'Unique ticket Id of the transaction or Id of the smart card used in the transaction.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    currentTripCount:    
      description: 'The current count of trips made by the vehicle corresponding to this observation on the given day of operation.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
    destinationStopCategory:    
      description: 'Type of the destination bus stop corresponding to this observation.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    destinationStopId:    
      description: 'Unique Id of the bus stop at which the passenger deboards from the bus corresponding to this observation.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    destinationStopName:    
      description: 'The name of the destination bus stop corresponding to this observation.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    direction_id:    
      description: "Indicates the direction of travel of the vehicle corresponding to this observation, can be referenced from the GTFS static feed trips.txt. SameAs: 'direction_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)"    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    entryAreaCode:    
      description: 'Area code of the passenger boarding stop (used by the fare collection agency). For example, whether the stop is city-bus-service stop or brts stop or other service type stop etc.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    equipmentCompanyCode:    
      description: 'Company/Agency code for the transaction equipment (used by fare collection agency). For example, 103 - CBS (city bus service),102 - BRTS etc.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    equipmentId:    
      description: 'Unique Id of the equipment corresponding to this observation.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    equipmentSequenceNumber:    
      description: 'Sequence number for the given equipment.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    equipmentStopId:    
      description: 'Stop Id (BRTS) at which the equipment corresponding to this transaction is installed.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    equipmentType:    
      description: 'Type of equipment or the name of the equipment corresponding to this observation.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    equipmentTypeCode:    
      description: 'Unique code indicating the type of equipment used in the transaction (used by fare collection agency).ENUM [1B, 42, 02, 08, 41] 1B - POS, 42 - HTT, 02- Mobile, 08- Fare Gate, 41- Pole Validator'    
      enum:    
        - 1B    
        - 42    
        - 02    
        - 08    
        - 41    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    exitAreaCode:    
      description: 'Area code of the passenger alighting stop (used by the fare collection agency). For example, whether the stop is city-bus-service stop or BRTS stop or other service type stop etc.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    fareForAdult:    
      description: 'The fare for an adult in the journey corresponding to this observation.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fareForChild:    
      description: 'The fare for a child in the journey corresponding to this observation.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    id:    
      anyOf: &farecollectionsystem_-_properties_-_owner_-_items_-_anyof    
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
    observationDateTime:    
      description: 'Last reported time of observation.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    occupancyLevel:    
      description: 'Occupancy level in the public transit bus corresponding to this observation. ''Red'' indicates the congestion level in the bus is HIGH, ''Yellow'' indicates the congestion level in the bus is MODERATE and ''Green'' indicates the congestion level in the bus is LOW.'    
      enum:    
        - Red    
        - Yellow    
        - Green    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    originDestinationCode:    
      description: 'The code for the origin and destination stops corresponding to this observation.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    originStopCategory:    
      description: 'Type of the origin bus stop corresponding to this observation.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    originStopId:    
      description: 'Unique Id of the bus stop at which the passenger boards into the bus corresponding to this observation.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    originStopName:    
      description: 'The name of the origin bus stop corresponding to this observation.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *farecollectionsystem_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    passengerCount:    
      description: 'Number of passengers travelling in the public transit bus corresponding to this observation. This count is computed based on the realtime ticketing transactions in the public transit bus.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    route_id:    
      description: "Route Id assigned to the route on which the bus/vehicle corresponding to the bus in this observation is currently plying on. SameAs: 'route_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)"    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
    shiftOfOperation:    
      description: 'Shift of operation of the public transit vehicle operated by the fare collection agency/ public transit agency or the employee corresponding to this observation. Indicated as ''1'' when the vehicle operates in the first shift, ''2'' when the vehicle operates in the second shift and ''3'' when the vehicle operates in the third shift.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    stage:    
      description: 'Total number of stages from the origin bus stop to the destination bus stop.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ticketTypeCode:    
      description: 'Unique ticket type code of the corresponding trip.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    transactionDateTime:    
      description: 'Date-time of the transaction corresponding to this observation.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    transactionType:    
      description: 'Type of the transaction corresponding to this observation. For Eg - Issue, ReIssue, Entry, Exit etc.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    transactionTypeDescription:    
      description: 'Description of the transaction type. Explanation of various transactionTypeId codes used in the data.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    transactionVehicleNum:    
      description: 'Code used by fare collection agency for the vehicle number corresponding to the transaction.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    travelDistance:    
      description: 'The distance between the origin bus stop and the destination bus stop corresponding to this observation.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    trip_id:    
      description: "Trip Id/Trip name alloted to the bus corresponding to this observation, in consideration to the time of the day and the direction of the trip on the given routeId. SameAs: 'trip_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)"    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    type:    
      description: 'NGSI entity type. It has to be FareCollectionSystem'    
      enum:    
        - FareCollectionSystem    
      type: string    
      x-ngsi:    
        type: Property    
    vehicle_label:    
      description: "User visible label, i.e., something that must be shown to the passenger to help identify the correct vehicle. SameAs: 'label' field from GTFS Realtime message-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)"    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Transportation/blob/master/FareCollectionSystem/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Transportation/FareCollectionSystem/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ＃＃＃＃有效载荷的例子  
#### FareCollectionSystem NGSI-v2 关键值示例  
下面是一个以JSON-LD格式作为关键值的FareCollectionSystem的例子。当使用`options=keyValues`时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:FareCollectionSystem:id:RJSB:34513580",  
  "type": "FareCollectionSystem",  
  "address": {  
    "addressCountry": "France",  
    "addressLocality": "Nice",  
    "addressRegion": "Provenza-Alpes-Costa Azul",  
    "postOfficeBoxNumber": "",  
    "postalCode": "06000",  
    "streetAddress": "Av. Nicolas II"  
  },  
  "alternateName": "",  
  "areaServed": "Nice",  
  "cardId": "987201910",  
  "currentTripCount": 12,  
  "dataProvider": "",  
  "dateCreated": "2020-11-02T06:16:42Z",  
  "dateModified": "2020-12-27T15:13:17Z",  
  "description": "Fare collection system Nize for regional routes",  
  "destinationStopCategory": "Airport",  
  "destinationStopId": "Nice-Airport",  
  "destinationStopName": "Hour risk somebody deal system discussion other plan. Stage the film occur.",  
  "direction_id": 1,  
  "entryAreaCode": "city-bus-service",  
  "equipmentCompanyCode": "103",  
  "equipmentId": "S23",  
  "equipmentSequenceNumber": 2,  
  "equipmentStopId": "BRTS-Sen-23",  
  "equipmentType": "Entry sensor",  
  "equipmentTypeCode": "42",  
  "exitAreaCode": "city-bus-service",  
  "fareForAdult": 4.5,  
  "fareForChild": 3.6,  
  "location": {  
    "coordinates": [  
      43.7034,  
      7.2663  
    ],  
    "type": "Point"  
  },  
  "name": "Fare collection system Nize",  
  "observationDateTime": "1988-12-24T07:06:19Z",  
  "occupancyLevel": "Green",  
  "originDestinationCode": "23",  
  "originStopCategory": "Bus stop",  
  "originStopId": "9",  
  "originStopName": "Vauban",  
  "owner": [  
    "urn:ngsi-ld:FareCollectionSystem:items:XMXR:79897582",  
    "urn:ngsi-ld:FareCollectionSystem:items:SKAX:98192518"  
  ],  
  "passengerCount": 6,  
  "route_id": "4",  
  "seeAlso": [  
    "urn:ngsi-ld:FareCollectionSystem:items:VSVS:72352464",  
    "urn:ngsi-ld:FareCollectionSystem:items:VMFR:36424993"  
  ],  
  "shiftOfOperation": "2",  
  "source": "",  
  "stage": 4,  
  "ticketTypeCode": "Normal",  
  "transactionDateTime": "2021-08-20T15:45:22Z",  
  "transactionType": "Issue",  
  "transactionTypeDescription": "Regular Fare.",  
  "transactionTypeId": "2401",  
  "transactionVehicleNum": 23,  
  "travelDistance": 7.5,  
  "trip_id": "4A",  
  "vehicle_label": "5821JZS"  
}  
```  
</details>  
#### FareCollectionSystem NGSI-v2规范化示例  
下面是一个以JSON-LD格式规范化的FareCollectionSystem的例子。当不使用选项时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:FareCollectionSystem:id:RJSB:34513580",  
  "type": "FareCollectionSystem",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2020-11-02T06:16:42Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2020-12-27T15:13:17Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": ""  
  },  
  "name": {  
    "type": "Text",  
    "value": "Fare collection system Nize"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": ""  
  },  
  "description": {  
    "type": "Text",  
    "value": "Fare collection system Nize for regional routes"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": ""  
  },  
  "owner": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:FareCollectionSystem:items:XMXR:79897582",  
      "urn:ngsi-ld:FareCollectionSystem:items:SKAX:98192518"  
    ]  
  },  
  "seeAlso": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:FareCollectionSystem:items:VSVS:72352464",  
      "urn:ngsi-ld:FareCollectionSystem:items:VMFR:36424993"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        43.7034,  
        7.2663  
      ]  
    }  
  },  
  "address": {  
    "type": "PostalAddress",  
    "value": {  
      "streetAddress": "Av. Nicolas II",  
      "addressLocality": "Nice",  
      "addressRegion": "Provenza-Alpes-Costa Azul",  
      "addressCountry": "France",  
      "postalCode": "06000",  
      "postOfficeBoxNumber": ""  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Nice"  
  },  
  "destinationStopName": {  
    "type": "Text",  
    "value": "Hour risk somebody deal system discussion other plan. Stage the film occur."  
  },  
  "occupancyLevel": {  
    "type": "Text",  
    "value": "Green"  
  },  
  "travelDistance": {  
    "type": "number",  
    "value": 7.5  
  },  
  "passengerCount": {  
    "type": "number",  
    "value": 6  
  },  
  "transactionType": {  
    "type": "Text",  
    "value": "Issue"  
  },  
  "ticketTypeCode": {  
    "type": "Text",  
    "value": "Normal"  
  },  
  "originStopName": {  
    "type": "Text",  
    "value": "Vauban"  
  },  
  "entryAreaCode": {  
    "type": "Text",  
    "value": "city-bus-service"  
  },  
  "cardId": {  
    "type": "Text",  
    "value": "987201910"  
  },  
  "transactionTypeId": {  
    "type": "Text",  
    "value": "2401"  
  },  
  "stage": {  
    "type": "number",  
    "value": 4  
  },  
  "equipmentId": {  
    "type": "Text",  
    "value": "S23"  
  },  
  "direction_id": {  
    "type": "number",  
    "value": 1  
  },  
  "equipmentSequenceNumber": {  
    "type": "number",  
    "value": 2  
  },  
  "shiftOfOperation": {  
    "type": "Text",  
    "value": "2"  
  },  
  "route_id": {  
    "type": "Text",  
    "value": "4"  
  },  
  "trip_id": {  
    "type": "Text",  
    "value": "4A"  
  },  
  "originStopCategory": {  
    "type": "Text",  
    "value": "Bus stop"  
  },  
  "vehicle_label": {  
    "type": "Text",  
    "value": "5821JZS"  
  },  
  "fareForChild": {  
    "type": "number",  
    "value": 3.6  
  },  
  "transactionDateTime": {  
    "type": "DateTime",  
    "value":  "2021-08-20T15:45:22Z"  
  },  
  "destinationStopId": {  
    "type": "Text",  
    "value": "Nice-Airport"  
  },  
  "originDestinationCode": {  
    "type": "Text",  
    "value": "23"  
  },  
  "currentTripCount": {  
    "type": "number",  
    "value": 12  
  },  
  "equipmentTypeCode": {  
    "type": "Text",  
    "value": "42"  
  },  
  "destinationStopCategory": {  
    "type": "Text",  
    "value": "Airport"  
  },  
  "transactionVehicleNum": {  
    "type": "number",  
    "value": 23  
  },  
  "fareForAdult": {  
    "type": "number",  
    "value": 4.5  
  },  
  "observationDateTime": {  
    "type": "DateTime",  
    "value": "1988-12-24T07:06:19Z"  
  },  
  "equipmentCompanyCode": {  
    "type": "Text",  
    "value": "103"  
  },  
  "transactionTypeDescription": {  
    "type": "Text",  
    "value": "Regular Fare."  
  },  
  "exitAreaCode": {  
    "type": "Text",  
    "value": "city-bus-service"  
  },  
  "equipmentType": {  
    "type": "Text",  
    "value": "Entry sensor"  
  },  
  "equipmentStopId": {  
    "type": "Text",  
    "value": "BRTS-Sen-23"  
  },  
  "originStopId": {  
    "type": "Text",  
    "value": "9"  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
</details>  
#### FareCollectionSystem NGSI-LD 关键值示例  
下面是一个以JSON-LD格式作为关键值的FareCollectionSystem的例子。当使用`options=keyValues`时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:FareCollectionSystem:id:RJSB:34513580",  
    "type": "FareCollectionSystem",  
    "address": {  
        "addressCountry": "France",  
        "addressLocality": "Nice",  
        "addressRegion": "Provenza-Alpes-Costa Azul",  
        "postOfficeBoxNumber": "",  
        "postalCode": "06000",  
        "streetAddress": "Av. Nicolas II"  
    },  
    "alternateName": "",  
    "areaServed": "Nice",  
    "cardId": "987201910",  
    "currentTripCount": 12,  
    "dataProvider": "",  
    "dateCreated": "2020-11-02T06:16:42Z",  
    "dateModified": "2020-12-27T15:13:17Z",  
    "description": "Fare collection system Nize for regional routes",  
    "destinationStopCategory": "Airport",  
    "destinationStopId": "Nice-Airport",  
    "destinationStopName": "Hour risk somebody deal system discussion other plan. Stage the film occur.",  
    "direction_id": 1,  
    "entryAreaCode": "city-bus-service",  
    "equipmentCompanyCode": "103",  
    "equipmentId": "S23",  
    "equipmentSequenceNumber": 2,  
    "equipmentStopId": "BRTS-Sen-23",  
    "equipmentType": "Entry sensor",  
    "equipmentTypeCode": "42",  
    "exitAreaCode": "city-bus-service",  
    "fareForAdult": 4.5,  
    "fareForChild": 3.6,  
    "location": {  
        "coordinates": [  
            43.7034,  
            7.2663  
        ],  
        "type": "Point"  
    },  
    "name": "Fare collection system Nize",  
    "observationDateTime": "1988-12-24T07:06:19Z",  
    "occupancyLevel": "Green",  
    "originDestinationCode": "23",  
    "originStopCategory": "Bus stop",  
    "originStopId": "9",  
    "originStopName": "Vauban",  
    "owner": [  
        "urn:ngsi-ld:FareCollectionSystem:items:XMXR:79897582",  
        "urn:ngsi-ld:FareCollectionSystem:items:SKAX:98192518"  
    ],  
    "passengerCount": 6,  
    "route_id": "4",  
    "seeAlso": [  
        "urn:ngsi-ld:FareCollectionSystem:items:VSVS:72352464",  
        "urn:ngsi-ld:FareCollectionSystem:items:VMFR:36424993"  
    ],  
    "shiftOfOperation": "2",  
    "source": "",  
    "stage": 4,  
    "ticketTypeCode": "Normal",  
    "transactionDateTime": "2021-08-20T15:45:22Z",  
    "transactionType": "Issue",  
    "transactionTypeDescription": "Regular Fare.",  
    "transactionTypeId": "2401",  
    "transactionVehicleNum": 23,  
    "travelDistance": 7.5,  
    "trip_id": "4A",  
    "vehicle_label": "5821JZS",  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Transportation/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### FareCollectionSystem NGSI-LD规范化示例  
下面是一个以JSON-LD格式规范化的FareCollectionSystem的例子。当不使用选项时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:FareCollectionSystem:id:RJSB:34513580",  
    "type": "FareCollectionSystem",  
    "address": {  
        "type": "Property",  
        "value": {  
            "streetAddress": "Av. Nicolas II",  
            "addressLocality": "Nice",  
            "addressRegion": "Provenza-Alpes-Costa Azul",  
            "addressCountry": "France",  
            "postalCode": "06000",  
            "postOfficeBoxNumber": ""  
        }  
    },  
    "alternateName": {  
        "type": "Property",  
        "value": ""  
    },  
    "areaServed": {  
        "type": "Property",  
        "value": "Nice"  
    },  
    "cardId": {  
        "type": "Property",  
        "value": "987201910"  
    },  
    "currentTripCount": {  
        "type": "Property",  
        "value": 12  
    },  
    "dataProvider": {  
        "type": "Property",  
        "value": ""  
    },  
    "dateCreated": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2020-11-02T06:16:42Z"  
        }  
    },  
    "dateModified": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2020-12-27T15:13:17Z"  
        }  
    },  
    "description": {  
        "type": "Property",  
        "value": "Fare collection system Nize for regional routes"  
    },  
    "destinationStopCategory": {  
        "type": "Property",  
        "value": "Airport"  
    },  
    "destinationStopId": {  
        "type": "Property",  
        "value": "Nice-Airport"  
    },  
    "destinationStopName": {  
        "type": "Property",  
        "value": "Hour risk somebody deal system discussion other plan. Stage the film occur."  
    },  
    "direction_id": {  
        "type": "Property",  
        "value": 1  
    },  
    "entryAreaCode": {  
        "type": "Property",  
        "value": "city-bus-service"  
    },  
    "equipmentCompanyCode": {  
        "type": "Property",  
        "value": "103"  
    },  
    "equipmentId": {  
        "type": "Property",  
        "value": "S23"  
    },  
    "equipmentSequenceNumber": {  
        "type": "Property",  
        "value": 2  
    },  
    "equipmentStopId": {  
        "type": "Property",  
        "value": "BRTS-Sen-23"  
    },  
    "equipmentType": {  
        "type": "Property",  
        "value": "Entry sensor"  
    },  
    "equipmentTypeCode": {  
        "type": "Property",  
        "value": "42"  
    },  
    "exitAreaCode": {  
        "type": "Property",  
        "value": "city-bus-service"  
    },  
    "fareForAdult": {  
        "type": "Property",  
        "value": 4.5  
    },  
    "fareForChild": {  
        "type": "Property",  
        "value": 3.6  
    },  
    "location": {  
        "type": "Property",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                43.7034,  
                7.2663  
            ]  
        }  
    },  
    "name": {  
        "type": "Property",  
        "value": "Fare collection system Nize"  
    },  
    "observationDateTime": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "1988-12-24T07:06:19Z"  
        }  
    },  
    "occupancyLevel": {  
        "type": "Property",  
        "value": "Green"  
    },  
    "originDestinationCode": {  
        "type": "Property",  
        "value": "23"  
    },  
    "originStopCategory": {  
        "type": "Property",  
        "value": "Bus stop"  
    },  
    "originStopId": {  
        "type": "Property",  
        "value": "9"  
    },  
    "originStopName": {  
        "type": "Property",  
        "value": "Vauban"  
    },  
    "owner": {  
        "type": "Property",  
        "value": [  
            "urn:ngsi-ld:FareCollectionSystem:items:XMXR:79897582",  
            "urn:ngsi-ld:FareCollectionSystem:items:SKAX:98192518"  
        ]  
    },  
    "passengerCount": {  
        "type": "Property",  
        "value": 6  
    },  
    "route_id": {  
        "type": "Property",  
        "value": "4"  
    },  
    "seeAlso": {  
        "type": "Property",  
        "value": [  
            "urn:ngsi-ld:FareCollectionSystem:items:VSVS:72352464",  
            "urn:ngsi-ld:FareCollectionSystem:items:VMFR:36424993"  
        ]  
    },  
    "shiftOfOperation": {  
        "type": "Property",  
        "value": "2"  
    },  
    "source": {  
        "type": "Property",  
        "value": ""  
    },  
    "stage": {  
        "type": "Property",  
        "value": 4  
    },  
    "ticketTypeCode": {  
        "type": "Property",  
        "value": "Normal"  
    },  
    "transactionDateTime": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2021-08-20T15:45:22Z"  
        }  
    },  
    "transactionType": {  
        "type": "Property",  
        "value": "Issue"  
    },  
    "transactionTypeDescription": {  
        "type": "Property",  
        "value": "Regular Fare."  
    },  
    "transactionTypeId": {  
        "type": "Property",  
        "value": "2401"  
    },  
    "transactionVehicleNum": {  
        "type": "Property",  
        "value": 23  
    },  
    "travelDistance": {  
        "type": "Property",  
        "value": 7.5  
    },  
    "trip_id": {  
        "type": "Property",  
        "value": "4A"  
    },  
    "vehicle_label": {  
        "type": "Property",  
        "value": "5821JZS"  
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
参见[常见问题10](https://smartdatamodels.org/index.php/faqs/)，以获得关于如何处理量级单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
