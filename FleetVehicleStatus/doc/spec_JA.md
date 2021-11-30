Entity:FleetVehicleStatus  
=========================  
[オープンライセンス](https://github.com/smart-data-models//dataModel.Transportation/blob/master/FleetVehicleStatus/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
グローバルな記述。**このエンティティには、一般的な車両の状態に関する統一された記述が含まれています。このエンティティは、主に輸送と物流の垂直セグメントに関連していますが、他の多くの関連するIoTアプリケーションにも使用される可能性があります。  

## プロパティのリスト  

- `address`: 郵送先住所  - `alternateName`: このアイテムの別称  - `areaServed`: サービスや提供されるアイテムが提供される地理的なエリア  - `bearing`: フリートビークルの現在の方位を北に対しての度数で示す。属性のtimestamp要素は、読み取り値がいつ得られたかを示すべきである。  - `currentOperative`: Schema.org personとして記述された車両の現在の操作者（例：ドライバー）。  - `currentStatus`: 車両の現在の状態の説明 例：Enum:'deployed, finished, terminated, servicing, starting'  - `dataProvider`: 調和されたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified`: エンティティが最後に変更された時のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `description`: このアイテムの説明  - `fleetVehicle`: このステータスエンティティが関連するFleetVehicleエンティティへの参照。  - `fleetVehicleOperation`: このステータスエンティティが関連するFleetVehicleOperationエンティティへの参照。  - `id`: エンティティのユニークな識別子  - `inRestrictedArea`: ステータス更新時に、車両が制限区域内にいることがわかっているかどうかを示す。  - `lastFuellingAmount`: 前回の給油時に車両に追加された燃料のレベルを示す。属性のtimestamp要素は、車両がいつ燃料補給されたかを示すべきである。記録されるデータの単位はLitres  - `lastKnownPosition`: アイテムへのGeojson参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygonのいずれかです。  - `lastKnownPositionUpdatedAt`: フリートビークルの最後に確認された位置更新のタイムスタンプです。  - `location`: アイテムへのGeojson参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygonのいずれかです。  - `mileageFromOdometer`: 搭載されたオドメーターによるフリートビークルの総走行距離をキロメーター（unitCode KMT）またはマイル（unitCode SMI）で表したもの。Schema.org Vehicle/ mileageFromOdometer も参照してください。timestamp 要素は、オドメーターの読み取りが行われた日時を記録します。  - `name`: このアイテムの名前です。  - `owner`: オーナーのIDを参照するJSONエンコードされた文字列を含むリスト  - `restFuelAmount`: 車両が最後に静止していた（すなわち、停止していた）ときに記録された燃料のレベル。属性のtimestamp要素は、車両が最後に静止していた時間を示す必要がある。記録されるデータはリットル単位。  - `seeAlso`: アイテムに関する追加リソースを示すuriのリスト  - `source`: エンティティデータのオリジナルソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `speed`: フリート車両の現在の速度（km/h）です。属性のtimestamp要素は、読み取り値がいつ取得されたかを示す必要があります。  - `type`: NGSI Entity 識別子。それはFleetVehicleStatusでなければならない。    
必須項目  
- `id`  - `type`    
このデータモデルは、GSMAのIoTプロジェクト（https://www.gsma.com/iot/iot-big-data/）の原型となるものです。スマートデータモデルの要件を満たすために、いくつかのマイナーな調整が行われています。  
## データモデルによるプロパティの記述  
アルファベット順（クリックすると詳細が表示されます）  
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
        type: Geoproperty    
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
## ペイロードの例  
#### FleetVehicleStatus NGSI-v2 キー・バリューの例  
ここではFleetVehicleStatusをJSON-LD形式でkey-valuesにした例を紹介します。これは`options=keyValues`を使用した場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### FleetVehicleStatus NGSI-v2 正規化された例。  
ここでは、正規化されたJSON-LD形式のFleetVehicleStatusの例を示します。これは、オプションを使用しない場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### FleetVehicleStatus NGSI-LD のキーバリューの例。  
ここではFleetVehicleStatusをJSON-LD形式でkey-valuesにした例を紹介します。これは`options=keyValues`を使った場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "@context": [  
    "https://smart-data-models.github.io/dataModel.Transportation/FleetVehicleStatus/context.jsonld"  
  ],  
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
#### FleetVehicleStatus NGSI-LD 正規化例  
ここでは、正規化されたJSON-LD形式のFleetVehicleStatusの例を示します。これはオプションを使用しない場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "@context": [  
    "https://smart-data-models.github.io/dataModel.Transportation/FleetVehicleStatus/context.jsonld"  
  ],  
  "id": "urn:ngsi-ld:FleetVehicleStatus:16ea1c5c-5aa6-11e8-8144-4b82063ca31c",  
  "type": "FleetVehicleStatus",  
  "source": {  
    "type": "Property",  
    "value": "https://source.example.com"  
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
  "restFuelAmount": {  
    "type": "Property",  
    "value": 28,  
    "unitCode": "LTR",  
    "observedAt": "2016-08-22T10:18:16Z"  
  },  
  "lastFuellingAmount": {  
    "type": "Property",  
    "value": 95,  
    "unitCode": "LTR",  
    "observedAt": "2016-08-22T10:18:16Z"  
  },  
  "currentStatus": {  
    "type": "Property",  
    "value": "finished"  
  },  
  "currentOperative": {  
    "type": "Property",  
    "value": {  
      "givenName": "John Smith",  
      "jobTitle": "Ambulance Operator",  
      "@type": "https://schema.org/Person"  
    }  
  },  
  "speed": {  
    "type": "Property",  
    "value": 60,  
    "unitCode": "KMH",  
    "observedAt": "2016-08-22T10:18:16Z"  
  },  
  "bearing": {  
    "type": "Property",  
    "value": 80,  
    "unitCode": "DD",  
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
  "inRestrictedArea": {  
    "type": "Property",  
    "value": true  
  },  
  "mileageFromOdometer": {  
    "type": "Property",  
    "value": 18756,  
    "unitCode": "SMI",  
    "observedAt": "2016-08-22T10:18:16Z"  
  }  
}  
```  
