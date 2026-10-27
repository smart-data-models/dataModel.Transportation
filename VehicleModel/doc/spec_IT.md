<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: VehicleModel  
====================<!-- /10-Header -->  
<!-- 15-License -->  
[Licenza Aperta](https://github.com/smart-data-models/dataModel.Transportation/blob/master/VehicleModel/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descrizione globale: **Questa entità modella un particolare modello di veicolo, incluse tutte le proprietà comuni a più istanze di veicoli appartenenti a tale modello.**  
version: 0.0.3  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Elenco delle proprietà  

<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/pattern</sub></sup>  
- `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Il paese. Ad esempio, Spagna  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: La località in cui si trova l'indirizzo civico e che si trova nella regione  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: La regione in cui si trova la località, e che si trova nel paese  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Un distretto è un tipo di divisione amministrativa che, in alcuni paesi, è gestita dal governo locale    
	- `postOfficeBoxNumber[string]`: Il numero di casella postale per gli indirizzi di casella postale. Ad esempio, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Il codice postale. Ad esempio, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: L'indirizzo civico  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: Numero che identifica una proprietà specifica su una strada pubblica    
- `alternateName[string]`: Un nome alternativo per questo elemento  - `annotations[array]`: Annotazioni sull'elemento  . Model: [https://schema.org/Text](https://schema.org/Text)- `areaServed[string]`: L'area geografica in cui viene fornito un servizio o un articolo offerto  . Model: [https://schema.org/Text](https://schema.org/Text)- `brandName[string]`: Nome del marchio del veicolo  . Model: [https://schema.org/brand](https://schema.org/brand)- `cargoVolume[number]`: Il volume disponibile per il carico o i bagagli. Per le automobili, si tratta solitamente del volume del bagagliaio. Se viene fornito un solo valore (tipo Number), si riferirà al volume massimo  . Model: [https://schema.org/cargoVolume](https://schema.org/cargoVolume)- `color[string]`: Il colore del prodotto  . Model: [https://schema.org/color](https://schema.org/color)- `dataProvider[string]`: Una sequenza di caratteri che identifica il fornitore dell'entità dati armonizzata  - `dateCreated[date-time]`: Timestamp di creazione dell'entità. Questo sarà solitamente assegnato dalla piattaforma di archiviazione  - `dateModified[date-time]`: Timestamp dell'ultima modifica dell'entità. Questo sarà solitamente allocato dalla piattaforma di archiviazione  - `depth[number]`: Profondità del veicolo  . Model: [https://schema.org/depth](https://schema.org/depth)- `description[string]`: Una descrizione di questo elemento  - `fuelConsumption[number]`: La quantità di carburante o energia consumata per percorrere una determinata distanza o durata temporale con il veicolo dato. Per i motori a combustione è espressa in litri per 100 km, per i veicoli elettrici (fuelType electric) in kilowattora per 100 km  . Model: [https://schema.org/fuelConsumption](https://schema.org/fuelConsumption)- `fuelType[string]`: Il tipo di carburante adatto al motore o ai motori del veicolo. Enum:'autogas, biodiesel, cng, diesel, electric, ethanol, gasoline, hybrid_electric_diesel, hybrid_electric_petrol, hydrogen, lpg, petrol, petrol(unleaded), petrol(leaded), other'  . Model: [https://schema.org/fuelType](https://schema.org/fuelType)- `height[number]`: Altezza del veicolo  . Model: [https://schema.org/height](https://schema.org/height)- `id[*]`: Identificatore unico dell'entità  - `image[uri]`: Un'immagine dell'elemento  . Model: [https://schema.org/URL](https://schema.org/URL)- `location[*]`: Riferimento Geojson all'elemento. Può essere Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `manufacturerName[string]`: Nome del produttore del veicolo  . Model: [https://schema.org/Text](https://schema.org/Text)- `modelName[string]`: Nome del modello del veicolo  . Model: [https://schema.org/model](https://schema.org/model)- `name[string]`: Il nome di questo elemento  - `owner[array]`: Un elenco contenente una sequenza di caratteri codificata in JSON che fa riferimento agli ID unici del/i proprietario/i  - `seeAlso[*]`: elenco di URI che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si raccomanda che sia il nome di dominio completo del fornitore della fonte, o l'URL dell'oggetto fonte  - `tractionBatteryCapacity[number]`: Capacità di energia utilizzabile della batteria di trazione dei veicoli alimentati totalmente o parzialmente a elettricità (veicoli elettrici a batteria, plug-in hybrid o ibridi). Consente, ad esempio, di stimare l'autonomia insieme al consumo di carburante  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: Tipo di entità NGSI. Deve essere VehicleModel  - `url[uri]`: URL che fornisce una descrizione di questo modello di veicolo  . Model: [https://schema.org/URL](https://schema.org/URL)- `vehicleEngine[string]`: Informazioni sul motore o sui motori del veicolo  . Model: [https://schema.org/vehicleEngine](https://schema.org/vehicleEngine)- `vehicleModelDate[date-time]`: La data di rilascio di un modello di veicolo (spesso utilizzata per differenziare le versioni della stessa marca e modello)  . Model: [https://schema.org/vehicleModelDate](https://schema.org/vehicleModelDate)- `vehicleType[string]`: Tipo di veicolo dal punto di vista delle sue caratteristiche strutturali. Questo è diverso dalla categoria del veicolo. Enum:'agriculturalVehicle, anyVehicle, articulatedVehicle, bicycle, binTrolley, bus, car, caravan, carOrLightVehicle, carWithCaravan, carWithTrailer, cleaningTrolley, constructionOrMaintenanceVehicle, fourWheelDrive, highSidedVehicle, lorry, minibus, moped, motorcycle, motorcycleWithSideCar, motorscooter, sweepingMachine, tanker, threeWheeledVehicle, trailer, tram, twoWheeledVehicle, trolley, van, vehicleWithoutCatalyticConverter, vehicleWithCaravan, vehicleWithTrailer, withEvenNumberedRegistrationPlates, withOddNumberedRegistrationPlates, other'. I seguenti valori sono definiti da _VehicleTypeEnum_ e _VehicleTypeEnum2_, [DATEX 2 versione 2.3](http://d2docs.ndwcloud.nu/_static/umlmodel/v2.3/index.htm)  . Model: [https://schema.org/Text](https://schema.org/Text)- `weight[number]`: Peso del veicolo  . Model: [https://schema.org/weight](https://schema.org/weight)- `width[number]`: Larghezza del veicolo  . Model: [https://schema.org/width](https://schema.org/width)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Proprietà richieste  
- `brandName`  - `id`  - `manufacturerName`  - `modelName`  - `name`  - `type`  - `vehicleType`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## Descrizione delle proprietà del modello di dati  
Ordinato alfabeticamente (clicca per dettagli)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
VehicleModel:    
  description: This entity models a particular vehicle model, including all properties which are common to multiple vehicle instances belonging to such model.    
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
    annotations:    
      description: Annotations about the item    
      items:    
        description: Eventy element in the annotations    
        type: string    
        x-ngsi:    
          type: Property    
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
      description: The available volume for cargo or luggage. For automobiles, this is usually the trunk volume. If only a single value is provided (type Number) it will refer to the maximum volume    
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
      description: The amount of fuel or energy consumed for traveling a particular distance or temporal duration with the given vehicle. For combustion engines it is expressed in liters per 100 km, for electric vehicles (fuelType electric) in kilowatt hours per 100 km    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/fuelConsumption    
        type: Property    
        units: liters per 100 kilometer or kilowatt hour per 100 kilometer    
    fuelType:    
      description: The type of fuel suitable for the engine or engines of the vehicle. Enum:'autogas, biodiesel, cng, diesel, electric, ethanol, gasoline, hybrid_electric_diesel, hybrid_electric_petrol, hydrogen, lpg, petrol, petrol(unleaded), petrol(leaded), other'    
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
        model: https://schema.org/fuelType    
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
        type: Relationship    
    image:    
      description: An image of the item    
      format: uri    
      type: string    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Property    
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
          type: Relationship    
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
      description: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object    
      type: string    
      x-ngsi:    
        type: Property    
    tractionBatteryCapacity:    
      description: Usable energy capacity of the traction battery of vehicles fully or partly powered by electricity (battery electric, plug-in hybrid or hybrid vehicles). Allows, for instance, estimating the driving range together with fuelConsumption    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: kilowatt hour    
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
      description: Type of vehicle from the point of view of its structural characteristics. This is different than the vehicle category . Enum:'agriculturalVehicle, anyVehicle, articulatedVehicle, bicycle, binTrolley, bus, car, caravan, carOrLightVehicle, carWithCaravan, carWithTrailer, cleaningTrolley, constructionOrMaintenanceVehicle, fourWheelDrive, highSidedVehicle, lorry, minibus, moped, motorcycle, motorcycleWithSideCar, motorscooter, sweepingMachine, tanker, threeWheeledVehicle, trailer, tram, twoWheeledVehicle, trolley, van, vehicleWithoutCatalyticConverter, vehicleWithCaravan, vehicleWithTrailer, withEvenNumberedRegistrationPlates, withOddNumberedRegistrationPlates, other'. The following values defined by _VehicleTypeEnum_ and _VehicleTypeEnum2_, [DATEX 2 version 2.3](http://d2docs.ndwcloud.nu/_static/umlmodel/v2.3/index.htm)    
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
      description: Vehicle's weight    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/weight    
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
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program    
  x-license-url: https://github.com/smart-data-models/dataModel.Transportation/blob/master/VehicleModel/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Transportation/VehicleModel/schema.json    
  x-model-tags: ''    
  x-version: 0.0.3    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Esempi di payload    
#### Esempio VehicleModel NGSI-v2 key-values  
Ecco un esempio di VehicleModel in formato JSON-LD come key-values. È compatibile con NGSI-v2 quando si utilizza `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "vehiclemodel:buzz",  
  "type": "VehicleModel",  
  "name": "VW-IDBuzz",  
  "brandName": "Volkswagen",  
  "modelName": "ID. Buzz",  
  "manufacturerName": "Volkswagen",  
  "vehicleType": "car",  
  "fuelType": "electric",  
  "fuelConsumption": 20.7,  
  "tractionBatteryCapacity": 79  
}  
```  
</details>  
#### Esempio VehicleModel NGSI-v2 normalizzato  
Ecco un esempio di VehicleModel in formato JSON-LD normalizzato. È compatibile con NGSI-v2 quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "vehiclemodel:buzz",  
  "type": "VehicleModel",  
  "name": {  
    "type": "Text",  
    "value": "VW-IDBuzz"  
  },  
  "brandName": {  
    "type": "Text",  
    "value": "Volkswagen"  
  },  
  "modelName": {  
    "type": "Text",  
    "value": "ID. Buzz"  
  },  
  "manufacturerName": {  
    "type": "Text",  
    "value": "Volkswagen"  
  },  
  "vehicleType": {  
    "type": "Text",  
    "value": "car"  
  },  
  "fuelType": {  
    "type": "Text",  
    "value": "electric"  
  },  
  "fuelConsumption": {  
    "type": "Number",  
    "value": 20.7  
  },  
  "tractionBatteryCapacity": {  
    "type": "Number",  
    "value": 79  
  }  
}  
```  
</details>  
#### Esempio VehicleModel NGSI-LD key-values  
Ecco un esempio di VehicleModel in formato JSON-LD come key-values. È compatibile con NGSI-LD quando si utilizza `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:VehicleModel:vehiclemodel:buzz",  
  "type": "VehicleModel",  
  "name": "VW-IDBuzz",  
  "brandName": "Volkswagen",  
  "modelName": "ID. Buzz",  
  "manufacturerName": "Volkswagen",  
  "vehicleType": "car",  
  "fuelType": "electric",  
  "fuelConsumption": 20.7,  
  "tractionBatteryCapacity": 79,  
  "@context": [  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Transportation/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### Esempio VehicleModel NGSI-LD normalizzato  
Ecco un esempio di VehicleModel in formato JSON-LD normalizzato. È compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:VehicleModel:vehiclemodel:buzz",  
    "type": "VehicleModel",  
    "name": {  
        "type": "Property",  
        "value": "VW-IDBuzz"  
    },  
    "brandName": {  
        "type": "Property",  
        "value": "Volkswagen"  
    },  
    "modelName": {  
        "type": "Property",  
        "value": "ID. Buzz"  
    },  
    "manufacturerName": {  
        "type": "Property",  
        "value": "Volkswagen"  
    },  
    "vehicleType": {  
        "type": "Property",  
        "value": "car"  
    },  
    "fuelType": {  
        "type": "Property",  
        "value": "electric"  
    },  
    "fuelConsumption": {  
        "type": "Property",  
        "value": 20.7  
    },  
    "tractionBatteryCapacity": {  
        "type": "Property",  
        "value": 79  
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
Vedi [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di misura  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
