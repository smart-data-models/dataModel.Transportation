<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティ車両状態  
==========<!-- /10-Header -->  
<!-- 15-License -->  
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.Transportation/blob/master/FleetVehicleStatus/LICENSE.md)  
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述：**このエンティティには、一般的な車両の状態に関する調和された記述が含まれる。このエンティティは、主に輸送・物流の垂直セグメントに関連するが、他の多くの関連 IoT アプリケーションにも使用できる。  
バージョン: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティのリスト  

<sup><sub>[*] 属性に型がない場合は、複数の型があるか、異なるフォーマット/パターンがある可能性があるためです</sub></sup>。  
- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: この項目の別名  - `areaServed[string]`: サービスまたは提供品が提供される地理的地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `bearing[number]`: フリート車両の現在の方位を北に対する度数で示す。属性のtimestamp要素は、その読みがいつ取得されたかを示すべきである。  - `currentOperative[object]`: Schema.orgの人物として記述されている車両の現在の操作者（運転手など）。  . Model: [https://schema.org/Person](https://schema.org/Person)- `currentStatus[string]`: 車両の現在のステータスの説明。例えば、Enum:'deployed, finished, terminated, servicing, starting'.  - `dataProvider[string]`: 整合データ・エンティティの提供者を識別する一連の文字。  - `dateCreated[string]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateModified[string]`: エンティティの最終変更のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: この商品の説明  - `fleetVehicle[*]`: この状態エンティティが関連する FleetVehicle エンティティへの参照。  - `fleetVehicleOperation[*]`: この状態エンティティが関連する FleetVehicleOperation エンティティへの参照。  - `id[*]`: エンティティの一意識別子  - `inRestrictedArea[boolean]`: ステータス更新時に車両が制限区域内にあることが判明しているかどうかを示す。  - `lastFuellingAmount[number]`: 最後の給油時に車両に追加された燃料のレベル。属性のタイムスタンプ要素は、車両がいつ給油されたかを示すこと。記録されるデータ単位：リットル  - `lastKnownPosition[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。  - `lastKnownPositionUpdatedAt[string]`: フリート車両の最後の既知の位置更新のタイムスタンプ。  - `location[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。  - `mileageFromOdometer[number]`: 車両に搭載されたオドメーターによる総走行距離をキロメートル（unitCode KMT）またはマイル（unitCode SMI）で表したもの。Schema.org Vehicle/ mileageFromOdometer も参照。timestamp 要素は、走行距離計の測定日時を記録する。  - `name[string]`: このアイテムの名前。  - `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリスト。  - `restFuelAmount[number]`: 車両が最後に静止（すなわち停止）したときに記録された燃料レベル。属性のタイムスタンプ要素は、車両が最後に停止した時刻を示す。リッター単位で記録されるデータ。  - `seeAlso[*]`: アイテムに関する追加リソースを指すURIのリスト  - `source[string]`: エンティティ・データの元のソースを URL として示す一連の文字。ソース・プロバイダの完全修飾ドメイン名、またはソース・オブジェクトの URL を推奨します。  - `speed[number]`: フリート車両の現在の速度（km/h）。属性のタイムスタンプ要素は、読み取り値がいつ取得されたかを示す必要があります。  - `type[string]`: NGSI エンティティ識別子。これは FleetVehicleStatus でなければならない。  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必須プロパティ  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
このデータ・モデルはGSMA IoTプロジェクト（https://www.gsma.com/iot/iot-big-data/）に由来する。スマート・データ・モデルの要件を満たすために、若干の修正が加えられている。  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順（クリックで詳細表示）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
FleetVehicleStatus:    
  description: This entity contains a harmonised description of the status of a generic fleet vehicle. This entity is primarily associated with the vertical segment of the transport and logistics but may also be used many other related IoT applications.    
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
    bearing:    
      description: The current bearing of the fleet vehicle in degrees relative to North. The timestamp element of the attribute should indicate when the reading was obtained.    
      type: number    
      x-ngsi:    
        type: Property    
    currentOperative:    
      description: The current operative (e.g. driver) of the vehicle described as a Schema.org  person    
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
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    fleetVehicle:    
      anyOf:    
        - description: Property. Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: Property. Identifier format of any NGSI entity    
          format: uri    
          type: string    
      description: Reference to the FleetVehicle entity to which this status entity relates.    
      x-ngsi:    
        type: Relationship    
    fleetVehicleOperation:    
      anyOf:    
        - description: Property. Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: Property. Identifier format of any NGSI entity    
          format: uri    
          type: string    
      description: Reference to the FleetVehicleOperation entity to which this status entity relates.    
      x-ngsi:    
        type: Relationship    
    id:    
      anyOf: &fleetvehiclestatus_-_properties_-_owner_-_items_-_anyof    
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
    inRestrictedArea:    
      description: Indicates if the vehicle is known to be in a restricted area at the time of the status update.    
      type: boolean    
      x-ngsi:    
        type: Property    
    lastFuellingAmount:    
      description: The level of fuel added to the vehicle at the last fuelling. The timestamp element of the attribute should indicate when the vehicle was fuelled. Data to be recorded in Litres    
      type: number    
      x-ngsi:    
        type: Property    
        units: litres    
    lastKnownPosition:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf: &fleetvehiclestatus_-_properties_-_location_-_oneof    
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
    lastKnownPositionUpdatedAt:    
      description: The timestamp of the last known position update for the fleet vehicle.    
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
      description: The total distance the fleet vehicle has travelled according to the on-board odometer in kilometres (unitCode KMT) or miles (unitCode SMI). See also Schema.org Vehicle/ mileageFromOdometer. The timestamp element records when the odometer reading was taken.    
      type: number    
      x-ngsi:    
        type: Property    
    name:    
      description: The name of this item.    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf: *fleetvehiclestatus_-_properties_-_owner_-_items_-_anyof    
        description: Property. Unique identifier of the entity    
      type: array    
      x-ngsi:    
        type: Property    
    restFuelAmount:    
      description: The level of fuel recorded when the vehicle was last at rest (i.e. stopped). The timestamp element of the attribute should indicate when the vehicle was last at rest. Data to be recorded in Litres.    
      type: number    
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    speed:    
      description: The current speed of the fleet vehicle (km/h). The timestamp element of the attribute should indicate when the reading was obtained    
      type: number    
      x-ngsi:    
        type: Property    
        units: km/h    
    type:    
      description: NGSI Entity identifier. It has to be FleetVehicleStatus    
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
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
## ペイロードの例  
#### FleetVehicleStatus NGSI-v2 キー値の例  
以下はFleetVehicleStatusをJSON-LD形式でkey-valuesとした例である。これはNGSI-v2と互換性があり、`options=keyValues`を使用すると個々のエンティティのコンテキストデータを返す。  
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
#### 車両状態 NGSI-v2 正規化例  
以下は、正規化された JSON-LD 形式の FleetVehicleStatus の例である。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### FleetVehicleStatus NGSI-LD キー値の例  
以下はFleetVehicleStatusをJSON-LD形式でkey-valuesとした例である。これは NGSI-LD と互換性があり、`options=keyValues` を使用すると個々のエンティティのコンテキストデータを返す。  
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
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Transportation/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### 車両状態 NGSI-LD 正規化例  
以下は、正規化された JSON-LD 形式の FleetVehicleStatus の例である。これは、オプションを使用しない場合はNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
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
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Transportation/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
マグニチュード単位の扱い方については、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照のこと。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
