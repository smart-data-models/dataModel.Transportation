<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entity: 도로 사고    
=============<!-- /10-Header -->    
<!-- 15-License -->    
[오픈 라이선스](https://github.com/smart-data-models//dataModel.Transportation/blob/master/RoadAccident/LICENSE.md)    
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
전체 설명: **원인과 여파가 포함된 도로 사고 설명. 싱크로니시티 프로젝트에서 개발된 첫 번째 버전**    
버전: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## 속성 목록    
<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.    
- `accidentDate[date-time]`: 사고 발생 시간  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `accidentDescription[array]`: 이 도로 사고에 대한 설명은 코드화된 상황의 조합으로 입력됩니다. 0: 불특정 상황, 1: 운전자가 회전하지 않고 규칙적으로 진행, 2: 운전자가 산만 운전 또는 진로 미확정으로 진행, 3: 운전자가 안전거리를 유지하지 않고 진행, 4: 운전자가 오른쪽에서 오는 차량에 우선권을 주지 않고 진행, 5: 운전자가 정지를 지키지 않고 진행, 6: 운전자가 우선권을 주는 신호를 지키지 않고 진행, 7: 신호등 또는 보조 신호를 지키지 않고 진행, 8: 신호등 또는 보조 신호를 지키지 않고 진행, 10: 통행 또는 접근 금지 표지판을 지키지 않고 진행, 11: 과속으로 진행, 12: 제한 속도를 지키지 않고 진행, 13: 다른 차량을 가로지르며 점멸등을 켜고 진행, 14: 운전자가 규칙적으로 우회전, 15: 불규칙적으로 우회전, 16: 운전자가 규칙적으로 좌회전, 17: 불규칙적으로 좌회전, 18: 운전자가 교차로를 통과, 20: 운전자가 규칙적으로 진행, 21: 운전자가 산만 운전 또는 미결정 경로로 진행, 22: 운전자가 안전거리 유지 없이 진행, 23: 운전자가 과속으로 진행, 24: 제한 속도를 지키지 않고 진행함, 25: 도로의 우측 가장자리에 근접하지 않고 진행함, 26: 교통에 역행하여 진행함, 27: 통행 또는 접근 금지 표지판을 지키지 않고 진행함, 28: 다른 차량을 가로지르며 눈부신 불빛으로 진행함, 29: 규칙적으로 추월함, 30: 불규칙적으로 오른쪽으로 추월함, 31: 운전자가 커브, 언덕 또는 시야가 충분하지 않은 상태에서 추월; 32 : 다른 차량을 추월하는 차량을 추월; 33 : 운전자가 적절한 금지 표지판을 준수하지 않고 통과; 34 : 강등 또는 전환으로 기동; 35 : 운전자가 순환 흐름에 들어가기 위해 기동; 36 : 좌회전 (개인 통로, 분배기)을 위해 기동; 37: 운전자가 정지 또는 정지를 위해 규칙적으로 기동; 38 : 운전자가 정지 또는 정지를 위해 불규칙적으로 기동; 39 : 다른 불규칙한 이륜차와 합류; 40 : 운전자가 규칙적으로 진행; 41 : 운전자가 과속으로 진행; 42 : 운전자가 제한 속도를 존중하지 않고 진행; 43 : 운전자가 교통에 반하여 진행; 44 : 운전자가 기어로 차량을 추월; 45 : 기동; 46: 신호등 또는 대리인 신호를 존중하지 않고 기동함, 47: 운전자가 주의 없이 차도에서 나왔음, 48: 운전자가 차선을 벗어나 폰을 치었음, 49: 적절한 횡단보도에서 보행자에게 우선권을 주지 않음, 50: 횡단을 허용하기 위해 정지한 차량을 추월함, 51: 운전자가 적재물로 보행자를 치었음, 52: 운전자가 정류장에서 트램을 고르지 않게 통과함, 60: 운전자가 규칙적으로 진행함, 61: 운전자가 산만하게 운전하거나 경로를 정하지 않고 진행함, 62: 운전자가 안전거리를 유지하지 않고 진행함, 63: 운전자가 교통에 반하여 진행함, 64: 운전자가 과속으로 진행함, 65: 운전자가 제한 속도를 지키지 않고 진행함, 66: 운전자가 통행 또는 접근 금지 표시를 지키지 않고 진행함, 67: 운전자가 기어로 다른 차량을 추월하고 있었음, 68: 운전자가 무분별하게 횡단보도를 건넜음, 70: 충격을 피하기 위해 유출물을 흘림, 71: 산만 운전으로 인한 유출과 함께 청취; 72: 과속 유출로 목록; 73: 운전자가 갑자기 운송 된 결과로 갑자기 제동; 74: 75: 차량에서 사람 추락: 문 개방, 75: 차량에서 사람 추락: 운행 중인 차량에서 하차, 76: 76: 달라붙거나 부적절한 위치로 인한 차량에서 사람 추락, 80: 브레이크 고장 또는 고장, 81: 파손 또는 조향 실패, 82: 타이어 파열 또는 과도한 마모, 83: 전조등 또는 포지션 라이트의 부족 또는 불충분, 84: 점멸등 또는 정지등 신호의 부족 또는 불충분, 85: 트레일러 결합 부품의 파손, 86: 위험물 운송 장비의 결함, 87: 87: 신체 장애인의 차량에 규정된 적응의 결함; 88: 바퀴 분리; 89: 사이클용 시각 장치의 부족 또는 불충분함  . Model: [https://schema.org/Text](https://schema.org/Text)- `accidentLocation[string]`: 사고가 도시 또는 도시 외 지역에서 발생한 경우 간략한 설명. 0: 도시 지역 내 지방도 1: 마을 내 도시 도로 2: 마을 내 지방도 3: 마을 내 국도 4: 도시 외 도로 5: 지방도 6: 국도 7: 고속도로 8: 기타 도로 9: 지방도  - `accidentStatisticalDate[object]`: 사고의 대략적인 날짜 시간(원본 사고 데이터 소스에는 계절, 요일, 대략적인 시간과 같은 통계적 속성만 보고되는 경우가 많습니다.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)	- `hour`:       
	- `quarter`:       
	- `weekday[string]`: 평일      
	- `year`:       
- `accidentType[array]`: 이 도로 사고를 빠르게 분류합니다. 1: 정면 충돌, 2: 정면-측면 충돌, 3: 측면 충돌, 4: 충돌, 5: 보행자 접촉, 6: 정지 또는 정차 중인 차량과의 충돌, 7: 주차된 차량과의 충돌, 8: 장애물과의 충돌, 9: 기차와의 충돌, 10: 유출, 미끄러짐, 11: 급제동으로 인한 사고, 12: 차량에서 추락으로 인한 사고입니다.  - `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 국가. 예를 들어, 스페인  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: 도로명 주소가 있는 지역 및 해당 지역에 속한 지역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: 해당 지역이 위치한 지역과 해당 국가의 지역  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: 지구는 일부 국가에서는 지방 정부에서 관리하는 행정 구역의 일종입니다.      
	- `postOfficeBoxNumber[string]`: 사서함 주소의 우체국 사서함 번호입니다. 예: 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: 우편 번호입니다. 예: 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: 거리 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
	- `streetNr[string]`: 공공 도로의 특정 건물을 식별하는 번호      
- `alternateName[string]`: 이 항목의 대체 이름  - `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `id[*]`: 엔티티의 고유 식별자  - `localId[string]`: 소스 데이터 집합의 고유 식별자  . Model: [https://schema.org/Text](https://schema.org/Text)- `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.  - `name[string]`: 이 항목의 이름  - `numPassengersDead[number]`: 사고로 인해 사망한 차량의 탑승자 수  . Model: [https://schema.org/Number](https://schema.org/Number)- `numPassengersInjured[number]`: 사고로 인해 부상을 입은 차량 탑승자 수  . Model: [https://schema.org/Number](https://schema.org/Number)- `numPedestrianDead[number]`: 사고로 인해 사망한 보행자 수  . Model: [https://schema.org/Number](https://schema.org/Number)- `numPedestrianInjured[number]`: 사고로 인해 부상당한 보행자 수  . Model: [https://schema.org/Number](https://schema.org/Number)- `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `pedestriansInvolved[boolean]`: 보행자가 사고에 연루되었는지 여부를 판단하는 부울입니다.  - `roadClass[string]`:  이 사고가 발생한 도로의 분류  . Model: [https://wiki.openstreetmap.org/wiki/Key:highway](https://wiki.openstreetmap.org/wiki/Key:highway)- `roadIntersection[string]`: 사고가 발생한 도로에 대한 간략한 설명.   1: 교차로, 2: 로터리, 3: 신고된 교차로, 4: 신호등 있는 교차로, 5: 신고되지 않은 교차로, 6: 건널목, 7: 직선, 8: 곡선, 9: 범프, 병목, 10: 경사, 11: 조명이 켜진 갤러리, 12: 조명이 없는 갤러리입니다;  - `roadPaving[string]`: 도로 포장. 1: 포장 도로, 2: 거친 포장 도로, 3: 비포장 도로;  - `roadSign[string]`: 사고가 발생한 도로 표지판에 대한 간략한 설명. 1: 없음, 2: 세로, 3: 가로, 4: 세로 및 가로, 5: 공사장별 임시;  - `roadSurface[string]`: 사고 당시 도로 상태에 대한 간략한 설명입니다. 1: 건조, 2: 습함, 3: 미끄러움, 4: 결빙, 5: 눈 덮임;  - `roadTrunk[string]`: 사고가 발생한 도로의 간선 유형에 대한 간략한 설명. 1: 도로 분기점, 2: 보조 분기점, 3: 부 분기점, 4: 교차로 분기점, 5: 도로 교차로, 6: 고속도로 좌측 차선, 7: 고속도로 차도 우측, 8: 고속도로 교차로 입구, 9: 고속도로 출구 교차로, 10: 고속도로 교차로 간선, 11: 고속도로 역, 12: 기타 사례, 15: 도시 외 도로  - `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `status[string]`: 도로 사고의 상태. Enum:'보관됨, 진행중, 해결됨'  . Model: [https://schema.org/Text](https://schema.org/Text)- `totalDeadPeopleWithin24Hours[number]`: 사고로 인해 직접 사망한 사람 수  . Model: [https://schema.org/Number](https://schema.org/Number)- `totalDeadPeopleWithin30Days[number]`: 사고의 여파로 인한 사망자 수  . Model: [https://schema.org/Number](https://schema.org/Number)- `totalInjured[number]`: 사고로 인해 부상당한 총 인원 수(사망자 제외)  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: NGSI 엔티티 유형은 RoadAccident여야 합니다.  - `vehiclesInvolved[array]`: 사고로 인해 관련된 차량(및 보행자) 목록 0 : 보행자 1 : 자전거 2 : 농업용 차량 3 : 버스 4 : 미니버스 5 : 자동차 6 : 카라반 7 : 트램 8 : 탱커 9 : 자동차WithCaravan 10 : 자동차WithTrailer 11 : 트럭 12 : 오토바이 13 : 유조선 14 : 오토바이 15 : 오토바이와부속차 16 : 모터스쿠터 17 : 트레일러 18 : 밴 19 : 카라반 20 : 건설용 또는 유지보수용 차량 21 : 트롤리 22 : 쓰레기통트롤리 23 : 청소기 24 : 청소트롤리  - `weakestSubject[string]`: 사고로 인해 가장 약한 대상(보통 보행자)을 나타내는 차량. 0 : 보행자 1 : 자전거 2 : 농업용차량 3 : 버스 4 : 미니버스 5 : 자동차 6 : 카라반 7 : 전차 8 : 탱커 9 : 자동차위드카라반 10 : 자동차위드트레일러 11 : 트럭 12 : 오토바이 13 : 탱커 14 : 오토바이 15 : 오토바이위드사이드카 16 : 모터스쿠터 17 : 트레일러 18 : 밴 19 : 카라반 20 : 건설 또는 유지보수용차량 21 : 트롤리 22 : 빈 트롤리 23 : 청소기 24 : 청소용트롤리  - `weatherConditions[array]`: 이 도로 사고 당시의 기상 상황에 대한 간략한 설명. 0 : 맑음밤 1 : 맑음낮 2 : 약간흐림3 : 구름많음4 : 안개5 : 안개6 : 높은구름7 : 흐림8 : 매우흐림9 : 흐림10 : 옅은비소나기11 : 이슬비12 : 옅은비13 : 무거운비샤워 14 : 무거운비 15 : 진눈깨비샤워 16 : 진눈깨비 17 : 우박샤워 18 : 우박 19 : 샤워 20 : 가벼운눈 21 : 눈 22 : 많은눈샤워 23 : 많은눈 24 : 천둥샤워 25 : 천둥  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
필수 속성    
- `id`  - `status`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
동시성 프로젝트에서 가져온 데이터 모델    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## 속성에 대한 데이터 모델 설명    
알파벳순으로 정렬(자세한 내용을 보려면 클릭)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
RoadAccident:      
  description: A road accident description with causes and aftermath. First version developed in Synchronicity project      
  properties:      
    accidentDate:      
      description: Datetime of the accident      
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
          description: Week days      
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
    localId:      
      description: Unique identifier from the source data set      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
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
    numPassengersDead:      
      description: Number of vehicle's passengers dead because the accident      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    numPassengersInjured:      
      description: Number of vehicle's passengers injured because the accident      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    numPedestrianDead:      
      description: Number of pedestrians dead because the accident      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    numPedestrianInjured:      
      description: Number of pedestrians injured because the accident      
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
    pedestriansInvolved:      
      description: Boolean to determine if pedestrians were involved in the accidents      
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
      description: 'Brief description of type of trunk of the road where the accident took place. 1: Road branch; 2: Secondary branch; 3: Minor branch; 4: Junction branch; 5: Road junction; 6: Motorway left lane; 7: Highway carriageway right; 8: Motorway junction entrance; 9: Highway exit junction; 10: Highway junction trunk; 11: Highway station; 12: Other cases; 15: Extra urban road'      
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
      description: Number of people dead directly because the accident      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    totalDeadPeopleWithin30Days:      
      description: Number of people dead because the aftermath of the accident      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    totalInjured:      
      description: total number of people injured (not dead) because the accident      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    type:      
      description: NGSI Entity type. it has to be RoadAccident      
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
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
## 페이로드 예시    
#### 도로 사고 NGSI-v2 키 값 예시    
다음은 키 값으로 JSON-LD 형식의 도로 사고의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
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
  "pedestriansInvolved": true,  
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
#### 도로 사고 NGSI-v2 정규화 예시    
다음은 정규화된 JSON-LD 형식의 도로 사고 예시입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:RoadAccident:id:ORHW:45620815",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2018-06-23T04:19:24Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2020-10-29T08:36:40Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "To be defined"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Name of the element of the accident."  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Other name."  
  },  
  "description": {  
    "type": "Text",  
    "value": "Clash in the middle of a traffic light"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Municipality."  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:RoadAccident:items:SUUU:18395806",  
      "urn:ngsi-ld:RoadAccident:items:GVOF:30958855"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:RoadAccident:items:ESLS:37894243",  
      "urn:ngsi-ld:RoadAccident:items:ZNUH:87936284"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -56.6404505,  
        168.370658  
      ]  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
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
    "type": "Text",  
    "value": "worldwide"  
  },  
  "type": "RoadAccident",  
  "localId": {  
    "type": "Text",  
    "value": "20210312-A1."  
  },  
  "status": {  
    "type": "Text",  
    "value": "onGoing"  
  },  
  "accidentDate": {  
    "type": "DateTime",  
    "value": "2021-03-12T13:59:36Z"  
  },  
  "accidentStatisticalDate": {  
    "type": "StructuredValue",  
    "value": {  
      "year": 2021,  
      "quarter": 1,  
      "weekday": "Friday",  
      "hour": 4  
    }  
  },  
  "accidentType": {  
    "type": "StructuredValue",  
    "value": [  
      "10",  
      "6"  
    ]  
  },  
  "accidentDescription": {  
    "type": "StructuredValue",  
    "value": [  
      "23",  
      "46"  
    ]  
  },  
  "weatherConditions": {  
    "type": "StructuredValue",  
    "value": [  
      "10",  
      "20"  
    ]  
  },  
  "roadSurface": {  
    "type": "Text",  
    "value": "2"  
  },  
  "roadPaving": {  
    "type": "Text",  
    "value": "2"  
  },  
  "accidentLocation": {  
    "type": "Text",  
    "value": "5"  
  },  
  "roadClass": {  
    "type": "Text",  
    "value": "Motorway."  
  },  
  "roadIntersection": {  
    "type": "Text",  
    "value": "8"  
  },  
  "roadTrunk": {  
    "type": "Text",  
    "value": "12"  
  },  
  "roadSign": {  
    "type": "Text",  
    "value": "5"  
  },  
  "pedestriansInvolved": {  
    "type": "Boolean",  
    "value": true  
  },  
  "vehiclesInvolved": {  
    "type": "StructuredValue",  
    "value": [  
      "21",  
      "6"  
    ]  
  },  
  "weakestSubject": {  
    "type": "Text",  
    "value": "20"  
  },  
  "numPassengersInjured": {  
    "type": "Boolean",  
    "value": true  
  },  
  "numPassengersDead": {  
    "type": "Boolean",  
    "value": true  
  },  
  "numPedestrianInjured": {  
    "type": "Boolean",  
    "value": true  
  },  
  "numPedestrianDead": {  
    "type": "Boolean",  
    "value": false  
  },  
  "totalInjured": {  
    "type": "Number",  
    "value": 2  
  },  
  "totalDeadPeopleWithin30Days": {  
    "type": "Boolean",  
    "value": false  
  },  
  "totalDeadPeopleWithin24Hours": {  
    "type": "Boolean",  
    "value": false  
  }  
}  
```  
</details>    
#### 도로 사고 NGSI-LD 키 값 예시    
다음은 키 값으로 JSON-LD 형식의 도로 사고의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
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
  "pedestriansInvolved": true,  
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
</details>    
#### 도로 사고 NGSI-LD 정규화 예시    
다음은 정규화된 JSON-LD 형식의 도로 사고 예시입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
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
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -56.6404505,  
        88.370658  
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
    "value": true  
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
</details><!-- /80-Examples -->    
<!-- 90-FooterNotes -->    
<!-- /90-FooterNotes -->    
<!-- 95-Units -->    
[FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하여 규모 단위를 다루는 방법에 대한 답변을 확인하세요.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
