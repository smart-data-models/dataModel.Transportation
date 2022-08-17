[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティ道路セグメント  
=============  
[オープンライセンス](https://github.com/smart-data-models//dataModel.Transportation/blob/master/RoadSegment/LICENSE.md)  
[ドキュメント自動生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
グローバルな記述。**このエンティティは、道路セグメントの調和された地理的および文脈的な記述を含む。道路セグメントの集合体は、道路を記述するために使用される。  
バージョン: 0.4.1  

## プロパティ一覧  

- `address`: 郵送先住所  - `agency_name`: agency_name フィールドには、対象となるエンティティの保守に責任を持つ機関または組織のフルネー ムが含まれる。SameAs:GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)の 'agency_name' フィールド。  - `allowedVehicleType`: この道路セグメントを通過することができる車両タイプ（複数可）。Enum:'agriculturalVehicle, bicycle, bus, car, caravan, carWithCaravan, carWithTrailer, constructionOrMaintenanceVehicle, lorry, moped, motorcycle, motorcycleWithSideCar, motorscooter, tanker, trailer, van, anyVehicle'（農業車両）.許容される値。VehicleTypeEnum_, [DATEX 2 version 2.3](http://d2docs.ndwcloud.nu/) で定義される以下の値。  - `alternateName`: この項目の別称  - `annotations`: アイテムに関するアノテーション  - `areaServed`: サービスまたは提供品が提供される地理的な地域  - `bridgeCount`: この観測に対応する道路セグメント内の橋の数。道路セグメントに橋がない場合は0を取る。  - `carriagewayLength`: この観測に対応する道路セグメントの車路の総延長。  - `carriagewayWidth`: この観測に対応する道路セグメントの車道幅の合計。  - `category`: 道路セグメントの特別な特性を伝えることができるようになります。Enum:'oneway, toll, link'.  一方通行`:道路セグメントが一方向にしか使えないかどうかを示すフラグ。このフラグがない場合、道路セグメントは両方向(前後方向)に使用できることを意味する。http://wiki.openstreetmap.org/wiki/Key:oneway](http://wiki.openstreetmap.org/wiki/Key:oneway) も参照してください。toll` : 道路セグメントが有料であるかどうかのフラグ。link` : この道路セグメントが、道路から出たり入ったりするための補助リンクセグメントであるかどうかのフラグです。https://wiki.openstreetmap.org/wiki/Tag:highway%3Dmotorway_link](https://wiki.openstreetmap.org/wiki/Tag:highway%3Dmotorway_link) を参照。その他、アプリケーションにとって意味のある任意の値。  - `color`: 製品の色  - `culvertCount`: この観測に対応する道路のトレースで普及しているカルバートの数。  - `cyclePathLeftHeight`: この観測に対応する道路左端の自転車道の高さ。  - `cyclePathLeftWidth`: この観測に対応する道路左端の自転車道の幅。  - `cyclePathMaterial`: この観測に対応する道路脇のサイクリングロード敷設に使用した建設資材。  - `cyclePathPlacement`: この観測に対応する道路セグメントに沿ったサイクルトラックの配置を記述する。Enum:' ['RIGHT, LEFT, BOTH, NOT_AVAILABLE' ]。  - `cyclePathRightHeight`: この観測に対応する道路右端の自転車道の高さ。  - `cyclePathRightWidth`: この観測に対応する道路右端の自転車道の幅。  - `dataDescriptor`: データ記述子実体を指すURI  - `dataProvider`: 調和されたデータエンティティの提供者を識別する一連の文字。  - `dateCreated`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateModified`: エンティティの最終更新のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description`: このアイテムの説明  - `endKilometer`: この道路セグメントが終了するキロメートル番号（道路の起点から計測）。  - `endPoint`: アイテムへの Geojson リファレンス。Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygonのいずれかを指定することができる。  - `id`: エンティティの一意な識別子  - `image`: アイテムの画像  - `laneInfo`: この観測に対応する道路の車線の様相を記述する。  - `laneUsage`: この属性は、各車線を説明する特定のパラメータを伝えるために使用される。道路セグメントのレーンごとに文字列を含む必要がある。配列の要素 0 には車線 1 の情報を格納し、以下同様とする。参照する文字列の形式は以下の通り。<lane_direction>, <lane_minimumAllowedSpeed>, <lane_maximumAllowedSpeed>, <lane_maximumAllowedHeight>, <lane_maximumAllowedWeight> とする。<lane_direction> はテキスト文字列で、以下の値が使用可能です。forward`.このレーンは現在 `forwards` 方向で使用されています．backward`.レーンは現在 `backwards` 方向に使用されています．必須パラメータは `lane_direction` のみである．指定がない場合、残りのパラメータはエンティティレベルで指定されたものと同じであるとみなすことができる。  - `length`: この道路セグメントの総延長（キロメートル）。  - `location`: アイテムへの Geojson リファレンス。Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygonのいずれかを指定することができる。  - `maximumAllowedHeight`: この道路区間を通過する車両の最大許容高さ  - `maximumAllowedSpeed`: 道路区間を通行することができる最高速度。特定の車種（トラック、キャラバンなど）には、より厳しい制限が適用される場合がある。  - `maximumAllowedWeight`: この道路区間を通過する車両の最大許容重量  - `maximumAllowedWidth`: この観測に対応するエンティティを使用する車両の最大許容幅。  - `medianHeight`: この観測に対応する道路の中央分離帯または中央保留地の高さ。  - `medianLength`: この観測に対応する道路の中央分離帯または中央保留地の長さ。  - `medianWidth`: この観測に対応する道路の中央分離帯または中央保留地の幅。  - `minimumAllowedSpeed`: この道路区間を通過する際の最低許容速度  - `municipalityInfo`: この観測に対応する市町村情報。  - `name`: このアイテムの名称です。  - `owner`: 所有者の一意のIDを参照するJSONエンコードされた文字列を含むリストです。  - `pedestrianPathLeftHeight`: この観測に対応する道路の左端に設置された歩道の高さ。  - `pedestrianPathLeftWidth`: この観測に対応する道路の左端に設置された歩道の幅。  - `pedestrianPathMaterial`: この観測に対応する道路脇の歩道／歩道敷設に使用された建設資材。  - `pedestrianPathPlacement`: この観測に対応する道路セグメントに沿って、歩行者の存在と配置を記述する。Enum:'RIGHT, LEFT, BOTH, NOT_AVAILABLE' とする。  - `pedestrianPathRightHeight`: この観測に対応する道路の右端に置かれた歩道の高さ。  - `pedestrianPathRightWidth`: この観測に対応する道路の右端に設置された歩道の幅。  - `refRoad`: この道路セグメントが属する道路。  - `rightOfWayWidth`: Right of Way (RoW) は、道路に利用できる土地の総面積である。その幅は、道路の線形に沿って、馬車道、その他の必需品、将来の拡張を収容する。  - `roadClass`: この観測に対応する道路のタイプ。Enum: [OTHER_PUBLIC_ROAD, PRIVATE_ROAD, MINOR_CITY_ROAD, MAJOR_DISTRICT_ROAD, MAJOR_CITY_ROAD, NATIONAL_HIGHWAY, SERVICE_ROAD, STATE_HIGHWAY, OTHER_DISTRICT_ROAD, PORT_ROAD] とする。  - `roadDirection`: 道路が向かっている方向を表す。Enum:' ['N, S, E, W''。値N,S,E,WはそれぞれNorth,South,East,Westを表す。  - `roadId`: この観測に対応する道路の一意な内部表現。  - `roadMaterial`: この観測に対応する車道敷設に使用された建設材料。例：コンクリート、土、タールなど。  - `roadName`: この観測に対応する道路の名前。  - `roadWork`: 緊急に介入する場合の道路工事の理由。これらの値の組み合わせ。Enum:'COLLAPSE, DERAILMENT, FIRE, FLOOD, GASLEAK, LANDSLIDE, OTHER, POWERCUT, ROCKFALL, SAGGING, WATERLEAK'.とする。  - `seeAlso`: 項目に関する追加リソースを指すURIのリスト。  - `source`: エンティティデータの元のソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `startKilometer`: この道路セグメントの始点となるキロメートル番号（道路の始点から計測）。  - `startPoint`: アイテムへの Geojson リファレンス。Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygonのいずれかを指定することができる。  - `status`: 道路セグメントの特定の運転状況。追加情報には、statusDescription を使用する。Enum: 'open, closed, limited'.  open`: 道路セグメントは意図した容量で使用できる。`closed`: 道路工事、橋や鍵が開いている、または他のイベントにより通行ができないため、通行できない。限定された`：通行は可能だが、完全な通行はできない。  - `statusDescription`: status 属性への追加情報。  - `totalCyclePathWidth`: この観測に対応する道路に存在する自転車道の幅の合計。  - `totalLaneNumber`: この道路セグメントが提供する総車線数  - `totalPedestrianPathLength`: この観測に対応する道路に存在する歩道の長さの合計。  - `totalPedestrianPathWidth`: この観測に対応する道路に存在する歩道の幅の合計。  - `type`: NGSI Entity タイプ。これはRoadSegmentでなければならない。  - `width`: 道路の区間幅。    
必要なプロパティ  
- `allowedVehicleType`  - `endPoint`  - `id`  - `name`  - `refRoad`  - `startPoint`  - `type`    
道路セグメントには、複数の車線が含まれることがある。このデータモデルでは、異種車線（用途、速度、高さなどが異なる）で構成される道路セグメントを表現することができる。車線は1〜nの整数値で識別され、1番が前方右側の車線となる。前進方向とは、セグメントの始点から終点に向かうベクトルによって示される方向である。これは、OpenStreetMap で使用されているものと同じである。このエンティティは、主に自動車、スマートシティの垂直セグメントと関連するIoTアプリケーションに関連している。このデータモデルは、携帯電話事業者及びGSMAの協力のもとで開発された。  
## プロパティのデータモデル記述  
アルファベット順に並びます（クリックで詳細へ）  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
RoadSegment:    
  description: 'This entity contains a harmonised geographic and contextual description of a road segment. A collection of road segments are used to describe a Road.'    
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
    agency_name:    
      description: "The agency_name field contains the full name of the agency or organisation responsible for maintenance of the entity under consideration. SameAs: 'agency_name' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)"    
      type: string    
      x-ngsi:    
        type: Property    
    allowedVehicleType:    
      description: 'Vehicle type(s) allowed to transit through this road segment. Enum:''agriculturalVehicle, bicycle, bus, car, caravan, carWithCaravan, carWithTrailer, constructionOrMaintenanceVehicle, lorry, moped, motorcycle, motorcycleWithSideCar, motorscooter, tanker, trailer, van, anyVehicle''. Allowed values: The following values defined by _VehicleTypeEnum_, [DATEX 2 version 2.3](http://d2docs.ndwcloud.nu/):'    
      items:    
        enum:    
          - agriculturalVehicle    
          - bicycle    
          - bus    
          - car    
          - caravan    
          - carWithCaravan    
          - carWithTrailer    
          - constructionOrMaintenanceVehicle    
          - lorry    
          - moped    
          - motorcycle    
          - motorcycleWithSideCar    
          - motorscooter    
          - tanker    
          - trailer    
          - van    
          - anyVehicle    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    annotations:    
      description: 'Annotations about the item'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    bridgeCount:    
      description: 'Number of bridges in the road segment corresponding to this observation. Takes 0 (zero) as the value when the road segment has no bridges.'    
      type: number    
      x-ngsi:    
        type: Property    
    carriagewayLength:    
      description: 'Total length of the carriage way of the road segment corresponding to this observation.'    
      type: number    
      x-ngsi:    
        type: Property    
    carriagewayWidth:    
      description: 'Total width of the carriage way of the road segment corresponding to this observation.'    
      type: number    
      x-ngsi:    
        type: Property    
    category:    
      description: 'Allows to convey extra characteristics of a road segment. Enum:''oneway, toll, link''.  `oneway`: Flags whether the road segment can only be used in one direction. If not present it means road segment can be used in both directions (forwards and backwards). See also [http://wiki.openstreetmap.org/wiki/Key:oneway](http://wiki.openstreetmap.org/wiki/Key:oneway). `toll` : Flags whether the road segment is under toll fees. `link` : Flags whether this road segment is an auxiliary link segment for exiting or entering a road. See [https://wiki.openstreetmap.org/wiki/Tag:highway%3Dmotorway_link](https://wiki.openstreetmap.org/wiki/Tag:highway%3Dmotorway_link). Any other value meaningful to an application.'    
      items:    
        enum:    
          - oneway    
          - toll    
          - link    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    color:    
      description: 'The color of the product'    
      type: string    
      x-ngsi:    
        model: https://schema.org/color    
        type: Property    
    culvertCount:    
      description: 'Number of culverts prevalent in the trace of the road corresponding to this observation.'    
      type: number    
      x-ngsi:    
        type: Property    
    cyclePathLeftHeight:    
      description: 'Height of the cycle track on the left edge of the road corresponding to this observation.'    
      type: number    
      x-ngsi:    
        type: Property    
    cyclePathLeftWidth:    
      description: 'Width of the cycle track on the left edge of the road corresponding to this observation.'    
      type: number    
      x-ngsi:    
        type: Property    
    cyclePathMaterial:    
      description: 'Construction material used for laying the cycle path on the sides of the road corresponding to this observation.'    
      type: string    
      x-ngsi:    
        type: Property    
    cyclePathPlacement:    
      description: 'Describes the placement of cycle track along the road segment corresponding to this observation. Enum:'' [''RIGHT, LEFT, BOTH, NOT_AVAILABLE'''    
      enum:    
        - BOTH    
        - LEFT    
        - NOT_AVAILABLE    
        - RIGHT    
      type: string    
      x-ngsi:    
        type: Property    
    cyclePathRightHeight:    
      description: 'Height of the cycle track on the right edge of the road corresponding to this observation.'    
      type: number    
      x-ngsi:    
        type: Property    
    cyclePathRightWidth:    
      description: 'Width of the cycle track on the right edge of the road corresponding to this observation.'    
      type: number    
      x-ngsi:    
        type: Property    
    dataDescriptor:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'URI pointing to the data-descriptor entity'    
      x-ngsi:    
        type: Relationship    
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
    endKilometer:    
      description: 'The kilometer number (measured from the road''s start point) where this road segment ends. '    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    endPoint:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf: &roadsegment_-_properties_-_location_-_oneof    
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
    id:    
      anyOf: &roadsegment_-_properties_-_owner_-_items_-_anyof    
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
    image:    
      description: 'An image of the item'    
      format: uri    
      type: string    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Property    
    laneInfo:    
      description: 'Describes the aspects of lanes of the road corresponding to this observation.'    
      properties:    
        laneDirection:    
          description: 'Property. Describes the direction in which vehicles are plying on the lane corresponding to this observation. Enum:''FORWARD, BACKWARD, INBOUND, OUTBOUND, RIGHT, LEFT'''    
          enum:    
            - BACKWARD    
            - FORWARD    
            - INBOUND    
            - LEFT    
            - OUTBOUND    
            - RIGHT    
          laneLength:    
            description: 'Property. Length of the lane corresponding to this observation.'    
            type: number    
          laneWidth:    
            description: 'Property. Width of the lane corresponding to this observation.'    
            type: number    
          type: string    
        laneId:    
          description: 'Property. Unique identification number of the lane corresponding to this observation.'    
          type: number    
      type: object    
      x-ngsi:    
        type: Property    
    laneUsage:    
      description: 'This attribute can be used to convey specific parameters describing each lane. It must contain a string per road segment lane. The element 0 of the array must contain the information of lane 1, and so on. Format of the referred string must be: <lane_direction>, <lane_minimumAllowedSpeed>, <lane_maximumAllowedSpeed>, <lane_maximumAllowedHeight>, <lane_maximumAllowedWeight>. <lane_direction> is a text string with the following allowed values: `forward`. The lane is currently used in the `forwards` direction. `backward`. The lane is currently used in the `backwards` direction. The only mandatory parameter is `lane_direction`. If not specified, the rest of parameters can be assumed to be equal to those specified at entity level.'    
      items:    
        enum:    
          - forward    
          - backward    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    length:    
      description: 'Total length of this road segment in kilometers'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/length    
        type: Property    
        units: 'Kilometer (Km)'    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf: *roadsegment_-_properties_-_location_-_oneof    
      x-ngsi:    
        type: Geoproperty    
    maximumAllowedHeight:    
      description: 'Maximum allowed height for vehicles transiting this road segment'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/height    
        type: Property    
        units: 'Meter (m)'    
    maximumAllowedSpeed:    
      description: 'Maximum allowed speed plying the road segment. More restrictive limits might be applied to specific vehicle types (trucks, caravans, etc.)'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: 'Kilometer per hour (Km/h)'    
    maximumAllowedWeight:    
      description: 'Maximum allowed weight for vehicles transiting this road segment'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/weight    
        type: Property    
        units: 'Kilogram (Kg)'    
    maximumAllowedWidth:    
      description: 'Maximum allowed width for vehicles using the entity corresponding to this observation.'    
      type: number    
      x-ngsi:    
        type: Property    
    medianHeight:    
      description: 'Height of the median or central reservation in the road corresponding to this observation.'    
      type: number    
      x-ngsi:    
        type: Property    
    medianLength:    
      description: 'Length of the median or central reservation in the road corresponding to this observation.'    
      type: number    
      x-ngsi:    
        type: Property    
    medianWidth:    
      description: 'Width of the median or central reservation in the road corresponding to this observation.'    
      type: number    
      x-ngsi:    
        type: Property    
    minimumAllowedSpeed:    
      description: 'Minimum allowed speed while transiting this road segment'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: 'Kilometer per hour (Km/h)'    
    municipalityInfo:    
      description: 'Municipality information corresponding to this observation.'    
      properties:    
        cityId:    
          description: 'Property. Model:''https://schema.org/Text''. City ID corresponding to this observation.'    
          type: string    
        cityName:    
          description: 'Property. Model:''https://schema.org/Text''. City name corresponding to this observation'    
          type: string    
        district:    
          description: 'Property. Model:''https://schema.org/Text''. District name corresponding to this observation.'    
          type: string    
        stateName:    
          description: 'Property. Model:''https://schema.org/Text''. Name of the state corresponding to this observation.'    
          type: string    
        ulbName:    
          description: 'Property. Model:''https://schema.org/Text''. Name of the Urban Local Body corresponding to this observation.'    
          type: string    
        wardId:    
          description: 'Property. Model:''https://schema.org/Text''. Ward ID corresponding to this observation.'    
          type: string    
        wardName:    
          description: 'Property. Model:''https://schema.org/Text''. Ward name corresponding to this observation.'    
          type: string    
        wardNum:    
          description: 'Property. Model:''https://schema.org/Number''. Ward number corresponding to this observation.'    
          type: number    
        zoneId:    
          description: 'Property. Model:''https://schema.org/Text''. Zone ID corresponding to this observation.'    
          type: string    
        zoneName:    
          description: 'Property. Model:''https://schema.org/Text''. Zone name corresponding to this observation.'    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *roadsegment_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    pedestrianPathLeftHeight:    
      description: 'Height of the walkway placed on the left edge of the road corresponding to this observation.'    
      type: number    
      x-ngsi:    
        type: Property    
    pedestrianPathLeftWidth:    
      description: 'Width of the walkway placed on the left edge of the road corresponding to this observation.'    
      type: number    
      x-ngsi:    
        type: Property    
    pedestrianPathMaterial:    
      description: 'Construction material used for laying the walkway / footpath on the sides of the road corresponding to this observation.'    
      type: string    
      x-ngsi:    
        type: Property    
    pedestrianPathPlacement:    
      description: 'Describes the presence and placement of pedestrian along the road segment corresponding to this observation. Enum:''RIGHT, LEFT, BOTH, NOT_AVAILABLE'''    
      type: string    
      x-ngsi:    
        type: Property    
    pedestrianPathRightHeight:    
      description: 'Height of the walkway placed on the right edge of the road corresponding to this observation.'    
      type: number    
      x-ngsi:    
        type: Property    
    pedestrianPathRightWidth:    
      description: 'Width of the walkway placed on the right edge of the road corresponding to this observation.'    
      type: number    
      x-ngsi:    
        type: Property    
    refRoad:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Road to which this road segment belongs to.'    
      x-ngsi:    
        type: Relationship    
    rightOfWayWidth:    
      description: 'Right of Way (RoW) is the total land area available for the roadway. Its width accommodates for carriages way + other necessities + future extension, along the road''s alignment.'    
      type: number    
      x-ngsi:    
        type: Property    
    roadClass:    
      description: 'The type of road corresponding to this observation. Enum: [OTHER_PUBLIC_ROAD, PRIVATE_ROAD, MINOR_CITY_ROAD, MAJOR_DISTRICT_ROAD, MAJOR_CITY_ROAD, NATIONAL_HIGHWAY, SERVICE_ROAD, STATE_HIGHWAY, OTHER_DISTRICT_ROAD, PORT_ROAD].'    
      enum:    
        - MAJOR_DISTRICT_ROAD    
        - MAJOR_CITY_ROAD    
        - MINOR_CITY_ROAD    
        - NATIONAL_HIGHWAY    
        - OTHER_DISTRICT_ROAD    
        - OTHER_PUBLIC_ROAD    
        - PORT_ROAD    
        - PRIVATE_ROAD    
        - SERVICE_ROAD    
        - STATE_HIGHWAY    
      type: string    
      x-ngsi:    
        type: Property    
    roadDirection:    
      description: 'Represents the direction the road is heading to. Enum:'' [''N, S, E, W''. The values N,S,E,W represent North,South,East,West respectively.'    
      type: string    
      x-ngsi:    
        type: Property    
    roadId:    
      description: 'Unique internal representation of the road corresponding to this observation.'    
      type: string    
      x-ngsi:    
        type: Property    
    roadMaterial:    
      description: 'The construction material used for laying the carriageway corresponding to this observation. For eg. concrete, earthen, tar etc.'    
      type: string    
      x-ngsi:    
        type: Property    
    roadName:    
      description: 'The name of the road corresponding to this observation.'    
      type: string    
      x-ngsi:    
        type: Property    
    roadWork:    
      description: 'Reasons for the road work in case of urgent intervention. A combination of these values. Enum:''COLLAPSE, DERAILMENT, FIRE, FLOOD, GASLEAK, LANDSLIDE, OTHER, POWERCUT, ROCKFALL, SAGGING, WATERLEAK''.'    
      enum:    
        - COLLAPSE    
        - DERAILMENT    
        - FIRE    
        - FLOOD    
        - GASLEAK    
        - LANDSLIDE    
        - OTHER    
        - POWERCUT    
        - ROCKFALL    
        - SAGGING    
        - WATERLEAK    
      type: string    
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
    startKilometer:    
      description: 'The kilometer number (measured from the road''s start point) where this road segment starts. '    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    startPoint:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf: *roadsegment_-_properties_-_location_-_oneof    
      x-ngsi:    
        type: Geoproperty    
    status:    
      description: 'Specific driving conditions on the roadsegment. Use statusDescription for additional information. Enum: ‘open, closed, limited’.  `open`: the roadsegment can be used in full intended capacity, `closed`: no traffic is possible, e.g. due to roadworks, an open bridge or lock, or any other event preventing traffic. `limited`: traffic is possible, but not in the full capacity.'    
      items:    
        enum:    
          - open    
          - closed    
          - limited    
        type: string    
      type: string    
      x-ngsi:    
        type: Property    
    statusDescription:    
      description: 'Additional information to the status attribute.'    
      type: string    
      x-ngsi:    
        type: Property    
    totalCyclePathWidth:    
      description: 'Total width of the cycle track present in the road corresponding to this observation.'    
      type: number    
      x-ngsi:    
        type: Property    
    totalLaneNumber:    
      description: 'Total number of lanes offered by this road segment'    
      minimum: 1    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number.    
        type: Property    
    totalPedestrianPathLength:    
      description: 'Total length of the walkway present in the road corresponding to this observation.'    
      type: number    
      x-ngsi:    
        type: Property    
    totalPedestrianPathWidth:    
      description: 'Total width of the walkway present in the road corresponding to this observation.'    
      type: number    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI Entity type. It has to be RoadSegment'    
      enum:    
        - RoadSegment    
      type: string    
      x-ngsi:    
        type: Property    
    width:    
      description: 'Road''s segment width.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: 'Meter (m)'    
  required:    
    - id    
    - name    
    - type    
    - refRoad    
    - startPoint    
    - endPoint    
    - allowedVehicleType    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Transportation/blob/master/RoadSegment/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Transportation/RoadSegment/schema.json    
  x-model-tags: IUDX    
  x-version: 0.4.1    
```  
</details>    
また、`laneUsage`プロパティや最大許容パラメータを伝えるプロパティは動的であり、例えば、交通状況を改善するために一時的にレーンの方向を変更することが可能である。  
## ペイロードの例  
#### RoadSegment NGSI-v2 key-value の例。  
ここでは、RoadSegmentをJSON-LD形式でkey-valuesとして表現した例を示す。これは、`options=keyValues`を使用した場合にNGSI-v2と互換性があり、個々のエンティティのコンテキストデータが返される。  
```json  
{  
  "id": "Spain-RoadSegment-A62-osm-24702186",  
  "type": "RoadSegment",  
  "name": "Valladolid-Dueñas",  
  "category": [  
    "oneway"  
  ],  
  "refRoad": "Spain-Road-A62",  
  "totalLaneNumber": 2,  
  "maximumAllowedSpeed": 120,  
  "minimumAllowedSpeed": 60,  
  "startPoint": {  
    "type": "Point",  
    "coordinates": [  
      -4.7299180606009,  
      41.6844918725019  
    ]  
  },  
  "endPoint": {  
    "type": "Point",  
    "coordinates": [  
      -4.55167335377909,  
      41.8570461783071  
    ]  
  },  
  "allowedVehicleType": [  
    "car",  
    "bus",  
    "lorry",  
    "trailer",  
    "tanker",  
    "van",  
    "caravan"  
  ],  
  "location": {  
    "type": "LineString",  
    "coordinates": [  
      [  
        -4.7299180606009,  
        41.6844918725019  
      ],  
      [  
        -4.72855890957602,  
        41.6860596957855  
      ],  
      [  
        -4.5520357341647,  
        41.8569278186523  
      ],  
      [  
        -4.55167335377909,  
        41.8570461783071  
      ]  
    ]  
  },  
  "laneUsage": [  
    "forward",  
    "forward"  
  ],  
  "source": "http://wwww.openstreetmap.org",  
  "status": "open",  
  "statusDescription": "Bridge state = DOWN",  
  "cyclePathMaterial": "ASPHALT",  
  "carriagewayLength": 0.095454461114818,  
  "totalPedestrianPathWidth": 7,  
  "bridgeCount": 1,  
  "pedestrianPathLeftHeight": 2,  
  "maximumAllowedHeight": 72,  
  "totalPedestrianPathLength": 0.09,  
  "culvertCount": 0,  
  "roadName": "GREEN VILLA ROAD TO CHAITHRAM HOUSE",  
  "roadClass": "OTHER_PUBLIC_ROAD",  
  "medianHeight": 3.6,  
  "roadWork": "OTHER",  
  "roadID": "5272",  
  "cyclePathRightWidth": 2.5,  
  "roadMaterial": "TAR",  
  "medianWidth": 1.5,  
  "carriagewayWidth": 3,  
  "cyclePathRightHeight": 1,  
  "roadDirection": "N",  
  "medianLength": 0.09,  
  "pedestrianPathMaterial": "PAVEMENT BLOCK",  
  "cyclePathLeftWidth": 2.5,  
  "maximumAllowedWidth": 74,  
  "rightOfWayWidth": 4,  
  "cyclePathLeftHeight": 1,  
  "maximumAllowedWeight": 109,  
  "pedestrianPathRightWidth": 3.5,  
  "pedestrianPathLeftWidth": 3.5,  
  "pedestrianPathPlacement": "NOT_AVAILABLE",  
  "pedestrianPathRightHeight": 2,  
  "cyclePathPlacement": "NOT_AVAILABLE",  
  "totalCyclePathWidth": 5,  
  "agency_name": "CORPORATION",  
  "municipalityInfo": {  
    "ulbName": "KANNUR MUNICIPAL CORPORATION"  
  }  
}  
```  
#### RoadSegment NGSI-v2 正規化例  
以下は、RoadSegmentをJSON-LD形式で正規化した例である。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "id": "Spain-RoadSegment-A62-osm-24702186",  
  "type": "RoadSegment",  
  "category": {  
    "value": [  
      "oneway"  
    ]  
  },  
  "endPoint": {  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -4.55167335377909,  
        41.8570461783071  
      ]  
    }  
  },  
  "name": {  
    "value": "Valladolid-Dueñas"  
  },  
  "startPoint": {  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -4.7299180606009,  
        41.6844918725019  
      ]  
    }  
  },  
  "allowedVehicleType": {  
    "value": [  
      "car",  
      "bus",  
      "lorry",  
      "trailer",  
      "tanker",  
      "van",  
      "caravan"  
    ]  
  },  
  "source": {  
    "value": "http://wwww.openstreetmap.org"  
  },  
  "totalLaneNumber": {  
    "value": 2  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "LineString",  
      "coordinates": [  
        [  
          -4.7299180606009,  
          41.6844918725019  
        ],  
        [  
          -4.72855890957602,  
          41.6860596957855  
        ],  
        [  
          -4.5520357341647,  
          41.8569278186523  
        ],  
        [  
          -4.55167335377909,  
          41.8570461783071  
        ]  
      ]  
    }  
  },  
  "minimumAllowedSpeed": {  
    "value": 60  
  },  
  "refRoad": {  
    "type": "Relationship",  
    "value": "Spain-Road-A62"  
  },  
  "maximumAllowedSpeed": {  
    "value": 120  
  },  
  "laneUsage": {  
    "value": [  
      "forward",  
      "forward"  
    ]  
  },  
  "status": {  
    "value": "open"  
  },  
  "statusDescription": {  
    "value": "Bridge state = DOWN"  
  },  
  "cyclePathMaterial": "ASPHALT",  
  "carriagewayLength": {  
    "type": "number",  
    "value": 0.095454461114818  
  },  
  "totalPedestrianPathWidth": {  
    "type": "number",  
    "value": 7  
  },  
  "bridgeCount": {  
    "type": "number",  
    "value": 1  
  },  
  "pedestrianPathLeftHeight": {  
    "type": "number",  
    "value": 2  
  },  
  "maximumAllowedHeight": {  
    "type": "number",  
    "value": 72  
  },  
  "totalPedestrianPathLength": {  
    "type": "number",  
    "value": 0.09  
  },  
  "culvertCount": {  
    "type": "number",  
    "value": 0  
  },  
  "roadName": {  
    "type": "string",  
    "value": "GREEN VILLA ROAD TO CHAITHRAM HOUSE"  
  },  
  "roadClass": {  
    "type": "string",  
    "value": "OTHER_PUBLIC_ROAD"  
  },  
  "medianHeight": {  
    "type": "number",  
    "value": 3.6  
  },  
  "roadWork": {  
    "type": "string",  
    "value": "OTHER"  
  },  
  "roadID": {  
    "type": "string",  
    "value": "5272"  
  },  
  "cyclePathRightWidth": {  
    "type": "number",  
    "value": 2.5  
  },  
  "roadMaterial": {  
    "type": "string",  
    "value": "TAR"  
  },  
  "medianWidth": {  
    "type": "number",  
    "value": 1.5  
  },  
  "carriagewayWidth": {  
    "type": "number",  
    "value": 3  
  },  
  "cyclePathRightHeight": {  
    "type": "number",  
    "value": 1  
  },  
  "roadDirection": {  
    "type": "string",  
    "value": "N"  
  },  
  "medianLength": {  
    "type": "number",  
    "value": 0.09  
  },  
  "pedestrianPathMaterial": {  
    "type": "string",  
    "value": "PAVEMENT BLOCK"  
  },  
  "cyclePathLeftWidth": {  
    "type": "number",  
    "value": 2.5  
  },  
  "maximumAllowedWidth": {  
    "type": "number",  
    "value": 74  
  },  
  "rightOfWayWidth": {  
    "type": "number",  
    "value": 4  
  },  
  "cyclePathLeftHeight": {  
    "type": "number",  
    "value": 1  
  },  
  "maximumAllowedWeight": {  
    "type": "number",  
    "value": 109  
  },  
  "pedestrianPathRightWidth": {  
    "type": "number",  
    "value": 3.5  
  },  
  "pedestrianPathLeftWidth": {  
    "type": "number",  
    "value": 3.5  
  },  
  "pedestrianPathPlacement": {  
    "type": "string",  
    "value": "NOT_AVAILABLE"  
  },  
  "pedestrianPathRightHeight": {  
    "type": "number",  
    "value": 2  
  },  
  "cyclePathPlacement": {  
    "type": "string",  
    "value": "NOT_AVAILABLE"  
  },  
  "totalCyclePathWidth": {  
    "type": "number",  
    "value": 5  
  },  
  "agency_name": {  
    "type": "string",  
    "value": "CORPORATION"  
  },  
  "municipalityInfo": {  
    "type": "StructuredValue",  
    "value": {  
      "ulbName": "KANNUR MUNICIPAL CORPORATION"  
    }  
  }  
}  
```  
#### RoadSegment NGSI-LD キー値例  
ここでは、RoadSegmentをJSON-LD形式でkey-valuesにした例を示す。これは、`options=keyValues`を使用した場合にNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "id": "urn:ngsi-ld:RoadSegment:Spain-RoadSegment-A62-osm-24702186",  
  "type": "RoadSegment",  
  "allowedVehicleType": [  
    "car",  
    "bus",  
    "lorry",  
    "trailer",  
    "tanker",  
    "van",  
    "caravan"  
  ],  
  "category": [  
    "oneway"  
  ],  
  "endPoint": {  
    "coordinates": [  
      -4.55167335377909,  
      41.8570461783071  
    ],  
    "type": "Point"  
  },  
  "laneUsage": [  
    "forward",  
    "forward"  
  ],  
  "location": {  
    "coordinates": [  
      [  
        -4.7299180606009,  
        41.6844918725019  
      ],  
      [  
        -4.72855890957602,  
        41.6860596957855  
      ],  
      [  
        -4.5520357341647,  
        41.8569278186523  
      ],  
      [  
        -4.55167335377909,  
        41.8570461783071  
      ]  
    ],  
    "type": "LineString"  
  },  
  "maximumAllowedSpeed": 120,  
  "minimumAllowedSpeed": 60,  
  "name": "Valladolid-DueÃ±as",  
  "refRoad": "urn:ngsi-ld:Road:Spain-Road-A62",  
  "source": "http://wwww.openstreetmap.org",  
  "startPoint": {  
    "coordinates": [  
      -4.7299180606009,  
      41.6844918725019  
    ],  
    "type": "Point"  
  },  
  "totalLaneNumber": 2,  
  "status": "open",  
  "statusDescription": "Bridge state = DOWN",  
  "cyclePathMaterial": "ASPHALT",  
  "carriagewayLength": 0.095454461114818,  
  "totalPedestrianPathWidth": 7,  
  "bridgeCount": 1,  
  "pedestrianPathLeftHeight": 2,  
  "maximumAllowedHeight": 72,  
  "totalPedestrianPathLength": 0.09,  
  "culvertCount": 0,  
  "roadName": "GREEN VILLA ROAD TO CHAITHRAM HOUSE",  
  "roadClass": "OTHER_PUBLIC_ROAD",  
  "medianHeight": 3.6,  
  "roadWork": "OTHER",  
  "roadID": "5272",  
  "cyclePathRightWidth": 2.5,  
  "roadMaterial": "TAR",  
  "medianWidth": 1.5,  
  "carriagewayWidth": 3,  
  "cyclePathRightHeight": 1,  
  "roadDirection": "N",  
  "medianLength": 0.09,  
  "pedestrianPathMaterial": "PAVEMENT BLOCK",  
  "cyclePathLeftWidth": 2.5,  
  "maximumAllowedWidth": 74,  
  "rightOfWayWidth": 4,  
  "cyclePathLeftHeight": 1,  
  "maximumAllowedWeight": 109,  
  "pedestrianPathRightWidth": 3.5,  
  "pedestrianPathLeftWidth": 3.5,  
  "pedestrianPathPlacement": "NOT_AVAILABLE",  
  "pedestrianPathRightHeight": 2,  
  "cyclePathPlacement": "NOT_AVAILABLE",  
  "totalCyclePathWidth": 5,  
  "agency_name": "CORPORATION",  
  "municipalityInfo": {  
    "ulbName": "KANNUR MUNICIPAL CORPORATION"  
  },  
  "@context": [  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### 道路セグメント NGSI-LD 正規化例  
以下は、RoadSegmentをJSON-LD形式で正規化した例である。これはオプションを使用しない場合、NGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
	"id": "urn:ngsi-ld:RoadSegment:Spain-RoadSegment-A62-osm-24702186",  
	"type": "RoadSegment",  
	"allowedVehicleType": {  
		"type": "Property",  
		"value": [  
			"car",  
			"bus",  
			"lorry",  
			"trailer",  
			"tanker",  
			"van",  
			"caravan"  
		]  
	},  
	"category": {  
		"type": "Property",  
		"value": [  
			"oneway"  
		]  
	},  
	"endPoint": {  
		"type": "Property",  
		"value": {  
			"type": "Point",  
			"coordinates": [  
				-4.55167335377909,  
				41.8570461783071  
			]  
		}  
	},  
	"laneUsage": {  
		"type": "Property",  
		"value": [  
			"forward",  
			"forward"  
		]  
	},  
	"location": {  
		"type": "GeoProperty",  
		"value": {  
			"type": "LineString",  
			"coordinates": [  
				[  
					-4.7299180606009,  
					41.6844918725019  
				],  
				[  
					-4.72855890957602,  
					41.6860596957855  
				],  
				[  
					-4.5520357341647,  
					41.8569278186523  
				],  
				[  
					-4.55167335377909,  
					41.8570461783071  
				]  
			]  
		}  
	},  
	"maximumAllowedSpeed": {  
		"type": "Property",  
		"value": 120  
	},  
	"minimumAllowedSpeed": {  
		"type": "Property",  
		"value": 60  
	},  
	"name": {  
		"type": "Property",  
		"value": "Valladolid-DueÃ±as"  
	},  
	"refRoad": {  
		"type": "Relationship",  
		"object": "urn:ngsi-ld:Road:Spain-Road-A62"  
	},  
	"source": {  
		"type": "Property",  
		"value": "http://wwww.openstreetmap.org"  
	},  
	"startPoint": {  
		"type": "Property",  
		"value": {  
			"type": "Point",  
			"coordinates": [  
				-4.7299180606009,  
				41.6844918725019  
			]  
		}  
	},  
	"totalLaneNumber": {  
		"type": "Property",  
		"value": 2  
	},  
	"status": {  
		"type": "Property",  
		"value": "open"  
	},  
	"statusDescription": {  
		"type": "Property",  
		"value": "Bridge state = DOWN"  
	},  
	"carriagewayLength": {  
    "type": "Property",  
    "value": 0.095454461114818  
  },  
  "totalPedestrianPathWidth": {  
    "type": "Property",  
    "value": 7  
  },  
  "bridgeCount": {  
    "type": "Property",  
    "value": 1  
  },  
  "pedestrianPathLeftHeight": {  
    "type": "Property",  
    "value": 2  
  },  
  "maximumAllowedHeight": {  
    "type": "Property",  
    "value": 72  
  },  
  "totalPedestrianPathLength": {  
    "type": "Property",  
    "value": 0.09  
  },  
  "culvertCount": {  
    "type": "Property",  
    "value": 0  
  },  
  "roadName": {  
    "type": "Property",  
    "value": "GREEN VILLA ROAD TO CHAITHRAM HOUSE"  
  },  
  "roadClass": {  
    "type": "Property",  
    "value": "OTHER_PUBLIC_ROAD"  
  },  
  "medianHeight": {  
    "type": "Property",  
    "value": 3.6  
  },  
  "roadWork": {  
    "type": "Property",  
    "value": "OTHER"  
  },  
  "roadID": {  
    "type": "Property",  
    "value": "5272"  
  },  
  "cyclePathRightWidth": {  
    "type": "Property",  
    "value": 2.5  
  },  
  "roadMaterial": {  
    "type": "Property",  
    "value": "TAR"  
  },  
  "medianWidth": {  
    "type": "Property",  
    "value": 1.5  
  },  
  "carriagewayWidth": {  
    "type": "Property",  
    "value": 3  
  },  
  "cyclePathRightHeight": {  
    "type": "Property",  
    "value": 1  
  },  
  "roadDirection": {  
    "type": "Property",  
    "value": "N"  
  },  
  "medianLength": {  
    "type": "Property",  
    "value": 0.09  
  },  
  "pedestrianPathMaterial": {  
    "type": "Property",  
    "value": "PAVEMENT BLOCK"  
  },  
  "cyclePathLeftWidth": {  
    "type": "Property",  
    "value": 2.5  
  },  
  "maximumAllowedWidth": {  
    "type": "Property",  
    "value": 74  
  },  
  "rightOfWayWidth": {  
    "type": "Property",  
    "value": 4  
  },  
  "cyclePathLeftHeight": {  
    "type": "Property",  
    "value": 1  
  },  
  "maximumAllowedWeight": {  
    "type": "Property",  
    "value": 109  
  },  
  "pedestrianPathRightWidth": {  
    "type": "Property",  
    "value": 3.5  
  },  
  "pedestrianPathLeftWidth": {  
    "type": "Property",  
    "value": 3.5  
  },  
  "pedestrianPathPlacement": {  
    "type": "Property",  
    "value": "NOT_AVAILABLE"  
  },  
  "pedestrianPathRightHeight": {  
    "type": "Property",  
    "value": 2  
  },  
  "cyclePathPlacement": {  
    "type": "Property",  
    "value": "NOT_AVAILABLE"  
  },  
  "totalCyclePathWidth": {  
    "type": "Property",  
    "value": 5  
  },  
  "agency_name": {  
    "type": "Property",  
    "value": "CORPORATION"  
  },  
 "municipalityInfo": {  
    "type": "Property",  
    "value": {  
      "ulbName": "KANNUR MUNICIPAL CORPORATION"  
    }  
  },  
	"@context": [  
		"https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
		"https://raw.githubusercontent.com/smart-data-models/dataModel.Transportation/master/context.jsonld"  
	]  
}  
```  
マグニチュード単位の扱いについては、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照してください。  
