<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: Osservazione APDSO  
==========================<!-- /10-Header -->  
<!-- 15-License -->  
[Licenza aperta](https://github.com/smart-data-models//dataModel.Transportation/blob/master/APDSObservation/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descrizione globale: **Questa entità modella una particolare osservazione di un insieme di telecamere ANPR. L'osservazione può essere effettuata con diverse telecamere ANPR, ma è limitata all'osservazione di UN solo veicolo. Implementa il modello di dati APDS https://www.allianceforparkingdatastandards.org/**  
versione: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Elenco delle proprietà  

<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.  
- `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Il paese. Ad esempio, la Spagna  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: La località in cui si trova l'indirizzo civico e che si trova nella regione  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: La regione in cui si trova la località, e che si trova nel paese  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Un distretto è un tipo di divisione amministrativa che, in alcuni Paesi, è gestita dal governo locale.    
	- `postOfficeBoxNumber[string]`: Il numero di casella postale per gli indirizzi di casella postale. Ad esempio, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Il codice postale. Ad esempio, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: L'indirizzo stradale  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: Numero che identifica una proprietà specifica su una strada pubblica    
- `alternateName[string]`: Un nome alternativo per questa voce  - `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `creator[string]`: Id del conducente attuale.  - `dataProvider[string]`: una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata  - `dateCreated[date-time]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `dateModified[date-time]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `description[string]`: Descrizione dell'articolo  - `id[*]`: Identificatore univoco dell'entità  - `images[array]`: Array di link a immagini. L'elemento dell'array contiene gli URL delle immagini e informazioni aggiuntive. In alternativa all'URL delle immagini, l'immagine stessa può essere inclusa nell'attributo binaryContent.  - `location[*]`: Riferimento geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `name[string]`: Il nome di questo elemento  - `observationDateTime[date-time]`: L'ora in cui è stata effettuata l'osservazione (UTC). Obbligatorio se observationStartDateTime e observationEndDateTime non sono utilizzati.  - `observationEndDateTime[date-time]`: La data e l'ora di conclusione dell'evento di osservazione (in UTC) (ad esempio, un'auto è stata osservata uscire da una zona di consegna alle 9:33). Obbligatorio se non si usa creationDateTime.  - `observationStartDateTime[date-time]`: Data e ora di inizio dell'evento di osservazione (in UTC) (ad esempio, un'auto è stata osservata entrare in una zona di consegna alle 8:01). Obbligatorio se non si usa creationDateTime.  - `observedCredentialCharacterConfidence[array]`: La fiducia del riconoscimento dei singoli caratteri. Come per observedCredentialConfidence, questo è specifico del fornitore. Utilizzare i metadati per indicare come interpretare le confidenze.  - `observedCredentialConfidence[number]`: La confidenza complessiva della misura. Può essere specifico del fornitore, ma dovrebbe sempre essere ridimensionato a un valore compreso tra 0 e 1. Utilizzare i metadati per indicare come interpretare questo numero. Arvoo: intervallo[0.0, 1.0] (più alto è meglio).  - `observedCredentialCountry[string]`: Codice Paese secondo lo standard ISO3166 a 2 caratteri (https://www.iban.com/country-codes). Si noti che il codice internazionale di immatricolazione dei veicoli non dovrebbe essere usato per evitare ambiguità (https://en.wikipedia.org/wiki/International_vehicle_registration_code). Se non è stato possibile determinare il codice paese, impostare 'XX' come per questo attributo.  - `observedCredentialId[string]`: Identificatore specifico della credenziale osservata di riferimento. La credenziale è specificata da observedCredentialType e può essere un tag RFID, un numero di biglietto di una stazione di pagamento, un numero di targa, ecc. Nel caso di una targa, sono ammessi solo valori numerici alfa (senza spazi o trattini). Opzionalmente si può usare un ":" per indicare la posizione, ad esempio, del sigillo della città tedesca (https://www.europeanplates.com/information/german-city-codes.html).  - `observedCredentialType[string]`: Tipo di credenziale a cui fa riferimento l'osservazione. I valori ammessi sono specificati nell'APDS CredentialType. Enum:'barcode, bluetooth, eticket, hangtag, licensePlate, permit, qrCode, rfid, ticket, other'.  - `observedHeading[*]`: Indica la direzione di marcia dell'osservatore ed è specificata in gradi decimali, dove 0 <= 'heading' < 360, contando in senso orario rispetto al nord vero. Se il veicolo è fermo (cioè il valore dell'attributo 'speed' è '0'), il valore dell'attributo heading deve essere uguale a '-1'. (Codice ONU DD)  . Model: [https://schema.org/Number](https://schema.org/Number)- `observedLocation`:   	- `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)  
	- `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `location[*]`: Riferimento geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.    
- `observedLocationPDOP[number]`: Precisione della posizione GPS del veicolo osservato. È espressa come "Diluizione di precisione della posizione" (https: //en.wikipedia.org/wiki/Diluizione_di_precisione_(navigazione)). (Codice ONU "MTR").  - `observedMethod[string]`: Il metodo di osservazione registrato per questo elemento di osservazione, come definito da APDS (ObservationType). Enum:'anpr, gesso, visivo, scanner, rfTranspoder, altro'.  - `observedSpeed[*]`: Indica la grandezza della componente orizzontale della velocità corrente del veicolo osservato ed è specificata in chilometri all'ora. Se fornito, il valore dell'attributo velocità deve essere un numero reale non negativo.'-1' PUO' essere usato se la velocità è transitoriamente sconosciuta per qualche motivo. (Codice ONU KMH).  . Model: [https://schema.org/Number](https://schema.org/Number)- `observedVehicleColour[string]`: Il colore del veicolo osservato  - `observedVehicleMake[string]`: La marca del veicolo osservato  - `observedVehicleType[string]`: Tipo di veicolo dal punto di vista delle sue caratteristiche strutturali. È diverso dalla categoria del veicolo. Enum:'veicolo agricolo, qualsiasi veicolo, veicolo articolato, bicicletta, carrello portarifiuti, autobus, automobile, roulotte, autovettura o veicolo leggero, autovettura con roulotte, autovettura con rimorchio, carrello per le pulizie, veicolo da costruzione o manutenzione, quattro ruote motrici, veicolo a ruote alte, autocarro, minibus, ciclomotore, motocicletta, motociclo con auto laterale, motoscooter, macchina spazzatrice, autocisterna, veicolo a tre ruote, rimorchio, tram, veicolo a due ruote, carrello, furgone, veicolo senza convertitore catalitico, veicolo con roulotte, veicolo con rimorchio, con targhe pari, con targhe dispari, altro". I seguenti valori definiti da _VehicleTypeEnum_ e _VehicleTypeEnum2_, [DATEX 2 versione 2.3](http://d2docs.ndwcloud.nu/_static/umlmodel/v2.3/index.htm) ed estesi per altri usi  . Model: [https://schema.org/Text](https://schema.org/Text)- `observer[string]`: Il nome o l'identificazione del sistema di scansione che effettua l'osservazione registrata in questo elemento di osservazione.  - `observerCameras[array]`: La prima telecamera dell'elenco è quella che ha effettuato il miglior riconoscimento. Utilizzare le seguenti abbreviazioni per indicare il posizionamento della telecamera su un'automobile: RF (Right Front), RM (Right Middle), RB (Right Back), LF (Left Front), LM (Left Middle), LB (Left Back).  - `observerDescription[string]`: Descrizione a testo libero per i dettagli dell'osservazione o dell'osservatore. Può essere utilizzata, ad esempio, come nome amichevole di una specifica auto di scansione ANPR.  - `observerHeading[*]`: Indica la direzione di marcia dell'osservatore ed è specificata in gradi decimali, dove 0 <= 'heading' < 360, contando in senso orario rispetto al nord vero. Se il veicolo è fermo (cioè il valore dell'attributo 'speed' è '0'), il valore dell'attributo heading deve essere uguale a '-1'.  . Model: [https://schema.org/Number](https://schema.org/Number)- `observerLocation`:   	- `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)  
	- `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `location[*]`: Riferimento geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.    
- `observerLocationPDOP[number]`: Precisione della posizione GPS dell'osservatore, espressa come "diluizione della posizione di precisione" (https: //en.wikipedia.org/wiki/Diluizione_di_precisione_(navigazione))  - `observerSpeed[*]`: Indica la grandezza della componente orizzontale della velocità corrente dell'osservatore ed è specificata in chilometri all'ora. Se fornito, il valore dell'attributo speed deve essere un numero reale non negativo. Si può usare '-1' se la velocità è transitoriamente sconosciuta per qualche motivo.  . Model: [https://schema.org/Number](https://schema.org/Number)- `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `towardsObserver[number]`: 1: il veicolo osservato si muove in direzione della telecamera, 0: il veicolo osservato si allontana dalla telecamera, -1: Direzione del veicolo osservato non rilevata.  - `type[string]`: Tipo di entità NGSI. Deve essere APDSObservation  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Proprietà richieste  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Questo modello cattura l'insieme di dati di un'osservazione di un veicolo in un momento specifico e in un luogo particolare. È derivato dalla specifica APDS (Alliance for Parking DataStandard). Il metodo di osservazione comprende l'uso di telecamere ALPR, l'osservazione visiva, lo scanner o qualsiasi altro mezzo di osservazione.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Modello di dati descrizione delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
APDSObservation:    
  description: 'This entity models a particular observation of a set of ANPR camera. The Observation might be done with several ANPR cameras, but is limited to the observation of ONE vehicle. It implements the APDS data model https://www.allianceforparkingdatastandards.org/'    
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
    creator:    
      description: Id of current driver.    
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
    images:    
      description: 'Array of links to images. The array element contain the URLs of the images and additional info. As an alternative to the images URL, the image itself can be included in the binaryContent attribute.'    
      items:    
        items:    
          description: Every element in the array of images    
          properties:    
            URL:    
              description: Uri of the image    
              format: uri    
              type: string    
              x-ngsi:    
                type: Property    
            binaryContent:    
              description: Binary format of the image content    
              format: uuencoded    
              type: string    
              x-ngsi:    
                type: Property    
            camId:    
              description: Identifier of the camera. It can be specified by the camera position (also used in the 'camera' attribute)    
              type: string    
              x-ngsi:    
                type: Property    
            distance:    
              description: The distance in meters from the observer    
              type: number    
              x-ngsi:    
                type: Property    
                units: meters    
            expiryDateTime:    
              description: Timestamp until which the URL is valid    
              format: date-time    
              type: string    
              x-ngsi:    
                type: Property    
            imageContent:    
              description: It specifies the content of the image    
              type: string    
              x-ngsi:    
                type: Property    
          type: object    
          x-ngsi:    
            type: Property    
        type: array    
      type: array    
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
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    observationDateTime:    
      description: The timestamp the Observation was made (UTC). Mandatory if observationStartDateTime and observationEndDateTime are not used.    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    observationEndDateTime:    
      description: 'The date and time of the observation event ended(in UTC).(e.g.a car was observed to exit a delivery zone at 9: 33am). Mandatory if creationDateTime is not used.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    observationStartDateTime:    
      description: 'The date and time of the observation(in UTC)event started.(e.g.a car was observed to enter a delivery zone at 8: 01am). Mandatory if creationDateTime is not used.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    observedCredentialCharacterConfidence:    
      description: The confidence of individual character recognition. As with observedCredentialConfidence this is vendor specific. Use the metadata to indicate how the confidences can be interpreted.    
      items:    
        description: Every observation of the credential character confidence    
        maximum: 1    
        minimum: 0    
        type: number    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        type: Property    
    observedCredentialConfidence:    
      description: 'The overall confidence of the measurement. This can be vendor specific, but should always be rescaled to value between 0 en 1. Use the metadata to indicate how this number should be interpreted. Arvoo: range[0.0, 1.0](higher is better).'    
      maximum: 1    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    observedCredentialCountry:    
      description: 'Country Code following the 2 character ISO3166 standard (https://www.iban.com/country-codes). Note that the International vehicle registration code should not be used to avoid ambiguity (https://en.wikipedia.org/wiki/International_vehicle_registration_code). If the country-code could not be determined, set ''XX'' as for this attribute.'    
      type: string    
      x-ngsi:    
        type: Property    
    observedCredentialId:    
      description: 'Specific identifier to the referenced observed credential. The credential is specified by observedCredentialType and may be an RFID tag, ticket number from a paystation, license plate number, etc. In case of a licensePlate only alpha numerical values (no spaces or hyphens) are allowed. Optionally an '':'' can be used to indicate the position of e.g. the German City Seal (https://www.europeanplates.com/information/german-city-codes.html).'    
      type: string    
      x-ngsi:    
        type: Property    
    observedCredentialType:    
      description: 'Type of the credential referenced within  the observation. Allowed values are specified in the APDS CredentialType. Enum:''barcode, bluetooth, eticket, hangtag, licensePlate, permit, qrCode, rfid, ticket, other'''    
      enum:    
        - barcode    
        - bluetooth    
        - eticket    
        - hangtag    
        - licensePlate    
        - permit    
        - qrCode    
        - rfid    
        - ticket    
        - other    
      type: string    
      x-ngsi:    
        type: Property    
    observedHeading:    
      description: 'Denotes the direction of travel of the observer and is specified in decimal degrees, where 0 <= ''heading'' < 360, counting clockwise relative to the true north.If the vehicle is stationary(i.e. the value of the ''speed'' attribute is ''0''), then the value of the heading attribute must be equal to ''-1''. (UN code DD)'    
      oneOf:    
        - exclusiveMaximum: true    
          maximum: 360    
          minimum: 0    
          type: number    
        - enum:    
            - -1    
          type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Degrees    
    observedLocation:    
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
        areaServed:    
          description: The geographic area where a service or offered item is provided    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        location:    
          description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
          oneOf:    
            - bbox:    
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
            - bbox:    
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
            - bbox:    
                items:    
                  type: number    
                minItems: 4    
                type: array    
              coordinates:    
                items:    
                  items:    
                    items:    
                    minItems: 2    
                    type: array    
                  minItems: 4    
                  type: array    
                type: array    
              type:    
                enum:    
                  - Polygon    
                type: string    
            - bbox:    
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
            - bbox:    
                items:    
                  type: number    
                minItems: 4    
                type: array    
              coordinates:    
                items:    
                  items:    
                    items:    
                    minItems: 2    
                    type: array    
                  minItems: 2    
                  type: array    
                type: array    
              type:    
                enum:    
                  - MultiLineString    
                type: string    
            - bbox:    
                items:    
                  type: number    
                minItems: 4    
                type: array    
              coordinates:    
                items:    
                  items:    
                    items:    
                    minItems: 4    
                    type: array    
                  type: array    
                type: array    
              type:    
                enum:    
                  - MultiPolygon    
                type: string    
          x-ngsi:    
            type: GeoProperty    
      type: object    
    observedLocationPDOP:    
      description: 'Accuracy of GPS position of the observed vehicle. This is expressed as ''Position Dilution Of Precision''(https: //en.wikipedia.org/wiki/Dilution_of_precision_(navigation)). (UN code ''MTR''). '    
      type: number    
      x-ngsi:    
        type: Property    
        units: meters    
    observedMethod:    
      description: 'The method of observation recorded for this observation element as defined by APDS (ObservationType). Enum:''anpr, chalk, visual, scanner, rfTranspoder, other'''    
      enum:    
        - anpr    
        - chalk    
        - other    
        - rfTranspoder    
        - scanner    
        - visual    
      type: string    
      x-ngsi:    
        type: Property    
    observedSpeed:    
      description: 'Denotes the magnitude of the horizontal component of the observed vehicles current velocity and is specified in kilometers per hour. If provided, the value of the speed attribute must be a non - negative real number.''-1'' MAY be used if speed is transiently unknown for some reason. (UN Code KMH).'    
      oneOf:    
        - minimum: 0    
          type: number    
        - maximum: -1    
          minimum: -1    
          type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: km/h    
    observedVehicleColour:    
      description: The colour of the observed vehicle    
      type: string    
      x-ngsi:    
        type: Property    
    observedVehicleMake:    
      description: The make of the observed vehicle    
      type: string    
      x-ngsi:    
        type: Property    
    observedVehicleType:    
      description: 'Type of vehicle from the point of view of its structural characteristics. This is different than the vehicle category . Enum:''agriculturalVehicle, anyVehicle, articulatedVehicle, bicycle, binTrolley, bus, car, caravan, carOrLightVehicle, carWithCaravan, carWithTrailer, cleaningTrolley, constructionOrMaintenanceVehicle, fourWheelDrive, highSidedVehicle, lorry, minibus, moped, motorcycle, motorcycleWithSideCar, motorscooter, sweepingMachine, tanker, threeWheeledVehicle, trailer, tram, twoWheeledVehicle, trolley, van, vehicleWithoutCatalyticConverter, vehicleWithCaravan, vehicleWithTrailer, withEvenNumberedRegistrationPlates, withOddNumberedRegistrationPlates, other''. The following values defined by _VehicleTypeEnum_ and _VehicleTypeEnum2_, [DATEX 2 version 2.3](http://d2docs.ndwcloud.nu/_static/umlmodel/v2.3/index.htm) and extended for other uses'    
      enum:    
        - agriculturalVehicle    
        - ambulance    
        - anyVehicle    
        - articulatedVehicle    
        - autorickshaw    
        - bicycle    
        - binTrolley    
        - BRT mini busÂ·    
        - BRT bus    
        - bus    
        - car    
        - caravan    
        - carOrLightVehicle    
        - carWithCaravan    
        - carWithTrailer    
        - cleaningTrolley    
        - compactor    
        - constructionOrMaintenanceVehicle    
        - dumper    
        - e-moped    
        - e-scooter    
        - e-motorcycle    
        - fireTender    
        - fourWheelDrive    
        - highSidedVehicle    
        - hopper    
        - lorry    
        - minibus    
        - moped    
        - motorcycle    
        - motorcycleWithSideCar    
        - motorscooter    
        - policeVan    
        - publicMotor    
        - sweepingMachine    
        - tanker    
        - tempo    
        - threeWheeledVehicle    
        - tipper    
        - trailer    
        - tram    
        - trolley    
        - twoWheeledVehicle    
        - van    
        - vehicleWithoutCatalyticConverter    
        - vehicleWithCaravan    
        - vehicleWithTrailer    
        - withEvenNumberedRegistrationPlates    
        - withOddNumberedRegistrationPlates    
        - other    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    observer:    
      description: The name or identification of the scanning system making the observation recorded in this observation element.    
      type: string    
      x-ngsi:    
        type: Property    
    observerCameras:    
      description: 'Array of camera positions that detected the vehicle.The first camera in the list has the best recognition.Use the following abbreviations to indicate the camera positioning on a car: RF(Right Front), RM(Right Middle), RB(Right Back), LF(Left Front), LM(Left Middle), LB(Left Back).'    
      items:    
        description: Every camera position    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        type: Property    
    observerDescription:    
      description: Free-text description for details of the observation or observer. Can e.g.be used as a friendly name of a specific ANPR scan car.    
      type: string    
      x-ngsi:    
        type: Property    
    observerHeading:    
      description: 'Denotes the direction of travel of the observer and is specified in decimal degrees, where 0 <= ''heading'' < 360, counting clockwise relative to the true north. If the vehicle is stationary(i.e. the value of the ''speed'' attribute is ''0''), then the value of the heading attribute must be equal to ''-1'''    
      oneOf:    
        - exclusiveMaximum: true    
          maximum: 360    
          minimum: 0    
          type: number    
        - enum:    
            - -1    
          type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Degree.    
    observerLocation:    
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
        areaServed:    
          description: The geographic area where a service or offered item is provided    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        location:    
          description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
          oneOf:    
            - bbox:    
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
            - bbox:    
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
            - bbox:    
                items:    
                  type: number    
                minItems: 4    
                type: array    
              coordinates:    
                items:    
                  items:    
                    items:    
                    minItems: 2    
                    type: array    
                  minItems: 4    
                  type: array    
                type: array    
              type:    
                enum:    
                  - Polygon    
                type: string    
            - bbox:    
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
            - bbox:    
                items:    
                  type: number    
                minItems: 4    
                type: array    
              coordinates:    
                items:    
                  items:    
                    items:    
                    minItems: 2    
                    type: array    
                  minItems: 2    
                  type: array    
                type: array    
              type:    
                enum:    
                  - MultiLineString    
                type: string    
            - bbox:    
                items:    
                  type: number    
                minItems: 4    
                type: array    
              coordinates:    
                items:    
                  items:    
                    items:    
                    minItems: 4    
                    type: array    
                  type: array    
                type: array    
              type:    
                enum:    
                  - MultiPolygon    
                type: string    
          x-ngsi:    
            type: GeoProperty    
      type: object    
    observerLocationPDOP:    
      description: 'Accuracy of the GPS position of the observer, expressed as ''Position Dilution Of Precision''(https: //en.wikipedia.org/wiki/Dilution_of_precision_(navigation))'    
      type: number    
      x-ngsi:    
        type: Property    
        units: meters.    
    observerSpeed:    
      description: 'Denotes the magnitude of the horizontal component of the observer current velocity and is specified in kilometers per hour. If provided, the value of the speed attribute must be a non - negative real number. ''-1'' MAY be used if speed is transiently unknown for some reason'    
      oneOf:    
        - minimum: 0    
          type: number    
        - maximum: -1    
          minimum: -1    
          type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: 'KMH '    
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
    towardsObserver:    
      description: '1: Observed vehicle moves in direction of camera, 0: Observed vehicle moves away direction of camera, -1: Observed vehicle direction not detected.'    
      enum:    
        - -1    
        - 0    
        - 1    
      type: number    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be APDSObservation    
      enum:    
        - APDSObservation    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: https://www.allianceforparkingdatastandards.org/    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Transportation/blob/master/APDSObservation/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Transportation/APDSObservation/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Esempi di payload  
