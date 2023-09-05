<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：EVC 充电站  
==========<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.Transportation/blob/master/EVChargingStation/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全球描述**电动汽车充电站**  
版本： 0.1.0  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 属性列表  

<sup><sub>[*] 如果属性中没有类型，是因为它可能有多个类型或不同的格式/模式</sub></sup>。  
- `acceptedPaymentMethod[array]`: 使用该站点时的收费类型。枚举:'ByBankTransferInAdvance, ByInvoice, Cash, CheckInAdvance, COD, DirectDebit, GoogleCheckout, PayPal, PaySwarm'.  . Model: [https://schema.org/Text](https://schema.org/Text)- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国家。例如，西班牙  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 街道地址所在的地点，以及该地点所在的区域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 地点所在的地区，以及该地区位于哪个国家  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 地区是一种行政区划，在一些国家由地方政府管理    
	- `postOfficeBoxNumber[string]`: 用于邮政信箱地址的邮政信箱号码。例如：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 邮政编码。例如：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 街道地址  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
- `allowedVehicleType[array]`: 可收费的车辆类型。枚举：'自行车、公共汽车、汽车、大篷车、摩托车、摩托车、卡车'。  . Model: [http://schema.org/Text](http://schema.org/Text)- `alternateName[string]`: 该项目的替代名称  - `amountCollected[number]`: 为与该观察结果相对应的服务收取的金额  - `amperage[number]`: 充电站提供的总安培数。  . Model: [http://schema.org/Number](http://schema.org/Number)- `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `availableCapacity[number]`: 目前可以充电的车辆数量。必须小于或等于 "容量  . Model: [http://schema.org/Number](http://schema.org/Number)- `capacity[number]`: 可同时充电的车辆总数。插座总数可以更高。  . Model: [http://schema.org/Number](http://schema.org/Number)- `chargeType[array]`: 使用该台站时的收费类型。枚举:'年付、统一、免费、月付、其他'。  . Model: [https://schema.org/Text](https://schema.org/Text)- `chargingUnitId[string]`: 与该观察结果相对应的电动汽车充电站充电点的 ID  - `contactPoint[object]`: 与物品联系的详细信息  . Model: [https://schema.org/ContactPoint](https://schema.org/ContactPoint)	- `areaServed[string]`: 提供服务或所提供项目的地理区域。取代服务区域    
	- `availabilityRestriction[*]`: 该属性将一个联络点与该联络点不在时的信息联系起来。详细信息通过 "开放时间规范 "类提供  . Model: [http://schema.org/hoursAvailable](http://schema.org/hoursAvailable)  
	- `availableLanguage[*]`: 某人在使用物品、服务或场所时可能使用的语言。请使用 IETF BCP 47 标准中的一种语言代码。可使用 "文本 "选项，但也可以使用 "语言 "选项。  . Model: [http://schema.org/availableLanguage](http://schema.org/availableLanguage)  
	- `contactOption[*]`: 该联络点的可用选项（如免费电话号码或对听力受损来电者的支持）  . Model: [http://schema.org/contactOption](http://schema.org/contactOption)  
	- `contactType[string]`: 此项目的联系类型    
	- `email[idn-email]`: 所有者的电子邮件地址    
	- `faxNumber[string]`: 传真号码  . Model: [http://schema.org/Text](http://schema.org/Text)  
	- `name[string]`: 该项目的名称    
	- `productSupported[string]`: 该支持联络点所涉及的产品或服务（如特定产品系列的产品支持）。可以是特定产品或产品系列（如 "iPhone"），也可以是产品或服务的一般类别（如 "智能手机）  . Model: [http://schema.org/Text](http://schema.org/Text)  
	- `telephone[string]`: 联系人电话    
- `dataDescriptor[uri]`: 指向数据描述符实体的 URI  - `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `description[string]`: 项目描述  - `endDateTime[date-time]`: 与该观测结果相对应的报告结束时间  - `id[*]`: 实体的唯一标识符  - `location[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `name[string]`: 该项目的名称  - `network[string]`: 与运营商合作的网络名称。  . Model: [https://schema.org/Text](https://schema.org/Text)- `observationDateTime[date-time]`: 最后报告的观察时间  - `openingHours[string]`: 充电站的开放时间。  . Model: [http://schema.org/openingHours](http://schema.org/openingHours)- `operator[string]`: 充电站运营商。  . Model: [https://schema.org/Text](https://schema.org/Text)- `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `powerConsumption[number]`: 该观测值对应的实体消耗的电量  - `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `socketNumber[number]`: 该充电站提供的插座总数  . Model: [http://schema.org/Number](http://schema.org/Number)- `socketType[array]`: 该站提供的插座类型。枚举:'Caravan_Mains_Socket、CHAdeMO、CCS/SAE、Dual_CHAdeMO、Dual_J-1772、Dual_Mennekes、J-1772、Mennekes、Other、Tesla、Type2、Type3、Wall_Euro'。  . Model: [http://schema.org/Text](http://schema.org/Text)- `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `startDateTime[date-time]`: 与该观测结果相对应的报告开始时间  - `stationName[string]`: 与该观测点相对应的站点名称。可以是自行车停靠站、充电站等名称  - `status[string]`: 充电站的状态。枚举："几乎空、几乎满、空、满、停用、有故障、工作"。或任何其他特定于应用程序的  . Model: [http://schema.org/Text](http://schema.org/Text)- `taxAmountCollected[number]`: 对产品、物品和服务征收的税额，包括销售税、增值税、服务税、货物与服务税、关税等。  - `transactionId[string]`: 与该观察结果相对应的实体的唯一交易 ID  - `transactionType[string]`: 根据该观察结果对应的支付方式（如手机/银联卡、银行卡等）或服务方式（如发行、再发行、输入、输出等）确定的交易类型  - `type[string]`: NGSI 实体类型。必须是 EVChargingStation  - `vehicleType[string]`: 从结构特征的角度来看的车辆类型。这与车辆类别不同。枚举农用车、救护车、任何车辆、铰接式车辆、自动人力车、自行车、垃圾车、快速公交巴士、快速公交小巴、公交车、汽车、房车、轻型车、带房车的车、带拖车的车、清洁车、压实机、建筑或维护车辆、翻斗车、电动轻便摩托车、电动摩托车、电动摩托车、消防车、四轮驱动车、高边车、料斗、货车、小客车、轻便摩托车、摩托车、带侧车的摩托车、电动摩托车、警车、扫地机、油罐车、tempo、三轮汽车、自卸车、拖车、电车、两轮汽车、手推车、面包车、无催化转换器的车辆、带大篷车的车辆、带拖车的车辆、带偶数登记牌照的车辆、带奇数登记牌照的车辆、其他"。下列由 _VehicleTypeEnum_ 和 _VehicleTypeEnum2_ 定义的值[DATEX 2 2.3 版](http://d2docs.ndwcloud.nu/_static/umlmodel/v2.3/index.htm)  . Model: [https://schema.org/Text](https://schema.org/Text)- `voltage[number]`: 充电站提供的总电压  . Model: [http://schema.org/Number](http://schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `allowedVehicleType`  - `capacity`  - `id`  - `socketType`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
为电动汽车供电的公共充电站。充电时间取决于充电站的最大功率输出、正在充电的车辆数量以及当前的电池电量。  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 属性的数据模型描述  
按字母顺序排列（点击查看详情）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
EVChargingStation:    
  description: EV Charging Station    
  properties:    
    acceptedPaymentMethod:    
      description: 'Type(s) of charge when using this station. Enum:''ByBankTransferInAdvance, ByInvoice, Cash, CheckInAdvance, COD, DirectDebit, GoogleCheckout, PayPal, PaySwarm'''    
      items:    
        enum:    
          - ByBankTransferInAdvance    
          - ByInvoice    
          - Cash    
          - CheckInAdvance    
          - COD    
          - DirectDebit    
          - GoogleCheckout    
          - PayPal    
          - PaySwarm    
        type: string    
      minItems: 1    
      type: array    
      uniqueItems: true    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
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
    allowedVehicleType:    
      description: 'Vehicle type(s) which can be charged. Enum:''bicycle, bus, car, caravan, motorcycle, motorscooter, truck'' '    
      items:    
        enum:    
          - bicycle    
          - bus    
          - car    
          - caravan    
          - motorcycle    
          - motorscooter    
          - truck    
        type: string    
      minItems: 1    
      type: array    
      uniqueItems: true    
      x-ngsi:    
        model: http://schema.org/Text    
        type: Property    
    alternateName:    
      description: An alternative name for this item    
      type: string    
      x-ngsi:    
        type: Property    
    amountCollected:    
      description: Amount collected towards the service corresponding to this observation    
      type: number    
      x-ngsi:    
        type: Property    
    amperage:    
      description: The total amperage offered by the charging station.    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: Ampers (A)    
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    availableCapacity:    
      description: The number of vehicles which currently can be charged. It must lower or equal than `capacity`    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    capacity:    
      description: 'The total number of vehicles which can be charged at the same time. The total number of sockets can be higher. '    
      minimum: 1    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    chargeType:    
      description: 'Type(s) of charge when using this station. Enum:''annualPayment, flat, free, monthlyPayment, other'''    
      items:    
        enum:    
          - annualPayment    
          - flat    
          - free    
          - monthlyPayment    
          - other    
        type: string    
      minItems: 1    
      type: array    
      uniqueItems: true    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    chargingUnitId:    
      description: The Id of the charging point in the EV charging station corresponding to this observation    
      type: string    
      x-ngsi:    
        type: Property    
    contactPoint:    
      description: The details to contact with the item    
      properties:    
        areaServed:    
          description: The geographic area where a service or offered item is provided. Supersedes serviceArea    
          type: string    
          x-ngsi:    
            type: Property    
        availabilityRestriction:    
          anyOf:    
            - description: Array of identifiers format of any NGSI entity    
              items:    
                maxLength: 256    
                minLength: 1    
                pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
                type: string    
              type: array    
              x-ngsi:    
                type: Property    
            - description: Array of identifiers format of any NGSI entity    
              items:    
                format: uri    
                type: string    
              type: array    
              x-ngsi:    
                type: Property    
          description: This property links a contact point to information about when the contact point is not available. The details are provided using the Opening Hours Specification class    
          x-ngsi:    
            model: http://schema.org/hoursAvailable    
            type: Relationship    
        availableLanguage:    
          anyOf:    
            - anyOf:    
                - type: string    
                - items:    
                    type: string    
                  type: array    
          description: 'A language someone may use with or at the item, service or place. Please use one of the language codes from the IETF BCP 47 standard. It is implemented the Text option but it could be also Language'    
          x-ngsi:    
            model: http://schema.org/availableLanguage    
            type: Property    
        contactOption:    
          anyOf:    
            - type: string    
            - items:    
                type: string    
              type: array    
          description: An option available on this contact point (e.g. a toll-free number or support for hearing-impaired callers)    
          x-ngsi:    
            model: http://schema.org/contactOption    
            type: Property    
        contactType:    
          description: Contact type of this item    
          type: string    
          x-ngsi:    
            type: Property    
        email:    
          description: Email address of owner    
          format: idn-email    
          type: string    
          x-ngsi:    
            type: Property    
        faxNumber:    
          description: The fax number    
          type: string    
          x-ngsi:    
            model: http://schema.org/Text    
            type: Property    
        name:    
          description: The name of this item    
          type: string    
          x-ngsi:    
            type: Property    
        productSupported:    
          description: The product or service this support contact point is related to (such as product support for a particular product line). This can be a specific product or product line (e.g. 'iPhone') or a general category of products or services (e.g. 'smartphones')    
          type: string    
          x-ngsi:    
            model: http://schema.org/Text    
            type: Property    
        telephone:    
          description: Telephone of this contact    
          type: string    
          x-ngsi:    
            type: Property    
        url:    
          description: URL which provides a description or further information about this item    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        model: https://schema.org/ContactPoint    
        type: Property    
    dataDescriptor:    
      description: URI pointing to the data-descriptor entity    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
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
    endDateTime:    
      description: Reported end time corresponding to this observation    
      format: date-time    
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
    network:    
      description: 'The name of the Network, with that the operator cooperates. '    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    observationDateTime:    
      description: Last reported time of observation    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    openingHours:    
      description: 'Opening hours of the charging station. '    
      type: string    
      x-ngsi:    
        model: http://schema.org/openingHours    
        type: Property    
    operator:    
      description: 'Charging station''s operator. '    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
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
    powerConsumption:    
      description: Power consumed by the entity corresponding to this observation    
      type: number    
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
    socketNumber:    
      description: The total number of sockets offered by this charging station    
      minimum: 1    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    socketType:    
      description: 'The type of sockets offered by this station. Enum:''Caravan_Mains_Socket, CHAdeMO, CCS/SAE, Dual_CHAdeMO, Dual_J-1772, Dual_Mennekes, J-1772, Mennekes, Other, Tesla, Type2, Type3, Wall_Euro'''    
      items:    
        enum:    
          - Caravan_Mains_Socket    
          - CHAdeMO    
          - CCS/SAE    
          - Dual_CHAdeMO    
          - Dual_J-1772    
          - Dual_Mennekes    
          - J-1772    
          - Mennekes    
          - Other    
          - Tesla    
          - Type2    
          - Type3    
          - Wall_Euro    
        type: string    
      minItems: 1    
      type: array    
      uniqueItems: true    
      x-ngsi:    
        model: http://schema.org/Text    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    startDateTime:    
      description: Reported start time corresponding to this observation    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    stationName:    
      description: 'The name station corresponding to this observation. It can be the name of bike docking station, charging station, etc'    
      type: string    
      x-ngsi:    
        type: Property    
    status:    
      description: 'Status of the charging station. Enum:''almostEmpty, almostFull, empty, full, outOfService, withIncidence, working''. Or any other application-specific'    
      enum:    
        - almostEmpty    
        - almostFull    
        - empty    
        - full    
        - outOfService    
        - withIncidence    
        - working    
      type: string    
      x-ngsi:    
        model: http://schema.org/Text    
        type: Property    
    taxAmountCollected:    
      description: 'The amount of tax levied on the products, things and services which includes sales tax, value-added tax, service tax, Good and Service tax, customs duty, etc'    
      type: number    
      x-ngsi:    
        type: Property    
    transactionId:    
      description: Unique transaction Id of the entity corresponding to this observation    
      type: string    
      x-ngsi:    
        type: Property    
    transactionType:    
      description: 'Type of the transaction based on the mode of payment (For eg. mobile/UPI, card, etc) or mode of service (For eg. Issue, ReIssue, Entry, Exit etc.) corresponding to this observation'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be EVChargingStation    
      enum:    
        - EVChargingStation    
      type: string    
      x-ngsi:    
        type: Property    
    vehicleType:    
      description: 'Type of vehicle from the point of view of its structural characteristics. This is different than the vehicle category . Enum:''agriculturalVehicle, ambulance, anyVehicle, articulatedVehicle, autorickshaw, bicycle, binTrolley, BRT bus, BRT minibus, bus, car, caravan, carOrLightVehicle, carWithCaravan, carWithTrailer, cleaningTrolley, compactor, constructionOrMaintenanceVehicle, dumper, e-moped, e-scooter, e-motorcycle,fire tender, fourWheelDrive, highSidedVehicle, hopper, lorry, minibus, moped, motorcycle, motorcycleWithSideCar, motorscooter, police van, sweepingMachine, tanker, tempo, threeWheeledVehicle, tipper, trailer, tram, twoWheeledVehicle, trolley, van, vehicleWithoutCatalyticConverter, vehicleWithCaravan, vehicleWithTrailer, withEvenNumberedRegistrationPlates, withOddNumberedRegistrationPlates, other''. The following values defined by _VehicleTypeEnum_ and _VehicleTypeEnum2_, [DATEX 2 version 2.3](http://d2docs.ndwcloud.nu/_static/umlmodel/v2.3/index.htm)'    
      enum:    
        - agriculturalVehicle    
        - ambulance    
        - articulatedVehicle    
        - autorickshaw    
        - bicycle    
        - binTrolley    
        - BRT bus    
        - BRT minibus    
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
        - fire tender    
        - fourWheelDrive    
        - highSidedVehicle    
        - hopper    
        - lorry    
        - minibus    
        - moped    
        - motorcycle    
        - motorcycleWithSideCar    
        - motorscooter    
        - police van    
        - sweepingMachine    
        - tanker    
        - tempo    
        - threeWheeledVehicle    
        - tipper    
        - trailer    
        - tram    
        - twoWheeledVehicle    
        - trolley    
        - van    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    voltage:    
      description: The total voltage offered by the charging station    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: Volts (V)    
  required:    
    - id    
    - type    
    - socketType    
    - capacity    
    - allowedVehicleType    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Transportation/blob/master/EVChargingStation/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Transportation/EVChargingStation/schema.json    
  x-model-tags: IUDX    
  x-version: 0.1.0    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 有效载荷示例  
#### EVChargingStation NGSI-v2 密钥值示例  
下面是一个以 JSON-LD 格式作为键值的 EVChargingStation 示例。当使用 `options=keyValues` 时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:EVChargingStation:ValladolI+D_Covaresa",  
  "type": "EVChargingStation",  
  "name": "Agencia de Innovación",  
  "location": {  
    "coordinates": [-4.747901, 41.618265],  
    "type": "Point"  
  },  
  "capacity": 2,  
  "socketType": ["Wall_Euro"],  
  "address": {  
    "streetAddress": "Paseo de Zorrilla, 191",  
    "addressLocality": "Valladolid",  
    "addressCountry": "España"  
  },  
  "contactPoint": {  
    "email": "vehiculoelectrico@ava.es"  
  },  
  "operator": "Iberdrola",  
  "allowedVehicleType": ["car"],  
  "chargeType": ["free"],  
  "source": "https://openchargemap.org/",  
   "powerConsumption": 10.0,  
  "chargingUnitId": "PZEV01-DeltaBharatAC001-SCTLGandhiPark001",  
  "transactionId": "84068784",  
  "transactionType": "RFID",  
  "stationName": "SmartCityTvmGandhiParkOne",  
  "amountCollected": 0.08,  
  "taxAmountCollected": 0.0,  
  "endDateTime": "2022-06-28T20:28:41+05:30",  
  "startDateTime": "2022-06-28T20:27:27+05:30",  
  "vehicleType": "e-motorcycle",  
  "observationDateTime": "2022-06-28T20:27:29+05:30"  
}  
```  
</details>  
#### EVChargingStation NGSI-v2 标准化示例  
下面是一个规范化 JSON-LD 格式的 EVChargingStation 示例。当不使用选项时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:EVChargingStation:ValladolI+D_Covaresa",  
  "type": "EVChargingStation",  
  "socketType": {  
    "type": "array",  
    "value": [  
      "Wall_Euro"  
    ]  
  },  
  "capacity": {  
    "type": "Number",  
    "value": 2  
  },  
  "name": {  
    "type": "Text",  
    "value": "Agencia de Innovaci\u00f3n"  
  },  
  "allowedVehicleType": {  
    "type": "array",  
    "value": [  
      "car"  
    ]  
  },  
  "source": {  
    "type": "Text",  
    "value": "https://openchargemap.org/"  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -4.747901,  
        41.618265  
      ]  
    }  
  },  
  "chargeType": {  
    "type": "array",  
    "value": [  
      "free"  
    ]  
  },  
  "address": {  
    "type": "PostalAddress",  
    "value": {  
      "addressLocality": "Valladolid",  
      "addressCountry": "Espa\u00f1a",  
      "streetAddress": "Paseo de Zorrilla, 191"  
    }  
  },  
  "operator": {  
    "type": "Text",  
    "value": "Iberdrola"  
  },  
  "contactPoint": {  
    "type": "StructuredValue",  
    "value": {  
      "email": "vehiculoelectrico@ava.es"  
    }  
  },  
  "powerConsumption": {  
    "type": "number",  
    "value": 10.0  
  },  
  "chargingUnitId": {  
    "type": "string",  
    "value": "PZEV01-DeltaBharatAC001-SCTLGandhiPark001"  
  },  
  "transactionId": {  
    "type": "string",  
    "value": "84068784"  
  },  
  "transactionType": {  
    "type": "string",  
    "value": "RFID"  
  },  
  "stationName": {  
    "type": "string",  
    "value": "SmartCityTvmGandhiParkOne"  
  },  
  "amountCollected": {  
    "type": "number",  
    "value": 0.08  
  },  
  "taxAmountCollected": {  
    "type": "Number",  
    "value": 0.0  
  },  
  "endDateTime": {  
    "format": "date-time",  
    "type": "string",  
    "value": "2022-06-28T20:28:41+05:30"  
  },  
  "startDateTime": {  
    "format": "date-time",  
    "type": "string",  
    "value": "2022-06-28T20:27:27+05:30"  
  },  
  "vehicleType": {  
    "type": "string",  
    "value": "e-motorcycle"  
  },  
  "observationDateTime": {  
    "format": "date-time",  
    "type": "string",  
    "value": "2022-06-28T20:27:29+05:30"  
  }  
}  
```  
</details>  
#### EVChargingStation NGSI-LD key-values 示例  
下面是一个以 JSON-LD 格式作为键值的 EVChargingStation 示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:EVChargingStation:ValladolI+D_Covaresa",  
    "type": "EVChargingStation",  
    "name": "Agencia de Innovaci\u00f3n",  
    "location": {  
        "coordinates": [  
            -4.747901,  
            41.618265  
        ],  
        "type": "Point"  
    },  
    "capacity": 2,  
    "socketType": [  
        "Wall_Euro"  
    ],  
    "address": {  
        "streetAddress": "Paseo de Zorrilla, 191",  
        "addressLocality": "Valladolid",  
        "addressCountry": "Espa\u00f1a"  
    },  
    "contactPoint": {  
        "email": "vehiculoelectrico@ava.es"  
    },  
    "operator": "Iberdrola",  
    "allowedVehicleType": [  
        "car"  
    ],  
    "chargeType": [  
        "free"  
    ],  
    "source": "https://openchargemap.org/",  
    "powerConsumption": 10.0,  
    "chargingUnitId": "PZEV01-DeltaBharatAC001-SCTLGandhiPark001",  
    "transactionId": "84068784",  
    "transactionType": "RFID",  
    "stationName": "SmartCityTvmGandhiParkOne",  
    "amountCollected": 0.08,  
    "taxAmountCollected": 0.0,  
    "endDateTime": "2022-06-28T20:28:41+05:30",  
    "startDateTime": "2022-06-28T20:27:27+05:30",  
    "vehicleType": "e-motorcycle",  
    "observationDateTime": "2022-06-28T20:27:29+05:30",  
    "@context": [  
        "https://smart-data-models.github.io/dataModel.Transportation/context.jsonld",  
        "iudx:EVChargingStation"  
    ]  
}  
```  
</details>  
#### EVChargingStation NGSI-LD 标准化示例  
下面是一个规范化 JSON-LD 格式的 EVChargingStation 示例。在不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:EVChargingStation:ValladolI+D_Covaresa",  
  "type": "EVChargingStation",  
  "address": {  
    "type": "Property",  
    "value": {  
      "addressCountry": "Espa\u00f1a",  
      "addressLocality": "Valladolid",  
      "streetAddress": "Paseo de Zorrilla, 191"  
    }  
  },  
  "allowedVehicleType": {  
    "type": "Property",  
    "value": [  
      "car"  
    ]  
  },  
  "capacity": {  
    "type": "Property",  
    "value": 2  
  },  
  "chargeType": {  
    "type": "Property",  
    "value": [  
      "free"  
    ]  
  },  
  "contactPoint": {  
    "type": "Property",  
    "value": {  
      "email": "vehiculoelectrico@ava.es"  
    }  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "coordinates": [  
        -4.747901,  
        41.618265  
      ],  
      "type": "Point"  
    }  
  },  
  "name": {  
    "type": "Property",  
    "value": "Agencia de Innovaci\u00f3n"  
  },  
  "operator": {  
    "type": "Property",  
    "value": "Iberdrola"  
  },  
  "socketType": {  
    "type": "Property",  
    "value": [  
      "Wall_Euro"  
    ]  
  },  
  "source": {  
    "type": "Property",  
    "value": "https://openchargemap.org/"  
  },  
  "powerConsumption": {  
    "type": "Property",  
    "value": 10.0  
  },  
  "chargingUnitId": {  
    "type": "Property",  
    "value": "PZEV01-DeltaBharatAC001-SCTLGandhiPark001"  
  },  
  "transactionId": {  
    "type": "Property",  
    "value": "84068784"  
  },  
  "transactionType": {  
    "type": "Property",  
    "value": "RFID"  
  },  
  "stationName": {  
    "type": "Property",  
    "value": "SmartCityTvmGandhiParkOne"  
  },  
  "amountCollected": {  
    "type": "Property",  
    "value": 0.08  
  },  
  "taxAmountCollected": {  
    "type": "Property",  
    "value": 0.0  
  },  
  "endDateTime": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2022-06-28T20:28:41+05:30"  
    }  
  },  
  "startDateTime": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2022-06-28T20:27:27+05:30"  
    }  
  },  
  "vehicleType": {  
    "type": "Property",  
    "value": "e-motorcycle"  
  },  
  "observationDateTime": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2022-06-28T20:27:29+05:30"  
    }  
  },  
  "@context": [  
    "https://smart-data-models.github.io/dataModel.Transportation/context.jsonld"  
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
