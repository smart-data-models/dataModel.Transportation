<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entity: BikeHireDockingStation    
==============================<!-- /10-Header -->    
<!-- 15-License -->    
[오픈 라이선스](https://github.com/smart-data-models//dataModel.Transportation/blob/master/BikeHireDockingStation/LICENSE.md)    
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
글로벌 설명: 자전거 대여소** **자전거 대여 스테이션    
버전: 0.1.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## 속성 목록    
<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.    
- `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 국가. 예를 들어, 스페인  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: 도로명 주소가 있는 지역 및 해당 지역에 속한 지역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: 해당 지역이 위치한 지역과 해당 국가의 지역  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: 지구는 일부 국가에서는 지방 정부에서 관리하는 행정 구역의 일종입니다.      
	- `postOfficeBoxNumber[string]`: 사서함 주소의 우체국 사서함 번호입니다. 예: 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: 우편 번호입니다. 예: 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: 거리 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
	- `streetNr[string]`: 공공 도로의 특정 건물을 식별하는 번호      
- `agency_fare_url[string]`: 요금에 대한 세부 정보가 포함되어 있으며 해당 여행사의 항공권을 온라인으로 구매할 수 있는 웹 페이지의 URL입니다. SameAs: GTFS 정적 필드 정의 - agency.txt(https://developers.google.com/transit/gtfs/reference#agencytxt)의 'agency_fare_url' 필드  - `agency_name[string]`: 에이전시_이름 필드에는 운송업체의 전체 이름이 포함됩니다. SameAs: GTFS 정적 필드 정의의 'agency_name' 필드 - agency.txt(https://developers.google.com/transit/gtfs/reference#agencytxt)  . Model: [https://schema.org/Text](https://schema.org/Text)- `agency_url[uri]`: agency_url 필드에는 운송 대행사의 URL이 포함됩니다. SameAs: GTFS 정적 필드 정의의 'agency_url' 필드 - agency.txt(https://developers.google.com/transit/gtfs/reference#agencytxt)  . Model: [https://schema.org/Text](https://schema.org/Text)- `alternateName[string]`: 이 항목의 대체 이름  - `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `availableBikeNumber[number]`: 자전거 대여 도킹 스테이션에서 사용자가 대여할 수 있는 자전거 대수  . Model: [https://schema.org/Number](https://schema.org/Number)- `contactPoint[object]`: 항목과 관련하여 문의할 세부 정보  . Model: [https://schema.org/ContactPoint](https://schema.org/ContactPoint)	- `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역입니다. 서비스 지역 대체      
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
- `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `freeSlotNumber[number]`: 자전거 반납 및 주차에 사용할 수 있는 슬롯 수입니다. 총 슬롯 수`보다 작거나 같아야 합니다.  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: 엔티티의 고유 식별자  - `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.  - `mediaURL[uri]`: 불만 사항 또는 장소의 이미지 또는 미디어에 대한 추가 정보를 제공하는 URL  . Model: [https://schema.org/Text](https://schema.org/Text)- `name[string]`: 이 항목의 이름  - `observationDateTime[date-time]`: 마지막으로 보고된 관찰 시간  . Model: [https://schema.org/Text](https://schema.org/Text)- `openingHours[string]`: 도킹 스테이션 운영 시간  . Model: [http://schema.org/openingHours](http://schema.org/openingHours)- `outOfServiceSlotNumber[number]`: 고장나서 자전거를 대여하거나 주차하는 데 사용할 수 없는 슬롯의 수입니다. 총 슬롯 수`보다 작거나 같아야 합니다.  . Model: [https://schema.org/Number](https://schema.org/Number)- `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `provider[string]`: 자전거 대여 서비스 제공업체  . Model: [https://schema.org/provider](https://schema.org/provider)- `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `stationCode[string]`: 관측에 해당하는 자전거 대여 스테이션의 스테이션 번호 또는 스테이션 코드  . Model: [https://schema.org/Text](https://schema.org/Text)- `stationName[string]`: 이 관측에 해당하는 자전거 대여소 이름  . Model: [https://schema.org/Text](https://schema.org/Text)- `status[string]`: 자전거 대여소 도킹 스테이션의 상태. Enum:'작동 중, 아웃오브서비스, 위드인시던트, 풀, 거의풀, 비어 있음, 거의비어 있음'. 또는 기타 애플리케이션별  . Model: [https://schema.org/Number](https://schema.org/Number)- `totalSlotNumber[number]`: 이 자전거 도킹 스테이션이 제공하는 총 슬롯 수  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: NGSI 엔티티 유형. BikeHireDockingStation이어야 합니다.  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
필수 속성    
- `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
많은 도시에서 시민을 위한 자전거 대여 시스템을 제공합니다. 다양한 유형의 구독을 통해 자전거를 대여할 수 있습니다. 구독한 사용자가 자전거를 대여하고 반납할 수 있는 자전거 대여 도킹 스테이션입니다. 주요 기능과 자전거의 가용성 및 무료 슬롯에 대한 데이터를 제공합니다.    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## 속성에 대한 데이터 모델 설명    
알파벳순으로 정렬(자세한 내용을 보려면 클릭)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
BikeHireDockingStation:      
  description: Bike Hire Docking Station      
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
    agency_fare_url:      
      description: "URL of a web page that contains the details of the fares and also could allow to purchase tickets for that agency online. SameAs: 'agency_fare_url' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt) "      
      type: string      
      x-ngsi:      
        type: Property      
    agency_name:      
      description: "The agency_name field contains the full name of the transit agency. SameAs: 'agency_name' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)"      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    agency_url:      
      description: "The agency_url field contains the URL of the transit agency. SameAs: 'agency_url' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)"      
      format: uri      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
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
    availableBikeNumber:      
      description: The number of bikes available in the bike hire docking station to be hired by users      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
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
    freeSlotNumber:      
      description: The number of slots available for returning and parking bikes. It must lower or equal than `totalSlotNumber`      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
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
    mediaURL:      
      description: URL providing further information of any image(s) or media of the complaint or place      
      format: uri      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    name:      
      description: The name of this item      
      type: string      
      x-ngsi:      
        type: Property      
    observationDateTime:      
      description: Last reported time of observation      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    openingHours:      
      description: Opening hours of the docking station      
      type: string      
      x-ngsi:      
        model: http://schema.org/openingHours      
        type: Property      
    outOfServiceSlotNumber:      
      description: The number of slots that are out of order and cannot be used to hire or park a bike. It must lower or equal than `totalSlotNumber`      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
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
    provider:      
      description: Bike hire service provider      
      type: string      
      x-ngsi:      
        model: https://schema.org/provider      
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
    stationCode:      
      description: The station number or station code of the bike hire docking station corresponding to the observation      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    stationName:      
      description: The name of the bike hire docking station corresponding to this observation      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    status:      
      description: 'Status of the bike hire docking station. Enum:''working, outOfService, withIncidence, full, almostFull, empty, almostEmpty''. Or any other application specific'      
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
        model: https://schema.org/Number      
        type: Property      
    totalSlotNumber:      
      description: The total number of slots offered by this bike docking station      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    type:      
      description: NGSI Entity type. It has to be BikeHireDockingStation      
      enum:      
        - BikeHireDockingStation      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.Transportation/blob/master/BikeHireDockingStation/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.Transportation/BikeHireDockingStation/schema.json      
  x-model-tags: ""      
  x-version: 0.1.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## 페이로드 예시    
#### BikeHireDockingStation NGSI-v2 키값 예시    
다음은 키값으로 JSON-LD 형식의 BikeHireDockingStation의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Bcn-BikeHireDockingStation-1",  
  "type": "BikeHireDockingStation",  
  "status": "working",  
  "provider": "University of Mumbay",  
  "contactPoint": {  
    "url": "uri:ngsi:www.lignesdazur.com"  
  },  
  "availableBikeNumber": 20,  
  "freeSlotNumber": 10,  
  "openingHours": "Mo-Fr 10:00-19:00, Sa 10:00-22:00, Su 10:00-21:00",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      2.180042,  
      41.397952  
    ]  
  },  
  "address": {  
    "addressCountry": "ES",  
    "addressLocality": "Barcelona",  
    "streetAddress": "Gran Via Corts Catalanes,760"  
  },  
  "totalSlotNumber": 100,  
  "outOfServiceSlotNumber": 21,  
  "stationName": "Pune",  
  "mediaURL": "http://pedalsaddle.in/",  
  "agency_url": "http://pedalsaddle.in/",  
  "agency_name": "PedalSaddle",  
  "stationCode": "2",  
  "observationDate": "2021-03-11T15:51:02+05:30",  
  "agency_fare_url": ""  
}  
```  
</details>    
#### BikeHireDockingStation NGSI-v2 정규화 예제    
다음은 정규화된 JSON-LD 형식의 BikeHireDockingStation의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Bcn-BikeHireDockingStation-1",  
  "type": "BikeHireDockingStation",  
  "status": {  
    "type": "Text",  
    "value": "working"  
  },  
  "provider": {  
    "type": "Text",  
    "value": "University of Mumbay"  
  },  
  "contactPoint": {  
    "type": "StructuredValue",  
    "value": {  
      "url": "uri:ngsi:www.lignesdazur.com"  
    }  
  },  
  "availableBikeNumber": {  
    "type": "Number",  
    "value": 20  
  },  
  "freeSlotNumber": {  
    "type": "Number",  
    "value": 10  
  },  
  "openingHours": {  
    "type": "Text",  
    "value": "Mo-Fr 10:00-19:00, Sa 10:00-22:00, Su 10:00-21:00"  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        2.180042,  
        41.397952  
      ]  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "addressCountry": "ES",  
      "addressLocality": "Barcelona",  
      "streetAddress": "Gran Via Corts Catalanes,760"  
    }  
  },  
  "totalSlotNumber": {  
    "type": "Number",  
    "value": 100  
  },  
  "outOfServiceSlotNumber": {  
    "type": "Number",  
    "value": 21  
  },  
  "stationName": {  
    "type": "Text",  
    "value": "Pune"  
  },  
  "mediaURL": {  
    "type": "Text",  
    "value": "http://pedalsaddle.in/"  
  },  
  "agency_url": {  
    "type": "Text",  
    "value": "http://pedalsaddle.in/"  
  },  
  "agency_name": {  
    "type": "Text",  
    "value": "PedalSaddle"  
  },  
  "stationCode": {  
    "type": "Text",  
    "value": "2"  
  },  
  "observationDate": {  
    "type": "DateTime",  
    "value": "2021-03-11T15:51:02+05:30"  
  },  
  "agency_fare_url": {  
    "type": "Text",  
    "value": ""  
  }  
}  
```  
</details>    
#### BikeHireDockingStation NGSI-LD 키값 예시    
다음은 키값으로 JSON-LD 형식의 BikeHireDockingStation의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Bcn-BikeHireDockingStation-1",  
  "type": "BikeHireDockingStation",  
  "address": {  
    "addressCountry": "ES",  
    "addressLocality": "Barcelona",  
    "streetAddress": "Gran Via Corts Catalanes,760"  
  },  
  "agency_fare_url": "",  
  "agency_name": "PedalSaddle",  
  "agency_url": "http://pedalsaddle.in/",  
  "availableBikeNumber": 20,  
  "contactPoint": {  
    "url": "uri:ngsi:www.lignesdazur.com"  
  },  
  "freeSlotNumber": 10,  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      2.180042,  
      41.397952  
    ]  
  },  
  "mediaURL": "http://pedalsaddle.in/",  
  "observationDate": "2021-03-11T15:51:02+05:30",  
  "openingHours": "Mo-Fr 10:00-19:00, Sa 10:00-22:00, Su 10:00-21:00",  
  "outOfServiceSlotNumber": 21,  
  "provider": "University of Mumbay",  
  "stationCode": "2",  
  "stationName": "Pune",  
  "status": "working",  
  "totalSlotNumber": 100,  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Transportation/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### BikeHireDockingStation NGSI-LD 정규화 예제    
다음은 정규화된 JSON-LD 형식의 BikeHireDockingStation의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
    "id": "urn:ngsi-ld:Bcn-BikeHireDockingStation-1",  
    "type": "BikeHireDockingStation",  
    "address": {  
        "type": "Property",  
        "value": {  
            "addressCountry": "ES",  
            "addressLocality": "Barcelona",  
            "streetAddress": "Gran Via Corts Catalanes,760"  
        }  
    },  
    "agency_fare_url": {  
        "type": "Property",  
        "value": ""  
    },  
    "agency_name": {  
        "type": "Property",  
        "value": "PedalSaddle"  
    },  
    "agency_url": {  
        "type": "Property",  
        "value": "http://pedalsaddle.in/"  
    },  
    "availableBikeNumber": {  
        "type": "Property",  
        "value": 20  
    },  
    "contactPoint": {  
        "type": "Property",  
        "value": {  
            "url": "uri:ngsi:www.lignesdazur.com"  
        }  
    },  
    "freeSlotNumber": {  
        "type": "Property",  
        "value": 10  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                2.180042,  
                41.397952  
            ]  
        }  
    },  
    "mediaURL": {  
        "type": "Property",  
        "value": "http://pedalsaddle.in/"  
    },  
    "observationDate": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2021-03-11T15:51:02+05:30"  
        }  
    },  
    "openingHours": {  
        "type": "Property",  
        "value": "Mo-Fr 10:00-19:00, Sa 10:00-22:00, Su 10:00-21:00"  
    },  
    "outOfServiceSlotNumber": {  
        "type": "Property",  
        "value": 21  
    },  
    "provider": {  
        "type": "Property",  
        "value": "University of Mumbay"  
    },  
    "stationCode": {  
        "type": "Property",  
        "value": "2"  
    },  
    "stationName": {  
        "type": "Property",  
        "value": "Pune"  
    },  
    "status": {  
        "type": "Property",  
        "value": "working"  
    },  
    "totalSlotNumber": {  
        "type": "Property",  
        "value": 100  
    },  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Transportation/master/context.jsonld"  
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
