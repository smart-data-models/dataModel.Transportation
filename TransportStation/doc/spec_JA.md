エンティティトランスポートステーション  
===================  
[オープンライセンス](https://github.com/smart-data-models//dataModel.Transportation/blob/master/TransportStation/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
グローバルな記述です。**データモデルは、GFTS標準https://developers.google.com/transit/gtfs/reference/#stopstxt に従った都市の駅（メトロ、バス、トラム、ヘリポート、...）の一般的な記述と、これらの詳細な記述（アクセス手段、プラットフォーム、アシスタンス、...）です。**。  

## プロパティのリスト  

- `address`: 郵送先住所  - `alternateName`: このアイテムの別称  - `areaServed`: サービスや提供されるアイテムが提供される地理的なエリア  - `contactPoint`: アイテムの連絡先です。  - `contractingAuthority`: 契約機関の名称  - `contractingCompany`: 駅の利用に責任を持つ契約会社の名前。  - `dataProvider`: 調和されたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateLastReported`: デバイスがデータの報告に成功した最後の時間を示すタイムスタンプ。ISO8601 UTC形式の日付と時刻。  - `dateModified`: エンティティが最後に変更された時のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `description`: このアイテムの説明  - `dimension`: グローバルな次元。フォーマットは3項目のサブプロパティで構成される。単位コード（テキスト）は，[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を用いて与えられる。例えば，**MTR**はメートルを表す。  - `id`: エンティティのユニークな識別子  - `installationMode`: 地面の基準に対する位置。Enum:'aerial, ground, underGround, underSea'.  - `inventory`: locationType` = 0, 1, 3, 4の場合のみの一般的なデータマッピングです。フォーマットは4項目のサブプロパティで構成されています。  - `levelId`: その場所がある階。フロアに関連する数値インデックス。他の階に対するこのステージの相対的な位置を示す。指標0は地上階を示す。地上階は正のインデックスで、地下ステージは負のインデックスで示される。  - `location`: アイテムへのGeojson参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygonのいずれかです。  - `locationType`: 異なる場所を記述したGTFS標準レポジトリへのリンク [Location Type].0 ストップまたはプラットフォーム（ユーザーが公共交通機関で乗り降りする場所）。1 駅（1つまたは複数のプラットフォームからなるエリアまたは物理的構造）。2 入口または出口（ユーザーが通りから駅に出入りできる場所）。3 汎用交差点（駅構内で他の `location_type` 値に対応しない場所）。4 Boarding area (ユーザーが車両に乗り降りすることができるプラットフォーム上の特定の場所).  - `name`: このアイテムの名前です。  - `openingHoursSpecification`: 場所の営業時間や、場所にある特定のサービスに関する情報を提供する構造化された値  - `owner`: オーナーのIDを参照するJSONエンコードされた文字列を含むリスト  - `parentStation`: StationとPlatformの間の異なるリンクを記述したGTFS標準レポジトリへのリンク [Parent STATION].ケース '1' location_type = 0 (Stop / platform ), parent_stationフィールドは駅のIDを含みます。ケース '2' location_type = 1 (Station)の場合、このフィールドは空でなければならない。ケース '3' location_type = 2 (Input / Output) または location_type = 3 (generic intersection), parent_station フィールドには location_type = 1 のステーションの ID が含まれる。ケース '4' location_type = 4 (biding area), parent_stationフィールドはプラットホームのIDを含む。  - `platformCode`: プラットフォームタイプの停留所のプラットフォーム識別子 `location_type` = 0 駅構内に停留所がある場合。  - `refPointOfInterest`: この観測に関連した興味のあるポイントへの参照です。  - `seeAlso`: アイテムに関する追加リソースを示すuriのリスト  - `source`: エンティティデータのオリジナルソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `stationConnected`: このステーションから可能な接続。0からNまでの構造化された値で、各項目は `stationType` : [コンマで区切られた接続ラインのリスト]というフォーマットの文字列です。Enum:'aerialLift, bus, cableTram, ferry, funicular, monorail, rail, subway, train, tram, trolleybus'.  - `stationType`: 交通機関の駅の種類。Enum:'aerialLift, bus, cableTram, ferry, funicular, monorail, rail, subway, trolleybus, tram'.  - `type`: NGSI エンティティタイプ。TransportStationである必要があります。  - `webSite`: 詳細は公式サイトにリンクしています。  - `wheelChairAccessible`: 移動の不自由な方でもアクセス可能です。両親がいない停留所の場合 0 停留所のアクセシビリティに関する情報はありません。1 この停留所では、PMRユーザーが乗車できる車両もあります。2 この停留所では、PRMユーザーは乗車できません。駅の一部である停留所の場合 0 停留所は、親駅が埋められている場合、親駅の wheelchair_boarding behavior を継承する。1 車線は、駅の外から停留所／プラットフォームへの車椅子アクセスを提供する。2 駅の外から停留所／プラットフォームへの車椅子アクセスを提供するレーンはない。駅の入出力について 0 駅の入口は、もし指定されていれば、主要駅の車椅子_乗車行動を継承する。1 駅の入口は、車椅子でアクセス可能である。2 駅の入口と停留所／プラットフォームを結ぶ、車椅子でアクセス可能なルートがない。  - `zoneId`: 駅の価格帯。    
必須項目  
- `dateLastReported`  - `dateObserved`  - `id`  - `location`  - `locationType`  - `stationType`  - `type`  ## データモデルによるプロパティの記述  
アルファベット順（クリックすると詳細が表示されます）  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
TransportStation:    
  description: "The data model is a general description of urban stations (Metro, Bus, Tram, Heliport, ...) according to the GFTS standard https://developers.google.com/transit/gtfs/reference/#stopstxt, as well the detailed description of these (means of access, platform, assistance, ...)."    
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
    contactPoint:    
      description: 'The details to contact with the item.'    
      properties:    
        contactType:    
          description: 'Property. Contact type of this item.'    
          type: string    
        email:    
          description: 'Property. Email address of owner.'    
          format: idn-email    
          type: string    
        name:    
          description: 'Property. The name of this item.'    
          type: string    
        telephone:    
          description: 'Property. Telephone of this contact.'    
          type: string    
        url:    
          description: 'Property. URL which provides a description or further information about this item.'    
          format: uri    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/ContactPoint    
        type: Property    
    contractingAuthority:    
      description: 'Name of the contracting authority.'    
      type: string    
      x-ngsi:    
        type: Property    
    contractingCompany:    
      description: 'Name of the contracting company responsible for the exploitation of the station.'    
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
    dateLastReported:    
      description: 'A timestamp which denotes the last time when the device successfully reported data. Date and time in an ISO8601 UTCformat.'    
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
    dimension:    
      description: 'Global dimension. The format is structured by a sub-property of 3 items. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **MTR** represents Meters'    
      properties:    
        depth:    
          minimum: 0    
          type: number    
        height:    
          minimum: 0    
          type: number    
        width:    
          minimum: 0    
          type: number    
      type: object    
      x-ngsi:    
        type: Property    
        units: meters    
    id:    
      anyOf: &transportstation_-_properties_-_owner_-_items_-_anyof    
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
    installationMode:    
      description: 'Location  relative to the ground reference. Enum:''aerial, ground, underGround, underSea'''    
      enum:    
        - aerial    
        - ground    
        - underGround    
        - underSea    
      type: string    
      x-ngsi:    
        type: Property    
    inventory:    
      description: 'General data mapping only for `locationType` = 0, 1, 3, 4. The format is structured by a sub-property of 4 items.'    
      properties:    
        PlatformType:    
          items:    
            enum:    
              - lateral    
              - central    
            type: string    
          type: array    
        nbOfIOPoint:    
          minimum: 0    
          type: number    
        nbOfLane:    
          minimum: 0    
          type: number    
        nbOfPlatform:    
          minimum: 0    
          type: number    
      type: object    
      x-ngsi:    
        type: Property    
    levelId:    
      description: 'Floor on which the location is located. Numerical index associated with the floor. Indicates the relative position of this stage in relation to the others. The index 0 indicates the ground floor. The floors above ground level are indicated by positive indices, and the underground stages by negative indices.'    
      type: number    
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
    locationType:    
      description: 'Link to the GTFS standard repository describing the different location [Location Type]. 0 Stop or platform (place where users get on or off in a public transport vehicle). 1 Station (area or physical structure comprising one or more platforms). 2 Entrance or Exit (place where users can enter / exit a station from the street). 3 Generic intersection (location in a station that doesn''t correspond to any other `location_type` value). 4 Boarding area of a specific location on a platform where users can get on / off in a vehicle.'    
      enum:    
        - 0    
        - 1    
        - 2    
        - 3    
        - 4    
      type: string    
      x-ngsi:    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    openingHoursSpecification:    
      description: 'A structured value providing information about the opening hours of a place or a certain service inside a place'    
      items:    
        properties:    
          closes:    
            format: time    
            type: string    
          dayOfWeek:    
            enum:    
              - Monday    
              - Tuesday    
              - Wednesday    
              - Thursday    
              - Friday    
              - Saturday    
              - Sunday    
              - PublicHolidays    
            type: string    
          opens:    
            format: time    
            type: string    
          validFrom:    
            format: date-time    
            type: string    
          validThrough:    
            format: date-time    
            type: string    
      minItems: 1    
      type: array    
      x-ngsi:    
        model: https://schema.org/openingHoursSpecification    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *transportstation_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    parentStation:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Link to the GTFS standard repository describing the different link between Station and Platform [Parent STATION]. Case ''1'' location_type = 0 (Stop / platform ), the parent_station field contains the ID of a station. Case ''2'' location_type = 1  (Station), this field must be empty. Case ''3'' location_type = 2 (Input / output) or location_type = 3 (generic intersection), the parent_station field contains the ID of a station location_type = 1. Case ''4'' location_type = 4 (boarding area), the parent_station field contains the ID of a platform.'    
      x-ngsi:    
        type: Relationship    
    platformCode:    
      description: 'Platform identifier for a platform type stop `location_type` = 0 when the stop is in a station.'    
      type: number    
      x-ngsi:    
        type: Property    
    refPointOfInterest:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'A reference to a point of interest associated to this observation.'    
      x-ngsi:    
        type: Relationship    
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
    stationConnected:    
      architect:    
        type: string    
      commissioningDate:    
        format: date-time    
        type: string    
      constructionDate:    
        format: date-time    
        type: string    
      currencyAccepted:    
        items:    
          enum:    
            - EUR    
            - USD    
          type: string    
        type: array    
      description: 'Connections possible from this station. A structured value from 0 to N occurrences where each items is a string in the format `stationType` : [List of Lines connected, separated by a comma]. Enum:''aerialLift, bus, cableTram, ferry, funicular, monorail, rail, subway, train, tram, trolleybus'''    
      featuredArtist:    
        items:    
          anyOf:    
            - anyOf: *transportstation_-_properties_-_owner_-_items_-_anyof    
              description: 'Property. Unique identifier of the entity'    
            - type: string    
        type: array    
      items:    
        properties:    
          linesConnected:    
            items:    
              type: string    
            type: array    
          stationType:    
            enum:    
              - aerialLift    
              - bus    
              - cableTram    
              - ferry    
              - funicular    
              - monorail    
              - rail    
              - subway    
              - train    
              - tram    
              - trolleybus    
            type: string    
        type: object    
      paymentAccepted:    
        items:    
          enum:    
            - Cash    
            - CreditCard    
            - CryptoCurrency    
            - other    
          type: string    
        type: array    
      services:    
        properties:    
          defibrillator:    
            type: Boolean    
          emergencyPhone:    
            type: Boolean    
          informationBoardDevice:    
            type: Boolean    
          interactiveDevice:    
            type: Boolean    
          messageDevice:    
            type: Boolean    
          purchaseDevice:    
            type: Boolean    
          restBench:    
            type: Boolean    
          shelters:    
            type: Boolean    
          timetableDevice:    
            type: Boolean    
          voiceDevice:    
            type: Boolean    
          wheelChairAccessible:    
            type: Boolean    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    stationType:    
      description: 'Type of transport station. Enum:''aerialLift, bus, cableTram, ferry, funicular, monorail, rail, subway, trolleybus, tram'''    
      items:    
        enum:    
          - aerialLift    
          - bus    
          - cableTram    
          - ferry    
          - funicular    
          - monorail    
          - rail    
          - subway    
          - trolleybus    
          - tram    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI Entity type. It has to be TransportStation'    
      enum:    
        - TransportStation    
      type: string    
      x-ngsi:    
        type: Property    
    webSite:    
      description: 'Link to the official website for more information..'    
      type: string    
      x-ngsi:    
        type: Property    
    wheelChairAccessible:    
      description: 'Access possible for Person with Reduced Mobility. For stops without parents 0 no information is available regarding the accessibility of the stop. 1 some vehicles at this stop can board a PMR user. 2 PRM user cannot board  at this stop. For a stop that is part of a station 0 the stop inherits the wheelchair_boarding behavior of the parent station, if it is filled in. 1 lanes provide wheelchair access to the stop / platform  from outside the station. 2 no lane provides wheelchair access to the stop / platform from outside the station. For station inputs / outputs 0 the station entry inherits the wheelchair_boarding behavior of the main station, if specified. 1 the station entrance is wheelchair accessible. 2 no wheelchair accessible route connects the station entrance to the stops / platforms.'    
      enum:    
        - 0    
        - 1    
        - 2    
      type: string    
      x-ngsi:    
        type: Property    
    zoneId:    
      description: 'Pricing zone of the station.'    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - location    
    - dateObserved    
    - dateLastReported    
    - stationType    
    - locationType    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Transportation/blob/master/TransportStation/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/data-models/Transportation/TransportStation/schema.json    
  x-model-tags: ""    
  x-version: 0.1.2    
```  
</details>    
## ペイロードの例  
#### TransportStation NGSI-v2 キーバリューの例  
TransportStationをkey-valuesとしてJSON-LD形式で表現した例です。これは`options=keyValues`を使用した場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "id": "urn:ngsi-ld:Station:Station:MNCA-STram-L02-AP-T2",  
  "type": "TransportStation",  
  "name": "NCE-Tram-Station-L02-AP-T2",  
  "alternateName": "Nice - Tramway Station Description - L02-AP-T2",  
  "description": "Description and services provided in the station",  
  "seeAlso": "http://tramway.nice.fr/wp-content/uploads/2019/10/BD_pocket_plan_MAJ03_2019_20082019.pdf",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      43.664810,  
      7.196545  
    ]  
  },  
  "address": {  
    "addressCountry": "FR",  
    "addressLocality": "Nice",  
    "streetAddress": "Airport - Terminal 2 - Door A2"  
  },  
  "areaServed": "Nice Airport",  
  "dateLastReported": "2020-03-17T08:45:00Z",  
  "dateObserved": "2020-03-17T08:45:00Z",  
  "stationType": [  
    "tram"  
  ],  
  "locationType": 1,  
  "levelId": 0,  
  "zoneId": "B",  
  "wheelChairAccessible": 1,  
  "openingHoursSpecification": [  
    {  
      "dayOfWeek": "Monday",  
      "opens": "07:00:00",  
      "closes": "22:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Tuesday",  
      "opens": "07:00:00",  
      "closes": "22:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Wednesday",  
      "opens": "07:00:00",  
      "closes": "22:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Thursday",  
      "opens": "07:00:00",  
      "closes": "22:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Friday",  
      "opens": "07:00:00",  
      "closes": "22:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Saturday",  
      "opens": "08:00:00",  
      "closes": "23:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Sunday",  
      "opens": "08:30:00",  
      "closes": "21:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "PublicHolidays",  
      "opens": "08:30:00",  
      "closes": "21:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    }  
  ],  
  "owner": [  
    "uri:ngsi:StreetRetail"  
  ],  
  "contractingAuthority": "MNCA - Metropole Nice Cote d'Azur",  
  "contractingCompagny": "Régie Ligne d'Azur",  
  "contactPoint": {  
    "url": "uri:ngsi:www.lignesdazur.com"  
  },  
  "webSite": "https://tramway.nice.fr/Plan-Station-L02-AP-T2.pdf",  
  "instalationMode": "ground",  
  "dimension": {  
    "length": 300,  
    "width": 25,  
    "thickness": 6.35  
  },  
  "inventory": {  
    "nbOfIOPoint": 2,  
    "nbOfLane": 1,  
    "nbOfPlatform": 1,  
    "PlatformType": [  
      "lateral"  
    ]  
  },  
  "stationConnected": [  
    {  
      "stationType": "tram",  
      "linesConnected": [  
        "Tram 2 - CADAM / Nikaia",  
        "Tram 3 - Saint Isidore / Stade Allianz Riviera"  
      ]  
    },  
    {  
      "stationType": "train",  
      "linesConnected": [  
        "Gare SNCF Nice Saint Augustin (600m)"  
      ]  
    },  
    {  
      "stationType": "bus",  
      "linesConnected": [  
        "L20 - Giono / Les Pugets",  
        "L20 - Centre Commercial St Isidore",  
        "L21 - Le Gué / Polygone Riviera",  
        "L54 - Centre Commercial Cap 3000 - St Jeannet",  
        "L90 - La Bolline",  
        "91 Auron",  
        "L92 - Isola 2000"  
      ]  
    }  
  ],  
  "services": {  
    "purchaseDevice": true,  
    "interactiveDevice": true,  
    "timetableDevice": true,  
    "voiceDevice": true,  
    "informationBoardDevice": true,  
    "messageDevice": false,  
    "shelters": true,  
    "restBench": false,  
    "emergencyPhone": false,  
    "videoSurveillance": true,  
    "defibrillator": false,  
    "wheelChairAccessible": true  
  },  
  "paymentAccepted": [  
    "Cash",  
    "CreditCard"  
  ],  
  "currencyAccepted": [  
    "EUR"  
  ],  
  "constructionDate": "2016-19-08",  
  "commissioningDate": "2018-09-15",  
  "architect": "Nice Architecture",  
  "featuredArtist ": [  
    "Leopold",  
    "De Renaiss"  
  ]  
}  
```  
#### トランスポートステーション NGSI-v2 正規化例  
JSON-LD形式で正規化されたTransportStationの例を示します。これは、オプションを使用しない場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "id": "urn:ngsi-ld:Station:Station:MNCA-STram-L02-AP-T2",  
  "type": "Station",  
  "name": {  
    "type": "Property",  
    "value": "NCE-Tram-Station-L02-AP-T2"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Nice - Tramway Station Description - L02-AP-T2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Description and services provided in the station"  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": "http://tramway.nice.fr/wp-content/uploads/2019/10/BD_pocket_plan_MAJ03_2019_20082019.pdf"  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "point",  
      "coordinates": [  
        43.664810,  
        7.196545  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "addressCountry": "FR",  
      "addressLocality": "Nice",  
      "streetAddress": "Airport - Terminal 2 - Door A2"  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Nice Airport"  
  },  
  "dateLastReported": {  
    "type": "DateTime",  
    "value": "2020-03-17T08:45:00Z"  
  },  
  "stationType": {  
    "type": "Property",  
    "value": "Tram"  
  },  
  "locationType": {  
    "type": "Property",  
    "value": 1  
  },  
  "levelId": {  
    "type": "Property",  
    "value": 0  
  },  
  "zoneId": {  
    "type": "Property",  
    "value": "B"  
  },  
  "wheelChairAccessible": {  
    "type": "Property",  
    "value": 1  
  },  
  "openingHoursSpecification": {  
    "type": "object",  
    "value": [  
      {  
        "dayOfWeek": "Monday, Tuesday, Wednesday, Thursday, Friday",  
        "opens": "07.00",  
        "closes": "22.00"  
      },  
      {  
        "dayOfWeek": "Saturday",  
        "opens": "08.00",  
        "closes": "23.00"  
      },  
      {  
        "dayOfWeek": "Sunday",  
        "opens": "8.30",  
        "closes": "21.00"  
      },  
      {  
        "dayOfWeek": "PublicHolidays",  
        "opens": "8.00",  
        "closes": "21.30"  
      }  
    ],  
    "validFrom": "-01-01",  
    "validThrough": "-31-12"  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "Street furniture Urbain & Retail"  
    ]  
  },  
  "contractingAuthority": {  
    "type": "Property",  
    "value": "MNCA - Metropole Nice Cote d'Azur"  
  },  
  "contractingCompany": {  
    "type": "Property",  
    "value": "Régie Ligne d'Azur"  
  },  
  "contactPoint": {  
    "type": "Property",  
    "value": "www.lignesdazur.com"  
  },  
  "webSite": {  
    "type": "Property",  
    "value": "https://tramway.nice.fr/Plan-Station-L02-AP-T2.pdf"  
  },  
  "installationMode": {  
    "type": "Property",  
    "value": "ground"  
  },  
  "dimension": {  
    "type": "Property",  
    "value": {  
      "length": 300,  
      "width": 25,  
      "thickness": 6.35  
    }  
  },  
  "inventory": {  
    "type": "Property",  
    "value": {  
      "nbOfIOPoint": 2,  
      "nbOfLane": 1,  
      "nbOfPlatform": 1,  
      "PlatformType": "lateral"  
    }  
  },  
  "stationConnected": {  
    "type": "Property",  
    "value": {  
      "tram": {  
        "type": "Property",  
        "value": [  
          "Tram 2 - CADAM / Nikaia",  
          "Tram 3 - Saint Isidore / Stade Allianz Riviera"  
        ]  
      },  
      "train": {  
        "type": "Property",  
        "value": [  
          "Gare SNCF Nice Saint Augustin (600m)"  
        ]  
      },  
      "bus": {  
        "type": "Property",  
        "value": [  
          "L20 - Giono / Les Pugets",  
          "L20 - Centre Commercial St Isidore",  
          "L21 - Le Gué / Polygone Riviera",  
          "L54 - Centre Commercial Cap 3000 - St Jeannet",  
          "L90 - La Bolline",  
          "91 Auron",  
          "L92 - Isola 2000"  
        ]  
      }  
    }  
  },  
  "services": {  
    "type": "Property",  
    "value": {  
      "purchaseDevice": {  
        "type": "Property",  
        "value": true  
      },  
      "interactiveDevice": {  
        "type": "Property",  
        "value": true  
      },  
      "timetableDevice": {  
        "type": "Property",  
        "value": true  
      },  
      "voiceDevice": {  
        "type": "Property",  
        "value": true  
      },  
      "informationBoardDevice": {  
        "type": "Property",  
        "value": true  
      },  
      "messageDevice": {  
        "type": "Property",  
        "value": false  
      },  
      "shelters": {  
        "type": "Property",  
        "value": true  
      },  
      "restBench": {  
        "type": "Property",  
        "value": false  
      },  
      "emergencyPhone": {  
        "type": "Property",  
        "value": false  
      },  
      "videoSurveillance": {  
        "type": "Property",  
        "value": true  
      },  
      "defibrillator": {  
        "type": "Property",  
        "value": false  
      },  
      "wheelChairAccessible": {  
        "type": "Property",  
        "value": true  
      }  
    }  
  },  
  "paymentAccepted": {  
    "type": "Property",  
    "value": [  
      "Cash",  
      "CreditCard"  
    ]  
  },  
  "currencyAccepted": {  
    "type": "Property",  
    "value": [  
      "EUR"  
    ]  
  },  
  "constructionDate": {  
    "type": "DateTime",  
    "value": "2016-19-08"  
  },  
  "commissioningDate": {  
    "type": "DateTime",  
    "value": "2018-09-15"  
  },  
  "architect": {  
    "type": "Property",  
    "value": "Nice Architecture"  
  },  
  "featuredArtist ": {  
    "type": "Property",  
    "value": [  
      "Leopold",  
      "De Renaiss"  
    ]  
  }  
}  
```  
#### トランスポートステーション NGSI-LDのキーバリューの例  
TransportStationをkey-valuesとしてJSON-LD形式で表現した例です。これは`options=keyValues`を使った場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "id": "urn:ngsi-ld:Station:Station:MNCA-STram-L02-AP-T2",  
  "type": "Station",  
  "name": {  
    "type": "Property",  
    "value": "NCE-Tram-Station-L02-AP-T2"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Nice - Tramway Station Description - L02-AP-T2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Description and services provided in the station"  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": "http://tramway.nice.fr/wp-content/uploads/2019/10/BD_pocket_plan_MAJ03_2019_20082019.pdf"  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "point",  
      "coordinates": [  
        43.66481,  
        7.196545  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "addressCountry": "FR",  
      "addressLocality": "Nice",  
      "streetAddress": "Airport - Terminal 2 - Door A2"  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Nice Airport"  
  },  
  "dateLastReported": {  
    "type": "DateTime",  
    "value": "2020-03-17T08:45:00Z"  
  },  
  "stationType": {  
    "type": "Property",  
    "value": "Tram"  
  },  
  "locationType": {  
    "type": "Property",  
    "value": 1  
  },  
  "levelId": {  
    "type": "Property",  
    "value": 0  
  },  
  "zoneId": {  
    "type": "Property",  
    "value": "B"  
  },  
  "wheelChairAccessible": {  
    "type": "Property",  
    "value": 1  
  },  
  "openingHoursSpecification": {  
    "type": "object",  
    "value": [  
      {  
        "dayOfWeek": "Monday, Tuesday, Wednesday, Thursday, Friday",  
        "opens": "07.00",  
        "closes": "22.00"  
      },  
      {  
        "dayOfWeek": "Saturday",  
        "opens": "08.00",  
        "closes": "23.00"  
      },  
      {  
        "dayOfWeek": "Sunday",  
        "opens": "8.30",  
        "closes": "21.00"  
      },  
      {  
        "dayOfWeek": "PublicHolidays",  
        "opens": "8.00",  
        "closes": "21.30"  
      }  
    ],  
    "validFrom": "-01-01",  
    "validThrough": "-31-12"  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "Street furniture Urbain & Retail"  
    ]  
  },  
  "contractingAuthority": {  
    "type": "Property",  
    "value": "MNCA - Metropole Nice Cote d'Azur"  
  },  
  "contractingCompagny": {  
    "type": "Property",  
    "value": "R\u00e9gie Ligne d'Azur"  
  },  
  "contactPoint": {  
    "type": "Property",  
    "value": "www.lignesdazur.com"  
  },  
  "webSite": {  
    "type": "Property",  
    "value": "https://tramway.nice.fr/Plan-Station-L02-AP-T2.pdf"  
  },  
  "instalationMode": {  
    "type": "Property",  
    "value": "ground"  
  },  
  "dimension": {  
    "type": "Property",  
    "value": {  
      "length": 300,  
      "width": 25,  
      "thickness": 6.35  
    }  
  },  
  "inventory": {  
    "type": "Property",  
    "value": {  
      "nbOfIOPoint": 2,  
      "nbOfLane": 1,  
      "nbOfPlatform": 1,  
      "PlatformType": "lateral"  
    }  
  },  
  "stationConnected": {  
    "type": "Property",  
    "value": {  
      "tram": {  
        "type": "Property",  
        "value": [  
          "Tram 2 - CADAM / Nikaia",  
          "Tram 3 - Saint Isidore / Stade Allianz Riviera"  
        ]  
      },  
      "train": {  
        "type": "Property",  
        "value": [  
          "Gare SNCF Nice Saint Augustin (600m)"  
        ]  
      },  
      "bus": {  
        "type": "Property",  
        "value": [  
          "L20 - Giono / Les Pugets",  
          "L20 - Centre Commercial St Isidore",  
          "L21 - Le Gu\u00e9 / Polygone Riviera",  
          "L54 - Centre Commercial Cap 3000 - St Jeannet",  
          "L90 - La Bolline",  
          "91 Auron",  
          "L92 - Isola 2000"  
        ]  
      }  
    }  
  },  
  "services": {  
    "type": "Property",  
    "value": {  
      "purchaseDevice": {  
        "type": "Property",  
        "value": true  
      },  
      "interactiveDevice": {  
        "type": "Property",  
        "value": true  
      },  
      "timetableDevice": {  
        "type": "Property",  
        "value": true  
      },  
      "voiceDevice": {  
        "type": "Property",  
        "value": true  
      },  
      "informationBoardDevice": {  
        "type": "Property",  
        "value": true  
      },  
      "messageDevice": {  
        "type": "Property",  
        "value": false  
      },  
      "shelters": {  
        "type": "Property",  
        "value": true  
      },  
      "restBench": {  
        "type": "Property",  
        "value": false  
      },  
      "emergencyPhone": {  
        "type": "Property",  
        "value": false  
      },  
      "videoSurveillance": {  
        "type": "Property",  
        "value": true  
      },  
      "defibrillator": {  
        "type": "Property",  
        "value": false  
      },  
      "wheelChairAccessible": {  
        "type": "Property",  
        "value": true  
      }  
    }  
  },  
  "paymentAccepted": {  
    "type": "Property",  
    "value": [  
      "Cash",  
      "CreditCard"  
    ]  
  },  
  "currencyAccepted": {  
    "type": "Property",  
    "value": [  
      "EUR"  
    ]  
  },  
  "constructionDate": {  
    "type": "DateTime",  
    "value": "2016-19-08"  
  },  
  "commissioningDate": {  
    "type": "DateTime",  
    "value": "2018-09-15"  
  },  
  "architecte": {  
    "type": "Property",  
    "value": "Nice Architecture"  
  },  
  "featuredArtist ": {  
    "type": "Property",  
    "value": [  
      "Leopold",  
      "De Renaiss"  
    ]  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### トランスポートステーション NGSI-LDの正規化例  
ここでは、TransportStationを正規化したJSON-LD形式の例を示します。これはオプションを使用しない場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "id": "urn:ngsi-ld:Station:Station:MNCA-STram-L02-AP-T2",  
  "type": "Station",  
  "name": "NCE-Tram-Station-L02-AP-T2",  
  "alternateName": "Nice - Tramway Station Description - L02-AP-T2",  
  "description": "Description and services provided in the station",  
  "seeAlso": "http://tramway.nice.fr/wp-content/uploads/2019/10/BD_pocket_plan_MAJ03_2019_20082019.pdf",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      43.66481,  
      7.196545  
    ]  
  },  
  "address": {  
    "addressCountry": "FR",  
    "addressLocality": "Nice",  
    "streetAddress": "Airport - Terminal 2 - Door A2"  
  },  
  "areaServed": "Nice Airport",  
  "dateLastReported": "2020-03-17T08:45:00Z",  
  "dateObserved": "2020-03-17T08:45:00Z",  
  "stationType": [  
    "tram"  
  ],  
  "locationType": 1,  
  "levelId": 0,  
  "zoneId": "B",  
  "wheelChairAccessible": 1,  
  "openingHoursSpecification": [  
    {  
      "dayOfWeek": "Monday",  
      "opens": "07:00:00",  
      "closes": "22:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Tuesday",  
      "opens": "07:00:00",  
      "closes": "22:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Wednesday",  
      "opens": "07:00:00",  
      "closes": "22:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Thursday",  
      "opens": "07:00:00",  
      "closes": "22:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Friday",  
      "opens": "07:00:00",  
      "closes": "22:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Saturday",  
      "opens": "08:00:00",  
      "closes": "23:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Sunday",  
      "opens": "08:30:00",  
      "closes": "21:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "PublicHolidays",  
      "opens": "08:30:00",  
      "closes": "21:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    }  
  ],  
  "owner": [  
    "uri:ngsi:StreetRetail"  
  ],  
  "contractingAuthority": "MNCA - Metropole Nice Cote d'Azur",  
  "contractingCompagny": "R\u00e9gie Ligne d'Azur",  
  "contactPoint": {  
    "url": "uri:ngsi:www.lignesdazur.com"  
  },  
  "webSite": "https://tramway.nice.fr/Plan-Station-L02-AP-T2.pdf",  
  "instalationMode": "ground",  
  "dimension": {  
    "length": 300,  
    "width": 25,  
    "thickness": 6.35  
  },  
  "inventory": {  
    "nbOfIOPoint": 2,  
    "nbOfLane": 1,  
    "nbOfPlatform": 1,  
    "PlatformType": [  
      "lateral"  
    ]  
  },  
  "stationConnected": [  
    {  
      "stationType": "tram",  
      "linesConnected": [  
        "Tram 2 - CADAM / Nikaia",  
        "Tram 3 - Saint Isidore / Stade Allianz Riviera"  
      ]  
    },  
    {  
      "stationType": "train",  
      "linesConnected": [  
        "Gare SNCF Nice Saint Augustin (600m)"  
      ]  
    },  
    {  
      "stationType": "bus",  
      "linesConnected": [  
        "L20 - Giono / Les Pugets",  
        "L20 - Centre Commercial St Isidore",  
        "L21 - Le Gu\u00e9 / Polygone Riviera",  
        "L54 - Centre Commercial Cap 3000 - St Jeannet",  
        "L90 - La Bolline",  
        "91 Auron",  
        "L92 - Isola 2000"  
      ]  
    }  
  ],  
  "services": {  
    "purchaseDevice": true,  
    "interactiveDevice": true,  
    "timetableDevice": true,  
    "voiceDevice": true,  
    "informationBoardDevice": true,  
    "messageDevice": false,  
    "shelters": true,  
    "restBench": false,  
    "emergencyPhone": false,  
    "videoSurveillance": true,  
    "defibrillator": false,  
    "wheelChairAccessible": true  
  },  
  "paymentAccepted": [  
    "Cash",  
    "CreditCard"  
  ],  
  "currencyAccepted": [  
    "EUR"  
  ],  
  "constructionDate": "2016-19-08",  
  "commissioningDate": "2018-09-15",  
  "architect": "Nice Architecture",  
  "featuredArtist ": [  
    "Leopold",  
    "De Renaiss"  
  ],  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
マグニチュード単位の扱いについては、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照してください。  