#### Valori-chiave APDSObservation NGSI-v2 Esempio  
Ecco un esempio di un'osservazione APDSO in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "uri:ngsi-ld:APDSObservation:Arvoo:ArvooSGIDxxxx",  
  "type": "APDSObservation",  
  "creator": "25399",  
  "images": [  
    [  
      {  
        "URL": "http://10.1.0.11:7400/getimage?sgid=8775639&amp;camid=lf&amp;imgreqtype=anpr"  
      },  
      {  
        "camId": "LF"  
      },  
      {  
        "imageContent": "ANPR"  
      }  
    ],  
    [  
      {  
        "URL": "http://10.1.0.11:7400/getimage?sgid=8775639&amp;camid=lf&amp;imgreqtype=overview"  
      },  
      {  
        "camId": "LF"  
      },  
      {  
        "imageContent": "Overview"  
      }  
    ],  
    [  
      {  
        "URL": "http://10.1.0.11:7400/getimage?sgid=8775639&amp;camid=lf&amp;imgreqtype=plate"  
      },  
      {  
        "camId": "LF"  
      },  
      {  
        "imageContent": "Plate"  
      }  
    ],  
    [  
      {  
        "URL": "http://10.1.0.11:7400/getimage?sgid=8775639&amp;camid=plf&amp;distance=-5.22"  
      },  
      {  
        "camId": "LF"  
      },  
      {  
        "imageContent": "Panorama"  
      },  
      {  
        "distance": -5.22  
      }  
    ]  
  ],  
  "observationDateTime": "2020-09-11T10:45:00.00Z",  
  "observedCredentialCharacterConfidence": [  
    0.944,  
    0.851,  
    0.876,  
    0.950,  
    0.932,  
    0.936,  
    0.901  
  ],  
  "observedCredentialConfidence": 0.851,  
  "observedCredentialCountry": "BE",  
  "observedCredentialId": "1ENC003",  
  "observedCredentialType": "licensePlate",  
  "observedHeading": 175,  
  "observedLocation": {  
    "coordinates": [  
      4.00412077,  
      51.00216632  
    ],  
    "type": "Point"  
  },  
  "observedLocationPDOP": 0.2959945752,  
  "observedMethod": "anpr",  
  "observedSpeed": -1,  
  "observer": "Arvoo",  
  "observerCameras": [  
    "LF,LB"  
  ],  
  "observerDescription": "Scangenius Auto-26",  
  "observerHeading": 175,  
  "observerLocation": {  
    "coordinates": [  
      4.412077,  
      51.216632  
    ],  
    "type": "Point"  
  },  
  "observerLocationPDOP": 0.2959945752,  
  "observerSpeed": 26  
}  
```  
</details>  
#### APDSObservation NGSI-v2 normalizzato Esempio  
Ecco un esempio di APDSObservation in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si usano le opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
	"id": "uri:ngsi-ld:APDSObservation:Arvoo:ArvooSGIDxxxx",  
	"type": "APDSObservation",  
	"observedMethod": {  
		"type": "Text",  
		"value": "anpr"  
	},  
	"observedCredentialType": {  
		"type": "Text",  
		"value": "license plate"  
	},  
	"observedCredentialId": {  
		"type": "Text",  
		"value": "1ENC003"  
	},  
	"observedCredentialCountry": {  
		"type": "Text",  
		"value": "BE"  
	},  
	"observedCredentialConfidence": {  
		"type": "Number",  
		"value": 0.851,  
		"metadata": {  
			"confidenceMethod": {  
				"type": "Text",  
				"value": "Arvoo. Higher is better."  
			}  
		}  
	},  
	"observedCredentialCharacterConfidence": {  
		"type": "array",  
		"value": [  
			0.944,  
			0.851,  
			0.876,  
			0.950,  
			0.932,  
			0.936,  
			0.901  
		],  
		"metadata": {  
			"confidenceMethod": {  
				"type": "Text",  
				"value": "Arvoo"  
			}  
		}  
	},  
	"observer": {  
		"type": "Text",  
		"value": "Arvoo",  
		"metadata": {}  
	},  
	"observerDescription": {  
		"type": "Text",  
		"value": "Scangenius Auto-26"  
	},  
	"creator": {  
		"type": "Text",  
		"value": "25399"  
	},  
	"observerCameras": {  
		"type": "Array",  
		"value": [  
			"LF,LB"  
		]  
	},  
	"observationDateTime": {  
		"type": "DateTime",  
		"value": "2020-09-11T10:45:00.00Z"  
	},  
	"observerLocation": {  
		"type": "geo:json",  
		"value": {  
			"type": "Point",  
			"coordinates": [  
				4.412077,  
				51.216632  
			]  
		},  
		"metadata": {  
			"timestamp": {  
				"type": "DateTime",  
				"value": "2020-09-11T10:45:00.00Z"  
			}  
		}  
	},  
	"observerLocationPDOP": {  
		"type": "Number",  
		"value": 0.2959945752,  
		"metadata": {  
			"UnitCode": {  
				"type": "Text",  
				"value": "MTR"  
			}  
		}  
	},  
	"observerHeading": {  
		"type": "Number",  
		"value": 175  
	},  
	"observerSpeed": {  
		"type": "Number",  
		"value": 26,  
		"metadata": {  
			"UnitCode": {  
				"type": "Text",  
				"value": "KMH"  
			}  
		}  
	},  
	"observedLocation": {  
		"type": "geo:json",  
		"value": {  
			"type": "Point",  
			"coordinates": [  
				4.00412077,  
				51.00216632  
			]  
		},  
		"metadata": {  
			"timestamp": {  
				"type": "DateTime",  
				"value": "2020-09-11T10:45:00.00Z"  
			}  
		}  
	},  
	"observedLocationPDOP": {  
		"type": "Number",  
		"value": 0.2959945752,  
		"metadata": {  
			"UnitCode": {  
				"type": "Text",  
				"value": "MTR"  
			}  
		}  
	},  
	"observedHeading": {  
		"type": "Number",  
		"value": 175  
	},  
	"observedSpeed": {  
		"type": "Number",  
		"value": -1  
	},  
	"images": {  
		"type": "array",  
		"value": [  
			{  
			  "URL": "http://localhost:4000/getimage?sgid=984133&camid=lf&imgreqtype=anpr",  
			  "expiryDateTime": "2023-11-25T11:13:42.133Z",  
			  "camId": "LF",  
			  "imageContent": "ANPR"  
			},  
			{  
			  "URL": "http://localhost:4000/getimage?sgid=984133&camid=lf&imgreqtype=overview",  
			  "expiryDateTime": "2023-11-25T11:13:42.133Z",  
			  "camId": "LF",  
			  "imageContent": "Overview"  
			},  
			{  
			  "URL": "http://localhost:4000/getimage?sgid=984133&camid=lf&imgreqtype=plate",  
			  "expiryDateTime": "2023-11-25T11:13:42.133Z",  
			  "camId": "LF",  
			  "imageContent": "Plate"  
			},  
			{  
			  "URL": "http://localhost:4000/getimage?sgid=984133&camid=plf&distance=-3.23",  
			  "expiryDateTime": "2023-11-25T11:13:42.133Z",  
			  "camId": "LF",  
			  "imageContent": "Panorama",  
			  "distance": -3.232  
			}  
		]  
	}  
}  
```  
</details>  
#### Valori chiave APDSObservation NGSI-LD Esempio  
Ecco un esempio di una APDSObservation in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "uri:ngsi-ld:APDSObservation:Arvoo:ArvooSGIDxxxx",  
    "type": "APDSObservation",  
    "creator": "25399",  
    "images": [  
        [  
            {  
                "URL": "http://10.1.0.11:7400/getimage?sgid=8775639&amp;camid=lf&amp;imgreqtype=anpr"  
            },  
            {  
                "camId": "LF"  
            },  
            {  
                "imageContent": "ANPR"  
            }  
        ],  
        [  
            {  
                "URL": "http://10.1.0.11:7400/getimage?sgid=8775639&amp;camid=lf&amp;imgreqtype=overview"  
            },  
            {  
                "camId": "LF"  
            },  
            {  
                "imageContent": "Overview"  
            }  
        ],  
        [  
            {  
                "URL": "http://10.1.0.11:7400/getimage?sgid=8775639&amp;camid=lf&amp;imgreqtype=plate"  
            },  
            {  
                "camId": "LF"  
            },  
            {  
                "imageContent": "Plate"  
            }  
        ],  
        [  
            {  
                "URL": "http://10.1.0.11:7400/getimage?sgid=8775639&amp;camid=plf&amp;distance=-5.22"  
            },  
            {  
                "camId": "LF"  
            },  
            {  
                "imageContent": "Panorama"  
            },  
            {  
                "distance": -5.22  
            }  
        ]  
    ],  
    "observationDateTime": "2020-09-11T10:45:00.00Z",  
    "observedCredentialCharacterConfidence": [  
        0.944,  
        0.851,  
        0.876,  
        0.950,  
        0.932,  
        0.936,  
        0.901  
    ],  
    "observedCredentialConfidence": 851,  
    "observedCredentialCountry": "BE",  
    "observedCredentialId": "1ENC003",  
    "observedCredentialType": "license plate",  
    "observedHeading": 175,  
    "observedLocation": {  
        "coordinates": [  
            4.00412077,  
            51.00216632  
        ],  
        "type": "Point"  
    },  
    "observedLocationPDOP": 0.2959945752,  
    "observedMethod": "anpr",  
    "observedSpeed": -1,  
    "observer": "Arvoo",  
    "observerCameras": [  
        "LF,LB"  
    ],  
    "observerDescription": "Scangenius Auto-26",  
    "observerHeading": 175,  
    "observerLocation": {  
        "coordinates": [  
            4.412077,  
            51.216632  
        ],  
        "type": "Point"  
    },  
    "observerLocationPDOP": 0.2959945752,  
    "observerSpeed": 26,  
    "@context": [  
        ""  
    ]  
}  
```  
</details>  
#### APDSObservation NGSI-LD normalizzato Esempio  
Ecco un esempio di APDSObservation in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si usano opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
	"id": "uri:ngsi-ld:APDSObservation:Arvoo:ArvooSGIDxxxx",  
	"type": "APDSObservation",  
	"observedMethod": {  
		"type": "Property",  
		"value": "anpr"  
	},  
	"observedCredentialType": {  
		"type": "Property",  
		"value": "license plate"  
	},  
	"observedCredentialId": {  
		"type": "Property",  
		"value": "1ENC003"  
	},  
	"observedCredentialCountry": {  
		"type": "Property",  
		"value": "BE"  
	},  
	"observedCredentialConfidence": {  
		"type": "Property",  
		"value": 0.851  
	},  
	"observedCredentialCharacterConfidence": {  
		"type": "Property",  
		"value": [  
			0.944,  
			0.851,  
			0.876,  
			0.950,  
			0.932,  
			0.936,  
			0.901  
		]  
	},  
	"observer": {  
		"type": "Property",  
		"value": "Arvoo"  
	},  
	"observerDescription": {  
		"type": "Property",  
		"value": "Scangenius Auto-26"  
	},  
	"creator": {  
		"type": "Property",  
		"value": "25399"  
	},  
	"observerCameras": {  
		"type": "Property",  
		"value": [  
			"LF,LB"  
		]  
	},  
	"observationDateTime": {  
		"type": "Property",  
		"value": {  
			"@type": "DateTime",  
			"@value": "2020-09-11T10:45:00.00Z"  
		}  
	},  
	"observerLocation": {  
		"type": "GeoProperty",  
		"value": {  
			"type": "Point",  
			"coordinates": [  
				4.412077,  
				51.216632  
			]  
		}  
	},  
	"observerLocationPDOP": {  
		"type": "Property",  
		"value": 0.2959945752  
	},  
	"observerHeading": {  
		"type": "Property",  
		"value": 175  
	},  
	"observerSpeed": {  
		"type": "Property",  
		"value": 26  
	},  
	"observedLocation": {  
		"type": "GeoProperty",  
		"value": {  
			"type": "Point",  
			"coordinates": [  
				4.00412077,  
				51.00216632  
			]  
		}  
	},  
	"observedLocationPDOP": {  
		"type": "Property",  
		"value": 0.2959945752  
	},  
	"observedHeading": {  
		"type": "Property",  
		"value": 175  
	},  
	"observedSpeed": {  
		"type": "Property",  
		"value": -1  
	},  
	"images": {  
		"type": "Property",  
		"value": [  
			{  
			  "URL": "http://localhost:4000/getimage?sgid=984133&camid=lf&imgreqtype=anpr",  
			  "expiryDateTime": "2023-11-25T11:13:42.133Z",  
			  "camId": "LF",  
			  "imageContent": "ANPR"  
			},  
			{  
			  "URL": "http://localhost:4000/getimage?sgid=984133&camid=lf&imgreqtype=overview",  
			  "expiryDateTime": "2023-11-25T11:13:42.133Z",  
			  "camId": "LF",  
			  "imageContent": "Overview"  
			},  
			{  
			  "URL": "http://localhost:4000/getimage?sgid=984133&camid=lf&imgreqtype=plate",  
			  "expiryDateTime": "2023-11-25T11:13:42.133Z",  
			  "camId": "LF",  
			  "imageContent": "Plate"  
			},  
			{  
			  "URL": "http://localhost:4000/getimage?sgid=984133&camid=plf&distance=-3.23",  
			  "expiryDateTime": "2023-11-25T11:13:42.133Z",  
			  "camId": "LF",  
			  "imageContent": "Panorama",  
			  "distance": -3.232  
			}  
		]  
	},  
	 "@context": [  
        ""  
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
