<!-- 10-Header -->
  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

Entità: ElectricVehicleMobility  
===============================
<!-- /10-Header -->
  
<!-- 15-License -->
  

[Licenza aperta](https://github.com/smart-data-models//dataModel.Transportation/blob/master/ElectricVehicleMobility/LICENSE.md)  

[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->
  
<!-- 20-Description -->
  

Global description: **Osservazione quotidiana dei modelli di mobilità dei veicoli elettrici aggregati per posizione, marca del veicolo e regione geografica.**  

version: 0.0.1  
<!-- /20-Description -->
  
<!-- 30-PropertiesList -->
  


## Elenco delle proprietà  


<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o formati/pattern diversi</sub></sup>  
- `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)
	- `addressCountry[string]`: Il paese. Ad esempio, la Spagna  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: La località in cui si trova l'indirizzo stradale e che si trova nella regione  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: La regione in cui si trova la località, e che si trova nel paese  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Un distretto è un tipo di divisione amministrativa che, in alcuni paesi, è gestita dal governo locale
	- `postOfficeBoxNumber[string]`: Il numero di casella postale per gli indirizzi di casella postale. Ad esempio, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Il codice postale. Ad esempio, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: L'indirizzo stradale  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: Numero civico
- `alternateName[string]`: Un nome alternativo per questo articolo
- `areaServed[string]`: L'area geografica in cui viene fornito un servizio o un articolo offerto  . Model: [https://schema.org/Text](https://schema.org/Text)
- `averageDistanceKm[number]`: Distanza media percorsa in chilometri  . Model: [https://schema.org/Number](https://schema.org/Number)
- `dataProvider[string]`: Fornitore dell'entità di dati armonizzati  . Model: [https://schema.org/Text](https://schema.org/Text)
- `dateCreated[date-time]`: Timestamp di creazione dell'entità. Questo di solito viene allocato dalla piattaforma di archiviazione
- `dateModified[date-time]`: Timestamp dell'ultima modifica dell'entità. Questo di solito verrà allocato dalla piattaforma di archiviazione
- `dateObserved[date]`: Data dell'osservazione (YYYY-MM-DD)  . Model: [https://schema.org/Date](https://schema.org/Date)
- `description[string]`: Una descrizione di questo articolo
- `deviceBrand[string]`: Marca o produttore del veicolo elettrico  . Model: [https://schema.org/Text](https://schema.org/Text)
- `district[string]`: Distretto in cui è stata effettuata l'osservazione  . Model: [https://schema.org/Text](https://schema.org/Text)
- `id[*]`: Identificatore univoco dell'entità
- `location[*]`: Riferimento Geojson dell'elemento. Può essere Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon
- `locationCode[string]`: Codice ufficiale del comune  . Model: [https://schema.org/Text](https://schema.org/Text)
- `municipality[string]`: Comune dove è stata effettuata l'osservazione  . Model: [https://schema.org/Text](https://schema.org/Text)
- `n[number]`: Numero di osservazioni utilizzate per calcolare la distanza media  . Model: [https://schema.org/Number](https://schema.org/Number)
- `name[string]`: Il nome di questo articolo
- `owner[array]`: Un elenco contenente una sequenza di caratteri codificati JSON che fanno riferimento agli ID univoci del proprietario/i
- `region[string]`: Regione in cui è stata effettuata l'osservazione  . Model: [https://schema.org/Text](https://schema.org/Text)
- `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento
- `source[string]`: Fonte originale dei dati come URL  . Model: [https://schema.org/Text](https://schema.org/Text)
- `type[string]`: Tipo di entità NGSI. Deve essere ElectricVehicleMobility
- `vehicleType[string]`: Tipo di veicolo elettrico  . Model: [https://schema.org/Text](https://schema.org/Text)
<!-- /30-PropertiesList -->
  
<!-- 35-RequiredProperties -->
  

Proprietà richieste  
- `id`  
- `type`  
<!-- /35-RequiredProperties -->
  
<!-- 40-NotesYaml -->
  
<!-- /40-NotesYaml -->
  
<!-- 50-DataModelHeader -->
  

## Descrizione del modello di dati delle proprietà  

Ordinati alfabeticamente (clicca per i dettagli)  
<!-- /50-DataModelHeader -->
  
<!-- 60-ModelYaml -->
  
<details><summary><strong>dettagli yaml completi</strong></summary>    

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
  

## Esempi di payload  

#### Esempio di valori chiave ElectricVehicleMobility NGSI-v2  

Ecco un esempio di ElectricVehicleMobility in formato JSON-LD come valori chiave. Questo è compatibile con NGSI-v2 quando si utilizza `options=keyValues` e restituisce i dati di contesto di un'entità individuale.  
<details><summary><strong>mostra/nascondi esempio</strong></summary>    

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

#### Esempio normalizzato ElectricVehicleMobility NGSI-v2  

Ecco un esempio di ElectricVehicleMobility in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano opzioni e restituisce i dati di contesto di un'entità individuale.  
<details><summary><strong>mostra/nascondi esempio</strong></summary>    

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

#### Esempio di valori chiave NGSI-LD per la mobilità dei veicoli elettrici  

Ecco un esempio di ElectricVehicleMobility in formato JSON-LD come valori-chiave. Ciò è compatibile con NGSI-LD quando si utilizza `options=keyValues` e restituisce i dati di contesto di un'entità individuale.  
<details><summary><strong>mostra/nascondi esempio</strong></summary>    

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

#### Esempio normalizzato ElectricVehicleMobility NGSI-LD  

Ecco un esempio di ElectricVehicleMobility in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di un'entità individuale.  
<details><summary><strong>mostra/nascondi esempio</strong></summary>    

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
  

Vedi [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di misura della grandezza  
<!-- /95-Units -->
  
<!-- 97-LastFooter -->
  
---  

[Modelli di dati intelligenti](https://smartdatamodels.org) +++ [Manuale dei contributi](https://bit.ly/contribution_manual)  
  
