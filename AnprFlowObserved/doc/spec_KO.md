<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
엔티티: AnprFlowObserved  
=====================<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models//dataModel.Transportation/blob/master/AnprFlowObserved/LICENSE.md)  
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
글로벌 설명: **데이터 모델은 특정 위치 및 특정 시간에 차량의 통과와 관련된 관측을 나타냅니다. 이 데이터 모델은 ANPR 관련 속성 및 관측 이미지에 대한 링크로 확장된 [dataModel.Transportation/ItemFlowObserved]를 기반으로 합니다**.  
버전: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 속성 목록  

<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.  
- `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 국가. 예를 들어, 스페인  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 도로명 주소가 있는 지역 및 해당 지역 내 지역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 해당 지역이 위치한 지역과 해당 국가의 지역  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 지구는 일부 국가에서는 지방 정부에서 관리하는 행정 구역의 일종입니다.    
	- `postOfficeBoxNumber[string]`: 사서함 주소의 우체국 사서함 번호입니다. 예: 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 우편 번호입니다. 예: 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 거리 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 공공 도로의 특정 건물을 식별하는 번호    
- `alternateName[string]`: 이 항목의 대체 이름  - `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateObserved[date-time]`: 사용자가 정의한 관찰된 엔티티의 날짜  - `dateReceived[date-time]`: 플랫폼에서 관측을 수신한 타임스탬프  - `description[string]`: 이 항목에 대한 설명  - `id[*]`: 엔티티의 고유 식별자  - `laneId[string]`: 차선 식별자. 관찰자가 제공한 차선 식별  - `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인스트링, 다각형, 멀티포인트, 멀티라인스트링 또는 멀티폴리곤일 수 있습니다.  - `name[string]`: 이 항목의 이름  - `observedBy[*]`: 이 관찰을 보고한 주체 또는 장치  - `observedVehicle[object]`: 관찰된 차량에 대한 정보  	- `brand[object]`: 관측된 차량의 브랜드 감지    
	- `color[object]`: 관찰된 차량의 감지된 색상    
	- `country[object]`: 관측된 차량의 감지 국가    
	- `direction[string]`: 관측된 차량의 감지된 방향    
	- `licensePlate[object]`: 관찰된 차량의 번호판 감지    
	- `model[object]`: 관측된 차량의 브랜드 모델 감지    
	- `speed[number]`: 관측된 차량의 감지 속도    
