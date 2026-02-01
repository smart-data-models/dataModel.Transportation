<!-- 10-Header -->
  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

엔티티: Vehicle  
===============
<!-- /10-Header -->
  
<!-- 15-License -->
  

[오픈 라이선스](https://github.com/smart-data-models//dataModel.Transportation/blob/master/Vehicle/LICENSE.md)  

[자동으로 생성된 문서](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->
  
<!-- 20-Description -->
  

Global description: **이 엔티티는 특정 차량 모델을 모델링하며, 그러한 모델에 속하는 여러 차량 인스턴스에 공통인 모든 속성을 포함한다.**  

version: 0.2.2  
<!-- /20-Description -->
  
<!-- 30-PropertiesList -->
  


## 속성 목록  


<sup><sub>[*] 속성에 유형이 없다면, 그것은 여러 유형이나 서로 다른 형식/패턴을 가질 수 있기 때문입니다.</sub></sup>  
- `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)  
	- `addressCountry[string]`: 그 국가. 예를 들어 스페인  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: 그 거리 주소가 속한 지역 및 그 지역에 있는  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: 그 지역은 지자체가 위치하고 있으며, 그 국가에 있습니다  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: 구는 일부 국가에서 지방 정부가 관리하는 유형의 행정 구역입니다  
	- `postOfficeBoxNumber[string]`: 우체국 사서함 번호(PO 박스 주소용). 예를 들어, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: 우편번호. 예를 들어, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: 도로 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
	- `streetNr[string]`: 공공 도로상 특정 부동산을 식별하는 번호  
- `alternateName[string]`: 이 항목의 대체 이름  
- `annotations[array]`: 아이템에 대한 주석  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `areaServed[string]`: 서비스나 제공되는 항목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `battery[number]`: 전기 자동차의 경우 남은 배터리 백분율 또는 차량에 연결된 장치  
- `bearing[number]`: 차량의 GPS 각도를 真北에서 시계 방향으로 측정한 값을 반환한다. GTFS 실시간 메시지의 Position(https://developers.google.com/transit/gtfs-realtime/reference#message-position) 필드의 'bearing'과 동일하다.  . Model: [https://schema.org/Number](https://schema.org/Number)  
- `cargoWeight[number]`: 차량의 화물 현재 무게  . Model: [https://schema.org/Number](https://schema.org/Number)  
- `category[array]`: 외부의 관점에서 차량 카테고리. 이것은 차량 유형(차, 트럭 등)과는 다르며, `vehicleType` 속성으로 표현된다. Enum: 'municipalServices, nonTracked, private, public, specialUsage, tracked'. 추적 가능한 차량은 원격 시스템에 의해 항상 위치가 추적되는 차량이다. 또는 애플리케이션이 필요로 하는 다른 것들. 위치, 속도, 방향 등을 주기적으로 업데이트하기 위해 GPS 수신기와 네트워크 연결을 함께 통합한다.  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `color[string]`: 제품의 색상  . Model: [https://schema.org/color](https://schema.org/color)  
- `currentTripCount[number]`: 해당 관측값에 해당하는 차량이 운행일에 수행한 여행의 현재 수  . Model: [https://schema.org/Number](https://schema.org/Number)  
- `dataProvider[string]`: 조화된 데이터 엔티티의 제공자를 식별하는 문자열 시퀀스  
- `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 저장소 플랫폼에 의해 할당됩니다.  
- `dateFirstUsed[date]`: 처음 사용된 시점을 나타내는 타임스탬프  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)  
- `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프. 이는 일반적으로 저장 플랫폼에 의해 할당됨  
- `dateVehicleFirstRegistered[date]`: 차량이 해당 공공기관에 최초로 등록된 날짜  . Model: [https://schema.org/dateVehicleFirstRegistered](https://schema.org/dateVehicleFirstRegistered)  
- `description[string]`: 이 항목에 대한 설명  
- `deviceBatteryStatus[string]`: 리포팅 장치의 배터리 충전 상태를 제공합니다. Enum: '연결됨, 연결안됨'  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `deviceSimNumber[string]`: 차량의 기기에서 SIM 번호를 제공합니다  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `emergencyVehicleType[string]`: 이 관찰에 해당하는 긴급 차량의 유형. Enum: '경찰차, 경찰모터사이클, 경찰밴, 경찰SWAT, 소방차, 소화차, 공중구급차, 구급차, 모터사이클구급차, 구조차, 위험물처리차, 견인차  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `feature[array]`: 차량에 통합된 기능. Enum: 'abs, 에어백, 경보, 후방카메라, 장애인 램프, gps, 인터넷 연결, 과속, 근접 센서, wifi'. 또는 애플리케이션에서 필요한 기타 항목. 여러 기능의 인스턴스를 나타내는 데에는 다음 구문을 사용할 수 있다: `<기능>,<발생 횟수>`. 예를 들어, 4개의 에어백이 있는 차량은 `에어백,4`로 표시된다.  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `fleetVehicleId[string]`: 그것이 속한 차량 대의 맥락에서 차량의 식별자  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `fuelEfficiency[number]`: 연료 사용량 당 이동한 거리, 일반적으로 리터당 킬로미터(km/L)로 표시된다.  . Model: [https://schema.org/Number](https://schema.org/Number)  
- `fuelFilled[number]`: 이 관찰에 해당하는 차량에 채워진 연료의 리터 단위 количе  . Model: [https://schema.org/Number](https://schema.org/Number)  
- `fuelType[string]`: 이 관찰에 해당하는 차량의 엔진 또는 엔진에 적합한 연료의 유형  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `heading[*]`: 차량의 이동 방향을 나타내며, 10진도 단위로 지정되며, 0 <= `heading` < 360이며, 진북을 기준으로 시계 방향으로 계산된다. 차량이 정지해 있는 경우(즉, `speed` 속성의 값이 `0`인 경우), `heading` 속성의 값은 `-1`과 같아야 한다.  . Model: [https://schema.org/Number](https://schema.org/Number)  
- `id[*]`: 개체의 고유 식별자  
- `ignitionStatus[boolean]`: 차량의 점화 상태를 반환합니다. True는 점화된 것을 의미합니다.  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)  
- `image[uri]`: 아이템의 이미지  . Model: [https://schema.org/URL](https://schema.org/URL)  
- `license_plate[string]`: 차량의 번호판 번호를 제공합니다. SameAs: GTFS 실시간 메시지-VehicleDescriptor의 license_plate 필드(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `location[*]`: Geojson 아이템 참조입니다. Point, LineString, Polygon, MultiPoint, MultiLineString 또는 MultiPolygon 중 하나일 수 있습니다.  
- `mileageFromOdometer[number]`: 초기 생산 이후 특정 차량이 이동한 총 거리로서, 그것의 속도계에서 읽은 거리  . Model: [https://schema.org/mileageFromOdometer](https://schema.org/mileageFromOdometer)  
- `municipalityInfo[object]`: 이 관측에 해당하는 자치체 정보  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `cityId[string]`: 이 관측에 해당하는 도시 ID  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `cityName[string]`: 이 관측에 해당하는 도시 이름  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `district[string]`: 이 관측에 해당하는 지구 이름  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `stateName[string]`: 이 관찰에 해당하는 주의 이름  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `ulbName[string]`: 이 관찰에 해당하는 도시 지역 단체의 이름  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `wardId[string]`: 이 관찰에 해당하는 Ward ID  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `wardName[string]`: 이 관찰에 해당하는 구 이름  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `wardNum[number]`: 이 관찰에 해당하는 구 번호  . Model: [https://schema.org/Number](https://schema.org/Number)    
	- `zoneId[string]`: 이 관측에 해당하는 존 ID  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `zoneName[string]`: 이 관측에 해당하는 구역 이름  . Model: [https://schema.org/Text](https://schema.org/Text)    
- `name[string]`: 이 항목의 이름  
- `observationDateTime[date-time]`: 최종 관측 보고 시간  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)  
- `owner[array]`: 소유자(들)의 고유 ID를 참조하는 문자열 시퀀스를 JSON으로 인코딩한 문자열을 포함하는 목록  
- `previousLocation[*]`: Geojson 아이템 참조입니다. Point, LineString, Polygon, MultiPoint, MultiLineString 또는 MultiPolygon 일 수 있습니다.  
- `purchaseDate[date-time]`: 현재 소유자가 차량 등을 구입한 날짜  . Model: [https://schema.org/purchaseDate](https://schema.org/purchaseDate)  
- `refVehicleModel[*]`: 차량 모델 참조  . Model: [https://schema.org/URL](https://schema.org/URL)  
- `reportId[string]`: 이 관찰에 해당하는 문제 또는 보고서 또는 피드백 또는 트랜잭션에 할당된 고유 ID  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `seeAlso[*]`: 아이템에 대한 추가 리소스를 가리키는 URI 목록  
- `serviceOnDuty[boolean]`: 이 관찰에 해당하는 응급 차량이 제공하는 서비스의 특성. True는 이 관찰에 해당하는 응급 차량이 응급 호출에 출동하여 서비스를 제공하고 있음을 나타내며, False는 그렇지 않음을 나타낸다.  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)  
- `serviceProvided[array]`: 차량이 제공할 수 있는 서비스 또는 할당된 서비스. Enum: 'auxiliaryServices, cargoTransport, construction, fairground, garbageCollection, goodsSelling, maintenance, parksAndGardens, roadSignalling, specialTransport, streetCleaning, streetLighting, urbanTransit, wasteContainerCleaning'. 또는 특정 애플리케이션이 필요로 하는 다른 값  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `serviceStatus[string]`: 차량 상태(제공되는 서비스의 관점에서 볼 때, 따라서 개인 차량에는 적용되지 않을 수 있음).
`parked` : 차량이 주차되어 있으며 현재 서비스를 제공하지 않고 있음.
`onRoute` : 차량이 임무를 수행 중임. 쉼표로 구분된 수정자(modifier)를 추가하여 현재 차량이 수행 중인 임무를 나타낼 수 있음. 예를 들어, `onRoute,garbageCollection`은 차량이 이동 중이며 쓰레기 수집 임무를 수행 중임을 나타낼 수 있음.
`broken` : 차량이 일시적인 고장을 겪고 있음.
`outOfService` : 차량이 도로에 있지만 임무를 수행하지 않고 있으므로 아마도 주차 구역으로 이동 중임.
Enum: 'broken, onRoute, outOfService, parked'  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)  
- `source[string]`: 엔티티 데이터의 원래 출처를 URL로 제공하는 문자열 시퀀스. 출처 제공자의 완전히 정규화된 도메인 이름이나 출처 개체에 대한 URL로 지정하는 것을 권장합니다.  
- `speed[*]`: 차량의 현재 속도의 수평 성분의 크기를 나타내며, 킬로미터당 시간으로 지정된다. 제공되는 경우, 속도 속성의 값은 음이 아닌 실수여야 한다. 일시적으로 어떤 이유로 속도가 알 수 없을 때는 `-1`을 사용할 수 있다.  . Model: [https://schema.org/Number](https://schema.org/Number)  
- `tripNetWeightCollected[number]`: 이 관찰에 해당하는 차량이 여행의 끝에 수집한 순중량  . Model: [https://schema.org/Number](https://schema.org/Number)  
- `type[string]`: NGSI 엔티티 유형. 차량이어야 합니다.  
- `vehicleAltitude[string]`: GPS를 이용하여 차량의 현재 고도를 제공합니다.  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `vehicleConfiguration[string]`: 차량의 구성에 대한 짧은 텍스트, 예를 들어 '5도어 해치백 ST 2.5 MT 225 마력' 또는 '한정판'  . Model: [https://schema.org/vehicleConfiguration](https://schema.org/vehicleConfiguration)  
- `vehicleIdentificationNumber[string]`: 차량 식별 번호(Vehicle Identification Number, VIN)는 자동차 산업에서 개별 자동차를 식별하기 위해 사용되는 고유한 일련 번호이다.  . Model: [https://schema.org/vehicleIdentificationNumber](https://schema.org/vehicleIdentificationNumber)  
- `vehiclePlateIdentifier[string]`:  차량 등록증에 부착되어 공식적인 식별 목적으로 사용되는 차량 등록 번호판에 표시된 식별자 또는 코드이다. 등록 식별자는 숫자 또는 영숫자이며 발급 기관의 지역 내에서 고유하다. 규범적 참조: DATEXII `vehicleRegistrationPlateIdentifier`  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `vehicleRunningStatus[string]`: 리포팅 장치의 배터리 충전 상태를 제공합니다. Enum: '실행중, 대기중, 중지됨'  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `vehicleSpecialUsage[string]`: 차량이 상업용 렌탈, 운전 학교 또는 택시와 같은 특별한 용도로 사용되었는지 여부를 나타냅니다. 많은 국가의 법률은 차량을 판매할 때 이 정보를 공개하도록 요구합니다. Enum: '구급차, 소방대, 군대, 경찰, 학교 교통, 택시, 쓰레기 관리'  . Model: [https://schema.org/vehicleSpecialUsage](https://schema.org/vehicleSpecialUsage)  
- `vehicleTrackerDevice[string]`: 이 관찰에 해당하는 차량에 장착된 GPS 장치 또는 추적 장치의 설치 상태  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `vehicleType[string]`: 차량의 구조적 특성으로 본 차량의 유형입니다. 이것은 차량 카테고리와 다릅니다. Enum: '농업용차량, 모든차량, 관절차량, 자전거, 쓰레기통, 버스, 자동차, 카라반, 자동차 또는 경차, 카라반을 끄는 자동차, 트레일러를 끄는 자동차, 청소용 수레, 건설 또는 유지 보수 차량, 4륜구동, 높은 측면 차량, 트럭, 미니버스, 모ペ드, 오토바이, 사이드카가 있는 오토바이, 모터스쿠터, 청소기, 탱크로리, 3륜차, 트레일러, 전차, 2륜차, 수레, 밴, 촉매 변환기가 없는 차량, 카라반을 끄는 차량, 트레일러를 끄는 차량, 짝수 번호판이 있는 차량, 홀수 번호판이 있는 차량, 기타'. 다음 값은 _VehicleTypeEnum_ 및 _VehicleTypeEnum2_에 의해 정의되며, [DATEX 2 버전 2.3](http://d2docs.ndwcloud.nu/_static/umlmodel/v2.3/index.htm) 및 기타 용도로 확장됩니다.  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `wardId[string]`: 이 관찰에 해당하는 엔티티의 워드 ID  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `wardName[string]`: 이 관찰에 해당하는 엔티티의 구 이름  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `zoneName[string]`: 이 관찰에 해당하는 엔티티의 존 이름  . Model: [https://schema.org/Text](https://schema.org/Text)  
<!-- /30-PropertiesList -->
  
<!-- 35-RequiredProperties -->
  

필수 속성  
- `카테고리`  
- `id`  
- `위치`  
- `유형`  
- `차량 유형`  
<!-- /35-RequiredProperties -->
  
<!-- 40-NotesYaml -->
  
<!-- /40-NotesYaml -->
  
<!-- 50-DataModelHeader -->
  

## 데이터 모델 속성 설명  

가나다순으로 정렬 (자세한 정보 클릭)  
<!-- /50-DataModelHeader -->
  
<!-- 60-ModelYaml -->
  
<details><summary><strong>full yaml details</strong></summary>    

```yaml  
Vehicle:    
  description: This entity models a particular vehicle model, including all properties which are common to multiple vehicle instances belonging to such model.    
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
    alternateName:    
      description: An alternative name for this item    
      type: string    
      x-ngsi:    
        type: Property    
    annotations:    
      description: Annotations about the item    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    battery:    
      description: The current percentage of battery left in case of an electric vehicle, or a device connected to the vehicle    
      maximum: 1    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    bearing:    
      description: Gives the vehicle GPS angle measured in a clockwise direction from the True North. SameAs 'bearing' field from GTFS Realtime message-Position(https://developers.google.com/transit/gtfs-realtime/reference#message-position)    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    cargoWeight:    
      description: Current weight of the vehicle's cargo    
      exclusiveMinimum: 0    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Kilograms    
    category:    
      description: Vehicle category(ies) from an external point of view. This is different than the vehicle type (car, lorry, etc.) represented by the `vehicleType` property. Enum:'municipalServices, nonTracked, private, public, specialUsage, tracked'. Tracked vehicles are those vehicles which position is permanently tracked by a remote system. Or any other needed by an application They incorporate a GPS receiver together with a network connection to periodically update a reported position (location, speed, heading ...)    
      items:    
        enum:    
          - municipalServices    
          - nonTracked    
          - private    
          - public    
          - specialUsage    
          - tracked    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    color:    
      description: The color of the product    
      type: string    
      x-ngsi:    
        model: https://schema.org/color    
        type: Property    
    currentTripCount:    
      description: The current count of trips made by the vehicle corresponding to this observation on the given day of operation    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
    dateFirstUsed:    
      description: Timestamp which denotes when the vehicle was first used    
      format: date    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateVehicleFirstRegistered:    
      description: The date of the first registration of the vehicle with the respective public authorities    
      format: date    
      type: string    
      x-ngsi:    
        model: https://schema.org/dateVehicleFirstRegistered    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    deviceBatteryStatus:    
      description: Gives the Battery charging status of the reporting device. Enum:'connected, disconnected'    
      enum:    
        - connected    
        - disconnected    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    deviceSimNumber:    
      description: Gives the SIM number of the device in the vehicle    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    emergencyVehicleType:    
      description: Type of emergency vehicle corresponding to this observation. Enum:'policeCar, policeMotorcycle, policeVan, policeSWAT, fireEngine, waterTender, airAmbulance, ambulance, motorcycleAmbulance, rescueVehicle, hazardousMaterialsApparatus, towTruck    
      enum:    
        - policeCar    
        - policeMotorcycle    
        - policeVan    
        - policeSWAT    
        - fireEngine    
        - waterTender    
        - airAmbulance    
        - ambulance    
        - motorcycleAmbulance    
        - rescueVehicle    
        - hazardousMaterialsApparatus    
        - towTruck    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    feature:    
      description: 'Feature(s) incorporated by the vehicle. Enum:'' abs, airbag, alarm, backCamera, disabledRamp, gps, internetConnection, overspeed, proximitySensor, wifi''. Or any other needed by the application. In order to represent multiple instances of a feature it can be used the following syntax: `<feature>,<occurences>`. For example, a car with 4 airbags will be represented by `airbag,4`'    
      items:    
        enum:    
          - abs    
          - airbag    
          - alarm    
          - backCamera    
          - disabledRamp    
          - gps    
          - internetConnection    
          - overspeed    
          - proximitySensor    
          - wifi    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    fleetVehicleId:    
      description: The identifier of the vehicle in the context of the fleet of vehicles to which it belongs    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    fuelEfficiency:    
      description: The distance traveled per unit of fuel used, commonly in kilometers per liter (km/L)    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fuelFilled:    
      description: Amount of fuel filled in liters to the vehicle corresponding to this observation    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fuelType:    
      description: The type of fuel suitable for the engine or engines of the vehicle corresponding to this observation    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    heading:    
      description: Denotes the direction of travel of the vehicle and is specified in decimal degrees, where 0 <= `heading` < 360, counting clockwise relative to the true north. If the vehicle is stationary (i.e. the value of the `speed` attribute is `0`), then the value of the heading attribute must be equal to `-1`    
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
        units: Degree    
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
    ignitionStatus:    
      description: Gives the ignition status of the vehicle. True means ignited    
      type: boolean    
      x-ngsi:    
        model: https://schema.org/Boolean    
        type: Property    
    image:    
      description: An image of the item    
      format: uri    
      type: string    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Property    
    license_plate:    
      description: 'Gives the License Plate number of the vehicle. SameAs: license_plate field from GTFS Realtime message-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)'''    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
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
    mileageFromOdometer:    
      description: The total distance travelled by the particular vehicle since its initial production, as read from its odometer    
      type: number    
      x-ngsi:    
        model: https://schema.org/mileageFromOdometer    
        type: Property    
    municipalityInfo:    
      description: Municipality information corresponding to this observation    
      properties:    
        cityId:    
          description: City ID corresponding to this observation    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        cityName:    
          description: City name corresponding to this observation    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        district:    
          description: District name corresponding to this observation    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        stateName:    
          description: Name of the state corresponding to this observation    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        ulbName:    
          description: Name of the Urban Local Body corresponding to this observation    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        wardId:    
          description: Ward ID corresponding to this observation    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        wardName:    
          description: Ward name corresponding to this observation    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        wardNum:    
          description: Ward number corresponding to this observation    
          type: number    
          x-ngsi:    
            model: https://schema.org/Number    
            type: Property    
        zoneId:    
          description: Zone ID corresponding to this observation    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        zoneName:    
          description: Zone name corresponding to this observation    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
      type: object    
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
        model: https://schema.org/DateTime    
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
    previousLocation:    
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
    purchaseDate:    
      description: The date the item e.g. vehicle was purchased by the current owner    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/purchaseDate    
        type: Property    
    refVehicleModel:    
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
      description: Reference to a VehicleModel    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Relationship    
    reportId:    
      description: Unique Id assigned for the issue or report or feedback or transaction corresponding to this observation    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
    serviceOnDuty:    
      description: Nature of service provided by emergency vehicle corresponding to this observation. True indicates the emergency vehicle corresponding to this observation is attending to/ servicing to an emergency call of duty and is False otherwise    
      type: boolean    
      x-ngsi:    
        model: https://schema.org/Boolean    
        type: Property    
    serviceProvided:    
      description: Service(s) the vehicle is capable of providing or it is assigned to. Enum:'auxiliaryServices, cargoTransport, construction, fairground, garbageCollection, goodsSelling, maintenance, parksAndGardens, roadSignalling, specialTransport, streetCleaning, streetLighting, urbanTransit, wasteContainerCleaning'. Or any other value needed by an specific application    
      items:    
        enum:    
          - auxiliaryServices    
          - cargoTransport    
          - construction    
          - fairground    
          - garbageCollection    
          - goodsSelling    
          - maintenance    
          - parksAndGardens    
          - roadSignalling    
          - specialTransport    
          - streetCleaning    
          - streetLighting    
          - urbanTransit    
          - wasteContainerCleaning    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    serviceStatus:    
      description: 'Vehicle status (from the point of view of the service provided, so it could not apply to private vehicles). `parked` : Vehicle is parked and not providing any service at the moment. `onRoute` : Vehicle is performing a mission. A comma-separated modifier(s) can be added to indicate what mission is currently delivering the vehicle. For instance `onRoute,garbageCollection` can be used to denote that the vehicle is on route and in a garbage collection mission. ''broken'' : Vehicle is suffering a temporary breakdown. `outOfService` : Vehicle is on the road but not performing any mission, probably going to its parking area. Enum:''broken, onRoute, outOfService, parked'''    
      enum:    
        - broken    
        - onRoute    
        - outOfService    
        - parked    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    source:    
      description: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object    
      type: string    
      x-ngsi:    
        type: Property    
    speed:    
      description: Denotes the magnitude of the horizontal component of the vehicle's current velocity and is specified in Kilometers per Hour. If provided, the value of the speed attribute must be a non-negative real number. `-1` MAY be used if speed is transiently unknown for some reason    
      oneOf:    
        - minimum: 0    
          type: number    
        - maximum: -1    
          minimum: -1    
          type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Km/h    
    tripNetWeightCollected:    
      description: The net weight collected by the vehicle corresponding to this observation at the end of the trip    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be Vehicle    
      enum:    
        - Vehicle    
      type: string    
      x-ngsi:    
        type: Property    
    vehicleAltitude:    
      description: Gives the current altitude of the vehicle using GPS    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    vehicleConfiguration:    
      description: A short text indicating the configuration of the vehicle, e.g. '5dr hatchback ST 2.5 MT 225 hp' or 'limited edition'    
      type: string    
      x-ngsi:    
        model: https://schema.org/vehicleConfiguration    
        type: Property    
    vehicleIdentificationNumber:    
      description: The Vehicle Identification Number (VIN) is a unique serial number used by the automotive industry to identify individual motor vehicles    
      type: string    
      x-ngsi:    
        model: https://schema.org/vehicleIdentificationNumber    
        type: Property    
    vehiclePlateIdentifier:    
      description: ' An identifier or code displayed on a vehicle registration plate attached to the vehicle used for official identification purposes. The registration identifier is numeric or alphanumeric and is unique within the issuing authority''s region. Normative References: DATEXII `vehicleRegistrationPlateIdentifier`'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    vehicleRunningStatus:    
      description: Gives the Battery charging status of the reporting device. Enum:'running, waiting, stopped'    
      enum:    
        - running    
        - stopped    
        - waiting    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    vehicleSpecialUsage:    
      description: Indicates whether the vehicle is been used for special purposes, like commercial rental, driving school, or as a taxi. The legislation in many countries requires this information to be revealed when offering a car for sale. Enum:'ambulance, fireBrigade, military, police, schoolTransportation, taxi, trashManagement'    
      enum:    
        - ambulance    
        - fireBrigade    
        - military    
        - police    
        - schoolTransportation    
        - taxi    
        - trashManagement    
      type: string    
      x-ngsi:    
        model: https://schema.org/vehicleSpecialUsage    
        type: Property    
    vehicleTrackerDevice:    
      description: Installation status of the GPS device or the tracking device fitted to the vehicle corresponding to this observation    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    vehicleType:    
      description: Type of vehicle from the point of view of its structural characteristics. This is different than the vehicle category . Enum:'agriculturalVehicle, anyVehicle, articulatedVehicle, bicycle, binTrolley, bus, car, caravan, carOrLightVehicle, carWithCaravan, carWithTrailer, cleaningTrolley, constructionOrMaintenanceVehicle, fourWheelDrive, highSidedVehicle, lorry, minibus, moped, motorcycle, motorcycleWithSideCar, motorscooter, sweepingMachine, tanker, threeWheeledVehicle, trailer, tram, twoWheeledVehicle, trolley, van, vehicleWithoutCatalyticConverter, vehicleWithCaravan, vehicleWithTrailer, withEvenNumberedRegistrationPlates, withOddNumberedRegistrationPlates, other'. The following values defined by _VehicleTypeEnum_ and _VehicleTypeEnum2_, [DATEX 2 version 2.3](http://d2docs.ndwcloud.nu/_static/umlmodel/v2.3/index.htm) and extended for other uses    
      enum:    
        - agriculturalVehicle    
        - ambulance    
        - anyVehicle    
        - articulatedVehicle    
        - autorickshaw    
        - bicycle    
        - binTrolley    
        - BRT mini bus·    
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
        - e-bike    
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
        - pilotVessel    
        - passengerVessel    
        - cargoVessel    
        - tug    
        - militaryVessel    
        - sailingVessel    
        - vessel    
        - other    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    wardId:    
      description: Ward ID of the entity corresponding to this observation    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    wardName:    
      description: Ward name of the entity corresponding to this observation    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    zoneName:    
      description: Zone name of the entity corresponding to this observation    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
  required:    
    - id    
    - type    
    - vehicleType    
    - category    
    - location    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms...    
  x-license-url: https://github.com/smart-data-models/dataModel.Transportation/blob/master/Vehicle/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Transportation/Vehicle/schema.json    
  x-model-tags: IUDX, SEDIMARK    
  x-version: 0.2.2    
```  
</details>    
<!-- /60-ModelYaml -->
  
<!-- 70-MiddleNotes -->
  
<!-- /70-MiddleNotes -->
  
<!-- 80-Examples -->
  

## 예시 페이로드  

#### 차량 NGSI-v2 키-값 예시  

여기에는 키-값으로 JSON 형식의 차량 예가 있습니다. 이것은 `options=keyValues`를 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    

```json  

{  
  "id": "vehicle:WasteManagement:1",  
  "type": "Vehicle",  
  "vehicleType": "lorry",  
  "battery": 0.81,  
  "category": [  
    "municipalServices"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -3.164485591715449,  
      40.62785133667262  
    ]  
  },  
  "name": "C Recogida 1",  
  "speed": 50,  
  "cargoWeight": 314,  
  "serviceStatus": "onRoute",  
  "serviceProvided": [  
    "garbageCollection",  
    "wasteContainerCleaning"  
  ],  
  "areaServed": "Centro",  
  "refVehicleModel": "vehiclemodel:econic",  
  "vehiclePlateIdentifier": "3456ABC",  
  "bearing": 43,  
  "fuelEfficiency": 13,  
  "fuelType": "Petrol",  
  "fuelFilled": 6,  
  "tripNetWeightCollected": 12,  
  "vehicleTrackerDevice": "Installed",  
  "wardId": "4",  
  "license_plate": "KA052134",  
  "currentTripCount": 1,  
  "reportId": "21645",  
  "zoneName": "South Zone",  
  "vehicleAltitude": "600",  
  "deviceSimNumber": "9942142573",  
  "wardName": "Kempegowda Ward",  
  "deviceBatteryStatus": "connected",  
  "ignitionStatus": true,  
  "vehicleRunningStatus": "running",  
  "observationDateTime": "2021-03-11T15:51:02+05:30",  
  "serviceOnDuty": false,  
  "emergencyVehicleType": "ambulance",  
  "municipalityInfo": {  
    "district": "Bangalore Urban",  
    "ulbName": "BMC",  
    "cityId": "23",  
    "wardId": "23",  
    "stateName": "Karnataka",  
    "cityName": "Bangalore",  
    "zoneName": "South",  
    "wardName": "Bangalore Urban",  
    "zoneId": "2",  
    "wardNum": 4  
  }  
}  
```  
</details>  

#### 차량 NGSI-v2 정규화 예시  

여기에는 JSON 형식으로 정규화된 차량의 예가 있습니다. 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    

```json  

{  
  "id": "vehicle:WasteManagement:1",  
  "type": "Vehicle",  
  "category": {  
    "type": "StructuredValue",  
    "value": [  
      "municipalServices"  
    ]  
  },  
  "vehicleType": {  
    "type": "Text",  
    "value": "lorry"  
  },  
  "battery": {  
    "type": "Number",  
    "value": 0.81  
  },  
  "name": {  
    "type": "Text",  
    "value": "C Recogida 1"  
  },  
  "vehiclePlateIdentifier": {  
    "type": "Text",  
    "value": "3456ABC"  
  },  
  "refVehicleModel": {  
    "type": "Text",  
    "value": "vehiclemodel:econic"  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -3.164485591715449,  
        40.62785133667262  
      ]  
    },  
    "metadata": {  
      "timestamp": {  
        "type": "DateTime",  
        "value": "2018-09-27T12:00:00"  
      }  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Centro"  
  },  
  "serviceStatus": {  
    "type": "Text",  
    "value": "onRoute"  
  },  
  "cargoWeight": {  
    "type": "Number",  
    "value": 314  
  },  
  "speed": {  
    "type": "Number",  
    "value": 50,  
    "metadata": {  
      "timestamp": {  
        "type": "DateTime",  
        "value": "2018-09-27T12:00:00"  
      }  
    }  
  },  
  "serviceProvided": {  
    "type": "StructuredValue",  
    "value": [  
      "garbageCollection",  
      "wasteContainerCleaning"  
    ]  
  },  
  "bearing": {  
    "type": "Number",  
    "value": 43  
  },  
  "fuelEfficiency": {  
    "type": "Number",  
    "value": 13  
  },  
  "fuelType": {  
    "type": "Text",  
    "value": "Petrol"  
  },  
  "fuelFilled": {  
    "type": "Number",  
    "value": 6  
  },  
  "tripNetWeightCollected": {  
    "type": "Number",  
    "value": 12  
  },  
  "vehicleTrackerDevice": {  
    "type": "Text",  
    "value": "Installed"  
  },  
  "wardId": {  
    "type": "Text",  
    "value": "4"  
  },  
  "license_plate": {  
    "type": "Text",  
    "value": "KA052134"  
  },  
  "currentTripCount": {  
    "type": "Boolean",  
    "value": true  
  },  
  "reportId": {  
    "type": "Text",  
    "value": "21645"  
  },  
  "zoneName": {  
    "type": "Text",  
    "value": "South Zone"  
  },  
  "vehicleAltitude": {  
    "type": "Text",  
    "value": "600"  
  },  
  "deviceSimNumber": {  
    "type": "Text",  
    "value": "9942142573"  
  },  
  "wardName": {  
    "type": "Text",  
    "value": "Kempegowda Ward"  
  },  
  "deviceBatteryStatus": {  
    "type": "Text",  
    "value": "connected"  
  },  
  "ignitionStatus": {  
    "type": "Boolean",  
    "value": true  
  },  
  "vehicleRunningStatus": {  
    "type": "Text",  
    "value": "running"  
  },  
  "observationDateTime": {  
    "type": "DateTime",  
    "value": "2021-03-11T15:51:02+05:30"  
  },  
  "serviceOnDuty": {  
    "type": "Boolean",  
    "value": false  
  },  
  "emergencyVehicleType": {  
    "type": "Text",  
    "value": "ambulance"  
  },  
  "municipalityInfo": {  
    "type": "StructuredValue",  
    "value": {  
      "district": "Bangalore Urban",  
      "ulbName": "BMC",  
      "cityId": "23",  
      "wardId": "23",  
      "stateName": "Karnataka",  
      "cityName": "Bangalore",  
      "zoneName": "South",  
      "wardName": "Bangalore Urban",  
      "zoneId": "2",  
      "wardNum": 4  
    }  
  }  
}  
```  
</details>  

#### 차량 NGSI-LD 키-값 예시  

여기에는 JSON-LD 형식의 키-값으로 된 차량의 예가 있습니다. 이것은 `options=keyValues`를 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    

```json  

{  
  "id": "urn:ngsi-ld:Vehicle:vehicle:WasteManagement:1",  
  "type": "Vehicle",  
  "areaServed": "Centro",  
  "battery": 0.81,  
  "bearing": 43,  
  "cargoWeight": 314,  
  "category": [  
    "municipalServices"  
  ],  
  "currentTripCount": 1,  
  "deviceBatteryStatus": "connected",  
  "deviceSimNumber": "9942142573",  
  "emergencyVehicleType": "ambulance",  
  "fuelEfficiency": 13,  
  "fuelFilled": 6,  
  "fuelType": "Petrol",  
  "ignitionStatus": true,  
  "license_plate": "KA052134",  
  "location": {  
    "coordinates": [  
      -3.164485591715449,  
      40.62785133667262  
    ],  
    "type": "Point"  
  },  
  "municipalityInfo": {  
    "district": "Bangalore Urban",  
    "ulbName": "BMC",  
    "cityId": "23",  
    "wardId": "23",  
    "stateName": "Karnataka",  
    "cityName": "Bangalore",  
    "zoneName": "South",  
    "wardName": "Bangalore Urban",  
    "zoneId": "2",  
    "wardNum": 4  
  },  
  "name": "C Recogida 1",  
  "observationDateTime": "2021-03-11T15:51:02+05:30",  
  "refVehicleModel": "urn:ngsi-ld:VehicleModel:vehiclemodel:econic",  
  "reportId": "21645",  
  "serviceOnDuty": false,  
  "serviceProvided": [  
    "garbageCollection",  
    "wasteContainerCleaning"  
  ],  
  "serviceStatus": "onRoute",  
  "speed": 50,  
  "tripNetWeightCollected": 12,  
  "vehicleAltitude": "600",  
  "vehiclePlateIdentifier": "3456ABC",  
  "vehicleRunningStatus": "running",  
  "vehicleTrackerDevice": "Installed",  
  "vehicleType": "lorry",  
  "wardId": "4",  
  "wardName": "Kempegowda Ward",  
  "zoneName": "South Zone",  
  "@context": [  
    "https://smart-data-models.github.io/dataModel.Transportation/context.jsonld"  
  ]  
}  
```  
</details>  

#### 차량 NGSI-LD 정규화 예시  

여기에는 JSON-LD 형식으로 정규화된 차량의 예가 있습니다. 이것은 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    

```json  

{  
  "id": "urn:ngsi-ld:Vehicle:vehicle:WasteManagement:1",  
  "type": "Vehicle",  
  "areaServed": {  
    "type": "Property",  
    "value": "Centro"  
  },  
  "battery": {  
    "type": "Property",  
    "value": 0.81,  
    "observedAt": "2021-03-11T15:51:02+05:30"  
  },  
  "bearing": {  
    "type": "Property",  
    "value": 43  
  },  
  "cargoWeight": {  
    "type": "Property",  
    "value": 314  
  },  
  "category": {  
    "type": "Property",  
    "value": [  
      "municipalServices"  
    ]  
  },  
  "currentTripCount": {  
    "type": "Property",  
    "value": 1  
  },  
  "deviceBatteryStatus": {  
    "type": "Property",  
    "value": "Connected"  
  },  
  "deviceSimNumber": {  
    "type": "Property",  
    "value": "9942142573"  
  },  
  "emergencyVehicleType": {  
    "type": "Property",  
    "value": "ambulance"  
  },  
  "fuelEfficiency": {  
    "type": "Property",  
    "value": 13  
  },  
  "fuelFilled": {  
    "type": "Property",  
    "value": 6  
  },  
  "fuelType": {  
    "type": "Property",  
    "value": "Petrol"  
  },  
  "ignitionStatus": {  
    "type": "Property",  
    "value": true  
  },  
  "license_plate": {  
    "type": "Property",  
    "value": "KA052134"  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -3.164485591715449,  
        40.62785133667262  
      ]  
    },  
    "observedAt": "2018-09-27T12:00:00Z"  
  },  
  "municipalityInfo": {  
    "type": "Property",  
    "value": {  
      "district": "Bangalore Urban",  
      "ulbName": "BMC",  
      "cityId": "23",  
      "wardId": "23",  
      "stateName": "Karnataka",  
      "cityName": "Bangalore",  
      "zoneName": "South",  
      "wardName": "Bangalore Urban",  
      "zoneId": "2",  
      "wardNum": 4  
    }  
  },  
  "name": {  
    "type": "Property",  
    "value": "C Recogida 1"  
  },  
  "observationDateTime": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2021-03-11T15:51:02+05:30"  
    }  
  },  
  "refVehicleModel": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:VehicleModel:vehiclemodel:econic"  
  },  
  "reportId": {  
    "type": "Property",  
    "value": "21645"  
  },  
  "serviceOnDuty": {  
    "type": "Property",  
    "value": false  
  },  
  "serviceProvided": {  
    "type": "Property",  
    "value": [  
      "garbageCollection",  
      "wasteContainerCleaning"  
    ]  
  },  
  "serviceStatus": {  
    "type": "Property",  
    "value": "onRoute"  
  },  
  "speed": {  
    "type": "Property",  
    "value": 50,  
    "observedAt": "2018-09-27T12:00:00Z"  
  },  
  "tripNetWeightCollected": {  
    "type": "Property",  
    "value": 12  
  },  
  "vehicleAltitude": {  
    "type": "Property",  
    "value": 600  
  },  
  "vehiclePlateIdentifier": {  
    "type": "Property",  
    "value": "3456ABC"  
  },  
  "vehicleRunningStatus": {  
    "type": "Property",  
    "value": "running"  
  },  
  "vehicleTrackerDevice": {  
    "type": "Property",  
    "value": "Installed"  
  },  
  "vehicleType": {  
    "type": "Property",  
    "value": "lorry"  
  },  
  "wardId": {  
    "type": "Property",  
    "value": "4"  
  },  
  "wardName": {  
    "type": "Property",  
    "value": "Kempegowda Ward"  
  },  
  "zoneName": {  
    "type": "Property",  
    "value": "South Zone"  
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
  

See [FAQ 10](https://smartdatamodels.org/index.php/faqs/) to get an answer on how to deal with magnitude units  
<!-- /95-Units -->
  
<!-- 97-LastFooter -->
  
---  

[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->
  
