<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：CrowdFlowObserved  
====================<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.Transportation/blob/master/CrowdFlowObserved/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全局描述：**观察到的人群流量**  
版本： 0.0.2  
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
- `alternateName[string]`: 该项目的替代名称  - `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `averageCrowdSpeed[number]`: 观测期间过境人群的平均速度  . Model: [https://schema.org/Number](https://schema.org/Number)- `averageHeadwayTime[number]`: 平均航程时间。前行时间是指  
    是指两个连续的人  . Model: [https://schema.org/Number](https://schema.org/Number)- `congested[boolean]`: 标志着在观察期间，所指人行道上是否有人群拥挤现象。没有该属性表示没有人群拥堵  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `dateObserved[string]`: 以 ISO8601 UTC 格式表示的观测日期和时间。它可以用一个特定的时间瞬间或一个 ISO8601 时间间隔来表示。由于 Orion Context Broker 不支持日期时间间隔，因此可以使用两个不同的属性：日期观测自 "和 "日期观测至  . Model: [https://schema.org/URL](https://schema.org/URL)- `dateObservedFrom[date-time]`: 观察期开始日期和时间。参见 `dateObserved` 。  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateObservedTo[date-time]`: 观察期结束日期和时间。请参阅 "观察日期"。  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `description[string]`: 项目描述  - `direction[string]`: 该观测点所指人行道相对于市中心的通常行进方向。枚举："入境、出境  . Model: [https://schema.org/Text](https://schema.org/Text)- `id[*]`: 实体的唯一标识符  - `location[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `name[string]`: 该项目的名称  - `occupancy[number]`: 有人占用被观测人行道的观测时间比例  . Model: [https://schema.org/Number)](https://schema.org/Number))- `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `peopleCount[number]`: 本次观测中发现的总人数  - `refRoadSegment[*]`: 观测所涉及的路段  . Model: [https://schema.org/URL](https://schema.org/URL)- `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `type[string]`: NGSI 实体类型。必须是 CrowdFlowObserved  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `dateObserved`  - `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
与某一地点和时间的人员流动有关的观察。  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 属性的数据模型描述  
按字母顺序排列（点击查看详情）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
CrowdFlowObserved:    
  description: CrowdFlowObserved    
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
    averageCrowdSpeed:    
      description: Average speed of the crowd transiting during the observation period    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Kilometer per hour (Km/h).    
    averageHeadwayTime:    
      description: |-    
        Average headway time. Headway time is the time    
            elapsed between two consecutive persons    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: second (s)    
    congested:    
      description: Flags whether there was a crowd congestion during the observation period in the referred walkway. The absence of this attribute means no crowd congestion    
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
      description: 'The date and time of this observation in ISO8601 UTC format. It can be represented by an specific time instant or by an ISO8601 interval. As a workaround for the lack of support of Orion Context Broker for datetime intervals, it can be used two separate attributes: `dateObservedFrom`, `dateObservedTo`'    
      type: string    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Property    
    dateObservedFrom:    
      description: Observation period start date and time. See `dateObserved`    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    dateObservedTo:    
      description: Observation period end date and time. See `dateObserved`.    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    direction:    
      description: 'Usual direction of travel in the walkway referred by this observation with respect to the city center. Enum:''inbound, outbound'''    
      enum:    
        - inbound    
        - outbound    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
      description: Fraction of the observation time where a person has been occupying the observed walkway    
      maximum: 1    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number)    
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
    peopleCount:    
      description: Total number of people detected during this observation    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    refRoadSegment:    
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
      description: Concerned road segment on which the observation has been made    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Relationship    
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
      description: NGSI Entity type. It has to be CrowdFlowObserved    
      enum:    
        - CrowdFlowObserved    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - dateObserved    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Transportation/blob/master/CrowdFlowObserved/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Transportation/CrowdFlowObserved/schema.json    
  x-model-tags: ""    
  x-version: 0.0.2    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 有效载荷示例  
#### CrowdFlowObserved NGSI-v2 key-values 示例  
下面是一个以 JSON-LD 格式作为键值的 CrowdFlowObserved 示例。当使用 `options=keyValues` 时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:CrowdFlowObserved:Valladolid_1",  
  "type": "CrowdFlowObserved",  
  "dateObserved": "2018-08-07T11:10:00/2018-08-07T11:15:00",  
  "dateObservedFrom": "2018-08-07T11:10:00Z",  
  "dateObservedTo": "2018-08-07T11:15:00Z",  
  "peopleCount": 100,  
  "averageHeadwayTime": 5,  
  "congested": false,  
  "direction": "inbound",  
  "location": {  
    "type": "LineString",  
    "coordinates": [  
      [-4.73735395519672, 41.6538181849672],  
      [-4.73414858659993, 41.6600594193478],  
      [-4.73447575302641, 41.659585195093]  
    ]  
  }  
}  
```  
</details>  
#### CrowdFlowObserved NGSI-v2 归一化示例  
下面是一个 CrowdFlowObserved 的示例，格式为规范化的 JSON-LD。当不使用选项时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:CrowdFlowObserved:Valladolid_1",  
  "type": "CrowdFlowObserved",  
  "dateObserved": {  
    "value": "2018-08-07T11:10:00/2018-08-07T11:15:00"  
  },  
  "direction": {  
    "value": "inbound"  
  },  
  "dateObservedFrom": {  
    "type": "DateTime",  
    "value": "2018-08-07T11:10:00Z"  
  },  
  "peopleCount": {  
    "value": 100  
  },  
  "averageHeadwayTime": {  
    "value": 5  
  },  
  "dateObservedTo": {  
    "type": "DateTime",  
    "value": "2018-08-07T11:15:00Z"  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "LineString",  
      "coordinates": [  
        [-4.73735395519672, 41.6538181849672],  
        [-4.73414858659993, 41.6600594193478],  
        [-4.73447575302641, 41.659585195093]  
      ]  
    }  
  },  
  "congested": {  
    "value": false  
  }  
}  
```  
</details>  
#### CrowdFlowObserved NGSI-LD key-values 示例  
下面是一个以 JSON-LD 格式作为键值的 CrowdFlowObserved 示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:CrowdFlowObserved:Valladolid_1",  
  "type": "CrowdFlowObserved",  
  "averageHeadwayTime": 5,  
  "congested": false,  
  "dateObservedFrom": "2018-08-07T11:10:00Z",  
  "dateObservedTo": "2018-08-07T11:15:00Z",  
  "direction": "inbound",  
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
  "peopleCount": 100,  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Transportation/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### CrowdFlowObserved NGSI-LD normalized 示例  
下面是一个 CrowdFlowObserved 的示例，格式为规范化的 JSON-LD。在不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:CrowdFlowObserved:Valladolid_1",  
  "type": "CrowdFlowObserved",  
  "averageHeadwayTime": {  
    "type": "Property",  
    "value": 5  
  },  
  "congested": {  
    "type": "Property",  
    "value": false  
  },  
  "dateObserved": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2018-08-07T11:10:00"  
    }  
  },  
  "dateObservedFrom": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2018-08-07T11:10:00Z"  
    }  
  },  
  "dateObservedTo": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2018-08-07T11:15:00Z"  
    }  
  },  
  "direction": {  
    "type": "Property",  
    "value": "inbound"  
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
  "peopleCount": {  
    "type": "Property",  
    "value": 100  
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
