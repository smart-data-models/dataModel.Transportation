<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：观察到的安普尔流量（AnprFlowObserved  
=============================<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.Transportation/blob/master/AnprFlowObserved/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全局描述：**该数据模型表示与某一地点和某一时间的车辆通过有关的观察。该数据模型基于[dataModel.Transportation/ItemFlowObserved]，用ANPR的特定属性和观察图像的链接来扩展。  
版本：  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

##属性列表  

<sup><sub>[*] 如果一个属性中没有一个类型，是因为它可能有几种类型或不同的格式/模式</sub></sup>。  
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: 这个项目的一个替代名称  - `areaServed[string]`: 提供服务或提供项目的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 一串识别统一数据实体提供者的字符。  - `dateCreated[string]`: 实体创建时间戳。这通常会由存储平台分配。  - `dateModified[string]`: 实体最后一次修改的时间戳。这通常会由存储平台分配。  - `dateObserved[string]`: 由用户定义的被观察实体的日期。  - `dateReceived[string]`: 属性。平台收到观察结果的时间戳。  - `description[string]`: 对这个项目的描述  - `id[*]`: 实体的唯一标识符  - `laneId[string]`: 属性。车道标识符。由观察者提供的车道标识。  - `location[*]`: 对该项目的Geojson引用。它可以是点、线字符串、多边形、多点、多线字符串或多多边形。  - `name[string]`: 这个项目的名称。  - `observedBy[*]`: 关系。报告这一观察结果的实体或设备  - `observedVehicle[object]`: 财产。关于观察到的车辆的信息。  - `owner[array]`: 一个包含JSON编码的字符序列的列表，引用所有者的唯一Ids。  - `refImages[array]`: 关系。指向图像的多个对象的阵列。  - `seeAlso[*]`: 指向有关该项目的其他资源的URI列表  - `source[string]`: 一系列的字符，以URL的形式给出实体数据的原始来源。建议为源提供者的完全合格域名，或源对象的URL。  - `type[string]`: 属性。NGSI实体类型。它必须是AnprFlowObserved  - `vehiclePlateNotRead[boolean]`: 属性。指示是否无法读取许可证  - `zonesServed[array]`: 能够接收或读取观察结果的区域阵列  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `dateObserved`  - `id`  - `location`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
该数据模型描述了与处理警察问题的智能应用有关的主要实体。这组实体主要与汽车和智能城市垂直细分市场以及相关的物联网应用有关。在可行的情况下，对现有schema.org实体类型和属性的引用也包括在内。该模型已被设计为尽可能的通用，从而允许不同的警察部门和区域使用，如ANPR、轨迹控制和警车。  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 数据模型的属性描述  
按字母顺序排列（点击查看详情）。  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
AnprFlowObserved:    
  description: 'The data model represents an observation linked to the passing of a vehicle at a certain location and at a given time. This Data Model is based on the [dataModel.Transportation/ItemFlowObserved], extended with ANPR specific properties and links to the observation images.'    
  properties:    
    address:    
      description: The mailing address    
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
        district:    
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government.'    
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
        streetNr:    
          description: Number identifying a specific property on a public street.    
          type: string    
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
    dataProvider:    
      description: A sequence of characters identifying the provider of the harmonised data entity.    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: Entity creation timestamp. This will usually be allocated by the storage platform.    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateObserved:    
      description: Date of the observed entity defined by the user.    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateReceived:    
      description: Property. Timestamp when the observation has been received by the platform.    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &anprflowobserved_-_properties_-_owner_-_items_-_anyof    
        - description: Property. Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: Property. Identifier format of any NGSI entity    
          format: uri    
          type: string    
      description: Unique identifier of the entity    
      x-ngsi:    
        type: Property    
    laneId:    
      description: Property. Lane identifier. Lane identification provided by the observer.    
      type: string    
      x-ngsi:    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf: &anprflowobserved_-_properties_-_observedvehicle_-_properties_-_licenseplate_-_properties_-_coordinates_-_oneof    
        - description: GeoProperty. Geojson reference to the item. Point    
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
        - description: GeoProperty. Geojson reference to the item. LineString    
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
        - description: GeoProperty. Geojson reference to the item. Polygon    
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
        - description: GeoProperty. Geojson reference to the item. MultiPoint    
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
        - description: GeoProperty. Geojson reference to the item. MultiLineString    
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
        - description: GeoProperty. Geojson reference to the item. MultiLineString    
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
    name:    
      description: The name of this item.    
      type: string    
      x-ngsi:    
        type: Property    
    observedBy:    
      anyOf:    
        - description: Property. Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: Property. Identifier format of any NGSI entity    
          format: uri    
          type: string    
      description: Relationship. The entity or device which has reported this observation    
      x-ngsi:    
        type: Relationship    
    observedVehicle:    
      description: Property. Information about the observed vehicle.    
      properties:    
        brand:    
          description: Property. Detected brand of the observed vehicle.    
          properties:    
            confidence:    
              description: Property. Confidence level of the detection    
              maximum: 1    
              minimum: 0    
              type: number    
            name:    
              description: Property. Brand name identified    
              type: string    
          type: object    
        color:    
          description: Property. Detected color of the observed vehicle.    
          properties:    
            confidence:    
              description: Property. Confidence level of the detection.    
              maximum: 1    
              minimum: 0    
              type: number    
            name:    
              description: Property. Color name.    
              type: string    
          type: object    
        country:    
          description: Property. Detected country of the observed vehicle.    
          properties:    
            code:    
              description: Property. Country code according to ISO 3166-1 alpha-2    
              type: string    
            confidence:    
              description: Property. Confidence level of the detection.    
              maximum: 1    
              minimum: 0    
              type: number    
          type: object    
        direction:    
          description: Property. Detected direction of the observed vehicle.    
          enum:    
            - away    
            - towards    
          type: string    
        licensePlate:    
          description: Property. Detected license plate of the observed vehicle.    
          properties:    
            confidence:    
              description: Property. Confidence level of the detection.    
              maximum: 1    
              minimum: 0    
              type: number    
            coordinates:    
              description: 'GeoProperty. Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
              oneOf: *anprflowobserved_-_properties_-_observedvehicle_-_properties_-_licenseplate_-_properties_-_coordinates_-_oneof    
            identifier:    
              description: Property. License plate identifier    
              type: string    
          required:    
            - identifier    
          type: object    
        model:    
          description: Property. Detected brand model of the observed vehicle.    
          properties:    
            confidence:    
              description: Property. Confidence level of the detection.    
              maximum: 1    
              minimum: 0    
              type: number    
            name:    
              description: Property. Model name.    
              type: string    
          type: object    
        speed:    
          description: Property. Detected speed of the observed vehicle.    
          minimum: 0    
          type: number    
      type: object    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf: *anprflowobserved_-_properties_-_owner_-_items_-_anyof    
        description: Property. Unique identifier of the entity    
      type: array    
      x-ngsi:    
        type: Property    
    refImages:    
      description: Relationship. Array of multiple objects that refer to images.    
      items:    
        - properties:    
            contentType:    
              description: Property. Content type according to IANA Media Types.    
              type: string    
            imageType:    
              description: Property. Type of image    
              enum:    
                - plate    
                - overview    
                - anpr    
              type: string    
            url:    
              description: Property. URL referencing to the image    
              format: uri    
              type: string    
          required:    
            - url    
            - contentType    
            - imageType    
          type: object    
      type: array    
      x-ngsi:    
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: Property. NGSI Entity type. It has to be AnprFlowObserved    
      enum:    
        - AnprFlowObserved    
      type: string    
      x-ngsi:    
        type: Property    
    vehiclePlateNotRead:    
      description: Property. Indicates if a license could not be read    
      type: boolean    
      x-ngsi:    
        type: Property    
    zonesServed:    
      description: Array of zones that are able to receive or read the observations    
      items:    
        type: string    
      type: array    
  required:    
    - id    
    - type    
    - location    
    - dateObserved    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Transportation/blob/master/AnprFlowObserved/LICENSE.md    
  x-model-schema: https://gitlab.inuits.io/tom.vda/dataModel.Police/AnprFlowObserved/schema.json    
  x-model-tags: ""    
  x-version: ""    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ＃＃＃＃有效载荷的例子  