- `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `refImages[array]`: 이미지를 참조하는 여러 객체의 배열  - `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `type[string]`: NGSI 엔티티 유형. AnprFlowObserved여야 합니다.  - `vehiclePlateNotRead[boolean]`: 라이선스를 읽을 수 없는지 여부를 나타냅니다.  - `zonesServed[array]`: 관측값을 수신하거나 읽을 수 있는 영역의 배열입니다.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
필수 속성  
- `dateObserved`  - `id`  - `location`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
이 데이터 모델은 경찰 문제를 다루는 스마트 애플리케이션과 관련된 주요 주체를 설명합니다. 이 엔티티 집합은 주로 자동차 및 스마트 시티 수직 세그먼트 및 관련 IoT 애플리케이션과 연관되어 있습니다. 가능한 경우 기존 schema.org 엔티티 유형 및 속성에 대한 참조가 포함되어 있습니다. 이 모델은 가능한 한 일반적이도록 고안되었기 때문에 ANPR, 궤적 제어 및 경찰 차량과 같은 다양한 경찰 부서 및 구역에서 사용할 수 있습니다.  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## 속성에 대한 데이터 모델 설명  
알파벳순으로 정렬(자세한 내용을 보려면 클릭)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
AnprFlowObserved:    
  description: 'The data model represents an observation linked to the passing of a vehicle at a certain location and at a given time. This Data Model is based on the [dataModel.Transportation/ItemFlowObserved], extended with ANPR specific properties and links to the observation images.'    
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
      description: Date of the observed entity defined by the user    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateReceived:    
      description: Timestamp when the observation has been received by the platform    
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
    laneId:    
      description: Lane identifier. Lane identification provided by the observer    
      type: string    
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
    observedBy:    
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
      description: The entity or device which has reported this observation    
      x-ngsi:    
        type: Relationship    
    observedVehicle:    
      description: Information about the observed vehicle    
      properties:    
        brand:    
          description: Detected brand of the observed vehicle    
          properties:    
            confidence:    
              description: Confidence level of the detection    
              maximum: 1    
              minimum: 0    
              type: number    
              x-ngsi:    
                type: Property    
            name:    
              description: Brand name identified    
              type: string    
              x-ngsi:    
                type: Property    
          type: object    
          x-ngsi:    
            type: Property    
        color:    
          description: Detected color of the observed vehicle    
          properties:    
            confidence:    
              description: Confidence level of the detection    
              maximum: 1    
              minimum: 0    
              type: number    
              x-ngsi:    
                type: Property    
            name:    
              description: Color name    
              type: string    
              x-ngsi:    
                type: Property    
          type: object    
          x-ngsi:    
            type: Property    
        country:    
          description: Detected country of the observed vehicle    
          properties:    
            code:    
              description: Country code according to ISO 3166-1 alpha-2    
              type: string    
              x-ngsi:    
                type: Property    
            confidence:    
              description: Confidence level of the detection    
              maximum: 1    
              minimum: 0    
              type: number    
              x-ngsi:    
                type: Property    
          type: object    
          x-ngsi:    
            type: Property    
        direction:    
          description: Detected direction of the observed vehicle    
          enum:    
            - away    
            - towards    
          type: string    
          x-ngsi:    
            type: Property    
        licensePlate:    
          description: Detected license plate of the observed vehicle    
          properties:    
            confidence:    
              description: Confidence level of the detection    
              maximum: 1    
              minimum: 0    
              type: number    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: 'Sequence of position points describing this location, expressed in coordinate system'    
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
                type: Property    
            identifier:    
              description: License plate identifier    
              type: string    
              x-ngsi:    
                type: Property    
          type: object    
          x-ngsi:    
            type: Property    
        model:    
          description: Detected brand model of the observed vehicle    
          properties:    
            confidence:    
              description: Confidence level of the detection    
              maximum: 1    
              minimum: 0    
              type: number    
              x-ngsi:    
                type: Property    
            name:    
              description: Model name    
              type: string    
              x-ngsi:    
                type: Property    
          type: object    
          x-ngsi:    
            type: Property    
        speed:    
          description: Detected speed of the observed vehicle    
          minimum: 0    
          type: number    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
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
    refImages:    
      description: Array of multiple objects that refer to images    
      items:    
        properties:    
          contentType:    
            description: Content type according to IANA Media Types    
            type: string    
            x-ngsi:    
              type: Property    
          imageType:    
            description: Type of image    
            enum:    
              - plate    
              - overview    
              - anpr    
            type: string    
            x-ngsi:    
              type: Property    
          url:    
            description: URL referencing to the image    
            format: uri    
            type: string    
            x-ngsi:    
              type: Property    
        type: object    
      type: array    
      x-ngsi:    
        type: Relationship    
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
    type:    
      description: NGSI Entity type. It has to be AnprFlowObserved    
      enum:    
        - AnprFlowObserved    
      type: string    
      x-ngsi:    
        type: Property    
    vehiclePlateNotRead:    
      description: Indicates if a license could not be read    
      type: boolean    
      x-ngsi:    
        type: Property    
    zonesServed:    
      description: Array of zones that are able to receive or read the observations    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - location    
    - dateObserved    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2024 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Transportation/blob/master/AnprFlowObserved/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Transportation/AnprFlowObserved/schema.json    
  x-model-tags: ""    
  x-version: 0.0.2    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 페이로드 예시  
#### AnprFlowObserved NGSI-v2 키 값 예시  
다음은 키 값으로 JSON-LD 형식의 AnprFlowObserved의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "anprFlowObserved:LEZ-Noorderlaan",  
  "type": "AnprFlowObserved",  
  "address": {  
    "addressCountry": "BE",  
    "addressLocality": "Antwerp",  
    "streetAddress": "Noorderlaan"  
  },  
  "dateObserved": "2022-09-01T16:30:00Z",  
  "dateReceived": "2022-09-01T16:35:00Z",  
  "observedBy": "ANPR1_Noorderlaan",  
  "laneId": "ABC123",  
  "areaServed": "Antwerp",  
  "zonesServed": [  
    "Antwerp"  
  ],  
  "vehiclePlateNotRead": false,  
  "observedVehicle": {  
    "direction": "towards",  
    "speed": 50,  
    "brand": {  
      "name": "Audi",  
      "confidence": 0.97  
    },  
    "model": {  
      "name": "A3",  
      "confidence": 0.98  
    },  
    "color": {  
      "name": "black",  
      "confidence": 0.95  
    },  
    "country": {  
      "code": "BE",  
      "confidence": 0.95  
    },  
    "licensePlate": {  
      "identifier": "1-ABC-123",  
      "confidence": 0.96  
    }  
  },  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -56.6404505,  
      168.370658  
    ]  
  },  
  "refImages": [  
    {  
      "contentType": "image/jpg",  
      "imageType": "anpr",  
      "url": "urn:ngsi-ld:ANPR:items:123"  
    }  
  ]  
}  
```  
</details>  
#### AnprFlowObserved NGSI-v2 정규화 예제  
다음은 정규화된 JSON-LD 형식의 AnprFlowObserved의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "anprFlowObserved:LEZ-Noorderlaan",  
  "type": "AnprFlowObserved",  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "addressCountry": "BE",  
      "addressLocality": "Antwerp",  
      "streetAddress": "Noorderlaan"  
    }  
  },  
  "dateObserved": {  
    "type": "DateTime",  
    "value": "2022-09-01T16:30:00Z"  
  },  
  "laneId": {  
    "type": "Text",  
    "value": "ABC123"  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Antwerp"  
  },  
  "zonesServed": {  
    "type": "StructuredValue",  
    "value": [  
      "Antwerp"  
    ]  
  },  
  "vehiclePlateNotRead": {  
    "type": "Boolean",  
    "value": false  
  },  
  "observedVehicle": {  
    "type": "StructuredValue",  
    "value": {  
      "direction": "towards",  
      "speed": 50,  
      "brand": {  
        "name": "Audi",  
        "confidence": 0.97  
      },  
      "model": {  
        "name": "A3",  
        "confidence": 0.98  
      },  
      "color": {  
        "name": "black",  
        "confidence": 0.95  
      },  
      "country": {  
        "code": "BE",  
        "confidence": 0.95  
      },  
      "licensePlate": {  
        "identifier": "1-ABC-123",  
        "confidence": 0.96  
      }  
    }  
  },  
  "refImages": {  
    "type": "StructuredValue",  
    "value": [  
      {  
        "url": "s3://bucket/object-xxx-plate",  
        "contentType": "image/jpg",  
        "imageType": "anpr"  
      }  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "coordinates": [  
        -56.6404505,  
        168.370658  
      ],  
      "type": "Point"  
    }  
  }  
}  
```  
</details>  
#### AnprFlowObserved NGSI-LD 키 값 예시  
다음은 키 값으로 JSON-LD 형식의 AnprFlowObserved의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "anprFlowObserved:LEZ-Noorderlaan",  
  "type": "AnprFlowObserved",  
  "address": {  
    "addressCountry": "BE",  
    "addressLocality": "Antwerp",  
    "streetAddress": "Noorderlaan"  
  },  
  "dateObserved": "2022-09-01T16:30:00Z",  
  "dateReceived": "2022-09-01T16:35:00Z",  
  "observedBy": "ANPR1_Noorderlaan",  
  "laneId": "ABC123",  
  "areaServed": "Antwerp",  
  "zonesServed": [  
    "Antwerp"  
  ],  
  "vehiclePlateNotRead": false,  
  "observedVehicle": {  
    "direction": "towards",  
    "speed": 50,  
    "brand": {  
      "name": "Audi",  
      "confidence": 0.97  
    },  
    "model": {  
      "name": "A3",  
      "confidence": 0.98  
    },  
    "color": {  
      "name": "black",  
      "confidence": 0.95  
    },  
    "country": {  
      "code": "BE",  
      "confidence": 0.95  
    },  
    "licensePlate": {  
      "identifier": "1-ABC-123",  
      "confidence": 0.96  
    }  
  },  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -56.6404505,  
      168.370658  
    ]  
  },  
  "refImages": [  
    {  
      "contentType": "image/jpg",  
      "imageType": "anpr",  
      "url": "urn:ngsi-ld:ANPR:items:123"  
    }  
  ],  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Transportation/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### AnprFlowObserved NGSI-LD 정규화 예제  
다음은 정규화된 JSON-LD 형식의 AnprFlowObserved의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "anprFlowObserved:LEZ-Noorderlaan",  
  "type": "AnprFlowObserved",  
  "address": {  
    "type": "Property",  
    "value": {  
      "addressCountry": "BE",  
      "addressLocality": "Antwerp",  
      "streetAddress": "Noorderlaan"  
    }  
  },  
  "dateObserved": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2022-09-01T16:30:00Z"  
    }  
  },  
  "laneId": {  
    "type": "Property",  
    "value": "ABC123"  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Antwerp"  
  },  
  "zonesServed": {  
    "type": "Property",  
    "value": {  
      "type": "string",  
      "coordinates": [  
        "Antwerp"  
      ]  
    }  
  },  
  "vehiclePlateNotRead": {  
    "type": "Property",  
    "value": false  
  },  
  "observedVehicle": {  
    "type": "Property",  
    "value": {  
      "direction": "towards",  
      "speed": 50,  
      "brand": "Audi",  
      "model": "A3",  
      "color": "black",  
      "country": "BE",  
      "licensePlate": "1-ABC-123"  
    }  
  },  
  "refImages": {  
    "type": "Property",  
    "value": [  
      {  
        "type": "s3://bucket/object-xxx-plate",  
        "contentType": "image/jpg",  
        "imageType": "anpr"  
      }  
    ]  
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
규모 단위를 다루는 방법에 대한 답변은 [FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하세요.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
