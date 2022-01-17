Entità: RoadSegment  
===================  
[Licenza aperta](https://github.com/smart-data-models//dataModel.Transportation/blob/master/RoadSegment/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descrizione globale: **Questa entità contiene una descrizione geografica e contestuale armonizzata di un segmento stradale. Un insieme di segmenti stradali è usato per descrivere una strada. **  

## Elenco delle proprietà  

- `address`: L'indirizzo postale  - `allowedVehicleType`: Tipo(i) di veicolo autorizzato(i) a transitare su questo segmento stradale. Enum:'agriculturalVehicle, bicycle, bus, car, caravan, carWithCaravan, carWithTrailer, constructionOrMaintenanceVehicle, lorry, moped, motorcycle, motorcycleWithSideCar, motorscooter, tanker, trailer, van, anyVehicle'. Valori ammessi: I seguenti valori definiti da _VehicleTypeEnum_, [DATEX 2 versione 2.3](http://d2docs.ndwcloud.nu/):  - `alternateName`: Un nome alternativo per questa voce  - `annotations`: Annotazioni sull'elemento  - `areaServed`: L'area geografica in cui viene fornito un servizio o un articolo offerto  - `category`: Permette di trasmettere caratteristiche extra di un segmento stradale. Enum:'oneway, toll, link'.  `oneway`: Indica se il segmento stradale può essere usato solo in una direzione. Se non presente significa che il segmento stradale può essere usato in entrambe le direzioni (avanti e indietro). Vedi anche [http://wiki.openstreetmap.org/wiki/Key:oneway](http://wiki.openstreetmap.org/wiki/Key:oneway). `toll` : Indica se il segmento stradale è soggetto a pedaggio. `link` : Indica se questo segmento stradale è un segmento di collegamento ausiliario per uscire o entrare in una strada. Vedere [https://wiki.openstreetmap.org/wiki/Tag:highway%3Dmotorway_link](https://wiki.openstreetmap.org/wiki/Tag:highway%3Dmotorway_link). Qualsiasi altro valore significativo per un'applicazione.  - `color`: Il colore del prodotto  - `dataProvider`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `dateCreated`: Timestamp di creazione dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `dateModified`: Timestamp dell'ultima modifica dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `description`: Una descrizione di questo articolo  - `endKilometer`: Il numero del chilometro (misurato dal punto di partenza della strada) in cui finisce questo segmento stradale.  - `endPoint`: Riferimento Geojson all'elemento. Può essere Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `id`: Identificatore unico dell'entità  - `image`: Un'immagine dell'oggetto  - `laneUsage`: Questo attributo può essere usato per trasmettere parametri specifici che descrivono ogni corsia. Deve contenere una stringa per ogni corsia del segmento stradale. L'elemento 0 dell'array deve contenere le informazioni della corsia 1, e così via. Il formato della stringa riferita deve essere: <lane_direction>, <lane_minimumAllowedSpeed>, <lane_maximumAllowedSpeed>, <lane_maximumAllowedHeight>, <lane_maximumAllowedWeight>. <lane_direction> è una stringa di testo con i seguenti valori ammessi: `forward`. La corsia è attualmente usata nella direzione `forward`. `backward`. La corsia è attualmente usata nella direzione `backwards`. L'unico parametro obbligatorio è `lane_direction`. Se non è specificato, il resto dei parametri può essere assunto uguale a quelli specificati a livello di entità.  - `length`: Lunghezza totale di questo segmento stradale in chilometri  - `location`: Riferimento Geojson all'elemento. Può essere Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `maximumAllowedHeight`: Altezza massima consentita per i veicoli che transitano su questo segmento stradale  - `maximumAllowedSpeed`: Velocità massima consentita durante il transito su questo segmento di strada. Limiti più restrittivi potrebbero essere applicati a tipi di veicoli specifici (camion, caravan, ecc.)  - `maximumAllowedWeight`: Peso massimo consentito per i veicoli che transitano su questo segmento stradale  - `minimumAllowedSpeed`: Velocità minima consentita durante il transito su questo segmento stradale  - `name`: Il nome di questo articolo.  - `owner`: Una lista contenente una sequenza di caratteri codificata in JSON che si riferisce agli ID unici dei proprietari  - `refRoad`: Strada a cui appartiene questo segmento stradale.  - `seeAlso`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source`: Una sequenza di caratteri che dà la fonte originale dei dati dell'entità come URL. Si raccomanda di essere il nome di dominio completamente qualificato del fornitore di origine, o l'URL dell'oggetto di origine.  - `startKilometer`: Il numero del chilometro (misurato dal punto di partenza della strada) in cui inizia questo segmento stradale.  - `startPoint`: Riferimento Geojson all'elemento. Può essere Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `status`: Condizioni di guida specifiche sul segmento di strada. Usa statusDescription per ulteriori informazioni. Enum: 'open, closed, limited'.  `open`: il tratto di strada può essere usato nella piena capacità prevista, `closed`: il traffico non è possibile, per esempio a causa di lavori stradali, un ponte o una chiusa aperti, o qualsiasi altro evento che impedisca il traffico. `limited`: il traffico è possibile, ma non nella piena capacità.  - `statusDescription`: Informazioni aggiuntive all'attributo status.  - `totalLaneNumber`: Numero totale di corsie offerte da questo segmento stradale  - `type`: Tipo di entità NGSI. Deve essere RoadSegment  - `width`: Larghezza del segmento della strada.    
Proprietà richieste  
- `allowedVehicleType`  - `endPoint`  - `id`  - `name`  - `refRoad`  - `startPoint`  - `type`    
I segmenti stradali possono includere diverse corsie. Questo modello di dati permette di trasmettere segmenti stradali composti da corsie eterogenee (diverse per uso, velocità, altezza, ecc.). Le corsie sono identificate da numeri interi compresi tra 1 e n, essendo il numero 1 la corsia a destra quando si va avanti. La direzione in avanti è la direzione indicata dal vettore che va dal punto di partenza del segmento al punto di arrivo del segmento. Questa è la stessa convenzione utilizzata da OpenStreetMap. Questa entità è principalmente associata ai segmenti verticali Automotive e Smart City e alle relative applicazioni IoT. Questo modello di dati è stato sviluppato in collaborazione con gli operatori mobili e la GSMA.  
## Descrizione del modello di dati delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
RoadSegment:    
  description: 'This entity contains a harmonised geographic and contextual description of a road segment. A collection of road segments are used to describe a Road. '    
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
    allowedVehicleType:    
      description: 'Vehicle type(s) allowed to transit through this road segment. Enum:''agriculturalVehicle, bicycle, bus, car, caravan, carWithCaravan, carWithTrailer, constructionOrMaintenanceVehicle, lorry, moped, motorcycle, motorcycleWithSideCar, motorscooter, tanker, trailer, van, anyVehicle''. Allowed values: The following values defined by _VehicleTypeEnum_, [DATEX 2 version 2.3](http://d2docs.ndwcloud.nu/):'    
      items:    
        enum:    
          - agriculturalVehicle    
          - bicycle    
          - bus    
          - car    
          - caravan    
          - carWithCaravan    
          - carWithTrailer    
          - constructionOrMaintenanceVehicle    
          - lorry    
          - moped    
          - motorcycle    
          - motorcycleWithSideCar    
          - motorscooter    
          - tanker    
          - trailer    
          - van    
          - anyVehicle    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    annotations:    
      description: 'Annotations about the item'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    category:    
      description: 'Allows to convey extra characteristics of a road segment. Enum:''oneway, toll, link''.  `oneway`: Flags whether the road segment can only be used in one direction. If not present it means road segment can be used in both directions (forwards and backwards). See also [http://wiki.openstreetmap.org/wiki/Key:oneway](http://wiki.openstreetmap.org/wiki/Key:oneway). `toll` : Flags whether the road segment is under toll fees. `link` : Flags whether this road segment is an auxiliary link segment for exiting or entering a road. See [https://wiki.openstreetmap.org/wiki/Tag:highway%3Dmotorway_link](https://wiki.openstreetmap.org/wiki/Tag:highway%3Dmotorway_link). Any other value meaningful to an application.'    
      items:    
        enum:    
          - oneway    
          - toll    
          - link    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    color:    
      description: 'The color of the product'    
      type: string    
      x-ngsi:    
        model: https://schema.org/color    
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
    endKilometer:    
      description: 'The kilometer number (measured from the road''s start point) where this road segment ends. '    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    endPoint:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf: &roadsegment_-_properties_-_location_-_oneof    
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
    id:    
      anyOf: &roadsegment_-_properties_-_owner_-_items_-_anyof    
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
    image:    
      description: 'An image of the item'    
      format: uri    
      type: string    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Property    
    laneUsage:    
      description: 'This attribute can be used to convey specific parameters describing each lane. It must contain a string per road segment lane. The element 0 of the array must contain the information of lane 1, and so on. Format of the referred string must be: <lane_direction>, <lane_minimumAllowedSpeed>, <lane_maximumAllowedSpeed>, <lane_maximumAllowedHeight>, <lane_maximumAllowedWeight>. <lane_direction> is a text string with the following allowed values: `forward`. The lane is currently used in the `forwards` direction. `backward`. The lane is currently used in the `backwards` direction. The only mandatory parameter is `lane_direction`. If not specified, the rest of parameters can be assumed to be equal to those specified at entity level.'    
      items:    
        enum:    
          - forward    
          - backward    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    length:    
      description: 'Total length of this road segment in kilometers'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/length    
        type: Property    
        units: 'Kilometer (Km)'    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf: *roadsegment_-_properties_-_location_-_oneof    
      x-ngsi:    
        type: Geoproperty    
    maximumAllowedHeight:    
      description: 'Maximum allowed height for vehicles transiting this road segment'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/height    
        type: Property    
        units: 'Meter (m)'    
    maximumAllowedSpeed:    
      description: 'Maximum allowed speed while transiting this road segment. More restrictive limits might be applied to specific vehicle types (trucks, caravans, etc.)'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: 'Kilometer per hour (Km/h)'    
    maximumAllowedWeight:    
      description: 'Maximum allowed weight for vehicles transiting this road segment'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/weight    
        type: Property    
        units: 'Kilogram (Kg)'    
    minimumAllowedSpeed:    
      description: 'Minimum allowed speed while transiting this road segment'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: 'Kilometer per hour (Km/h)'    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *roadsegment_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    refRoad:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Road to which this road segment belongs to.'    
      x-ngsi:    
        type: Relationship    
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
    startKilometer:    
      description: 'The kilometer number (measured from the road''s start point) where this road segment starts. '    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    startPoint:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf: *roadsegment_-_properties_-_location_-_oneof    
      x-ngsi:    
        type: Geoproperty    
    status:    
      description: 'Specific driving conditions on the roadsegment. Use statusDescription for additional information. Enum: ‘open, closed, limited’.  `open`: the roadsegment can be used in full intended capacity, `closed`: no traffic is possible, e.g. due to roadworks, an open bridge or lock, or any other event preventing traffic. `limited`: traffic is possible, but not in the full capacity.'    
      items:    
        enum:    
          - open    
          - closed    
          - limited    
        type: string    
      type: string    
      x-ngsi:    
        type: Property    
    statusDescription:    
      description: 'Additional information to the status attribute.'    
      type: string    
      x-ngsi:    
        type: Property    
    totalLaneNumber:    
      description: 'Total number of lanes offered by this road segment'    
      minimum: 1    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number.    
        type: Property    
    type:    
      description: 'NGSI Entity type. It has to be RoadSegment'    
      enum:    
        - RoadSegment    
      type: string    
      x-ngsi:    
        type: Property    
    width:    
      description: 'Road''s segment width.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: 'Meter (m)'    
  required:    
    - id    
    - name    
    - type    
    - refRoad    
    - startPoint    
    - endPoint    
    - allowedVehicleType    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Transportation/blob/master/RoadSegment/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Transportation/RoadSegment/schema.json    
  x-model-tags: ""    
  x-version: 0.3.0    
```  
</details>    
Le proprietà `laneUsage` e quelle che trasmettono i parametri massimi consentiti possono essere dinamiche, per esempio, una direzione di corsia può essere cambiata temporaneamente per migliorare le condizioni del traffico.  
## Esempio di payloads  
#### Esempio di valori chiave di RoadSegment NGSI-v2  
Ecco un esempio di un RoadSegment in formato JSON-LD come key-values. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
```json  
{  
	"id": "Spain-RoadSegment-A62-osm-24702186",  
	"type": "RoadSegment",  
	"name": "Valladolid-Dueñas",  
	"category": [  
		"oneway"  
	],  
	"refRoad": "Spain-Road-A62",  
	"totalLaneNumber": 2,  
	"maximumAllowedSpeed": 120,  
	"minimumAllowedSpeed": 60,  
	"startPoint": {  
		"type": "Point",  
		"coordinates": [  
			-4.7299180606009,  
			41.6844918725019  
		]  
	},  
	"endPoint": {  
		"type": "Point",  
		"coordinates": [  
			-4.55167335377909,  
			41.8570461783071  
		]  
	},  
	"allowedVehicleType": [  
		"car",  
		"bus",  
		"lorry",  
		"trailer",  
		"tanker",  
		"van",  
		"caravan"  
	],  
	"location": {  
		"type": "LineString",  
		"coordinates": [  
			[  
				-4.7299180606009,  
				41.6844918725019  
			],  
			[  
				-4.72855890957602,  
				41.6860596957855  
			],  
			[  
				-4.5520357341647,  
				41.8569278186523  
			],  
			[  
				-4.55167335377909,  
				41.8570461783071  
			]  
		]  
	},  
	"laneUsage": [  
		"forward",  
		"forward"  
	],  
	"source": "http://wwww.openstreetmap.org",  
	"status": "open",  
	"statusDescription": "Bridge state = DOWN"  
}  
```  
#### RoadSegment NGSI-v2 normalizzato Esempio  
Ecco un esempio di un RoadSegment in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
```json  
{  
	"id": "Spain-RoadSegment-A62-osm-24702186",  
	"type": "RoadSegment",  
	"category": {  
		"value": [  
			"oneway"  
		]  
	},  
	"endPoint": {  
		"value": {  
			"type": "Point",  
			"coordinates": [  
				-4.55167335377909,  
				41.8570461783071  
			]  
		}  
	},  
	"name": {  
		"value": "Valladolid-Dueñas"  
	},  
	"startPoint": {  
		"value": {  
			"type": "Point",  
			"coordinates": [  
				-4.7299180606009,  
				41.6844918725019  
			]  
		}  
	},  
	"allowedVehicleType": {  
		"value": [  
			"car",  
			"bus",  
			"lorry",  
			"trailer",  
			"tanker",  
			"van",  
			"caravan"  
		]  
	},  
	"source": {  
		"value": "http://wwww.openstreetmap.org"  
	},  
	"totalLaneNumber": {  
		"value": 2  
	},  
	"location": {  
		"type": "geo:json",  
		"value": {  
			"type": "LineString",  
			"coordinates": [  
				[  
					-4.7299180606009,  
					41.6844918725019  
				],  
				[  
					-4.72855890957602,  
					41.6860596957855  
				],  
				[  
					-4.5520357341647,  
					41.8569278186523  
				],  
				[  
					-4.55167335377909,  
					41.8570461783071  
				]  
			]  
		}  
	},  
	"minimumAllowedSpeed": {  
		"value": 60  
	},  
	"refRoad": {  
		"type": "Relationship",  
		"value": "Spain-Road-A62"  
	},  
	"maximumAllowedSpeed": {  
		"value": 120  
	},  
	"laneUsage": {  
		"value": [  
			"forward",  
			"forward"  
		]  
	},  
	"status": {  
		"value": "open"  
	},  
	"statusDescription": {  
		"value": "Bridge state = DOWN"  
	}  
}  
```  
#### Valori chiave NGSI-LD di RoadSegment Esempio  
Ecco un esempio di un RoadSegment in formato JSON-LD come key-values. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
```json  
{  
	"id": "urn:ngsi-ld:RoadSegment:Spain-RoadSegment-A62-osm-24702186",  
	"type": "RoadSegment",  
	"allowedVehicleType": [  
		"car",  
		"bus",  
		"lorry",  
		"trailer",  
		"tanker",  
		"van",  
		"caravan"  
	],  
	"category": [  
		"oneway"  
	],  
	"endPoint": {  
		"coordinates": [  
			-4.55167335377909,  
			41.8570461783071  
		],  
		"type": "Point"  
	},  
	"laneUsage": [  
		"forward",  
		"forward"  
	],  
	"location": {  
		"coordinates": [  
			[  
				-4.7299180606009,  
				41.6844918725019  
			],  
			[  
				-4.72855890957602,  
				41.6860596957855  
			],  
			[  
				-4.5520357341647,  
				41.8569278186523  
			],  
			[  
				-4.55167335377909,  
				41.8570461783071  
			]  
		],  
		"type": "LineString"  
	},  
	"maximumAllowedSpeed": 120,  
	"minimumAllowedSpeed": 60,  
	"name": "Valladolid-DueÃ±as",  
	"refRoad": "urn:ngsi-ld:Road:Spain-Road-A62",  
	"source": "http://wwww.openstreetmap.org",  
	"startPoint": {  
		"coordinates": [  
			-4.7299180606009,  
			41.6844918725019  
		],  
		"type": "Point"  
	},  
	"totalLaneNumber": 2,  
	"status": "open",  
	"statusDescription": "Bridge state = DOWN",  
	"@context": [  
		"https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
	]  
}  
```  
#### Esempio normalizzato di RoadSegment NGSI-LD  
Ecco un esempio di un RoadSegment in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
```json  
{  
	"id": "urn:ngsi-ld:RoadSegment:Spain-RoadSegment-A62-osm-24702186",  
	"type": "RoadSegment",  
	"allowedVehicleType": {  
		"type": "Property",  
		"value": [  
			"car",  
			"bus",  
			"lorry",  
			"trailer",  
			"tanker",  
			"van",  
			"caravan"  
		]  
	},  
	"category": {  
		"type": "Property",  
		"value": [  
			"oneway"  
		]  
	},  
	"endPoint": {  
		"type": "Property",  
		"value": {  
			"type": "Point",  
			"coordinates": [  
				-4.55167335377909,  
				41.8570461783071  
			]  
		}  
	},  
	"laneUsage": {  
		"type": "Property",  
		"value": [  
			"forward",  
			"forward"  
		]  
	},  
	"location": {  
		"type": "GeoProperty",  
		"value": {  
			"type": "LineString",  
			"coordinates": [  
				[  
					-4.7299180606009,  
					41.6844918725019  
				],  
				[  
					-4.72855890957602,  
					41.6860596957855  
				],  
				[  
					-4.5520357341647,  
					41.8569278186523  
				],  
				[  
					-4.55167335377909,  
					41.8570461783071  
				]  
			]  
		}  
	},  
	"maximumAllowedSpeed": {  
		"type": "Property",  
		"value": 120  
	},  
	"minimumAllowedSpeed": {  
		"type": "Property",  
		"value": 60  
	},  
	"name": {  
		"type": "Property",  
		"value": "Valladolid-DueÃ±as"  
	},  
	"refRoad": {  
		"type": "Relationship",  
		"object": "urn:ngsi-ld:Road:Spain-Road-A62"  
	},  
	"source": {  
		"type": "Property",  
		"value": "http://wwww.openstreetmap.org"  
	},  
	"startPoint": {  
		"type": "Property",  
		"value": {  
			"type": "Point",  
			"coordinates": [  
				-4.7299180606009,  
				41.6844918725019  
			]  
		}  
	},  
	"totalLaneNumber": {  
		"type": "Property",  
		"value": 2  
	},  
	"status": {  
		"type": "Property",  
		"value": "open"  
	},  
	"statusDescription": {  
		"type": "Property",  
		"value": "Bridge state = DOWN"  
	},  
	"@context": [  
		"https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
		"https://raw.githubusercontent.com/smart-data-models/dataModel.Transportation/master/context.jsonld"  
	]  
}  
```  
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per avere una risposta su come trattare le unità di grandezza  