#### AnprFlowObserved NGSI-v2 key-values 示例  
这里是一个以JSON-LD格式作为key-values的AnprFlowObserved的例子。当使用`options=keyValues`时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "anprFlowObserved:LEZ-Noorderlaan",  
  "type": "AnprFlowObserved",  
  "address": {  
    "addressCountry": "BE",  
    "addressLocality": "Antwerp",  
    "streetAddress": "Noorderlaan"  
  },  
  "dateObserved": "2022-09-01T16:30:00Z",  
  "dateReceived": "2022-09-01T16:35:00Z",  
  "observedBy": "ANPR1_Noorderlaan",  
  "laneId": "ABC123",  
  "areaServed":"Antwerp",  
  "zonesServed": [  
      "Antwerp"  
    ],  
  "vehiclePlateNotRead": false,  
  "observedVehicle": {  
    "direction": "towards",  
    "speed": 50,  
    "brand":{  
      "name": "Audi",  
      "confidence": 0.97  
    },  
    "model":{  
      "name": "A3",  
      "confidence": 0.98  
    },  
    "color":{  
      "name": "black",  
      "confidence": 0.95  
    },  
    "country":{  
      "code": "BE",  
      "confidence":0.95  
    },  
    "licensePlate":{  
      "identifier": "1-ABC-123",  
      "confidence": 0.96  
    }   
  },  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -56.6404505,  
      168.370658  
    ]  
  },  
  "refImages":[  
    {  
      "contentType": "image/jpg",  
      "imageType": "anpr",  
      "url": "urn:ngsi-ld:ANPR:items:123"  
    }  
  ]  
}  
```  
</details>  
#### AnprFlowObserved NGSI-v2 normalized 示例  
下面是一个以JSON-LD格式规范化的AnprFlowObserved的例子。当不使用选项时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "anprFlowObserved:LEZ-Noorderlaan",  
  "type": "AnprFlowObserved",  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "addressCountry": "BE",  
      "addressLocality": "Antwerp",  
      "streetAddress": "Noorderlaan"  
    }  
  },  
  "dateObserved": {  
    "type": "DateTime",  
    "@value": "2022-09-01T16:30:00Z"  
  },  
  "laneId": {  
    "type": "Text",  
    "value": "ABC123"  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Antwerp"  
  },  
  "zonesServed": {  
    "type": "StructuredValue",  
    "value": {  
      "type": "string",  
      "coordinates": [  
        "Antwerp"  
      ]  
    }  
  },  
  "vehiclePlateNotRead": {  
    "type": "Boolean",  
    "value": false  
  },  
  "observedVehicle": {  
    "type": "StructuredValue",  
    "value": {  
      "direction": "towards",  
      "speed": 50,  
      "brand": "Audi",  
      "model": "A3",  
      "color": "black",  
      "country": "BE",  
      "licensePlate": "1-ABC-123"  
    }  
  },  
  "refImages": {  
    "type": "StructuredValue",  
    "value": {  
      "type": "s3://bucket/object-xxx-plate",  
      "contentType": "image/jpg",  
      "imageType": "anpr"  
    }  
  }  
}  
```  
</details>  
#### AnprFlowObserved NGSI-LD key-values 示例  
这里是一个以JSON-LD格式作为key-values的AnprFlowObserved的例子。当使用`options=keyValues`时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "anprFlowObserved:LEZ-Noorderlaan",  
  "type": "AnprFlowObserved",  
  "address": {  
    "addressCountry": "BE",  
    "addressLocality": "Antwerp",  
    "streetAddress": "Noorderlaan"  
  },  
  "dateObserved": "2022-09-01T16:30:00Z",  
  "dateReceived": "2022-09-01T16:35:00Z",  
  "observedBy": "ANPR1_Noorderlaan",  
  "laneId": "ABC123",  
  "areaServed":"Antwerp",  
  "zonesServed": [  
      "Antwerp"  
    ],  
  "vehiclePlateNotRead": false,  
  "observedVehicle": {  
    "direction": "towards",  
    "speed": 50,  
    "brand":{  
      "name": "Audi",  
      "confidence": 0.97  
    },  
    "model":{  
      "name": "A3",  
      "confidence": 0.98  
    },  
    "color":{  
      "name": "black",  
      "confidence": 0.95  
    },  
    "country":{  
      "code": "BE",  
      "confidence":0.95  
    },  
    "licensePlate":{  
      "identifier": "1-ABC-123",  
      "confidence": 0.96  
    }   
  },  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -56.6404505,  
      168.370658  
    ]  
  },  
  "refImages":[  
    {  
      "contentType": "image/jpg",  
      "imageType": "anpr",  
      "url": "urn:ngsi-ld:ANPR:items:123"  
    }  
  ],  
    "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Transportation/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### AnprFlowObserved NGSI-LD归一化实例  
