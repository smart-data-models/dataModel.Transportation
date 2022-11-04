<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
事業者ロードアクシデント  
============<!-- /10-Header -->  
<!-- 15-License -->  
[オープンライセンス](https://github.com/smart-data-models//dataModel.Transportation/blob/master/RoadAccident/LICENSE.md)  
[ドキュメント自動生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述です。**原因や後遺症を含む交通事故の説明。Synchronicityプロジェクトで開発された最初のバージョン**。  
バージョン: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティ一覧  

<sup><sub>[*] 属性にタイプがない場合、複数のタイプまたは異なるフォーマット/パターンを持つ可能性があるためです</sub></sup>。  
- `accidentDate[string]`: 事故発生時刻  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `accidentDescription[array]`: この交通事故について、状況をコード化したものを組み合わせて記述しています。0：特定できない状況 1：曲がることなく定常的に進行した 2：脇見運転または進路未定で進行した 3：車間距離を取らずに進行した 4：右からの車両を優先せずに進行した 5：停止を守らずに進行した 6：優先信号を守らずに進行した 7：交通に逆らって進行した 8：信号または代行信号を守らずに進行した 10：進入禁止の標識を守らずに進行した 6：進入禁止を守らずに進行した 7：進入した車両を優先した信号や係員信号を無視して進行した 10: 通行禁止や進入禁止の標識を無視して進行した 11: スピードを出して進行した 12: 制限速度を無視して進行した 13: 他の車両を横切るまぶしい光で進行した 14: 規則正しく右折した 15: 他の車両を横切るまぶしい光で進行した 6:14: 規則正しく右折した 15: 不規則に右折した 16: 規則正しく左折した 17: 不規則に左折した 18: 交差点を通過した 20: 規則正しく進行した 21: 脇見運転や未決定で進行した 22: 安全距離を保たずに進行した 23: スピードを出して進行した 24: スピードを出さずに進行した制限速度を守らずに進行した 25: 車道の右端に寄らずに進行した 26: 交通に逆らって進行した 27: 通行・進入禁止の標識を守らずに進行した 28: 他の車両を横切る眩しいライトで進行した 29: 規則的に通過した 30: 右側通行が不規則だった 31:カーブや坂道、見通しの悪い場所で追い越した 32: 他の車両を追い越していた 33: 適切な禁止標識を守らずに追い越した 34: 降格または転換の操作をした 35: 循環の流れに乗る操作をした 36: 左折する操作をした （専用通路、分配器） 37:運転者が規則的に停止または停止するように操縦した、38：運転者が不規則に停止または停止するように操縦した、39：他の不規則な二輪車が加わった、40：運転者が規則的に進行した、41：運転者が速度を出して進行した、42：運転者が制限速度を守らずに進行した、43：運転者が交通に対して進行した、44：運転者がギアで車両を通過した、45：操縦した、46：操縦した。信号や係員信号を無視して運転した 47: 警戒せずに車道に出てきた 48: 車線から飛び出して手先にぶつかった 49: 適正な横断歩道で歩行者を優先しなかった 50: 横断を許可するために停止している車両を追い越した 51: 荷物を持った歩行者にぶつかった 52: 停留所で路面電車を不均等に追い抜いていた 60:運転者が規則的に進行した 61: 運転者が脇見運転または進路未定で進行した 62: 運転者が安全な距離を保たずに進行した 63: 運転者が交通に逆らって進行した 64: 運転者がスピード違反で進行した 65: 運転者が制限速度を守らずに進行した 66: 運転者が通過禁止または進入禁止の標識を守らずに進行した 67:運転者がギアを入れたまま他の車両を追い越した、 68: 運転者が軽率に踏切を横断した、 70: 衝撃を避けるためにこぼれ話をした、 71:漫然運転で流出ありのリスト、72:速度超過のこぼれ話でリスト、73:運転者が急ブレーキをかけ、その結果搬送されたもの、74:ドア開放による車両からの人の転落； 75: 走行中の車両からの降下による人の転落； 76:76: しがみつき、または不適切な配置による車両からの人の落下 80: ブレーキの故障または不具合 81:破損またはステアリングの故障、82：タイヤの破裂または過度の磨耗、83．前照灯またはポジションランプの欠品または不足、84：点滅灯または停止灯の欠品または不足、85：トレーラー連結部の破損、86：危険物輸送用具の不備、87．身体障害者用車両に定められた適合の不備 88：車輪の脱落 89：自転車用視覚装置の欠落又は不足  . Model: [https://schema.org/Text](https://schema.org/Text)- `accidentLocation[string]`: 事故が市街地または市外地域で発生した場合の簡単な説明。0：市街地内の地方 1：町内の市道 2：町内の省道 3：村内の国道 4：都市外道路 5：省道 6：国道 7：高速道路 8：別の道 9：地方道路  - `accidentStatisticalDate[object]`: 事故のおおよその発生日時（元の事故データソースは、季節、平日、おおよその時間帯などの統計的属性のみを報告していることが多い  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `accidentType[array]`: この交通事故の分類を簡単に説明します。1：前面衝突、2：前面-側面衝突、3：側面衝突、4：衝突、5：歩行者死亡、6：停止または停車中の車両との衝突、7：駐車車両との衝突、8：障害物との衝突、9：列車との衝突、10：流出、スリップ、11：急制動による事故、12：車両からの転落による事故、。  - `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: この項目の別称  - `areaServed[string]`: サービスまたは提供品が提供される地理的な地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 調和されたデータエンティティの提供者を識別する一連の文字。  - `dateCreated[string]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateModified[string]`: エンティティの最終更新のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: このアイテムの説明  - `id[*]`: エンティティの一意な識別子  - `localId[string]`: ソースデータセットからの一意な識別子  . Model: [https://schema.org/Text](https://schema.org/Text)- `location[*]`: アイテムへの Geojson リファレンス。Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygonのいずれかを指定することができる。  - `name[string]`: このアイテムの名称です。  - `numPassengersDead[integer]`: 事故により死亡した同乗者の数  . Model: [https://schema.org/Number](https://schema.org/Number)- `numPassengersInjured[integer]`: 事故による同乗者の負傷者数  . Model: [https://schema.org/Number](https://schema.org/Number)- `numPedestrianDead[integer]`: 事故による歩行者死亡者数  . Model: [https://schema.org/Number](https://schema.org/Number)- `numPedestrianInjured[integer]`: 事故による歩行者負傷者数  . Model: [https://schema.org/Number](https://schema.org/Number)- `owner[array]`: 所有者の一意のIDを参照するJSONエンコードされた文字列を含むリストです。  - `pedestriansInvolved[boolean]`: 歩行者が事故に巻き込まれたかどうかを判断するためのブール値  - `roadClass[string]`: 事故が発生した道路の区分  . Model: [https://wiki.openstreetmap.org/wiki/Key:highway](https://wiki.openstreetmap.org/wiki/Key:highway)- `roadIntersection[string]`: 事故が発生した道路の一部を簡単に説明する。   1：十字路、2：ラウンドアバウト、3：報告された交差点、4：信号機のある交差点、5：報告されていない交差点、6：踏切、7：直線、8：カーブ、9：バンプ、ボトルネック、10：坂、11：照明付きギャラリー、12：照明なしのギャラリーを示す。  - `roadPaving[string]`: 道路の舗装。1：舗装道路、2：粗舗装道路、3：未舗装道路。  - `roadSign[string]`: 事故が発生した道路標識の簡単な説明。1：なし、2：縦、3：横、4：縦と横、5：工事現場による仮設。  - `roadSurface[string]`: 事故時の道路の状態を簡単に説明する。1：乾いている、2：濡れている、3：滑りやすい、4：凍結している、5：雪が積もっている。  - `roadTrunk[string]`: 事故が発生した道路の幹の種類を簡単に説明する。1：道路分岐、2：二次分岐、3：マイナー分岐、4：ジャンクション分岐、5：道路分岐、6：自動車道左車線、7：高速道路右、8：自動車道ジャンクション入口、9：高速道路出口ジャンクション、10：高速道路ジャンクション幹、11：高速道路駅、12：その他のケース、15：都市外道路。  - `seeAlso[*]`: 項目に関する追加リソースを指すURIのリスト。  - `source[string]`: エンティティデータの元のソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `status[string]`: 交通事故の状況。Enum:'archived, onGoing, solved' （アーカイブ、進行中、解決済  . Model: [https://schema.org/Text](https://schema.org/Text)- `totalDeadPeopleWithin24Hours[integer]`: 事故による直接死者数  . Model: [https://schema.org/Number](https://schema.org/Number)- `totalDeadPeopleWithin30Days[integer]`: 事故の余波による死者数  . Model: [https://schema.org/Number](https://schema.org/Number)- `totalInjured[integer]`: じこけんじゅつしゃすう  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: NGSI Entity タイプ。RoadAccident である必要があります。  - `vehiclesInvolved[array]`: 事故車両（および歩行者）のリスト 0 ：歩行者 1 ：自転車 2 ：農業用車両 3 ：バス 4 ：ミニバス 5 ：自動車 6 ：キャラバン 7 ：路面電車 8 ：タンカー 9 ：キャラバン付き自動車 10 ：トレーラー付き自動車 11 :ローリー 12 ：原付 13 ：タンカー 14 ：オートバイ 15 ：オートバイWithSideCar 16 ：モータースクーター 17 ：トレーラー 18 ：バン 19 ：キャラバン 20 ：建設・整備車両 21 ：トロリー 22 ：ビントロリー 23 ：掃除機 24 ：清掃用トロリー  - `weakestSubject[string]`: 0 : 歩行者 1 : 自転車 2 : 農業用車両 3 : バス 5 : 自動車 7 : 路面電車 8 : タンクローリー 9 : キャラバン付き自動車 10 : タンクローリー 9 : 歩行者0 : 歩行者 1 : 自転車 2 : 農業用車両 3 : バス 4 : ミニバス 5 : 自動車 6 : キャラバン 7 : 路面電車 8 : タンカー 9 : carWithCaravan 10 : carWithTrailer 11 : トラック 12 : 原付 13 : タンカー 14 : バイク 15 : motorcycleWithSideCar 16 : モータースクーター 17 : トレーラー 18 : バン 19 : キャラバン 20 : 建設またはメンテナンス車両 21 : トロリー 22 : ビントロリー 23 : 掃き掃除機械 24 : 清掃トロリー  - `weatherConditions[array]`: この交通事故の際の天候の簡単な説明。0 : 晴れ1 : 晴れ2 : やや曇り3 : 曇り4 : 霧5 : 霧6 : 高曇り7 : 曇り8 : 非常に曇り9 : 曇り10 : 小雨11 : 霧12 : 小雨13 :heavyRainShower 14 : heavyRain 15 : sleetShower 16 : sleet 17 : hailShower 18 : hail 19 : shower 20 : lightSnow 21 : snow 22 : heavySnowShower 23 : heavySnow 24 : thunderShower 25 : thunder  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必要なプロパティ  
- `id`  - `status`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
シンクロニシティプロジェクトから生まれたデータモデル  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順に並びます（クリックで詳細へ）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
RoadAccident:    
  description: 'A road accident description with causes and aftermath. First version developed in Synchronicity project'    
  properties:    
    accidentDate:    
      description: 'Datetime of the accident'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    accidentDescription:    
      description: 'Description about this Road Accident as a combination of codified situation enlisted. 0: Unspecified circumstance; 1: Driver proceeded regularly without turning; 2: Driver proceeded with a distracted driving or undecided course; 3: Driver proceeded without maintaining a safe distance; 4: Driver proceeded without giving priority to the vehicle coming from the right; 5: Driver proceeded without respecting the stop; 6: Driver proceeded without respecting the signal to give precedence; 7: Driver proceeded against traffic; 8: Driver proceeded without respecting the traffic light or agent signals; 10: Driver proceeded without respecting the signs of prohibition of transit or access; 11: Driver proceeded with speeding; 12: Driver proceeded without respecting the speed limits; 13: Driver proceeded with the dazzling lights crossing other vehicles; 14: Driver turned right regularly; 15: It turned irregularly to the right; 16: Driver turned left regularly; 17: It turned irregularly to the left; 18: Driver passed at the intersection; 20: Driver proceeded regularly; 21: Driver proceeded with a distracted driving or undecided course; 22: Driver proceeded without maintaining a safe distance; 23: Driver proceeded with speeding; 24: Driver proceeded without respecting the speed limits; 25: It proceeded not near the right edge of the roadway; 26: Driver proceeded against traffic; 27: Driver proceeded without respecting the signs of prohibition of transit or access; 28: Driver proceeded with the dazzling lights crossing other vehicles; 29: Driver passed regularly; 30: It passed irregularly to the right; 31: Driver overtook on a curve, on a hill or with insufficient visibility; 32: It overtook a vehicle that was overtaking another; 33: Driver passed without observing the appropriate prohibition sign; 34: Maneuvered in relegation or conversion; 35: Driver maneuvered to get into the flow of circulation; 36: Maneuvering To turn left (private passage, distributor); 37: Driver maneuvered regularly to stop or stop; 38: Driver maneuvered irregularly to stop or stop; 39: It was joined by other irregular two-wheeled vehicles; 40: Driver proceeded regularly; 41: Driver proceeded with speeding; 42: Driver proceeded without respecting the speed limits; 43: Driver proceeded against traffic; 44: Driver passed the vehicle in gear; 45: Maneuvered; 46: Maneuvered without respecting traffic light or agent signals; 47: Driver came out of the driveway without precaution; 48: Driver stepped out of the lane and hit the pawn; 49: It did not give priority to the pedestrian on the appropriate crossings; 50: It overtook a vehicle stopped to allow the crossing; 51: Driver hit the pedestrian with the load; 52: Driver was passing a tram unevenly at the stop; 60: Driver proceeded regularly; 61: Driver proceeded with a distracted driving or undecided course; 62: Driver proceeded without maintaining a safe distance; 63: Driver proceeded against traffic; 64: Driver proceeded with speeding; 65: Driver proceeded without respecting the speed limits; 66: Driver proceeded without respecting the signs of prohibition of transit or access; 67: Driver was passing another vehicle in gear; 68: Driver imprudently crossed the level crossing; 70: Spill with spillage to avoid impact; 71: Listening with spillage for distracted driving; 72: List with over-speed spill; 73: Driver suddenly braked with consequence to the transported; 74: Fall of person from vehicle for: door opening; 75: Fall of person from vehicle for: descent from vehicle in motion; 76: Fall of person from vehicle due to: clinging or improperly placed; 80: Brake failure or failure; 81: Breakage or steering failure; 82: Tire burst or excessive wear; 83: Lack or insufficiency of headlights or position lights; 84: Lack or insufficiency of flashing lights or stopping light signals; 85: Breaking of trailer coupling parts; 86: Deficiency of dangerous goods transport equipment; 87: Deficiency of the adaptations prescribed to vehicles of physically handicapped people; 88: Wheel detachment; 89: Lack or insufficiency    
        of visual devices for cycles'    
      items:    
        enum:    
          - 0    
          - 1    
          - 2    
          - 3    
          - 4    
          - 5    
          - 6    
          - 7    
          - 8    
          - 9    
          - 10    
          - 11    
          - 12    
          - 13    
          - 14    
          - 15    
          - 16    
          - 17    
          - 18    
          - 19    
          - 20    
          - 21    
          - 22    
          - 23    
          - 24    
          - 25    
          - 26    
          - 27    
          - 28    
          - 29    
          - 30    
          - 31    
          - 32    
          - 33    
          - 34    
          - 35    
          - 36    
          - 37    
          - 38    
          - 39    
          - 40    
          - 41    
          - 42    
          - 43    
          - 44    
          - 45    
          - 46    
          - 47    
          - 48    
          - 49    
          - 50    
          - 51    
          - 52    
          - 53    
          - 54    
          - 55    
          - 56    
          - 57    
          - 58    
          - 59    
          - 60    
          - 61    
          - 62    
          - 63    
          - 64    
          - 65    
          - 66    
          - 67    
          - 68    
          - 69    
          - 70    
          - 71    
          - 72    
          - 73    
          - 74    
          - 75    
          - 76    
          - 77    
          - 78    
          - 79    
          - 80    
          - 81    
          - 82    
          - 83    
          - 84    
          - 85    
          - 86    
          - 87    
          - 88    
          - 89    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    accidentLocation:    
      description: 'Brief description if the accident took place in a urban or extra-urban area. 0: Regional within the urban area 1: Urban road in the town 2: Provincial road within the town 3: State road within the village 4: Extra-urban road 5: Provincial 6: State road 7: Highway 8: Another way 9: Regional road'    
      enum:    
        - 0    
        - 1    
        - 2    
        - 3    
        - 4    
        - 5    
        - 6    
        - 7    
        - 8    
        - 9    
      type: string    
      x-ngsi:    
        type: Property    
    accidentStatisticalDate:    
      description: 'approximate datetime of the accident (often original accident data source reports only statistical attributes such as season, weekday and approximate hour'    
      properties:    
        hour:    
          type: integer    
        quarter:    
          type: integer    
        weekday:    
          description: 'Week days'    
          enum:    
            - Monday    
            - Tuesday    
            - Wednesday    
            - Thursday    
            - Friday    
            - Saturday    
            - Sunday    
          type: string    
        year:    
          type: integer    
      type: object    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    accidentType:    
      description: 'Quick classification this Road Accident. 1: Frontal collision; 2: Frontal-lateral collision; 3: Side crash; 4: Collision; 5: Pedestrian investment; 6: Impact with vehicle stopped or stopped; 7: Impact with parked vehicle; 8: Impact with obstacle; 9: Impact with train; 10: Spill, slip; 11: Accident due to sudden braking; 12: Accident due to falling from a vehicle;. '    
      items:    
        enum:    
          - 1    
          - 2    
          - 3    
          - 4    
          - 5    
          - 6    
          - 7    
          - 8    
          - 9    
          - 10    
          - 11    
          - 12    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
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
    id:    
      anyOf: &roadaccident_-_properties_-_owner_-_items_-_anyof    
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
    localId:    
      description: 'Unique identifier from the source data set'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
    numPassengersDead:    
      description: 'Number of vehicle''s passengers dead because the accident'    
      minimum: 0    
      type: integer    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    numPassengersInjured:    
      description: 'Number of vehicle''s passengers injured because the accident'    
      minimum: 0    
      type: integer    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    numPedestrianDead:    
      description: 'Number of pedestrians dead because the accident'    
      minimum: 0    
      type: integer    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    numPedestrianInjured:    
      description: 'Number of pedestrians injured because the accident'    
      minimum: 0    
      type: integer    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *roadaccident_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    pedestriansInvolved:    
      description: 'Boolean to determine if pedestrians were involved in the accidents'    
      type: boolean    
      x-ngsi:    
        type: Property    
    roadClass:    
      description: ' The classification of road where this accident took place'    
      type: string    
      x-ngsi:    
        model: https://wiki.openstreetmap.org/wiki/Key:highway    
        type: Property    
    roadIntersection:    
      description: 'Brief description of the piece of the road where the accident took place.   1: Crossroad; 2: Roundabout; 3: Reported intersection; 4: Intersection with traffic light; 5: Intersection not reported; 6: Rail crossing; 7: Straight; 8: Curve; 9: Bump, bottleneck; 10: Slope; 11: Illuminated gallery; 12: Unlit gallery;'    
      enum:    
        - 1    
        - 2    
        - 3    
        - 4    
        - 5    
        - 6    
        - 7    
        - 8    
        - 9    
        - 10    
        - 11    
        - 12    
      type: string    
      x-ngsi:    
        type: Property    
    roadPaving:    
      description: 'Road paving. 1: Paved road; 2: Rough paved road; 3: Unpaved road;'    
      enum:    
        - 1    
        - 2    
        - 3    
      type: string    
      x-ngsi:    
        type: Property    
    roadSign:    
      description: 'Brief description of the road sign where the accident took place. 1: Absent; 2: Vertical; 3: Horizontal; 4: Vertical and horizontal; 5: Temporary by construction site;'    
      enum:    
        - 1    
        - 2    
        - 3    
        - 4    
        - 5    
      type: string    
      x-ngsi:    
        type: Property    
    roadSurface:    
      description: 'Brief description of the condition of the road during the accident. 1: Dry; 2: Wet; 3: Slippery; 4: frozen; 5: Snowcapped;'    
      enum:    
        - 1    
        - 2    
        - 3    
        - 4    
        - 5    
      type: string    
      x-ngsi:    
        type: Property    
    roadTrunk:    
      description: 'Brief description of type of trunk of the road where the accident took place. 1: Road branch; 2: Secondary branch; 3: Minor branch; 4: Junction branch; 5: Road junction; 6: Motorway left lane; 7: Highway carriageway right; 8: Motorway junction entrance; 9: Highway exit junction; 10: Highway junction trunk; 11: Highway station; 12: Other cases; 15: Extra urban road.'    
      enum:    
        - 1    
        - 2    
        - 3    
        - 4    
        - 5    
        - 6    
        - 7    
        - 8    
        - 9    
        - 10    
        - 11    
        - 12    
        - 15    
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
    status:    
      description: 'Status of the Road Accident. Enum:''archived, onGoing, solved'''    
      enum:    
        - archived    
        - onGoing    
        - solved    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    totalDeadPeopleWithin24Hours:    
      description: 'Number of people dead directly because the accident'    
      minimum: 0    
      type: integer    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    totalDeadPeopleWithin30Days:    
      description: 'Number of people dead because the aftermath of the accident'    
      minimum: 0    
      type: integer    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    totalInjured:    
      description: 'total number of people injured (not dead) because the accident'    
      minimum: 0    
      type: integer    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: 'NGSI Entity type. it has to be RoadAccident'    
      enum:    
        - RoadAccident    
      type: string    
      x-ngsi:    
        type: Property    
    vehiclesInvolved:    
      description: 'List of the vehicles (and pedestrians) involved because the accident 0 : pedestrian 1 : bicycle 2 : agriculturalVehicle 3 : bus 4 : minibus 5 : car 6 : caravan 7 : tram 8 : tanker 9 : carWithCaravan 10 : carWithTrailer 11 : lorry 12 : moped 13 : tanker 14 : motorcycle 15 : motorcycleWithSideCar 16 : motorscooter 17 : trailer 18 : van 19 : caravan 20 : constructionOrMaintenanceVehicle 21 : trolley 22 : binTrolley 23 : sweepingMachine 24 : cleaningTrolley'    
      items:    
        enum:    
          - 0    
          - 1    
          - 2    
          - 3    
          - 4    
          - 5    
          - 6    
          - 7    
          - 8    
          - 9    
          - 10    
          - 11    
          - 12    
          - 13    
          - 14    
          - 15    
          - 16    
          - 17    
          - 18    
          - 19    
          - 20    
          - 21    
          - 22    
          - 23    
          - 24    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    weakestSubject:    
      description: 'vehicle that represent the weakest subject involved because the accident (usually pedestrian). 0 : pedestrian 1 : bicycle 2 : agriculturalVehicle 3 : bus 4 : minibus 5 : car 6 : caravan 7 : tram 8 : tanker 9 : carWithCaravan 10 : carWithTrailer 11 : lorry 12 : moped 13 : tanker 14 : motorcycle 15 : motorcycleWithSideCar 16 : motorscooter 17 : trailer 18 : van 19 : caravan 20 : constructionOrMaintenanceVehicle 21 : trolley 22 : binTrolley 23 : sweepingMachine 24 : cleaningTrolley'    
      enum:    
        - 0    
        - 1    
        - 2    
        - 3    
        - 4    
        - 5    
        - 6    
        - 7    
        - 8    
        - 9    
        - 10    
        - 11    
        - 12    
        - 13    
        - 14    
        - 15    
        - 16    
        - 17    
        - 18    
        - 19    
        - 20    
        - 21    
        - 22    
        - 23    
        - 24    
      type: string    
      x-ngsi:    
        type: Property    
    weatherConditions:    
      description: 'Brief description of weather conditions during this Road Accident. 0 : clearNight 1 : sunnyDay 2 : slightlyCloudy 3 : partlyCloudy 4 : mist 5 : fog 6 : highClouds 7 : cloudy 8 : veryCloudy 9 : overcast 10 : lightRainShower 11 : drizzle 12 : lightRain 13 : heavyRainShower 14 : heavyRain 15 : sleetShower 16 : sleet 17 : hailShower 18 : hail 19 : shower 20 : lightSnow 21 : snow 22 : heavySnowShower 23 : heavySnow 24 : thunderShower 25 : thunder'    
      items:    
        enum:    
          - 0    
          - 1    
          - 2    
          - 3    
          - 4    
          - 5    
          - 6    
          - 7    
          - 8    
          - 9    
          - 10    
          - 11    
          - 12    
          - 13    
          - 14    
          - 15    
          - 16    
          - 17    
          - 18    
          - 19    
          - 20    
          - 21    
          - 22    
          - 23    
          - 24    
          - 25    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - status    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Transportation/blob/master/RoadAccident/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Transportation/RoadAccident/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ペイロードの例  
#### RoadAccident NGSI-v2 key-value の例。  
ここでは、RoadAccidentをJSON-LD形式でkey-valuesにした例を示す。これは、`options=keyValues`を使用した場合にNGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:RoadAccident:id:ORHW:45620815",  
  "type": "RoadAccident",  
  "dateCreated": "2018-06-23T04:19:24Z",  
  "dateModified": "2020-10-29T08:36:40Z",  
  "source": "To be defined",  
  "name": "Name of the element of the accident.",  
  "alternateName": "Other name.",  
  "description": "Clash in the middle of a traffic light",  
  "dataProvider": "Municipality.",  
  "owner": [  
    "urn:ngsi-ld:RoadAccident:items:SUUU:18395806",  
    "urn:ngsi-ld:RoadAccident:items:GVOF:30958855"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:RoadAccident:items:ESLS:37894243",  
    "urn:ngsi-ld:RoadAccident:items:ZNUH:87936284"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -56.6404505,  
      168.370658  
    ]  
  },  
  "address": {  
    "streetAddress": "FranklinStrasse",  
    "addressLocality": "Berlin",  
    "addressRegion": "Berlin",  
    "addressCountry": "Germany",  
    "postalCode": "10387",  
    "postOfficeBoxNumber": "",  
    "areaServed": "worldwide."  
  },  
  "areaServed": "worldwide",  
  "localId": "20210312-A1.",  
  "status": "onGoing",  
  "accidentDate": "2021-03-12T13:59:36Z",  
  "accidentStatisticalDate": {  
    "year": 2021,  
    "quarter": 1,  
    "weekday": "Friday",  
    "hour": 4  
  },  
  "accidentType": [  
    "10",  
    "6"  
  ],  
  "accidentDescription": [  
    "23",  
    "46"  
  ],  
  "weatherConditions": [  
    "10",  
    "20"  
  ],  
  "roadSurface": "2",  
  "roadPaving": "2",  
  "accidentLocation": "5",  
  "roadClass": "Motorway.",  
  "roadIntersection": "8",  
  "roadTrunk": "12",  
  "roadSign": "5",  
  "pedestriansInvolved":  
    true  
  ,  
  "vehiclesInvolved": [  
    "21",  
    "6"  
  ],  
  "weakestSubject": "20",  
  "numPassengersInjured": 1,  
  "numPassengersDead": 1,  
  "numPedestrianInjured": 1,  
  "numPedestrianDead": 0,  
  "totalInjured": 2,  
  "totalDeadPeopleWithin30Days": 0,  
  "totalDeadPeopleWithin24Hours": 0  
}  
```  
</details>  
#### RoadAccident NGSI-v2 正規化例  
以下は、RoadAccident を JSON-LD 形式で正規化した例である。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:RoadAccident:id:ORHW:45620815",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2018-06-23T04:19:24Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2020-10-29T08:36:40Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "To be defined"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Name of the element of the accident."  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Other name."  
  },  
  "description": {  
    "type": "Property",  
    "value": "Clash in the middle of a traffic light"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Municipality."  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:RoadAccident:items:SUUU:18395806",  
      "urn:ngsi-ld:RoadAccident:items:GVOF:30958855"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:RoadAccident:items:ESLS:37894243",  
      "urn:ngsi-ld:RoadAccident:items:ZNUH:87936284"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -56.6404505,  
        168.370658  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "FranklinStrasse",  
      "addressLocality": "Berlin",  
      "addressRegion": "Berlin",  
      "addressCountry": "Germany",  
      "postalCode": "10387",  
      "postOfficeBoxNumber": "",  
      "areaServed": "worldwide."  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "worldwide"  
  },  
  "type": "RoadAccident",  
  "localId": {  
    "type": "Property",  
    "value": "20210312-A1."  
  },  
  "status": {  
    "type": "Property",  
    "value": "onGoing"  
  },  
  "accidentDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2021-03-12T13:59:36Z"  
    }  
  },  
  "accidentStatisticalDate": {  
    "type": "Property",  
    "value": {  
      "year": 2021,  
      "quarter": 1,  
      "weekday": "Friday",  
      "hour": 4  
    }  
  },  
  "accidentType": {  
    "type": "Property",  
    "value": [  
      "10",  
      "6"  
    ]  
  },  
  "accidentDescription": {  
    "type": "Property",  
    "value": [  
      "23",  
      "46"  
    ]  
  },  
  "weatherConditions": {  
    "type": "Property",  
    "value": [  
      "10",  
      "20"  
    ]  
  },  
  "roadSurface": {  
    "type": "Property",  
    "value": "2"  
  },  
  "roadPaving": {  
    "type": "Property",  
    "value": "2"  
  },  
  "accidentLocation": {  
    "type": "Property",  
    "value": "5"  
  },  
  "roadClass": {  
    "type": "Property",  
    "value": "Motorway."  
  },  
  "roadIntersection": {  
    "type": "Property",  
    "value": "8"  
  },  
  "roadTrunk": {  
    "type": "Property",  
    "value": "12"  
  },  
  "roadSign": {  
    "type": "Property",  
    "value": "5"  
  },  
  "pedestriansInvolved": {  
    "type": "Property",  
    "value": [  
      "true"  
    ]  
  },  
  "vehiclesInvolved": {  
    "type": "Property",  
    "value": [  
      "21",  
      "6"  
    ]  
  },  
  "weakestSubject": {  
    "type": "Property",  
    "value": "20"  
  },  
  "numPassengersInjured": {  
    "type": "Property",  
    "value": 1  
  },  
  "numPassengersDead": {  
    "type": "Property",  
    "value": 1  
  },  
  "numPedestrianInjured": {  
    "type": "Property",  
    "value": 1  
  },  
  "numPedestrianDead": {  
    "type": "Property",  
    "value": 0  
  },  
  "totalInjured": {  
    "type": "Property",  
    "value": 2  
  },  
  "totalDeadPeopleWithin30Days": {  
    "type": "Property",  
    "value": 0  
  },  
  "totalDeadPeopleWithin24Hours": {  
    "type": "Property",  
    "value": 0  
  }  
}  
```  
</details>  
#### RoadAccident NGSI-LD キー値例  
RoadAccidentをJSON-LD形式でkey-valuesにした例です。これは、`options=keyValues`を使用した場合にNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:RoadAccident:id:ORHW:45620815",  
    "type": "RoadAccident",  
    "accidentDate": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2021-03-12T13:59:36Z"  
        }  
    },  
    "accidentDescription": {  
        "type": "Property",  
        "value": [  
            "23",  
            "46"  
        ]  
    },  
    "accidentLocation": {  
        "type": "Property",  
        "value": "5"  
    },  
    "accidentStatisticalDate": {  
        "type": "Property",  
        "value": {  
            "year": 2021,  
            "quarter": 1,  
            "weekday": "Friday",  
            "hour": 4  
        }  
    },  
    "accidentType": {  
        "type": "Property",  
        "value": [  
            "10",  
            "6"  
        ]  
    },  
    "address": {  
        "type": "Property",  
        "value": {  
            "streetAddress": "FranklinStrasse",  
            "addressLocality": "Berlin",  
            "addressRegion": "Berlin",  
            "addressCountry": "Germany",  
            "postalCode": "10387",  
            "postOfficeBoxNumber": "",  
            "areaServed": "worldwide."  
        }  
    },  
    "alternateName": {  
        "type": "Property",  
        "value": "Other name."  
    },  
    "areaServed": {  
        "type": "Property",  
        "value": "worldwide"  
    },  
    "dataProvider": {  
        "type": "Property",  
        "value": "Municipality."  
    },  
    "dateCreated": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2018-06-23T04:19:24Z"  
        }  
    },  
    "dateModified": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2020-10-29T08:36:40Z"  
        }  
    },  
    "description": {  
        "type": "Property",  
        "value": "Clash in the middle of a traffic light"  
    },  
    "localId": {  
        "type": "Property",  
        "value": "20210312-A1."  
    },  
    "location": {  
        "type": "Property",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                -56.6404505,  
                168.370658  
            ]  
        }  
    },  
    "name": {  
        "type": "Property",  
        "value": "Name of the element of the accident."  
    },  
    "numPassengersDead": {  
        "type": "Property",  
        "value": 1  
    },  
    "numPassengersInjured": {  
        "type": "Property",  
        "value": 1  
    },  
    "numPedestrianDead": {  
        "type": "Property",  
        "value": 0  
    },  
    "numPedestrianInjured": {  
        "type": "Property",  
        "value": 1  
    },  
    "owner": {  
        "type": "Property",  
        "value": [  
            "urn:ngsi-ld:RoadAccident:items:SUUU:18395806",  
            "urn:ngsi-ld:RoadAccident:items:GVOF:30958855"  
        ]  
    },  
    "pedestriansInvolved": {  
        "type": "Property",  
        "value": [  
            "true"  
        ]  
    },  
    "roadClass": {  
        "type": "Property",  
        "value": "Motorway."  
    },  
    "roadIntersection": {  
        "type": "Property",  
        "value": "8"  
    },  
    "roadPaving": {  
        "type": "Property",  
        "value": "2"  
    },  
    "roadSign": {  
        "type": "Property",  
        "value": "5"  
    },  
    "roadSurface": {  
        "type": "Property",  
        "value": "2"  
    },  
    "roadTrunk": {  
        "type": "Property",  
        "value": "12"  
    },  
    "seeAlso": {  
        "type": "Property",  
        "value": [  
            "urn:ngsi-ld:RoadAccident:items:ESLS:37894243",  
            "urn:ngsi-ld:RoadAccident:items:ZNUH:87936284"  
        ]  
    },  
    "source": {  
        "type": "Property",  
        "value": "To be defined"  
    },  
    "status": {  
        "type": "Property",  
        "value": "onGoing"  
    },  
    "totalDeadPeopleWithin24Hours": {  
        "type": "Property",  
        "value": 0  
    },  
    "totalDeadPeopleWithin30Days": {  
        "type": "Property",  
        "value": 0  
    },  
    "totalInjured": {  
        "type": "Property",  
        "value": 2  
    },  
    "vehiclesInvolved": {  
        "type": "Property",  
        "value": [  
            "21",  
            "6"  
        ]  
    },  
    "weakestSubject": {  
        "type": "Property",  
        "value": "20"  
    },  
    "weatherConditions": {  
        "type": "Property",  
        "value": [  
            "10",  
            "20"  
        ]  
    },  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Transportation/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### RoadAccident NGSI-LD 正規化例  
