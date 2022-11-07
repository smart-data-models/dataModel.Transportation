<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: AnonimoCommuterId  
=========================<!-- /10-Header -->  
<!-- 15-License -->  
[Licenza aperta](https://github.com/smart-data-models//dataModel.Transportation/blob/master/AnonymousCommuterId/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descrizione globale: **Identificatore anonimizzato per il monitoraggio dei flussi. Include una proprietà di origine e una di destino per mappare il suo percorso **.  
versione: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Elenco delle proprietà  

<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.  
- `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)- `algorithm[string]`: Nome dell'algoritmo utilizzato per rendere anonimo l'Id  - `alternateName[string]`: Un nome alternativo per questa voce  - `anonymizedId[string]`: Identificatore anonimizzato  - `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `date[string]`: Data dell'identificatore anonimo rilevato.  - `dateCreated[string]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione.  - `dateModified[string]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione.  - `description[string]`: Descrizione dell'articolo  - `dest[string]`: Valore stringa dell'id di destinazione, entità effettiva in cui è stato rilevato l'id anonimo.  - `id[*]`: Identificatore univoco dell'entità  - `location[*]`: Riferimento geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `name[string]`: Il nome di questo elemento.  - `orig[string]`: Valore stringa dell'id di origine, ultima entità in cui è stato rilevato l'id anonimo.  - `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Valore stringa della fonte di questo AnonymousCommuterId, ad esempio (ALPR, monitoraggio persone, riconoscimento facciale, ecc...)  - `type[string]`: Tipo di entità NGSI. Deve essere AnonymousCommuterId  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Proprietà richieste  
- `anonymizedId`  - `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Modello di dati descrizione delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
AnonymousCommuterId:    
  description: 'Anonymized identifier for flow monitoring. Includes an origin and destiny property to map its path.'    
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
    algorithm:    
      description: 'Name of the algorithm used to anonymize the Id'    
      type: string    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    anonymizedId:    
      description: 'Anonymized identifier'    
      type: string    
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
    date:    
      description: 'Date of the detected anonymous identifier.'    
      format: date-time    
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
    dest:    
      description: 'String value of destination id, actual entity where the anonymous id was detected.'    
      type: string    
    id:    
      anyOf: &anonymouscommuterid_-_properties_-_owner_-_items_-_anyof    
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
    orig:    
      description: 'String value of origin id, last entity where the anonymous id was detected.'    
      type: string    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *anonymouscommuterid_-_properties_-_owner_-_items_-_anyof    
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
      description: 'String value of source of this AnonymousCommuterId, eg. (ALPR, People Monitoring, Face Recognition, etc...)'    
      type: string    
    type:    
      description: 'NGSI entity type. It has to be AnonymousCommuterId'    
      enum:    
        - AnonymousCommuterId    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - anonymizedId    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Transportation/blob/master/AnonymousCommuterId/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Transportation/AnonymousCommuterId/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Esempi di payload  
#### AnonymousCommuterId Valori chiave NGSI-v2 Esempio  
Ecco un esempio di AnonymousCommuterId in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "ngsi-ld:HUES:001",  
    "anonymizedId": "D20220AC3478565F",  
    "type": "AnonymousCommuterId",  
    "date": "2022-09-05T08:25:35.00Z",  
    "orig": "City hall",  
    "dest": "Library",  
    "source": "People Monitoring",  
    "algorithm": "SHA1",  
    "dateCreated": "2022-09-05T09:25:35.00Z",  
    "dateModified": "2022-09-12T09:25:35.00Z",  
    "location": {  
        "type": "Point",  
        "coordinates": [  
            43.23161118206764,  
            -2.844695196525928  
        ]  
    }  
}  
```  
</details>  
#### AnonymousCommuterId NGSI-v2 normalizzato Esempio  
Ecco un esempio di AnonymousCommuterId in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si usano le opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
   "id": "ngsi-ld:HUES:001",  
    "anonymizedId": {  
        "type": "Text",  
        "value": "D20220AC3478565F"  
    },  
    "type": "AnonymousCommuterId",  
    "orig": {  
        "type": "Text",  
        "value": "City hall"  
    },  
    "dest": {  
        "type": "Text",  
        "value": "Library"  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                43.23161118206764,  
                -2.844695196525928  
            ]  
        }  
    },  
    "date": {  
        "type": "DateTime",  
        "value": "2022-09-05T08:25:35.00Z"  
    },  
    "algorithm": {  
        "type": "Text",  
        "value": "SHA1"  
    },  
    "dateCreated": {  
        "type": "DateTime",  
        "value": "2022-09-05T09:25:35.00Z"  
    },  
    "dateModified": {  
        "type": "DateTime",  
        "value": "2022-09-12T09:25:35.00Z"  
    }  
}  
```  
</details>  
#### AnonymousCommuterId Valori chiave NGSI-LD Esempio  
Ecco un esempio di AnonymousCommuterId in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "ngsi-ld:HUES:001",  
    "anonymizedId": {  
        "type": "Text",  
        "value": "D20220AC3478565F"  
    },  
    "type": "AnonymousCommuterId",  
    "orig": {  
        "type": "Text",  
        "value": "City hall"  
    },  
    "dest": {  
        "type": "Text",  
        "value": "Library"  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                43.23161118206764,  
                -2.844695196525928  
            ]  
        }  
    },  
    "date": {  
        "type": "DateTime",  
        "value": "2022-09-05T08:25:35.00Z"  
    },  
    "algorithm": {  
        "type": "Text",  
        "value": "SHA1"  
    },  
    "dateCreated": {  
        "type": "DateTime",  
        "value": "2022-09-05T09:25:35.00Z"  
    },  
    "dateModified": {  
        "type": "DateTime",  
        "value": "2022-09-12T09:25:35.00Z"  
    },  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Transportation/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### AnonymousCommuterId NGSI-LD normalizzato Esempio  
Ecco un esempio di AnonymousCommuterId in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si usano opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "ngsi-ld:HUES:001",  
    "anonymizedId": "D20220AC3478565F",  
    "type": "AnonymousCommuterId",  
    "date": "2022-09-05T08:25:35.00Z",  
    "orig": "City hall",  
    "dest": "Library",  
    "source": "People Monitoring",  
    "algorithm": "SHA1",  
    "dateCreated": "2022-09-05T09:25:35.00Z",  
    "dateModified": "2022-09-12T09:25:35.00Z",  
    "location": {  
        "type": "Point",  
        "coordinates": [  
            43.23161118206764,   
            -2.844695196525928  
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
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di grandezza.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
