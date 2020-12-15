Entity: VehicleModel  
====================  
This specification is a **temporal version**. It is automatically generated from the  documented properties described in the schema.json condensed into the file `model.yaml`. A temporary `new_model.yaml` file has been created in every data model to avoid impacting into existing scripts. Thus, the specification will be incomplete as long as the schema.json is not updated to the new format (documenting properties). Once updated the `model.yaml` (`new_model.yaml`) needs to be updated as well (automatically) . Further info in this [link](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). As long as it is a provisional format any [feedback is welcomed in this form](https://smartdatamodels.org/index.php/submit-an-issue-2/) choosing option `Feedback on the new specification`  
Global description: **This entity models a particular vehicle model, including all properties which are common to multiple vehicle instances belonging to such model.**  

## List of properties  

- `address`: The mailing address.  - `alternateName`: An alternative name for this item  - `annotations`:   - `areaServed`: The geographic area where a service or offered item is provided.  - `brandName`:   - `cargoVolume`:   - `color`: The color of the product.  - `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  - `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `depth`:   - `description`: A description of this item  - `fuelConsumption`:   - `fuelType`:   - `height`:   - `id`:   - `image`:   - `location`:   - `manufacturerName`:   - `modelName`:   - `name`: The name of this item.  - `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `seeAlso`:   - `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `type`: NGSI Entity type  - `url`:   - `vehicleEngine`:   - `vehicleModelDate`:   - `vehicleType`:   - `weight`:   - `width`:     
Required properties  
- `brandName`  - `id`  - `manufacturerName`  - `modelName`  - `name`  - `type`  - `vehicleType`  ## Data Model description of properties  
Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
VehicleModel:    
  description: 'This entity models a particular vehicle model, including all properties which are common to multiple vehicle instances belonging to such model.'    
  properties:    
    address:    
      description: 'The mailing address.'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/Text'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/Text'''    
          type: string    
        areaServed:    
          description: 'Property. The geographic area where a service or offered item is provided. Model:''https://schema.org/Text'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/Text'''    
          type: string    
      type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    annotations:    
      description: 'Annotations about the item'    
      items:    
        type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    brandName:    
      description: 'Vehicle''s brand name'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/brand.    
    cargoVolume:    
      description: 'The available volume for cargo or luggage. For automobiles, this is usually the trunk volume. If only a single value is provided (type Number) it will refer to the maximum volume.'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/cargoVolume    
        units: Liters    
    color:    
      description: 'The color of the product'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/color    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    depth:    
      description: 'Vehicle''s depth'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/depth.    
    description:    
      description: 'A description of this item'    
      type: Property    
    fuelConsumption:    
      description: 'The amount of fuel consumed for traveling a particular distance or temporal duration with the given vehicle (e.g. liters per 100 km)'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/fuelConsumption    
        units: 'liters per 100 kilometer'    
    fuelType:    
      description: 'The type of fuel suitable for the engine or engines of the vehicle. Enum:''autogas, biodiesel ethanol, cng, diesel, electric, gasoline, hybrid electric/diesel, hybrid electric/petrol, hydrogen, lpg, petrol, petrol(unleaded), petrol(leaded), other'''    
      enum:    
        - autogas    
        - biodiesel    
        - cng    
        - diesel    
        - electric    
        - ethanol    
        - gasoline    
        - 'hybrid electric/diesel'    
        - 'hybrid electric/petrol'    
        - hydrogen    
        - lpg    
        - petrol    
        - petrol(unleaded)    
        - petrol(leaded)    
        - other    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
    height:    
      description: 'Vehicle''s height'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/height.    
    id:    
      anyOf: &vehiclemodel_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      type: Property    
    image:    
      description: 'An image of the item'    
      format: uri    
      type: Property    
      x-ngsi:    
        model: https://schema.org/URL    
    location:    
      $id: https://geojson.org/schema/Geometry.json    
      $schema: "http://json-schema.org/draft-07/schema#"    
      oneOf:    
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
    manufacturerName:    
      description: 'Vehicle''s manufacturer name'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text.    
    modelName:    
      description: 'Vehicle''s model name'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/model.    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *vehiclemodel_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            - format: uri    
              type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    type:    
      description: 'NGSI Entity type. It has to be VehicleModel'    
      enum:    
        - VehicleModel    
      type: Property    
    url:    
      description: 'URL which provides a description of this vehicle model'    
      format: uri    
      type: Property    
      x-ngsi:    
        model: https://schema.org/URL.    
    vehicleEngine:    
      description: 'Information about the engine or engines of the vehicle'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/vehicleEngine.    
    vehicleModelDate:    
      description: 'The release date of a vehicle model (often used to differentiate versions of the same make and model)'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/vehicleModelDate.    
    vehicleType:    
      description: 'Type of vehicle from the point of view of its structural characteristics. This is different than the vehicle category . Enum:''agriculturalVehicle, anyVehicle, articulatedVehicle, bicycle, binTrolley, bus, car, caravan, carOrLightVehicle, carWithCaravan, carWithTrailer, cleaningTrolley, constructionOrMaintenanceVehicle, fourWheelDrive, highSidedVehicle, lorry, minibus, moped, motorcycle, motorcycleWithSideCar, motorscooter, sweepingMachine, tanker, threeWheeledVehicle, trailer, tram, twoWheeledVehicle, trolley, van, vehicleWithoutCatalyticConverter, vehicleWithCaravan, vehicleWithTrailer, withEvenNumberedRegistrationPlates, withOddNumberedRegistrationPlates, other''. The following values defined by _VehicleTypeEnum_ and _VehicleTypeEnum2_, [DATEX 2 version 2.3](http://d2docs.ndwcloud.nu/_static/umlmodel/v2.3/index.htm)'    
      enum:    
        - agriculturalVehicle    
        - bicycle    
        - binTrolley    
        - bus    
        - car    
        - caravan    
        - carWithCaravan    
        - carWithTrailer    
        - cleaningTrolley    
        - constructionOrMaintenanceVehicle    
        - lorry    
        - minibus    
        - moped    
        - motorcycle    
        - motorcycleWithSideCar    
        - motorscooter    
        - sweepingMachine    
        - tanker    
        - trailer    
        - tram    
        - van    
        - trolley    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    weight:    
      description: 'Vehicle''s weigth'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/weigth.    
    width:    
      description: 'Vehicle''s width'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/width.    
  required:    
    - id    
    - name    
    - type    
    - vehicleType    
    - brandName    
    - modelName    
    - manufacturerName    
  type: object    
```  
</details>    
## Example payloads    
#### VehicleModel NGSI V2 key-values Example    
Here is an example of a VehicleModel in JSON format as key-values. This is compatible with NGSI V2 when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
      "id": "vehiclemodel:econic",  
      "type": "VehicleModel",  
      "name": "MBenz-Econic2014",  
      "brandName": "Mercedes Benz",  
      "modelName": "Econic",  
      "manufacturerName": "Daimler",  
      "vehicleType": "lorry",  
      "cargoVolume": 1000,  
      "fuelType": "diesel"  
}  
```  
#### VehicleModel NGSI V2 normalized Example    
Here is an example of a VehicleModel in JSON format as normalized. This is compatible with NGSI V2 when not using options and returns the context data of an individual entity.  
```json  
{  
    "id": "vehiclemodel:econic",  
    "type": "VehicleModel",  
    "name": {  
        "value": "MBenz-Econic2014"  
    },  
    "cargoVolume": {  
        "value": 1000  
    },   
    "modelName": {  
        "value": "Econic"  
    },   
    "brandName": {  
        "value": "Mercedes Benz"  
    },  
    "manufacturerName": {  
        "value": "Daimler"  
    },   
    "fuelType": {  
        "value": "diesel"  
    },   
    "vehicleType": {  
        "value": "lorry"  
    }  
}  
```  
#### VehicleModel NGSI-LD key-values Example    
Here is an example of a VehicleModel in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context",  
              "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"],  
 "brandName": "Mercedes Benz",  
 "cargoVolume": 1000,  
 "fuelType": "diesel",  
 "id": "urn:ngsi-ld:VehicleModel:vehiclemodel:econic",  
 "manufacturerName": "Daimler",  
 "modelName": "Econic",  
 "name": "MBenz-Econic2014",  
 "type": "VehicleModel",  
 "vehicleType": "lorry"}  
```  
#### VehicleModel NGSI-LD normalized Example    
Here is an example of a VehicleModel in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
```json  
{  
    "id": "urn:ngsi-ld:VehicleModel:vehiclemodel:econic",  
    "type": "VehicleModel",  
    "name": {  
        "type": "Property",  
        "value": "MBenz-Econic2014"  
    },  
    "cargoVolume": {  
        "type": "Property",  
        "value": 1000  
    },  
    "modelName": {  
        "type": "Property",  
        "value": "Econic"  
    },  
    "brandName": {  
        "type": "Property",  
        "value": "Mercedes Benz"  
    },  
    "manufacturerName": {  
        "type": "Property",  
        "value": "Daimler"  
    },  
    "fuelType": {  
        "type": "Property",  
        "value": "diesel"  
    },  
    "vehicleType": {  
        "type": "Property",  
        "value": "lorry"  
    },  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  
