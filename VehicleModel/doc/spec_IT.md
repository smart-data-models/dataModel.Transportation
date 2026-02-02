<!-- 10-Header -->
  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

Entità: VehicleModel  
====================
<!-- /10-Header -->
  
<!-- 15-License -->
  

[Licenza aperta](https://github.com/smart-data-models//dataModel.Transportation/blob/master/VehicleModel/LICENSE.md)  

[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->
  
<!-- 20-Description -->
  

Global description: **Questa entità modella un particolare modello di veicolo, inclusi tutte le proprietà che sono comuni a più istanze di veicolo appartenenti a tale modello.**  

version: 0.0.1  
<!-- /20-Description -->
  
<!-- 30-PropertiesList -->
  


## Elenco delle proprietà  


<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o formati/modello diversi</sub></sup>  
- `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)  
	- `addressCountry[string]`: Il paese. Ad esempio, la Spagna  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: La località in cui si trova l'indirizzo di via, e che si trova nella regione  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: La regione in cui si trova la località, e che si trova nel paese  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Un distretto è un tipo di divisione amministrativa che, in alcuni paesi, è gestito dal governo locale  
	- `postOfficeBoxNumber[string]`: Il numero di casella postale per gli indirizzi di casella postale. Ad esempio, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: Il codice postale. Ad esempio, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: L'indirizzo di via  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
	- `streetNr[string]`: Numero che identifica una proprietà specifica in una strada pubblica  
- `alternateName[string]`: Un nome alternativo per questo elemento  
- `annotations[array]`: Annotazioni sull'articolo  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `areaServed[string]`: L'area geografica in cui viene fornito un servizio o un articolo offerto  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `brandName[string]`: Nome del marchio del veicolo  . Model: [https://schema.org/brand](https://schema.org/brand)  
- `cargoVolume[number]`: Il volume disponibile per il carico o i bagagli. Per le automobili, si tratta solitamente del volume del bagagliaio. Se viene fornito solo un valore (tipo Numero) si riferirà al volume massimo  . Model: [https://schema.org/cargoVolume](https://schema.org/cargoVolume)  
- `color[string]`: Il colore del prodotto  . Model: [https://schema.org/color](https://schema.org/color)  
- `dataProvider[string]`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzati  
- `dateCreated[date-time]`: Timestamp di creazione dell'entità. Questo verrà solitamente assegnato dalla piattaforma di archiviazione  
- `dateModified[date-time]`: Timestamp dell'ultima modifica dell'entità. Questo verrà solitamente assegnato dalla piattaforma di archiviazione  
- `depth[number]`: Profondità del veicolo  . Model: [https://schema.org/depth](https://schema.org/depth)  
- `description[string]`: Una descrizione di questo articolo  
- `fuelConsumption[number]`: La quantità di carburante consumato per percorrere una determinata distanza o durata temporale con il veicolo dato (ad esempio litri per 100 km)  . Model: [https://schema.org/fuelConsumption](https://schema.org/fuelConsumption)  
- `fuelType[string]`: Il tipo di carburante adatto al motore o ai motori del veicolo. Enum: 'autogas, biodiesel, etanolo, cng, diesel, elettrico, benzina, ibrido elettrico/diesel, ibrido elettrico/benzina, idrogeno, gpl, benzina, benzina(senza piombo), benzina(con piombo), altro'  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)  
- `height[number]`: Altezza del veicolo  . Model: [https://schema.org/height](https://schema.org/height)  
- `id[*]`: Identificatore univoco dell'entità  
- `image[uri]`: Un'immagine dell'oggetto  . Model: [https://schema.org/URL](https://schema.org/URL)  
- `location[*]`: Riferimento Geojson all'elemento. Può essere Punto, LineString, Poligono, MultiPunto, MultiLineString o MultiPoligono  
- `manufacturerName[string]`: Nome del costruttore del veicolo  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `modelName[string]`: Nome del modello del veicolo  . Model: [https://schema.org/model](https://schema.org/model)  
- `name[string]`: Il nome di questo elemento  
- `owner[array]`: Una lista che contiene una sequenza di caratteri codificata in JSON che fa riferimento agli Id univoci del/dei proprietario/i  
- `seeAlso[*]`: Elenco di uri che puntano a risorse aggiuntive sull'elemento  
- `source[string]`: Una sequenza di caratteri che fornisce la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del fornitore di origine o l'URL dell'oggetto di origine  
- `type[string]`: Tipo di entità NGSI. Deve essere VehicleModel  
- `url[uri]`: URL che fornisce una descrizione di questo modello di veicolo  . Model: [https://schema.org/URL](https://schema.org/URL)  
- `vehicleEngine[string]`: Informazioni sul motore o sui motori del veicolo  . Model: [https://schema.org/vehicleEngine](https://schema.org/vehicleEngine)  
- `vehicleModelDate[date-time]`: La data di rilascio di un modello di veicolo (spesso utilizzato per differenziare le versioni dello stesso marchio e modello)  . Model: [https://schema.org/vehicleModelDate](https://schema.org/vehicleModelDate)  
- `vehicleType[string]`: Tipo di veicolo dal punto di vista delle sue caratteristiche strutturali. Ciò è diverso dalla categoria di veicolo. Enum: 'agriculturalVehicle, anyVehicle, articulatedVehicle, bicycle, binTrolley, bus, car, caravan, carOrLightVehicle, carWithCaravan, carWithTrailer, cleaningTrolley, constructionOrMaintenanceVehicle, fourWheelDrive, highSidedVehicle, lorry, minibus, moped, motorcycle, motorcycleWithSideCar, motorscooter, sweepingMachine, tanker, threeWheeledVehicle, trailer, tram, twoWheeledVehicle, trolley, van, vehicleWithoutCatalyticConverter, vehicleWithCaravan, vehicleWithTrailer, withEvenNumberedRegistrationPlates, withOddNumberedRegistrationPlates, other'. I seguenti valori definiti da _VehicleTypeEnum_ e _VehicleTypeEnum2_, [DATEX 2 versione 2.3](http://d2docs.ndwcloud.nu/_static/umlmodel/v2.3/index.htm)  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `weight[number]`: Peso del veicolo  . Model: [https://schema.org/weigth](https://schema.org/weigth)  
- `width[number]`: Larghezza del veicolo  . Model: [https://schema.org/width](https://schema.org/width)  
<!-- /30-PropertiesList -->
  
<!-- 35-RequiredProperties -->
  

Proprietà richieste  
- `nomeMarchio`  
- `id`  
- `nomeDelFabbricante`  
- `nomeModello`  
- `nome`  
- `tipo`  
- `tipoDiVeicolo`  
<!-- /35-RequiredProperties -->
  
<!-- 40-NotesYaml -->
  
<!-- /40-NotesYaml -->
  
<!-- 50-DataModelHeader -->
  

## Descrizione del modello di dati delle proprietà  

Ordinati in ordine alfabetico (clicca per i dettagli)  
<!-- /50-DataModelHeader -->
  
<!-- 60-ModelYaml -->
  
<details><summary><strong>full yaml details</strong></summary>    

```yaml  
VehicleModel:    
  description: 'This entity models a particular vehicle model, including all properties which are common to multiple vehicle instances belonging to such model.'    
  properties:    
    address:    
      description: The mailing address    
      properties:    
        addressCountry:    
          description: 'The country. For example, Spain'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressCountry    
            type: Property    
        addressLocality:    
          description: 'The locality in which the street address is, and which is in the region'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressLocality    
            type: Property    
        addressRegion:    
          description: 'The region in which the locality is, and which is in the country'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressRegion    
            type: Property    
        district:    
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government'    
          type: string    
          x-ngsi:    
            type: Property    
        postOfficeBoxNumber:    
          description: 'The post office box number for PO box addresses. For example, 03578'    
          type: string    
          x-ngsi:    
            model: https://schema.org/postOfficeBoxNumber    
            type: Property    
        postalCode:    
          description: 'The postal code. For example, 24004'    
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
    annotations:    
      description: Annotations about the item    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    brandName:    
      description: Vehicle's brand name    
      type: string    
      x-ngsi:    
        model: https://schema.org/brand    
        type: Property    
    cargoVolume:    
      description: 'The available volume for cargo or luggage. For automobiles, this is usually the trunk volume. If only a single value is provided (type Number) it will refer to the maximum volume'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/cargoVolume    
        type: Property    
        units: Liters    
    color:    
      description: The color of the product    
      type: string    
      x-ngsi:    
        model: https://schema.org/color    
        type: Property    
    dataProvider:    
      description: A sequence of characters identifying the provider of the harmonised data entity    
      type: string    
      x-ngsi:    
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
    depth:    
      description: Vehicle's depth    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/depth    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    fuelConsumption:    
      description: The amount of fuel consumed for traveling a particular distance or temporal duration with the given vehicle (e.g. liters per 100 km)    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/fuelConsumption    
        type: Property    
        units: liters per 100 kilometer    
    fuelType:    
      description: 'The type of fuel suitable for the engine or engines of the vehicle. Enum:''autogas, biodiesel, ethanol, cng, diesel, electric, gasoline, hybrid electric/diesel, hybrid electric/petrol, hydrogen, lpg, petrol, petrol(unleaded), petrol(leaded), other'''    
      enum:    
        - autogas    
        - biodiesel    
        - cng    
        - diesel    
        - electric    
        - ethanol    
        - gasoline    
        - hybrid_electric_diesel    
        - hybrid_electric_petrol    
        - hydrogen    
        - lpg    
        - petrol    
        - petrol(unleaded)    
        - petrol(leaded)    
        - other    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    height:    
      description: Vehicle's height    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/height    
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
        type: Property    
    image:    
      description: An image of the item    
      format: uri    
      type: string    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: Geojson reference to the item. Point    
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
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. LineString    
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
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. Polygon    
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
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiPoint    
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
      x-ngsi:    
        type: GeoProperty    
    manufacturerName:    
      description: Vehicle's manufacturer name    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    modelName:    
      description: Vehicle's model name    
      type: string    
      x-ngsi:    
        model: https://schema.org/model    
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
          type: Property    
      type: array    
      x-ngsi:    
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be VehicleModel    
      enum:    
        - VehicleModel    
      type: string    
      x-ngsi:    
        type: Property    
    url:    
      description: URL which provides a description of this vehicle model    
      format: uri    
      type: string    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Property    
    vehicleEngine:    
      description: Information about the engine or engines of the vehicle    
      type: string    
      x-ngsi:    
        model: https://schema.org/vehicleEngine    
        type: Property    
    vehicleModelDate:    
      description: The release date of a vehicle model (often used to differentiate versions of the same make and model)    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/vehicleModelDate    
        type: Property    
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
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    weight:    
      description: Vehicle's weigth    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/weigth    
        type: Property    
    width:    
      description: Vehicle's width    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/width    
        type: Property    
  required:    
    - id    
    - name    
    - type    
    - vehicleType    
    - brandName    
    - modelName    
    - manufacturerName    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Transportation/blob/master/VehicleModel/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Transportation/VehicleModel/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->
  
<!-- 70-MiddleNotes -->
  
<!-- /70-MiddleNotes -->
  
<!-- 80-Examples -->
  

## Payload di esempio  

#### ModelloVeicolo esempio di valori chiave NGSI-v2  

Ecco un esempio di VehicleModel in formato JSON come chiavi-valori. Ciò è compatibile con NGSI-v2 quando si utilizza `options=keyValues` e restituisce i dati di contesto di un'entità individuale.  
<details><summary><strong>show/hide example</strong></summary>    

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
</details>  

#### ModelloVeicolo NGSI-v2 normalizzato Esempio  

Ecco un esempio di VehicleModel in formato JSON come normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano opzioni e restituisce i dati di contesto di un'entità individuale.  
<details><summary><strong>show/hide example</strong></summary>    

```json  

{  
  "id": "vehiclemodel:econic",  
  "type": "VehicleModel",  
  "name": {  
    "type": "Text",  
    "value": "MBenz-Econic2014"  
  },  
  "cargoVolume": {  
    "type": "Number",  
    "value": 1000  
  },  
  "modelName": {  
    "type": "Text",  
    "value": "Econic"  
  },  
  "brandName": {  
    "type": "Text",  
    "value": "Mercedes Benz"  
  },  
  "manufacturerName": {  
    "type": "Text",  
    "value": "Daimler"  
  },  
  "fuelType": {  
    "type": "Text",  
    "value": "diesel"  
  },  
  "vehicleType": {  
    "type": "Text",  
    "value": "lorry"  
  }  
}  
```  
</details>  

#### ModelloVeicolo valori-chiave esempio NGSI-LD  

Ecco un esempio di VehicleModel in formato JSON-LD come chiavi-valori. Ciò è compatibile con NGSI-LD quando si utilizza `options=keyValues` e restituisce i dati di contesto di un'entità individuale.  
<details><summary><strong>show/hide example</strong></summary>    

```json  

{  
  "id": "urn:ngsi-ld:VehicleModel:vehiclemodel:econic",  
  "type": "VehicleModel",  
  "brandName": "Mercedes Benz",  
  "cargoVolume": 1000,  
  "fuelType": "diesel",  
  "manufacturerName": "Daimler",  
  "modelName": "Econic",  
  "name": "MBenz-Econic2014",  
  "vehicleType": "lorry",  
  "@context": [  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Transportation/master/context.jsonld"  
  ]  
}  
```  
</details>  

#### ModelloVeicolo Esempio normalizzato NGSI-LD  

Ecco un esempio di VehicleModel in formato JSON-LD normalizzato, compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di un'entità individuale.  
<details><summary><strong>show/hide example</strong></summary>    

```json  

{  
    "id": "urn:ngsi-ld:VehicleModel:vehiclemodel:econic",  
    "type": "VehicleModel",  
    "brandName": {  
        "type": "Property",  
        "value": "Mercedes Benz"  
    },  
    "cargoVolume": {  
        "type": "Property",  
        "value": 1000  
    },  
    "fuelType": {  
        "type": "Property",  
        "value": "diesel"  
    },  
    "manufacturerName": {  
        "type": "Property",  
        "value": "Daimler"  
    },  
    "modelName": {  
        "type": "Property",  
        "value": "Econic"  
    },  
    "name": {  
        "type": "Property",  
        "value": "MBenz-Econic2014"  
    },  
    "vehicleType": {  
        "type": "Property",  
        "value": "lorry"  
    },  
    "@context": [  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Transportation/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->
  
<!-- 90-FooterNotes -->
  
<!-- /90-FooterNotes -->
  
<!-- 95-Units -->
  

See [FAQ 10](https://smartdatamodels.org/index.php/faqs/) to get an answer on how to deal with magnitude units  
<!-- /95-Units -->
  
<!-- 97-LastFooter -->
  
---  

[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->
  
