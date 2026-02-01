<!-- 10-Header -->
  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

엔티티: OriginDestinationFlow  
=============================
<!-- /10-Header -->
  
<!-- 15-License -->
  

[오픈 라이선스](https://github.com/smart-data-models//dataModel.Transportation/blob/master/OriginDestinationFlow/LICENSE.md)  

[자동으로 생성된 문서](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->
  
<!-- 20-Description -->
  

Global description: **방문자 이동 흐름의 출발지와 도착지 자치체 간의 시간별 관찰, 국적별 구분. 각 엔티티는 특정 시간 동안 두 위치 간의 흐름 수를 나타낸다.**  

version: 0.0.1  
<!-- /20-Description -->
  
<!-- 30-PropertiesList -->
  


## 속성 목록  


<sup><sub>[*] 속성에 유형이 없으면 여러 유형이나 다른 형식/패턴을 가질 수 있기 때문입니다.</sub></sup>  
- `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)  
	- `addressCountry[string]`: 그 국가. 예를 들어 스페인  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: 그 거리 주소가 속한 지역 및 지역에 속한  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: 그 지역은 그 지방이 있으며, 또한 그 국가에 있습니다  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: 구는 일부 국가에서 지방 정부가 관리하는 유형의 행정 구역입니다  
	- `postOfficeBoxNumber[string]`: 우체국 사서함 번호(PO 박스 주소용). 예를 들어, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: 우편번호. 예를 들어, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: 도로 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
	- `streetNr[string]`: 공공 도로상 특정 부동산을 식별하는 번호  
- `aggregationDateType[string]`: 날짜 집계 유형(예: 시간별, 일별, 월별)  
- `alternateName[string]`: 이 항목의 대체 이름  
- `areaServed[string]`: 서비스나 제공된 항목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `countryCode[string]`: 흐름과 관련된 사람들과 관련된 국가 코드, 예를 들어 ES, IT, FR 등...  
- `dataProvider[string]`: 조화된 데이터 엔티티의 제공자를 식별하는 문자열 시퀀스  
- `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이것은 일반적으로 저장소 플랫폼에 의해 할당됩니다.  
- `dateModified[date-time]`: 엔티티의 마지막 수정 시각. 이것은 일반적으로 저장소 플랫폼에 의해 할당된다.  
- `dateObserved[date-time]`: ISO 8601 형식의 관측 일시  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)  
- `description[string]`: 이 항목에 대한 설명  
- `destinationLocation[*]`: Geojson 아이템 참조입니다. Point, LineString, Polygon, MultiPoint, MultiLineString 또는 MultiPolygon 중 하나일 수 있습니다.  
- `destinationLocationCode[string]`: 도착 지자체의 공식 코드  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `destinationLocationName[string]`: 도착지 시정촌의 이름  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `flowCount[number]`: 이 시간 동안 출발지와 도착지 사이를 이동한 총 이동/흐름 수  . Model: [https://schema.org/Number](https://schema.org/Number)  
- `flowType[string]`: 유형의 흐름. Enum: '관광, 통근, 비즈니스, 이주, 혼합'  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `hour[number]`: 이 관측에 대한 일일 시간(0-23)  . Model: [https://schema.org/Number](https://schema.org/Number)  
- `id[*]`: 엔티티의 고유 식별자  
- `location[*]`: Geojson 아이템 참조입니다. Point, LineString, Polygon, MultiPoint, MultiLineString 또는 MultiPolygon 중 하나가 될 수 있습니다.  
- `name[string]`: 이 항목의 이름  
- `nationality[string]`: 방문자 국적. ISO 3166-1 alpha-2 국가 코드 (예: ES, FR, GB, PT, DE)  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `nationalityName[string]`: 국적 국가의 전체 이름(선택 사항, 인간의 가독성을 위해)  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `originLocation[*]`: Geojson 아이템 참조입니다. Point, LineString, Polygon, MultiPoint, MultiLineString 또는 MultiPolygon 중 하나일 수 있습니다.  
- `originLocationCode[string]`: 원래 자치체의 공식 코드  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `originLocationName[string]`: 원래 시정촌 이름  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `owner[array]`: 소유자(들)의 고유 ID를 참조하는 문자열 시퀀스를 JSON으로 인코딩한 문자열을 포함하는 목록  
- `seeAlso[*]`: 아이템에 대한 추가 리소스를 가리키는 URI 목록  
- `source[string]`: 엔티티 데이터의 원래 출처를 URL로 제공하는 문자열 시퀀스. 출처 제공자의 완전한 도메인 이름이나 출처 객체에 대한 URL로 지정하는 것을 권장합니다.  
- `type[string]`: NGSI 엔티티 유형입니다. OriginDestinationFlow이어야 합니다.  
<!-- /30-PropertiesList -->
  
<!-- 35-RequiredProperties -->
  

필수 속성  
- `id`  
- `유형`  
<!-- /35-RequiredProperties -->
  
<!-- 40-NotesYaml -->
  
<!-- /40-NotesYaml -->
  
<!-- 50-DataModelHeader -->
  

## 데이터 모델 속성 설명  

가나다순으로 정렬됨 (자세한 정보 클릭)  
<!-- /50-DataModelHeader -->
  
<!-- 60-ModelYaml -->
  
<details><summary><strong>full yaml details</strong></summary>    

```yaml  
OriginDestinationFlow:    
  description: Hourly observation of visitor movement flows between origin and destination municipalities, segmented by nationality. Each entity represents the flow count between two locations during a specific hour.    
  properties:    
    address:    
      description: The mailing address    
      properties:    
        addressCountry:    
          description: The country. For example, Spain    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressCountry    
            type: Property    
        addressLocality:    
          description: The locality in which the street address is, and which is in the region    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressLocality    
            type: Property    
        addressRegion:    
          description: The region in which the locality is, and which is in the country    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressRegion    
            type: Property    
        district:    
          description: A district is a type of administrative division that, in some countries, is managed by the local government    
          type: string    
          x-ngsi:    
            type: Property    
        postOfficeBoxNumber:    
          description: The post office box number for PO box addresses. For example, 03578    
          type: string    
          x-ngsi:    
            model: https://schema.org/postOfficeBoxNumber    
            type: Property    
        postalCode:    
          description: The postal code. For example, 24004    
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
    aggregationDateType:    
      description: Type of date aggregation (e.g., hourly, daily, monthly)    
      type: string    
      x-ngsi:    
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
    countryCode:    
      description: Origin country code associated to the people associated to the flow, eg. ES, IT, FR, etc...    
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
    dateObserved:    
      description: Date and time of the observation in ISO 8601 format    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    destinationLocation:    
      description: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon    
      oneOf:    
        - description: Geojson reference to the item. Point    
          properties:    
            bbox:    
              description: BBox of the  Point    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the Point    
              items:    
                type: number    
              minItems: 2    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the LineString    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: BBox coordinates of the Polygon    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the Polygon    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the MulitPoint    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the MultiLineString    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: Coordinates of the MultiPolygon    
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
              x-ngsi:    
                type: Property    
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
    destinationLocationCode:    
      description: Official code of the destination municipality    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    destinationLocationName:    
      description: Name of the destination municipality    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    flowCount:    
      description: Total number of movements/flows between origin and destination during this hour    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: movements    
    flowType:    
      description: Type of flow. Enum:'tourism, commuting, business, migration, mixed'    
      enum:    
        - tourism    
        - commuting    
        - business    
        - migration    
        - mixed    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    hour:    
      description: Hour of the day (0-23) for this observation    
      maximum: 23    
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
        type: Relationship    
    location:    
      description: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon    
      oneOf:    
        - description: Geojson reference to the item. Point    
          properties:    
            bbox:    
              description: BBox of the  Point    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the Point    
              items:    
                type: number    
              minItems: 2    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the LineString    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: BBox coordinates of the Polygon    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the Polygon    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the MulitPoint    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the MultiLineString    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: Coordinates of the MultiPolygon    
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
              x-ngsi:    
                type: Property    
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
    nationality:    
      description: Nationality of visitors making the movement. ISO 3166-1 alpha-2 country code (e.g., ES, FR, GB, PT, DE)    
      pattern: ^[A-Z]{2}$    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    nationalityName:    
      description: Full name of the nationality country (optional, for human readability)    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    originLocation:    
      description: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon    
      oneOf:    
        - description: Geojson reference to the item. Point    
          properties:    
            bbox:    
              description: BBox of the  Point    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the Point    
              items:    
                type: number    
              minItems: 2    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the LineString    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: BBox coordinates of the Polygon    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the Polygon    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the MulitPoint    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the MultiLineString    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: Coordinates of the MultiPolygon    
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
              x-ngsi:    
                type: Property    
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
    originLocationCode:    
      description: Official code of the origin municipality    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    originLocationName:    
      description: Name of the origin municipality    
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
          type: Relationship    
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
      description: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI entity type. It has to be OriginDestinationFlow    
      enum:    
        - OriginDestinationFlow    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms...    
  x-license-url: https://github.com/smart-data-models/dataModel.Transportation/blob/master/OriginDestinationFlow/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Transportation/OriginDestinationFlow/schema.json    
  x-model-tags: ''    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->
  
<!-- 70-MiddleNotes -->
  
<!-- /70-MiddleNotes -->
  
<!-- 80-Examples -->
  

## 예제 페이로드  

#### 원본목적지흐름 NGSI-v2 키-값 예시  

여기에는 키-값으로 JSON 형식의 OriginDestinationFlow의 예가 나와 있습니다. 이것은 `options=keyValues`를 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    

```json  

{  
  "id": "OriginDestinationFlow:PT:CO0101:CO0102:DE:20241231T10",  
  "type": "OriginDestinationFlow",  
  "dateObserved": "2024-12-31T10:30:00.00Z",  
  "aggregationDateType": "hourly",  
  "hour": 10,  
  "originLocationCode": "CO0101",  
  "originLocationName": "Coimbra",  
  "destinationLocationCode": "CO0102",  
  "destinationLocationName": "Figueira da Foz",  
  "nationality": "DE",  
  "nationalityName": "Germany",  
  "flowCount": 145,  
  "flowType": "tourism",  
  "countryCode": "PT",  
  "originLocation": {  
    "type": "Point",  
    "coordinates": [-8.4103, 40.2033]  
  },  
  "destinationLocation": {  
    "type": "Point",  
    "coordinates": [-8.8618, 40.1508]  
  },  
  "description": "Hourly visitor flow from Coimbra to Figueira da Foz (German tourists) on 2024-12-31 at 10:00-11:00",  
  "source": "MobilityDataPlatform",  
  "dateCreated": "2024-12-31T11:00:00.00Z",  
  "dateModified": "2024-12-31T11:00:00.00Z"  
}  
```  
</details>  

#### 원본목적지흐름 NGSI-v2 정규화 예시  

여기에는 JSON 형식으로 정규화된 OriginDestinationFlow의 예가 나와 있습니다. 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    

```json  

{  
  "id": "urn:ngsi-ld:OriginDestinationFlow:PT:CO0101:CO0102:DE:20241231T10",  
  "type": "OriginDestinationFlow",  
  "dateObserved": {  
    "type": "DateTime",  
    "value": "2024-12-31T10:30:00.00Z"  
  },  
  "aggregationDateType": {  
    "type": "Text",  
    "value": "hourly"  
  },  
  "hour": {  
    "type": "Number",  
    "value": 10  
  },  
  "originLocationCode": {  
    "type": "Text",  
    "value": "CO0101"  
  },  
  "originLocationName": {  
    "type": "Text",  
    "value": "Coimbra"  
  },  
  "destinationLocationCode": {  
    "type": "Text",  
    "value": "CO0102"  
  },  
  "destinationLocationName": {  
    "type": "Text",  
    "value": "Figueira da Foz"  
  },  
  "nationality": {  
    "type": "Text",  
    "value": "DE"  
  },  
  "nationalityName": {  
    "type": "Text",  
    "value": "Germany"  
  },  
  "flowCount": {  
    "type": "Number",  
    "value": 145  
  },  
  "flowType": {  
    "type": "Text",  
    "value": "tourism"  
  },  
  "countryCode": {  
    "type": "Text",  
    "value": "PT"  
  },  
  "originLocation": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -8.4103,  
        40.2033  
      ]  
    }  
  },  
  "destinationLocation": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -8.8618,  
        40.1508  
      ]  
    }  
  },  
  "description": {  
    "type": "Text",  
    "value": "Hourly visitor flow from Coimbra to Figueira da Foz (German tourists) on 2024-12-31 at 10:00-11:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "MobilityDataPlatform"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2024-12-31T11:00:00.00Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2024-12-31T11:00:00.00Z"  
  }  
}  
```  
</details>  

#### 원본목적지흐름 NGSI-LD 키-값 예시  

여기에는 JSON-LD 형식의 키-값 쌍으로 OriginDestinationFlow의 예가 나와 있습니다. 이것은 `options=keyValues`를 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    

```json  

