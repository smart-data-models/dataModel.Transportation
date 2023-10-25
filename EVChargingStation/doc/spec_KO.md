<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
엔티티: EVChargingStation  
======================<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models//dataModel.Transportation/blob/master/EVChargingStation/LICENSE.md)  
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
글로벌 설명: **전기차 충전소**  
버전: 0.1.0  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 속성 목록  

<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.  
- `acceptedPaymentMethod[array]`: 이 스테이션을 사용할 때의 충전 유형입니다. Enum:'ByBankTransferInAdvance, ByInvoice, Cash, CheckInAdvance, COD, DirectDebit, GoogleCheckout, PayPal, PaySwarm'  . Model: [https://schema.org/Text](https://schema.org/Text)- `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 국가. 예를 들어, 스페인  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 도로명 주소가 있는 지역 및 해당 지역에 속한 지역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 해당 지역이 위치한 지역과 해당 국가의 지역  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 지구는 일부 국가에서는 지방 정부에서 관리하는 행정 구역의 일종입니다.    
	- `postOfficeBoxNumber[string]`: 사서함 주소의 우체국 사서함 번호입니다. 예: 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 우편 번호입니다. 예: 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 거리 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 공공 도로의 특정 건물을 식별하는 번호    
- `allowedVehicleType[array]`: 충전할 수 있는 차량 유형. Enum: '자전거, 버스, 자동차, 카라반, 오토바이, 모터스쿠터, 트럭'  . Model: [http://schema.org/Text](http://schema.org/Text)- `alternateName[string]`: 이 항목의 대체 이름  - `amountCollected[number]`: 이 관찰에 해당하는 서비스를 위해 수집된 금액  - `amperage[number]`: 충전 스테이션에서 제공하는 총 암페어입니다.  . Model: [http://schema.org/Number](http://schema.org/Number)- `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `availableCapacity[number]`: 현재 충전할 수 있는 차량 수입니다. '용량'보다 낮거나 같아야 합니다.  . Model: [http://schema.org/Number](http://schema.org/Number)- `capacity[number]`: 동시에 충전할 수 있는 총 차량 수입니다. 총 소켓 수는 더 많을 수 있습니다.  . Model: [http://schema.org/Number](http://schema.org/Number)- `chargeType[array]`: 이 스테이션을 사용할 때의 요금 유형입니다. Enum:'연간결제, 정액, 무료, 월정액, 기타'  . Model: [https://schema.org/Text](https://schema.org/Text)- `chargingUnitId[string]`: 이 관측에 해당하는 전기차 충전소의 충전 지점 ID입니다.  - `contactPoint[object]`: 항목과 관련하여 문의할 세부 정보  . Model: [https://schema.org/ContactPoint](https://schema.org/ContactPoint)	- `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역입니다. 서비스 지역 대체    
	- `availabilityRestriction[*]`: 이 속성은 연락처를 연락처를 사용할 수 없는 시간에 대한 정보에 연결합니다. 세부 정보는 영업 시간 지정 클래스를 사용하여 제공됩니다.  . Model: [http://schema.org/hoursAvailable](http://schema.org/hoursAvailable)  
	- `availableLanguage[*]`: 누군가가 해당 상품, 서비스 또는 장소에서 사용할 수 있는 언어입니다. IETF BCP 47 표준의 언어 코드 중 하나를 사용하세요. 텍스트 옵션이 구현되어 있지만 언어  . Model: [http://schema.org/availableLanguage](http://schema.org/availableLanguage)  
	- `contactOption[*]`: 이 연락처에서 사용할 수 있는 옵션(예: 수신자 부담 번호 또는 청각 장애 발신자를 위한 지원)  . Model: [http://schema.org/contactOption](http://schema.org/contactOption)  
	- `contactType[string]`: 이 항목의 연락처 유형    
	- `email[idn-email]`: 소유자의 이메일 주소    
	- `faxNumber[string]`: 팩스 번호  . Model: [http://schema.org/Text](http://schema.org/Text)  
	- `name[string]`: 이 항목의 이름    
	- `productSupported[string]`: 이 지원 문의처가 관련된 제품 또는 서비스(예: 특정 제품 라인에 대한 제품 지원). 특정 제품 또는 제품 라인(예: 'iPhone') 또는 일반적인 제품 또는 서비스 카테고리(예: '스마트폰')일 수 있습니다.  . Model: [http://schema.org/Text](http://schema.org/Text)  
	- `telephone[string]`: 이 연락처의 전화    
	- `url[uri]`: 이 항목에 대한 설명이나 추가 정보를 제공하는 URL입니다.    
- `dataDescriptor[uri]`: 데이터 기술자 엔티티를 가리키는 URI  - `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `endDateTime[date-time]`: 이 관측에 해당하는 보고된 종료 시간  - `id[*]`: 엔티티의 고유 식별자  - `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.  - `name[string]`: 이 항목의 이름  - `network[string]`: 운영자가 협력하는 네트워크의 이름입니다.  . Model: [https://schema.org/Text](https://schema.org/Text)- `observationDateTime[date-time]`: 마지막으로 보고된 관찰 시간  - `openingHours[string]`: 충전소 영업 시간.  . Model: [http://schema.org/openingHours](http://schema.org/openingHours)- `operator[string]`: 충전소 운영자.  . Model: [https://schema.org/Text](https://schema.org/Text)- `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `powerConsumption[number]`: 이 관측에 해당하는 엔티티가 소비한 전력  - `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `socketNumber[number]`: 이 충전 스테이션에서 제공하는 총 소켓 수  . Model: [http://schema.org/Number](http://schema.org/Number)- `socketType[array]`: 이 스테이션에서 제공하는 소켓 유형입니다. Enum:'Caravan_Mains_Socket, CHAdeMO, CCS/SAE, Dual_CHAdeMO, Dual_J-1772, Dual_Mennekes, J-1772, Mennekes, 기타, 테슬라, 타입2, 타입3, Wall_Euro'  . Model: [http://schema.org/Text](http://schema.org/Text)- `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `startDateTime[date-time]`: 이 관측에 해당하는 보고된 시작 시간  - `stationName[string]`: 이 관측에 해당하는 스테이션 이름입니다. 자전거 도킹 스테이션, 충전 스테이션 등의 이름이 될 수 있습니다.  - `status[string]`: 충전소의 상태. Enum: '거의 비어 있음, 거의 가득 찼음, 비어 있음, 가득 찼음, 서비스 중 없음, 사용 중임, 작동 중임'. 또는 기타 애플리케이션별  . Model: [http://schema.org/Text](http://schema.org/Text)- `taxAmountCollected[number]`: 판매세, 부가가치세, 서비스세, 상품 및 서비스세, 관세 등이 포함된 제품, 물건 및 서비스에 부과되는 세금 금액입니다.  - `transactionId[string]`: 이 관찰에 해당하는 엔티티의 고유 트랜잭션 ID  - `transactionType[string]`: 해당 관찰에 해당하는 결제 모드(예: 모바일/UPI, 카드 등) 또는 서비스 모드(예: 발급, 재발급, 진입, 퇴장 등)를 기반으로 한 거래 유형  - `type[string]`: NGSI 엔티티 유형. EVChargingStation이어야 합니다.  - `vehicleType[string]`: 구조적 특성의 관점에서 본 차량 유형. 이는 차량 카테고리와는 다릅니다. Enum:'농업용차량, 구급차, 모든차량, 굴절형차량, 인력거, 자전거, 빈트롤리, BRT버스, BRT미니버스, 버스, 자동차, 카라반, 자동차Or경량차량, 자동차위드카라반, 자동차위드트레일러, 청소트롤리, 컴팩터, 건설용차량, 덤프, 전자모페드, 전자스쿠터, 전자오토바이,소방차, 4륜구동, 하이사이드차량, 호퍼, 화물차, 미니버스, 오토바이, 모터사이클, 모터스쿠터, 경찰차, 청소차, 유조선, 템포, 3륜차, 팁퍼, 트레일러, 트램, 2륜차, 트롤리, 밴, 차량위드아웃촉매컨버터, 차량위드카라반, 차량위드트레일러, 짝수번호등록번호판, 홀수번호등록번호판, 기타'. 차량 유형에 따라 정의되는 값은 다음과 같습니다. _VehicleTypeEnum_ 및 _VehicleTypeEnum2_, [DATEX 2 버전 2.3](http://d2docs.ndwcloud.nu/_static/umlmodel/v2.3/index.htm).  . Model: [https://schema.org/Text](https://schema.org/Text)- `voltage[number]`: 충전소에서 제공하는 총 전압  . Model: [http://schema.org/Number](http://schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
필수 속성  
- `allowedVehicleType`  - `capacity`  - `id`  - `socketType`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
전기 자동차에 에너지를 공급하는 공공 충전소입니다. 충전 시간은 충전소의 최대 전력 출력, 현재 충전 중인 차량 수, 현재 배터리 잔량에 따라 달라집니다.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 속성에 대한 데이터 모델 설명  
알파벳순으로 정렬(자세한 내용을 보려면 클릭)  
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
## 페이로드 예시  
#### EVChargingStation NGSI-v2 키-값 예시  
다음은 키-값으로 JSON-LD 형식의 EVChargingStation의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
#### EVChargingStation NGSI-v2 정규화 예제  
다음은 정규화된 JSON-LD 형식의 EVChargingStation의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
#### EVChargingStation NGSI-LD 키-값 예시  
다음은 키-값으로 JSON-LD 형식의 EVChargingStation의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
#### EVChargingStation NGSI-LD 정규화 예시  
다음은 정규화된 JSON-LD 형식의 EVChargingStation의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
[FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하여 규모 단위를 다루는 방법에 대한 답변을 확인하세요.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
