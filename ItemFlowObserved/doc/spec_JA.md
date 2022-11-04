<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティItemFlowObserved  
======================<!-- /10-Header -->  
<!-- 15-License -->  
[オープンライセンス](https://github.com/smart-data-models//dataModel.Transportation/blob/master/ItemFlowObserved/LICENSE.md)  
[ドキュメント自動生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述。**特定の場所と期間におけるアイテムの移動に関連した観測を測定することを目的としたデータモデル。このデータモデルは、2つのデータモデルを統合し、初期バージョンの[TrafficFlowObserved]と[CrowFlowObserved]のすべての属性を統合し、さらに動きを分析したいアイテムのあらゆるタイプを統合して進化することを提案する。属性 `vehicleType` と `vehicleSubType` は初期データモデルから削除され、一般的な `itemType` と `itemSubType` という値になりました。(人, 乗り物の種類, 船の種類, 飛行機の種類, ...).**。  
のバージョンです。  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティ一覧  

<sup><sub>[*] 属性にタイプがない場合、複数のタイプまたは異なるフォーマット/パターンを持つ可能性があるためです</sub></sup>。  
- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: この項目の別称  - `areaServed[string]`: サービスまたは提供品が提供される地理的な地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `averageGapDistance[number]`: 連続する2つの検出項目間の平均ギャップ距離。単位コード（テキスト）は、[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を用いて付与する。例えば、**MTR**はMeterを表します。  - `averageHeadwayTime[number]`: 平均頭出し時間。ヘッドアウェイタイムとは、連続する2つのアイテムの間の経過時間です。単位コード（テキスト）は、[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を用いて付与する。例えば、**SEC** は Second を表す。  - `averageLength[number]`: 観測期間中に通過した検出物体の平均長。単位コード（テキスト）は、[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を用いて与えられる。例えば、**MTR** は Meter を表す。  - `averageSpeed[number]`: 観測期間中に通過した検出物体の平均速度。単位コード（テキスト）は、[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を用いて付与される。Flowの種類によって、**KMH**（車両、歩行者等）はKilometer per hour（km/h）、**KNT**はKnot（Boat）を表すことがある。  - `congested[boolean]`: 参照された通路で、観測期間中に混雑があったかどうかを示すフラグ。この属性がない場合は、混雑がないことを意味する。  - `dataProvider[string]`: 調和されたデータエンティティの提供者を識別する一連の文字。  - `dateCreated[string]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateModified[string]`: エンティティの最終更新のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateObserved[string]`: ユーザが定義した観測対象の日付。  - `dateObservedFrom[string]`: 観測期間:開始日時、ISO8601 UTC フォーマット。  - `dateObservedTo[string]`: 観測期間:終了日時（ISO8601 UTCフォーマット）。  - `description[string]`: このアイテムの説明  - `id[*]`: エンティティの一意な識別子  - `intensity[number]`: 今回の観測期間中に検出されたアイテムの総数  - `itemSubType[string]`: NGSI エンティティ（Vehicle / BoatType / Person ）の既存の 'subType' 属性、またはカウントされる項目の 'subType' をリストする将来のエンティティの識別子を参照すること。  - `itemType[string]`: NGSIエンティティ（Vehicle / BoatType / Person）の既存の'Type'属性、またはカウントされる項目の'Type'をリストする将来のエンティティの識別子を参照すること。Enum:'people, ship, vehicle, yacht' （人、船、乗り物、ヨット）。  - `laneDirection[string]`: この観測で参照される車線の通常の進行方向。この属性は、観測された交通流の進行方向を知ることができ、観測がどの道路セグメントも参照していない場合に有用である。これらの値の意味については、RoadSegment を参照のこと。  - `laneId[integer]`: 車線識別。車線の識別は、[OpenStreetMap](http://wiki.openstreetmap.org/wiki/Forward_%26_backward,_left_%26_right)に準拠したRoadSegmentエンティティで定義された規約を使用しています。  - `location[*]`: アイテムへの Geojson リファレンス。Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygonのいずれかを指定することができる。  - `name[string]`: このアイテムの名称です。  - `occupancy[number]`: 観測時間のうち、レーンを占有していた時間の割合  - `owner[array]`: 所有者の一意のIDを参照するJSONエンコードされた文字列を含むリストです。  - `refDevice[*]`: このレコードで表現されたデータを取得するために使用された装置または機器  - `refRoadSegment[*]`: 観測された該当道路区間  - `reversedLane[boolean]`: 観測期間中に車線の逆走があったかどうかを示すフラグ。この属性がない場合は、レーン逆転がないことを意味する  - `seeAlso[*]`: 項目に関する追加リソースを指すURIのリスト。  - `source[string]`: エンティティデータの元のソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `speedMax[number]`: 観測期間中に検出された最高速度。単位コード（テキスト）は、[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を用いて付与される。Flowの種類によって、**KMH**（車両、歩行者、...）はKilometer per hour（km/h）、**KNT**はKnot（Boat）を表すことがある。  - `speedMin[number]`: 観測期間中に検出された最低速度。単位コード（テキスト）は、[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を用いて付与される。Flowの種類によって、**KMH**（車両、歩行者、...）はKilometer per hour（km/h）、**KNT**はKnot（Boat）を表すことがある。  - `type[string]`: NGSI Entity タイプ。ItemFlowObservedでなければならない。  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必要なプロパティ  
- `dateObserved`  - `id`  - `laneId`  - `location`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順に並びます（クリックで詳細へ）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
ItemFlowObserved:    
  description: 'The data model intended to measure an observation linked to the movement of an item at a certain location and over a given period. This Data Model proposes an evolution of two Data Model by merging them and integrating all the attributes of the initial version of [TrafficFlowObserved] and [CrowFlowObserved] and by extension any type of item that we want to analyze the movements. Attributes `vehicleType` and `vehicleSubType` are removed from the initial data Model in order to become generic `itemType` and `itemSubType` of possible values. (people, Type of vehicle, Type of boat, Type of plane, ...).'    
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
      description: 'Average gap distance between consecutive 2 detected items. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **MTR** represents Meter.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    averageHeadwayTime:    
      description: 'Average headway time. Head away time is the time elapsed between two consecutive items. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **SEC** represents Second.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    averageLength:    
      description: 'Average length of detected items transiting during the observation period. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . For instance, **MTR** represents Meter.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    averageSpeed:    
      description: 'Average speed of detected items transiting during the observation period. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . Depending the type of Flow, the value can be **KMH** f(vehicule, pedestrian, etc.) represents Kilometer per hour (km/h) or **KNT** represents Knot (Boat).'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    congested:    
      description: 'Flags whether there was a crowd congestion during the observation period in the referred walkway. The absence of this attribute means no crowd congestion'    
      type: boolean    
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
    dateObserved:    
      description: 'Date of the observed entity defined by the user.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateObservedFrom:    
      description: 'Observation period : Start date and time in an ISO8601 UTC format.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateObservedTo:    
      description: 'Observation period : End date and time in an ISO8601 UTC format.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &itemflowobserved_-_properties_-_owner_-_items_-_anyof    
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
      description: 'Total number of items detected during this observation period'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    itemSubType:    
      description: 'Reference to an identifier of an existing ''subType'' attribute of an NGSI entity (Vehicle / BoatType / Person ) or of a future entity listing an item ''subType'' to be counted.'    
      type: string    
      x-ngsi:    
        type: Property    
    itemType:    
      description: 'Reference to an identifier of an existing ''Type'' attribute of an NGSI entity (Vehicle / BoatType / Person) or of a future entity listing an item ''Type'' to be counted. Enum:''people, ship, vehicle, yacht'''    
      enum:    
        - people    
        - ship    
        - vehicle    
        - yacht    
      type: string    
      x-ngsi:    
        type: Property    
    laneDirection:    
      description: 'Usual direction of travel in the lane referred by this observation. This attribute is useful when the observation is not referencing any road segment, allowing to know the direction of travel of the traffic flow observed. See RoadSegment for a description of the semantics of these values.'    
      enum:    
        - forward    
        - backward    
        - inbound    
        - outbound    
        - right    
        - left    
      type: string    
      x-ngsi:    
        type: Property    
    laneId:    
      description: 'Lane identifier. Lane identification is done using the conventions defined by RoadSegment entity which are based on [OpenStreetMap](http://wiki.openstreetmap.org/wiki/Forward_%26_backward,_left_%26_right).'    
      min: 1    
      type: integer    
      x-ngsi:    
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
      description: 'Fraction of the observation time where a item has been occupying the observed lane'    
      maximum: 1    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *itemflowobserved_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    refDevice:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'The device or devices used to obtain the data expressed by this record'    
      x-ngsi:    
        type: Relationship    
    refRoadSegment:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Concerned road segment on which the observation has been made'    
      x-ngsi:    
        type: Relationship    
    reversedLane:    
      description: 'Flags whether traffic in the lane was reversed during the observation period. The absence of this attribute means no lane reversion'    
      type: boolean    
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
    speedMax:    
      description: 'Maximum speed detected during the observation period. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . Depending the type of Flow, the value can be **KMH** (vehicule, pedestrian, ...) represents Kilometer per hour (km/h) or **KNT** represents Knot (Boat).'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    speedMin:    
      description: 'Minimum speed detected during the observation period. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . Depending the type of Flow, the value can be **KMH** (vehicule, pedestrian, ...) represents Kilometer per hour (km/h) or **KNT** represents Knot (Boat).'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI Entity type. It has to be ItemFlowObserved'    
      enum:    
        - ItemFlowObserved    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - location    
    - dateObserved    
    - laneId    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Transportation/blob/master/ItemFlowObserved/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/data-models/Transportation/ItemFlowObserved/schema.json    
  x-model-tags: ""    
  x-version: ""    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ペイロードの例  
#### ItemFlowObserved NGSI-v2 key-value の例。  
以下は、ItemFlowObservedをJSON-LD形式でkey-valuesとした例である。これは、`options=keyValues`を使用した場合にNGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "FlowObserved:BFO-NCE-MNCA-SP-001",  
  "type": "ItemFlowObserved",  
  "address": {  
    "addressCountry": "FR",  
    "addressLocality": "Nice",  
    "streetAddress": "Port Lympia"  
  },  
  "areaServed": "Nice Harbor",  
  "averageGapDistance": 35.28,  
  "averageHeadwayTime": 156,  
  "averageLength": 7.44,  
  "averageSpeed": 2.7,  
  "congested": false,  
  "dateObserved": "2020-03-20T16:30:00Z",  
  "dateObservedFrom": "2020-03-20T16:30:00Z",  
  "dateObservedTo": "2020-03-20T22:30:00Z",  
  "description": "Boat Flow Observed from Nice Harbor.",  
  "itemSubType": "monoHull",  
  "itemType": "yacht",  
  "intensity": 12,  
  "laneDirection": "outbound",  
  "laneId": 1,  
  "location": {  
    "coordinates": [  
      7.196545,  
      43.664809  
    ],  
    "type": "Point"  
  },  
  "maxSpeed": 3.8,  
  "minSpeed": 2.6,  
  "name": "BFO-NCE-MNCA-SP-001",  
  "occupancy": 0.1562,  
  "refDevice": "Device:BFO-NCE-MNCA-SP-001-Dev-02",  
  "reverseLane": false  
}  
```  
</details>  
#### ItemFlowObserved NGSI-v2 正規化例  
以下は、ItemFlowObserved を JSON-LD 形式で正規化した例である。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "FlowObserved:BFO-NCE-MNCA-SP-001",  
  "type": "ItemFlowObserved",  
  "name": {  
    "type": "Text",  
    "value": "BFO-NCE-MNCA-SP-001"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Boat Flow Observed from Nice Harbor."  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        7.196545,  
        43.664809  
      ]  
    }  
  },  
  "address": {  
    "type": "PostalAddress",  
    "value": {  
      "streetAddress": "Port Lympia",  
      "addressLocality": "Nice",  
      "addressCountry": "FR"  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Nice Harbor"  
  },  
  "dateObserved": {  
    "type": "DateTime",  
    "value": "2020-03-20T16:30:00Z"  
  },  
  "dateObservedFrom": {  
    "type": "DateTime",  
    "value": "2020-03-20T16:30:00Z"  
  },  
  "dateObservedTo": {  
    "type": "DateTime",  
    "value": "2020-03-20T22:30:00Z"  
  },  
  "refDevice": {  
    "type": "Relationship",  
    "value": "Device:BFO-NCE-MNCA-SP-001-Dev-02"  
  },  
  "itemType": {  
    "type": "Text",  
    "value": "yacht"  
  },  
  "itemSubType": {  
    "type": "Text",  
    "value": "monoHull"  
  },  
  "laneId": {  
    "type": "Integer",  
    "value": 1  
  },  
  "laneDirection": {  
    "type": "Text",  
    "value": "outbound"  
  },  
  "reverseLane": {  
    "type": "Boolean",  
    "value": false  
  },  
  "intensity": {  
    "type": "Number",  
    "value": 12  
  },  
  "occupancy": {  
    "type": "Number",  
    "value": 0.1562  
  },  
  "congested": {  
    "type": "Boolean",  
    "value": false  
  },  
  "averageSpeed": {  
    "type": "Number",  
    "value": 2.7  
  },  
  "averageLength": {  
    "type": "Number",  
    "value": 7.44  
  },  
  "averageHeadwayTime": {  
    "type": "Number",  
    "value": 156  
  },  
  "averageGapDistance": {  
    "type": "Number",  
    "value": 35.28  
  },  
  "minSpeed": {  
    "type": "Number",  
    "value": 2.6  
  },  
  "maxSpeed": {  
    "type": "Number",  
    "value": 3.8  
  }  
}  
```  
</details>  
#### ItemFlowObserved NGSI-LD key-value Example  
ItemFlowObservedをJSON-LD形式でkey-valuesとした例です。これは、`options=keyValues`を使用した場合にNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "itemFlowObserved:BFO-NCE-MNCA-SP-001",  
    "type": "ItemFlowObserved",  
    "address": {  
        "addressCountry": "FR",  
        "addressLocality": "Nice",  
        "streetAddress": "Port Lympia"  
    },  
    "areaServed": "Nice Harbor",  
    "averageGapDistance": 35.28,  
    "averageHeadwayTime": 156,  
    "averageLength": 7.44,  
    "averageSpeed": 2.7,  
    "congested": false,  
    "dateObserved": "2020-03-20T16:30:00Z",  
    "dateObservedFrom": "2020-03-20T16:30:00Z",  
    "dateObservedTo": "2020-03-20T22:30:00Z",  
    "description": "Boat Flow Observed from Nice Harbor.",  
    "intensity": 12,  
    "itemSubtype": "monoHull",  
    "itemType": "yacht",  
    "laneDirection": "outbound",  
    "laneId": 1,  
    "location": {  
        "coordinates": [  
            7.196545,  
            43.664809  
        ],  
        "type": "Point"  
    },  
    "maxSpeed": 3.8,  
    "minSpeed": 2.6,  
    "name": "BFO-NCE-MNCA-SP-001",  
    "occupancy": 0.1562,  
    "refDevice": "Device:BFO-NCE-MNCA-SP-001-Dev-02",  
    "reverseLane": false,  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Transportation/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### ItemFlowObserved NGSI-LD 正規化例  
以下は、ItemFlowObserved を JSON-LD 形式で正規化した例である。これはオプションを使用しない場合、NGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "FlowObserved:BFO-NCE-MNCA-SP-001",  
    "type": "ItemFlowObserved",  
    "address": {  
        "type": "Property",  
        "value": {  
            "streetAddress": "Port Lympia",  
            "addressLocality": "Nice",  
            "addressCountry": "FR"  
        }  
    },  
    "areaServed": {  
        "type": "Property",  
        "value": "Nice Harbor"  
    },  
    "averageGapDistance": {  
        "type": "Property",  
        "value": 35.28,  
        "unitCode": "MTR"  
    },  
    "averageHeadwayTime": {  
        "type": "Property",  
        "value": 156,  
        "unitCode": "SEC"  
    },  
    "averageLength": {  
        "type": "Property",  
        "value": 7.44,  
        "unitCode": "MTR"  
    },  
    "averageSpeed": {  
        "type": "Property",  
        "value": 2.7,  
        "unitCode": "KNT"  
    },  
    "congested": {  
        "type": "Property",  
        "value": false  
    },  
    "dateObserved": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2020-03-20T16:30:00Z"  
        }  
    },  
    "dateObservedFrom": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2020-03-20T16:30:00Z"  
        }  
    },  
    "dateObservedTo": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2020-03-20T22:30:00Z"  
        }  
    },  
    "description": {  
        "type": "Property",  
        "value": "Boat Flow Observed from Nice Harbor."  
    },  
    "intensity": {  
        "type": "Property",  
        "value": 12  
    },  
    "itemSubType": {  
        "type": "Property",  
        "value": "monoHull"  
    },  
    "itemType": {  
        "type": "Property",  
        "value": "yatching"  
    },  
    "laneDirection": {  
        "type": "Property",  
        "value": "outbound"  
    },  
    "laneId": {  
        "type": "Property",  
        "value": 1  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                7.196545,  
                43.664809  
            ]  
        }  
    },  
    "maxSpeed": {  
        "type": "Property",  
        "value": 3.8,  
        "unitCode": "KNT"  
    },  
    "minSpeed": {  
        "type": "Property",  
        "value": 2.6,  
        "unitCode": "KNT"  
    },  
    "name": {  
        "type": "Property",  
        "value": "BFO-NCE-MNCA-SP-001"  
    },  
    "occupancy": {  
        "type": "Property",  
        "value": 0.1562  
    },  
    "refDevice": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Device:BFO-NCE-MNCA-SP-001-Dev-02"  
    },  
    "reverseLane": {  
        "type": "Property",  
        "value": false  
    },  
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
