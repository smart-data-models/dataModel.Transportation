<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: StradaSegmento  
======================<!-- /10-Header -->  
<!-- 15-License -->  
[Licenza aperta](https://github.com/smart-data-models//dataModel.Transportation/blob/master/RoadSegment/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descrizione globale: **Questa entità contiene una descrizione geografica e contestuale armonizzata di un segmento stradale. Per descrivere una strada si utilizza un insieme di segmenti stradali **.  
versione: 0.4.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Elenco delle proprietà  

<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.  
- `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Il paese. Ad esempio, la Spagna  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: La località in cui si trova l'indirizzo civico e che si trova nella regione  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: La regione in cui si trova la località, e che si trova nel paese  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Un distretto è un tipo di divisione amministrativa che, in alcuni paesi, è gestita dal governo locale.    
	- `postOfficeBoxNumber[string]`: Il numero di casella postale per gli indirizzi di casella postale. Ad esempio, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Il codice postale. Ad esempio, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: L'indirizzo stradale  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
- `agency_name[string]`: Il campo agency_name contiene il nome completo dell'agenzia o dell'organizzazione responsabile della manutenzione dell'entità in esame. Uguale a: Campo 'agency_name' da GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)  - `allowedVehicleType[array]`: Tipo di veicolo autorizzato a transitare su questo segmento stradale. Enum:'veicolo agricolo, bicicletta, autobus, auto, roulotte, auto con roulotte, auto con rimorchio, veicolo da costruzione o manutenzione, autocarro, ciclomotore, motociclo, motociclo con auto laterale, motoscooter, autocisterna, rimorchio, furgone, qualsiasi veicolo'. Valori ammessi: I seguenti valori definiti da _VehicleTypeEnum_, [DATEX 2 versione 2.3](http://d2docs.ndwcloud.nu/):  . Model: [https://schema.org/Text](https://schema.org/Text)- `alternateName[string]`: Un nome alternativo per questa voce  - `annotations[array]`: Annotazioni sull'elemento  . Model: [https://schema.org/Text](https://schema.org/Text)- `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `bridgeCount[number]`: Numero di ponti nel segmento stradale corrispondente a questa osservazione. Assume il valore 0 (zero) quando il segmento stradale non ha ponti.  - `carriagewayLength[number]`: Lunghezza totale della carreggiata del segmento di strada corrispondente a questa osservazione  - `carriagewayWidth[number]`: Larghezza totale della carreggiata del segmento stradale corrispondente a questa osservazione  - `category[array]`: Permette di comunicare le caratteristiche aggiuntive di un segmento stradale. Enum:'oneway, toll, link'.  `oneway`: Indica se il segmento stradale può essere utilizzato solo in una direzione. Se non è presente, significa che il segmento stradale può essere utilizzato in entrambe le direzioni (avanti e indietro). Si veda anche [http://wiki.openstreetmap.org/wiki/Key:oneway](http://wiki.openstreetmap.org/wiki/Key:oneway). `toll` : segnala se il segmento stradale è soggetto a pedaggio. `link` : Indica se questo segmento stradale è un segmento di collegamento ausiliario per uscire o entrare in una strada. Vedere [https://wiki.openstreetmap.org/wiki/Tag:highway%3Dmotorway_link](https://wiki.openstreetmap.org/wiki/Tag:highway%3Dmotorway_link). Qualsiasi altro valore significativo per un'applicazione  . Model: [https://schema.org/Text](https://schema.org/Text)- `color[string]`: Il colore del prodotto  . Model: [https://schema.org/color](https://schema.org/color)- `culvertCount[number]`: Numero di canalizzazioni prevalenti nel tracciato della strada corrispondente a questa osservazione  - `cyclePathLeftHeight[number]`: Altezza della pista ciclabile sul margine sinistro della strada corrispondente a questa osservazione  - `cyclePathLeftWidth[number]`: Larghezza della pista ciclabile sul margine sinistro della strada corrispondente a questa osservazione  - `cyclePathMaterial[string]`: Materiale da costruzione utilizzato per la posa della pista ciclabile ai lati della strada corrispondente a questa osservazione  - `cyclePathPlacement[string]`: Descrive il posizionamento della pista ciclabile lungo il segmento stradale corrispondente a questa osservazione. Enum:" ["DESTRA, SINISTRA, ENTRAMBI, NON_INTERESSANTE"].  - `cyclePathRightHeight[number]`: Altezza della pista ciclabile sul bordo destro della strada corrispondente a questa osservazione  - `cyclePathRightWidth[number]`: Larghezza della pista ciclabile sul margine destro della strada corrispondente a questa osservazione  - `dataDescriptor[*]`: URI che punta all'entità descrittore di dati  - `dataProvider[string]`: una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata  - `dateCreated[date-time]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `dateModified[date-time]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `description[string]`: Descrizione dell'articolo  - `endKilometer[number]`: Il numero di chilometri (misurato dal punto di partenza della strada) in cui termina il segmento stradale.  . Model: [https://schema.org/Number](https://schema.org/Number)- `endPoint[*]`: Riferimento geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `id[*]`: Identificatore univoco dell'entità  - `image[uri]`: Un'immagine dell'articolo  . Model: [https://schema.org/URL](https://schema.org/URL)- `laneInfo[object]`: Descrive gli aspetti delle corsie della strada che corrispondono a questa osservazione.  	- `laneDirection[string]`: Descrive la direzione in cui i veicoli circolano sulla corsia corrispondente a questa osservazione. Enum:'FORWARD, BACKWARD, INBOUND, OUTBOUND, RIGHT, LEFT'    
- `laneUsage[array]`: Questo attributo può essere utilizzato per trasmettere parametri specifici che descrivono ciascuna corsia. Deve contenere una stringa per ogni corsia del segmento stradale. L'elemento 0 dell'array deve contenere le informazioni della corsia 1 e così via. Il formato della stringa deve essere: <direzione_di_corsia>, <velocità_minima_consentita>, <velocità_massima_consentita>, <altezza_massima_consentita>, <peso_massimo_consentito>. <lane_direction> è una stringa di testo con i seguenti valori ammessi: `avanti`. La corsia è attualmente utilizzata nella direzione `forward`. `backward`. La corsia è attualmente utilizzata nella direzione `indietro`. L'unico parametro obbligatorio è `lane_direction`. Se non viene specificato, gli altri parametri possono essere assunti uguali a quelli specificati a livello di entità.  . Model: [https://schema.org/Text](https://schema.org/Text)- `length[number]`: Lunghezza totale di questo segmento stradale in chilometri  . Model: [https://schema.org/length](https://schema.org/length)- `location[*]`: Riferimento geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `maximumAllowedHeight[number]`: Altezza massima consentita per i veicoli in transito su questo segmento stradale  . Model: [https://schema.org/height](https://schema.org/height)- `maximumAllowedSpeed[number]`: Velocità massima consentita per il segmento stradale. Limiti più restrittivi possono essere applicati a tipi di veicoli specifici (camion, caravan, ecc.).  . Model: [https://schema.org/Number](https://schema.org/Number)- `maximumAllowedWeight[number]`: Peso massimo consentito per i veicoli che transitano su questo segmento stradale  . Model: [https://schema.org/weight](https://schema.org/weight)- `maximumAllowedWidth[number]`: Larghezza massima consentita per i veicoli che utilizzano l'entità corrispondente a questa osservazione  - `medianHeight[number]`: Altezza della mediana o dello spartitraffico centrale della strada corrispondente a questa osservazione  - `medianLength[number]`: Lunghezza della mediana o dello spartitraffico centrale della strada corrispondente a questa osservazione  - `medianWidth[number]`: Larghezza della mediana o dello spartitraffico centrale della strada corrispondente a questa osservazione  - `minimumAllowedSpeed[number]`: Velocità minima consentita durante il transito su questo segmento stradale  . Model: [https://schema.org/Number](https://schema.org/Number)- `municipalityInfo[object]`: Informazioni sul comune corrispondenti a questa osservazione  . Model: [https://schema.org/Text](https://schema.org/Text)	- `cityId[string]`: ID della città corrispondente a questa osservazione  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `cityName[string]`: Nome della città corrispondente a questa osservazione  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `district[string]`: Nome del distretto corrispondente a questa osservazione  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `stateName[string]`: Nome dello stato corrispondente a questa osservazione  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `ulbName[string]`: Nome dell'Ente Locale Urbano corrispondente a questa osservazione  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `wardId[string]`: ID del reparto corrispondente a questa osservazione  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `wardName[string]`: Nome del reparto corrispondente a questa osservazione  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `wardNum[number]`: Numero del reparto corrispondente a questa osservazione  . Model: [https://schema.org/Number](https://schema.org/Number)  
	- `zoneId[string]`: ID della zona corrispondente a questa osservazione  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `name[string]`: Il nome di questo elemento  - `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `pedestrianPathLeftHeight[number]`: Altezza della passerella posta sul bordo sinistro della strada corrispondente a questa osservazione  - `pedestrianPathLeftWidth[number]`: Larghezza della passerella posta sul bordo sinistro della strada corrispondente a questa osservazione  - `pedestrianPathMaterial[string]`: Materiale da costruzione utilizzato per la posa del camminamento/pedana ai lati della strada corrispondente a questa osservazione  - `pedestrianPathPlacement[string]`: Descrive la presenza e la posizione dei pedoni lungo il segmento stradale corrispondente a questa osservazione. Enum:'DESTRA, SINISTRA, ENTRAMBI, NON DISPONIBILE'.  - `pedestrianPathRightHeight[number]`: Altezza della passerella posta sul bordo destro della strada corrispondente a questa osservazione  - `pedestrianPathRightWidth[number]`: Larghezza della passerella posta sul bordo destro della strada corrispondente a questa osservazione  - `refRoad[*]`: Strada a cui appartiene questo segmento stradale  - `rightOfWayWidth[number]`: Il diritto di passaggio (RdC) è l'area totale disponibile per la carreggiata. La sua larghezza consente di ospitare il passaggio delle carrozze + altre necessità + un'estensione futura, lungo l'allineamento della strada.  - `roadClass[string]`: Il tipo di strada corrispondente a questa osservazione. Enum: [ALTRA STRADA_PUBBLICA, STRADA_PRIVATA, STRADA_MINOR_CITTA', STRADA_MAGGIORE_DISTRETTO, STRADA_MAGGIORE_CITTA', STRADA_NAZIONALE, STRADA_SERVIZI, STRADA_STATO, STRADA_ALTRO_DISTRETTO, STRADA PORTO].  - `roadDirection[string]`: Rappresenta la direzione verso cui è diretta la strada. Enum:" ["N, S, E, W". I valori N, S, E, W rappresentano rispettivamente Nord, Sud, Est e Ovest.  - `roadId[string]`: Rappresentazione interna unica della strada corrispondente a questa osservazione  - `roadMaterial[string]`: Il materiale di costruzione utilizzato per la posa della carreggiata corrispondente a questa osservazione. Ad esempio, cemento, terra, catrame, ecc.  - `roadName[string]`: Il nome della strada corrispondente a questa osservazione  - `roadWork[string]`: Motivi dell'intervento stradale in caso di intervento urgente. Una combinazione di questi valori. Enum:'COLLASSO, DISSESTO, INCENDIO, INONDAZIONE, GAS, TERRENI, ALTRO, TAGLIO DI ENERGIA, CADUTA DI ROCCE, SAGGIAMENTO, ALLAGAMENTO'.  - `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `startKilometer[number]`: Il numero di chilometro (misurato dal punto di partenza della strada) da cui inizia questo segmento stradale.  . Model: [https://schema.org/Number](https://schema.org/Number)- `startPoint[*]`: Riferimento geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `status[string]`: Condizioni di guida specifiche del segmento stradale. Utilizzare statusDescription per ulteriori informazioni. Enum: "aperto, chiuso, limitato".  `aperto`: il segmento stradale può essere utilizzato in tutta la sua capacità, `chiuso`: il traffico non è possibile, ad esempio a causa di lavori stradali, di un ponte o di una chiusa aperti o di qualsiasi altro evento che impedisca il traffico. `limitato`: il traffico è possibile, ma non nella sua piena capacità.  - `statusDescription[string]`: Informazioni aggiuntive all'attributo status  - `totalCyclePathWidth[number]`: Larghezza totale della pista ciclabile presente nella strada corrispondente a questa osservazione  - `totalLaneNumber[number]`: Numero totale di corsie offerte da questo segmento stradale  . Model: [https://schema.org/Number](https://schema.org/Number)- `totalPedestrianPathLength[number]`: Lunghezza totale della passerella presente nella strada corrispondente a questa osservazione  - `totalPedestrianPathWidth[number]`: Larghezza totale del passaggio pedonale presente nella strada corrispondente a questa osservazione  - `type[string]`: Tipo di entità NGSI. Deve essere RoadSegment  - `width[number]`: Larghezza del segmento stradale.  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Proprietà richieste  
- `allowedVehicleType`  - `endPoint`  - `id`  - `name`  - `refRoad`  - `startPoint`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
I segmenti stradali possono includere diverse corsie. Questo modello di dati consente di trasmettere segmenti stradali composti da corsie eterogenee (diverse per uso, velocità, altezza, ecc.). Le corsie sono identificate utilizzando numeri interi compresi tra 1 e n, essendo il numero 1 la corsia a destra quando si procede in avanti. La direzione di marcia è quella indicata dal vettore che va dal punto di inizio del segmento al punto di fine del segmento. È la stessa convenzione utilizzata da OpenStreetMap. Questa entità è associata principalmente ai segmenti verticali Automotive e Smart City e alle relative applicazioni IoT. Questo modello di dati è stato sviluppato in collaborazione con gli operatori di telefonia mobile e il GSMA.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Modello di dati descrizione delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
RoadSegment:    
  description: This entity contains a harmonised geographic and contextual description of a road segment. A collection of road segments are used to describe a Road.    
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
    bridgeCount:    
      description: Number of bridges in the road segment corresponding to this observation. Takes 0 (zero) as the value when the road segment has no bridges    
      type: number    
      x-ngsi:    
        type: Property    
    carriagewayLength:    
      description: Total length of the carriage way of the road segment corresponding to this observation    
      type: number    
      x-ngsi:    
        type: Property    
    carriagewayWidth:    
      description: Total width of the carriage way of the road segment corresponding to this observation    
      type: number    
      x-ngsi:    
        type: Property    
    category:    
      description: 'Allows to convey extra characteristics of a road segment. Enum:''oneway, toll, link''.  `oneway`: Flags whether the road segment can only be used in one direction. If not present it means road segment can be used in both directions (forwards and backwards). See also [http://wiki.openstreetmap.org/wiki/Key:oneway](http://wiki.openstreetmap.org/wiki/Key:oneway). `toll` : Flags whether the road segment is under toll fees. `link` : Flags whether this road segment is an auxiliary link segment for exiting or entering a road. See [https://wiki.openstreetmap.org/wiki/Tag:highway%3Dmotorway_link](https://wiki.openstreetmap.org/wiki/Tag:highway%3Dmotorway_link). Any other value meaningful to an application'    
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
      description: The color of the product    
      type: string    
      x-ngsi:    
        model: https://schema.org/color    
        type: Property    
    culvertCount:    
      description: Number of culverts prevalent in the trace of the road corresponding to this observation    
      type: number    
      x-ngsi:    
        type: Property    
    cyclePathLeftHeight:    
      description: Height of the cycle track on the left edge of the road corresponding to this observation    
      type: number    
      x-ngsi:    
        type: Property    
    cyclePathLeftWidth:    
      description: Width of the cycle track on the left edge of the road corresponding to this observation    
      type: number    
      x-ngsi:    
        type: Property    
    cyclePathMaterial:    
      description: Construction material used for laying the cycle path on the sides of the road corresponding to this observation    
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
      description: Height of the cycle track on the right edge of the road corresponding to this observation    
      type: number    
      x-ngsi:    
        type: Property    
    cyclePathRightWidth:    
      description: Width of the cycle track on the right edge of the road corresponding to this observation    
      type: number    
      x-ngsi:    
        type: Property    
    dataDescriptor:    
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
      description: URI pointing to the data-descriptor entity    
      x-ngsi:    
        type: Relationship    
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
    description:    
      description: A description of this item    
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
    laneInfo:    
      description: Describes the aspects of lanes of the road corresponding to this observation    
      properties:    
        laneDirection:    
          description: 'Describes the direction in which vehicles are plying on the lane corresponding to this observation. Enum:''FORWARD, BACKWARD, INBOUND, OUTBOUND, RIGHT, LEFT'''    
          enum:    
            - BACKWARD    
            - FORWARD    
            - INBOUND    
            - LEFT    
            - OUTBOUND    
            - RIGHT    
          laneLength:    
            description: Length of the lane corresponding to this observation    
            type: number    
            x-ngsi:    
              type: Property    
          laneWidth:    
            description: Width of the lane corresponding to this observation    
            type: number    
            x-ngsi:    
              type: Property    
          type: string    
          x-ngsi:    
            type: Property    
        laneId:    
          description: Unique identification number of the lane corresponding to this observation    
          type: number    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    laneUsage:    
      description: 'This attribute can be used to convey specific parameters describing each lane. It must contain a string per road segment lane. The element 0 of the array must contain the information of lane 1, and so on. Format of the referred string must be: <lane_direction>, <lane_minimumAllowedSpeed>, <lane_maximumAllowedSpeed>, <lane_maximumAllowedHeight>, <lane_maximumAllowedWeight>. <lane_direction> is a text string with the following allowed values: `forward`. The lane is currently used in the `forwards` direction. `backward`. The lane is currently used in the `backwards` direction. The only mandatory parameter is `lane_direction`. If not specified, the rest of parameters can be assumed to be equal to those specified at entity level'    
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
      description: Total length of this road segment in kilometers    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/length    
        type: Property    
        units: Kilometer (Km)    
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
    maximumAllowedHeight:    
      description: Maximum allowed height for vehicles transiting this road segment    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/height    
        type: Property    
        units: Meter (m)    
    maximumAllowedSpeed:    
      description: 'Maximum allowed speed plying the road segment. More restrictive limits might be applied to specific vehicle types (trucks, caravans, etc.)'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Kilometer per hour (Km/h)    
    maximumAllowedWeight:    
      description: Maximum allowed weight for vehicles transiting this road segment    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/weight    
        type: Property    
        units: Kilogram (Kg)    
    maximumAllowedWidth:    
      description: Maximum allowed width for vehicles using the entity corresponding to this observation    
      type: number    
      x-ngsi:    
        type: Property    
    medianHeight:    
      description: Height of the median or central reservation in the road corresponding to this observation    
      type: number    
      x-ngsi:    
        type: Property    
    medianLength:    
      description: Length of the median or central reservation in the road corresponding to this observation    
      type: number    
      x-ngsi:    
        type: Property    
    medianWidth:    
      description: Width of the median or central reservation in the road corresponding to this observation    
      type: number    
      x-ngsi:    
        type: Property    
    minimumAllowedSpeed:    
      description: Minimum allowed speed while transiting this road segment    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Kilometer per hour (Km/h)    
    municipalityInfo:    
      description: Municipality information corresponding to this observation    
      properties:    
        cityId:    
          description: City ID corresponding to this observation    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        cityName:    
          description: City name corresponding to this observation    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        district:    
          description: District name corresponding to this observation    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        stateName:    
          description: Name of the state corresponding to this observation    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        ulbName:    
          description: Name of the Urban Local Body corresponding to this observation    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        wardId:    
          description: Ward ID corresponding to this observation    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        wardName:    
          description: Ward name corresponding to this observation    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        wardNum:    
          description: Ward number corresponding to this observation    
          type: number    
          x-ngsi:    
            model: https://schema.org/Number    
            type: Property    
        zoneId:    
          description: Zone ID corresponding to this observation    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        zoneName:    
          description: Zone name corresponding to this observation    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
      type: object    
      x-ngsi:    
        model: https://schema.org/Text    
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
    pedestrianPathLeftHeight:    
      description: Height of the walkway placed on the left edge of the road corresponding to this observation    
      type: number    
      x-ngsi:    
        type: Property    
    pedestrianPathLeftWidth:    
      description: Width of the walkway placed on the left edge of the road corresponding to this observation    
      type: number    
      x-ngsi:    
        type: Property    
    pedestrianPathMaterial:    
      description: Construction material used for laying the walkway / footpath on the sides of the road corresponding to this observation    
      type: string    
      x-ngsi:    
        type: Property    
    pedestrianPathPlacement:    
      description: 'Describes the presence and placement of pedestrian along the road segment corresponding to this observation. Enum:''RIGHT, LEFT, BOTH, NOT_AVAILABLE'''    
      type: string    
      x-ngsi:    
        type: Property    
    pedestrianPathRightHeight:    
      description: Height of the walkway placed on the right edge of the road corresponding to this observation    
      type: number    
      x-ngsi:    
        type: Property    
    pedestrianPathRightWidth:    
      description: Width of the walkway placed on the right edge of the road corresponding to this observation    
      type: number    
      x-ngsi:    
        type: Property    
    refRoad:    
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
      description: Road to which this road segment belongs to    
      x-ngsi:    
        type: Relationship    
    rightOfWayWidth:    
      description: 'Right of Way (RoW) is the total land area available for the roadway. Its width accommodates for carriages way + other necessities + future extension, along the road''s alignment'    
      type: number    
      x-ngsi:    
        type: Property    
    roadClass:    
      description: 'The type of road corresponding to this observation. Enum: [OTHER_PUBLIC_ROAD, PRIVATE_ROAD, MINOR_CITY_ROAD, MAJOR_DISTRICT_ROAD, MAJOR_CITY_ROAD, NATIONAL_HIGHWAY, SERVICE_ROAD, STATE_HIGHWAY, OTHER_DISTRICT_ROAD, PORT_ROAD]'    
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
      description: 'Represents the direction the road is heading to. Enum:'' [''N, S, E, W''. The values N,S,E,W represent North,South,East,West respectively'    
      type: string    
      x-ngsi:    
        type: Property    
    roadId:    
      description: Unique internal representation of the road corresponding to this observation    
      type: string    
      x-ngsi:    
        type: Property    
    roadMaterial:    
      description: 'The construction material used for laying the carriageway corresponding to this observation. For eg. concrete, earthen, tar etc'    
      type: string    
      x-ngsi:    
        type: Property    
    roadName:    
      description: The name of the road corresponding to this observation    
      type: string    
      x-ngsi:    
        type: Property    
    roadWork:    
      description: 'Reasons for the road work in case of urgent intervention. A combination of these values. Enum:''COLLAPSE, DERAILMENT, FIRE, FLOOD, GASLEAK, LANDSLIDE, OTHER, POWERCUT, ROCKFALL, SAGGING, WATERLEAK'''    
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
    startKilometer:    
      description: 'The kilometer number (measured from the road''s start point) where this road segment starts. '    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    startPoint:    
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
    status:    
      description: 'Specific driving conditions on the roadsegment. Use statusDescription for additional information. Enum: ‘open, closed, limited’.  `open`: the roadsegment can be used in full intended capacity, `closed`: no traffic is possible, e.g. due to roadworks, an open bridge or lock, or any other event preventing traffic. `limited`: traffic is possible, but not in the full capacity'    
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
      description: Additional information to the status attribute    
      type: string    
      x-ngsi:    
        type: Property    
    totalCyclePathWidth:    
      description: Total width of the cycle track present in the road corresponding to this observation    
      type: number    
      x-ngsi:    
        type: Property    
    totalLaneNumber:    
      description: Total number of lanes offered by this road segment    
      minimum: 1    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    totalPedestrianPathLength:    
      description: Total length of the walkway present in the road corresponding to this observation    
      type: number    
      x-ngsi:    
        type: Property    
    totalPedestrianPathWidth:    
      description: Total width of the walkway present in the road corresponding to this observation    
      type: number    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be RoadSegment    
      enum:    
        - RoadSegment    
      type: string    
      x-ngsi:    
        type: Property    
    width:    
      description: Road's segment width.    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Meter (m)    
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Transportation/blob/master/RoadSegment/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Transportation/RoadSegment/schema.json    
  x-model-tags: IUDX    
  x-version: 0.4.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
Le proprietà `laneUsage` e quelle che indicano i parametri massimi consentiti possono essere dinamiche, ad esempio la direzione di una corsia può essere temporaneamente modificata per migliorare le condizioni del traffico.  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Esempi di payload  
#### Valori-chiave RoadSegment NGSI-v2 Esempio  
Ecco un esempio di RoadSegment in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### RoadSegment NGSI-v2 normalizzato Esempio  
Ecco un esempio di RoadSegment in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano le opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### Valori chiave RoadSegment NGSI-LD Esempio  
Ecco un esempio di RoadSegment in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
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
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Transportation/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### RoadSegment NGSI-LD normalizzato Esempio  
Ecco un esempio di RoadSegment in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di grandezza.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
