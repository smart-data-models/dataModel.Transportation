Entità: FleetVehicleOperation  
=============================  
[Licenza aperta](https://github.com/smart-data-models//dataModel.Transportation/blob/master/FleetVehicleOperation/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descrizione globale: **Questa entità contiene una descrizione armonizzata di un'operazione generica del veicolo della flotta come una consegna o una raccolta postale. Questa entità è principalmente associata al segmento verticale del trasporto e della logistica, ma può anche essere utilizzata molte altre applicazioni IoT correlate.  

## Elenco delle proprietà  

- `address`: L'indirizzo postale  - `alternateName`: Un nome alternativo per questa voce  - `areaServed`: L'area geografica in cui viene fornito un servizio o un articolo offerto  - `dataProvider`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `dateCreated`: Timestamp di creazione dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `dateModified`: Timestamp dell'ultima modifica dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `description`: Una descrizione di questo articolo  - `endedAt`: La data e l'ora di fine dell'evento, quando si sa che l'evento o l'operazione sono finiti/completati. Null/omessa se non ancora terminata.  - `fleetVehicle`: Riferimento all'entità FleetVehicle a cui si riferisce questa operazione.  - `fleetVehicleOperation`: Riferimento all'entità FleetVehicleOperation a cui si riferisce questa entità di stato.  - `id`: Identificatore unico dell'entità  - `initiatingLocation`: Riferimento Geojson all'elemento. Può essere Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `location`: Riferimento Geojson all'elemento. Può essere Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `name`: Il nome di questo articolo.  - `operationType`: Il tipo di testo libero dell'evento o dell'operazione, ad esempio chiamata per il trasporto di un paziente, raccolta postale, consegna, vicino a un'area limitata, velocità eccessiva.  - `owner`: Una lista contenente una sequenza di caratteri codificata in JSON che si riferisce agli ID unici dei proprietari  - `responseTime`: Indica il tempo di risposta a un evento, in secondi. Il timestamp associato observedAt indica quando è stato registrato l'ultimo aggiornamento. Ad esempio, registra il tempo di risposta di un'ambulanza per raggiungere un paziente  - `result`: Il risultato finale dell'evento o dell'operazione.  - `seeAlso`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source`: Una sequenza di caratteri che dà la fonte originale dei dati dell'entità come URL. Si raccomanda di essere il nome di dominio completamente qualificato del fornitore di origine, o l'URL dell'oggetto di origine.  - `startedAt`: La data e l'ora di inizio dell'evento o dell'operazione.  - `transportTime`: Indica il tempo che il veicolo della flotta ha trascorso trasportando persone o forniture per l'operazione corrente. Ad esempio, indica il tempo che un'ambulanza ha trascorso trasportando un paziente al pronto soccorso di un ospedale.  - `type`: Identificatore di entità NGSI. Deve essere FleetVehicleOperation    
Proprietà richieste  
- `id`  - `type`    
Questo modello di dati proviene dal progetto originale GSMA IoT, https://www.gsma.com/iot/iot-big-data/. Ci sono alcuni adattamenti minori per soddisfare i requisiti dei modelli di dati intelligenti.  
## Descrizione del modello di dati delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
FleetVehicleOperation:    
  description: 'This entity contains a harmonised description of a generic fleet vehicle operation such as a delivery, or a postal collection. This entity is primarily associated with the vertical segment of the transport and logistics but may also be used many other related IoT applications.'    
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
    endedAt:    
      description: 'The end date and time of the event when the event or operation is known to be over/complete. Null/omitted if not yet ended.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    fleetVehicle:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Reference to the FleetVehicle entity to which this operation relates.'    
      x-ngsi:    
        type: Relationship    
    fleetVehicleOperation:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Reference to the FleetVehicleOperation entity to which this status entity relates.'    
      x-ngsi:    
        type: Relationship    
    id:    
      anyOf: &fleetvehicleoperation_-_properties_-_owner_-_items_-_anyof    
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
    initiatingLocation:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf: &fleetvehicleoperation_-_properties_-_location_-_oneof    
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
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf: *fleetvehicleoperation_-_properties_-_location_-_oneof    
      x-ngsi:    
        type: Geoproperty    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    operationType:    
      description: 'The free text type of the event or operation e.g. e.g. Call for a patient transportation, postal collection, delivery, close to a restricted area, overspeed.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *fleetvehicleoperation_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    responseTime:    
      description: 'Indicates the time to respond to an event, in seconds. The associated observedAt timestamp indicates when the last update was recorded. E.g. records the response time for an ambulance to reach to a patient'    
      type: number    
      x-ngsi:    
        type: Property    
        units: seconds    
    result:    
      description: 'The final result of the event or operation.'    
      type: string    
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
    startedAt:    
      description: 'The start date and time when the event or operation was triggered.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    transportTime:    
      description: 'Indicates the time that the fleet vehicle has spent transporting people or supplies for the current operation. E.g. indicates the time an ambulance spent transporting a patient to a hospital emergency department.'    
      type: number    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI Entity identifier. It has to be FleetVehicleOperation'    
      enum:    
        - FleetVehicleOperation    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Transportation/blob/master/FleetVehicleOperation/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Transportation/FleetVehicleOperation/schema.json    
  x-model-tags: GSMA    
  x-version: 0.0.1    
```  
</details>    
## Esempio di payloads  
#### FleetVehicleOperation NGSI-v2 valori chiave Esempio  
Ecco un esempio di una FleetVehicleOperation in formato JSON-LD come valori chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "id": "urn:ngsi-ld:FleetVehicleOperation:8e876a60-5aa3-11e8-b350-d7b51a09fb6c",  
  "type": "FleetVehicleOperation",  
  "source": "https://source.example.com",  
  "dataProvider": "https://provider.example.com",  
  "fleetVehicle": "urn:ngsi-ld:FleetVehicle:84c6a3a8-5aa6-11e8-bedc-27e105edd16f",  
  "fleetVehicleStatus": "urn:ngsi-ld:FleetVehicleStatus:0284e0dc-5aa4-11e8-97e6-2351fc70c286",  
  "initiatingLocation": {  
    "type": "Point",  
    "coordinates": [  
      -104.99404,  
      39.75621  
    ]  
  },  
  "startedAt": "2016-08-22T10:18:16Z",  
  "endedAt": "2016-08-28T10:18:16Z",  
  "operationType": "Patient transportation",  
  "description": "An emergency transportation of a 3 year old boy",  
  "result": "Completed",  
  "responseTime": 2500,  
  "transportTime": 1220  
}  
```  
#### FleetVehicleOperation NGSI-v2 normalizzato Esempio  
Ecco un esempio di una FleetVehicleOperation in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "id": "urn:ngsi-ld:FleetVehicleOperation:8e876a60-5aa3-11e8-b350-d7b51a09fb6c",  
  "type": "FleetVehicleOperation",  
  "source": {  
    "type": "URL",  
    "value": "https://source.example.com"  
  },  
  "dataProvider": {  
    "type": "URL",  
    "value": "https://provider.example.com"  
  },  
  "fleetVehicle": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:FleetVehicle:84c6a3a8-5aa6-11e8-bedc-27e105edd16f"  
  },  
  "fleetVehicleStatus": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:FleetVehicleStatus:0284e0dc-5aa4-11e8-97e6-2351fc70c286"  
  },  
  "initiatingLocation": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -104.99404,  
        39.75621  
      ]  
    }  
  },  
  "startedAt": {  
    "type": "DateTime",  
    "value": "2016-08-22T10:18:16Z"  
  },  
  "endedAt": {  
    "type": "DateTime",  
    "@value": "2016-08-28T10:18:16Z"  
  },  
  "operationType": {  
    "type": "Text",  
    "value": "Patient transportation"  
  },  
  "description": {  
    "type": "Text",  
    "value": "An emergency transportation of a 3 year old boy"  
  },  
  "result": {  
    "type": "Property",  
    "value": "Completed"  
  },  
  "responseTime": {  
    "type": "Number",  
    "value": 2500  
  },  
  "transportTime": {  
    "type": "Number",  
    "value": 1220  
  }  
}  
```  
#### FleetVehicleOperation valori chiave NGSI-LD Esempio  
Ecco un esempio di una FleetVehicleOperation in formato JSON-LD come valori chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "@context": [  
    "https://smart-data-models.github.io/dataModel.Transportation/FleetVehicleOperation/context.jsonld"  
  ],  
  "id": "urn:ngsi-ld:FleetVehicleOperation:8e876a60-5aa3-11e8-b350-d7b51a09fb6c",  
  "type": "FleetVehicleOperation",  
  "source": "https://source.example.com",  
  "dataProvider": "https://provider.example.com",  
  "fleetVehicle": "urn:ngsi-ld:FleetVehicle:84c6a3a8-5aa6-11e8-bedc-27e105edd16f",  
  "fleetVehicleStatus": "urn:ngsi-ld:FleetVehicleStatus:0284e0dc-5aa4-11e8-97e6-2351fc70c286",  
  "initiatingLocation": {  
    "type": "Point",  
    "coordinates": [  
      -104.99404,  
      39.75621  
    ]  
  },  
  "startedAt": "2016-08-22T10:18:16Z",  
  "endedAt": "2016-08-28T10:18:16Z",  
  "operationType": "Patient transportation",  
  "description": "An emergency transportation of a 3 year old boy",  
  "result": "Completed",  
  "responseTime": 2500,  
  "transportTime": 1220  
}  
```  
#### FleetVehicleOperation NGSI-LD normalizzato Esempio  
Ecco un esempio di una FleetVehicleOperation in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "@context": [  
    "https://smart-data-models.github.io/dataModel.Transportation/FleetVehicleOperation/context.jsonld"  
  ],  
  "id": "urn:ngsi-ld:FleetVehicleOperation:8e876a60-5aa3-11e8-b350-d7b51a09fb6c",  
  "type": "FleetVehicleOperation",  
  "source": {  
    "type": "Property",  
    "value": "https://source.example.com"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "https://provider.example.com"  
  },  
  "fleetVehicle": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:FleetVehicle:84c6a3a8-5aa6-11e8-bedc-27e105edd16f"  
  },  
  "fleetVehicleStatus": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:FleetVehicleStatus:0284e0dc-5aa4-11e8-97e6-2351fc70c286"  
  },  
  "initiatingLocation": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -104.99404,  
        39.75621  
      ]  
    }  
  },  
  "startedAt": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2016-08-22T10:18:16Z"  
    }  
  },  
  "endedAt": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2016-08-28T10:18:16Z"  
    }  
  },  
  "operationType": {  
    "type": "Property",  
    "value": "Patient transportation"  
  },  
  "description": {  
    "type": "Property",  
    "value": "An emergency transportation of a 3 year old boy"  
  },  
  "result": {  
    "type": "Property",  
    "value": "Completed"  
  },  
  "responseTime": {  
    "type": "Property",  
    "value": 2500,  
    "unitCode": "SEC",  
    "observedAt": "2016-08-28T10:18:16Z"  
  },  
  "transportTime": {  
    "type": "Property",  
    "value": 1220,  
    "unitCode": "SEC",  
    "observedAt": "2016-08-28T10:18:16Z"  
  }  
}  
```  