{  
  "id": "urn:ngsi-ld:OriginDestinationFlow:PT:0602:0406:DE:20241231T10",  
  "type": "OriginDestinationFlow",  
  "dateObserved": "2024-12-31T10:00:00.00Z",  
  "aggregationDateType": "hourly",  
  "hour": 10,  
  "originLocationCode": "0602",  
  "originLocationName": "Coimbra",  
  "destinationLocationCode": "0406",  
  "destinationLocationName": "Figueira da Foz",  
  "nationality": "DE",  
  "nationalityName": "Germany",  
  "flowCount": 145,  
  "flowType": "tourism",  
  "countryCode": "PT",  
  "originLocation": {  
    "type": "Point",  
    "coordinates": [-8.4103, 40.2033]  
  },  
  "destinationLocation": {  
    "type": "Point",  
    "coordinates": [-8.8618, 40.1508]  
  },  
  "description": "Hourly visitor flow from Coimbra to Figueira da Foz (German tourists) on 2024-12-31 at 10:00-11:00",  
  "source": "MobilityDataPlatform",  
  "dateCreated": "2024-12-31T11:00:00.00Z",  
  "dateModified": "2024-12-31T11:00:00.00Z",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Transportation/master/context.jsonld"  
  ]  
}  
```  
</details>  

#### 원본목적지흐름 NGSI-LD 정규화 예시  

여기에는 JSON-LD 형식으로 정규화된 OriginDestinationFlow의 예가 있습니다. 이것은 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    

```json  

