エンティティトラフィックバイオレーション  
====================  
[オープンライセンス](https://github.com/smart-data-models//dataModel.Transportation/blob/master/TrafficViolation/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
グローバルな記述です。**都市で登録された交通違反と発生したE-Challanのデータモデルです。  

## プロパティのリスト  

- `address`: 郵送先住所  - `alternateName`: このアイテムの別称  - `amountCollected`: この観測に対応するサービスに向けて収集された金額。  - `areaServed`: サービスや提供されるアイテムが提供される地理的なエリア  - `dataProvider`: 調和されたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified`: エンティティが最後に変更された時のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `description`: このアイテムの説明  - `equipmentId`: この観測に対応する機器のユニークID。  - `equipmentType`: 機器の種類、またはこの観測に対応する機器の名前。  - `id`: エンティティのユニークな識別子  - `location`: アイテムへのGeojson参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygonのいずれかです。  - `mediaURL`: 苦情や場所に関する画像やメディアの詳細情報を提供するURL。  - `name`: このアイテムの名前です。  - `observationDateTime`: 最後に報告された観測時刻。  - `owner`: オーナーのIDを参照するJSONエンコードされた文字列を含むリスト  - `paymentStatus`: この観測に対応する罰金や違反金、チャランの支払い状況です。Enum:'Paid, Unpaid'.  - `reportId`: このオブザベーションに対応する課題、レポート、フィードバック、トランザクションに割り当てられた一意のID。  - `seeAlso`: アイテムに関する追加リソースを示すuriのリスト  - `source`: エンティティデータのオリジナルソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `titleCode`: この観測結果に対応するタイトルに割り当てられたコードです。  - `type`: NGSIエンティティタイプ。それはTrafficViolationでなければならない。    
必須項目  
- `id`  - `type`  ## データモデルによるプロパティの記述  
アルファベット順（クリックすると詳細が表示されます）  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
TrafficViolation:    
  description: 'A Data Model for Traffic Violations registered and E-Challans generated in Cities.'    
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
    amountCollected:    
      description: 'Amount collected towards the service corresponding to this observation.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
    equipmentId:    
      description: 'Unique Id of the equipment corresponding to this observation.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    equipmentType:    
      description: 'Type of equipment or the name of the equipment corresponding to this observation.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    id:    
      anyOf: &trafficviolation_-_properties_-_owner_-_items_-_anyof    
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
    mediaURL:    
      description: 'URL providing further information of any image(s) or media of the complaint or place.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    observationDateTime:    
      description: 'Last reported time of observation.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *trafficviolation_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    paymentStatus:    
      description: ' The payment status of the fine or violation or challan corresponding to this observation. Enum:''Paid, Unpaid''.'    
      enum:    
        - Paid    
        - Unpaid    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    reportId:    
      description: 'Unique Id assigned for the issue or report or feedback or transaction corresponding to this observation.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
    titleCode:    
      description: 'The code assigned to the title corresponding to this observation.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    type:    
      description: 'NGSI entity type. It has to be TrafficViolation.'    
      enum:    
        - TrafficViolation    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Transportation/blob/master/TrafficViolation/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Transportation/TrafficViolations/schema.json    
  x-model-tags: IUDX    
  x-version: 0.0.1    
```  
</details>    
## ペイロードの例  
#### TrafficViolation NGSI-v2 key-valuesの例  
ここではTrafficViolationをkey-valuesとしてJSON-LD形式にした例を紹介します。これは`options=keyValues`を使った場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "id": "ngsi-ld:Trafficviolation:234R:0212",  
  "type": "TrafficViolation",  
  "amountCollected": 10500,  
  "mediaURL": "https://www.google.com/",  
  "equipmentId": "4",  
  "equipmentType": "Camera",  
  "titleCode": "11",  
  "reportId": "182",  
  "observationDateTime": "2021-03-11T15:51:02+05:30",  
  "paymentStatus": "Paid"  
}  
```  
#### TrafficViolation NGSI-v2 正規化例  
ここでは、正規化されたJSON-LD形式のTrafficViolationの例を示します。これは、オプションを使用しない場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "id": "ngsi-ld:Trafficviolation:234R:0212",  
  "type": "TrafficViolation",  
  "amountCollected": {  
    "type": "number",  
    "value": 10500  
  },  
  "mediaURL": {  
    "type": "Text",  
    "value": "https://www.google.com/"  
  },  
  "equipmentId": {  
    "type": "Text",  
    "value": "4"  
  },  
  "equipmentType": {  
    "type": "Text",  
    "value": "Camera"  
  },  
  "titleCode": {  
    "type": "Text",  
    "value": "11"  
  },  
  "reportId": {  
    "type": "Text",  
    "value": "182"  
  },  
  "observationDateTime": {  
    "type": "DateTime",  
    "value": "2021-03-11T15:51:02+05:30"  
  },  
  "paymentStatus": {  
    "type": "Text",  
    "value": "Paid"  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### TrafficViolation NGSI-LDのキーバリューの例  
ここではTrafficViolationをkey-valuesとしてJSON-LD形式にした例を紹介します。これは、`options=keyValues`を使った場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "id": "ngsi-ld:Trafficviolation:234R:0212",  
  "type": "TrafficViolation",  
  "amountCollected": 10500,  
  "mediaURL": "https://www.google.com/",  
  "equipmentId": "4",  
  "equipmentType": "Camera",  
  "titleCode": "11",  
  "reportId": "182",  
  "observationDateTime": "2021-03-11T15:51:02+05:30",  
  "paymentStatus": "Paid",  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### TrafficViolation NGSI-LDの正規化例  
ここでは、正規化されたJSON-LD形式のTrafficViolationの例を示します。これはオプションを使用しない場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "id": "ngsi-ld:Trafficviolation:234R:0212",  
  "type": "TrafficViolation",  
  "amountCollected": {  
    "type": "Property",  
    "value": 10500  
  },  
  "mediaURL": {  
    "type": "Property",  
    "value": "https://www.google.com/"  
  },  
  "equipmentId": {  
    "type": "Property",  
    "value": "4"  
  },  
  "equipmentType": {  
    "type": "Property",  
    "value": "Camera"  
  },  
  "titleCode": {  
    "type": "Property",  
    "value": "11"  
  },  
  "reportId": {  
    "type": "Property",  
    "value": "182"  
  },  
  "observationDateTime": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2021-03-11T15:51:02+05:30"  
    }  
  },  
  "paymentStatus": {  
    "type": "Property",  
    "value": "Paid"  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
