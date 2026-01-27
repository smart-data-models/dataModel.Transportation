<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
 电动车移动性实体  
===============================<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可证](https://github.com/smart-data-models//dataModel.Transportation/blob/master/ElectricVehicleMobility/LICENSE.md)  
[自动生成的文档](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
 全局描述：**按位置、车辆品牌和地理区域聚合的电动汽车移动模式的每日观察。**  
 版本：0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

 ## 属性列表  

<sup><sub>如果一个属性中没有指定类型，那是因为它可能有多种类型或不同的格式/模式</sub></sup>  
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: The country. For example, Spain  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 该街道地址所在的地区，以及该地区所在的区域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 该地所在的地区，也是位于该国的地区  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 区是某些国家的一种行政区划，由当地政府管理
	- `postOfficeBoxNumber[string]`: 邮政信箱号码用于邮政信箱地址。例如，03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 邮政编码。例如，24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 街道地址  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 公共街道上特定房产的识别号码
- `alternateName[string]`: 该项目的另一个名称 
- `areaServed[string]`：提供服务或提供的项目的的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `averageDistanceKm[number]`: Average distance traveled in kilometers  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: Provider of the harmonised data entity  . Model: [https://schema.org/Text](https://schema.org/Text)- `dateCreated[date-time]`: Entity creation timestamp. This will usually be allocated by the storage platform  - `dateModified[date-time]`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform  - `dateObserved[date]`: Date of the observation (YYYY-MM-DD)  . Model: [https://schema.org/Date](https://schema.org/Date)- `description[string]`: A description of this item  - `deviceBrand[string]`: Brand or manufacturer of the electric vehicle  . Model: [https://schema.org/Text](https://schema.org/Text)- `district[string]`: District where the observation was made  . Model: [https://schema.org/Text](https://schema.org/Text)- `id[*]`: Unique identifier of the entity  - `location[*]`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `locationCode[string]`: Official municipality code  . Model: [https://schema.org/Text](https://schema.org/Text)- `municipality[string]`: Municipality where the observation was made  . Model: [https://schema.org/Text](https://schema.org/Text)- `n[number]`: Number of observations used to calculate the average distance  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: The name of this item  - `owner[array]`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `region[string]`: Region where the observation was made  . Model: [https://schema.org/Text](https://schema.org/Text)- `seeAlso[*]`: list of uri pointing to additional resources about the item  - `source[string]`: Original source of the data as a URL  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: NGSI entity type. It has to be ElectricVehicleMobility  - `vehicleType[string]`: Type of electric vehicle  . Model: [https://schema.org/Text](https://schema.org/Text)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必需属性  
- `id`   
- `type`   
<!-- /35-RequiredProperties --> 

- `id`   
- `类型`   
<!-- /35-必需属性 -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
 ## 数据模型属性描述  
按字母顺序排列（点击查看详细信息）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>完整的YAML详细信息</strong></summary>    
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
 示例有效载荷  
 电动车辆移动性NGSI-v2键值示例  
 这是一个以JSON-LD格式表示的ElectricVehicleMobility示例，以键值对的形式给出。当使用`options=keyValues`时，它与NGSI-v2兼容，并返回个体实体的上下文数据。  
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
 电动车辆移动性NGSI-v2标准化示例  
 这是一个电动车移动性（ElectricVehicleMobility）的JSON-LD格式示例，已标准化。当不使用选项时，它与NGSI-v2兼容，并返回单个实体的上下文数据。  
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
 电动车辆移动性NGSI-LD关键值示例  
 这是一个以JSON-LD格式表示的ElectricVehicleMobility的例子，以键值对的形式给出。当使用`options=keyValues`时，它与NGSI-LD兼容，并返回个体实体的上下文数据。  
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
 电动车辆移动性NGSI-LD标准化示例  
 这是一个电动车移动性的JSON-LD格式的例子，已经标准化。这与NGSI-LD兼容，当不使用选项时，返回单个实体的上下文数据。  
<details><summary><strong>顯示/隱藏範例</strong></summary>    
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
 参见 [FAQ 10](https://smartdatamodels.org/index.php/faqs/) 以了解如何处理量级单位的问题答案  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[智能数据模型](https://smartdatamodels.org) +++ [贡献手册](https://bit.ly/contribution_manual)  
