エンティティ道路セグメント  
=============  
[オープンライセンス](https://github.com/smart-data-models//dataModel.Transportation/blob/master/RoadSegment/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
グローバルな記述。**このエンティティは、道路セグメントの地理的および文脈的な記述を含んでいます。道路セグメントのコレクションは、道路を記述するために使用されます。**  

## プロパティのリスト  

- `address`: 郵送先住所  - `allowedVehicleType`: この道路セグメントを通過することが許可されている車両タイプ。Enum:'agriculturalVehicle, bicycle, bus, car, caravan, carWithCaravan, carWithTrailer, constructionOrMaintenanceVehicle, lorry, moped, motorcycle, motorcycleWithSideCar, motorscooter, tanker, trailer, van, anyVehicle'.許可される値VehicleTypeEnum_, [DATEX 2 version 2.3](http://d2docs.ndwcloud.nu/)で定義された以下の値。  - `alternateName`: このアイテムの別称  - `annotations`: アイテムに関するアノテーション  - `areaServed`: サービスや提供されるアイテムが提供される地理的なエリア  - `category`: 道路セグメントの特別な特性を伝えることができます。Enum:'oneway, toll, link'.  oneway`:道路セグメントが一方向にしか使用できないかどうかを示すフラグです。存在しない場合は、道路セグメントが両方向(前方と後方)に使用できることを意味します。[http://wiki.openstreetmap.org/wiki/Key:oneway](http://wiki.openstreetmap.org/wiki/Key:oneway)も参照してください。toll` : その道路セグメントが有料であるかどうかを示します。link` : この道路セグメントが、道路を出たり入ったりするための補助的なリンクセグメントであるかどうかを表示します。[https://wiki.openstreetmap.org/wiki/Tag:highway%3Dmotorway_link](https://wiki.openstreetmap.org/wiki/Tag:highway%3Dmotorway_link)を参照してください。アプリケーションにとって意味のあるその他の値です。  - `color`: 商品の色について  - `dataProvider`: 調和されたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified`: エンティティが最後に変更された時のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `description`: このアイテムの説明  - `endKilometer`: この道路セグメントが終了するキロ数（道路の始点からの測定値）。  - `endPoint`: アイテムへのGeojson参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygonのいずれかです。  - `id`: エンティティのユニークな識別子  - `image`: アイテムのイメージ  - `laneUsage`: この属性は、各車線を説明する特定のパラメータを伝えるために使用することができます。道路セグメントの車線ごとに文字列を含まなければならない。配列の要素0には、車線1の情報が含まれていなければならず、以下のようになります。参照する文字列のフォーマットは以下の通りです。<lane_direction>, <lane_minimumAllowedSpeed>, <lane_maximumAllowedSpeed>, <lane_maximumAllowedHeight>, <lane_maximumAllowedWeight>.<lane_direction>は文字列で，以下の値が許容されます。forward`.レーンは現在、`forwards`の方向で使用されています。backward`.レーンは現在、`backwards`の方向に使用されています。唯一の必須パラメータは `lane_direction` です。指定されていない場合、残りのパラメータはエンティティレベルで指定されたものと同じであるとみなすことができます。  - `length`: この道路セグメントの総延長（キロメートル  - `location`: アイテムへのGeojson参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygonのいずれかです。  - `maximumAllowedHeight`: この道路セグメントを通過する車両の最大許容高さ  - `maximumAllowedSpeed`: この道路セグメントを通過する際の最大許容速度。特定の車両タイプ（トラック、キャラバンなど）には、より厳しい制限が適用される場合があります。  - `maximumAllowedWeight`: この道路セグメントを通過する車両の最大許容重量  - `minimumAllowedSpeed`: この道路セグメントを通過する際の最低許容速度  - `name`: このアイテムの名前です。  - `owner`: オーナーのIDを参照するJSONエンコードされた文字列を含むリスト  - `refRoad`: この道路セグメントが所属する道路  - `seeAlso`: アイテムに関する追加リソースを示すuriのリスト  - `source`: エンティティデータのオリジナルソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `startKilometer`: この道路セグメントの始点となる（道路の始点から測った）キロメーター番号。  - `startPoint`: アイテムへのGeojson参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygonのいずれかです。  - `status`: 道路セグメント上の特定の走行条件。追加情報には statusDescription を使用する。Enum: 'open, closed, limited'.  open`: 道路セグメントは意図された容量で完全に使用することができます。`closed`: 道路工事、橋やロックの開放、またはその他のイベントによる交通の妨げなどの理由で、交通は不可能です。限定的」：交通は可能だが、完全な容量ではない。  - `statusDescription`: status属性への追加情報。  - `totalLaneNumber`: この道路セグメントが提供する総レーン数  - `type`: NGSI エンティティタイプ。これはRoadSegmentでなければならない。  - `width`: 道路のセグメント幅    
必須項目  
- `allowedVehicleType`  - `endPoint`  - `id`  - `name`  - `refRoad`  - `startPoint`  - `type`    
道路セグメントには複数の車線が含まれることがあります。このデータモデルでは、異種の車線（使用方法、速度、高さなどが異なる）で構成された道路セグメントを伝えることができます。車線は1からnまでの整数で識別され、1番の車線は前方に向かって右側の車線となります。前進方向とは、セグメントの始点から終点までのベクトルで示される方向のことです。これは、OpenStreetMapで使用されているものと同じです。このエンティティは、主に自動車およびスマートシティの垂直セグメントと関連するIoTアプリケーションに関連しています。このデータモデルは、携帯電話事業者およびGSMAの協力を得て開発されました。  
## データモデルによるプロパティの記述  
アルファベット順（クリックすると詳細が表示されます）  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
RoadSegment:    
  description: 'This entity contains a harmonised geographic and contextual description of a road segment. A collection of road segments are used to describe a Road. '    
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
      description: 'Maximum allowed speed while transiting this road segment. More restrictive limits might be applied to specific vehicle types (trucks, caravans, etc.)'    
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
    minimumAllowedSpeed:    
      description: 'Minimum allowed speed while transiting this road segment'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: 'Kilometer per hour (Km/h)'    
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
    totalLaneNumber:    
      description: 'Total number of lanes offered by this road segment'    
      minimum: 1    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number.    
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
  x-model-tags: ""    
  x-version: 0.3.0    
```  
</details>    
プロパティ`laneUsage`と最大許容パラメータを伝えるものは、動的なものにすることができます。例えば、交通状況を改善するために車線の方向を一時的に変更することができます。  
## ペイロードの例  
#### RoadSegment NGSI-v2 key-valuesの例。  
RoadSegmentをkey-valuesとしてJSON-LD形式で出力した例です。これは、`options=keyValues`を使用した場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
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
	"statusDescription": "Bridge state = DOWN"  
}  
```  
#### RoadSegment NGSI-v2 正規化例  
ここでは、正規化されたJSON-LD形式のRoadSegmentの例を示します。これは、オプションを使用しない場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
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
	}  
}  
```  
#### RoadSegment NGSI-LDのキーバリューの例。  
RoadSegmentをkey-valuesとしてJSON-LD形式で表現した例です。これは、`options=keyValues`を使用した場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
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
	"@context": [  
		"https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
	]  
}  
```  
#### RoadSegment NGSI-LD 正規化例  
ここでは、正規化されたJSON-LD形式のRoadSegmentの例を示します。これは、オプションを使用しない場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
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
	"@context": [  
		"https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
		"https://raw.githubusercontent.com/smart-data-models/dataModel.Transportation/master/context.jsonld"  
	]  
}  
```  
マグニチュード単位の扱いについては、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照してください。  
