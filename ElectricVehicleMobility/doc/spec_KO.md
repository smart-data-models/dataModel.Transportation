<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
 전기차 이동성  
===============================<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models//dataModel.Transportation/blob/master/ElectricVehicleMobility/LICENSE.md)  
[자동으로 생성된 문서](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
 전역 설명: 위치, 차량 브랜드, 지리적 지역별로 집계된 전기차 이동 패턴에 대한 일일 관찰  
 버전: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

 ## 속성 목록  

<sup><sub>속성에 유형이 없다면 그것은 여러 유형이나 서로 다른 형식/패턴을 가질 수 있기 때문이다</sub></sup>  
- `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: The country. For example, Spain  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 그 거리 주소가 속한 지역이자 그 지역에 있는  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 그 지역은 지자체가 위치하고 있으며, 그 국가에 있습니다  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 구는 일부 국가에서 지방 정부에 의해 관리되는 유형의 행정 구역입니다
	- `postOfficeBoxNumber[string]`: 우체국 사서함 주소의 사서함 번호입니다. 예를 들어, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 우편번호, 예를 들어 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 도로 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 공공 도로상 특정 부동산을 식별하는 번호
- `alternateName[string]`: 이 항목의 대체 이름 
 - `areaServed[string]`: 서비스 또는 제공된 항목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `averageDistanceKm[number]`: Average distance traveled in kilometers  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: Provider of the harmonised data entity  . Model: [https://schema.org/Text](https://schema.org/Text)- `dateCreated[date-time]`: Entity creation timestamp. This will usually be allocated by the storage platform  - `dateModified[date-time]`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform  - `dateObserved[date]`: Date of the observation (YYYY-MM-DD)  . Model: [https://schema.org/Date](https://schema.org/Date)- `description[string]`: A description of this item  - `deviceBrand[string]`: Brand or manufacturer of the electric vehicle  . Model: [https://schema.org/Text](https://schema.org/Text)- `district[string]`: District where the observation was made  . Model: [https://schema.org/Text](https://schema.org/Text)- `id[*]`: Unique identifier of the entity  - `location[*]`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `locationCode[string]`: Official municipality code  . Model: [https://schema.org/Text](https://schema.org/Text)- `municipality[string]`: Municipality where the observation was made  . Model: [https://schema.org/Text](https://schema.org/Text)- `n[number]`: Number of observations used to calculate the average distance  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: The name of this item  - `owner[array]`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `region[string]`: Region where the observation was made  . Model: [https://schema.org/Text](https://schema.org/Text)- `seeAlso[*]`: list of uri pointing to additional resources about the item  - `source[string]`: Original source of the data as a URL  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: NGSI entity type. It has to be ElectricVehicleMobility  - `vehicleType[string]`: Type of electric vehicle  . Model: [https://schema.org/Text](https://schema.org/Text)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
필수 속성  
- `id`   
- `type`   
<!-- /35-필수 속성 -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
 ## 데이터 모델 속성 설명  
알파벳 순으로 정렬됨(자세한 정보 클릭)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>전체 yaml 세부 정보</strong></summary>    
```yaml  
ElectricVehicleMobility:    
  description: Daily observation of electric vehicle mobility patterns aggregated by location, vehicle brand, and geographic region.    
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
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    averageDistanceKm:    
      description: Average distance traveled in kilometers    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: kilometers    
    dataProvider:    
      description: Provider of the harmonised data entity    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
      description: Date of the observation (YYYY-MM-DD)    
      format: date    
      type: string    
      x-ngsi:    
        model: https://schema.org/Date    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    deviceBrand:    
      description: Brand or manufacturer of the electric vehicle    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    district:    
      description: District where the observation was made    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
    locationCode:    
      description: Official municipality code    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    municipality:    
      description: Municipality where the observation was made    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    n:    
      description: Number of observations used to calculate the average distance    
      minimum: 1    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    name:    
      description: The name of this item    
      type: string    
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
          type: Relationship    
      type: array    
      x-ngsi:    
        type: Property    
    region:    
      description: Region where the observation was made    
      enum:    
        - CONTINENTE    
        - AÇORES    
        - MADEIRA    
        - Outros - GDPR    
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
    source:    
      description: Original source of the data as a URL    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    type:    
      description: NGSI entity type. It has to be ElectricVehicleMobility    
      enum:    
        - ElectricVehicleMobility    
      type: string    
      x-ngsi:    
        type: Property    
    vehicleType:    
      description: Type of electric vehicle    
      enum:    
        - BEV    
        - PHEV    
        - HEV    
        - FCEV    
        - unknown    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms...    
  x-license-url: https://github.com/smart-data-models/dataModel.Transportation/blob/master/ElectricVehicleMobility/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Transportation/ElectricVehicleMobility/schema.json    
  x-model-tags: transportation,electricVehicle,mobility,statistics    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
 ## 예시 페이로드  
 전기차 이동성 NGSI-v2 키-값 예시  
 JSON-LD 형식의 키-값으로 된 ElectricVehicleMobility의 예는 다음과 같습니다. 이것은 `options=keyValues`를 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>예시 표시/숨기기</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:ElectricVehicleMobility:PT:OUTROS-GDPR:OUTROS-GDPR:20251215",  
  "type": "ElectricVehicleMobility",  
  "dateObserved": "2025-12-15",  
  "region": "Outros - GDPR",  
  "district": "Outros - GDPR",  
  "municipality": "Outros - GDPR",  
  "locationCode": "Outros - GDPR",  
  "deviceBrand": "Outros - GDPR",  
  "averageDistanceKm": "",  
  "n": 26  
}  
```  
</details>  
 전기차이동성 NGSI-v2 정규화 예시  
 JSON-LD 형식으로 정규화된 ElectricVehicleMobility의 예는 다음과 같다. 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환한다.  
<details><summary><strong>예시 표시/숨기기</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:ElectricVehicleMobility:PT:OUTROS-GDPR:OUTROS-GDPR:20251215",  
  "type": "ElectricVehicleMobility",  
  "dateObserved": {  
    "type": "Date-Time",  
    "value": "2025-12-15"  
  },  
  "region": {  
    "type": "Text",  
    "value": "Outros - GDPR"  
  },  
  "district": {  
    "type": "Text",  
    "value": "Outros - GDPR"  
  },  
  "municipality": {  
    "type": "Text",  
    "value": "Outros - GDPR"  
  },  
  "locationCode": {  
    "type": "Text",  
    "value": "Outros - GDPR"  
  },  
  "deviceBrand": {  
    "type": "Text",  
    "value": "Outros - GDPR"  
  },  
  "averageDistanceKm": {  
    "type": "Text",  
    "value": ""  
  },  
  "n": {  
    "type": "Property",  
    "value": 26  
  }  
}  
```  
</details>  
 전기차 모빌리티 NGSI-LD 키-값 예시  
 이것은 JSON-LD 형식의 ElectricVehicleMobility의 예시로서 키-값으로 제공됩니다. 이것은 `options=keyValues`를 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>보기/숨기기 예시</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:ElectricVehicleMobility:PT:OUTROS-GDPR:OUTROS-GDPR:20251215",  
  "type": "ElectricVehicleMobility",  
  "dateObserved": "2025-12-15",  
  "region": "Outros - GDPR",  
  "district": "Outros - GDPR",  
  "municipality": "Outros - GDPR",  
  "locationCode": "Outros - GDPR",  
  "deviceBrand": "Outros - GDPR",  
  "averageDistanceKm": "",  
  "n": 26,  
  "@context": [  
    "https://smart-data-models.github.io/dataModel.Transportation/context.jsonld"  
  ]  
}  
```  
</details>  
 전기차 이동성 NGSI-LD 정형화 예시  
 JSON-LD 형식으로 정규화된 ElectricVehicleMobility의 예는 다음과 같습니다. 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>보기/숨기기 예시</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:ElectricVehicleMobility:PT:OUTROS-GDPR:OUTROS-GDPR:20251215",  
  "type": "ElectricVehicleMobility",  
  "dateObserved": {  
    "type": "Property",  
    "value": {  
      "@type": "Date",  
      "@value": "2025-12-15"  
    }  
  },  
  "region": {  
    "type": "Property",  
    "value": "Outros - GDPR"  
  },  
  "district": {  
    "type": "Property",  
    "value": "Outros - GDPR"  
  },  
  "municipality": {  
    "type": "Property",  
    "value": "Outros - GDPR"  
  },  
  "locationCode": {  
    "type": "Property",  
    "value": "Outros - GDPR"  
  },  
  "deviceBrand": {  
    "type": "Property",  
    "value": "Outros - GDPR"  
  },  
  "averageDistanceKm": {  
    "type": "Property",  
    "value": ""  
  },  
  "n": {  
    "type": "Property",  
    "value": 26  
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
 [FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하여 크기 단위 처리 방법에 대한 답변을 얻으십시오  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[스마트 데이터 모델](https://smartdatamodels.org) +++ [기여자 매뉴얼](https://bit.ly/contribution_manual)  
