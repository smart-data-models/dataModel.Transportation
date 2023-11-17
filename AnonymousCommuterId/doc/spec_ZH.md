<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
实体：匿名通勤者 ID    
===========<!-- /10-Header -->    
<!-- 15-License -->    
[开放许可](https://github.com/smart-data-models//dataModel.Transportation/blob/master/AnonymousCommuterId/LICENSE.md)    
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
全局描述：**用于流量监控的匿名标识符。包括一个起点和终点属性，用于映射其路径。    
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
	- `streetNr[string]`: 标识公共街道上特定房产的编号      
- `algorithm[string]`: 用于匿名标识的算法名称  - `alternateName[string]`: 该项目的替代名称  - `anonymizedId[string]`: 匿名标识符  - `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `date[date-time]`: 检测到匿名标识符的日期  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `description[string]`: 项目描述  - `dest[string]`: 目标 ID 的字符串值，即检测到匿名 ID 的实际实体  - `id[*]`: 实体的唯一标识符  - `location[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `name[string]`: 该项目的名称  - `orig[string]`: 来源 ID 的字符串值，即检测到匿名 ID 的最后一个实体  - `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `source[string]`: 匿名通勤者 ID 来源的字符串值，例如（ALPR、人员监控、人脸识别等......）。  - `type[string]`: NGSI 实体类型。必须是 AnonymousCommuterId  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
所需属性    
- `anonymizedId`  - `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
这种模式的目的是在需要对某些 PII 进行跟踪时使用，因此需要对标识符进行匿名化处理，以便仍能提供一些有用的见解，但使用的是不可逆的匿名化（散列）函数。  通常情况下，都会提供标准化属性来指示检测的当前和先前位置。它们的目的是保存另一个实体 ID，因为检测器也以实体的形式复制，可以提供更好的数据建模体验。最后，还添加了一个算法属性，以帮助使用多种方式和方法对 PII 进行匿名化处理。    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## 属性的数据模型描述    
按字母顺序排列（点击查看详情）    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
AnonymousCommuterId:      
  description: Anonymized identifier for flow monitoring. Includes an origin and destiny property to map its path.      
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
    algorithm:      
      description: Name of the algorithm used to anonymize the Id      
      type: string      
      x-ngsi:      
        type: Property      
    alternateName:      
      description: An alternative name for this item      
      type: string      
      x-ngsi:      
        type: Property      
    anonymizedId:      
      description: Anonymized identifier      
      type: string      
      x-ngsi:      
        type: Property      
    areaServed:      
      description: The geographic area where a service or offered item is provided      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    dataProvider:      
      description: A sequence of characters identifying the provider of the harmonised data entity      
      type: string      
      x-ngsi:      
        type: Property      
    date:      
      description: Date of the detected anonymous identifier      
      format: date-time      
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
    description:      
      description: A description of this item      
      type: string      
      x-ngsi:      
        type: Property      
    dest:      
      description: 'String value of destination id, actual entity where the anonymous id was detected'      
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
    orig:      
      description: 'String value of origin id, last entity where the anonymous id was detected'      
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
          type: Property      
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
      description: 'String value of source of this AnonymousCommuterId, eg. (ALPR, People Monitoring, Face Recognition, etc...)'      
      type: string      
      x-ngsi:      
        type: Property      
    type:      
      description: NGSI entity type. It has to be AnonymousCommuterId      
      enum:      
        - AnonymousCommuterId      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - anonymizedId      
    - type      
  type: object      
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.Transportation/blob/master/AnonymousCommuterId/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.Transportation/AnonymousCommuterId/schema.json      
  x-model-tags: ""      
  x-version: 0.0.3      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## 有效载荷示例    
#### AnonymousCommuterId NGSI-v2 键值示例    
下面是一个以 JSON-LD 格式作为键值的 AnonymousCommuterId 示例。当使用 "options=keyValues "时，这与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "ngsi-ld:HUES:001",  
  "anonymizedId": "D20220AC3478565F",  
  "type": "AnonymousCommuterId",  
  "date": "2022-09-05T08:25:35.00Z",  
  "orig": "City hall",  
  "dest": "Library",  
  "source": "People Monitoring",  
  "algorithm": "SHA1",  
  "dateCreated": "2022-09-05T09:25:35.00Z",  
  "dateModified": "2022-09-12T09:25:35.00Z",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      43.23161118206764,  
      -2.844695196525928  
    ]  
  }  
}  
```  
</details>    
#### AnonymousCommuterId NGSI-v2 标准化示例    
下面是一个规范化 JSON-LD 格式的 AnonymousCommuterId 示例。在不使用选项的情况下，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "ngsi-ld:HUES:001",  
  "anonymizedId": {  
    "type": "Text",  
    "value": "D20220AC3478565F"  
  },  
  "type": "AnonymousCommuterId",  
  "orig": {  
    "type": "Text",  
    "value": "City hall"  
  },  
  "dest": {  
    "type": "Text",  
    "value": "Library"  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        43.23161118206764,  
        -2.844695196525928  
      ]  
    }  
  },  
  "date": {  
    "type": "DateTime",  
    "value": "2022-09-05T08:25:35.00Z"  
  },  
  "algorithm": {  
    "type": "Text",  
    "value": "SHA1"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2022-09-05T09:25:35.00Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2022-09-12T09:25:35.00Z"  
  }  
}  
```  
</details>    
#### AnonymousCommuterId NGSI-LD 键值示例    
下面是一个以 JSON-LD 格式作为键值的 AnonymousCommuterId 示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "ngsi-ld:HUES:001",  
  "anonymizedId": "D20220AC3478565F",  
  "type": "AnonymousCommuterId",  
  "date": "2022-09-05T08:25:35.00Z",  
  "orig": "City hall",  
  "dest": "Library",  
  "source": "People Monitoring",  
  "algorithm": "SHA1",  
  "dateCreated": "2022-09-05T09:25:35.00Z",  
  "dateModified": "2022-09-12T09:25:35.00Z",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      43.23161118206764,  
      -2.844695196525928  
    ]  
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Transportation/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### AnonymousCommuterId NGSI-LD 标准化示例    
下面是一个以 JSON-LD 格式规范化的 AnonymousCommuterId 示例。在不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
    "id": "ngsi-ld:HUES:001",  
    "anonymizedId": {  
        "type": "Property",  
        "value": "D20220AC3478565F"  
    },  
    "type": "AnonymousCommuterId",  
    "orig": {  
        "type": "Property",  
        "value": "City hall"  
    },  
    "dest": {  
        "type": "Property",  
        "value": "Library"  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                43.23161118206764,  
                -2.844695196525928  
            ]  
        }  
    },  
    "date": {  
        "type": "Property",  
        "value": "2022-09-05T08:25:35.00Z"  
    },  
    "algorithm": {  
        "type": "Property",  
        "value": "SHA1"  
    },  
    "dateCreated": {  
        "type": "Property",  
        "value": "2022-09-05T09:25:35.00Z"  
    },  
    "dateModified": {  
        "type": "Property",  
        "value": "2022-09-12T09:25:35.00Z"  
    },  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Transportation/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->    
<!-- 90-FooterNotes -->    
该模型由 Purple Blob S.L. 提供，并根据我们的 METIS 匿名人流产品的观点和需要进行了调整。我们对开发可广泛使用的 AnonymousCommuterId 互操作数据模型持开放态度，因此，请随时联系 adelgado@purpleblob.net 或 iruiz@purpleblob.net 以进行更多讨论，或者最好是在 Github 上发布问题！    
<!-- /90-FooterNotes -->    
<!-- 95-Units -->    
请参阅 [FAQ 10](https://smartdatamodels.org/index.php/faqs/)，获取如何处理幅度单位的答案。    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
