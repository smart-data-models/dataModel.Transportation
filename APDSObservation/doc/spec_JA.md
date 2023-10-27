<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティAPDSObservation  
=====================<!-- /10-Header -->  
<!-- 15-License -->  
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.Transportation/blob/master/APDSObservation/LICENSE.md)  
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバル記述：**このエンティティは一組の ANPR カメラの特定の観測をモデル化する。観測は複数の ANPR カメラで行われるかもしれないが、1 台の車両の観測に限定される。APDS データモデル https://www.allianceforparkingdatastandards.org/** を実装している。  
バージョン: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティのリスト  

<sup><sub>[*] 属性に型がない場合は、複数の型があるか、異なるフォーマット/パターンがある可能性があるためです</sub></sup>。  
- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国。例えば、スペイン  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 番地がある地域と、その地域に含まれる地域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: その地域がある地域、またその国がある地域  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 地区とは行政区画の一種で、国によっては地方自治体によって管理されている。    
	- `postOfficeBoxNumber[string]`: 私書箱の住所のための私書箱番号。例：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 郵便番号。例：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 番地  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 公道上の特定の物件を特定する番号    
- `alternateName[string]`: この項目の別名  - `areaServed[string]`: サービスまたは提供品が提供される地理的地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `creator[string]`: 現在のドライバーのID。  - `dataProvider[string]`: ハーモナイズされたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated[date-time]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified[date-time]`: エンティティの最終変更のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: この商品の説明  - `id[*]`: エンティティの一意識別子  - `images[array]`: 画像へのリンクの配列。配列要素には、画像のURLと追加情報が含まれます。画像のURLの代わりに、画像そのものをbinaryContent属性に含めることができます。  - `location[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。  - `name[string]`: このアイテムの名前  - `observationDateTime[date-time]`: Observationが作成されたタイムスタンプ(UTC)。ObservationStartDateTimeとObservationEndDateTimeを使用しない場合は必須。  - `observationEndDateTime[date-time]`: 観測イベントが終了した日時(UTC)(例:9:33amに配達区域から出る車が観測された)。creationDateTimeを使用しない場合は必須。  - `observationStartDateTime[date-time]`: 観測が開始された日時(UTC)(例:午前8時1分に車が配達区域に入るのが観測された)。creationDateTimeを使用しない場合は必須。  - `observedCredentialCharacterConfidence[array]`: 個々の文字認識の信頼度。observedCredentialConfidence と同様、これはベンダー固有である。メタデータを使用して、信頼度をどのように解釈できるかを示す。  - `observedCredentialConfidence[number]`: 測定の全体的な信頼度。これはベンダーによって異なるが、常に0から1の間の値に再スケーリングされるべきである。この数値をどのように解釈すべきかを示すためにメタデータを使用する。Arvoo: range[0.0, 1.0](高ければ高いほど良い)。  - `observedCredentialCountry[string]`: 2文字のISO3166標準に従った国コード(https://www.iban.com/country-codes)。曖昧さを避けるため、国際車両登録コードは使用しないことに注意すること（https://en.wikipedia.org/wiki/International_vehicle_registration_code）。国コードを決定できない場合は、この属性に'XX'を設定する。  - `observedCredentialId[string]`: 参照される観察されたクレデンシャルへの固有識別子。クレデンシャルは observedCredentialType で指定され、RFID タグ、ペイステーションのチケット番号、ライ センスプレート番号などである。licensePlate の場合、アルファの数値（スペースやハイフンなし）のみが許可される。オプションで':'を使用して、例えばドイツ市章(https://www.europeanplates.com/information/german-city-codes.html)の位置を示すことができる。  - `observedCredentialType[string]`: オブザベーション内で参照されるクレデンシャルのタイプ。許容される値は APDS CredentialType で指定される。Enum:'バーコード、ブルートゥース、エチケット、ハングタグ、ライセンスプレート、許可証、qrCode、rfid、チケット、その他'  - `observedHeading[*]`: 車両が静止している場合（すなわち 'speed' 属性の値が '0' の場合）、heading 属性の値は '-1' でなければならない。(国連コード DD)  . Model: [https://schema.org/Number](https://schema.org/Number)- `observedLocation`:   	- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)  
	- `areaServed[string]`: サービスまたは提供品が提供される地理的地域  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `location[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。    
- `observedLocationPDOP[number]`: 観測された車両のGPS位置の精度。これは「Position Dilution Of Precision」(https: //ja.wikipedia.org/wiki/Dilution_of_precision_(navigation))として表される。(国連コード「MTR」）。  - `observedMethod[string]`: APDS(ObservationType)で定義される、この観測要素に記録された観測方法。Enum:'anpr、チョーク、視覚、スキャナー、rfTranspoder、その他'  - `observedSpeed[*]`: 観測された車両の現在速度の水平成分の大きさを示し、時速キロメートルで指定する。提供される場合、speed 属性の値は負でない実数でなければならない。何らかの理由で速度が一時的に不明な場合、'-1' を使用してもよい。(UNコードKMH）。  . Model: [https://schema.org/Number](https://schema.org/Number)- `observedVehicleColour[string]`: 観測された車両の色  - `observedVehicleMake[string]`: 観察された車両のメーカー  - `observedVehicleType[string]`: 車両の構造的特徴から見た車両のタイプ。これは車両カテゴリーとは異なる。列挙する：agriculturalVehicle, anyVehicle, articulatedVehicle, bicycle, binTrolley, bus, car, caravan, carOrLightVehicle, carWithCaravan, carWithTrailer, cleaningTrolley, constructionOrMaintenanceVehicle, fourWheelDrive, highSidedVehicle, lorry, minibus, moped, motorcycle、motorcycleWithSideCar, motorscooter, sweepingMachine, tanker, threeWheeledVehicle, trailer, tram, twoWheeledVehicle, trolley, van, vehicleWithoutCatalyticConverter, vehicleWithCaravan, vehicleWithTrailer, withEvenNumberedRegistrationPlates, withOddNumberedRegistrationPlates, other'.VehicleTypeEnum_および_VehicleTypeEnum2_、[DATEX 2 version 2.3](http://d2docs.ndwcloud.nu/_static/umlmodel/v2.3/index.htm)で定義され、他の用途のために拡張された以下の値。  . Model: [https://schema.org/Text](https://schema.org/Text)- `observer[string]`: この観察要素に記録された観察を行ったスキャンシステムの名称または識別。  - `observerCameras[array]`: 車両を検出したカメラ位置の配列。リストの最初のカメラが最も認識度が高い。車のカメラ位置を示すには、以下の略号を使用する：RF(右前)、RM(右中)、RB(右後)、LF(左前)、LM(左中)、LB(左後)。  - `observerDescription[string]`: 観察または観察者の詳細のためのフリーテキストの説明。例えば、特定のANPRスキャンカーの友好的な名前として使用できます。  - `observerHeading[*]`: 観測者の進行方向を表し、0 <= 'heading' < 360 で、真北を基準に時計回りで数える10進数で指定する。車両が静止している場合（つまり 'speed' 属性の値が '0' の場合）、heading 属性の値は '-1' でなければなりません。  . Model: [https://schema.org/Number](https://schema.org/Number)- `observerLocation`:   	- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)  
	- `areaServed[string]`: サービスまたは提供品が提供される地理的地域  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `location[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。    
- `observerLocationPDOP[number]`: 観測者のGPS位置の精度。「Position Dilution Of Precision（精度の位置希釈）」として表される(https: //ja.wikipedia.org/wiki/Dilution_of_precision_(navigation))。  - `observerSpeed[*]`: 観測者の現在速度の水平成分の大きさを表し、時速キロメートルで指定する。指定する場合、speed 属性の値は負でない実数でなければならない。何らかの理由で速度が一時的に不明な場合は、'-1' を使用してもよい。  . Model: [https://schema.org/Number](https://schema.org/Number)- `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリスト。  - `seeAlso[*]`: アイテムに関する追加リソースを指すURIのリスト  - `source[string]`: エンティティ・データの元のソースを URL として示す一連の文字。ソース・プロバイダの完全修飾ドメイン名、またはソース・オブジェクトの URL を推奨する。  - `towardsObserver[number]`: 1：観測車両がカメラの方向に移動、0：観測車両がカメラの方向から遠ざかる、-1：観測車両の方向が検出されない。  - `type[string]`: NGSI エンティティタイプ。APDSObservationでなければならない。  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必須プロパティ  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
このモデルは、特定の場所における特定の時刻の車両の観測データセットをキャプチャする。APDS（Alliance for Parking DataStandard）仕様から派生している。観測方法には、ALPR カメラ、目視観測、スキャナー、その他の観測手段が含まれる。  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順（クリックで詳細表示）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
APDSObservation:    
  description: 'This entity models a particular observation of a set of ANPR camera. The Observation might be done with several ANPR cameras, but is limited to the observation of ONE vehicle. It implements the APDS data model https://www.allianceforparkingdatastandards.org/'    
  properties:    
    address:    
      description: The mailing address    
      properties:    
        addressCountry:    
          description: 'The country. For example, Spain'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressCountry    
            type: Property    
        addressLocality:    
          description: 'The locality in which the street address is, and which is in the region'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressLocality    
            type: Property    
        addressRegion:    
          description: 'The region in which the locality is, and which is in the country'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressRegion    
            type: Property    
        district:    
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government'    
          type: string    
          x-ngsi:    
            type: Property    
        postOfficeBoxNumber:    
          description: 'The post office box number for PO box addresses. For example, 03578'    
          type: string    
          x-ngsi:    
            model: https://schema.org/postOfficeBoxNumber    
            type: Property    
        postalCode:    
          description: 'The postal code. For example, 24004'    
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
    creator:    
      description: Id of current driver.    
      type: string    
      x-ngsi:    
        type: Property    
    dataProvider:    
      description: A sequence of characters identifying the provider of the harmonised data entity    
      type: string    
      x-ngsi:    
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
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
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
        type: Property    
    images:    
      description: 'Array of links to images. The array element contain the URLs of the images and additional info. As an alternative to the images URL, the image itself can be included in the binaryContent attribute.'    
      items:    
        items:    
          description: Every element in the array of images    
          properties:    
            URL:    
              description: Uri of the image    
              format: uri    
              type: string    
              x-ngsi:    
                type: Property    
            binaryContent:    
              description: Binary format of the image content    
              format: uuencoded    
              type: string    
              x-ngsi:    
                type: Property    
            camId:    
              description: Identifier of the camera. It can be specified by the camera position (also used in the 'camera' attribute)    
              type: string    
              x-ngsi:    
                type: Property    
            distance:    
              description: The distance in meters from the observer    
              type: number    
              x-ngsi:    
                type: Property    
                units: meters    
            expiryDateTime:    
              description: Timestamp until which the URL is valid    
              format: date-time    
              type: string    
              x-ngsi:    
                type: Property    
            imageContent:    
              description: It specifies the content of the image    
              type: string    
              x-ngsi:    
                type: Property    
          type: object    
          x-ngsi:    
            type: Property    
        type: array    
      type: array    
      x-ngsi:    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: Geojson reference to the item. Point    
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
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. LineString    
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
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. Polygon    
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
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiPoint    
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
      x-ngsi:    
        type: GeoProperty    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    observationDateTime:    
      description: The timestamp the Observation was made (UTC). Mandatory if observationStartDateTime and observationEndDateTime are not used.    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    observationEndDateTime:    
      description: 'The date and time of the observation event ended(in UTC).(e.g.a car was observed to exit a delivery zone at 9: 33am). Mandatory if creationDateTime is not used.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    observationStartDateTime:    
      description: 'The date and time of the observation(in UTC)event started.(e.g.a car was observed to enter a delivery zone at 8: 01am). Mandatory if creationDateTime is not used.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    observedCredentialCharacterConfidence:    
      description: The confidence of individual character recognition. As with observedCredentialConfidence this is vendor specific. Use the metadata to indicate how the confidences can be interpreted.    
      items:    
        description: Every observation of the credential character confidence    
        maximum: 1    
        minimum: 0    
        type: number    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        type: Property    
    observedCredentialConfidence:    
      description: 'The overall confidence of the measurement. This can be vendor specific, but should always be rescaled to value between 0 en 1. Use the metadata to indicate how this number should be interpreted. Arvoo: range[0.0, 1.0](higher is better).'    
      maximum: 1    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    observedCredentialCountry:    
      description: 'Country Code following the 2 character ISO3166 standard (https://www.iban.com/country-codes). Note that the International vehicle registration code should not be used to avoid ambiguity (https://en.wikipedia.org/wiki/International_vehicle_registration_code). If the country-code could not be determined, set ''XX'' as for this attribute.'    
      type: string    
      x-ngsi:    
        type: Property    
    observedCredentialId:    
      description: 'Specific identifier to the referenced observed credential. The credential is specified by observedCredentialType and may be an RFID tag, ticket number from a paystation, license plate number, etc. In case of a licensePlate only alpha numerical values (no spaces or hyphens) are allowed. Optionally an '':'' can be used to indicate the position of e.g. the German City Seal (https://www.europeanplates.com/information/german-city-codes.html).'    
      type: string    
      x-ngsi:    
        type: Property    
    observedCredentialType:    
      description: 'Type of the credential referenced within  the observation. Allowed values are specified in the APDS CredentialType. Enum:''barcode, bluetooth, eticket, hangtag, licensePlate, permit, qrCode, rfid, ticket, other'''    
      enum:    
        - barcode    
        - bluetooth    
        - eticket    
        - hangtag    
        - licensePlate    
        - permit    
        - qrCode    
        - rfid    
        - ticket    
        - other    
      type: string    
      x-ngsi:    
        type: Property    
    observedHeading:    
      description: 'Denotes the direction of travel of the observer and is specified in decimal degrees, where 0 <= ''heading'' < 360, counting clockwise relative to the true north.If the vehicle is stationary(i.e. the value of the ''speed'' attribute is ''0''), then the value of the heading attribute must be equal to ''-1''. (UN code DD)'    
      oneOf:    
        - exclusiveMaximum: 360    
          maximum: 360    
          minimum: 0    
          type: number    
        - enum:    
            - -1    
          type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Degrees    
    observedLocation:    
      description: GPS position of the middle position of the scanned vehicle.    
      properties:    
        address:    
          description: The mailing address    
          properties:    
            addressCountry:    
              description: 'The country. For example, Spain'    
              type: string    
              x-ngsi:    
                model: https://schema.org/addressCountry    
                type: Property    
            addressLocality:    
              description: 'The locality in which the street address is, and which is in the region'    
              type: string    
              x-ngsi:    
                model: https://schema.org/addressLocality    
                type: Property    
            addressRegion:    
              description: 'The region in which the locality is, and which is in the country'    
              type: string    
              x-ngsi:    
                model: https://schema.org/addressRegion    
                type: Property    
            district:    
              description: 'A district is a type of administrative division that, in some countries, is managed by the local government'    
              type: string    
              x-ngsi:    
                type: Property    
            postOfficeBoxNumber:    
              description: 'The post office box number for PO box addresses. For example, 03578'    
              type: string    
              x-ngsi:    
                model: https://schema.org/postOfficeBoxNumber    
                type: Property    
            postalCode:    
              description: 'The postal code. For example, 24004'    
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
        areaServed:    
          description: The geographic area where a service or offered item is provided    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        location:    
          description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
          oneOf:    
            - bbox:    
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
            - bbox:    
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
            - bbox:    
                items:    
                  type: number    
                minItems: 4    
                type: array    
              coordinates:    
                items:    
                  items:    
                    items:    
                    minItems: 2    
                    type: array    
                  minItems: 4    
                  type: array    
                type: array    
              type:    
                enum:    
                  - Polygon    
                type: string    
            - bbox:    
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
            - bbox:    
                items:    
                  type: number    
                minItems: 4    
                type: array    
              coordinates:    
                items:    
                  items:    
                    items:    
                    minItems: 2    
                    type: array    
                  minItems: 2    
                  type: array    
                type: array    
              type:    
                enum:    
                  - MultiLineString    
                type: string    
            - bbox:    
                items:    
                  type: number    
                minItems: 4    
                type: array    
              coordinates:    
                items:    
                  items:    
                    items:    
                    minItems: 4    
                    type: array    
                  type: array    
                type: array    
              type:    
                enum:    
                  - MultiPolygon    
                type: string    
          x-ngsi:    
            type: GeoProperty    
      type: object    
      x-ngsi:    
        type: GeoProperty    
    observedLocationPDOP:    
      description: 'Accuracy of GPS position of the observed vehicle. This is expressed as ''Position Dilution Of Precision''(https: //en.wikipedia.org/wiki/Dilution_of_precision_(navigation)). (UN code ''MTR''). '    
      type: number    
      x-ngsi:    
        type: Property    
        units: meters    
    observedMethod:    
      description: 'The method of observation recorded for this observation element as defined by APDS (ObservationType). Enum:''anpr, chalk, visual, scanner, rfTranspoder, other'''    
      enum:    
        - anpr    
        - chalk    
        - other    
        - rfTranspoder    
        - scanner    
        - visual    
      type: string    
      x-ngsi:    
        type: Property    
    observedSpeed:    
      description: 'Denotes the magnitude of the horizontal component of the observed vehicles current velocity and is specified in kilometers per hour. If provided, the value of the speed attribute must be a non - negative real number.''-1'' MAY be used if speed is transiently unknown for some reason. (UN Code KMH).'    
      oneOf:    
        - minimum: 0    
          type: number    
        - maximum: -1    
          minimum: -1    
          type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: km/h    
    observedVehicleColour:    
      description: The colour of the observed vehicle    
      type: string    
      x-ngsi:    
        type: Property    
    observedVehicleMake:    
      description: The make of the observed vehicle    
      type: string    
      x-ngsi:    
        type: Property    
    observedVehicleType:    
      description: 'Type of vehicle from the point of view of its structural characteristics. This is different than the vehicle category . Enum:''agriculturalVehicle, anyVehicle, articulatedVehicle, bicycle, binTrolley, bus, car, caravan, carOrLightVehicle, carWithCaravan, carWithTrailer, cleaningTrolley, constructionOrMaintenanceVehicle, fourWheelDrive, highSidedVehicle, lorry, minibus, moped, motorcycle, motorcycleWithSideCar, motorscooter, sweepingMachine, tanker, threeWheeledVehicle, trailer, tram, twoWheeledVehicle, trolley, van, vehicleWithoutCatalyticConverter, vehicleWithCaravan, vehicleWithTrailer, withEvenNumberedRegistrationPlates, withOddNumberedRegistrationPlates, other''. The following values defined by _VehicleTypeEnum_ and _VehicleTypeEnum2_, [DATEX 2 version 2.3](http://d2docs.ndwcloud.nu/_static/umlmodel/v2.3/index.htm) and extended for other uses'    
      enum:    
        - agriculturalVehicle    
        - ambulance    
        - anyVehicle    
        - articulatedVehicle    
        - autorickshaw    
        - bicycle    
        - binTrolley    
        - BRT mini busÂ·    
        - BRT bus    
        - bus    
        - car    
        - caravan    
        - carOrLightVehicle    
        - carWithCaravan    
        - carWithTrailer    
        - cleaningTrolley    
        - compactor    
        - constructionOrMaintenanceVehicle    
        - dumper    
        - e-moped    
        - e-scooter    
        - e-motorcycle    
        - fireTender    
        - fourWheelDrive    
        - highSidedVehicle    
        - hopper    
        - lorry    
        - minibus    
        - moped    
        - motorcycle    
        - motorcycleWithSideCar    
        - motorscooter    
        - policeVan    
        - publicMotor    
        - sweepingMachine    
        - tanker    
        - tempo    
        - threeWheeledVehicle    
        - tipper    
        - trailer    
        - tram    
        - trolley    
        - twoWheeledVehicle    
        - van    
        - vehicleWithoutCatalyticConverter    
        - vehicleWithCaravan    
        - vehicleWithTrailer    
        - withEvenNumberedRegistrationPlates    
        - withOddNumberedRegistrationPlates    
        - other    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    observer:    
      description: The name or identification of the scanning system making the observation recorded in this observation element.    
      type: string    
      x-ngsi:    
        type: Property    
    observerCameras:    
      description: 'Array of camera positions that detected the vehicle.The first camera in the list has the best recognition.Use the following abbreviations to indicate the camera positioning on a car: RF(Right Front), RM(Right Middle), RB(Right Back), LF(Left Front), LM(Left Middle), LB(Left Back).'    
      items:    
        description: Every camera position    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        type: Property    
    observerDescription:    
      description: Free-text description for details of the observation or observer. Can e.g.be used as a friendly name of a specific ANPR scan car.    
      type: string    
      x-ngsi:    
        type: Property    
    observerHeading:    
      description: 'Denotes the direction of travel of the observer and is specified in decimal degrees, where 0 <= ''heading'' < 360, counting clockwise relative to the true north. If the vehicle is stationary(i.e. the value of the ''speed'' attribute is ''0''), then the value of the heading attribute must be equal to ''-1'''    
      oneOf:    
        - exclusiveMaximum: 360    
          maximum: 360    
          minimum: 0    
          type: number    
        - enum:    
            - -1    
          type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Degree.    
    observerLocation:    
      description: GPS position of the person or car equipped with the Camera/s that produce the observation.    
      properties:    
        address:    
          description: The mailing address    
          properties:    
            addressCountry:    
              description: 'The country. For example, Spain'    
              type: string    
              x-ngsi:    
                model: https://schema.org/addressCountry    
                type: Property    
            addressLocality:    
              description: 'The locality in which the street address is, and which is in the region'    
              type: string    
              x-ngsi:    
                model: https://schema.org/addressLocality    
                type: Property    
            addressRegion:    
              description: 'The region in which the locality is, and which is in the country'    
              type: string    
              x-ngsi:    
                model: https://schema.org/addressRegion    
                type: Property    
            district:    
              description: 'A district is a type of administrative division that, in some countries, is managed by the local government'    
              type: string    
              x-ngsi:    
                type: Property    
            postOfficeBoxNumber:    
              description: 'The post office box number for PO box addresses. For example, 03578'    
              type: string    
              x-ngsi:    
                model: https://schema.org/postOfficeBoxNumber    
                type: Property    
            postalCode:    
              description: 'The postal code. For example, 24004'    
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
        areaServed:    
          description: The geographic area where a service or offered item is provided    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        location:    
          description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
          oneOf:    
            - bbox:    
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
            - bbox:    
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
            - bbox:    
                items:    
                  type: number    
                minItems: 4    
                type: array    
              coordinates:    
                items:    
                  items:    
                    items:    
                    minItems: 2    
                    type: array    
                  minItems: 4    
                  type: array    
                type: array    
              type:    
                enum:    
                  - Polygon    
                type: string    
            - bbox:    
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
            - bbox:    
                items:    
                  type: number    
                minItems: 4    
                type: array    
              coordinates:    
                items:    
                  items:    
                    items:    
                    minItems: 2    
                    type: array    
                  minItems: 2    
                  type: array    
                type: array    
              type:    
                enum:    
                  - MultiLineString    
                type: string    
            - bbox:    
                items:    
                  type: number    
                minItems: 4    
                type: array    
              coordinates:    
                items:    
                  items:    
                    items:    
                    minItems: 4    
                    type: array    
                  type: array    
                type: array    
              type:    
                enum:    
                  - MultiPolygon    
                type: string    
          x-ngsi:    
            type: GeoProperty    
      type: object    
      x-ngsi:    
        type: GeoProperty    
    observerLocationPDOP:    
      description: 'Accuracy of the GPS position of the observer, expressed as ''Position Dilution Of Precision''(https: //en.wikipedia.org/wiki/Dilution_of_precision_(navigation))'    
      type: number    
      x-ngsi:    
        type: Property    
        units: meters.    
    observerSpeed:    
      description: 'Denotes the magnitude of the horizontal component of the observer current velocity and is specified in kilometers per hour. If provided, the value of the speed attribute must be a non - negative real number. ''-1'' MAY be used if speed is transiently unknown for some reason'    
      oneOf:    
        - minimum: 0    
          type: number    
        - maximum: -1    
          minimum: -1    
          type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: 'KMH '    
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
          type: Property    
      type: array    
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    towardsObserver:    
      description: '1: Observed vehicle moves in direction of camera, 0: Observed vehicle moves away direction of camera, -1: Observed vehicle direction not detected.'    
      enum:    
        - -1    
        - 0    
        - 1    
      type: number    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be APDSObservation    
      enum:    
        - APDSObservation    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: https://www.allianceforparkingdatastandards.org/    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Transportation/blob/master/APDSObservation/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Transportation/APDSObservation/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ペイロードの例  
#### APDSObservation NGSI-v2 キー値の例  
以下はJSON-LD形式のAPDSObservationのkey-valuesの例である。これはNGSI-v2と互換性があり、`options=keyValues`を使用すると個々のエンティティのコンテキストデータを返す。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "uri:ngsi-ld:APDSObservation:Arvoo:ArvooSGIDxxxx",  
  "type": "APDSObservation",  
  "creator": "25399",  
  "images": [  
    [  
      {  
        "URL": "http://10.1.0.11:7400/getimage?sgid=8775639&amp;camid=lf&amp;imgreqtype=anpr"  
      },  
      {  
        "camId": "LF"  
      },  
      {  
        "imageContent": "ANPR"  
      }  
    ],  
    [  
      {  
        "URL": "http://10.1.0.11:7400/getimage?sgid=8775639&amp;camid=lf&amp;imgreqtype=overview"  
      },  
      {  
        "camId": "LF"  
      },  
      {  
        "imageContent": "Overview"  
      }  
    ],  
    [  
      {  
        "URL": "http://10.1.0.11:7400/getimage?sgid=8775639&amp;camid=lf&amp;imgreqtype=plate"  
      },  
      {  
        "camId": "LF"  
      },  
      {  
        "imageContent": "Plate"  
      }  
    ],  
    [  
      {  
        "URL": "http://10.1.0.11:7400/getimage?sgid=8775639&amp;camid=plf&amp;distance=-5.22"  
      },  
      {  
        "camId": "LF"  
      },  
      {  
        "imageContent": "Panorama"  
      },  
      {  
        "distance": -5.22  
      }  
    ]  
  ],  
  "observationDateTime": "2020-09-11T10:45:00.00Z",  
  "observedCredentialCharacterConfidence": [  
    0.944,  
    0.851,  
    0.876,  
    0.950,  
    0.932,  
    0.936,  
    0.901  
  ],  
  "observedCredentialConfidence": 0.851,  
  "observedCredentialCountry": "BE",  
  "observedCredentialId": "1ENC003",  
  "observedCredentialType": "licensePlate",  
  "observedHeading": 175,  
  "observedLocation": {  
    "coordinates": [  
      4.00412077,  
      51.00216632  
    ],  
    "type": "Point"  
  },  
  "observedLocationPDOP": 0.2959945752,  
  "observedMethod": "anpr",  
  "observedSpeed": -1,  
  "observer": "Arvoo",  
  "observerCameras": [  
    "LF,LB"  
  ],  
  "observerDescription": "Scangenius Auto-26",  
  "observerHeading": 175,  
  "observerLocation": {  
    "coordinates": [  
      4.412077,  
      51.216632  
    ],  
    "type": "Point"  
  },  
  "observerLocationPDOP": 0.2959945752,  
  "observerSpeed": 26  
}  
```  
</details>  
#### APDSObservation NGSI-v2 正規化例  
以下は正規化されたJSON-LD形式のAPDSObservationの例である。これはNGSI-v2と互換性があり、オプションを使用しない場合、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
	"id": "uri:ngsi-ld:APDSObservation:Arvoo:ArvooSGIDxxxx",  
	"type": "APDSObservation",  
	"observedMethod": {  
		"type": "Text",  
		"value": "anpr"  
	},  
	"observedCredentialType": {  
		"type": "Text",  
		"value": "license plate"  
	},  
	"observedCredentialId": {  
		"type": "Text",  
		"value": "1ENC003"  
	},  
	"observedCredentialCountry": {  
		"type": "Text",  
		"value": "BE"  
	},  
	"observedCredentialConfidence": {  
		"type": "Number",  
		"value": 0.851,  
		"metadata": {  
			"confidenceMethod": {  
				"type": "Text",  
				"value": "Arvoo. Higher is better."  
			}  
		}  
	},  
	"observedCredentialCharacterConfidence": {  
		"type": "array",  
		"value": [  
			0.944,  
			0.851,  
			0.876,  
			0.950,  
			0.932,  
			0.936,  
			0.901  
		],  
		"metadata": {  
			"confidenceMethod": {  
				"type": "Text",  
				"value": "Arvoo"  
			}  
		}  
	},  
	"observer": {  
		"type": "Text",  
		"value": "Arvoo",  
		"metadata": {}  
	},  
	"observerDescription": {  
		"type": "Text",  
		"value": "Scangenius Auto-26"  
	},  
	"creator": {  
		"type": "Text",  
		"value": "25399"  
	},  
	"observerCameras": {  
		"type": "Array",  
		"value": [  
			"LF,LB"  
		]  
	},  
	"observationDateTime": {  
		"type": "DateTime",  
		"value": "2020-09-11T10:45:00.00Z"  
	},  
	"observerLocation": {  
		"type": "geo:json",  
		"value": {  
			"type": "Point",  
			"coordinates": [  
				4.412077,  
				51.216632  
			]  
		},  
		"metadata": {  
			"timestamp": {  
				"type": "DateTime",  
				"value": "2020-09-11T10:45:00.00Z"  
			}  
		}  
	},  
	"observerLocationPDOP": {  
		"type": "Number",  
		"value": 0.2959945752,  
		"metadata": {  
			"UnitCode": {  
				"type": "Text",  
				"value": "MTR"  
			}  
		}  
	},  
	"observerHeading": {  
		"type": "Number",  
		"value": 175  
	},  
	"observerSpeed": {  
		"type": "Number",  
		"value": 26,  
		"metadata": {  
			"UnitCode": {  
				"type": "Text",  
				"value": "KMH"  
			}  
		}  
	},  
	"observedLocation": {  
		"type": "geo:json",  
		"value": {  
			"type": "Point",  
			"coordinates": [  
				4.00412077,  
				51.00216632  
			]  
		},  
		"metadata": {  
			"timestamp": {  
				"type": "DateTime",  
				"value": "2020-09-11T10:45:00.00Z"  
			}  
		}  
	},  
	"observedLocationPDOP": {  
		"type": "Number",  
		"value": 0.2959945752,  
		"metadata": {  
			"UnitCode": {  
				"type": "Text",  
				"value": "MTR"  
			}  
		}  
	},  
	"observedHeading": {  
		"type": "Number",  
		"value": 175  
	},  
	"observedSpeed": {  
		"type": "Number",  
		"value": -1  
	},  
	"images": {  
		"type": "array",  
		"value": [  
			{  
			  "URL": "http://localhost:4000/getimage?sgid=984133&camid=lf&imgreqtype=anpr",  
			  "expiryDateTime": "2023-11-25T11:13:42.133Z",  
			  "camId": "LF",  
			  "imageContent": "ANPR"  
			},  
			{  
			  "URL": "http://localhost:4000/getimage?sgid=984133&camid=lf&imgreqtype=overview",  
			  "expiryDateTime": "2023-11-25T11:13:42.133Z",  
			  "camId": "LF",  
			  "imageContent": "Overview"  
			},  
			{  
			  "URL": "http://localhost:4000/getimage?sgid=984133&camid=lf&imgreqtype=plate",  
			  "expiryDateTime": "2023-11-25T11:13:42.133Z",  
			  "camId": "LF",  
			  "imageContent": "Plate"  
			},  
			{  
			  "URL": "http://localhost:4000/getimage?sgid=984133&camid=plf&distance=-3.23",  
			  "expiryDateTime": "2023-11-25T11:13:42.133Z",  
			  "camId": "LF",  
			  "imageContent": "Panorama",  
			  "distance": -3.232  
			}  
		]  
	}  
}  
```  
</details>  
#### APDSObservation NGSI-LD キー値の例  
以下はAPDSObservationをJSON-LD形式でkey-valuesとした例です。これはNGSI-LDと互換性があり、`options=keyValues`を使うと個々のエンティティのコンテキストデータを返す。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "uri:ngsi-ld:APDSObservation:Arvoo:ArvooSGIDxxxx",  
    "type": "APDSObservation",  
    "creator": "25399",  
    "images": [  
        [  
            {  
                "URL": "http://10.1.0.11:7400/getimage?sgid=8775639&amp;camid=lf&amp;imgreqtype=anpr"  
            },  
            {  
                "camId": "LF"  
            },  
            {  
                "imageContent": "ANPR"  
            }  
        ],  
        [  
            {  
                "URL": "http://10.1.0.11:7400/getimage?sgid=8775639&amp;camid=lf&amp;imgreqtype=overview"  
            },  
            {  
                "camId": "LF"  
            },  
            {  
                "imageContent": "Overview"  
            }  
        ],  
        [  
            {  
                "URL": "http://10.1.0.11:7400/getimage?sgid=8775639&amp;camid=lf&amp;imgreqtype=plate"  
            },  
            {  
                "camId": "LF"  
            },  
            {  
                "imageContent": "Plate"  
            }  
        ],  
        [  
            {  
                "URL": "http://10.1.0.11:7400/getimage?sgid=8775639&amp;camid=plf&amp;distance=-5.22"  
            },  
            {  
                "camId": "LF"  
            },  
            {  
                "imageContent": "Panorama"  
            },  
            {  
                "distance": -5.22  
            }  
        ]  
    ],  
    "observationDateTime": "2020-09-11T10:45:00.00Z",  
    "observedCredentialCharacterConfidence": [  
        0.944,  
        0.851,  
        0.876,  
        0.950,  
        0.932,  
        0.936,  
        0.901  
    ],  
    "observedCredentialConfidence": 851,  
    "observedCredentialCountry": "BE",  
    "observedCredentialId": "1ENC003",  
    "observedCredentialType": "license plate",  
    "observedHeading": 175,  
    "observedLocation": {  
        "coordinates": [  
            4.00412077,  
            51.00216632  
        ],  
        "type": "Point"  
    },  
    "observedLocationPDOP": 0.2959945752,  
    "observedMethod": "anpr",  
    "observedSpeed": -1,  
    "observer": "Arvoo",  
    "observerCameras": [  
        "LF,LB"  
    ],  
    "observerDescription": "Scangenius Auto-26",  
    "observerHeading": 175,  
    "observerLocation": {  
        "coordinates": [  
            4.412077,  
            51.216632  
        ],  
        "type": "Point"  
    },  
    "observerLocationPDOP": 0.2959945752,  
    "observerSpeed": 26,  
    "@context": [  
        ""  
    ]  
}  
```  
</details>  
#### APDSObservation NGSI-LD 正規化例  
以下は正規化されたJSON-LD形式のAPDSObservationの例です。これはオプションを使用しない場合のNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
	"id": "uri:ngsi-ld:APDSObservation:Arvoo:ArvooSGIDxxxx",  
	"type": "APDSObservation",  
	"observedMethod": {  
		"type": "Property",  
		"value": "anpr"  
	},  
	"observedCredentialType": {  
		"type": "Property",  
		"value": "license plate"  
	},  
	"observedCredentialId": {  
		"type": "Property",  
		"value": "1ENC003"  
	},  
	"observedCredentialCountry": {  
		"type": "Property",  
		"value": "BE"  
	},  
	"observedCredentialConfidence": {  
		"type": "Property",  
		"value": 0.851  
	},  
	"observedCredentialCharacterConfidence": {  
		"type": "Property",  
		"value": [  
			0.944,  
			0.851,  
			0.876,  
			0.950,  
			0.932,  
			0.936,  
			0.901  
		]  
	},  
	"observer": {  
		"type": "Property",  
		"value": "Arvoo"  
	},  
	"observerDescription": {  
		"type": "Property",  
		"value": "Scangenius Auto-26"  
	},  
	"creator": {  
		"type": "Property",  
		"value": "25399"  
	},  
	"observerCameras": {  
		"type": "Property",  
		"value": [  
			"LF,LB"  
		]  
	},  
	"observationDateTime": {  
		"type": "Property",  
		"value": {  
			"@type": "DateTime",  
			"@value": "2020-09-11T10:45:00.00Z"  
		}  
	},  
	"observerLocation": {  
		"type": "GeoProperty",  
		"value": {  
			"type": "Point",  
			"coordinates": [  
				4.412077,  
				51.216632  
			]  
		}  
	},  
	"observerLocationPDOP": {  
		"type": "Property",  
		"value": 0.2959945752  
	},  
	"observerHeading": {  
		"type": "Property",  
		"value": 175  
	},  
	"observerSpeed": {  
		"type": "Property",  
		"value": 26  
	},  
	"observedLocation": {  
		"type": "GeoProperty",  
		"value": {  
			"type": "Point",  
			"coordinates": [  
				4.00412077,  
				51.00216632  
			]  
		}  
	},  
	"observedLocationPDOP": {  
		"type": "Property",  
		"value": 0.2959945752  
	},  
	"observedHeading": {  
		"type": "Property",  
		"value": 175  
	},  
	"observedSpeed": {  
		"type": "Property",  
		"value": -1  
	},  
	"images": {  
		"type": "Property",  
		"value": [  
			{  
			  "URL": "http://localhost:4000/getimage?sgid=984133&camid=lf&imgreqtype=anpr",  
			  "expiryDateTime": "2023-11-25T11:13:42.133Z",  
			  "camId": "LF",  
			  "imageContent": "ANPR"  
			},  
			{  
			  "URL": "http://localhost:4000/getimage?sgid=984133&camid=lf&imgreqtype=overview",  
			  "expiryDateTime": "2023-11-25T11:13:42.133Z",  
			  "camId": "LF",  
			  "imageContent": "Overview"  
			},  
			{  
			  "URL": "http://localhost:4000/getimage?sgid=984133&camid=lf&imgreqtype=plate",  
			  "expiryDateTime": "2023-11-25T11:13:42.133Z",  
			  "camId": "LF",  
			  "imageContent": "Plate"  
			},  
			{  
			  "URL": "http://localhost:4000/getimage?sgid=984133&camid=plf&distance=-3.23",  
			  "expiryDateTime": "2023-11-25T11:13:42.133Z",  
			  "camId": "LF",  
			  "imageContent": "Panorama",  
			  "distance": -3.232  
			}  
		]  
	},  
	 "@context": [  
        ""  
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