以下は、RoadAccidentをJSON-LD形式で正規化した例である。これはオプションを使用しない場合、NGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:RoadAccident:id:ORHW:45620815",  
    "type": "RoadAccident",  
    "accidentDate": "2021-03-12T13:59:36Z",  
    "accidentDescription": [  
        "23",  
        "46"  
    ],  
    "accidentLocation": "5",  
    "accidentStatisticalDate": {  
        "year": 2021,  
        "quarter": 1,  
        "weekday": "Friday",  
        "hour": 4  
    },  
    "accidentType": [  
        "10",  
        "6"  
    ],  
    "address": {  
        "streetAddress": "FranklinStrasse",  
        "addressLocality": "Berlin",  
        "addressRegion": "Berlin",  
        "addressCountry": "Germany",  
        "postalCode": "10387",  
        "postOfficeBoxNumber": "",  
        "areaServed": "worldwide."  
    },  
    "alternateName": "Other name.",  
    "areaServed": "worldwide",  
    "dataProvider": "Municipality.",  
    "dateCreated": "2018-06-23T04:19:24Z",  
    "dateModified": "2020-10-29T08:36:40Z",  
    "description": "Clash in the middle of a traffic light",  
    "localId": "20210312-A1.",  
    "location": {  
        "type": "Point",  
        "coordinates": [  
            -56.6404505,  
            168.370658  
        ]  
    },  
    "name": "Name of the element of the accident.",  
    "numPassengersDead": 1,  
    "numPassengersInjured": 1,  
    "numPedestrianDead": 0,  
    "numPedestrianInjured": 1,  
    "owner": [  
        "urn:ngsi-ld:RoadAccident:items:SUUU:18395806",  
        "urn:ngsi-ld:RoadAccident:items:GVOF:30958855"  
    ],  
    "pedestriansInvolved": [  
        "true"  
    ],  
    "roadClass": "Motorway.",  
    "roadIntersection": "8",  
    "roadPaving": "2",  
    "roadSign": "5",  
    "roadSurface": "2",  
    "roadTrunk": "12",  
    "seeAlso": [  
        "urn:ngsi-ld:RoadAccident:items:ESLS:37894243",  
        "urn:ngsi-ld:RoadAccident:items:ZNUH:87936284"  
    ],  
    "source": "To be defined",  
    "status": "onGoing",  
    "totalDeadPeopleWithin24Hours": 0,  
    "totalDeadPeopleWithin30Days": 0,  
    "totalInjured": 2,  
    "vehiclesInvolved": [  
        "21",  
        "6"  
    ],  
    "weakestSubject": "20",  
    "weatherConditions": [  
        "10",  
        "20"  
    ],  
    "@context": [  
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
