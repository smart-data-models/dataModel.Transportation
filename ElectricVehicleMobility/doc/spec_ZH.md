<!-- 10-Header -->
  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

实体: ElectricVehicleMobility  
===============================
<!-- /10-Header -->
  
<!-- 15-License -->
  

[开放许可](https://github.com/smart-data-models//dataModel.Transportation/blob/master/ElectricVehicleMobility/LICENSE.md)  

[自动生成的文档](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->
  
<!-- 20-Description -->
  

Global description: **按位置、车辆品牌和地理区域汇总的电动汽车出行模式的日常观察。**  

version: 0.0.1  
<!-- /20-Description -->
  
<!-- 30-PropertiesList -->
  


## 财产清单  


<sup><sub>[*] 属性中没有类型是因为它可能有多种类型或不同的格式/模式</sub></sup>  
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)
	- `addressCountry[string]`: 国家。例如，西班牙  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 地点  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 行政區  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 区是一种行政区划，一些国家的区由地方政府管理。
	- `postOfficeBoxNumber[string]`: 邮政信箱地址的邮政信箱号码。例如，03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 邮政编码。例如：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 街道地址  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 街道编号
- `alternateName[string]`: 此条目的另一个名称
- `areaServed[string]`: 提供服务或所提供项目的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)
- `averageDistanceKm[number]`: 平均旅行距离（公里）  . Model: [https://schema.org/Number](https://schema.org/Number)
- `dataProvider[string]`: 统一数据实体的提供者  . Model: [https://schema.org/Text](https://schema.org/Text)
- `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配。
- `dateModified[date-time]`: 实体上一次修改的时间戳。通常由存储平台分配。
- `dateObserved[date]`: 观测日期（年-月-日）  . Model: [https://schema.org/Date](https://schema.org/Date)
- `description[string]`: 该商品的描述
- `deviceBrand[string]`: 电动车辆的品牌或制造商  . Model: [https://schema.org/Text](https://schema.org/Text)
- `district[string]`: 进行观测的地区  . Model: [https://schema.org/Text](https://schema.org/Text)
- `id[*]`: 实体的唯一标识符
- `location[*]`: 与该项目相关的Geojson引用，可以是Point、LineString、Polygon、MultiPoint、MultiLineString或MultiPolygon。
- `locationCode[string]`: 官方自治市代码  . Model: [https://schema.org/Text](https://schema.org/Text)
- `municipality[string]`: 进行观测的市区町村  . Model: [https://schema.org/Text](https://schema.org/Text)
- `n[number]`: 用于计算平均距离的观测值数量  . Model: [https://schema.org/Number](https://schema.org/Number)
- `name[string]`: 该物品的名称
- `owner[array]`: 包含一个 JSON 编码的字符序列，引用所有者（owner(s)）的唯一标识符（Id(s)）的列表。
- `region[string]`: 进行观测的区域  . Model: [https://schema.org/Text](https://schema.org/Text)
- `seeAlso[*]`: 指向关于该项目其他资源的 URI 列表
- `source[string]`: 数据来源的原始网址  . Model: [https://schema.org/Text](https://schema.org/Text)
- `type[string]`: NGSI 实体类型. 它必须是 ElectricVehicleMobility
- `vehicleType[string]`: 电动车辆类型  . Model: [https://schema.org/Text](https://schema.org/Text)
<!-- /30-PropertiesList -->
  
<!-- 35-RequiredProperties -->
  

必填属性  
- `id`  
- `type`  
<!-- /35-RequiredProperties -->
  
<!-- 40-NotesYaml -->
  
<!-- /40-NotesYaml -->
  
<!-- 50-DataModelHeader -->
  

## 属性的数据模型描述  

按字母顺序排列（点击了解详情）  
<!-- /50-DataModelHeader -->
  
<!-- 60-ModelYaml -->
  
<details><summary><strong>完整的yaml详情</strong></summary>    

```yaml  
ElectricVehicleMobility:    
  description: Daily observation of electric vehicle mobility patterns aggregated by location, vehicle brand, and geographic region.    
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
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    averageDistanceKm:    
      description: Average distance traveled in kilometers    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: kilometers    
    dataProvider:    
      description: Provider of the harmonised data entity    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
      description: Date of the observation (YYYY-MM-DD)    
      format: date    
      type: string    
      x-ngsi:    
        model: https://schema.org/Date    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    deviceBrand:    
      description: Brand or manufacturer of the electric vehicle    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    district:    
      description: District where the observation was made    
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
        type: Relationship    
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
    locationCode:    
      description: Official municipality code    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    municipality:    
      description: Municipality where the observation was made    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    n:    
      description: Number of observations used to calculate the average distance    
      minimum: 1    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
    region:    
      description: Region where the observation was made    
      enum:    
        - CONTINENTE    
        - AÇORES    
        - MADEIRA    
        - Outros - GDPR    
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
    source:    
      description: Original source of the data as a URL    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    type:    
      description: NGSI entity type. It has to be ElectricVehicleMobility    
      enum:    
        - ElectricVehicleMobility    
      type: string    
      x-ngsi:    
        type: Property    
    vehicleType:    
      description: Type of electric vehicle    
      enum:    
        - BEV    
        - PHEV    
        - HEV    
        - FCEV    
        - unknown    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms...    
  x-license-url: https://github.com/smart-data-models/dataModel.Transportation/blob/master/ElectricVehicleMobility/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Transportation/ElectricVehicleMobility/schema.json    
  x-model-tags: transportation,electricVehicle,mobility,statistics    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->
  
<!-- 70-MiddleNotes -->
  
<!-- /70-MiddleNotes -->
  
<!-- 80-Examples -->
  

## 示例载荷  

#### 電動車輛移動性NGSI-v2鍵值示例  

以下是一个以JSON-LD格式表示的 ElectricVehicleMobility 示例，以键值对形式呈现。当使用 `options=keyValues` 时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>显示/隐藏示例</strong></summary>    

```json  

{  
  "id": "urn:ngsi-ld:ElectricVehicleMobility:PT:OUTROS-GDPR:OUTROS-GDPR:20251215",  
  "type": "ElectricVehicleMobility",  
  "dateObserved": "2025-12-15",  
  "region": "Outros - GDPR",  
  "district": "Outros - GDPR",  
  "municipality": "Outros - GDPR",  
  "locationCode": "Outros - GDPR",  
  "deviceBrand": "Outros - GDPR",  
  "averageDistanceKm": "",  
  "n": 26  
}  
```  
</details>  

#### 电动车辆移动性 NGSI-v2 标准化示例  

以下是一个归一化的JSON-LD格式的ElectricVehicleMobility示例。当不使用选项时，此示例与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>显示/隐藏示例</strong></summary>    

```json  

{  
  "id": "urn:ngsi-ld:ElectricVehicleMobility:PT:OUTROS-GDPR:OUTROS-GDPR:20251215",  
  "type": "ElectricVehicleMobility",  
  "dateObserved": {  
    "type": "Date-Time",  
    "value": "2025-12-15"  
  },  
  "region": {  
    "type": "Text",  
    "value": "Outros - GDPR"  
  },  
  "district": {  
    "type": "Text",  
    "value": "Outros - GDPR"  
  },  
  "municipality": {  
    "type": "Text",  
    "value": "Outros - GDPR"  
  },  
  "locationCode": {  
    "type": "Text",  
    "value": "Outros - GDPR"  
  },  
  "deviceBrand": {  
    "type": "Text",  
    "value": "Outros - GDPR"  
  },  
  "averageDistanceKm": {  
    "type": "Text",  
    "value": ""  
  },  
  "n": {  
    "type": "Property",  
    "value": 26  
  }  
}  
```  
</details>  

#### 电动车辆移动性 NGSI-LD 键值示例  

以下是一个以JSON-LD格式表示的电动汽车出行的例子，以键值对形式呈现。当使用`options=keyValues`时，它与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>显示/隐藏示例</strong></summary>    

```json  

{  
  "id": "urn:ngsi-ld:ElectricVehicleMobility:PT:OUTROS-GDPR:OUTROS-GDPR:20251215",  
  "type": "ElectricVehicleMobility",  
  "dateObserved": "2025-12-15",  
  "region": "Outros - GDPR",  
  "district": "Outros - GDPR",  
  "municipality": "Outros - GDPR",  
  "locationCode": "Outros - GDPR",  
  "deviceBrand": "Outros - GDPR",  
  "averageDistanceKm": "",  
  "n": 26,  
  "@context": [  
    "https://smart-data-models.github.io/dataModel.Transportation/context.jsonld"  
  ]  
}  
```  
</details>  

#### 电动车辆移动性 NGSI-LD 标准化示例  

以下是一个归一化的JSON-LD格式的ElectricVehicleMobility示例。当不使用选项时，此示例与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>显示/隐藏示例</strong></summary>    

```json  

{  
  "id": "urn:ngsi-ld:ElectricVehicleMobility:PT:OUTROS-GDPR:OUTROS-GDPR:20251215",  
  "type": "ElectricVehicleMobility",  
  "dateObserved": {  
    "type": "Property",  
    "value": {  
      "@type": "Date",  
      "@value": "2025-12-15"  
    }  
  },  
  "region": {  
    "type": "Property",  
    "value": "Outros - GDPR"  
  },  
  "district": {  
    "type": "Property",  
    "value": "Outros - GDPR"  
  },  
  "municipality": {  
    "type": "Property",  
    "value": "Outros - GDPR"  
  },  
  "locationCode": {  
    "type": "Property",  
    "value": "Outros - GDPR"  
  },  
  "deviceBrand": {  
    "type": "Property",  
    "value": "Outros - GDPR"  
  },  
  "averageDistanceKm": {  
    "type": "Property",  
    "value": ""  
  },  
  "n": {  
    "type": "Property",  
    "value": 26  
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
  

参见[FAQ 10](https://smartdatamodels.org/index.php/faqs/)以获取有关如何处理量级单位的答案  
<!-- /95-Units -->
  
<!-- 97-LastFooter -->
  
---  

[智能数据模型](https://smartdatamodels.org) +++ [贡献指南](https://bit.ly/contribution_manual)  
  
