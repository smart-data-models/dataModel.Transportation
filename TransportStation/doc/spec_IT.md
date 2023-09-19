<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: Stazione di trasporto  
=============================<!-- /10-Header -->  
<!-- 15-License -->  
[Licenza aperta](https://github.com/smart-data-models//dataModel.Transportation/blob/master/TransportStation/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descrizione globale: **Il modello di dati è una descrizione generale delle stazioni urbane (Metro, Bus, Tram, Eliporto, ...) secondo lo standard GFTS https://developers.google.com/transit/gtfs/reference/#stopstxt, così come la descrizione dettagliata di queste (mezzi di accesso, piattaforma, assistenza, ...).  
versione: 0.1.3  
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
- `alternateName[string]`: Un nome alternativo per questa voce  - `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `contactPoint[object]`: I dati da contattare con l'articolo  . Model: [https://schema.org/ContactPoint](https://schema.org/ContactPoint)	- `areaServed[string]`: L'area geografica in cui viene fornito un servizio o un articolo offerto. Sostituisce ServiceArea    
	- `availabilityRestriction[*]`: Questa proprietà collega un punto di contatto a informazioni su quando il punto di contatto non è disponibile. I dettagli sono forniti utilizzando la classe Specifica degli orari di apertura  . Model: [http://schema.org/hoursAvailable](http://schema.org/hoursAvailable)  
	- `availableLanguage[*]`: Una lingua che qualcuno può usare con o per l'oggetto, il servizio o il luogo. Utilizzare uno dei codici lingua dello standard BCP 47 dell'IETF. È stata implementata l'opzione Testo, ma potrebbe essere anche Lingua.  . Model: [http://schema.org/availableLanguage](http://schema.org/availableLanguage)  
	- `contactOption[*]`: Un'opzione disponibile su questo punto di contatto (ad esempio un numero verde o un supporto per chi chiama con problemi di udito)  . Model: [http://schema.org/contactOption](http://schema.org/contactOption)  
	- `contactType[string]`: Tipo di contatto di questo articolo    
	- `email[idn-email]`: Indirizzo e-mail del proprietario    
	- `faxNumber[string]`: Il numero di fax  . Model: [http://schema.org/Text](http://schema.org/Text)  
	- `name[string]`: Il nome di questo elemento    
	- `productSupported[string]`: Il prodotto o il servizio a cui si riferisce il punto di contatto dell'assistenza (ad esempio, l'assistenza per una particolare linea di prodotti). Può trattarsi di un prodotto o di una linea di prodotti specifici (ad esempio, "iPhone") o di una categoria generale di prodotti o servizi (ad esempio, "smartphone").  . Model: [http://schema.org/Text](http://schema.org/Text)  
	- `telephone[string]`: Telefono di questo contatto    
- `contractingAuthority[string]`: Nome dell'amministrazione aggiudicatrice  - `contractingCompany[string]`: Nome della società appaltatrice responsabile dello sfruttamento della stazione  - `dataProvider[string]`: una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata  - `dateCreated[date-time]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `dateLastReported[date-time]`: Un timestamp che indica l'ultima volta in cui il dispositivo ha riportato dati con successo. Data e ora in formato ISO8601 UTC  - `dateModified[date-time]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `description[string]`: Descrizione dell'articolo  - `dimension[object]`: Dimensione globale. Il formato è strutturato da una sotto-proprietà di 3 elementi. Il codice dell'unità (testo) è fornito utilizzando i [Codici comuni UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Ad esempio, **MTR** rappresenta i metri.  	- `depth`:     
	- `height`:     
- `id[*]`: Identificatore univoco dell'entità  - `installationMode[string]`: Posizione rispetto al riferimento al suolo. Enum:'aerial, ground, underGround, underSea'.  - `inventory[object]`: Mappatura generale dei dati solo per `locationType` = 0, 1, 3, 4. Il formato è strutturato da una sotto-proprietà di 4 elementi  	- `PlatformType`:     
	- `nbOfIOPoint`:     
	- `nbOfLane`:     
- `levelId[number]`: Piano in cui si trova la posizione. Indice numerico associato al piano. Indica la posizione relativa di questo piano rispetto agli altri. L'indice 0 indica il piano terra. I piani sopra il livello del suolo sono indicati da indici positivi e gli stadi sotterranei da indici negativi.  - `location[*]`: Riferimento geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `locationType[number]`: Collegamento all'archivio standard GTFS che descrive le diverse località [Tipo di località]. 0 Fermata o piattaforma (luogo in cui gli utenti salgono o scendono da un veicolo di trasporto pubblico). 1 Stazione (area o struttura fisica che comprende una o più piattaforme). 2 Ingresso o uscita (luogo in cui gli utenti possono entrare/uscire da una stazione dalla strada). 3 Intersezione generica (luogo in una stazione che non corrisponde a nessun altro valore di `tipo_di_localizzazione`). 4 Area di imbarco (luogo specifico su un binario dove gli utenti possono salire/scendere con un veicolo).  - `name[string]`: Il nome di questo elemento  - `openingHoursSpecification[array]`: Un valore strutturato che fornisce informazioni sugli orari di apertura di un luogo o di un determinato servizio all'interno di un luogo.  . Model: [https://schema.org/openingHoursSpecification](https://schema.org/openingHoursSpecification)- `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `parentStation[*]`: Collegamento all'archivio standard GTFS che descrive il diverso collegamento tra stazione e piattaforma [Parent STATION]. Caso '1' location_type = 0 (Stop / platform ), il campo parent_station contiene l'ID di una stazione. Caso '2' location_type = 1 (Station), questo campo deve essere vuoto. Caso '3' location_type = 2 (Input / output) o location_type = 3 (intersezione generica), il campo parent_station contiene l'ID di una stazione location_type = 1. Caso '4' location_type = 4 (area di imbarco), il campo parent_station contiene l'ID di una piattaforma  - `platformCode[number]`: Identificatore del binario per una fermata di tipo binario `location_type` = 0 se la fermata è in una stazione  - `refPointOfInterest[*]`: Un riferimento a un punto di interesse associato a questa osservazione.  - `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `stationConnected[array]`: Connessioni possibili da questa stazione. Un valore strutturato da 0 a N occorrenze, dove ogni voce è una stringa nel formato `stationType` : [Elenco delle linee collegate, separate da una virgola]. Enum:'aerialLift, bus, cableTram, ferry, funicular, monorail, rail, subway, train, tram, trolleybus'.  - `stationType[array]`: Tipo di stazione di trasporto. Enum:'aerialLift, bus, cableTram, ferry, funicular, monorail, rail, subway, trolleybus, tram'.  - `type[string]`: Tipo di entità NGSI. Deve essere TransportStation  - `webSite[string]`: Link al sito ufficiale per maggiori informazioni  - `wheelChairAccessible[number]`: Accesso possibile per le persone a mobilità ridotta. Per le fermate senza genitori 0 non sono disponibili informazioni sull'accessibilità della fermata. 1 alcuni veicoli di questa fermata possono far salire un utente PMR. 2 L'utente PMR non può salire su questa fermata. Per una fermata che fa parte di una stazione 0 la fermata eredita il comportamento di imbarco di sedie a rotelle della stazione madre, se questa è compilata. 1 le corsie consentono l'accesso delle sedie a rotelle alla fermata/piattaforma dall'esterno della stazione. 2 nessuna corsia consente l'accesso della sedia a rotelle alla fermata/piattaforma dall'esterno della stazione. Per gli ingressi/uscite della stazione 0 l'ingresso della stazione eredita il comportamento di accesso per sedie a rotelle della stazione principale, se specificato. 1 l'ingresso della stazione è accessibile alle sedie a rotelle. 2 nessun percorso accessibile alle sedie a rotelle collega l'ingresso della stazione alle fermate/piattaforme.  - `zoneId[string]`: Zona tariffaria della stazione  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Proprietà richieste  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Modello di dati descrizione delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
TransportStation:    
  description: "The data model is a general description of urban stations (Metro, Bus, Tram, Heliport, ...) according to the GFTS standard https://developers.google.com/transit/gtfs/reference/#stopstxt, as well the detailed description of these (means of access, platform, assistance, ...)."    
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
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    contactPoint:    
      description: The details to contact with the item    
      properties:    
        areaServed:    
          description: The geographic area where a service or offered item is provided. Supersedes serviceArea    
          type: string    
          x-ngsi:    
            type: Property    
        availabilityRestriction:    
          anyOf:    
            - description: Array of identifiers format of any NGSI entity    
              items:    
                maxLength: 256    
                minLength: 1    
                pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
                type: string    
              type: array    
              x-ngsi:    
                type: Property    
            - description: Array of identifiers format of any NGSI entity    
              items:    
                format: uri    
                type: string    
              type: array    
              x-ngsi:    
                type: Property    
          description: This property links a contact point to information about when the contact point is not available. The details are provided using the Opening Hours Specification class    
          x-ngsi:    
            model: http://schema.org/hoursAvailable    
            type: Relationship    
        availableLanguage:    
          anyOf:    
            - anyOf:    
                - type: string    
                - items:    
                    type: string    
                  type: array    
          description: 'A language someone may use with or at the item, service or place. Please use one of the language codes from the IETF BCP 47 standard. It is implemented the Text option but it could be also Language'    
          x-ngsi:    
            model: http://schema.org/availableLanguage    
            type: Property    
        contactOption:    
          anyOf:    
            - type: string    
            - items:    
                type: string    
              type: array    
          description: An option available on this contact point (e.g. a toll-free number or support for hearing-impaired callers)    
          x-ngsi:    
            model: http://schema.org/contactOption    
            type: Property    
        contactType:    
          description: Contact type of this item    
          type: string    
          x-ngsi:    
            type: Property    
        email:    
          description: Email address of owner    
          format: idn-email    
          type: string    
          x-ngsi:    
            type: Property    
        faxNumber:    
          description: The fax number    
          type: string    
          x-ngsi:    
            model: http://schema.org/Text    
            type: Property    
        name:    
          description: The name of this item    
          type: string    
          x-ngsi:    
            type: Property    
        productSupported:    
          description: The product or service this support contact point is related to (such as product support for a particular product line). This can be a specific product or product line (e.g. 'iPhone') or a general category of products or services (e.g. 'smartphones')    
          type: string    
          x-ngsi:    
            model: http://schema.org/Text    
            type: Property    
        telephone:    
          description: Telephone of this contact    
          type: string    
          x-ngsi:    
            type: Property    
        url:    
          description: URL which provides a description or further information about this item    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        model: https://schema.org/ContactPoint    
        type: Property    
    contractingAuthority:    
      description: Name of the contracting authority    
      type: string    
      x-ngsi:    
        type: Property    
    contractingCompany:    
      description: Name of the contracting company responsible for the exploitation of the station    
      type: string    
      x-ngsi:    
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
    dateLastReported:    
      description: A timestamp which denotes the last time when the device successfully reported data. Date and time in an ISO8601 UTCformat    
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
    dimension:    
      description: 'Global dimension. The format is structured by a sub-property of 3 items. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **MTR** represents Meters'    
      properties:    
        depth:    
          minimum: 0    
          type: number    
        height:    
          minimum: 0    
          type: number    
        width:    
          minimum: 0    
          type: number    
      type: object    
      x-ngsi:    
        type: Property    
        units: meters    
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
    installationMode:    
      description: 'Location  relative to the ground reference. Enum:''aerial, ground, underGround, underSea'''    
      enum:    
        - aerial    
        - ground    
        - underGround    
        - underSea    
      type: string    
      x-ngsi:    
        type: Property    
    inventory:    
      description: 'General data mapping only for `locationType` = 0, 1, 3, 4. The format is structured by a sub-property of 4 items'    
      properties:    
        PlatformType:    
          items:    
            enum:    
              - lateral    
              - central    
            type: string    
          type: array    
        nbOfIOPoint:    
          minimum: 0    
          type: number    
        nbOfLane:    
          minimum: 0    
          type: number    
        nbOfPlatform:    
          minimum: 0    
          type: number    
      type: object    
      x-ngsi:    
        type: Property    
    levelId:    
      description: 'Floor on which the location is located. Numerical index associated with the floor. Indicates the relative position of this stage in relation to the others. The index 0 indicates the ground floor. The floors above ground level are indicated by positive indices, and the underground stages by negative indices'    
      type: number    
      x-ngsi:    
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
    locationType:    
      description: 'Link to the GTFS standard repository describing the different location [Location Type]. 0 Stop or platform (place where users get on or off in a public transport vehicle). 1 Station (area or physical structure comprising one or more platforms). 2 Entrance or Exit (place where users can enter / exit a station from the street). 3 Generic intersection (location in a station that doesn''t correspond to any other `location_type` value). 4 Boarding area of a specific location on a platform where users can get on / off in a vehicle'    
      enum:    
        - 0    
        - 1    
        - 2    
        - 3    
        - 4    
      type: number    
      x-ngsi:    
        type: Property    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    openingHoursSpecification:    
      description: A structured value providing information about the opening hours of a place or a certain service inside a place    
      items:    
        properties:    
          closes:    
            description: ' 	The closing hour of the place or service on the given day(s) of the week'    
            format: time    
            type: string    
            x-ngsi:    
              type: Property    
          dayOfWeek:    
            anyOf:    
              - description: Array of days of the week    
                enum:    
                  - Monday    
                  - Tuesday    
                  - Wednesday    
                  - Thursday    
                  - Friday    
                  - Saturday    
                  - Sunday    
                  - PublicHolidays    
                type: string    
                x-ngsi:    
                  type: Property    
              - description: Array of days of the week    
                enum:    
                  - https://schema.org/Monday    
                  - https://schema.org/Tuesday    
                  - https://schema.org/Wednesday    
                  - https://schema.org/Thursday    
                  - https://schema.org/Friday    
                  - https://schema.org/Saturday    
                  - https://schema.org/Sunday    
                  - https://schema.org/PublicHolidays    
                type: string    
                x-ngsi:    
                  type: Property    
            description: 'The day of the week for which these opening hours are valid. URLs from GoodRelations (http://purl.org/goodrelations/v1) are used (for Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday plus a special entry for PublicHolidays)'    
            type: string    
            x-ngsi:    
              model: http://schema.org/dayOfWeek    
              type: Property    
          opens:    
            description: The opening hour of the place or service on the given day(s) of the week    
            format: time    
            type: string    
            x-ngsi:    
              type: Property    
          validFrom:    
            anyOf:    
              - description: ""    
                format: date    
                type: string    
                x-ngsi:    
                  model: http://schema.org/Date    
                  type: Property    
              - description: ""    
                format: date-time    
                type: string    
                x-ngsi:    
                  model: http://schema.org/DateTime    
                  type: Property    
            description: 'The date when the item becomes valid. A date value in the form CCYY-MM-DD or a combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm] in ISO 8601 date format'    
            x-ngsi:    
              type: Property    
          validThrough:    
            anyOf:    
              - description: ""    
                format: date    
                type: string    
                x-ngsi:    
                  model: http://schema.org/Date    
                  type: Property    
              - description: ""    
                format: date-time    
                type: string    
                x-ngsi:    
                  model: http://schema.org/DateTime    
                  type: Property    
            description: 'The date after when the item is not valid. For example the end of an offer, salary period, or a period of opening hours. A date value in the form CCYY-MM-DD or a combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm] in ISO 8601 date format'    
            type: string    
            x-ngsi:    
              type: Property    
        type: object    
      minItems: 1    
      type: array    
      x-ngsi:    
        model: https://schema.org/openingHoursSpecification    
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
    parentStation:    
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
      description: 'Link to the GTFS standard repository describing the different link between Station and Platform [Parent STATION]. Case ''1'' location_type = 0 (Stop / platform ), the parent_station field contains the ID of a station. Case ''2'' location_type = 1  (Station), this field must be empty. Case ''3'' location_type = 2 (Input / output) or location_type = 3 (generic intersection), the parent_station field contains the ID of a station location_type = 1. Case ''4'' location_type = 4 (boarding area), the parent_station field contains the ID of a platform'    
      x-ngsi:    
        type: Relationship    
    platformCode:    
      description: Platform identifier for a platform type stop `location_type` = 0 when the stop is in a station    
      type: number    
      x-ngsi:    
        type: Property    
    refPointOfInterest:    
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
      description: A reference to a point of interest associated to this observation    
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    stationConnected:    
      architect:    
        type: string    
      commissioningDate:    
        format: date-time    
        type: string    
      constructionDate:    
        format: date-time    
        type: string    
      currencyAccepted:    
        items:    
          enum:    
            - EUR    
            - USD    
          type: string    
        type: array    
      description: 'Connections possible from this station. A structured value from 0 to N occurrences where each items is a string in the format `stationType` : [List of Lines connected, separated by a comma]. Enum:''aerialLift, bus, cableTram, ferry, funicular, monorail, rail, subway, train, tram, trolleybus'''    
      featuredArtist:    
        items:    
          anyOf:    
            - anyOf:    
                - description: Property. Identifier format of any NGSI entity    
                  maxLength: 256    
                  minLength: 1    
                  pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
                  type: string    
                - description: Property. Identifier format of any NGSI entity    
                  format: uri    
                  type: string    
              description: Property. Unique identifier of the entity    
            - type: string    
        type: array    
      items:    
        properties:    
          linesConnected:    
            items:    
              type: string    
            type: array    
          stationType:    
            enum:    
              - aerialLift    
              - bus    
              - cableTram    
              - ferry    
              - funicular    
              - monorail    
              - rail    
              - subway    
              - train    
              - tram    
              - trolleybus    
            type: string    
        type: object    
      paymentAccepted:    
        items:    
          enum:    
            - Cash    
            - CreditCard    
            - CryptoCurrency    
            - other    
          type: string    
        type: array    
      services:    
        properties:    
          defibrillator:    
            type: Boolean    
          emergencyPhone:    
            type: Boolean    
          informationBoardDevice:    
            type: Boolean    
          interactiveDevice:    
            type: Boolean    
          messageDevice:    
            type: Boolean    
          purchaseDevice:    
            type: Boolean    
          restBench:    
            type: Boolean    
          shelters:    
            type: Boolean    
          timetableDevice:    
            type: Boolean    
          voiceDevice:    
            type: Boolean    
          wheelChairAccessible:    
            type: Boolean    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    stationType:    
      description: 'Type of transport station. Enum:''aerialLift, bus, cableTram, ferry, funicular, monorail, rail, subway, trolleybus, tram'''    
      items:    
        enum:    
          - aerialLift    
          - bus    
          - cableTram    
          - ferry    
          - funicular    
          - monorail    
          - rail    
          - subway    
          - trolleybus    
          - tram    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be TransportStation    
      enum:    
        - TransportStation    
      type: string    
      x-ngsi:    
        type: Property    
    webSite:    
      description: Link to the official website for more information    
      type: string    
      x-ngsi:    
        type: Property    
    wheelChairAccessible:    
      description: 'Access possible for Person with Reduced Mobility. For stops without parents 0 no information is available regarding the accessibility of the stop. 1 some vehicles at this stop can board a PMR user. 2 PRM user cannot board  at this stop. For a stop that is part of a station 0 the stop inherits the wheelchair_boarding behavior of the parent station, if it is filled in. 1 lanes provide wheelchair access to the stop / platform  from outside the station. 2 no lane provides wheelchair access to the stop / platform from outside the station. For station inputs / outputs 0 the station entry inherits the wheelchair_boarding behavior of the main station, if specified. 1 the station entrance is wheelchair accessible. 2 no wheelchair accessible route connects the station entrance to the stops / platforms'    
      enum:    
        - 0    
        - 1    
        - 2    
      type: number    
      x-ngsi:    
        type: Property    
    zoneId:    
      description: Pricing zone of the station    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Transportation/blob/master/TransportStation/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/data-models/Transportation/TransportStation/schema.json    
  x-model-tags: ""    
  x-version: 0.1.3    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Esempi di payload  
#### TransportStation NGSI-v2 Valori chiave Esempio  
Ecco un esempio di TransportStation in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Station:Station:MNCA-STram-L02-AP-T2",  
  "type": "TransportStation",  
  "name": "NCE-Tram-Station-L02-AP-T2",  
  "alternateName": "Nice - Tramway Station Description - L02-AP-T2",  
  "description": "Description and services provided in the station",  
  "seeAlso": "http://tramway.nice.fr/wp-content/uploads/2019/10/BD_pocket_plan_MAJ03_2019_20082019.pdf",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      43.664810,  
      7.196545  
    ]  
  },  
  "address": {  
    "addressCountry": "FR",  
    "addressLocality": "Nice",  
    "streetAddress": "Airport - Terminal 2 - Door A2"  
  },  
  "areaServed": "Nice Airport",  
  "dateLastReported": "2020-03-17T08:45:00Z",  
  "dateObserved": "2020-03-17T08:45:00Z",  
  "stationType": [  
    "tram"  
  ],  
  "locationType": 1,  
  "levelId": 0,  
  "zoneId": "B",  
  "wheelChairAccessible": 1,  
  "openingHoursSpecification": [  
    {  
      "dayOfWeek": "Monday",  
      "opens": "07:00:00",  
      "closes": "22:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Tuesday",  
      "opens": "07:00:00",  
      "closes": "22:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Wednesday",  
      "opens": "07:00:00",  
      "closes": "22:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Thursday",  
      "opens": "07:00:00",  
      "closes": "22:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Friday",  
      "opens": "07:00:00",  
      "closes": "22:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Saturday",  
      "opens": "08:00:00",  
      "closes": "23:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Sunday",  
      "opens": "08:30:00",  
      "closes": "21:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "PublicHolidays",  
      "opens": "08:30:00",  
      "closes": "21:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    }  
  ],  
  "owner": [  
    "uri:ngsi:StreetRetail"  
  ],  
  "contractingAuthority": "MNCA - Metropole Nice Cote d'Azur",  
  "contractingCompagny": "Régie Ligne d'Azur",  
  "contactPoint": {  
    "url": "uri:ngsi:www.lignesdazur.com"  
  },  
  "webSite": "https://tramway.nice.fr/Plan-Station-L02-AP-T2.pdf",  
  "instalationMode": "ground",  
  "dimension": {  
    "length": 300,  
    "width": 25,  
    "thickness": 6.35  
  },  
  "inventory": {  
    "nbOfIOPoint": 2,  
    "nbOfLane": 1,  
    "nbOfPlatform": 1,  
    "PlatformType": [  
      "lateral"  
    ]  
  },  
  "stationConnected": [  
    {  
      "stationType": "tram",  
      "linesConnected": [  
        "Tram 2 - CADAM / Nikaia",  
        "Tram 3 - Saint Isidore / Stade Allianz Riviera"  
      ]  
    },  
    {  
      "stationType": "train",  
      "linesConnected": [  
        "Gare SNCF Nice Saint Augustin (600m)"  
      ]  
    },  
    {  
      "stationType": "bus",  
      "linesConnected": [  
        "L20 - Giono / Les Pugets",  
        "L20 - Centre Commercial St Isidore",  
        "L21 - Le Gué / Polygone Riviera",  
        "L54 - Centre Commercial Cap 3000 - St Jeannet",  
        "L90 - La Bolline",  
        "91 Auron",  
        "L92 - Isola 2000"  
      ]  
    }  
  ],  
  "services": {  
    "purchaseDevice": true,  
    "interactiveDevice": true,  
    "timetableDevice": true,  
    "voiceDevice": true,  
    "informationBoardDevice": true,  
    "messageDevice": false,  
    "shelters": true,  
    "restBench": false,  
    "emergencyPhone": false,  
    "videoSurveillance": true,  
    "defibrillator": false,  
    "wheelChairAccessible": true  
  },  
  "paymentAccepted": [  
    "Cash",  
    "CreditCard"  
  ],  
  "currencyAccepted": [  
    "EUR"  
  ],  
  "constructionDate": "2016-19-08",  
  "commissioningDate": "2018-09-15",  
  "architect": "Nice Architecture",  
  "featuredArtist ": [  
    "Leopold",  
    "De Renaiss"  
  ]  
}  
```  
</details>  
#### TransportStation NGSI-v2 normalizzato Esempio  
Ecco un esempio di TransportStation in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si usano opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Station:Station:MNCA-STram-L02-AP-T2",  
  "type": "TransportStation",  
  "name": {  
    "type": "Property",  
    "value": "NCE-Tram-Station-L02-AP-T2"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Nice - Tramway Station Description - L02-AP-T2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Description and services provided in the station"  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": "http://tramway.nice.fr/wp-content/uploads/2019/10/BD_pocket_plan_MAJ03_2019_20082019.pdf"  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        43.664810,  
        7.196545  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "addressCountry": "FR",  
      "addressLocality": "Nice",  
      "streetAddress": "Airport - Terminal 2 - Door A2"  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Nice Airport"  
  },  
  "dateLastReported": {  
    "type": "DateTime",  
    "value": "2020-03-17T08:45:00Z"  
  },  
  "stationType": {  
    "type": "Property",  
    "value": ["tram"]  
  },  
  "locationType": {  
    "type": "Property",  
    "value": 1  
  },  
  "levelId": {  
    "type": "Property",  
    "value": 0  
  },  
  "zoneId": {  
    "type": "Property",  
    "value": "B"  
  },  
  "wheelChairAccessible": {  
    "type": "Property",  
    "value": 1  
  },  
  "openingHoursSpecification": {  
    "type": "object",  
    "value": [  
      {  
        "dayOfWeek": "Monday, Tuesday, Wednesday, Thursday, Friday",  
        "opens": "07:00:00",  
        "closes": "22:00:00",  
        "validFrom": "2021-01-01T00:00:00",  
        "validThrough": "2021-12-31T23:59:59"  
      },  
      {  
        "dayOfWeek": "Saturday",  
        "opens": "08:00:00",  
        "closes": "23:00:00",  
        "validFrom": "2021-01-01T00:00:00",  
        "validThrough": "2021-12-31T23:59:59"  
      },  
      {  
        "dayOfWeek": "Sunday",  
        "opens": "8:00:30",  
        "closes": "21:00:00",  
        "validFrom": "2021-01-01T00:00:00",  
        "validThrough": "2021-12-31T23:59:59"  
      },  
      {  
        "dayOfWeek": "PublicHolidays",  
        "opens": "8:00:00",  
        "closes": "21:00:30",  
        "validFrom": "2021-01-01T00:00:00",  
        "validThrough": "2021-12-31T23:59:59"  
      }  
    ]  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "Street furniture Urbain & Retail"  
    ]  
  },  
  "contractingAuthority": {  
    "type": "Property",  
    "value": "MNCA - Metropole Nice Cote d'Azur"  
  },  
  "contractingCompany": {  
    "type": "Property",  
    "value": "Régie Ligne d'Azur"  
  },  
  "contactPoint": {  
    "type": "Property",  
    "value": {  
      "url": "www.lignesdazur.com"  
    }  
  },  
  "webSite": {  
    "type": "Property",  
    "value": "https://tramway.nice.fr/Plan-Station-L02-AP-T2.pdf"  
  },  
  "installationMode": {  
    "type": "Property",  
    "value": "ground"  
  },  
  "dimension": {  
    "type": "Property",  
    "value": {  
      "length": 300,  
      "width": 25,  
      "thickness": 6.35  
    }  
  },  
  "inventory": {  
    "type": "Property",  
    "value": {  
      "nbOfIOPoint": 2,  
      "nbOfLane": 1,  
      "nbOfPlatform": 1,  
      "PlatformType": ["lateral"]  
    }  
  },  
  "stationConnected": {  
    "type": "Property",  
    "value": [  
      {  
        "stationType": "tram",  
        "linesConnected": {  
          "type": "Property",  
          "value": [  
            "Tram 2 - CADAM / Nikaia",  
            "Tram 3 - Saint Isidore / Stade Allianz Riviera"  
          ]  
        }  
      },  
      {  
        "stationType": "train",  
        "linesConnected": {  
          "type": "Property",  
          "value": [  
            "Gare SNCF Nice Saint Augustin (600m)"  
          ]  
        }  
      },  
      {  
        "stationType": "bus",  
        "linesConnected": {  
          "type": "Property",  
          "value": [  
            "L20 - Giono / Les Pugets",  
            "L20 - Centre Commercial St Isidore",  
            "L21 - Le Gué / Polygone Riviera",  
            "L54 - Centre Commercial Cap 3000 - St Jeannet",  
            "L90 - La Bolline",  
            "91 Auron",  
            "L92 - Isola 2000"  
          ]  
        }  
      }  
    ]  
  },  
  "services": {  
    "type": "Property",  
    "value": {  
      "purchaseDevice": {  
        "type": "Property",  
        "value": true  
      },  
      "interactiveDevice": {  
        "type": "Property",  
        "value": true  
      },  
      "timetableDevice": {  
        "type": "Property",  
        "value": true  
      },  
      "voiceDevice": {  
        "type": "Property",  
        "value": true  
      },  
      "informationBoardDevice": {  
        "type": "Property",  
        "value": true  
      },  
      "messageDevice": {  
        "type": "Property",  
        "value": false  
      },  
      "shelters": {  
        "type": "Property",  
        "value": true  
      },  
      "restBench": {  
        "type": "Property",  
        "value": false  
      },  
      "emergencyPhone": {  
        "type": "Property",  
        "value": false  
      },  
      "videoSurveillance": {  
        "type": "Property",  
        "value": true  
      },  
      "defibrillator": {  
        "type": "Property",  
        "value": false  
      },  
      "wheelChairAccessible": {  
        "type": "Property",  
        "value": true  
      }  
    }  
  },  
  "paymentAccepted": {  
    "type": "Property",  
    "value": [  
      "Cash",  
      "CreditCard"  
    ]  
  },  
  "currencyAccepted": {  
    "type": "Property",  
    "value": [  
      "EUR"  
    ]  
  },  
  "constructionDate": {  
    "type": "DateTime",  
    "value": "2016-19-08"  
  },  
  "commissioningDate": {  
    "type": "DateTime",  
    "value": "2018-09-15"  
  },  
  "architect": {  
    "type": "Property",  
    "value": "Nice Architecture"  
  },  
  "featuredArtist ": {  
    "type": "Property",  
    "value": [  
      "Leopold",  
      "De Renaiss"  
    ]  
  }  
}  
```  
</details>  
#### TransportStation NGSI-LD valori chiave Esempio  
Ecco un esempio di TransportStation in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Station:Station:MNCA-STram-L02-AP-T2",  
  "type": "TransportStation",  
  "address": {  
    "addressCountry": "FR",  
    "addressLocality": "Nice",  
    "streetAddress": "Airport - Terminal 2 - Door A2"  
  },  
  "alternateName": "Nice - Tramway Station Description - L02-AP-T2",  
  "architect": "Nice Architecture",  
  "areaServed": "Nice Airport",  
  "commissioningDate": "2018-09-15",  
  "constructionDate": "2016-19-08",  
  "contactPoint": {  
    "url": "uri:ngsi:www.lignesdazur.com"  
  },  
  "contractingAuthority": "MNCA - Metropole Nice Cote d'Azur",  
  "contractingCompagny": "R\u00e9gie Ligne d'Azur",  
  "currencyAccepted": [  
    "EUR"  
  ],  
  "dateLastReported": "2020-03-17T08:45:00Z",  
  "dateObserved": "2020-03-17T08:45:00Z",  
  "description": "Description and services provided in the station",  
  "dimension": {  
    "length": 300,  
    "width": 25,  
    "thickness": 6.35  
  },  
  "featuredArtist ": [  
    "Leopold",  
    "De Renaiss"  
  ],  
  "instalationMode": "ground",  
  "inventory": {  
    "nbOfIOPoint": 2,  
    "nbOfLane": 1,  
    "nbOfPlatform": 1,  
    "PlatformType": [  
      "lateral"  
    ]  
  },  
  "levelId": 0,  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      43.66481,  
      7.196545  
    ]  
  },  
  "locationType": 1,  
  "name": "NCE-Tram-Station-L02-AP-T2",  
  "openingHoursSpecification": [  
    {  
      "dayOfWeek": "Monday",  
      "opens": "07:00:00",  
      "closes": "22:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Tuesday",  
      "opens": "07:00:00",  
      "closes": "22:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Wednesday",  
      "opens": "07:00:00",  
      "closes": "22:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Thursday",  
      "opens": "07:00:00",  
      "closes": "22:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Friday",  
      "opens": "07:00:00",  
      "closes": "22:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Saturday",  
      "opens": "08:00:00",  
      "closes": "23:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Sunday",  
      "opens": "08:30:00",  
      "closes": "21:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "PublicHolidays",  
      "opens": "08:30:00",  
      "closes": "21:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    }  
  ],  
  "owner": [  
    "uri:ngsi:StreetRetail"  
  ],  
  "paymentAccepted": [  
    "Cash",  
    "CreditCard"  
  ],  
  "seeAlso": "http://tramway.nice.fr/wp-content/uploads/2019/10/BD_pocket_plan_MAJ03_2019_20082019.pdf",  
  "services": {  
    "purchaseDevice": true,  
    "interactiveDevice": true,  
    "timetableDevice": true,  
    "voiceDevice": true,  
    "informationBoardDevice": true,  
    "messageDevice": false,  
    "shelters": true,  
    "restBench": false,  
    "emergencyPhone": false,  
    "videoSurveillance": true,  
    "defibrillator": false,  
    "wheelChairAccessible": true  
  },  
  "stationConnected": [  
    {  
      "stationType": "tram",  
      "linesConnected": [  
        "Tram 2 - CADAM / Nikaia",  
        "Tram 3 - Saint Isidore / Stade Allianz Riviera"  
      ]  
    },  
    {  
      "stationType": "train",  
      "linesConnected": [  
        "Gare SNCF Nice Saint Augustin (600m)"  
      ]  
    },  
    {  
      "stationType": "bus",  
      "linesConnected": [  
        "L20 - Giono / Les Pugets",  
        "L20 - Centre Commercial St Isidore",  
        "L21 - Le Gu\u00e9 / Polygone Riviera",  
        "L54 - Centre Commercial Cap 3000 - St Jeannet",  
        "L90 - La Bolline",  
        "91 Auron",  
        "L92 - Isola 2000"  
      ]  
    }  
  ],  
  "stationType": [  
    "tram"  
  ],  
  "webSite": "https://tramway.nice.fr/Plan-Station-L02-AP-T2.pdf",  
  "wheelChairAccessible": 1,  
  "zoneId": "B",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Transportation/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### TransportStation NGSI-LD normalizzato Esempio  
Ecco un esempio di TransportStation in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si usano opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Station:Station:MNCA-STram-L02-AP-T2",  
  "type": "TransportStation",  
  "name": {  
    "type": "Property",  
    "value": "NCE-Tram-Station-L02-AP-T2"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Nice - Tramway Station Description - L02-AP-T2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Description and services provided in the station"  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": "http://tramway.nice.fr/wp-content/uploads/2019/10/BD_pocket_plan_MAJ03_2019_20082019.pdf"  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        43.664810,  
        7.196545  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "addressCountry": "FR",  
      "addressLocality": "Nice",  
      "streetAddress": "Airport - Terminal 2 - Door A2"  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Nice Airport"  
  },  
  "dateLastReported": {  
    "type": "DateTime",  
    "value": "2020-03-17T08:45:00Z"  
  },  
  "stationType": {  
    "type": "Property",  
    "value": ["tram"]  
  },  
  "locationType": {  
    "type": "Property",  
    "value": 1  
  },  
  "levelId": {  
    "type": "Property",  
    "value": 0  
  },  
  "zoneId": {  
    "type": "Property",  
    "value": "B"  
  },  
  "wheelChairAccessible": {  
    "type": "Property",  
    "value": 1  
  },  
  "openingHoursSpecification": {  
    "type": "object",  
    "value": [  
      {  
        "dayOfWeek": "Monday, Tuesday, Wednesday, Thursday, Friday",  
        "opens": "07:00:00",  
        "closes": "22:00:00",  
        "validFrom": "2021-01-01T00:00:00",  
        "validThrough": "2021-12-31T23:59:59"  
      },  
      {  
        "dayOfWeek": "Saturday",  
        "opens": "08:00:00",  
        "closes": "23:00:00",  
        "validFrom": "2021-01-01T00:00:00",  
        "validThrough": "2021-12-31T23:59:59"  
      },  
      {  
        "dayOfWeek": "Sunday",  
        "opens": "8:00:30",  
        "closes": "21:00:00",  
        "validFrom": "2021-01-01T00:00:00",  
        "validThrough": "2021-12-31T23:59:59"  
      },  
      {  
        "dayOfWeek": "PublicHolidays",  
        "opens": "8:00:00",  
        "closes": "21:00:30",  
        "validFrom": "2021-01-01T00:00:00",  
        "validThrough": "2021-12-31T23:59:59"  
      }  
    ]  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "Street furniture Urbain & Retail"  
    ]  
  },  
  "contractingAuthority": {  
    "type": "Property",  
    "value": "MNCA - Metropole Nice Cote d'Azur"  
  },  
  "contractingCompany": {  
    "type": "Property",  
    "value": "Régie Ligne d'Azur"  
  },  
  "contactPoint": {  
    "type": "Property",  
    "value": {  
      "url": "www.lignesdazur.com"  
    }  
  },  
  "webSite": {  
    "type": "Property",  
    "value": "https://tramway.nice.fr/Plan-Station-L02-AP-T2.pdf"  
  },  
  "installationMode": {  
    "type": "Property",  
    "value": "ground"  
  },  
  "dimension": {  
    "type": "Property",  
    "value": {  
      "length": 300,  
      "width": 25,  
      "thickness": 6.35  
    }  
  },  
  "inventory": {  
    "type": "Property",  
    "value": {  
      "nbOfIOPoint": 2,  
      "nbOfLane": 1,  
      "nbOfPlatform": 1,  
      "PlatformType": ["lateral"]  
    }  
  },  
  "stationConnected": {  
    "type": "Property",  
    "value": [  
      {  
        "stationType": "tram",  
        "linesConnected": {  
          "type": "Property",  
          "value": [  
            "Tram 2 - CADAM / Nikaia",  
            "Tram 3 - Saint Isidore / Stade Allianz Riviera"  
          ]  
        }  
      },  
      {  
        "stationType": "train",  
        "linesConnected": {  
          "type": "Property",  
          "value": [  
            "Gare SNCF Nice Saint Augustin (600m)"  
          ]  
        }  
      },  
      {  
        "stationType": "bus",  
        "linesConnected": {  
          "type": "Property",  
          "value": [  
            "L20 - Giono / Les Pugets",  
            "L20 - Centre Commercial St Isidore",  
            "L21 - Le Gué / Polygone Riviera",  
            "L54 - Centre Commercial Cap 3000 - St Jeannet",  
            "L90 - La Bolline",  
            "91 Auron",  
            "L92 - Isola 2000"  
          ]  
        }  
      }  
    ]  
  },  
  "services": {  
    "type": "Property",  
    "value": {  
      "purchaseDevice": {  
        "type": "Property",  
        "value": true  
      },  
      "interactiveDevice": {  
        "type": "Property",  
        "value": true  
      },  
      "timetableDevice": {  
        "type": "Property",  
        "value": true  
      },  
      "voiceDevice": {  
        "type": "Property",  
        "value": true  
      },  
      "informationBoardDevice": {  
        "type": "Property",  
        "value": true  
      },  
      "messageDevice": {  
        "type": "Property",  
        "value": false  
      },  
      "shelters": {  
        "type": "Property",  
        "value": true  
      },  
      "restBench": {  
        "type": "Property",  
        "value": false  
      },  
      "emergencyPhone": {  
        "type": "Property",  
        "value": false  
      },  
      "videoSurveillance": {  
        "type": "Property",  
        "value": true  
      },  
      "defibrillator": {  
        "type": "Property",  
        "value": false  
      },  
      "wheelChairAccessible": {  
        "type": "Property",  
        "value": true  
      }  
    }  
  },  
  "paymentAccepted": {  
    "type": "Property",  
    "value": [  
      "Cash",  
      "CreditCard"  
    ]  
  },  
  "currencyAccepted": {  
    "type": "Property",  
    "value": [  
      "EUR"  
    ]  
  },  
  "constructionDate": {  
    "type": "DateTime",  
    "value": "2016-19-08"  
  },  
  "commissioningDate": {  
    "type": "DateTime",  
    "value": "2018-09-15"  
  },  
  "architect": {  
    "type": "Property",  
    "value": "Nice Architecture"  
  },  
  "featuredArtist ": {  
    "type": "Property",  
    "value": [  
      "Leopold",  
      "De Renaiss"  
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
