Entidad: RestrictionException  
=============================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.Transportation/blob/master/RestrictionException/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descripción global: **Una Excepción de Restricción representa un caso particular que especializa la restricción reportada en una Zona de Tráfico Restringido; por ejemplo podría describir permisos particulares aplicados a vehículos de tipo específico**  

## Lista de propiedades  

- `address`: La dirección postal  - `allowedVehicleType`: Tipo de vehículo(s) autorizado(s) a cruzar la zona de tráfico restringido.  - `alternateName`: Un nombre alternativo para este artículo  - `areaServed`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `description`: Una descripción de este artículo  - `exceptionValidityHours`: Días de la semana y horas en que la excepción es válida  - `id`: Identificador único de la entidad  - `location`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `name`: El nombre de este artículo.  - `owner`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `refRestrictedTrafficArea`: La zona de tráfico restringido a la que pertenece esta excepción.  - `refVehicleModel`: Especifique las características del vehículo para el que se ha establecido la excepción  - `seeAlso`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `type`: Tipo de entidad NGSI. Tiene que ser RestrictionException    
Propiedades requeridas  
- `allowedVehicleType`  - `id`  - `refRestrictedTrafficArea`  - `type`    
Modelo de datos procedente del proyecto synchronicity  
## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
RestrictionException:    
  description: 'A Restriction Exception represents a particular case that specialise restriction reported in a Restricted Traffic Areas; for instance it could describe particular permissions applied to specific kind vehicles'    
  properties:    
    address:    
      description: 'The mailing address'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/addressCountry'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/addressLocality'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/addressRegion'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/address    
    allowedVehicleType:    
      description: 'Vehicle type(s) allowed to cross the restricted traffic area.'    
      items:    
        enum:    
          - anyVehicle    
          - agriculturalVehicle    
          - bicycle    
          - bus    
          - car    
          - caravan    
          - carWithCaravan    
          - carWithTrailer    
          - constructionOrMaintenanceVehicle    
          - dieselCarEuro0    
          - dieselCarEuro1    
          - dieselCarEuro2    
          - dieselCarEuro3    
          - dieselCarEuro4    
          - dieselCarEuro5a    
          - dieselCarEuro5b    
          - dieselCarEuro6    
          - freightTransportVehicle    
          - lorry    
          - moped    
          - motorcycle    
          - motorcycleWithSideCar    
          - motorscooter    
          - petrolCarEuro0    
          - petrolCarEuro1    
          - petrolCarEuro2    
          - petrolCarEuro3    
          - petrolCarEuro4    
          - petrolCarEuro5    
          - petrolCarEuro6    
          - tanker    
          - trailer    
          - van    
        type: string    
      minItems: 1    
      type: Property    
      uniqueItems: true    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
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
    description:    
      description: 'A description of this item'    
      type: Property    
    exceptionValidityHours:    
      description: 'Days of the week and hours in which the exception is valid'    
      type: Property    
      x-ngsi:    
        model: 'http://schema.org/openingHours '    
    id:    
      anyOf: &restrictionexception_-_properties_-_owner_-_items_-_anyof    
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
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'Geoproperty. Geojson reference to the item. Point'    
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
          title: 'GeoJSON Point'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. LineString'    
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
          title: 'GeoJSON LineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. Polygon'    
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
          title: 'GeoJSON Polygon'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiPoint'    
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
          title: 'GeoJSON MultiPoint'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
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
          title: 'GeoJSON MultiLineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
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
          title: 'GeoJSON MultiPolygon'    
          type: object    
      type: Geoproperty    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *restrictionexception_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    refRestrictedTrafficArea:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'The Restricted Traffic Area this exception belongs.'    
      type: Relationship    
    refVehicleModel:    
      description: 'Specify characteristics of the vehicle for which the exception has been established'    
      items:    
        anyOf: *restrictionexception_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            format: uri    
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
      description: 'NGSI Entity type. It has to be RestrictionException'    
      enum:    
        - RestrictionException    
      type: Property    
  required:    
    - id    
    - type    
    - allowedVehicleType    
    - refRestrictedTrafficArea    
  type: object    
```  
</details>    
## Ejemplo de carga útil  
#### RestrictionException Ejemplo de valores clave NGSI-v2  
Aquí hay un ejemplo de una RestrictionException en formato JSON-LD como valores-clave. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:RestrictedTrafficArea:Milan:RestrictionException:GeoJson:ds51-1",  
  "type": "RestrictionException",  
  "name": "Corso Concordia Area",  
  "allowedVehicleType": [  
    "dieselCarEuro6",  
    "petrolCarEuro6"  
  ],  
  "exceptionValidityHours": "Tu,Th 16:00-20:00",  
  "refVehicleModel": [  
    "vehicle:VehicleModel:modelName-1"  
  ],  
  "refRestrictedTrafficArea": "urn:ngsi-ld:RestrictedTrafficArea:Milan:RestrictedTrafficAreas:GeoJson:ds51-1"  
}  
```  
#### RestrictionException NGSI-v2 normalizado Ejemplo  
Este es un ejemplo de una RestrictionException en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:RestrictedTrafficArea:Milan:RestrictionException:GeoJson:ds51-1",  
  "type": "RestrictionException",  
  "name": {  
    "type": "string",  
    "value": "Corso Concordia Area"  
  },  
  "allowedVehicleType": {  
    "type": "array",  
    "value": [  
      "dieselCarEuro6",  
      "petrolCarEuro6"  
    ]  
  },  
  "exceptionValidityHours": {  
    "type": "string",  
    "value": "Tu,Th 16:00-20:00"  
  },  
  "refVehicleModel": {  
    "type": "string",  
    "Object": "vehicle:VehicleModel:modelName-1"  
  },  
  "refRestrictedTrafficArea": {  
    "type": "string",  
    "Object": "urn:ngsi-ld:RestrictedTrafficArea:Milan:RestrictedTrafficAreas:GeoJson:ds51-1"  
  }  
}  
```  
#### RestrictionException Ejemplo de valores clave NGSI-LD  
Aquí hay un ejemplo de una RestrictionException en formato JSON-LD como valores-clave. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:RestrictedTrafficArea:Milan:RestrictionException:GeoJson:ds51-1",  
  "type": "RestrictionException",  
  "name": {  
    "type": "string",  
    "value": "Corso Concordia Area"  
  },  
  "allowedVehicleType": {  
    "type": "array",  
    "value": [  
      "dieselCarEuro6",  
      "petrolCarEuro6"  
    ]  
  },  
  "exceptionValidityHours": {  
    "type": "string",  
    "value": "Tu,Th 16:00-20:00"  
  },  
  "refVehicleModel": {  
    "type": "string",  
    "Object": "vehicle:VehicleModel:modelName-1"  
  },  
  "refRestrictedTrafficArea": {  
    "type": "string",  
    "Object": "urn:ngsi-ld:RestrictedTrafficArea:Milan:RestrictedTrafficAreas:GeoJson:ds51-1"  
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/data-models/master/context.jsonld"  
  ]  
}  
```  
#### RestrictionException NGSI-LD normalizado Ejemplo  
Este es un ejemplo de una RestrictionException en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:RestrictedTrafficArea:Milan:RestrictionException:GeoJson:ds51-1",  
  "type": "RestrictionException",  
  "name": "Corso Concordia Area",  
  "allowedVehicleType": [  
    "dieselCarEuro6",  
    "petrolCarEuro6"  
  ],  
  "exceptionValidityHours": "Tu,Th 16:00-20:00",  
  "refVehicleModel": [  
    "vehicle:VehicleModel:modelName-1"  
  ],  
  "refRestrictedTrafficArea": "urn:ngsi-ld:RestrictedTrafficArea:Milan:RestrictedTrafficAreas:GeoJson:ds51-1",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/data-models/master/context.jsonld"  
  ]  
}  
```  
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud