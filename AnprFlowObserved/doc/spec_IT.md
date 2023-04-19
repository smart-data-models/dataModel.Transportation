<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: AnprFlowObserved  
========================<!-- /10-Header -->  
<!-- 15-License -->  
[Licenza aperta](https://github.com/smart-data-models//dataModel.Transportation/blob/master/AnprFlowObserved/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descrizione globale: **Il modello di dati rappresenta un'osservazione legata al passaggio di un veicolo in un determinato luogo e in un determinato momento. Questo modello di dati si basa su [dataModel.Transportation/ItemFlowObserved], esteso con proprietà specifiche ANPR e collegamenti alle immagini dell'osservazione.**  
versione:  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Elenco delle proprietà  

<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.  
- `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nome alternativo per questa voce  - `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `dateCreated[string]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione.  - `dateModified[string]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione.  - `dateObserved[string]`: Data dell'entità osservata definita dall'utente.  - `dateReceived[string]`: Proprietà. Timestamp in cui l'osservazione è stata ricevuta dalla piattaforma.  - `description[string]`: Descrizione dell'articolo  - `id[*]`: Identificatore univoco dell'entità  - `laneId[string]`: Proprietà. Identificatore di corsia. Identificazione della corsia fornita dall'osservatore.  - `location[*]`: Riferimento geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `name[string]`: Il nome di questo elemento.  - `observedBy[*]`: Relazione. L'entità o il dispositivo che ha segnalato l'osservazione  - `observedVehicle[object]`: Proprietà. Informazioni sul veicolo osservato.  - `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `refImages[array]`: Relazione. Array di oggetti multipli che si riferiscono alle immagini.  - `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `type[string]`: Proprietà. Tipo di entità NGSI. Deve essere AnprFlowObserved  - `vehiclePlateNotRead[boolean]`: Proprietà. Indica se non è stato possibile leggere una licenza  - `zonesServed[array]`: Array di zone che sono in grado di ricevere o leggere le osservazioni  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Proprietà richieste  
- `dateObserved`  - `id`  - `location`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Questo modello di dati descrive le principali entità coinvolte nelle applicazioni intelligenti che si occupano di questioni di polizia. Questo insieme di entità è principalmente associato ai segmenti verticali Automotive e Smart City e alle relative applicazioni IoT. Quando possibile, sono inclusi riferimenti a tipi di entità e attributi esistenti di schema.org. Questo modello è stato concepito per essere il più generico possibile, in modo da poter essere utilizzato da diversi dipartimenti di polizia e zone come ANPR, controllo della traiettoria e veicoli della polizia.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Modello di dati descrizione delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
AnprFlowObserved:    
  description: 'The data model represents an observation linked to the passing of a vehicle at a certain location and at a given time. This Data Model is based on the [dataModel.Transportation/ItemFlowObserved], extended with ANPR specific properties and links to the observation images.'    
  properties:    
    address:    
      description: The mailing address    
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
        district:    
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government.'    
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
        streetNr:    
          description: Number identifying a specific property on a public street.    
          type: string    
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
      description: A sequence of characters identifying the provider of the harmonised data entity.    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: Entity creation timestamp. This will usually be allocated by the storage platform.    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateObserved:    
      description: Date of the observed entity defined by the user.    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateReceived:    
      description: Property. Timestamp when the observation has been received by the platform.    
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
      anyOf: &anprflowobserved_-_properties_-_owner_-_items_-_anyof    
        - description: Property. Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: Property. Identifier format of any NGSI entity    
          format: uri    
          type: string    
      description: Unique identifier of the entity    
      x-ngsi:    
        type: Property    
    laneId:    
      description: Property. Lane identifier. Lane identification provided by the observer.    
      type: string    
      x-ngsi:    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf: &anprflowobserved_-_properties_-_observedvehicle_-_properties_-_licenseplate_-_properties_-_coordinates_-_oneof    
        - description: GeoProperty. Geojson reference to the item. Point    
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
        - description: GeoProperty. Geojson reference to the item. LineString    
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
        - description: GeoProperty. Geojson reference to the item. Polygon    
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
        - description: GeoProperty. Geojson reference to the item. MultiPoint    
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
        - description: GeoProperty. Geojson reference to the item. MultiLineString    
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
        - description: GeoProperty. Geojson reference to the item. MultiLineString    
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
    name:    
      description: The name of this item.    
      type: string    
      x-ngsi:    
        type: Property    
    observedBy:    
      anyOf:    
        - description: Property. Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: Property. Identifier format of any NGSI entity    
          format: uri    
          type: string    
      description: Relationship. The entity or device which has reported this observation    
      x-ngsi:    
        type: Relationship    
    observedVehicle:    
      description: Property. Information about the observed vehicle.    
      properties:    
        brand:    
          description: Property. Detected brand of the observed vehicle.    
          properties:    
            confidence:    
              description: Property. Confidence level of the detection    
              maximum: 1    
              minimum: 0    
              type: number    
            name:    
              description: Property. Brand name identified    
              type: string    
          type: object    
        color:    
          description: Property. Detected color of the observed vehicle.    
          properties:    
            confidence:    
              description: Property. Confidence level of the detection.    
              maximum: 1    
              minimum: 0    
              type: number    
            name:    
              description: Property. Color name.    
              type: string    
          type: object    
        country:    
          description: Property. Detected country of the observed vehicle.    
          properties:    
            code:    
              description: Property. Country code according to ISO 3166-1 alpha-2    
              type: string    
            confidence:    
              description: Property. Confidence level of the detection.    
              maximum: 1    
              minimum: 0    
              type: number    
          type: object    
        direction:    
          description: Property. Detected direction of the observed vehicle.    
          enum:    
            - away    
            - towards    
          type: string    
        licensePlate:    
          description: Property. Detected license plate of the observed vehicle.    
          properties:    
            confidence:    
              description: Property. Confidence level of the detection.    
              maximum: 1    
              minimum: 0    
              type: number    
            coordinates:    
              description: 'GeoProperty. Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
              oneOf: *anprflowobserved_-_properties_-_observedvehicle_-_properties_-_licenseplate_-_properties_-_coordinates_-_oneof    
            identifier:    
              description: Property. License plate identifier    
              type: string    
          required:    
            - identifier    
          type: object    
        model:    
          description: Property. Detected brand model of the observed vehicle.    
          properties:    
            confidence:    
              description: Property. Confidence level of the detection.    
              maximum: 1    
              minimum: 0    
              type: number    
            name:    
              description: Property. Model name.    
              type: string    
          type: object    
        speed:    
          description: Property. Detected speed of the observed vehicle.    
          minimum: 0    
          type: number    
      type: object    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf: *anprflowobserved_-_properties_-_owner_-_items_-_anyof    
        description: Property. Unique identifier of the entity    
      type: array    
      x-ngsi:    
        type: Property    
    refImages:    
      description: Relationship. Array of multiple objects that refer to images.    
      items:    
        - properties:    
            contentType:    
              description: Property. Content type according to IANA Media Types.    
              type: string    
            imageType:    
              description: Property. Type of image    
              enum:    
                - plate    
                - overview    
                - anpr    
              type: string    
            url:    
              description: Property. URL referencing to the image    
              format: uri    
              type: string    
          required:    
            - url    
            - contentType    
            - imageType    
          type: object    
      type: array    
      x-ngsi:    
        type: Relationship    
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: Property. NGSI Entity type. It has to be AnprFlowObserved    
      enum:    
        - AnprFlowObserved    
      type: string    
      x-ngsi:    
        type: Property    
    vehiclePlateNotRead:    
      description: Property. Indicates if a license could not be read    
      type: boolean    
      x-ngsi:    
        type: Property    
    zonesServed:    
      description: Array of zones that are able to receive or read the observations    
      items:    
        type: string    
      type: array    
  required:    
    - id    
    - type    
    - location    
    - dateObserved    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Transportation/blob/master/AnprFlowObserved/LICENSE.md    
  x-model-schema: https://gitlab.inuits.io/tom.vda/dataModel.Police/AnprFlowObserved/schema.json    
  x-model-tags: ""    
  x-version: ""    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Esempi di payload  
#### AnprFlowObserved NGSI-v2 valori-chiave Esempio  
Ecco un esempio di AnprFlowObserved in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "anprFlowObserved:LEZ-Noorderlaan",  
  "type": "AnprFlowObserved",  
  "address": {  
    "addressCountry": "BE",  
    "addressLocality": "Antwerp",  
    "streetAddress": "Noorderlaan"  
  },  
  "dateObserved": "2022-09-01T16:30:00Z",  
  "dateReceived": "2022-09-01T16:35:00Z",  
  "observedBy": "ANPR1_Noorderlaan",  
  "laneId": "ABC123",  
  "areaServed":"Antwerp",  
  "zonesServed": [  
      "Antwerp"  
    ],  
  "vehiclePlateNotRead": false,  
  "observedVehicle": {  
    "direction": "towards",  
    "speed": 50,  
    "brand":{  
      "name": "Audi",  
      "confidence": 0.97  
    },  
    "model":{  
      "name": "A3",  
      "confidence": 0.98  
    },  
    "color":{  
      "name": "black",  
      "confidence": 0.95  
    },  
    "country":{  
      "code": "BE",  
      "confidence":0.95  
    },  
    "licensePlate":{  
      "identifier": "1-ABC-123",  
      "confidence": 0.96  
    }   
  },  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -56.6404505,  
      168.370658  
    ]  
  },  
  "refImages":[  
    {  
      "contentType": "image/jpg",  
      "imageType": "anpr",  
      "url": "urn:ngsi-ld:ANPR:items:123"  
    }  
  ]  
}  
```  
</details>  
#### AnprFlowObserved NGSI-v2 normalizzato Esempio  
Ecco un esempio di AnprFlowObserved in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "anprFlowObserved:LEZ-Noorderlaan",  
  "type": "AnprFlowObserved",  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "addressCountry": "BE",  
      "addressLocality": "Antwerp",  
      "streetAddress": "Noorderlaan"  
    }  
  },  
  "dateObserved": {  
    "type": "DateTime",  
    "@value": "2022-09-01T16:30:00Z"  
  },  
  "laneId": {  
    "type": "Text",  
    "value": "ABC123"  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Antwerp"  
  },  
  "zonesServed": {  
    "type": "StructuredValue",  
    "value": {  
      "type": "string",  
      "coordinates": [  
        "Antwerp"  
      ]  
    }  
  },  
  "vehiclePlateNotRead": {  
    "type": "Boolean",  
    "value": false  
  },  
  "observedVehicle": {  
    "type": "StructuredValue",  
    "value": {  
      "direction": "towards",  
      "speed": 50,  
      "brand": "Audi",  
      "model": "A3",  
      "color": "black",  
      "country": "BE",  
      "licensePlate": "1-ABC-123"  
    }  
  },  
  "refImages": {  
    "type": "StructuredValue",  
    "value": {  
      "type": "s3://bucket/object-xxx-plate",  
      "contentType": "image/jpg",  
      "imageType": "anpr"  
    }  
  }  
}  
```  
</details>  
#### Valori chiave NGSI-LD di AnprFlowObserved Esempio  
Ecco un esempio di AnprFlowObserved in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "anprFlowObserved:LEZ-Noorderlaan",  
  "type": "AnprFlowObserved",  
  "address": {  
    "addressCountry": "BE",  
    "addressLocality": "Antwerp",  
    "streetAddress": "Noorderlaan"  
  },  
  "dateObserved": "2022-09-01T16:30:00Z",  
  "dateReceived": "2022-09-01T16:35:00Z",  
  "observedBy": "ANPR1_Noorderlaan",  
  "laneId": "ABC123",  
  "areaServed":"Antwerp",  
  "zonesServed": [  
      "Antwerp"  
    ],  
  "vehiclePlateNotRead": false,  
  "observedVehicle": {  
    "direction": "towards",  
    "speed": 50,  
    "brand":{  
      "name": "Audi",  
      "confidence": 0.97  
    },  
    "model":{  
      "name": "A3",  
      "confidence": 0.98  
    },  
    "color":{  
      "name": "black",  
      "confidence": 0.95  
    },  
    "country":{  
      "code": "BE",  
      "confidence":0.95  
    },  
    "licensePlate":{  
      "identifier": "1-ABC-123",  
      "confidence": 0.96  
    }   
  },  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -56.6404505,  
      168.370658  
    ]  
  },  
  "refImages":[  
    {  
      "contentType": "image/jpg",  
      "imageType": "anpr",  
      "url": "urn:ngsi-ld:ANPR:items:123"  
    }  
  ],  
    "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Transportation/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### AnprFlowObserved NGSI-LD normalizzato Esempio  
Ecco un esempio di AnprFlowObserved in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "anprFlowObserved:LEZ-Noorderlaan",  
  "type": "AnprFlowObserved",  
  "address": {  
    "type": "Property",  
    "value": {  
      "addressCountry": "BE",  
      "addressLocality": "Antwerp",  
      "streetAddress": "Noorderlaan"  
    }  
  },  
  "dateObserved": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2022-09-01T16:30:00Z"  
    }  
  },  
  "laneId": {  
    "type": "Property",  
    "value": "ABC123"  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Antwerp"  
  },  
  "zonesServed": {  
    "type": "Property",  
    "value": {  
      "type": "string",  
      "coordinates": [  
        "Antwerp"  
      ]  
    }  
  },  
  "vehiclePlateNotRead": {  
    "type": "Property",  
    "value": false  
  },  
  "observedVehicle": {  
    "type": "Property",  
    "value": {  
      "direction": "towards",  
      "speed": 50,  
      "brand": "Audi",  
      "model": "A3",  
      "color": "black",  
      "country": "BE",  
      "licensePlate": "1-ABC-123"  
    }  
  },  
  "refImages": {  
    "type": "Property",  
    "value": {  
      "type": "s3://bucket/object-xxx-plate",  
      "contentType": "image/jpg",  
      "imageType": "anpr"  
    }  
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
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di grandezza.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
