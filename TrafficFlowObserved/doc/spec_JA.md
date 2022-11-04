<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティTrafficFlowObserved  
=========================<!-- /10-Header -->  
<!-- 15-License -->  
[オープンライセンス](https://github.com/smart-data-models//dataModel.Transportation/blob/master/TrafficFlowObserved/LICENSE.md)  
[ドキュメント自動生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述。**ある場所と時間における交通の流れの状態を観察すること。  
バージョン: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティ一覧  

<sup><sub>[*] 属性にタイプがない場合、複数のタイプまたは異なるフォーマット/パターンを持つ可能性があるためです</sub></sup>。  
- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: この項目の別称  - `areaServed[string]`: サービスまたは提供品が提供される地理的な地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `averageGapDistance[number]`: 連続車間距離の平均値  . Model: [https://schema.org/Number](https://schema.org/Number)- `averageHeadwayTime[number]`: 平均ヘッドウェイ時間。ヘッドウェイ時間とは、連続する2台の車両が通過するまでの楕円形の時間です  . Model: [https://schema.org/Number](https://schema.org/Number)- `averageVehicleLength[number]`: 観測期間中に通過した車両の平均長  
    観測期間中  . Model: [https://schema.org/Number](https://schema.org/Number)- `averageVehicleSpeed[number]`: 観測期間中に通過した車両の平均速度  . Model: [https://schema.org/Number](https://schema.org/Number)- `congested[boolean]`: 観測期間中に参照レーンに渋滞が発生したか否かのフラグ。この属性がない場合、渋滞が発生していないことを示す。  . Model: [https://schema.org/Boolean.](https://schema.org/Boolean.)- `dataProvider[string]`: 調和されたデータエンティティの提供者を識別する一連の文字。  - `dateCreated[string]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateModified[string]`: エンティティの最終更新のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateObserved[string]`: ISO8601 UTCフォーマットでのこの観測の日付と時間。これは、特定の時間の瞬間かISO8601の間隔で表すことができます。Orion Context Broker が日時の間隔をサポートしていないことに対する回避策として、2つの別々の属性を使用することができます。dateObservedFrom`, `dateObservedTo` です。[DateTime](https://schema.org/DateTime) または [Text](https://schema.org/Text) として表される ISO8601 のインターバル。  . Model: [https://schema.org/DateTime.](https://schema.org/DateTime.)- `dateObservedFrom[string]`: 観測期間の開始日時。dateObserved` を参照。  . Model: [https://schema.org/Datetime.](https://schema.org/Datetime.)- `dateObservedTo[string]`: 観測期間の終了日時。DateObserved` を参照。  . Model: [https://schema.org/Datetime.](https://schema.org/Datetime.)- `description[string]`: このアイテムの説明  - `id[*]`: エンティティの一意な識別子  - `intensity[number]`: 今回の観測期間中に検出された車両の総台数  . Model: [https://schema.org/Number.](https://schema.org/Number.)- `laneDirection[string]`: この観測で参照される車線の通常の進行方向。この属性は、観測された交通流の進行方向を知ることができ、どの道路セグメントも参照していない場合に有用である。Enum:forward, backward'.これらの値のセマンティクスの説明については、RoadSegment を参照のこと。  . Model: [https://schema.org/Text](https://schema.org/Text)- `laneId[integer]`: 車線識別。車線の識別は、[OpenStreetMap](http://wiki.openstreetmap.org/wiki/Forward_%26_backward,_left_%26_right)に準拠したRoadSegmentエンティティで定義された規約を使用しています。  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: アイテムへの Geojson リファレンス。Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygonのいずれかを指定することができる。  - `name[string]`: このアイテムの名称です。  - `occupancy[number]`: 観測車線を占有した観測時間の割合  . Model: [https://schema.org/Number.](https://schema.org/Number.)- `owner[array]`: 所有者の一意のIDを参照するJSONエンコードされた文字列を含むリストです。  - `refRoadSegment[string]`: 観測された道路セグメント。RoadSegment 型のエンティティへの参照。  . Model: [https://schema.org/URL](https://schema.org/URL)- `reversedLane[boolean]`: 観測期間中に車線の逆走があったかどうかを示すフラグ。この属性がない場合は、レーン逆転がないことを意味する  . Model: [https://schema.org/Boolean.](https://schema.org/Boolean.)- `seeAlso[*]`: 項目に関する追加リソースを指すURIのリスト。  - `source[string]`: エンティティデータの元のソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `type[string]`: NGSI Entity タイプ。TrafficFlowObservedでなければならない。  - `vehicleSubType[string]`: 例えば、`vehicleType` が `Lorry` の場合、`vehicleSubType` は `OGV1` や `OGV2` で、より正確な車両の種類を伝えることができるようにすることができる。  - `vehicleType[string]`: 構造的特徴から見た車両のタイプ。Enum:'agriculturalVehicle, bicycle, bus, minibus, car, caravan, tram, tanker, carWithCaravan, carWithTrailer, lorry, moped, motorcycle, motorcycleWithSideCar, motorscooter, trailer, van, constructionOrMaintenanceVehicle, trolley, binTrolley, sweepingMachine, cleaningTrolley'.  . Model: [https://schema.org/Text](https://schema.org/Text)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必要なプロパティ  
- `dateObserved`  - `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
この事業体は、主に自動車およびスマートシティの垂直セグメントと関連するIoTアプリケーションに関連しています。  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順に並びます（クリックで詳細へ）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
TrafficFlowObserved:    
  description: 'An observation of traffic flow conditions at a certain place and time.'    
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
      description: 'Average gap distance between consecutive vehicles'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: 'meter (m)'    
    averageHeadwayTime:    
      description: 'Average headway time. Headway time is the time ellapsed between two consecutive vehicles'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: 'second (s)'    
    averageVehicleLength:    
      description: |-    
        Average length of the vehicles transiting during    
            the observation period    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: 'meter (m)'    
    averageVehicleSpeed:    
      description: 'Average speed of the vehicles transiting during the observation period'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: 'Kilometer per hour (Km/h)'    
    congested:    
      description: ' Flags whether there was a traffic congestion during the observation period in the referred lane. The absence of this attribute means no traffic congestion'    
      type: boolean    
      x-ngsi:    
        model: https://schema.org/Boolean.    
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
      description: 'The date and time of this observation in ISO8601 UTC format. It can be represented by an specific time instant or by an ISO8601 interval. As a workaround for the lack of support of Orion Context Broker for datetime intervals, it can be used two separate attributes: `dateObservedFrom`, `dateObservedTo`. [DateTime](https://schema.org/DateTime) or an ISO8601 interval represented as [Text](https://schema.org/Text)'    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime.    
        type: Property    
    dateObservedFrom:    
      description: 'Observation period start date and time. See `dateObserved`'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Datetime.    
        type: Property    
    dateObservedTo:    
      description: 'Observation period end date and time. See `dateObserved`'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Datetime.    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &trafficflowobserved_-_properties_-_owner_-_items_-_anyof    
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
      description: 'Total number of vehicles detected during this observation period'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number.    
        type: Property    
    laneDirection:    
      description: 'Usual direction of travel in the lane referred by this observation. This attribute is useful when the observation is not referencing any road segment, allowing to know the direction of travel of the traffic flow observed. Enum:forward, backward''. See RoadSegment for a description of the semantics of these values.'    
      enum:    
        - forward    
        - backward    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    laneId:    
      description: 'Lane identifier. Lane identification is done using the conventions defined by RoadSegment entity which are based on [OpenStreetMap](http://wiki.openstreetmap.org/wiki/Forward_%26_backward,_left_%26_right).'    
      minimum: 1    
      type: integer    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'GeoProperty. Geojson reference to the item. Point'    
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
        - description: 'GeoProperty. Geojson reference to the item. LineString'    
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
        - description: 'GeoProperty. Geojson reference to the item. Polygon'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiPoint'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
        type: GeoProperty    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    occupancy:    
      description: 'Fraction of the observation time where a vehicle has been occupying the observed lane'    
      maximum: 1    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number.    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *trafficflowobserved_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    refRoadSegment:    
      description: 'Concerned road segment on which the observation has been made. Reference to an entity of type RoadSegment'    
      format: uri    
      type: string    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Relationship    
    reversedLane:    
      description: 'Flags whether traffic in the lane was reversed during the observation period. The absence of this attribute means no lane reversion'    
      type: boolean    
      x-ngsi:    
        model: https://schema.org/Boolean.    
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
    type:    
      description: 'NGSI Entity type. It has to be TrafficFlowObserved'    
      enum:    
        - TrafficFlowObserved    
      type: string    
      x-ngsi:    
        type: Property    
    vehicleSubType:    
      description: 'It allows to specify a sub type of `vehicleType`, eg if the `vehicleType` is set to `Lorry` the `vehicleSubType` may be `OGV1` or `OGV2` to convey more information about the exact type of vehicle.'    
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
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
## ペイロードの例  
#### TrafficFlowObserved NGSI-v2 key-value の例。  
TrafficFlowObservedをJSON-LD形式でkey-valuesとした例です。これは、`options=keyValues`を使用した場合にNGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
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
      [-4.73735395519672, 41.6538181849672],  
      [-4.73414858659993, 41.6600594193478],  
      [-4.73447575302641, 41.659585195093]  
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
#### TrafficFlowObserved NGSI-v2 正規化例  
以下は、TrafficFlowObservedをJSON-LD形式で正規化した例である。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "TrafficFlowObserved-Valladolid-osm-60821110",  
  "type": "TrafficFlowObserved",  
  "dateObserved": {  
    "value": "2016-12-07T11:10:00/2016-12-07T11:15:00"  
  },  
  "laneDirection": {  
    "value": "forward"  
  },  
  "dateObservedFrom": {  
    "type": "DateTime",  
    "value": "2016-12-07T11:10:00Z"  
  },  
  "averageVehicleLength": {  
    "value": 9.87  
  },  
  "averageHeadwayTime": {  
    "value": 0.5  
  },  
  "occupancy": {  
    "value": 0.76  
  },  
  "reversedLane": {  
    "value": false  
  },  
  "dateObservedTo": {  
    "type": "DateTime",  
    "value": "2016-12-07T11:15:00Z"  
  },  
  "intensity": {  
    "value": 197  
  },  
  "laneId": {  
    "value": 1  
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
  "address": {  
    "type": "PostalAddress",  
    "value": {  
      "addressLocality": "Valladolid",  
      "addressCountry": "ES",  
      "streetAddress": "Avenida de Salamanca"  
    }  
  },  
  "averageVehicleSpeed": {  
    "value": 52.6  
  }  
}  
```  
</details>  
#### TrafficFlowObserved NGSI-LD key-value の例。  
TrafficFlowObservedをJSON-LD形式でkey-valuesにした例です。これは、`options=keyValues`を使用した場合にNGSI-LDと互換性があり、個々のエンティティのコンテキストデータが返されます。  
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
            "streetAddress": "Avenida de Salamanca",  
            "type": "PostalAddress"  
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
        "value": "2016-12-07T11:10:00/2016-12-07T11:15:00"  
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
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Transportation/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### TrafficFlowObserved NGSI-LD 正規化例  
TrafficFlowObservedをJSON-LD形式で正規化した例です。これはオプションを使用しない場合、NGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
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
    "dateObservedFrom": {  
        "@type": "DateTime",  
        "@value": "2016-12-07T11:10:00Z"  
    },  
    "dateObservedTo": {  
        "@type": "DateTime",  
        "@value": "2016-12-07T11:15:00Z"  
    },  
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
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Transportation/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
マグニチュード単位の扱いについては、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照してください。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
