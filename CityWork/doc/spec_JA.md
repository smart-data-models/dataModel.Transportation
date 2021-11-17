エンティティシティワーク  
============  
[オープンライセンス](https://github.com/smart-data-models//dataModel.Transportation/blob/master/CityWork/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
グローバルな記述。**このデータモデルは、道路軸上で行われる都市工事の文脈的な説明であり、個人（自動車、オートバイ、自転車、....）や一般の交通機関（トラム、バス、地下鉄）に影響を与える可能性があります。GeoJSONオブジェクトには地理的な表現が含まれており、特定のJSONオブジェクトやよりグローバルなレベル（道路セグメント、道路、地区、...）での作業の位置を特定し、循環への潜在的な影響を評価することができます。GeoJSONオブジェクトは、空間の領域（Geometry）、空間的に境界のあるエンティティ（Feature）、またはフィーチャのリスト（Feature Collection）を表すことができます。モデル化と可能な値の詳細については、ドキュメント[geojson](https://tools.ietf.org/pdf/draft-ietf-geojson-03.pdf)を参照してください。  

## プロパティのリスト  

- `allowedVehicle`: 循環することを許可された車両のタイプ。これらの値の組み合わせです。Enum:'all Vehicle, bicycle, bus, car, companiesTrucks, emergencyVehicle, firefighters, lorry, motorcycle, police, subway, sweepingMachine, trailer, tramway, trucks, van'.  - `alternateName`: このアイテムの別称  - `busImpacted`: 作品の影響を受けるバス路線。0からNまでの発生数の構造化された値で、項目ごとに2つのサブプロパティがある。1つ目のサブプロパティは、「lineId / lineName / lineLocation」のいずれか。2つ目のサブプロパティは、「segmentId / segmentName / segmentLocation」のいずれか。  - `contactPoint`: アイテムの連絡先です。  - `contractingAuthority`: 契約機関の名称  - `countOfBusLineImpacted`: 工事の影響を受けるバス路線数  - `countOfDerogation`: 作品に付与された軽減措置の数 番号  - `countOfEventImpacted`: 作品の影響を受けたイベント数  - `countOfRailwayLineImpacted`: 工事の影響を受ける鉄道路線の数  - `countOfRoadImpacted`: 工事の影響を受ける道路の数  - `countOfSchoolBusLineImpacted`: 工事の影響を受けるスクールバス路線の数  - `countOfSchoolImpacted`: 作品の影響を受ける大学、学校、またはその他の教育資源の名称  - `countOfStationImpacted`: 工事の影響を受ける鉄道駅の数  - `countOfSubwayLineImpacted`: 工事の影響を受ける地下鉄路線の数  - `countOfTramwayLineImpacted`: 工事の影響を受けるトラムウェイ路線の数  - `dataProvider`: 調和されたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateLastReported`: デバイスがデータの報告に成功した最後の時間を示すタイムスタンプ。ISO8601のUTCフォーマットで、この観測の日付と時刻を表します。  - `dateModified`: エンティティが最後に変更された時のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `decrees`: テキストのリストで、各要素はダウンロードするためのURLや法令名の文字列です。  - `derogation`: 曜日や時間に合わせて作業を行うために認められた免除。0からNまでの構造化された値で、各項目は以下のフォーマット `derogationType` : サブプロパティ「startDate, endDate, dayOfWeek, comment」を持つ。  - `description`: このアイテムの説明  - `encroachment`: 作品が公共、私有地に与える影響。これらの値の組み合わせ。Enum:'other, private, public'.  - `endDate`: ISO8601 UTC形式の作品の終了日時が表示されます。この属性は、ハイライトされる時間間隔に対応する場合、`workDate`属性に加えて使用することができます。  - `eventsImpacted`: フリーテキストのリスト、またはエンティティ[Events](https://github.com/smart-data-models/dataModel.TourismDestinations/blob/master/Event/doc/spec.md)が存在する場合はそのリスト。  - `id`: エンティティのユニークな識別子  - `infrastructureFunction`: 作業によって影響を受けるインフラの機能。Enum:'collection, distribution, other, transportation'.  - `isMainRoadImpactedHTR`: 幹線道路に影響があるかどうかを示す値。デフォルトはfalse。https://schema.org/Boolean  - `isMobile`: 作品の移動性に関する特性：固定（デフォルト）の場合はfalse、移動性の場合はtrue  - `mainContractingCompany`: 作品の責任者である主契約会社  - `maxAuthorizedTonnage`: 最大トン数が許可された作業によって影響を受ける道路。1項目につき2つのサブプロパティを持つ、0からNまでの構造化された値。最初のサブプロパティは、「roadId / roadName / roadLocation」のいずれか。2 番目のサブプロパティ、「maxTonnage」。  - `name`: このアイテムの名前です。  - `openingHoursSpecification`: 場所の営業時間や、場所にある特定のサービスに関する情報を提供する構造化された値  - `othersContractingCompany`: 主契約会社の責任下にある契約会社の名前を文字列で表現したリストです。  - `owner`: オーナーのIDを参照するJSONエンコードされた文字列を含むリスト  - `railwayImpacted`: 作業によって影響を受ける鉄道路線。アイテムごとに2つのサブプロパティを持つ、0からNまでの発生数の構造化された値。1つ目のサブプロパティは、「lineId / lineName / lineLocation」のいずれか。2つ目のサブプロパティは、「segmentId / segmentName / segmentLocation」のうちの1つ。  - `roadImpacted`: 作業によって影響を受ける道路と、作業に関係する道路の詳細を示す。0からNまでの構造化された値で、各項目は'roadImpact':[List of Segment Impacted or Free Text or geo-property, separated by a comma]の形式の文字列です。isMainRoadImpactedHTR` = true の場合、最初の項目はこの項目です。  - `roadImpactedMT`: Major Trafficとして定義された、工事によって影響を受ける道路のリスト。値は roadImpacted 属性にも含まれます。  - `roadImpactedSA`: 作業によって影響を受ける、敏感なエリアとして定義された道路のリストです。値は、roadImpacted属性にも含まれます。  - `schoolBusImpacted`: ショールバスのラインが作品に影響を与えている。0からNまでの発生数の構造化された値で、1項目につき2つのサブプロパティを持つ。1つ目のサブプロパティは、「lineId / lineName / lineLocation」のいずれか。2つ目のサブプロパティは、「segmentId / segmentName / segmentLocation」のうちの1つ。  - `schoolImpacted`: フリーテキストのリスト、または[GeoProperty]、または存在する場合はエンティティ[SCHOOL]への参照。  - `seeAlso`: アイテムに関する追加リソースを示すuriのリスト  - `source`: エンティティデータのオリジナルソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `startDate`: ISO8601 UTC形式の作品の開始日時が設定されています。この属性は、ハイライトされる時間間隔に対応する場合、`workDate`属性に加えて使用することができます。  - `stationImpacted`: 駅 作品に影響を受けた。1項目につき2つのサブプロパティを持つ、0からNまでの出現回数の構造化された値。最初のサブプロパティ、「stationType」。2つ目のサブプロパティは、「stationId / stationName / stationLocation」のいずれか。  - `subwayImpacted`: 工事の影響を受ける地下鉄の路線。0からNまでの発生数の構造化された値で、項目ごとに2つのサブプロパティがある。1 つ目のサブプロパティは、「lineId / lineName / lineLocation」のいずれか。2つ目のサブプロパティは、「segmentId / segmentName / segmentLocation」のうちの1つ。  - `territorialArea`: テリトリアル・エリア。属性'areaServed'の上位レベル。フリーテキストのリスト  - `tramwayImpacted`: 路面電車の線路が工事の影響を受けること。0からNまでの発生数の構造化された値で、1項目につき2つのサブプロパティがある。1つ目のサブプロパティは、「lineId / lineName / lineLocation」のうちの1つ。2つ目のサブプロパティは、「segmentId / segmentName / segmentLocation」のうちの1つ。  - `type`: NGSI エンティティタイプ。それはCityWorkでなければならない。  - `typeOfInterventionRequest`: ワークスを行うためのリクエストの初期タイプ。Enum:'authorizationRequest, interventionNotice, other, urgentWorks'.  - `workDate`: 作品の撮影日時（日または期間）。特定の時間の文字列で表現することができます  - `workDisposition`: 作品に対して取られた特定のルール。0からNまでの構造化された値で、各項目は以下のフォーマットを持っています： `Disposition`: サブプロパティ `startDate`, `endDate`, `dayOfWeek`, `comment` を持つ。Enum:'alternatingLights , bicyclePathClosure, bicyclePathDeviation, bicyclePathReduction, circulationManualControl, laneClosure, laneDeviation, laneReduction, noRestriction, parkingForbidden, parkingModification, sidewalkClosure, sidewalkClosureOrReduction, sidewalkReduction, speedReduction'.  - `workLastDateUpdate`: 作品の契約上の要素を更新するための最終期限  - `workLevel`: 地面を基準にした作品の位置決め。これらの要素を組み合わせたもの。Enum:'aerial, ground, mixed, other, roofing, surface, underground, wall'.  - `workNature`: 作品の性質。これらの値の組み合わせ。イナム。'additionalInvestigations, brushCutting, cleaning, collection, connection, consolidation, construction, control, counting, craneLifting, creation, demolition, drivingSwitch, experimentation, extension, filmShooting, Installation-OR-layout, investigation, landFill, maintenance, manholeOpening, ManholeOpeningToRestoreService, miscellaneousInstallation, miscellaneousWorks, mowingDeburring,other, overheadLinesWorksIntervention, pruning, pulling, refurbishment, rehabilitation, reinforcement, renewal, renovation, repair, replacement, riprap, roadSign, safetyAndComplianceWork, safetyRailsInstallation, securingPerimeter, siteInstallation, staking, supportImplantation, surfaceOccupationAuthorization, survey, tarring, tonnageExemption, treeCutting, trenchOpening, upgrading'.  - `workNumber`: 作品に割り当てられた番号  - `workOtherImpact`: その他の影響｜大手電子書籍ストアお得なストアBookLive!自由な価値観のリスト  - `workReason`: 緊急に介入する場合の作品の理由。これらの値の組み合わせ。Enum:'collapse, derailment, fire, flood, gasLeak, landslide, other, powerCut, rockfall, sagging, waterLeak'  - `workState`: 作品に割り当てられた番号。Enum:'all, approved, authorized, canceled, completed, decreeToBeSigned, draft, editedDecrees, instructionInProgress, investigated, nonCompliantOccupation, open, pendingAuthorization, pendingCancellation, planningCompleted, pendingDocument, pendingExtension, pendingPlanning, planned, received, reject, supported, validatedInPlanning'.  - `workTarget`: 異なる職業に関する作品のカテゴリー。これらの要素を組み合わせたもの。イナム。'bicyclePath, busCorridor, catainers, cityMotorBike, cityBike, cityCar, cityScooter, coldAndAirCon, coldGroup, copperCable, CoringPenetrometry, drinkingWater, electricityNetworks, ExploratoryWork,消火栓、フレームルーフ、ガスネットワーク、発電機、歴史的建造物、インフラストラクチャー、ランドスケープエリア、ムービングホイストナセルトラック、ネットワーク、オフストリートパーキング、光ファイバー、その他、オーバーヘッドライン、ペーパーコレクション。舗装、公共装飾照明、公共領域、公共交通、鉄道、雨水、リップラップ、rMTネットワーク、道路、道路と公共領域、衛生、足場、歩道、減速装置、路上駐車。surfaceOccupation, supportStructures, tags andPosters, telecomNetworks, telecom-RMT-VideoNetworks, trafficSignalingRegulation, tramway, urbanFurniture, urbanHeating, variousWorks, videoNetworks, vrd'.  - `workZone`: 作品のゾーン。これらの値の組み合わせです。Enum:' 空港、海岸、自転車道、橋、バス通路、ドック、洪水地域、港、ヘリポート、山岳地域、オフロード、その他、駐車場、公園庭園、道、保護地域、鉄道線、危険地域、川、道路、岩場、セベソ地域、サイドウォーク、地下鉄線、路面電車線、トンネル'    
必須項目  
- `id`  - `location`  - `type`  ## データモデルによるプロパティの記述  
アルファベット順（クリックすると詳細が表示されます）  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
CityWork:    
  description: 'The Data Model is a contextual description of urban works carried out on a road axis and which can impact individual (Cars, motorcycle, bicycles, .…) or common transport (Tram, Bus, subway). It contains a geographic representation making it possible to locate its work from a specific JSON Object and at a more global level (Road segment, Road, District, ...) in order to assess the potential impacts on the circulation. A GeoJSON object may represent a region of space (a Geometry), a spatially-bounded entity (a Feature), or a list of features (a Feature Collection). refer to the document [geojson](https://tools.ietf.org/pdf/draft-ietf-geojson-03.pdf) for more information about the modeling and the possible value.'    
  properties:    
    allowedVehicle:    
      description: 'Type of vehicle authorized to circulate. A combination of these values. Enum:''all Vehicle, bicycle, bus, car, companiesTrucks,  emergencyVehicle, firefighters, lorry, motorcycle, police, subway, sweepingMachine, trailer, tramway, trucks, van'''    
      items:    
        enum:    
          - allVehicle    
          - bicycle    
          - bus    
          - car    
          - companiesTrucks    
          - emergencyVehicle    
          - firefighters    
          - lorry    
          - motorcycle    
          - police    
          - subway    
          - sweepingMachine    
          - trailer    
          - tramway    
          - trucks    
          - van    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    busImpacted:    
      description: 'Bus lines impacted by the works. A structured value from 0 to N occurrences with 2 subproperties per item. First subproperties, one of ''lineId / lineName / lineLocation''. Second subproperties, one of ''segmentId / segmentName / segmentLocation'''    
      items:    
        properties:    
          lineId:    
            anyOf: &citywork_-_properties_-_id_-_anyof    
              - description: 'Property. Identifier format of any NGSI entity'    
                maxLength: 256    
                minLength: 1    
                pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
                type: string    
              - description: 'Property. Identifier format of any NGSI entity'    
                format: uri    
                type: string    
            description: 'Property. Unique identifier of the entity'    
          lineLocation:    
            description: 'Geoproperty. Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
            oneOf: &citywork_-_properties_-_busimpacted_-_items_-_properties_-_segmentid_-_items_-_oneof    
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
          lineName:    
            type: string    
          segmentId:    
            items:    
              description: 'Geoproperty. Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
              oneOf: *citywork_-_properties_-_busimpacted_-_items_-_properties_-_segmentid_-_items_-_oneof    
            type: array    
          segmentLocation:    
            description: 'Property. Segment Location. A GeoProperty.'    
            items:    
              description: 'Geoproperty. Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
              oneOf: *citywork_-_properties_-_busimpacted_-_items_-_properties_-_segmentid_-_items_-_oneof    
            type: array    
          segmentName:    
            description: 'Property. Segment Name.'    
            items:    
              type: string    
            type: array    
        type: object    
      type: array    
      x-ngsi:    
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
      description: 'Name of the contracting authority'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    countOfBusLineImpacted:    
      description: 'Count of Bus Lines impacted by the works'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    countOfDerogation:    
      description: 'Count of derogations granted to the work Number'    
      type: number    
      x-ngsi:    
        model: https://schema.org/number    
        type: Property    
    countOfEventImpacted:    
      description: 'Count of Events impacted by the works'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    countOfRailwayLineImpacted:    
      description: 'Count of Railway Lines impacted by the works'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    countOfRoadImpacted:    
      description: 'Count of roads impacted by the works'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    countOfSchoolBusLineImpacted:    
      description: 'Count of School Bus Lines impacted by the works'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    countOfSchoolImpacted:    
      description: 'Count of University, School, or other educational resource impacted by the works'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    countOfStationImpacted:    
      description: 'Count of Railway stations impacted by the works'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    countOfSubwayLineImpacted:    
      description: 'Count of Subway Lines impacted by the works'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    countOfTramwayLineImpacted:    
      description: 'Count of tramway lines impacted by the works'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
      description: 'A timestamp which denotes the last time when the device successfully reported data. The date and time of this observation in ISO8601 UTCformat'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    decrees:    
      description: 'A List of text where each element is a string with the URL to download or the name of the decree.'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    derogation:    
      description: 'Derogation granted for carrying out work on days and times. A structured value from 0 to N occurrences where each items has the following format `derogationType` :  with sub properties ''startDate, endDate, dayOfWeek, comment'''    
      items:    
        properties:    
          comment:    
            type: string    
          dayOfWeek:    
            items:    
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
            type: array    
          derogationType:    
            type: string    
          endDate:    
            format: date-time    
            type: string    
          startDate:    
            format: date-time    
            type: string    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    encroachment:    
      description: 'Impact of the works on public, private area. A combination of these values. Enum:''other, private, public'''    
      items:    
        enum:    
          - other    
          - private    
          - public    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    endDate:    
      description: 'End date and time of the works in an ISO8601 UTC format. The attribute can be used in addition to the `workDate` attribute when it corresponds to a time interval to be highlighted'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    eventsImpacted:    
      description: 'List of free text or to the entity [Events](https://github.com/smart-data-models/dataModel.TourismDestinations/blob/master/Event/doc/spec.md) if exist.'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: *citywork_-_properties_-_id_-_anyof    
      description: 'Unique identifier of the entity'    
      x-ngsi:    
        type: Property    
    infrastructureFunction:    
      description: ' Function of the infrastructure impacted by the works. Enum:''collection, distribution, other, transportation'''    
      items:    
        enum:    
          - collection    
          - distribution    
          - other    
          - transportation    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    isMainRoadImpactedHTR:    
      description: 'Value to indicate whether the main traffic road is impacted. Default false. https://schema.org/Boolean'    
      type: boolean    
      x-ngsi:    
        type: Property    
    isMobile:    
      description: 'Characteristic on the mobility of the works : false for Fixed (default) and true for Mobile'    
      type: boolean    
      x-ngsi:    
        model: https://schema.org/Boolean    
        type: Property    
    mainContractingCompany:    
      description: 'The Main Contracting Company responsible of the works'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    maxAuthorizedTonnage:    
      description: 'Roads impacted by the works with Maximum tonnage authorized. A structured value from 0 to N occurrences with 2 subproperties per item. First subproperties, one of ''roadId / roadName / roadLocation''. Second subproperties, ''maxTonnage'''    
      items:    
        properties:    
          maxTonnage:    
            description: 'Property. Maximum tonnage authorized for the road. The unit code (text) **TNE** which represents Tonne Metric.'    
            type: number    
          roadId:    
            anyOf: *citywork_-_properties_-_id_-_anyof    
            description: 'Property. Unique identifier of the entity'    
          roadImpacted:    
            type: string    
          roadLocation:    
            description: 'Geoproperty. Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
            oneOf: *citywork_-_properties_-_busimpacted_-_items_-_properties_-_segmentid_-_items_-_oneof    
          roadName:    
            description: 'Property. Road Name'    
            type: string    
        type: object    
      type: array    
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
    othersContractingCompany:    
      description: 'A List of Text where each element is a string with the name of the contracting Companies under the responsibility of the main Contracting Company.'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *citywork_-_properties_-_id_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    railwayImpacted:    
      description: 'Rail lines impacted by the works. A structured value from 0 to N occurrences with 2 subproperties per item. First subproperties, one of ''lineId / lineName / lineLocation''. Second subproperties, one of ''segmentId / segmentName / segmentLocation'''    
      items:    
        properties:    
          lineId:    
            anyOf: *citywork_-_properties_-_id_-_anyof    
            description: 'Property. Unique identifier of the entity'    
          lineLocation:    
            description: 'Geoproperty. Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
            oneOf: *citywork_-_properties_-_busimpacted_-_items_-_properties_-_segmentid_-_items_-_oneof    
          lineName:    
            type: string    
          segmentId:    
            items:    
              description: 'Geoproperty. Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
              oneOf: *citywork_-_properties_-_busimpacted_-_items_-_properties_-_segmentid_-_items_-_oneof    
            type: array    
          segmentLocation:    
            description: 'Property. Segment Location. A GeoProperty.'    
            items:    
              description: 'Geoproperty. Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
              oneOf: *citywork_-_properties_-_busimpacted_-_items_-_properties_-_segmentid_-_items_-_oneof    
            type: array    
          segmentName:    
            description: 'Property. Segment Name.'    
            items:    
              type: string    
            type: array    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    roadImpacted:    
      description: 'Roads impacted by the works and the details of the roads concerned by the work. A structured value from 0 to N occurrences where each items is a string in the format : ''roadImpact'':[List of Segment Impacted or Free Text or geo-property, separated by a comma]. If `isMainRoadImpactedHTR` = true, The first item is this one.'    
      items:    
        properties:    
          roadId:    
            anyOf: *citywork_-_properties_-_id_-_anyof    
            description: 'Property. Unique identifier of the entity'    
          roadLocation:    
            description: 'Geoproperty. Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
            oneOf: *citywork_-_properties_-_busimpacted_-_items_-_properties_-_segmentid_-_items_-_oneof    
          roadName:    
            description: 'Property. Road Name'    
            type: string    
          segmentId:    
            items:    
              description: 'Geoproperty. Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
              oneOf: *citywork_-_properties_-_busimpacted_-_items_-_properties_-_segmentid_-_items_-_oneof    
            type: array    
          segmentLocation:    
            description: 'Property. Segment Location. A GeoProperty.'    
            items:    
              description: 'Geoproperty. Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
              oneOf: *citywork_-_properties_-_busimpacted_-_items_-_properties_-_segmentid_-_items_-_oneof    
            type: array    
          segmentName:    
            description: 'Property. Segment Name.'    
            items:    
              type: string    
            type: array    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    roadImpactedMT:    
      description: 'A list of roads defined as Major Traffic, impacted by the works. Values are also included in the roadImpacted attribute.'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    roadImpactedSA:    
      description: 'A list of roads defined as sensitive areas, impacted by the works. Values are also included in the roadImpacted attribute.'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    schoolBusImpacted:    
      description: 'Scholl Bus lines impacted by the works. A structured value from 0 to N occurrences with 2 subproperties per item. First subproperties, one of ''lineId / lineName / lineLocation''. Second subproperties, one of ''segmentId / segmentName / segmentLocation'''    
      items:    
        properties:    
          lineId:    
            anyOf: *citywork_-_properties_-_id_-_anyof    
            description: 'Property. Unique identifier of the entity'    
          lineLocation:    
            description: 'Geoproperty. Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
            oneOf: *citywork_-_properties_-_busimpacted_-_items_-_properties_-_segmentid_-_items_-_oneof    
          lineName:    
            type: string    
          segmentId:    
            items:    
              description: 'Geoproperty. Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
              oneOf: *citywork_-_properties_-_busimpacted_-_items_-_properties_-_segmentid_-_items_-_oneof    
            type: array    
          segmentLocation:    
            description: 'Property. Segment Location. A GeoProperty.'    
            items:    
              description: 'Geoproperty. Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
              oneOf: *citywork_-_properties_-_busimpacted_-_items_-_properties_-_segmentid_-_items_-_oneof    
            type: array    
          segmentName:    
            description: 'Property. Segment Name.'    
            items:    
              type: string    
            type: array    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    schoolImpacted:    
      description: 'List of free text or [GeoProperty] or a Reference to an entity [SCHOOL] if exist. '    
      items:    
        type: string    
      type: array    
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
    startDate:    
      description: 'Start date and time of the works in an ISO8601 UTC format. The attribute can be used in addition to the `workDate` attribute when it corresponds to a time interval to be highlighted'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    stationImpacted:    
      description: 'Station Impacted by the works. A structured value from 0 to N occurrences with 2 subproperties per item. First subproperties, ''stationType''. Second subproperties, one of ''stationId / stationName / stationLocation'''    
      items:    
        properties:    
          stationId:    
            description: 'Property. List of free text or reference to the entity [TransportStation](https://github.com/smart-data-models/dataModel.Transportation/blob/master/TransportStation/doc/spec.md) if used.'    
            items:    
              anyOf: *citywork_-_properties_-_id_-_anyof    
              description: 'Property. Unique identifier of the entity'    
            type: array    
          stationLocation:    
            description: 'Property. Station Location. A GeoProperty.'    
            items:    
              description: 'Geoproperty. Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
              oneOf: *citywork_-_properties_-_busimpacted_-_items_-_properties_-_segmentid_-_items_-_oneof    
            type: array    
          stationName:    
            description: 'Property. Station Name.'    
            items:    
              type: string    
            type: array    
          stationType:    
            description: "Property. A unique value of free text or from the urban transport Mode GFTS standard [STOP](https://developers.google.com/transit/gtfs/reference/#stopstxt). Enum:'aerialLift, bus, cableTram, ferry, funicular, monorail, rail, subway, tram, trolleybus'"    
            enum:    
              - aerialLift    
              - bus    
              - cableTram    
              - ferry    
              - funicular    
              - monorail    
              - rail    
              - subway    
              - tram    
              - trolleybus    
            type: string    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    subwayImpacted:    
      description: 'Subway lines impacted by the works. A structured value from 0 to N occurrences with 2 subproperties per item. First subproperties, one of ''lineId / lineName / lineLocation''. Second subproperties, one of ''segmentId / segmentName / segmentLocation'''    
      items:    
        properties:    
          lineId:    
            anyOf: *citywork_-_properties_-_id_-_anyof    
            description: 'Property. Unique identifier of the entity'    
          lineLocation:    
            description: 'Geoproperty. Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
            oneOf: *citywork_-_properties_-_busimpacted_-_items_-_properties_-_segmentid_-_items_-_oneof    
          lineName:    
            type: string    
          segmentId:    
            items:    
              description: 'Geoproperty. Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
              oneOf: *citywork_-_properties_-_busimpacted_-_items_-_properties_-_segmentid_-_items_-_oneof    
            type: array    
          segmentLocation:    
            description: 'Property. Segment Location. A GeoProperty.'    
            items:    
              description: 'Geoproperty. Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
              oneOf: *citywork_-_properties_-_busimpacted_-_items_-_properties_-_segmentid_-_items_-_oneof    
            type: array    
          segmentName:    
            items:    
              type: string    
            type: array    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    territorialArea:    
      description: 'Territorial area. Level higher to the attribute ''areaServed''. A list of Free Text'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    tramwayImpacted:    
      description: 'Tramway Line impacted by the works. A structured value from 0 to N occurrences with 2 subproperties per item. First subproperties, one of ''lineId / lineName / lineLocation''. Second subproperties, one of ''segmentId / segmentName / segmentLocation'''    
      items:    
        properties:    
          lineId:    
            anyOf: *citywork_-_properties_-_id_-_anyof    
            description: 'Property. Unique identifier of the entity'    
          lineLocation:    
            description: 'Geoproperty. Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
            oneOf: *citywork_-_properties_-_busimpacted_-_items_-_properties_-_segmentid_-_items_-_oneof    
          lineName:    
            description: 'Property. Line Name.'    
            type: string    
          segmentId:    
            items:    
              description: 'Geoproperty. Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
              oneOf: *citywork_-_properties_-_busimpacted_-_items_-_properties_-_segmentid_-_items_-_oneof    
            type: array    
          segmentLocation:    
            description: 'Property. Segment Location. A GeoProperty.'    
            items:    
              description: 'Geoproperty. Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
              oneOf: *citywork_-_properties_-_busimpacted_-_items_-_properties_-_segmentid_-_items_-_oneof    
            type: array    
          segmentName:    
            items:    
              type: string    
            type: array    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI Entity type. It has to be CityWork'    
      enum:    
        - CityWork    
      type: string    
      x-ngsi:    
        type: Property    
    typeOfInterventionRequest:    
      description: 'Initial type of request to do the works. Enum:''authorizationRequest,  interventionNotice,  other,  urgentWorks'''    
      enum:    
        - authorizationRequest    
        - interventionNotice    
        - other    
        - urgentWorks    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    workDate:    
      description: 'Date and time (Day or period) of the works. It can be represented by an specific time string'    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    workDisposition:    
      description: 'Specific rules taken for the works. A structured value from 0 to N occurrences where each items has the following format : `Disposition`: with sub properties  `startDate`, `endDate`,  `dayOfWeek`, `comment`. Enum:''alternatingLights , bicyclePathClosure, bicyclePathDeviation, bicyclePathReduction, circulationManualControl, laneClosure, laneDeviation, laneReduction, noRestriction, parkingForbidden, parkingModification, sidewalkClosure, sidewalkClosureOrReduction, sidewalkReduction, speedReduction'''    
      items:    
        properties:    
          comment:    
            type: string    
          dayOfWeek:    
            items:    
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
            type: array    
          disposition:    
            enum:    
              - alternatingLights    
              - bicyclePathClosure    
              - bicyclePathDeviation    
              - bicyclePathReduction    
              - circulationManualControl    
              - laneClosure    
              - laneDeviation    
              - laneReduction    
              - noRestriction    
              - parkingForbidden    
              - parkingModification    
              - sidewalkClosure    
              - sidewalkClosureOrReduction    
              - sidewalkReduction    
              - speedReduction    
              - workOtherImpact    
            type: string    
          endDate:    
            format: date-time    
            type: string    
          startDate:    
            format: date-time    
            type: string    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    workLastDateUpdate:    
      description: 'Last date for updating a contractual element of the work'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    workLevel:    
      description: 'Positioning of the works in relation to a ground reference system. A combination of these elements. Enum:''aerial, ground, mixed, other, roofing, surface, underground, wall'''    
      items:    
        enum:    
          - aerial    
          - ground    
          - mixed    
          - other    
          - roofing    
          - surface    
          - underground    
          - wall    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    workNature:    
      description: 'Nature of the works. A combination of these values.Enum:''additionalInvestigations, brushCutting, cleaning, collection, connection, consolidation, construction, control, counting, craneLifting, creation, demolition, drivingSwitch, experimentation, extension, filmShooting, Installation-OR-layout, investigation, landFill, maintenance, manholeOpening, ManholeOpeningToRestoreService, miscellaneousInstallation, miscellaneousWorks, mowingDeburring, other, overheadLinesWorksIntervention, pruning, pulling, refurbishment, rehabilitation, reinforcement, renewal, renovation, repair, replacement, riprap, roadSign, safetyAndComplianceWork, safetyRailsInstallation, securingPerimeter, siteInstallation, staking, supportImplantation, surfaceOccupationAuthorization, survey, tarring, tonnageExemption, treeCutting, trenchOpening, upgrading'''    
      items:    
        enum:    
          - additionalInvestigations    
          - brushCutting    
          - cleaning    
          - collection    
          - connection    
          - consolidation    
          - construction    
          - control    
          - counting    
          - craneLifting    
          - creation    
          - demolition    
          - drivingSwitch    
          - experimentation    
          - extension    
          - filmShooting    
          - Installation-OR-layout    
          - investigation    
          - landFill    
          - maintenance    
          - manholeOpening    
          - ManholeOpeningToRestoreService    
          - miscellaneousInstallation    
          - miscellaneousWorks    
          - mowingDeburring    
          - other    
          - overheadLinesWorksIntervention    
          - pruning    
          - pulling    
          - refurbishment    
          - rehabilitation    
          - reinforcement    
          - renewal    
          - renovation    
          - repair    
          - replacement    
          - riprap    
          - roadSign    
          - safetyAndComplianceWork    
          - safetyRailsInstallation    
          - securingPerimeter    
          - siteInstallation    
          - staking    
          - supportImplantation    
          - surfaceOccupationAuthorization    
          - survey    
          - tarring    
          - tonnageExemption    
          - treeCutting    
          - trenchOpening    
          - upgrading    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    workNumber:    
      description: 'Number assigned to the work'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    workOtherImpact:    
      description: 'Other impact. A list of free values'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    workReason:    
      description: 'Reasons of the works in case of urgent intervention. A combination of these values. Enum:''collapse, derailment, fire, flood, gasLeak, landslide, other, powerCut, rockfall, sagging, waterLeak'''    
      items:    
        enum:    
          - collapse    
          - derailment    
          - fire    
          - flood    
          - gasLeak    
          - landslide    
          - other    
          - powerCut    
          - rockfall    
          - sagging    
          - waterLeak    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    workState:    
      description: 'Number assigned to the work. Enum:''all, approved, authorized, canceled, completed, decreeToBeSigned, draft, editedDecrees, instructionInProgress, investigated, nonCompliantOccupation, open, pendingAuthorization, pendingCancellation, planningCompleted, pendingDocument, pendingExtension, pendingPlanning, planned, received, reject, supported, validatedInPlanning'''    
      enum:    
        - all    
        - approved    
        - authorized    
        - canceled    
        - completed    
        - decreeToBeSigned    
        - draft    
        - editedDecrees    
        - instructionInProgress    
        - investigated    
        - nonCompliantOccupation    
        - open    
        - other    
        - pendingAuthorization    
        - pendingCancellation    
        - planningCompleted    
        - pendingDocument    
        - pendingExtension    
        - pendingPlanning    
        - planned    
        - received    
        - reject    
        - supported    
        - validatedInPlanning    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    workTarget:    
      description: 'Categories of works regarding the different profession. A combination of these elements. Enum:''bicyclePath, busCorridor, catainers, cityMotorBike, cityBike, cityCar, cityScooter, coldAndAirCon, coldGroup, copperCable, CoringPenetrometry, drinkingWater, electricityNetworks, exploratoryWork, fireHydrants, frameRoof, gasNetworks, generator, historicalMonuments, infrastructure, landscapedArea, movingHoistNacelleTruck, networks, offStreetParking, opticalFibers, other, overheadLine, papersCollection, pavement, publicDecorativeLighting, publicDomain, publicTransport, railway, rainyWaters, riprap, rMTNetworks, roads, roadsAndPublicDomain, sanitation, scaffolding, sideWalk, speedReductionDevices, streetParking, surfaceOccupation, supportStructures, tagsAndPosters, telecomNetworks, telecom-RMT-VideoNetworks, trafficSignalingRegulation, tramway, urbanFurniture, urbanHeating, variousWorks, videoNetworks, vrd'''    
      items:    
        enum:    
          - bicyclePath    
          - busCorridor    
          - catainers    
          - cityMotorBike    
          - cityBike    
          - cityCar    
          - cityScooter    
          - coldAndAirCon    
          - coldGroup    
          - copperCable    
          - CoringPenetrometry    
          - drinkingWater    
          - electricityNetworks    
          - exploratoryWork    
          - fireHydrants    
          - frameRoof    
          - gasNetworks    
          - generator    
          - historicalMonuments    
          - infrastructure    
          - landscapedArea    
          - movingHoistNacelleTruck    
          - networks    
          - offStreetParking    
          - opticalFibers    
          - other    
          - overheadLine    
          - papersCollection    
          - pavement    
          - publicDecorativeLighting    
          - publicDomain    
          - publicTransport    
          - railway    
          - rainyWaters    
          - riprap    
          - rMTNetworks    
          - roads    
          - roadsAndPublicDomain    
          - sanitation    
          - scaffolding    
          - sideWalk    
          - speedReductionDevices    
          - streetParking    
          - surfaceOccupation    
          - supportStructures    
          - tagsAndPosters    
          - telecomNetworks    
          - telecom-RMT-VideoNetworks    
          - trafficSignalingRegulation    
          - tramway    
          - urbanFurniture    
          - urbanHeating    
          - variousWorks    
          - videoNetworks    
          - vrd    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    workZone:    
      description: 'Zone of Works. A combination of these values. Enum:'' airport, beach, bicyclePath, bridge, busCorridor, dock, floodArea, harbor, heliport, mountainousArea, offRoad, other, parking, parksGardens, path, protectArea, railwayLine, riskArea, river, road, rockyArea, sevesoArea, sideWalk, subwayLine, tramwayLine, tunnel'''    
      items:    
        enum:    
          - airport    
          - beach    
          - bicyclePath    
          - bridge    
          - busCorridor    
          - dock    
          - floodArea    
          - harbor    
          - heliport    
          - mountainousArea    
          - offRoad    
          - other    
          - parking    
          - parksGardens    
          - path    
          - protectArea    
          - railwayLine    
          - riskArea    
          - river    
          - road    
          - rockyArea    
          - sevesoArea    
          - sideWalk    
          - subwayLine    
          - tramwayLine    
          - tunnel    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - location    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Transportation/blob/master/CityWork/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Transportation/CityWork/schema.json    
  x-model-tags: ""    
  x-version: 0.3.0    
```  
</details>    
## ペイロードの例  
#### CityWork NGSI-v2 キー・バリューの例  
JSON-LD形式でCityWorkをkey-valuesとして表現した例です。これは`options=keyValues`を使うとNGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返すことができます。  
```json  
{  
  "id": "urn:ngsi-ld:CityWork:CityWork:MNCA-CW-2020Q2-006",  
  "type": "CityWork",  
  "name": "Nce-Airport-CW2020Q2-006",  
  "alternateName": "AirPort global Observation",  
  "description": "Widening work on access roads and installation of a new electrical and digital network for the connection of T1 & T2 terminals",  
  "location": {  
    "type": "Polygon",  
    "coordinates": [  
      [  
        43.20315,  
        7.20186  
      ],  
      [  
        43.20384,  
        7.20372  
      ],  
      [  
        43.20388,  
        7.20493  
      ],  
      [  
        43.19938,  
        7.20312  
      ],  
      [  
        43.20045,  
        7.20152  
      ],  
      [  
        43.20315,  
        7.20186  
      ]  
    ]  
  },  
  "areaServed": "Nice Aeroport",  
  "territorialArea": "subwaypole Nice",  
  "dateLastReported": "2020-04-02T10:30:00Z",  
  "workNumber": "CW2020Q2-006",  
  "workState": "open",  
  "workDate": "2020-03-17T08:45:00Z/2020-04-22T18:45:00Z",  
  "startDate": "2020-03-17T08:45:00Z",  
  "endDate": "2020-04-22T18:45:00Z",  
  "openingHoursSpecification": [  
    {  
      "dayOfWeek": "Monday",  
      "opens": "07:00:00",  
      "closes": "20:00:00"  
    },  
    {  
      "dayOfWeek": "Tuesday",  
      "opens": "07:00:00",  
      "closes": "20:00:00"  
    },  
    {  
      "dayOfWeek": "Wednesday",  
      "opens": "07:00:00",  
      "closes": "20:00:00"  
    },  
    {  
      "dayOfWeek": "Thursday",  
      "opens": "07:00:00",  
      "closes": "20:00:00"  
    },  
    {  
      "dayOfWeek": "Friday",  
      "opens": "07:00:00",  
      "closes": "20:00:00"  
    },  
    {  
      "dayOfWeek": "Saturday",  
      "opens": "08:30:00",  
      "closes": "17:00:00"  
    }  
  ],  
  "contractingAuthority": "MNCA - subwaypole Nice Cote d'Azur",  
  "contactPoint": {  
    "name": "Service des AO"  
  },  
  "decrees": [  
    "https://MNCA/CityWork/Decree/CW-2020Q2-006",  
    "CW-2020Q2-006",  
    "CW-2020Q2-006-Av-001",  
    "CW-2020Q2-006-Av-002"  
  ],  
  "workLastDateUpdate": "2020-03-17T08:45:00Z",  
  "mainContractingCompagny": "XRP - NICOLSPA",  
  "othersContractingCompagny": [  
    "VRD - Terrassement Nicois",  
    "ELEC - Electricite de Nice",  
    "NUM - Consortium operateur"  
  ],  
  "workLevel": [  
    "ground",  
    "underground"  
  ],  
  "workTarget": [  
    "roads",  
    "pavement",  
    "electricityNetworks",  
    "opticalFibers",  
    "videoNetworks",  
    "vrd"  
  ],  
  "workNature": [  
    "landFill",  
    "repair",  
    "tonnageExemption",  
    "securingPerimeter",  
    "trenchOpening",  
    "tarring"  
  ],  
  "infrastructureFunction": [  
    "distribution",  
    "collection"  
  ],  
  "encroachment": [  
    "public",  
    "private"  
  ],  
  "typeOfInteventionRequest": "authorizationRequest",  
  "workReason": [  
    "sagging",  
    "powerCut"  
  ],  
  "workZone": [  
    "road",  
    "sideWalk",  
    "busCorridor",  
    "tramwayLine"  
  ],  
  "workDisposition": [  
    {  
      "disposition": "laneReduction",  
      "startDate": "2020-05-11T08:00:00Z",  
      "endDate": "2020-05-15T18:30:00Z",  
      "dayOfWeek": [  
        "Monday",  
        "Tuesday",  
        "Wednesday",  
        "Thursday",  
        "Friday"  
      ],  
      "comment": "Switching from 2 lanes to 1 lane - BusCorridor not available"  
    },  
    {  
      "disposition": "sidewalkReduction",  
      "startDate": "2020-05-12T00:00:00Z",  
      "endDate": "2020-05-14T24:00:00Z",  
      "dayOfWeek": [  
        "Monday",  
        "Tuesday",  
        "Wednesday",  
        "Thursday",  
        "Friday"  
      ]  
    },  
    {  
      "disposition": "alternatingLights",  
      "startDate": "2020-05-11T08:00:00Z",  
      "endDate": "2020-05-15T18:30:00Z",  
      "dayOfWeek": [  
        "Monday",  
        "Tuesday",  
        "Wednesday",  
        "Thursday",  
        "Friday"  
      ]  
    },  
    {  
      "disposition": "speedReduction",  
      "startDate": "2020-05-12T00:00:00Z",  
      "dayOfWeek": [  
        "Monday",  
        "Tuesday",  
        "Wednesday",  
        "Thursday",  
        "Friday",  
        "Saturday",  
        "Sunday"  
      ],  
      "comment": "Speed Switching from 2 lanes to 1 lane"  
    }  
  ],  
  "workOtherImpact": [  
    "layingCablesOnGround",  
    "shopsTerrace"  
  ],  
  "isMobile": false,  
  "countOfDerogation": 2,  
  "derogation": [  
    {  
      "derogationType": "Work Nigth during Workday",  
      "startDate": "2020-05-11T20:30:00Z",  
      "endDate": "2020-05-15T23:30:00",  
      "dayOfWeek": [  
        "Monday",  
        "Tuesday",  
        "Wednesday",  
        "Thursday",  
        "Friday"  
      ]  
    },  
    {  
      "derogationType": "BRH",  
      "startDate": "2020-05-13T20:30:00Z",  
      "endDate": "2020-05-13T23:30:00Z",  
      "dayOfWeek": [  
        "Wednesday"  
      ]  
    }  
  ],  
  "isMainRoadImpactedHTR": true,  
  "countOfRoadImpacted": 3,  
  "roadImpacted": [  
    {  
      "roadId": "urn:ngsi-ld:Road:N202",  
      "segmentImpacted": [  
        "urn:ngsi-ld:RoadSegment:N202-12",  
        "urn:ngsi-ld:RoadSegment:N202-13"  
      ]  
    },  
    {  
      "roadId": "Road:D021",  
      "segmentImpacted": [  
        "12",  
        "13",  
        "14",  
        "15"  
      ]  
    },  
    {  
      "roadId": "urn:ngsi-ld:Road:D032",  
      "segmentArea": {  
        "type": "LineString",  
        "coordinates": [  
          [  
            102.0,  
            0.0  
          ],  
          [  
            103.0,  
            1.0  
          ],  
          [  
            104.0,  
            0.0  
          ],  
          [  
            105.0,  
            1.0  
          ]  
        ]  
      }  
    }  
  ],  
  "allowedVehicle": [  
    "firefighters",  
    "police",  
    "emergencyVehicle",  
    "companiesTrucks"  
  ],  
  "maxAuthorizedTonnage": [  
    {  
      "roadImpacted": "urn:ngsi-ld:Road:N202",  
      "maxTonnage": 30  
    },  
    {  
      "roadImpacted": "Road:D021",  
      "maxTonnage": 20  
    },  
    {  
      "roadImpacted": "urn:ngsi-ld:Road:D032",  
      "maxTonnage": 15.2  
    }  
  ],  
  "countOfBusLineImpacted": 1,  
  "busImpacted": [  
    {  
      "lineImpacted": "urn:ngsi-ld:BusLine:L205"  
    }  
  ],  
  "countOfTramwayLineImpacted": 2,  
  "tramwayImpacted": [  
    {  
      "lineImpacted": "TramWayLine:L01",  
      "segmentImpacted": [  
        "urn:ngsi-ld:TramWaySegment:L01-12",  
        "urn:ngsi-ld:TramWaySegment:L01-19"  
      ]  
    },  
    {  
      "lineImpacted": "TramWayLine:L03",  
      "segmentImpacted": [  
        "urn:ngsi-ld:TramWaySegment:L03-19"  
      ]  
    }  
  ],  
  "countOfRailwayLineImpacted": 1,  
  "railwayImpacted": [  
    {  
      "lineImpacted": "Nice-Grasse",  
      "segmentImpact": [  
        "Nice Saint Augustin section"  
      ]  
    }  
  ],  
  "countOfSchoolImpacted": 2,  
  "schoolImpacted": [  
    "Lycée Massena",  
    "Université Campus Saint Jean"  
  ],  
  "countOfStationImpacted": 4,  
  "stationImpacted": [  
    {  
      "stationId": [  
        "urn:ngsi-ld:station:L205-S13",  
        "urn:ngsi-ld:station:L205-S14"  
      ]  
    },  
    {  
      "stationType": "tram",  
      "stationId": [  
        "L01-S12",  
        "L01-S19"  
      ]  
    }  
  ],  
  "countOfEventImpacted": 2,  
  "eventsImpact": [  
    "urn:ngsi-ld:events:MNCA-EV-JazzCimiez",  
    "NiceMarathon"  
  ]  
}  
```  
#### CityWork NGSI-v2の正規化例  
ここでは、正規化されたJSON-LD形式のCityWorkの例を示します。これは、オプションを使用しない場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "id": "urn:ngsi-ld:CityWork:CityWork:MNCA-CW-2020Q2-006",  
  "type": "CityWork",  
  "name": {  
    "type": "string",  
    "value": "Nice-Airport-CW2020Q2-006"  
  },  
  "alternateName": {  
    "type": "string",  
    "value": "AirPort global Observation"  
  },  
  "description": {  
    "type": "string",  
    "value": "Widening work on access roads and installation of a new electrical and digital network for the connection of T1 & T2 terminals"  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Polygon",  
      "coordinates": [  
        [  
          43.20315,  
          7.20186  
        ],  
        [  
          43.20384,  
          7.20372  
        ],  
        [  
          43.20388,  
          7.20493  
        ],  
        [  
          43.19938,  
          7.20312  
        ],  
        [  
          43.20045,  
          7.20152  
        ],  
        [  
          43.20315,  
          7.20186  
        ]  
      ]  
    }  
  },  
  "areaServed": {  
    "type": "string",  
    "value": "Nice Aeroport"  
  },  
  "territorialArea": {  
    "type": "string",  
    "value": "subwaypole Nice"  
  },  
  "dateLastReported": {  
    "type": "DateTime",  
    "value": "2020-04-02T10:30:00Z"  
  },  
  "workNumber": {  
    "type": "string",  
    "value": "CW2020Q2-006"  
  },  
  "workState": {  
    "type": "string",  
    "value": "open"  
  },  
  "workDate": {  
    "type": "DateTime",  
    "value": "2020-03-17T08:45:00Z/2020-04-22T18:45:00Z",  
    "metadata": {  
      "TimeInstant": {  
        "type": "Text",  
        "value": "2020-04-02T10:30:00Z"  
      }  
    }  
  },  
  "startDate": {  
    "type": "DateTime",  
    "value": "2020-03-17T08:45:00Z",  
    "metadata": {  
      "TimeInstant": {  
        "type": "Text",  
        "value": "2020-02-01TT17:25:00Z"  
      }  
    }  
  },  
  "endDate": {  
    "type": "DateTime",  
    "value": "2020-04-22T18:45:00Z",  
    "metadata": {  
      "TimeInstant": {  
        "type": "Text",  
        "value": "2020-04-02T10:30:00Z"  
      }  
    }  
  },  
  "openingHoursSpecification": {  
    "type": "array",  
    "value": [  
      {  
        "dayOfWeek": "Monday",  
        "opens": "07:00:00",  
        "closes": "20:00:00"  
      },  
      {  
        "dayOfWeek": "Tuesday",  
        "opens": "07:00:00",  
        "closes": "20:00:00"  
      },  
      {  
        "dayOfWeek": "Wednesday",  
        "opens": "07:00:00",  
        "closes": "20:00:00"  
      },  
      {  
        "dayOfWeek": "Thursday",  
        "opens": "07:00:00",  
        "closes": "20:00:00"  
      },  
      {  
        "dayOfWeek": "Friday",  
        "opens": "07:00:00",  
        "closes": "20:00:00"  
      },  
      {  
        "dayOfWeek": "Saturday",  
        "opens": "08:30:00",  
        "closes": "17.00:00"  
      }  
    ]  
  },  
  "contractingAuthority": {  
    "type": "string",  
    "value": "MNCA - subwaypole Nice Cote d'Azur"  
  },  
  "contactPoint": {  
    "type": "string",  
    "value": "Service des AO"  
  },  
  "decrees": {  
    "type": "array",  
    "value": [  
      "https://MNCA/CityWork/Decree/CW-2020Q2-006",  
      "CW-2020Q2-006",  
      "CW-2020Q2-006-Av-001",  
      "CW-2020Q2-006-Av-002"  
    ]  
  },  
  "workLastDateUpdate": {  
    "type": "DateTime",  
    "value": "2020-03-17T08:45:00Z",  
     "metadata": {  
      "TimeInstant": {  
        "type": "Text",  
        "value": "2020-03-16T09:12:25Z"  
      }  
    }  
  },  
  "mainContractingCompany": {  
    "type": "string",  
    "value": "XRP - NICOLSPA"  
  },  
  "othersContractingCompagny": {  
    "type": "array",  
    "value": [  
      "VRD - Terrassement Nicois",  
      "ELEC - Electricite de Nice",  
      "NUM - Consortium operateur"  
    ]  
  },  
  "workLevel": {  
    "type": "array",  
    "value": [  
      "ground",  
      "underground"  
    ]  
  },  
  "workTarget": {  
    "type": "array",  
    "value": [  
      "electricityNetworks",  
      "opticalFibers",  
      "pavement",  
      "roads",  
      "videoNetworks",  
      "vrd"  
    ]  
  },  
  "workNature": {  
    "type": "array",  
    "value": [  
      "landFill",  
      "repair",  
      "securingPerimeter",  
      "tarring",  
      "tonnageExemption",  
      "trenchOpening"  
    ]  
  },  
  "infrastructureFunction": {  
    "type": "array",  
    "value": [  
      "collection",  
      "distribution"  
    ]  
  },  
  "encroachment": {  
    "type": "array",  
    "value": [  
      "private",  
      "public"  
    ]  
  },  
  "typeOfInterventionRequest": {  
    "type": "string",  
    "value": "authorizationRequest"  
  },  
  "workReason": {  
    "type": "array",  
    "value": [  
      "sagging",  
      "powerCut"  
    ]  
  },  
  "workZone": {  
    "type": "array",  
    "value": [  
      "busCorridor",  
      "road",  
      "sideWalk",  
      "tramwayLine"  
    ]  
  },  
  "workDisposition": {  
    "type": "array",  
    "value": [  
      {  
        "disposition": "laneReduction",  
        "startDate": "2020-05-11T08:00:00Z",  
        "endDate": "2020-05-15T18:30:00Z",  
        "dayOfWeek": [  
          "Monday",  
          "Tuesday",  
          "Wednesday",  
          "Thursday",  
          "Friday"  
        ],  
        "comment": "Switching from 2 lanes to 1 lane - BusCorridor not available"  
      },  
      {  
        "disposition": "sidewalkReduction",  
        "startDate": "2020-05-12T00:00:00Z",  
        "endDate": "2020-05-14T24:00:00Z",  
        "dayOfWeek": [  
          "Monday",  
          "Tuesday",  
          "Wednesday",  
          "Thursday",  
          "Friday",  
          "Saturday",  
          "Sunday"  
        ]  
      },  
      {  
        "disposition": "alternatingLights",  
        "startDate": "2020-05-11T08:00:00Z",  
        "endDate": "2020-05-15T18:30:00Z",  
        "dayOfWeek": [  
          "Monday",  
          "Tuesday",  
          "Wednesday",  
          "Thursday",  
          "Friday"  
        ]  
      },  
      {  
        "disposition": "speedReduction",  
        "startDate": "2020-05-12T00:00:00Z",  
        "dayOfWeek": [  
          "Monday",  
          "Tuesday",  
          "Wednesday",  
          "Thursday",  
          "Friday",  
          "Saturday",  
          "Sunday"  
        ],  
        "comment": "Speed Switching from 2 lanes to 1 lane"  
      }  
    ]  
  },  
  "workOtherImpact": {  
    "type": "array",  
    "value": [  
      "layingCablesOnGround",  
      "shopsTerrace"  
    ]  
  },  
  "isMobile": {  
    "type": "Boolean",  
    "value": false  
  },  
  "countOfDerogation": {  
    "type": "number",  
    "value": 2  
  },  
  "derogation": {  
    "type": "array",  
    "value": [  
      {  
        "derogationType": "Work Night during Workday",  
        "startDate": "2020-05-11T20:30:00Z",  
        "endDate": "2020-05-15T23:30:00",  
        "dayOfWeek": [  
          "Monday",  
          "Tuesday",  
          "Wednesday",  
          "Thursday",  
          "Friday"  
        ]  
      },  
      {  
        "derogationType": "BRH",  
        "startDate": "2020-05-13T20:30:00Z",  
        "endDate": "2020-05-13T23:30:00Z",  
        "dayOfWeek": [  
          "Wednesday"  
        ]  
      }  
    ]  
  },  
  "isMainRoadImpactedHTR": {  
    "type": "Boolean",  
    "value": true  
  },  
  "countOfRoadImpacted": {  
    "type": "number",  
    "value": 3  
  },  
  "roadImpacted": {  
    "type": "array",  
    "value": [  
      {  
        "roadImpacted": "urn:ngsi-ld:Road:N202",  
        "segmentImpacted": [  
          "urn:ngsi-ld:RoadSegment:N202-12",  
          "urn:ngsi-ld:RoadSegment:N202-13"  
        ]  
      },  
      {  
        "roadImpacted": "Road:D021",  
        "segmentImpacted": [  
          "12",  
          "13",  
          "14",  
          "15"  
        ]  
      },  
      {  
        "roadImpacted": "urn:ngsi-ld:Road:D032",  
        "segmentArea": {  
          "type": "LineString",  
          "coordinates": [  
            [  
              102.0,  
              0.0  
            ],  
            [  
              103.0,  
              1.0  
            ],  
            [  
              104.0,  
              0.0  
            ],  
            [  
              105.0,  
              1.0  
            ]  
          ]  
        }  
      }  
    ]  
  },  
  "allowedVehicle": {  
    "type": "array",  
    "value": [  
      "companiesTrucks",  
      "emergencyVehicle",  
      "firefighters",  
      "police"  
    ]  
  },  
  "maxAuthorizedTonnage": {  
    "type": "array",  
    "value": [  
      {  
        "roadImpacted": "urn:ngsi-ld:Road:N202",  
        "maxTonnage": 30  
      },  
      {  
        "roadImpacted": "Road:D021",  
        "maxTonnage": 20  
      },  
      {  
        "roadImpacted": "urn:ngsi-ld:Road:D032",  
        "maxTonnage": 15.2  
      }  
    ]  
  },  
  "countOfBusLineImpacted": {  
    "type": "number",  
    "value": 1  
  },  
  "busImpacted": {  
    "type": "array",  
    "value": [  
      {  
        "lineImpacted": "urn:ngsi-ld:BusLine:L205"  
      }  
    ]  
  },  
  "countOfTramwayLineImpacted": {  
    "type": "number",  
    "value": 2  
  },  
  "tramwayImpacted": {  
    "type": "array",  
    "value": [  
      {  
        "lineImpacted": "TramWayLine:L01",  
        "segmentImpacted": [  
          "urn:ngsi-ld:TramWaySegment:L01-12",  
          "urn:ngsi-ld:TramWaySegment:L01-19"  
        ]  
      },  
      {  
        "lineImpacted": "TramWayLine:L03",  
        "segmentImpacted": [  
          "urn:ngsi-ld:TramWaySegment:L03-19"  
        ]  
      }  
    ]  
  },  
  "countOfRailwayLineImpacted": {  
    "type": "number",  
    "value": 1  
  },  
  "railwayImpacted": {  
    "type": "array",  
    "value": [  
      {  
        "lineImpacted": "Nice-Grasse",  
        "segmentImpact": [  
          "Nice Saint Augustin section"  
        ]  
      }  
    ]  
  },  
  "countOfSchoolImpacted": {  
    "type": "number",  
    "value": 2  
  },  
  "schoolImpacted": {  
    "type": "array",  
    "value": [  
      "Lycée Massena",  
      "Université Campus Saint Jean"  
    ]  
  },  
  "countOfStationImpacted": {  
    "type": "number",  
    "value": 4  
  },  
  "stationImpacted": {  
    "type": "array",  
    "value": [  
      {  
        "stationType": "bus",  
        "stationId": [  
          "urn:ngsi-ld:station:L205-S13",  
          "urn:ngsi-ld:station:L205-S14"  
        ]  
      },  
      {  
        "stationType": "tram",  
        "stationId": [  
          "L01-S12",  
          "L01-S19"  
        ]  
      }  
    ]  
  },  
  "countOfEventImpacted": {  
    "type": "number",  
    "value": 2  
  },  
  "eventsImpact": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:events:MNCA-EV-JazzCimiez",  
      "NiceMarathon"  
    ]  
  }  
}  
```  
#### CityWork NGSI-LDのキーバリューの例  
ここでは、CityWorkをkey-valuesとしてJSON-LD形式で表現した例を紹介します。これは`options=keyValues`を使うとNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "id": "urn:ngsi-ld:CityWork:CityWork:MNCA-CW-2020Q2-006",  
  "type": "CityWork",  
  "name": "Nce-Airport-CW2020Q2-006",  
  "alternateName": "AirPort global Observation",  
  "description": "Widening work on access roads and installation of a new electrical and digital network for the connection of T1 & T2 terminals",  
  "location": {  
    "type": "Polygon",  
    "coordinates": [  
      [  
        43.20315,  
        7.20186  
      ],  
      [  
        43.20384,  
        7.20372  
      ],  
      [  
        43.20388,  
        7.20493  
      ],  
      [  
        43.19938,  
        7.20312  
      ],  
      [  
        43.20045,  
        7.20152  
      ],  
      [  
        43.20315,  
        7.20186  
      ]  
    ]  
  },  
  "areaServed": "Nice Aeroport",  
  "territorialArea": "subwaypole Nice",  
  "dateLastReported": "2020-04-02T10:30:00Z",  
  "workNumber": "CW2020Q2-006",  
  "workState": "open",  
  "workDate": "2020-03-17T08:45:00Z/2020-04-22T18:45:00Z",  
  "startDate": "2020-03-17T08:45:00Z",  
  "endDate": "2020-04-22T18:45:00Z",  
  "openingHoursSpecification": [  
    {  
      "dayOfWeek": "Monday",  
      "opens": "07:00:00",  
      "closes": "20:00:00"  
    },  
    {  
      "dayOfWeek": "Tuesday",  
      "opens": "07:00:00",  
      "closes": "20:00:00"  
    },  
    {  
      "dayOfWeek": "Wednesday",  
      "opens": "07:00:00",  
      "closes": "20:00:00"  
    },  
    {  
      "dayOfWeek": "Thursday",  
      "opens": "07:00:00",  
      "closes": "20:00:00"  
    },  
    {  
      "dayOfWeek": "Friday",  
      "opens": "07:00:00",  
      "closes": "20:00:00"  
    },  
    {  
      "dayOfWeek": "Saturday",  
      "opens": "08:30:00",  
      "closes": "17:00:00"  
    }  
  ],  
  "contractingAuthority": "MNCA - subwaypole Nice Cote d'Azur",  
  "contactPoint": {  
    "name": "Service des AO"  
  },  
  "decrees": [  
    "https://MNCA/CityWork/Decree/CW-2020Q2-006",  
    "CW-2020Q2-006",  
    "CW-2020Q2-006-Av-001",  
    "CW-2020Q2-006-Av-002"  
  ],  
  "workLastDateUpdate": "2020-03-17T08:45:00Z",  
  "mainContractingCompagny": "XRP - NICOLSPA",  
  "othersContractingCompagny": [  
    "VRD - Terrassement Nicois",  
    "ELEC - Electricite de Nice",  
    "NUM - Consortium operateur"  
  ],  
  "workLevel": [  
    "ground",  
    "underground"  
  ],  
  "workTarget": [  
    "roads",  
    "pavement",  
    "electricityNetworks",  
    "opticalFibers",  
    "videoNetworks",  
    "vrd"  
  ],  
  "workNature": [  
    "landFill",  
    "repair",  
    "tonnageExemption",  
    "securingPerimeter",  
    "trenchOpening",  
    "tarring"  
  ],  
  "infrastructureFunction": [  
    "distribution",  
    "collection"  
  ],  
  "encroachment": [  
    "public",  
    "private"  
  ],  
  "typeOfInterventionRequest": "authorizationRequest",  
  "workReason": [  
    "sagging",  
    "powerCut"  
  ],  
  "workZone": [  
    "road",  
    "sideWalk",  
    "busCorridor",  
    "tramwayLine"  
  ],  
  "workDisposition": [  
    {  
      "disposition": "laneReduction",  
      "startDate": "2020-05-11T08:00:00Z",  
      "endDate": "2020-05-15T18:30:00Z",  
      "dayOfWeek": [  
        "Monday",  
        "Tuesday",  
        "Wednesday",  
        "Thursday",  
        "Friday"  
      ],  
      "comment": "Switching from 2 lanes to 1 lane - BusCorridor not available"  
    },  
    {  
      "disposition": "sidewalkReduction",  
      "startDate": "2020-05-12T00:00:00Z",  
      "endDate": "2020-05-14T24:00:00Z",  
      "dayOfWeek": [  
        "Monday",  
        "Tuesday",  
        "Wednesday",  
        "Thursday",  
        "Friday"  
      ]  
    },  
    {  
      "disposition": "alternatingLights",  
      "startDate": "2020-05-11T08:00:00Z",  
      "endDate": "2020-05-15T18:30:00Z",  
      "dayOfWeek": [  
        "Monday",  
        "Tuesday",  
        "Wednesday",  
        "Thursday",  
        "Friday"  
      ]  
    },  
    {  
      "disposition": "speedReduction",  
      "startDate": "2020-05-12T00:00:00Z",  
      "dayOfWeek": [  
        "Monday",  
        "Tuesday",  
        "Wednesday",  
        "Thursday",  
        "Friday",  
        "Saturday",  
        "Sunday"  
      ],  
      "comment": "Speed Switching from 2 lanes to 1 lane"  
    }  
  ],  
  "workOtherImpact": [  
      "layingCablesOnGround",  
      "shopsTerrace"  
    ]  
  ,  
  "isMobile": false,  
  "countOfDerogation": 2,  
  "derogation": [  
    {  
      "derogationType": "Work Nigth during Workday",  
      "startDate": "2020-05-11T20:30:00Z",  
      "endDate": "2020-05-15T23:30:00",  
      "dayOfWeek": [  
        "Monday",  
        "Tuesday",  
        "Wednesday",  
        "Thursday",  
        "Friday"  
      ]  
    },  
    {  
      "derogationType": "BRH",  
      "startDate": "2020-05-13T20:30:00Z",  
      "endDate": "2020-05-13T23:30:00Z",  
      "dayOfWeek": [  
        "Wednesday"  
      ]  
    }  
  ],  
  "isMainRoadImpactedHTR": true,  
  "countOfRoadImpacted": 3,  
  "roadImpacted": [  
    {  
      "roadId": "urn:ngsi-ld:Road:N202",  
      "segmentImpacted": [  
        "urn:ngsi-ld:RoadSegment:N202-12",  
        "urn:ngsi-ld:RoadSegment:N202-13"  
      ]  
    },  
    {  
      "roadId": "Road:D021",  
      "segmentImpacted": [  
        "12",  
        "13",  
        "14",  
        "15"  
      ]  
    },  
    {  
      "roadId": "urn:ngsi-ld:Road:D032",  
      "segmentArea": {  
        "type": "LineString",  
        "coordinates": [  
          [  
            102.0,  
            0.0  
          ],  
          [  
            103.0,  
            1.0  
          ],  
          [  
            104.0,  
            0.0  
          ],  
          [  
            105.0,  
            1.0  
          ]  
        ]  
      }  
    }  
  ],  
  "allowedVehicle": [  
    "firefighters",  
    "police",  
    "emergencyVehicle",  
    "companiesTrucks"  
  ],  
  "maxAuthorizedTonnage": [  
    {  
      "roadImpacted": "urn:ngsi-ld:Road:N202",  
      "maxTonnage": 30  
    },  
    {  
      "roadImpacted": "Road:D021",  
      "maxTonnage": 20  
    },  
    {  
      "roadImpacted": "urn:ngsi-ld:Road:D032",  
      "maxTonnage": 15.2  
    }  
  ],  
  "countOfBusLineImpacted": 1,  
  "busImpacted": [  
    {  
      "lineImpacted": "urn:ngsi-ld:BusLine:L205"  
    }  
  ],  
  "countOfTramwayLineImpacted": 2,  
  "tramwayImpacted": [  
    {  
      "lineImpacted": "TramWayLine:L01",  
      "segmentImpacted": [  
        "urn:ngsi-ld:TramWaySegment:L01-12",  
        "urn:ngsi-ld:TramWaySegment:L01-19"  
      ]  
    },  
    {  
      "lineImpacted": "TramWayLine:L03",  
      "segmentImpacted": [  
        "urn:ngsi-ld:TramWaySegment:L03-19"  
      ]  
    }  
  ],  
  "countOfRailwayLineImpacted": 1,  
  "railwayImpacted": [  
    {  
      "lineImpacted": "Nice-Grasse",  
      "segmentImpact": [  
        "Nice Saint Augustin section"  
      ]  
    }  
  ],  
  "countOfSchoolImpacted": 2,  
  "schoolImpacted": [  
    "Lycée Massena",  
    "Université Campus Saint Jean"  
  ],  
  "countOfStationImpacted": 4,  
  "stationImpacted": [  
    {  
      "stationType": "bus",  
      "stationId": [  
        "urn:ngsi-ld:station:L205-S13",  
        "urn:ngsi-ld:station:L205-S14"  
      ]  
    },  
    {  
      "stationType": "tram",  
      "stationId": [  
        "L01-S12",  
        "L01-S19"  
      ]  
    }  
  ],  
  "countOfEventImpacted": 2,  
  "eventsImpact": [  
    "urn:ngsi-ld:events:MNCA-EV-JazzCimiez",  
    "NiceMarathon"  
  ],  
  "@context": [  
    "https://smartdatamodels.org/context",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### CityWork NGSI-LDの正規化例  
ここでは、正規化されたJSON-LD形式のCityWorkの例を示します。これはオプションを使用しない場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "id": "urn:ngsi-ld:CityWork:CityWork:MNCA-CW-2020Q2-006",  
  "type": "CityWork",  
  "name": {  
    "type": "Property",  
    "value": "Nce-Airport-CW2020Q2-006"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "AirPort global Observation"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Widening work on access roads and installation of a new electrical and digital network for the connection of T1 & T2 terminals"  
  },  
  "location": {  
    "type": "Geoproperty",  
    "value": {  
      "type": "Polygon",  
      "coordinates": [  
        [  
          43.20315,  
          7.20186  
        ],  
        [  
          43.20384,  
          7.20372  
        ],  
        [  
          43.20388,  
          7.20493  
        ],  
        [  
          43.19938,  
          7.20312  
        ],  
        [  
          43.20045,  
          7.20152  
        ],  
        [  
          43.20315,  
          7.20186  
        ]  
      ]  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Nice Aeroport"  
  },  
  "territorialArea": {  
    "type": "Property",  
    "value": "subwaypole Nice"  
  },  
  "dateLastReported": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2020-04-02T10:30:00Z"  
    }  
  },  
  "workNumber": {  
    "type": "Property",  
    "value": "CW2020Q2-006"  
  },  
  "workState": {  
    "type": "Property",  
    "value": "open"  
  },  
  "workDate": {  
    "type": "DateTime",  
    "value": "2020-03-17T08:45:00Z/2020-04-22T18:45:00Z"  
  },  
  "startDate": {  
    "type": "DateTime",  
    "value": "2020-03-17T08:45:00Z"  
  },  
  "endDate": {  
    "type": "DateTime",  
    "value": "2020-04-22T18:45:00Z"  
  },  
  "openingHoursSpecification": {  
    "type": "Property",  
    "value": [  
      {  
        "dayOfWeek": "Monday",  
        "Opens": "07.00",  
        "closes": "20.00"  
      },  
      {  
        "dayOfWeek": "Tuesday",  
        "Opens": "07.00",  
        "closes": "20.00"  
      },  
      {  
        "dayOfWeek": "Wednesday",  
        "Opens": "07.00",  
        "closes": "20.00"  
      },  
      {  
        "dayOfWeek": "Thursday",  
        "Opens": "07.00",  
        "closes": "20.00"  
      },  
      {  
        "dayOfWeek": "Friday",  
        "Opens": "07.00",  
        "closes": "20.00"  
      },  
      {  
        "dayOfWeek": "Saturday",  
        "Opens": "08.30",  
        "closes": "17.00"  
      }  
    ]  
  },  
  "contractingAuthority": {  
    "type": "Property",  
    "value": "MNCA - subwaypole Nice Cote d'Azur"  
  },  
  "contactPoint": {  
    "type": "Property",  
    "value": "Service des AO"  
  },  
  "decrees": {  
    "type": "Property",  
    "value": [  
      "https://MNCA/CityWork/Decree/CW-2020Q2-006",  
      "CW-2020Q2-006",  
      "CW-2020Q2-006-Av-001",  
      "CW-2020Q2-006-Av-002"  
    ]  
  },  
  "workLastDateUpdate": {  
    "type": "DateTime",  
    "value": "2020-03-17T08:45:00Z"  
  },  
  "mainContractingCompany": {  
    "type": "Property",  
    "value": "XRP - NICOLSPA"  
  },  
  "othersContractingCompany": {  
    "type": "Property",  
    "value": [  
      "VRD - Terrassement Nicois",  
      "ELEC - Electricite de Nice",  
      "NUM - Consortium operateur"  
    ]  
  },  
  "workLevel": {  
    "type": "Property",  
    "value": [  
      "ground",  
      "underGround"  
    ]  
  },  
  "workTarget": {  
    "type": "Property",  
    "value": [  
      "electricityNetworks",  
      "opticalFibers",  
      "pavement",  
      "roads",  
      "videoNetworks",  
      "vrd"  
    ]  
  },  
  "workNature": {  
    "type": "Property",  
    "value": [  
      "landFill",  
      "repair",  
      "securingPerimeter",  
      "tarring",  
      "tonnageExemption",  
      "trenchOpening"  
    ]  
  },  
  "infrastructureFunction": {  
    "type": "Property",  
    "value": [  
      "collection",  
      "distribution"  
    ]  
  },  
  "encroachment": {  
    "type": "Property",  
    "value": [  
      "private",  
      "public"  
    ]  
  },  
  "typeOfInteventionRequest": {  
    "type": "Property",  
    "value": "authorizationRequest"  
  },  
  "workReason": {  
    "type": "Property",  
    "value": [  
      "powerCut",  
      "sagging"  
    ]  
  },  
  "workZone": {  
    "type": "Property",  
    "value": [  
      "busCorridor",  
      "road",  
      "sideWalk",  
      "tramwayLine"  
    ]  
  },  
  "workDisposition": {  
    "type": "Property",  
    "value": [  
      {  
        "disposition": "laneReduction",  
        "startDate": "2020-05-11T08:00:00Z",  
        "endDate": "2020-05-15T18:30:00Z",  
        "dayOfWeek": [  
          "Monday",  
          "Tuesday",  
          "Wednesday",  
          "Thursday",  
          "Friday"  
        ],  
        "comment": "Switching from 2 lanes to 1 lane - BusCorridor not available"  
      },  
      {  
        "disposition": "sidewalkReduction",  
        "startDate": "2020-05-12T00:00:00Z",  
        "endDate": "2020-05-14T24:00:00Z",  
        "dayOfWeek": [  
          "Monday",  
          "Tuesday",  
          "Wednesday",  
          "Thursday",  
          "Friday",  
          "Saturday",  
          "Sunday"  
        ]  
      },  
      {  
        "disposition": "alternatingLights",  
        "startDate": "2020-05-11T08:00:00Z",  
        "endDate": "2020-05-15T18:30:00Z",  
        "dayOfWeek": [  
          "Monday",  
          "Tuesday",  
          "Wednesday",  
          "Thursday",  
          "Friday"  
        ]  
      },  
      {  
        "disposition": "speedReduction",  
        "startDate": "2020-05-12T00:00:00Z",  
        "dayOfWeek": [  
          "Monday",  
          "Tuesday",  
          "Wednesday",  
          "Thursday",  
          "Friday",  
          "Saturday",  
          "Sunday"  
        ],  
        "comment": "Speed Switching from 2 lanes to 1 lane"  
      }  
    ],  
    "workOtherImpact": {  
      "type": "Property",  
      "value": [  
        "layingCablesOnGround",  
        "shopsTerrace"  
      ]  
    },  
    "isMobile": {  
      "type": "Property",  
      "value": false  
    },  
    "countOfDerogation": {  
      "type": "Property",  
      "value": 2  
    },  
    "derogation": {  
      "type": "Property",  
      "value": [  
        {  
          "derogationType": "Work Nigth during Workday",  
          "startDate": "2020-05-11T20:30:00Z",  
          "endDate": "2020-05-15T23:30:00",  
          "dayOfWeek": [  
            "Monday",  
            "Tuesday",  
            "Wednesday",  
            "Thursday",  
            "Friday",  
            "Saturday",  
            "Sunday"  
          ]  
        },  
        {  
          "derogationType": "BRH",  
          "startDate": "2020-05-13T20:30:00Z ",  
          "endDate": "2020-05-13T23:30:00Z",  
          "dayOfWeek": "Wednesday"  
        }  
      ]  
    },  
    "isMainRoadImpactedHTR": {  
      "type": "Property",  
      "value": true  
    },  
    "countOfRoadImpacted": {  
      "type": "Property",  
      "value": 3  
    },  
    "roadImpacted": {  
      "type": "Property",  
      "value": [  
        {  
          "roadId": "urn:ngsi-ld:Road:N202",  
          "segmentId": [  
            "urn:ngsi-ld:RoadSegment:N202-12",  
            "urn:ngsi-ld:RoadSegment:N202-13"  
          ]  
        },  
        {  
          "roadId": "Road:D021",  
          "segmentName": [  
            "Nº 12",  
            "Nº 13",  
            "Nº 14"  
          ]  
        },  
        {  
          "roadId": "urn:ngsi-ld:Road:D032",  
          "segmentLocation": [  
            {  
              "type": "LineString",  
              "coordinates": [  
                [  
                  102.0,  
                  0.0  
                ],  
                [  
                  103.0,  
                  1.0  
                ],  
                [  
                  104.0,  
                  0.0  
                ],  
                [  
                  105.0,  
                  1.0  
                ]  
              ]  
            },  
            {  
              "type": "Point",  
              "coordinates": [  
                43.655675,  
                7.161232  
              ]  
            }  
          ]  
        },  
        {  
          "roadLocation": {  
            "type": "Point",  
            "coordinates": [  
              43.67428,  
              7.161589  
            ]  
          }  
        }  
      ]  
    },  
    "allowedVehicle": {  
      "type": "Property",  
      "value": [  
        "companiesTrucks",  
        "emergencyVehicle",  
        "firefighters",  
        "police"  
      ]  
    },  
    "maxAuthorizedTonnage": {  
      "type": "Property",  
      "value": [  
        {  
          "roadImpacted": "urn:ngsi-ld:Road:N202",  
          "maxTonnage": 30  
        },  
        {  
          "roadImpacted": "Road:D021",  
          "maxTonnage": 20  
        },  
        {  
          "roadImpacted": "urn:ngsi-ld:Road:D032",  
          "maxTonnage": 15.2  
        }  
      ]  
    },  
    "countOfBusLineImpacted": {  
      "type": "Property",  
      "value": 1  
    },  
    "busImpacted": {  
      "type": "Property",  
      "value": [  
        {  
          "lineImpacted": "urn:ngsi-ld:BusLine:L205"  
        }  
      ]  
    },  
    "countOfTramwayLineImpacted": {  
      "type": "Property",  
      "value": 2  
    },  
    "tramwayImpacted": {  
      "type": "Property ",  
      "value": [  
        {  
          "lineImpacted": "TramWayLine:L01",  
          "segmentImpacted": [  
            "urn:ngsi-ld:TramWaySegment:L01-12",  
            "urn:ngsi-ld:TramWaySegment:L01-19"  
          ]  
        },  
        {  
          "lineImpacted": "TramWayLine:L03",  
          "segmentImpacted": [  
            "urn:ngsi-ld:TramWaySegment:L03-19"  
          ]  
        }  
      ]  
    },  
    "countOfRailwayLineImpacted": {  
      "type": "Property",  
      "value": 1  
    },  
    "railwayImpacted": {  
      "type": "Property ",  
      "value": [  
        {  
          "lineImpacted": "Nice-Grasse",  
          "segmentImpact": [  
            "Nice Saint Augustin section"  
          ]  
        }  
      ]  
    },  
    "countOfSchoolImpacted": {  
      "type": "Property",  
      "value": 2  
    },  
    "schoolImpacted": {  
      "type": "Property",  
      "value": [  
        "Lycée Massena",  
        "Université Campus Saint Jean"  
      ]  
    },  
    "countOfStationImpacted": {  
      "type": "Property",  
      "value": 4  
    },  
    "stationImpacted": {  
      "type": "Property ",  
      "value": [  
        {  
          "stationType": "bus",  
          "stationId": [  
            "urn:ngsi-ld:station:L205-S13",  
            "urn:ngsi-ld:station:L205-S14"  
          ]  
        },  
        {  
          "stationType": "tram",  
          "stationId": [  
            "L01-S12",  
            "L01-S19"  
          ]  
        }  
      ]  
    },  
    "countOfEventImpacted": {  
      "type": "Property",  
      "value": 2  
    },  
    "eventsImpact": {  
      "type": "Property",  
      "value": [  
        "urn:ngsi-ld:events:MNCA-EV-JazzCimiez",  
        "NiceMarathon"  
      ]  
    },  
    "@context": [  
      "https://smartdatamodels.org/ld/context",  
      "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
  }  
}  
```  
