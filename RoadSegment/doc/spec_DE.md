[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: RoadSegment  
====================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.Transportation/blob/master/RoadSegment/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Globale Beschreibung: **Diese Einheit enthält eine harmonisierte geografische und kontextbezogene Beschreibung eines Straßenabschnitts. Eine Sammlung von Straßensegmenten wird zur Beschreibung einer Straße verwendet.**  
Version: 0.4.1  

## Liste der Eigenschaften  

- `address`: Die Postanschrift  - `agency_name`: Das Feld agency_name enthält den vollständigen Namen der Behörde oder Organisation, die für die Instandhaltung der betreffenden Stelle zuständig ist. SameAs: Feld "agency_name" aus GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)  - `allowedVehicleType`: Fahrzeugtyp(en), der/die für die Durchfahrt durch diesen Straßenabschnitt zugelassen ist/sind. Enum:'agriculturalVehicle, bicycle, bus, car, caravan, carWithCaravan, carWithTrailer, constructionOrMaintenanceVehicle, lorry, moped, motorcycle, motorcycleWithSideCar, motorscooter, tanker, trailer, van, anyVehicle'. Erlaubte Werte: Die folgenden Werte, definiert durch _VehicleTypeEnum_, [DATEX 2 Version 2.3](http://d2docs.ndwcloud.nu/):  - `alternateName`: Ein alternativer Name für diesen Artikel  - `annotations`: Anmerkungen zum Artikel  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `bridgeCount`: Anzahl der Brücken in dem Straßenabschnitt, der dieser Beobachtung entspricht. Nimmt den Wert 0 (Null) an, wenn der Straßenabschnitt keine Brücken hat.  - `carriagewayLength`: Gesamtlänge der Fahrbahn des Straßenabschnitts, der dieser Beobachtung entspricht.  - `carriagewayWidth`: Gesamtbreite der Fahrbahn des Straßenabschnitts, der dieser Beobachtung entspricht.  - `category`: Ermöglicht die Übermittlung zusätzlicher Merkmale eines Straßenabschnitts. Enum:'Einbahnstraße, Mautstraße, Verbindungsstraße'.  Einbahnstraße": Gibt an, ob der Straßenabschnitt nur in eine Richtung befahren werden kann. Wenn nicht vorhanden, bedeutet dies, dass das Straßensegment in beide Richtungen (vorwärts und rückwärts) genutzt werden kann. Siehe auch [http://wiki.openstreetmap.org/wiki/Key:oneway](http://wiki.openstreetmap.org/wiki/Key:oneway). `toll` : Gibt an, ob für den Straßenabschnitt Mautgebühren erhoben werden. Link": Gibt an, ob es sich bei diesem Straßenabschnitt um einen Hilfsabschnitt für die Ausfahrt oder Einfahrt auf eine Straße handelt. Siehe [https://wiki.openstreetmap.org/wiki/Tag:highway%3Dmotorway_link](https://wiki.openstreetmap.org/wiki/Tag:highway%3Dmotorway_link). Jeder andere Wert, der für eine Anwendung von Bedeutung ist.  - `color`: Die Farbe des Produkts  - `culvertCount`: Anzahl der Durchlässe, die im Verlauf der Straße, die dieser Beobachtung entspricht, vorhanden sind.  - `cyclePathLeftHeight`: Höhe des Radwegs am linken Fahrbahnrand entsprechend dieser Beobachtung.  - `cyclePathLeftWidth`: Breite des Radwegs am linken Fahrbahnrand entsprechend dieser Beobachtung.  - `cyclePathMaterial`: Baumaterial, das für die Verlegung des Radwegs an den Seiten der Straße verwendet wurde, entsprechend dieser Beobachtung.  - `cyclePathPlacement`: Beschreibt die Lage des Radwegs entlang des Straßenabschnitts, der dieser Beobachtung entspricht. Enum:' ['RECHTS, LINKS, BEIDES, NICHT_VERFÜGBAR'  - `cyclePathRightHeight`: Höhe des Radwegs am rechten Fahrbahnrand entsprechend dieser Beobachtung.  - `cyclePathRightWidth`: Breite des Radwegs am rechten Fahrbahnrand entsprechend dieser Beobachtung.  - `dataDescriptor`: URI, die auf die Daten-Deskriptor-Entität verweist  - `dataProvider`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird in der Regel von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `endKilometer`: Die Kilometernummer (gemessen vom Anfangspunkt der Straße), an der dieser Straßenabschnitt endet.  - `endPoint`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `id`: Eindeutiger Bezeichner der Entität  - `image`: Ein Bild des Artikels  - `laneInfo`: Beschreibt die Aspekte der Fahrspuren der Straße, die dieser Beobachtung entsprechen.  - `laneUsage`: Dieses Attribut kann zur Übermittlung spezifischer Parameter verwendet werden, die jeden Fahrstreifen beschreiben. Es muss eine Zeichenkette pro Fahrspur des Straßenabschnitts enthalten. Das Element 0 des Arrays muss die Informationen für Fahrspur 1 enthalten usw. Das Format der angegebenen Zeichenfolge muss sein: <Spur_Richtung>, <Spur_minimale_erlaubteGeschwindigkeit>, <Spur_maximale_erlaubteGeschwindigkeit>, <Spur_maximale_erlaubteHöhe>, <Spur_maximales_erlaubtesGewicht>. <lane_direction> ist eine Zeichenkette mit den folgenden zulässigen Werten: `forward`. Die Fahrspur wird derzeit in der Richtung "vorwärts" verwendet. Rückwärts". Die Fahrspur wird gegenwärtig in der Richtung "rückwärts" benutzt. Der einzige obligatorische Parameter ist `lane_direction`. Wird er nicht angegeben, kann davon ausgegangen werden, dass die übrigen Parameter denen entsprechen, die auf Entitätsebene angegeben wurden.  - `length`: Gesamtlänge dieses Straßenabschnitts in Kilometern  - `location`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `maximumAllowedHeight`: Maximal zulässige Höhe für Fahrzeuge, die diesen Straßenabschnitt passieren  - `maximumAllowedSpeed`: Zulässige Höchstgeschwindigkeit auf dem betreffenden Straßenabschnitt. Für bestimmte Fahrzeugtypen (Lkw, Wohnwagen usw.) können strengere Grenzwerte gelten.  - `maximumAllowedWeight`: Zulässiges Höchstgewicht für Fahrzeuge, die diesen Straßenabschnitt passieren  - `maximumAllowedWidth`: Maximal zulässige Breite für Fahrzeuge, die die dieser Beobachtung entsprechende Einheit benutzen.  - `medianHeight`: Höhe des Mittelstreifens oder Mittelstreifens auf der Straße, die dieser Beobachtung entspricht.  - `medianLength`: Länge des Mittelstreifens oder Mittelstreifens auf der Straße, die dieser Beobachtung entspricht.  - `medianWidth`: Breite des Mittelstreifens oder Mittelstreifens auf der Straße, die dieser Beobachtung entspricht.  - `minimumAllowedSpeed`: Zulässige Mindestgeschwindigkeit beim Befahren dieses Straßenabschnitts  - `municipalityInfo`: Informationen der Gemeinde zu dieser Beobachtung.  - `name`: Der Name dieses Artikels.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `pedestrianPathLeftHeight`: Höhe des Gehwegs am linken Fahrbahnrand, der dieser Beobachtung entspricht.  - `pedestrianPathLeftWidth`: Breite des Gehweges am linken Fahrbahnrand entsprechend dieser Beobachtung.  - `pedestrianPathMaterial`: Das Baumaterial, das für die Verlegung des Gehwegs an den Seiten der Straße verwendet wurde, entspricht dieser Beobachtung.  - `pedestrianPathPlacement`: Beschreibt das Vorhandensein und die Position von Fußgängern entlang des Straßenabschnitts, der dieser Beobachtung entspricht. Enum:'RIGHT, LEFT, BOTH, NOT_AVAILABLE'  - `pedestrianPathRightHeight`: Höhe des Gehwegs am rechten Fahrbahnrand, der dieser Beobachtung entspricht.  - `pedestrianPathRightWidth`: Breite des Gehweges am rechten Fahrbahnrand entsprechend dieser Beobachtung.  - `refRoad`: Straße, zu der dieser Straßenabschnitt gehört.  - `rightOfWayWidth`: Das Wegerecht (RoW) ist die gesamte für die Straße verfügbare Fläche. Seine Breite bietet Platz für den Fahrweg + andere Notwendigkeiten + zukünftige Erweiterungen entlang der Straßenführung.  - `roadClass`: Die Art der Straße, die dieser Beobachtung entspricht. Enum: [OTHER_PUBLIC_ROAD, PRIVATE_ROAD, MINOR_CITY_ROAD, MAJOR_DISTRICT_ROAD, MAJOR_CITY_ROAD, NATIONAL_HIGHWAY, SERVICE_ROAD, STATE_HIGHWAY, OTHER_DISTRICT_ROAD, PORT_ROAD].  - `roadDirection`: Stellt die Richtung dar, in die die Straße führt. Enum:' ['N, S, E, W'. Die Werte N,S,E,W stehen jeweils für Nord,Süd,Ost,West.  - `roadId`: Einzigartige interne Darstellung der Straße, die dieser Beobachtung entspricht.  - `roadMaterial`: Das für den Einbau der Fahrbahn verwendete Baumaterial, das dieser Bemerkung entspricht. Z. B. Beton, Lehm, Teer usw.  - `roadName`: Der Name der Straße, die dieser Beobachtung entspricht.  - `roadWork`: Gründe für die Straßenarbeiten im Falle eines dringenden Eingriffs. Eine Kombination aus diesen Werten. Enum:'COLLAPSE, DERAILMENT, FIRE, FLOOD, GASLEAK, LANDSLIDE, OTHER, POWERCUT, ROCKFALL, SAGGING, WATERLEAK'.  - `seeAlso`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `startKilometer`: Die Kilometernummer (gemessen vom Anfangspunkt der Straße), an der dieser Straßenabschnitt beginnt.  - `startPoint`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `status`: Spezifische Fahrbedingungen auf dem Straßenabschnitt. Verwenden Sie statusDescription für zusätzliche Informationen. Enum: "offen, geschlossen, eingeschränkt".  open": Das Straßensegment kann in vollem Umfang genutzt werden, "closed": Es ist kein Verkehr möglich, z. B. aufgrund von Baustellen, einer offenen Brücke oder Schleuse oder eines anderen Ereignisses, das den Verkehr verhindert. eingeschränkt": Verkehr ist möglich, aber nicht in der vollen Kapazität.  - `statusDescription`: Zusätzliche Informationen zum Attribut "Status".  - `totalCyclePathWidth`: Gesamtbreite des Radwegs auf der Straße, die dieser Beobachtung entspricht.  - `totalLaneNumber`: Gesamtzahl der Fahrspuren in diesem Straßenabschnitt  - `totalPedestrianPathLength`: Gesamtlänge des Gehweges auf der Straße, die dieser Beobachtung entspricht.  - `totalPedestrianPathWidth`: Gesamtbreite des Gehweges auf der Straße, die dieser Beobachtung entspricht.  - `type`: NGSI-Entitätstyp. Es muss RoadSegment sein  - `width`: Die Breite des Straßenabschnitts.    
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
    agency_name:    
      description: "The agency_name field contains the full name of the agency or organisation responsible for maintenance of the entity under consideration. SameAs: 'agency_name' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)"    
      type: string    
      x-ngsi:    
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
    bridgeCount:    
      description: 'Number of bridges in the road segment corresponding to this observation. Takes 0 (zero) as the value when the road segment has no bridges.'    
      type: number    
      x-ngsi:    
        type: Property    
    carriagewayLength:    
      description: 'Total length of the carriage way of the road segment corresponding to this observation.'    
      type: number    
      x-ngsi:    
        type: Property    
    carriagewayWidth:    
      description: 'Total width of the carriage way of the road segment corresponding to this observation.'    
      type: number    
      x-ngsi:    
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
    culvertCount:    
      description: 'Number of culverts prevalent in the trace of the road corresponding to this observation.'    
      type: number    
      x-ngsi:    
        type: Property    
    cyclePathLeftHeight:    
      description: 'Height of the cycle track on the left edge of the road corresponding to this observation.'    
      type: number    
      x-ngsi:    
        type: Property    
    cyclePathLeftWidth:    
      description: 'Width of the cycle track on the left edge of the road corresponding to this observation.'    
      type: number    
      x-ngsi:    
        type: Property    
    cyclePathMaterial:    
      description: 'Construction material used for laying the cycle path on the sides of the road corresponding to this observation.'    
      type: string    
      x-ngsi:    
        type: Property    
    cyclePathPlacement:    
      description: 'Describes the placement of cycle track along the road segment corresponding to this observation. Enum:'' [''RIGHT, LEFT, BOTH, NOT_AVAILABLE'''    
      enum:    
        - BOTH    
        - LEFT    
        - NOT_AVAILABLE    
        - RIGHT    
      type: string    
      x-ngsi:    
        type: Property    
    cyclePathRightHeight:    
      description: 'Height of the cycle track on the right edge of the road corresponding to this observation.'    
      type: number    
      x-ngsi:    
        type: Property    
    cyclePathRightWidth:    
      description: 'Width of the cycle track on the right edge of the road corresponding to this observation.'    
      type: number    
      x-ngsi:    
        type: Property    
    dataDescriptor:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'URI pointing to the data-descriptor entity'    
      x-ngsi:    
        type: Relationship    
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
    laneInfo:    
      description: 'Describes the aspects of lanes of the road corresponding to this observation.'    
      properties:    
        laneDirection:    
          description: 'Property. Describes the direction in which vehicles are plying on the lane corresponding to this observation. Enum:''FORWARD, BACKWARD, INBOUND, OUTBOUND, RIGHT, LEFT'''    
          enum:    
            - BACKWARD    
            - FORWARD    
            - INBOUND    
            - LEFT    
            - OUTBOUND    
            - RIGHT    
          laneLength:    
            description: 'Property. Length of the lane corresponding to this observation.'    
            type: number    
          laneWidth:    
            description: 'Property. Width of the lane corresponding to this observation.'    
            type: number    
          type: string    
        laneId:    
          description: 'Property. Unique identification number of the lane corresponding to this observation.'    
          type: number    
      type: object    
      x-ngsi:    
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
      description: 'Maximum allowed speed plying the road segment. More restrictive limits might be applied to specific vehicle types (trucks, caravans, etc.)'    
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
    maximumAllowedWidth:    
      description: 'Maximum allowed width for vehicles using the entity corresponding to this observation.'    
      type: number    
      x-ngsi:    
        type: Property    
    medianHeight:    
      description: 'Height of the median or central reservation in the road corresponding to this observation.'    
      type: number    
      x-ngsi:    
        type: Property    
    medianLength:    
      description: 'Length of the median or central reservation in the road corresponding to this observation.'    
      type: number    
      x-ngsi:    
        type: Property    
    medianWidth:    
      description: 'Width of the median or central reservation in the road corresponding to this observation.'    
      type: number    
      x-ngsi:    
        type: Property    
    minimumAllowedSpeed:    
      description: 'Minimum allowed speed while transiting this road segment'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: 'Kilometer per hour (Km/h)'    
    municipalityInfo:    
      description: 'Municipality information corresponding to this observation.'    
      properties:    
        cityId:    
          description: 'Property. Model:''https://schema.org/Text''. City ID corresponding to this observation.'    
          type: string    
        cityName:    
          description: 'Property. Model:''https://schema.org/Text''. City name corresponding to this observation'    
          type: string    
        district:    
          description: 'Property. Model:''https://schema.org/Text''. District name corresponding to this observation.'    
          type: string    
        stateName:    
          description: 'Property. Model:''https://schema.org/Text''. Name of the state corresponding to this observation.'    
          type: string    
        ulbName:    
          description: 'Property. Model:''https://schema.org/Text''. Name of the Urban Local Body corresponding to this observation.'    
          type: string    
        wardId:    
          description: 'Property. Model:''https://schema.org/Text''. Ward ID corresponding to this observation.'    
          type: string    
        wardName:    
          description: 'Property. Model:''https://schema.org/Text''. Ward name corresponding to this observation.'    
          type: string    
        wardNum:    
          description: 'Property. Model:''https://schema.org/Number''. Ward number corresponding to this observation.'    
          type: number    
        zoneId:    
          description: 'Property. Model:''https://schema.org/Text''. Zone ID corresponding to this observation.'    
          type: string    
        zoneName:    
          description: 'Property. Model:''https://schema.org/Text''. Zone name corresponding to this observation.'    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
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
    pedestrianPathLeftHeight:    
      description: 'Height of the walkway placed on the left edge of the road corresponding to this observation.'    
      type: number    
      x-ngsi:    
        type: Property    
    pedestrianPathLeftWidth:    
      description: 'Width of the walkway placed on the left edge of the road corresponding to this observation.'    
      type: number    
      x-ngsi:    
        type: Property    
    pedestrianPathMaterial:    
      description: 'Construction material used for laying the walkway / footpath on the sides of the road corresponding to this observation.'    
      type: string    
      x-ngsi:    
        type: Property    
    pedestrianPathPlacement:    
      description: 'Describes the presence and placement of pedestrian along the road segment corresponding to this observation. Enum:''RIGHT, LEFT, BOTH, NOT_AVAILABLE'''    
      type: string    
      x-ngsi:    
        type: Property    
    pedestrianPathRightHeight:    
      description: 'Height of the walkway placed on the right edge of the road corresponding to this observation.'    
      type: number    
      x-ngsi:    
        type: Property    
    pedestrianPathRightWidth:    
      description: 'Width of the walkway placed on the right edge of the road corresponding to this observation.'    
      type: number    
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
    rightOfWayWidth:    
      description: 'Right of Way (RoW) is the total land area available for the roadway. Its width accommodates for carriages way + other necessities + future extension, along the road''s alignment.'    
      type: number    
      x-ngsi:    
        type: Property    
    roadClass:    
      description: 'The type of road corresponding to this observation. Enum: [OTHER_PUBLIC_ROAD, PRIVATE_ROAD, MINOR_CITY_ROAD, MAJOR_DISTRICT_ROAD, MAJOR_CITY_ROAD, NATIONAL_HIGHWAY, SERVICE_ROAD, STATE_HIGHWAY, OTHER_DISTRICT_ROAD, PORT_ROAD].'    
      enum:    
        - MAJOR_DISTRICT_ROAD    
        - MAJOR_CITY_ROAD    
        - MINOR_CITY_ROAD    
        - NATIONAL_HIGHWAY    
        - OTHER_DISTRICT_ROAD    
        - OTHER_PUBLIC_ROAD    
        - PORT_ROAD    
        - PRIVATE_ROAD    
        - SERVICE_ROAD    
        - STATE_HIGHWAY    
      type: string    
      x-ngsi:    
        type: Property    
    roadDirection:    
      description: 'Represents the direction the road is heading to. Enum:'' [''N, S, E, W''. The values N,S,E,W represent North,South,East,West respectively.'    
      type: string    
      x-ngsi:    
        type: Property    
    roadId:    
      description: 'Unique internal representation of the road corresponding to this observation.'    
      type: string    
      x-ngsi:    
        type: Property    
    roadMaterial:    
      description: 'The construction material used for laying the carriageway corresponding to this observation. For eg. concrete, earthen, tar etc.'    
      type: string    
      x-ngsi:    
        type: Property    
    roadName:    
      description: 'The name of the road corresponding to this observation.'    
      type: string    
      x-ngsi:    
        type: Property    
    roadWork:    
      description: 'Reasons for the road work in case of urgent intervention. A combination of these values. Enum:''COLLAPSE, DERAILMENT, FIRE, FLOOD, GASLEAK, LANDSLIDE, OTHER, POWERCUT, ROCKFALL, SAGGING, WATERLEAK''.'    
      enum:    
        - COLLAPSE    
        - DERAILMENT    
        - FIRE    
        - FLOOD    
        - GASLEAK    
        - LANDSLIDE    
        - OTHER    
        - POWERCUT    
        - ROCKFALL    
        - SAGGING    
        - WATERLEAK    
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
    totalCyclePathWidth:    
      description: 'Total width of the cycle track present in the road corresponding to this observation.'    
      type: number    
      x-ngsi:    
        type: Property    
    totalLaneNumber:    
      description: 'Total number of lanes offered by this road segment'    
      minimum: 1    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number.    
        type: Property    
    totalPedestrianPathLength:    
      description: 'Total length of the walkway present in the road corresponding to this observation.'    
      type: number    
      x-ngsi:    
        type: Property    
    totalPedestrianPathWidth:    
      description: 'Total width of the walkway present in the road corresponding to this observation.'    
      type: number    
      x-ngsi:    
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
  x-model-tags: IUDX    
  x-version: 0.4.1    
```  
</details>    
Die Eigenschaften `laneUsage` und diejenigen, die die maximal zulässigen Parameter angeben, können dynamisch sein, z.B. kann eine Fahrbahnrichtung vorübergehend geändert werden, um die Verkehrsbedingungen zu verbessern.  
## Beispiel-Nutzlasten  
#### RoadSegment NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für ein RoadSegment im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
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
  "statusDescription": "Bridge state = DOWN",  
  "cyclePathMaterial": "ASPHALT",  
  "carriagewayLength": 0.095454461114818,  
  "totalPedestrianPathWidth": 7,  
  "bridgeCount": 1,  
  "pedestrianPathLeftHeight": 2,  
  "maximumAllowedHeight": 72,  
  "totalPedestrianPathLength": 0.09,  
  "culvertCount": 0,  
  "roadName": "GREEN VILLA ROAD TO CHAITHRAM HOUSE",  
  "roadClass": "OTHER_PUBLIC_ROAD",  
  "medianHeight": 3.6,  
  "roadWork": "OTHER",  
  "roadID": "5272",  
  "cyclePathRightWidth": 2.5,  
  "roadMaterial": "TAR",  
  "medianWidth": 1.5,  
  "carriagewayWidth": 3,  
  "cyclePathRightHeight": 1,  
  "roadDirection": "N",  
  "medianLength": 0.09,  
  "pedestrianPathMaterial": "PAVEMENT BLOCK",  
  "cyclePathLeftWidth": 2.5,  
  "maximumAllowedWidth": 74,  
  "rightOfWayWidth": 4,  
  "cyclePathLeftHeight": 1,  
  "maximumAllowedWeight": 109,  
  "pedestrianPathRightWidth": 3.5,  
  "pedestrianPathLeftWidth": 3.5,  
  "pedestrianPathPlacement": "NOT_AVAILABLE",  
  "pedestrianPathRightHeight": 2,  
  "cyclePathPlacement": "NOT_AVAILABLE",  
  "totalCyclePathWidth": 5,  
  "agency_name": "CORPORATION",  
  "municipalityInfo": {  
    "ulbName": "KANNUR MUNICIPAL CORPORATION"  
  }  
}  
```  
#### RoadSegment NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für ein RoadSegment im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
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
  },  
  "cyclePathMaterial": "ASPHALT",  
  "carriagewayLength": {  
    "type": "number",  
    "value": 0.095454461114818  
  },  
  "totalPedestrianPathWidth": {  
    "type": "number",  
    "value": 7  
  },  
  "bridgeCount": {  
    "type": "number",  
    "value": 1  
  },  
  "pedestrianPathLeftHeight": {  
    "type": "number",  
    "value": 2  
  },  
  "maximumAllowedHeight": {  
    "type": "number",  
    "value": 72  
  },  
  "totalPedestrianPathLength": {  
    "type": "number",  
    "value": 0.09  
  },  
  "culvertCount": {  
    "type": "number",  
    "value": 0  
  },  
  "roadName": {  
    "type": "string",  
    "value": "GREEN VILLA ROAD TO CHAITHRAM HOUSE"  
  },  
  "roadClass": {  
    "type": "string",  
    "value": "OTHER_PUBLIC_ROAD"  
  },  
  "medianHeight": {  
    "type": "number",  
    "value": 3.6  
  },  
  "roadWork": {  
    "type": "string",  
    "value": "OTHER"  
  },  
  "roadID": {  
    "type": "string",  
    "value": "5272"  
  },  
  "cyclePathRightWidth": {  
    "type": "number",  
    "value": 2.5  
  },  
  "roadMaterial": {  
    "type": "string",  
    "value": "TAR"  
  },  
  "medianWidth": {  
    "type": "number",  
    "value": 1.5  
  },  
  "carriagewayWidth": {  
    "type": "number",  
    "value": 3  
  },  
  "cyclePathRightHeight": {  
    "type": "number",  
    "value": 1  
  },  
  "roadDirection": {  
    "type": "string",  
    "value": "N"  
  },  
  "medianLength": {  
    "type": "number",  
    "value": 0.09  
  },  
  "pedestrianPathMaterial": {  
    "type": "string",  
    "value": "PAVEMENT BLOCK"  
  },  
  "cyclePathLeftWidth": {  
    "type": "number",  
    "value": 2.5  
  },  
  "maximumAllowedWidth": {  
    "type": "number",  
    "value": 74  
  },  
  "rightOfWayWidth": {  
    "type": "number",  
    "value": 4  
  },  
  "cyclePathLeftHeight": {  
    "type": "number",  
    "value": 1  
  },  
  "maximumAllowedWeight": {  
    "type": "number",  
    "value": 109  
  },  
  "pedestrianPathRightWidth": {  
    "type": "number",  
    "value": 3.5  
  },  
  "pedestrianPathLeftWidth": {  
    "type": "number",  
    "value": 3.5  
  },  
  "pedestrianPathPlacement": {  
    "type": "string",  
    "value": "NOT_AVAILABLE"  
  },  
  "pedestrianPathRightHeight": {  
    "type": "number",  
    "value": 2  
  },  
  "cyclePathPlacement": {  
    "type": "string",  
    "value": "NOT_AVAILABLE"  
  },  
  "totalCyclePathWidth": {  
    "type": "number",  
    "value": 5  
  },  
  "agency_name": {  
    "type": "string",  
    "value": "CORPORATION"  
  },  
  "municipalityInfo": {  
    "type": "StructuredValue",  
    "value": {  
      "ulbName": "KANNUR MUNICIPAL CORPORATION"  
    }  
  }  
}  
```  
#### RoadSegment NGSI-LD Schlüsselwerte Beispiel  
Hier ist ein Beispiel für ein RoadSegment im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
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
  "cyclePathMaterial": "ASPHALT",  
  "carriagewayLength": 0.095454461114818,  
  "totalPedestrianPathWidth": 7,  
  "bridgeCount": 1,  
  "pedestrianPathLeftHeight": 2,  
  "maximumAllowedHeight": 72,  
  "totalPedestrianPathLength": 0.09,  
  "culvertCount": 0,  
  "roadName": "GREEN VILLA ROAD TO CHAITHRAM HOUSE",  
  "roadClass": "OTHER_PUBLIC_ROAD",  
  "medianHeight": 3.6,  
  "roadWork": "OTHER",  
  "roadID": "5272",  
  "cyclePathRightWidth": 2.5,  
  "roadMaterial": "TAR",  
  "medianWidth": 1.5,  
  "carriagewayWidth": 3,  
  "cyclePathRightHeight": 1,  
  "roadDirection": "N",  
  "medianLength": 0.09,  
  "pedestrianPathMaterial": "PAVEMENT BLOCK",  
  "cyclePathLeftWidth": 2.5,  
  "maximumAllowedWidth": 74,  
  "rightOfWayWidth": 4,  
  "cyclePathLeftHeight": 1,  
  "maximumAllowedWeight": 109,  
  "pedestrianPathRightWidth": 3.5,  
  "pedestrianPathLeftWidth": 3.5,  
  "pedestrianPathPlacement": "NOT_AVAILABLE",  
  "pedestrianPathRightHeight": 2,  
  "cyclePathPlacement": "NOT_AVAILABLE",  
  "totalCyclePathWidth": 5,  
  "agency_name": "CORPORATION",  
  "municipalityInfo": {  
    "ulbName": "KANNUR MUNICIPAL CORPORATION"  
  },  
  "@context": [  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### RoadSegment NGSI-LD normalisiert Beispiel  
Hier ein Beispiel für ein RoadSegment im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
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
	"carriagewayLength": {  
    "type": "Property",  
    "value": 0.095454461114818  
  },  
  "totalPedestrianPathWidth": {  
    "type": "Property",  
    "value": 7  
  },  
  "bridgeCount": {  
    "type": "Property",  
    "value": 1  
  },  
  "pedestrianPathLeftHeight": {  
    "type": "Property",  
    "value": 2  
  },  
  "maximumAllowedHeight": {  
    "type": "Property",  
    "value": 72  
  },  
  "totalPedestrianPathLength": {  
    "type": "Property",  
    "value": 0.09  
  },  
  "culvertCount": {  
    "type": "Property",  
    "value": 0  
  },  
  "roadName": {  
    "type": "Property",  
    "value": "GREEN VILLA ROAD TO CHAITHRAM HOUSE"  
  },  
  "roadClass": {  
    "type": "Property",  
    "value": "OTHER_PUBLIC_ROAD"  
  },  
  "medianHeight": {  
    "type": "Property",  
    "value": 3.6  
  },  
  "roadWork": {  
    "type": "Property",  
    "value": "OTHER"  
  },  
  "roadID": {  
    "type": "Property",  
    "value": "5272"  
  },  
  "cyclePathRightWidth": {  
    "type": "Property",  
    "value": 2.5  
  },  
  "roadMaterial": {  
    "type": "Property",  
    "value": "TAR"  
  },  
  "medianWidth": {  
    "type": "Property",  
    "value": 1.5  
  },  
  "carriagewayWidth": {  
    "type": "Property",  
    "value": 3  
  },  
  "cyclePathRightHeight": {  
    "type": "Property",  
    "value": 1  
  },  
  "roadDirection": {  
    "type": "Property",  
    "value": "N"  
  },  
  "medianLength": {  
    "type": "Property",  
    "value": 0.09  
  },  
  "pedestrianPathMaterial": {  
    "type": "Property",  
    "value": "PAVEMENT BLOCK"  
  },  
  "cyclePathLeftWidth": {  
    "type": "Property",  
    "value": 2.5  
  },  
  "maximumAllowedWidth": {  
    "type": "Property",  
    "value": 74  
  },  
  "rightOfWayWidth": {  
    "type": "Property",  
    "value": 4  
  },  
  "cyclePathLeftHeight": {  
    "type": "Property",  
    "value": 1  
  },  
  "maximumAllowedWeight": {  
    "type": "Property",  
    "value": 109  
  },  
  "pedestrianPathRightWidth": {  
    "type": "Property",  
    "value": 3.5  
  },  
  "pedestrianPathLeftWidth": {  
    "type": "Property",  
    "value": 3.5  
  },  
  "pedestrianPathPlacement": {  
    "type": "Property",  
    "value": "NOT_AVAILABLE"  
  },  
  "pedestrianPathRightHeight": {  
    "type": "Property",  
    "value": 2  
  },  
  "cyclePathPlacement": {  
    "type": "Property",  
    "value": "NOT_AVAILABLE"  
  },  
  "totalCyclePathWidth": {  
    "type": "Property",  
    "value": 5  
  },  
  "agency_name": {  
    "type": "Property",  
    "value": "CORPORATION"  
  },  
 "municipalityInfo": {  
    "type": "Property",  
    "value": {  
      "ulbName": "KANNUR MUNICIPAL CORPORATION"  
    }  
  },  
	"@context": [  
		"https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
		"https://raw.githubusercontent.com/smart-data-models/dataModel.Transportation/master/context.jsonld"  
	]  
}  
```  
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht  
