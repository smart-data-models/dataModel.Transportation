Entität: RoadSegment  
====================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.Transportation/blob/master/RoadSegment/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Globale Beschreibung: **Diese Einheit enthält eine harmonisierte geografische und kontextbezogene Beschreibung eines Straßenabschnitts. Eine Sammlung von Straßensegmenten wird zur Beschreibung einer Straße verwendet.**  

## Liste der Eigenschaften  

- `address`: Die Postanschrift  - `allowedVehicleType`: Fahrzeugtyp(en), der/die für die Durchfahrt durch diesen Straßenabschnitt zugelassen ist/sind. Enum:'agriculturalVehicle, bicycle, bus, car, caravan, carWithCaravan, carWithTrailer, constructionOrMaintenanceVehicle, lorry, moped, motorcycle, motorcycleWithSideCar, motorscooter, tanker, trailer, van, anyVehicle'. Erlaubte Werte: Die folgenden Werte, definiert durch _VehicleTypeEnum_, [DATEX 2 Version 2.3](http://d2docs.ndwcloud.nu/):  - `alternateName`: Ein alternativer Name für diesen Artikel  - `annotations`: Anmerkungen zum Artikel  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `category`: Ermöglicht die Übermittlung zusätzlicher Merkmale eines Straßenabschnitts. Enum:'Einbahnstraße, Mautstraße, Verbindungsstraße'.  Einbahnstraße": Gibt an, ob der Straßenabschnitt nur in eine Richtung befahren werden kann. Wenn nicht vorhanden, bedeutet dies, dass das Straßensegment in beide Richtungen (vorwärts und rückwärts) benutzt werden kann. Siehe auch [http://wiki.openstreetmap.org/wiki/Key:oneway](http://wiki.openstreetmap.org/wiki/Key:oneway). `toll` : Gibt an, ob für den Straßenabschnitt Mautgebühren erhoben werden. Link": Gibt an, ob es sich bei diesem Straßenabschnitt um einen Hilfsabschnitt für die Ausfahrt oder Einfahrt auf eine Straße handelt. Siehe [https://wiki.openstreetmap.org/wiki/Tag:highway%3Dmotorway_link](https://wiki.openstreetmap.org/wiki/Tag:highway%3Dmotorway_link). Jeder andere Wert, der für eine Anwendung von Bedeutung ist.  - `color`: Die Farbe des Produkts  - `dataProvider`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird in der Regel von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `endKilometer`: Die Kilometernummer (gemessen vom Anfangspunkt der Straße), an der dieser Straßenabschnitt endet.  - `endPoint`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `id`: Eindeutiger Bezeichner der Entität  - `image`: Ein Bild des Artikels  - `laneUsage`: Dieses Attribut kann zur Übermittlung spezifischer Parameter verwendet werden, die jeden Fahrstreifen beschreiben. Es muss eine Zeichenkette pro Fahrspur des Straßenabschnitts enthalten. Das Element 0 des Arrays muss die Informationen für Fahrspur 1 enthalten usw. Das Format der angegebenen Zeichenfolge muss sein: <Spur_Richtung>, <Spur_minimale_erlaubteGeschwindigkeit>, <Spur_maximale_erlaubteGeschwindigkeit>, <Spur_maximale_erlaubteHöhe>, <Spur_maximales_erlaubtesGewicht>. <lane_direction> ist eine Textzeichenfolge mit den folgenden zulässigen Werten: `forward`. Die Fahrspur wird derzeit in der Richtung "vorwärts" verwendet. Rückwärts". Die Fahrspur wird gegenwärtig in der Richtung "rückwärts" benutzt. Der einzige obligatorische Parameter ist `lane_direction`. Wird er nicht angegeben, kann davon ausgegangen werden, dass die übrigen Parameter den auf Entitätsebene angegebenen entsprechen.  - `length`: Gesamtlänge dieses Straßenabschnitts in Kilometern  - `location`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `maximumAllowedHeight`: Maximal zulässige Höhe für Fahrzeuge, die diesen Straßenabschnitt passieren  - `maximumAllowedSpeed`: Zulässige Höchstgeschwindigkeit beim Befahren dieses Straßenabschnitts. Für bestimmte Fahrzeugtypen (Lkw, Wohnwagen usw.) können strengere Grenzwerte gelten.  - `maximumAllowedWeight`: Zulässiges Höchstgewicht für Fahrzeuge, die diesen Straßenabschnitt passieren  - `minimumAllowedSpeed`: Zulässige Mindestgeschwindigkeit beim Befahren dieses Straßenabschnitts  - `name`: Der Name dieses Artikels.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `refRoad`: Straße, zu der dieser Straßenabschnitt gehört.  - `seeAlso`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `startKilometer`: Die Kilometernummer (gemessen vom Anfangspunkt der Straße), an der dieser Straßenabschnitt beginnt.  - `startPoint`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `totalLaneNumber`: Gesamtzahl der Fahrspuren in diesem Straßenabschnitt  - `type`: NGSI-Entitätstyp. Es muss RoadSegment sein  - `width`: Die Breite des Straßenabschnitts.    
Erforderliche Eigenschaften  
- `allowedVehicleType`  - `endPoint`  - `id`  - `name`  - `refRoad`  - `startPoint`  - `type`    
Straßenabschnitte können mehrere Fahrspuren umfassen. Dieses Datenmodell ermöglicht es, Straßenabschnitte zu übermitteln, die aus heterogenen Fahrspuren bestehen (unterschiedlich in ihrer Nutzung, Geschwindigkeit, Höhe usw.). Die Fahrspuren werden durch ganzzahlige Zahlen zwischen 1 und n identifiziert, wobei die Nummer 1 die Fahrspur auf der rechten Seite ist, wenn man vorwärts fährt. Die Vorwärtsrichtung ist die Richtung, die durch den Vektor angegeben wird, der vom Startpunkt des Segments zum Endpunkt des Segments führt. Dies ist die gleiche Konvention wie die von OpenStreetMap verwendete. Diese Entität ist in erster Linie mit den vertikalen Segmenten Automotive und Smart City und den damit verbundenen IoT-Anwendungen verbunden. Dieses Datenmodell wurde in Zusammenarbeit mit Mobilfunkbetreibern und der GSMA entwickelt.  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
RoadSegment:    
  description: 'This entity contains a harmonised geographic and contextual description of a road segment. A collection of road segments are used to describe a Road.'    
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
  x-version: 0.2.0    
```  
</details>    
Die Eigenschaften `laneUsage` und diejenigen, die die maximal zulässigen Parameter angeben, können dynamisch sein, z.B. kann eine Fahrbahnrichtung vorübergehend geändert werden, um die Verkehrsbedingungen zu verbessern.  
## Beispiel-Nutzlasten  
#### RoadSegment NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für ein RoadSegment im JSON-LD-Format als Key-Values. Dies ist mit NGSI-v2 kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "Spain-RoadSegment-A62-osm-24702186",  
  "type": "RoadSegment",  
  "name": "Valladolid-Dueñas",  
  "category": ["oneway"],  
  "refRoad": "Spain-Road-A62",  
  "totalLaneNumber": 2,  
  "maximumAllowedSpeed": 120,  
  "minimumAllowedSpeed": 60,  
  "startPoint": {  
    "type": "Point",  
    "coordinates": [-4.7299180606009, 41.6844918725019]  
  },  
  "endPoint": {  
    "type": "Point",  
    "coordinates": [-4.55167335377909, 41.8570461783071]  
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
      [-4.7299180606009, 41.6844918725019],  
      [-4.72855890957602, 41.6860596957855],  
      [-4.5520357341647, 41.8569278186523],  
      [-4.55167335377909, 41.8570461783071]  
    ]  
  },  
  "laneUsage": ["forward", "forward"],  
  "source": "http://wwww.openstreetmap.org"  
}  
```  
#### RoadSegment NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für ein RoadSegment im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "Spain-RoadSegment-A62-osm-24702186",  
  "type": "RoadSegment",  
  "category": {  
    "value": ["oneway"]  
  },  
  "endPoint": {  
    "value": {  
      "type": "Point",  
      "coordinates": [-4.55167335377909, 41.8570461783071]  
    }  
  },  
  "name": {  
    "value": "Valladolid-Due\u00f1as"  
  },  
  "startPoint": {  
    "value": {  
      "type": "Point",  
      "coordinates": [-4.7299180606009, 41.6844918725019]  
    }  
  },  
  "allowedVehicleType": {  
    "value": ["car", "bus", "lorry", "trailer", "tanker", "van", "caravan"]  
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
        [-4.7299180606009, 41.6844918725019],  
        [-4.72855890957602, 41.6860596957855],  
        [-4.5520357341647, 41.8569278186523],  
        [-4.55167335377909, 41.8570461783071]  
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
    "value": ["forward", "forward"]  
  }  
}  
```  
#### RoadSegment NGSI-LD Schlüsselwerte Beispiel  
Hier ist ein Beispiel für ein RoadSegment im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:RoadSegment:Spain-RoadSegment-A62-osm-24702186",  
  "type": "RoadSegment",  
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
  "name": {  
    "type": "Property",  
    "value": "Valladolid-Due\u00f1as"  
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
  "source": {  
    "type": "Property",  
    "value": "http://wwww.openstreetmap.org"  
  },  
  "totalLaneNumber": {  
    "type": "Property",  
    "value": 2  
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
  "minimumAllowedSpeed": {  
    "type": "Property",  
    "value": 60  
  },  
  "refRoad": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Road:Spain-Road-A62"  
  },  
  "maximumAllowedSpeed": {  
    "type": "Property",  
    "value": 120  
  },  
  "laneUsage": {  
    "type": "Property",  
    "value": [  
      "forward",  
      "forward"  
    ]  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### RoadSegment NGSI-LD normalisiert Beispiel  
Hier ein Beispiel für ein RoadSegment im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
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
  "id": "urn:ngsi-ld:RoadSegment:Spain-RoadSegment-A62-osm-24702186",  
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
  "name": "Valladolid-Due\u00f1as",  
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
  "type": "RoadSegment"  
}  
```  
Siehe [FAQ 10](https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht