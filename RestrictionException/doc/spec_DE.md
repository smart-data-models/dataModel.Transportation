Entität: RestrictionException  
=============================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.Transportation/blob/master/RestrictionException/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Globale Beschreibung: **Eine Einschränkungsausnahme stellt einen besonderen Fall dar, der eine in einem eingeschränkten Verkehrsbereich gemeldete Einschränkung spezialisiert; sie könnte z. B. besondere Berechtigungen beschreiben, die für Fahrzeuge einer bestimmten Art gelten**  

## Liste der Eigenschaften  

- `address`: Die Postanschrift  - `allowedVehicleType`: Fahrzeugtyp(en), der/die den gesperrten Verkehrsbereich durchqueren darf/dürfen.  - `alternateName`: Ein alternativer Name für diesen Artikel  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `dataProvider`: Eine Folge von Zeichen, die den Anbieter der harmonisierten Dateneinheit identifiziert.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `exceptionValidityHours`: Wochentage und Stunden, in denen die Ausnahme gültig ist  - `id`: Eindeutiger Bezeichner der Entität  - `location`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `name`: Der Name dieses Elements.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Ids der Eigentümer verweist  - `refRestrictedTrafficArea`: Zum Bereich mit eingeschränktem Verkehr gehört diese Ausnahme.  - `refVehicleModel`: Geben Sie die Merkmale des Fahrzeugs an, für das die Ausnahme festgelegt wurde  - `seeAlso`: Liste von uri, die auf zusätzliche Ressourcen über das Element verweist  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL zum Quellobjekt.  - `type`: NGSI Entity-Typ. Es muss RestrictionException sein    
Erforderliche Eigenschaften  
- `allowedVehicleType`  - `id`  - `refRestrictedTrafficArea`  - `type`    
Datenmodell aus dem Synchronizitätsprojekt  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
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
## Beispiel-Nutzlasten  
#### RestrictionException NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für eine RestrictionException im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2 bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
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
#### RestrictionException NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für eine RestrictionException im JSON-LD-Format wie normalisiert. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und gibt die Kontextdaten einer einzelnen Entität zurück.  
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
#### RestrictionException NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für eine RestrictionException im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
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
#### RestrictionException NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für eine RestrictionException im JSON-LD-Format wie normalisiert. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und gibt die Kontextdaten einer einzelnen Entität zurück.  
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
Siehe [FAQ 10](https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht