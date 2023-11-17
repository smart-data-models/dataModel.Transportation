<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
实体：APDSObservation    
==================<!-- /10-Header -->    
<!-- 15-License -->    
[开放许可](https://github.com/smart-data-models//dataModel.Transportation/blob/master/APDSObservation/LICENSE.md)    
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
全局描述：**该实体模拟对一组 ANPR 摄像机的特定观察。观察可能会使用多个 ANPR 摄像机进行，但仅限于观察一辆车。它实现了 APDS 数据模型 https://www.allianceforparkingdatastandards.org/**    
版本： 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## 属性列表    
<sup><sub>[*] 如果属性中没有类型，是因为它可能有多个类型或不同的格式/模式</sub></sup>。    
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国家。例如，西班牙  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: 街道地址所在的地点，以及该地点所在的区域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: 地点所在的地区，以及该地区位于哪个国家  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: 地区是一种行政区划，在一些国家由地方政府管理      
	- `postOfficeBoxNumber[string]`: 用于邮政信箱地址的邮政信箱号码。例如：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: 邮政编码。例如：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: 街道地址  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
	- `streetNr[string]`: 在公共街道上标识特定房产的编号      
- `alternateName[string]`: 该项目的替代名称  - `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `creator[string]`: 当前驱动程序的 ID。  - `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `description[string]`: 项目描述  - `id[*]`: 实体的唯一标识符  - `images[array]`: 图片链接数组。数组元素包含图片的 URL 和其他信息。作为图像 URL 的替代，图像本身也可以包含在二进制内容属性中。  - `location[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `name[string]`: 该项目的名称  - `observationDateTime[date-time]`: 观测的时间戳（UTC）。如果未使用 observationStartDateTime 和 observationEndDateTime，则必须使用。  - `observationEndDateTime[date-time]`: 观察事件结束的日期和时间（UTC 时）（例如，观察到一辆汽车于上午 9:33 离开交货区）。如果未使用创建日期时间，则必须填写。  - `observationStartDateTime[date-time]`: 观察事件开始的日期和时间（UTC 内）（例如，观察到一辆汽车在上午 8:01 进入交货区）。如果未使用创建日期时间，则为必填项。  - `observedCredentialCharacterConfidence[array]`: 单个字符识别的可信度。与 observedCredentialConfidence 一样，这是针对特定供应商的。请使用元数据说明如何解释置信度。  - `observedCredentialConfidence[number]`: 测量的总体置信度。可以根据供应商的具体情况而定，但应始终在 0 至 1 之间进行调整。Arvoo：范围[0.0, 1.0]（越高越好）。  - `observedCredentialCountry[string]`: 国家代码采用 2 个字符的 ISO3166 标准 (https://www.iban.com/country-codes)。请注意，为避免歧义，不应使用国际车辆登记代码 (https://en.wikipedia.org/wiki/International_vehicle_registration_code)。如果无法确定国家代码，则将该属性设置为 "XX"。  - `observedCredentialId[string]`: 参考观察凭证的特定标识符。凭证由 observedCredentialType 指定，可以是 RFID 标签、支付站的票号、车牌号等。如果是车牌号，则只允许使用字母数值（不得使用空格或连字符）。可选择使用": "来表示德国城市印章 (https://www.europeanplates.com/information/german-city-codes.html) 等的位置。  - `observedCredentialType[string]`: 观察结果中引用的凭证类型。允许的值在 APDS CredentialType 中指定。枚举:'条形码, 蓝牙, 电子票证, 吊牌, 牌照, 许可证, qrCode, rfid, 门票, 其他'  - `observedHeading[*]`: 表示观察者的行进方向，以十进制度表示，其中 0 <= 'heading' < 360，相对于真正的北方顺时针计数。(联合国代码 DD）  . Model: [https://schema.org/Number](https://schema.org/Number)- `observedLocation`:   	- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)    
	- `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `location[*]`: 项目的 Geojson 引用。可以是点、线条字符串、多边形、多点、多线条字符串或多多边形      
- `observedLocationPDOP[number]`: 观测车辆 GPS 位置的精度。用 "Position Dilution Of Precision "表示（https：//en.wikipedia.org/wiki/Dilution_of_precision_(navigation)）。(联合国代码'MTR'）。  - `observedMethod[string]`: 由 APDS（ObservationType）定义的该观测要素的观测方法。枚举：'anpr、粉笔、视觉、扫描仪、rfTranspoder、其他  - `observedSpeed[*]`: 表示观测到的车辆当前速度水平分量的大小，单位为公里/小时。如果提供，速度属性值必须是非负实数。如果由于某种原因速度暂时未知，可以使用'-1'。(联合国代码 KMH）。  . Model: [https://schema.org/Number](https://schema.org/Number)- `observedVehicleColour[string]`: 被观测车辆的颜色  - `observedVehicleMake[string]`: 被观察车辆的品牌  - `observedVehicleType[string]`: 从结构特征的角度来看的车辆类型。这与车辆类别不同。枚举'农用车、任何车辆、铰接式车辆、自行车、垃圾车、公共汽车、轿车、大篷车、轻型车、带大篷车的车、带拖车的车、清洁车、建筑或维护车辆、四轮驱动、高边车、货车、小客车、轻便摩托车、摩托车、摩托车、带侧车的摩托车、摩托艇、扫地机、油罐车、三轮汽车、拖车、电车、两轮汽车、手推车、面包车、无催化转换器的车辆、带大篷车的车辆、带拖车的车辆、带偶数登记牌照的车辆、带奇数登记牌照的车辆、其他"。下列由 _VehicleTypeEnum_ 和 _VehicleTypeEnum2_, [DATEX 2 版本 2.3](http://d2docs.ndwcloud.nu/_static/umlmodel/v2.3/index.htm) 定义并扩展用于其他用途的值  . Model: [https://schema.org/Text](https://schema.org/Text)- `observer[string]`: 在此观察要素中记录的进行观察的扫描系统的名称或标识。  - `observerCameras[array]`: 检测到车辆的摄像头位置阵列。列表中第一个摄像头的识别率最高。使用以下缩写表示汽车上的摄像头位置：RF（右前）、RM（右中）、RB（右后）、LF（左前）、LM（左中）、LB（左后）。  - `observerDescription[string]`: 自由文本描述，用于描述观察点或观察者的详细信息。例如，可用作特定 ANPR 扫描车的友好名称。  - `observerHeading[*]`: 表示观察者的行进方向，以十进制度表示，其中 0 <= 'heading' < 360，相对于真正的北方顺时针计数。如果车辆静止不动（即 "速度 "属性值为 "0"），则航向属性值必须等于"-1"。  . Model: [https://schema.org/Number](https://schema.org/Number)- `observerLocation`:   	- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)    
	- `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `location[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形      
- `observerLocationPDOP[number]`: 观测者的 GPS 定位精度，用 "精度位置稀释 "表示(https: //en.wikipedia.org/wiki/Dilution_of_precision_(navigation))  - `observerSpeed[*]`: 表示观测器当前速度水平分量的大小，单位为公里/小时。如果提供，速度属性值必须是非负实数。如果由于某种原因速度暂时未知，可以使用'-1'。  . Model: [https://schema.org/Number](https://schema.org/Number)- `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `towardsObserver[number]`: 1： 观察到的车辆朝摄像机方向移动，0： 观察到的车辆朝摄像机方向移动，-1：-1： 未检测到观察到的车辆方向。  - `type[string]`: NGSI 实体类型。必须是 APDSObservation  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
所需属性    
- `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
该模型捕捉特定时间、特定地点的车辆观测数据集。它源自 APDS（停车场数据标准联盟）规范。观察方法包括使用 ALPR 摄像机、目视观察、扫描仪或任何其他观察手段。    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## 属性的数据模型描述    
按字母顺序排列（点击查看详情）    
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
## 有效载荷示例    
#### APDSObservation NGSI-v2 密钥值示例    
下面是一个以 JSON-LD 格式作为键值的 APDSObservation 的示例。当使用 `options=keyValues` 时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
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
    0.95,  
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
#### APDSObservation NGSI-v2 标准化示例    
下面是一个规范化 JSON-LD 格式 APDSObservation 的示例。当不使用选项时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
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
#### APDSObservation NGSI-LD 键值示例    
下面是一个以 JSON-LD 格式作为键值的 APDSObservation 的示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
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
    0.95,  
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
  "observerSpeed": 26,  
  "@context": [  
    "https://raw.githubusercontent.com/dataModel.Transportation/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### APDSObservation NGSI-LD normalized 示例    
下面是一个规范化 JSON-LD 格式 APDSObservation 的示例。当不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
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
请参阅 [FAQ 10](https://smartdatamodels.org/index.php/faqs/)，获取如何处理幅度单位的答案。    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