这里是一个以JSON-LD格式规范化的AnprFlowObserved的例子。当不使用选项时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "anprFlowObserved:LEZ-Noorderlaan",  
  "type": "AnprFlowObserved",  
  "address": {  
    "type": "Property",  
    "value": {  
      "addressCountry": "BE",  
      "addressLocality": "Antwerp",  
      "streetAddress": "Noorderlaan"  
    }  
  },  
  "dateObserved": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2022-09-01T16:30:00Z"  
    }  
  },  
  "laneId": {  
    "type": "Property",  
    "value": "ABC123"  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Antwerp"  
  },  
  "zonesServed": {  
    "type": "Property",  
    "value": {  
      "type": "string",  
      "coordinates": [  
        "Antwerp"  
      ]  
    }  
  },  
  "vehiclePlateNotRead": {  
    "type": "Property",  
    "value": false  
  },  
  "observedVehicle": {  
    "type": "Property",  
    "value": {  
      "direction": "towards",  
      "speed": 50,  
      "brand": "Audi",  
      "model": "A3",  
      "color": "black",  
      "country": "BE",  
      "licensePlate": "1-ABC-123"  
    }  
  },  
  "refImages": {  
    "type": "Property",  
    "value": {  
      "type": "s3://bucket/object-xxx-plate",  
      "contentType": "image/jpg",  
      "imageType": "anpr"  
    }  
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