{  
  "id": "urn:ngsi-ld:OriginDestinationFlow:PT:CO0101:CO0102:DE:20241231T10",  
  "type": "OriginDestinationFlow",  
  "dateObserved": {  
    "type": "Property",  
    "value": "2024-12-31T10:30:00.00Z"  
  },  
  "aggregationDateType": {  
    "type": "Property",  
    "value": "hourly"  
  },  
  "hour": {  
    "type": "Property",  
    "value": 10  
  },  
  "originLocationCode": {  
    "type": "Property",  
    "value": "CO0101"  
  },  
  "originLocationName": {  
    "type": "Property",  
    "value": "Coimbra"  
  },  
  "destinationLocationCode": {  
    "type": "Property",  
    "value": "CO0102"  
  },  
  "destinationLocationName": {  
    "type": "Property",  
    "value": "Figueira da Foz"  
  },  
  "nationality": {  
    "type": "Property",  
    "value": "DE"  
  },  
  "nationalityName": {  
    "type": "Property",  
    "value": "Germany"  
  },  
  "flowCount": {  
    "type": "Property",  
    "value": 145  
  },  
  "flowType": {  
    "type": "Property",  
    "value": "tourism"  
  },  
  "countryCode": {  
    "type": "Property",  
    "value": "PT"  
  },  
  "originLocation": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -8.4103,  
        40.2033  
      ]  
    }  
  },  
  "destinationLocation": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -8.8618,  
        40.1508  
      ]  
    }  
  },  
  "description": {  
    "type": "Property",  
    "value": "Hourly visitor flow from Coimbra to Figueira da Foz (German tourists) on 2024-12-31 at 10:00-11:00"  
  },  
  "source": {  
    "type": "Property",  
    "value": "MobilityDataPlatform"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2024-12-31T11:00:00.00Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2024-12-31T11:00:00.00Z"  
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
  

See [FAQ 10](https://smartdatamodels.org/index.php/faqs/) to get an answer on how to deal with magnitude units  
<!-- /95-Units -->
  
<!-- 97-LastFooter -->
  
---  

[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->
  
