Entità: FleetVehicle  
====================  
[Licenza aperta](https://github.com/smart-data-models//dataModel.Transportation/blob/master/FleetVehicle/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descrizione globale: **Questa entità contiene una descrizione armonizzata di un veicolo generico della flotta come un veicolo di consegna, un'ambulanza o un veicolo postale. Questa entità è principalmente associata al segmento verticale del trasporto e della logistica, ma può anche essere utilizzata molte altre applicazioni IoT correlate.  

## Elenco delle proprietà  

- `address`: L'indirizzo postale  - `alternateName`: Un nome alternativo per questa voce  - `areaServed`: L'area geografica in cui viene fornito un servizio o un articolo offerto  - `dataProvider`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `dateCreated`: Timestamp di creazione dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `dateModified`: Timestamp dell'ultima modifica dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `description`: Una descrizione di questo articolo  - `fleetVehicleType`: Il tipo di veicolo per esempio (non limitato a) questi. Enum:'Taxi, Ambulanza, Postale, Fuoco e Salvataggio, Consegna'.  - `id`: Identificatore unico dell'entità  - `location`: Riferimento Geojson all'elemento. Può essere Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `name`: Il nome di questo articolo.  - `operatingCompany`: Dettagli dell'organizzazione che gestisce questo veicolo della flotta. Basato su Schema.org organizzazione  - `operator`: L'operatore/guidatore/custode abituale di questo veicolo della flotta codificato come una persona Schema.org  - `owner`: Una lista contenente una sequenza di caratteri codificata in JSON che si riferisce agli ID unici dei proprietari  - `seeAlso`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source`: Una sequenza di caratteri che dà la fonte originale dei dati dell'entità come URL. Si raccomanda di essere il nome di dominio completamente qualificato del fornitore di origine, o l'URL dell'oggetto di origine.  - `type`: Identificatore di entità NGSI. Deve essere FleetVehicle  - `vehicle`: Riferimento all'istanza dell'entità Vehicle correlata che descrive gli attributi principali di questo Fleet Vehicle.    
Proprietà richieste  
- `id`  - `type`    
Questo modello di dati proviene dal progetto originale GSMA IoT, https://www.gsma.com/iot/iot-big-data/. Ci sono alcuni adattamenti minori per soddisfare i requisiti dei modelli di dati intelligenti.  
## Descrizione del modello di dati delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
FleetVehicle:    
  description: 'This entity contains a harmonised description of a generic fleet vehicle such as a delivery vehicle, an ambulance or a postal vehicle. This entity is primarily associated with the vertical segment of the transport and logistics but may also be used many other related IoT applications.'    
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
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    fleetVehicleType:    
      description: 'The type of the Vehicle for example (not limited to) these ones. Enum:''Taxi, Ambulance, Postal, Fire & Rescue, Delivery'''    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &fleetvehicle_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      x-ngsi:    
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
      x-ngsi:    
        type: Geoproperty    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    operatingCompany:    
      description: 'Details of the organization that is operating this fleet vehicle. Based on Schema.org organization'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Organization    
        type: Property    
    operator:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'The usual operator/driver/keeper of this fleet vehicle encoded as a Schema.org person'    
      x-ngsi:    
        model: https://schema.org/Person    
        type: Relationship    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *fleetvehicle_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
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
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI Entity identifier. It has to be FleetVehicle'    
      enum:    
        - FleetVehicle    
      type: string    
      x-ngsi:    
        type: Property    
    vehicle:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Reference to the related Vehicle entity instance that describes the core attributes of this Fleet Vehicle.'    
      x-ngsi:    
        type: Relationship    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Transportation/blob/master/FleetVehicle/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/datamodel.Transportation/FleetVehicle/schema.json    
  x-model-tags: GSMA    
  x-version: 0.0.1    
```  
</details>    
## Esempio di payloads  
#### FleetVehicle NGSI-v2 valori chiave Esempio  
Ecco un esempio di un FleetVehicle in formato JSON-LD come key-values. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "id": "urn:ngsi-ld:FleetVehicle:630b8818-5aa2-11e8-91c6-bf6b90c0ad02",  
  "type": "FleetVehicle",  
  "source": "https://source.example.com",  
  "dataProvider": "https://provider.example.com",  
  "vehicle": "urn:ngsi-ld:Vehicle:76a67054-5aa2-11e8-b0ee-43cfe58d3cd1",  
  "fleetVehicleType": "Ambulance",  
  "operatingCompany": "NHS",  
  "operator": "urn:ngsi-ld:Person:fe018d4e-46f8-11e8-ae6b-df5577f85836"  
}  
```  
#### FleetVehicle NGSI-v2 normalizzato Esempio  
Ecco un esempio di un FleetVehicle in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "id": "urn:ngsi-ld:FleetVehicle:630b8818-5aa2-11e8-91c6-bf6b90c0ad02",  
  "type": "FleetVehicle",  
  "source": {  
    "type": "URL",  
    "value": "https://source.example.com"  
  },  
  "dataProvider": {  
    "type": "URL",  
    "value": "https://provider.example.com"  
  },  
  "vehicle": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:Vehicle:76a67054-5aa2-11e8-b0ee-43cfe58d3cd1"  
  },  
  "fleetVehicleType": {  
    "type": "Text",  
    "value": "Ambulance"  
  },  
  "operatingCompany": {  
    "type": "Text",  
    "value": "NHS"  
  },  
  "operator": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:Person:fe018d4e-46f8-11e8-ae6b-df5577f85836"  
  }  
}  
```  
#### FleetVehicle NGSI-LD valori chiave Esempio  
Ecco un esempio di un FleetVehicle in formato JSON-LD come key-values. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "@context": [  
    "https://smart-data-models.github.io/datamodel.Transportation/FleetVehicle/context.jsonld"  
  ],  
  "id": "urn:ngsi-ld:FleetVehicle:630b8818-5aa2-11e8-91c6-bf6b90c0ad02",  
  "type": "FleetVehicle",  
  "source": "https://source.example.com",  
  "dataProvider": "https://provider.example.com",  
  "vehicle": "urn:ngsi-ld:Vehicle:76a67054-5aa2-11e8-b0ee-43cfe58d3cd1",  
  "fleetVehicleType": "Ambulance",  
  "operatingCompany": "NHS",  
  "operator": "urn:ngsi-ld:Person:fe018d4e-46f8-11e8-ae6b-df5577f85836"  
}  
```  
#### FleetVehicle NGSI-LD normalizzato Esempio  
Ecco un esempio di un FleetVehicle in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "@context": [  
    "https://smart-data-models.github.io/datamodel.Transportation/FleetVehicle/context.jsonld"  
  ],  
  "id": "urn:ngsi-ld:FleetVehicle:630b8818-5aa2-11e8-91c6-bf6b90c0ad02",  
  "type": "FleetVehicle",  
  "source": {  
    "type": "Property",  
    "value": "https://source.example.com"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "https://provider.example.com"  
  },  
  "vehicle": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Vehicle:76a67054-5aa2-11e8-b0ee-43cfe58d3cd1"  
  },  
  "fleetVehicleType": {  
    "type": "Property",  
    "value": "Ambulance"  
  },  
  "operatingCompany": {  
    "type": "Property",  
    "value": {  
      "@type": "https://schema.org/Organization",  
      "@value": "NHS"  
    }  
  },  
  "operator": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Person:fe018d4e-46f8-11e8-ae6b-df5577f85836"  
  }  
}  
```  
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per avere una risposta su come trattare le unità di grandezza