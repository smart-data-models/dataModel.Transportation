<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
엔티티: APDSObservation  
====================<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models//dataModel.Transportation/blob/master/APDSObservation/LICENSE.md)  
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
전역 설명: **이 엔티티는 ANPR 카메라 세트의 특정 관측을 모델링합니다. 관찰은 여러 대의 ANPR 카메라로 수행될 수 있지만, 한 대의 차량 관찰로 제한됩니다. APDS 데이터 모델 https://www.allianceforparkingdatastandards.org/**을 구현합니다.  
버전: 0.0.1  
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
- `alternateName[string]`: 이 항목의 대체 이름  - `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `creator[string]`: 현재 드라이버의 ID입니다.  - `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `id[*]`: 엔티티의 고유 식별자  - `images[array]`: 이미지에 대한 링크 배열입니다. 배열 요소에는 이미지의 URL과 추가 정보가 포함됩니다. 이미지 URL 대신 이미지 자체를 binaryContent 속성에 포함할 수 있습니다.  - `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.  - `name[string]`: 이 항목의 이름  - `observationDateTime[date-time]`: 관찰이 이루어진 타임스탬프(UTC)입니다. 관찰 시작 날짜 시간 및 관찰 종료 날짜 시간을 사용하지 않는 경우 필수입니다.  - `observationEndDateTime[date-time]`: 관찰 이벤트가 종료된 날짜와 시간(UTC 기준)(예: 오전 9시 33분에 차량이 배송 구역을 빠져나가는 것이 관찰됨). 생성 날짜/시간을 사용하지 않는 경우 필수입니다.  - `observationStartDateTime[date-time]`: 관측이 시작된 날짜와 시간(UTC 기준) 이벤트입니다(예: 오전 8:01에 차량이 배송 구역에 진입하는 것이 관측됨). 생성 날짜/시간을 사용하지 않는 경우 필수입니다.  - `observedCredentialCharacterConfidence[array]`: 개별 문자 인식의 신뢰도입니다. 관찰된 자격증명 신뢰도와 마찬가지로 공급업체에 따라 다릅니다. 메타데이터를 사용하여 신뢰도를 해석할 수 있는 방법을 나타냅니다.  - `observedCredentialConfidence[number]`: 측정의 전반적인 신뢰도입니다. 이 값은 공급업체에 따라 다를 수 있지만 항상 0에서 1 사이의 값으로 재조정되어야 합니다. 메타데이터를 사용하여 이 숫자를 어떻게 해석해야 하는지 표시하세요. Arvoo: 범위[0.0, 1.0](높을수록 좋음).  - `observedCredentialCountry[string]`: 2자 ISO3166 표준을 따르는 국가 코드(https://www.iban.com/country-codes). 모호성을 피하기 위해 국제 차량 등록 코드를 사용해서는 안 됩니다(https://en.wikipedia.org/wiki/International_vehicle_registration_code). 국가 코드를 확인할 수 없는 경우 이 속성에 대해 'XX'를 설정합니다.  - `observedCredentialId[string]`: 참조된 관찰된 자격 증명에 대한 특정 식별자입니다. 자격 증명은 관찰된 자격 증명 유형으로 지정되며 RFID 태그, 결제 스테이션의 티켓 번호, 번호판 번호 등이 될 수 있습니다. 번호판의 경우 영숫자 값(공백이나 하이픈 없음)만 허용됩니다. 선택적으로 ':'를 사용하여 독일 도시 인장(https://www.europeanplates.com/information/german-city-codes.html)과 같은 위치를 표시할 수 있습니다.  - `observedCredentialType[string]`: 관찰 내에서 참조된 자격 증명 유형입니다. 허용되는 값은 APDS CredentialType에 지정되어 있습니다. 열거형: '바코드, 블루투스, 전자티켓, 행택, 번호판, 허가증, qrCode, RFID, 티켓, 기타'  - `observedHeading[*]`: 관측자의 진행 방향을 나타내며 소수점으로 지정되며, 0 <= '방향' < 360, 진북을 기준으로 시계 방향으로 계산, 차량이 정지한 경우(즉, '속도' 속성 값이 '0') 방향 속성 값은 '-1'과 같아야 합니다. (UN 코드 DD)  . Model: [https://schema.org/Number](https://schema.org/Number)- `observedLocation`:   	- `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)  
	- `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.    
- `observedLocationPDOP[number]`: 관측된 차량의 GPS 위치 정확도. 이는 '위치 희석 정밀도'(https: //en.wikipedia.org/wiki/Dilution_of_precision_(navigation))로 표현됩니다. (UN 코드 'MTR').  - `observedMethod[string]`: APDS에 정의된 대로 이 관찰 요소에 대해 기록된 관찰 방법(ObservationType)입니다. 열거형: 'anpr, 초크, 시각, 스캐너, rfTranspoder, 기타'  - `observedSpeed[*]`: 관측된 차량 현재 속도의 수평 성분의 크기를 나타내며 시속 킬로미터 단위로 지정됩니다. 속도 속성의 값은 음수가 아닌 실수여야 하며, 어떤 이유로 인해 일시적으로 속도를 알 수 없는 경우 '-1'을 사용할 수 있습니다. (UN 코드 KMH).  . Model: [https://schema.org/Number](https://schema.org/Number)- `observedVehicleColour[string]`: 관찰된 차량의 색상  - `observedVehicleMake[string]`: 관찰된 차량의 제조사  - `observedVehicleType[string]`: 구조적 특성의 관점에서 본 차량 유형. 이는 차량 카테고리와는 다릅니다. Enum:'농업용차량, 모든차량, 굴절식차량, 자전거, 빈트롤리, 버스, 자동차, 카라반, 자동차Or경량차량, 자동차With카라반, 자동차With트레일러, 청소트롤리, 건설용차량, 4륜구동, 하이사이드차량, 트럭, 미니버스, 오토바이, 오토바이, 모터사이클, 모터스쿠터, 청소차, 유조차, 삼륜차, 트레일러, 트램, 이륜차, 트롤리, 밴, 차량무촉매변환기, 차량위드카라반, 차량위드트레일러, 짝수번호등록번호판, 홀수번호등록번호판, 기타'. DATEX 2 버전 2.3](http://d2docs.ndwcloud.nu/_static/umlmodel/v2.3/index.htm)에서 정의하고 다른 용도로 확장된 _VehicleTypeEnum_ 및 _VehicleTypeEnum2_에 의해 정의된 다음 값  . Model: [https://schema.org/Text](https://schema.org/Text)- `observer[string]`: 이 관찰 요소에 기록된 관찰을 수행하는 스캐닝 시스템의 이름 또는 식별자입니다.  - `observerCameras[array]`: 차량을 감지한 카메라 위치의 배열로, 목록에서 첫 번째 카메라의 인식률이 가장 높습니다. 다음 약어를 사용하여 차량의 카메라 위치를 표시합니다: RF(오른쪽 전면), RM(오른쪽 중앙), RB(오른쪽 후면), LF(왼쪽 전면), LM(왼쪽 중앙), LB(왼쪽 후면).  - `observerDescription[string]`: 관찰 또는 관찰자에 대한 세부 사항을 설명하는 자유 텍스트 설명입니다. 예를 들어 특정 ANPR 스캔 차량의 친근한 이름으로 사용할 수 있습니다.  - `observerHeading[*]`: 관측자의 이동 방향을 나타내며 소수점으로 지정되며, 0 <= '방향' < 360, 진북을 기준으로 시계 방향으로 계산합니다. 차량이 정지 상태인 경우(즉, '속도' 속성의 값이 '0'인 경우), 방향 속성 값은 '-1'이어야 합니다.  . Model: [https://schema.org/Number](https://schema.org/Number)- `observerLocation`:   	- `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)  
	- `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.    
- `observerLocationPDOP[number]`: '위치 희석 정밀도'로 표현되는 관측자의 GPS 위치 정확도(https: //en.wikipedia.org/wiki/Dilution_of_precision_(navigation))  - `observerSpeed[*]`: 관측자 현재 속도의 수평 성분의 크기를 나타내며 시간당 킬로미터 단위로 지정됩니다. 제공된 경우 속도 속성의 값은 음수가 아닌 실수여야 합니다. 어떤 이유로 일시적으로 속도를 알 수 없는 경우 '-1'을 사용할 수 있습니다.  . Model: [https://schema.org/Number](https://schema.org/Number)- `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `towardsObserver[number]`: 1: 관찰된 차량이 카메라 방향으로 이동, 0: 관찰된 차량이 카메라 방향에서 멀어짐, -1: 관찰된 차량 방향이 감지되지 않음.  - `type[string]`: NGSI 엔티티 유형. APDSObservation이어야 합니다.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
필수 속성  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
이 모델은 특정 위치에서 특정 시간에 차량을 관찰한 데이터 세트를 캡처합니다. 이 모델은 APDS(Alliance for Parking DataStandard) 사양에서 파생되었습니다. 관찰 방법에는 ALPR 카메라, 육안 관찰, 스캐너 또는 기타 관찰 수단의 사용이 포함됩니다.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 속성에 대한 데이터 모델 설명  
알파벳순으로 정렬(자세한 내용을 보려면 클릭)  
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
## 페이로드 예시  
#### APDSObservation NGSI-v2 키-값 예시  
다음은 키 값으로 JSON-LD 형식의 APDSObservation의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
#### APDSObservation NGSI-v2 정규화 예제  
다음은 정규화된 JSON-LD 형식의 APDSObservation의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
#### APDSObservation NGSI-LD 키-값 예시  
다음은 키 값으로 JSON-LD 형식의 APDSObservation의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
#### APDSObservation NGSI-LD 정규화 예제  
다음은 정규화된 JSON-LD 형식의 APDSObservation의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
10](https://smartdatamodels.org/index.php/faqs/)를 참조하여 규모 단위를 다루는 방법에 대한 답변을 확인하세요.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
