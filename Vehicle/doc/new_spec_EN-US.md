Entity: Vehicle  
===============  
This specification is a **temporal version**. It is automatically generated from the  documented properties described in the schema.json condensed into the file `model.yaml`. A temporary `new_model.yaml` file has been created in every data model to avoid impacting into existing scripts. Thus, the specification will be incomplete as long as the schema.json is not updated to the new format (documenting properties). Once updated the `model.yaml` (`new_model.yaml`) needs to be updated as well (automatically) . Further info in this [link](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). As long as it is a provisional format any [feedback is welcomed in this form](https://smartdatamodels.org/index.php/submit-an-issue-2/) choosing option `Feedback on the new specification`  
Global description: **This entity models a particular vehicle model, including all properties which are common to multiple vehicle instances belonging to such model.**  

## List of properties  

- `address`: The mailing address.  - `alternateName`: An alternative name for this item  - `annotations`:   - `areaServed`:   - `cargoWeight`:   - `category`:   - `color`:   - `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  - `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateFirstUsed`:   - `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `dateVehicleFirstRegistered`:   - `description`: A description of this item  - `feature`:   - `fleetVehicleId`:   - `heading`:   - `id`:   - `image`: An image of the item.  - `location`:   - `mileageFromOdometer`:   - `name`: The name of this item.  - `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `previousLocation`:   - `purchaseDate`:   - `refVehicleModel`:   - `seeAlso`:   - `serviceProvided`:   - `serviceStatus`:   - `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `speed`:   - `type`: NGSI Entity type  - `vehicleConfiguration`:   - `vehicleIdentificationNumber`:   - `vehiclePlateIdentifier`:   - `vehicleSpecialUsage`:   - `vehicleType`:   ## Data Model description of properties  
Sorted alphabetically  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Vehicle:    
  description: 'This entity models a particular vehicle model, including all properties which are common to multiple vehicle instances belonging to such model.'    
  properties:    
    address:    
      description: 'The mailing address.'    
      properties:    
        addressCountry:    
          type: string    
        addressLocality:    
          type: string    
        addressRegion:    
          type: string    
        areaServed:    
          type: string    
        postOfficeBoxNumber:    
          type: string    
        postalCode:    
          type: string    
        streetAddress:    
          type: string    
      type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    annotations:    
      items:    
        type: string    
      type: array    
    areaServed:    
      type: string    
    cargoWeight:    
      exclusiveMinimum: 0    
      type: number    
    category:    
      items:    
        enum:    
          - public    
          - private    
          - municipalServices    
          - specialUsage    
          - tracked    
          - nonTracked    
        type: string    
      type: array    
    color:    
      type: string    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateFirstUsed:    
      format: date    
      type: string    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateVehicleFirstRegistered:    
      format: date    
      type: string    
    description:    
      description: 'A description of this item'    
      type: Property    
    feature:    
      items:    
        enum:    
          - gps    
          - airbag    
          - overspeed    
          - abs    
          - wifi    
          - backCamera    
          - proximitySensor    
          - disabledRamp    
          - alarm    
          - internetConnection    
        type: string    
      type: array    
    fleetVehicleId:    
      type: string    
    heading:    
      oneOf:    
        - maximum: 360    
          minimum: 0    
          type: number    
        - const: -1    
          type: number    
    id:    
      anyOf: &vehicle_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
    image:    
      description: 'An image of the item.'    
      format: uri    
      type: string    
    location:    
      $id: https://geojson.org/schema/Geometry.json    
      $schema: "http://json-schema.org/draft-07/schema#"    
      oneOf: &vehicle_-_properties_-_previouslocation_-_oneof    
        - properties:    
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
          title: 'GeoJSON Point'    
          type: object    
        - properties:    
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
          title: 'GeoJSON LineString'    
          type: object    
        - properties:    
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
          title: 'GeoJSON Polygon'    
          type: object    
        - properties:    
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
          title: 'GeoJSON MultiPoint'    
          type: object    
        - properties:    
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
          title: 'GeoJSON MultiLineString'    
          type: object    
        - properties:    
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
          title: 'GeoJSON MultiPolygon'    
          type: object    
      title: 'GeoJSON Geometry'    
    mileageFromOdometer:    
      type: number    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *vehicle_-_properties_-_owner_-_items_-_anyof    
      type: Property    
    previousLocation:    
      $id: https://geojson.org/schema/Geometry.json    
      $schema: "http://json-schema.org/draft-07/schema#"    
      oneOf: *vehicle_-_properties_-_previouslocation_-_oneof    
      title: 'GeoJSON Geometry'    
    purchaseDate:    
      format: date-time    
      type: string    
    refVehicleModel:    
      anyOf: *vehicle_-_properties_-_owner_-_items_-_anyof    
    seeAlso:    
      oneOf:    
        - items:    
            - format: uri    
              type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
    serviceProvided:    
      items:    
        enum:    
          - garbageCollection    
          - parksAndGardens    
          - construction    
          - streetLighting    
          - roadSignalling    
          - cargoTransport    
          - urbanTransit    
          - maintenance    
          - streetCleaning    
          - wasteContainerCleaning    
          - auxiliaryServices    
          - goodsSelling    
          - fairground    
          - specialTransport    
        type: string    
      type: array    
    serviceStatus:    
      enum:    
        - parked    
        - onRoute    
        - broken    
        - outOfService    
      type: string    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    speed:    
      oneOf:    
        - minimum: 0    
          type: number    
        - enum:    
            - -1    
          type: number    
    type:    
      description: 'NGSI Entity type'    
      enum:    
        - Vehicle    
      type: string    
    vehicleConfiguration:    
      type: string    
    vehicleIdentificationNumber:    
      type: string    
    vehiclePlateIdentifier:    
      type: string    
    vehicleSpecialUsage:    
      enum:    
        - taxi    
        - ambulance    
        - police    
        - fireBrigade    
        - schoolTransportation    
        - military    
      type: string    
    vehicleType:    
      enum:    
        - agriculturalVehicle    
        - anyVehicle    
        - articulatedVehicle    
        - bicycle    
        - bus    
        - minibus    
        - car    
        - caravan    
        - carOrLightVehicle    
        - carWithCaravan    
        - carWithTrailer    
        - constructionOrMaintenanceVehicle    
        - fourWheelDrive    
        - highSidedVehicle    
        - lorry    
        - moped    
        - motorcycle    
        - motorcycleWithSideCar    
        - motorscooter    
        - tanker    
        - threeWheeledVehicle    
        - trailer    
        - tram    
        - twoWheeledVehicle    
        - van    
        - vehicleWithoutCatalyticConverter    
        - vehicleWithCaravan    
        - vehicleWithTrailer    
        - withEvenNumberedRegistrationPlates    
        - withOddNumberedRegistrationPlates    
        - other    
      type: string    
  required:    
    - id    
    - type    
    - vehicleType    
    - category    
    - location    
  type: object    
```  
</details>    
#### Vehicle NGSI V2 key-values Example    
Here is an example of a Vehicle in JSON format as key-values. This is compatible with NGSI V2 when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
      "id": "vehicle:WasteManagement:1",  
      "type": "Vehicle",  
      "vehicleType": "lorry",  
      "category": ["municipalServices"],  
      "location": {  
         "type": "Point",  
         "coordinates": [ -3.164485591715449, 40.62785133667262 ]  
      },  
      "name": "C Recogida 1",  
      "speed": 50,  
      "cargoWeight": 314,  
      "serviceStatus": "onRoute",  
      "serviceProvided": ["garbageCollection", "wasteContainerCleaning"],  
      "areaServed": "Centro",  
      "refVehicleModel": "vehiclemodel:econic",  
      "vehiclePlateIdentifier": "3456ABC"  
}  
```  
#### Vehicle NGSI V2 normalized Example    
Here is an example of a Vehicle in JSON format as normalized. This is compatible with NGSI V2 when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
    "id": "vehicle:WasteManagement:1",  
    "type": "Vehicle",   
    "category": {  
        "value": [  
            "municipalServices"  
        ]  
    },   
    "vehicleType": {  
        "value": "lorry"  
    },   
    "name": {  
        "value": "C Recogida 1"  
    },   
    "vehiclePlateIdentifier": {  
        "value": "3456ABC"  
    },   
    "refVehicleModel": {  
        "type": "Relationship",   
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
        "value": "Centro"  
    },   
    "serviceStatus": {  
        "value": "onRoute"  
    },   
    "cargoWeight": {  
        "value": 314  
    },   
    "speed": {  
        "value": 50,  
        "metadata": {  
            "timestamp": {  
                "type": "DateTime",  
                "value": "2018-09-27T12:00:00"  
            }  
        }  
    },    
    "serviceProvided": {  
        "value": [  
            "gargabeCollection",   
            "wasteContainerCleaning"  
        ]  
    }  
}  
```  
#### Vehicle NGSI-LD key-values Example    
Here is an example of a Vehicle in JSON-LD format as key-values. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context",  
              "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"],  
 "areaServed": "Centro",  
 "cargoWeight": 314,  
 "category": ["municipalServices"],  
 "id": "urn:ngsi-ld:Vehicle:vehicle:WasteManagement:1",  
 "location": {"coordinates": [-3.164485591715449, 40.62785133667262],  
              "type": "Point"},  
 "name": "C Recogida 1",  
 "refVehicleModel": "urn:ngsi-ld:VehicleModel:vehiclemodel:econic",  
 "serviceProvided": ["gargabeCollection", "wasteContainerCleaning"],  
 "serviceStatus": "onRoute",  
 "speed": 50,  
 "type": "Vehicle",  
 "vehiclePlateIdentifier": "3456ABC",  
 "vehicleType": "lorry"}  
```  
#### Vehicle NGSI-LD normalized Example    
Here is an example of a Vehicle in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
```json  
{  
    "id": "urn:ngsi-ld:Vehicle:vehicle:WasteManagement:1",  
    "type": "Vehicle",  
    "category": {  
        "type": "Property",  
        "value": [  
            "municipalServices"  
        ]  
    },  
    "vehicleType": {  
        "type": "Property",  
        "value": "lorry"  
    },  
    "name": {  
        "type": "Property",  
        "value": "C Recogida 1"  
    },  
    "vehiclePlateIdentifier": {  
        "type": "Property",  
        "value": "3456ABC"  
    },  
    "refVehicleModel": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:VehicleModel:vehiclemodel:econic"  
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
    "areaServed": {  
        "type": "Property",  
        "value": "Centro"  
    },  
    "serviceStatus": {  
        "type": "Property",  
        "value": "onRoute"  
    },  
    "cargoWeight": {  
        "type": "Property",  
        "value": 314  
    },  
    "speed": {  
        "type": "Property",  
        "value": 50,  
        "observedAt": "2018-09-27T12:00:00Z"  
    },  
    "serviceProvided": {  
        "type": "Property",  
        "value": [  
            "gargabeCollection",  
            "wasteContainerCleaning"  
        ]  
    },  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  
