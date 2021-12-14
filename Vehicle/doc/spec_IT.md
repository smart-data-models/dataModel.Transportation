Entità: Veicolo  
===============  
[Licenza aperta](https://github.com/smart-data-models//dataModel.Transportation/blob/master/Vehicle/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descrizione globale: **Questa entità modella un particolare modello di veicolo, includendo tutte le proprietà che sono comuni a più istanze di veicolo appartenenti a tale modello.  

## Elenco delle proprietà  

- `address`: L'indirizzo postale  - `alternateName`: Un nome alternativo per questa voce  - `annotations`: Annotazioni sull'elemento  - `areaServed`: L'area geografica in cui viene fornito un servizio o un articolo offerto  - `bearing`: Fornisce l'angolo GPS del veicolo misurato in senso orario dal Nord vero. Come il campo "bearing" del messaggio in tempo reale GTFS-Position(https://developers.google.com/transit/gtfs-realtime/reference#message-position)  - `cargoWeight`: Peso attuale del carico del veicolo  - `category`: Categoria(i) di veicolo da un punto di vista esterno. Questo è diverso dal tipo di veicolo (auto, camion, ecc.) rappresentato dalla proprietà `vehicleType`. Enum:'municipalServices, nonTracked, private, public, specialUsage, tracked'. I veicoli tracciati sono quei veicoli la cui posizione è permanentemente tracciata da un sistema remoto. O qualsiasi altro necessario per un'applicazione Essi incorporano un ricevitore GPS insieme a una connessione di rete per aggiornare periodicamente una posizione riportata (posizione, velocità, direzione ...).  - `color`: Il colore del prodotto  - `currentTripCount`: Il conteggio attuale dei viaggi effettuati dal veicolo corrispondente a questa osservazione in un dato giorno di funzionamento.  - `dataProvider`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `dateCreated`: Timestamp di creazione dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `dateFirstUsed`: Timestamp che denota quando il veicolo è stato usato per la prima volta  - `dateModified`: Timestamp dell'ultima modifica dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `dateVehicleFirstRegistered`: La data della prima registrazione del veicolo presso le rispettive autorità pubbliche  - `description`: Una descrizione di questo articolo  - `deviceBatteryStatus`: Fornisce lo stato di carica della batteria del dispositivo di segnalazione. Enum:'connected, disconnected'.  - `deviceSimNumber`: Fornisce il numero di SIM del dispositivo nel veicolo.  - `emergencyVehicleType`: Tipo di veicolo di emergenza corrispondente a questa osservazione. Enum:'policeCar, policeMotorcycle, policeVan, policeSWAT, fireEngine, waterTender, airAmbulance, ambulanza, motorcycleAmbulance, rescueVehicle, hazardousMaterialsApparatus, towTruck  - `feature`: Caratteristica(e) incorporata(e) dal veicolo. Enum:' abs, airbag, alarm, backCamera, disabledRamp, gps, internetConnection, overspeed, proximitySensor, wifi'. O qualsiasi altro necessario all'applicazione. Per rappresentare istanze multiple di una caratteristica si può usare la seguente sintassi: `<caratteristica>,<occorrenze>`. Per esempio, un'auto con 4 airbag sarà rappresentata da `airbag,4`.  - `fleetVehicleId`: L'identificatore del veicolo nel contesto della flotta di veicoli a cui appartiene  - `fuelEfficiency`: La distanza percorsa per unità di carburante utilizzato, comunemente in chilometri per litro (km/L).  - `fuelFilled`: Quantità di carburante riempito in litri al veicolo corrispondente a questa osservazione.  - `fuelType`: Il tipo di carburante adatto al motore o ai motori del veicolo corrispondente a questa osservazione.  - `heading`: Indica la direzione di marcia del veicolo ed è specificata in gradi decimali, dove 0 <= `heading` < 360, contando in senso orario rispetto al vero nord. Se il veicolo è fermo (cioè il valore dell'attributo `speed` è `0`), allora il valore dell'attributo heading deve essere uguale a `-1`  - `id`: Identificatore unico dell'entità  - `ignitionStatus`: Dà lo stato di accensione del veicolo. Vero significa acceso  - `image`: Un'immagine dell'oggetto  - `license_plate`: Fornisce il numero di targa del veicolo. SameAs: license_plate field from GTFS Realtime message-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)'  - `location`: Riferimento Geojson all'elemento. Può essere Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `mileageFromOdometer`: La distanza totale percorsa dal veicolo in questione dalla sua produzione iniziale, letta dal suo contachilometri  - `municipalityInfo`: Informazioni del comune corrispondenti a questa osservazione.  - `name`: Il nome di questo articolo.  - `observationDateTime`: Ultima ora di osservazione riportata  - `owner`: Una lista contenente una sequenza di caratteri codificata in JSON che si riferisce agli ID unici dei proprietari  - `previousLocation`: Riferimento Geojson all'elemento. Può essere Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `purchaseDate`: La data in cui l'oggetto, ad esempio il veicolo, è stato acquistato dall'attuale proprietario  - `refVehicleModel`: Riferimento a un modello di veicolo  - `reportId`: Id unico assegnato per il problema o il rapporto o il feedback o la transazione corrispondente a questa osservazione.  - `seeAlso`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `serviceOnDuty`: Natura del servizio fornito dal veicolo di emergenza corrispondente a questa osservazione. True (vero) indica che il veicolo d'emergenza corrispondente a questa osservazione sta assistendo/assistendo a una chiamata d'emergenza ed è False (falso) altrimenti.  - `serviceProvided`: Servizio(i) che il veicolo è in grado di fornire o a cui è assegnato. Enum:'auxiliaryServices, cargoTransport, construction, fairground, garbageCollection, goodsSelling, maintenance, parksAndGardens, roadSignalling, specialTransport, streetCleaning, streetLighting, urbanTransit, wasteContainerCleaning'. O qualsiasi altro valore necessario per un'applicazione specifica.  - `serviceStatus`: Stato del veicolo (dal punto di vista del servizio fornito, quindi non potrebbe applicarsi ai veicoli privati). `parked` : Il veicolo è parcheggiato e non fornisce alcun servizio al momento. `onRoute` : Il veicolo sta svolgendo una missione. Un modificatore separato da virgole può essere aggiunto per indicare quale missione sta attualmente consegnando il veicolo. Per esempio `onRoute,garbageCollection` può essere usato per indicare che il veicolo è in rotta e in una missione di raccolta rifiuti. 'broken' : Il veicolo sta subendo un guasto temporaneo. `outOfService` : Il veicolo è sulla strada ma non sta svolgendo alcuna missione, probabilmente sta andando al suo parcheggio. Enum:'broken, onRoute, outOfService, parked'  - `source`: Una sequenza di caratteri che dà la fonte originale dei dati dell'entità come URL. Si raccomanda di essere il nome di dominio completamente qualificato del fornitore di origine, o l'URL dell'oggetto di origine.  - `speed`: Indica la grandezza della componente orizzontale della velocità attuale del veicolo ed è specificata in chilometri all'ora. Se fornito, il valore dell'attributo speed deve essere un numero reale non negativo. `-1` PUÒ essere usato se la velocità è transitoriamente sconosciuta per qualche motivo  - `tripNetWeightCollected`: Il peso netto raccolto dal veicolo corrispondente a questa osservazione alla fine del viaggio.  - `type`: Tipo di entità NGSI. Deve essere Veicolo  - `vehicleAltitude`: Dà l'altitudine attuale del veicolo usando il GPS  - `vehicleConfiguration`: Un breve testo che indichi la configurazione del veicolo, ad esempio "5dr hatchback ST 2.5 MT 225 hp" o "limited edition".  - `vehicleIdentificationNumber`: Il numero di identificazione del veicolo (VIN) è un numero di serie unico utilizzato dall'industria automobilistica per identificare i singoli veicoli a motore  - `vehiclePlateIdentifier`:  Un identificatore o un codice visualizzato su una targa di immatricolazione del veicolo attaccata al veicolo usato per scopi di identificazione ufficiale. L'identificatore di registrazione è numerico o alfanumerico ed è unico all'interno della regione dell'autorità emittente. Riferimenti normativi: DATEXII `vehicleRegistrationPlateIdentifier`.  - `vehicleRunningStatus`: Fornisce lo stato di carica della batteria del dispositivo di segnalazione. Enum:'running, waiting, stopped'.  - `vehicleSpecialUsage`: Indica se il veicolo è stato usato per scopi speciali, come il noleggio commerciale, la scuola guida o come taxi. La legislazione di molti paesi richiede che queste informazioni siano rivelate quando si offre un'auto in vendita. Enum:'ambulanza, vigili del fuoco, militare, polizia, trasporto scolastico, taxi, gestione rifiuti'.  - `vehicleTrackerDevice`: Stato di installazione del dispositivo GPS o del dispositivo di localizzazione montato sul veicolo corrispondente a questa osservazione.  - `vehicleType`: Tipo di veicolo dal punto di vista delle sue caratteristiche strutturali. Questo è diverso dalla categoria del veicolo. Enum:'agriculturalVehicle, anyVehicle, articulatedVehicle, bicycle, binTrolley, bus, car, caravan, carOrLightVehicle, carWithCaravan, carWithTrailer, cleaningTrolley, constructionOrMaintenanceVehicle, fourWheelDrive, highSidedVehicle, lorry, minibus, moped, motorcycle, motorcycleWithSideCar, motorscooter, sweepingMachine, tanker, threeWheeledVehicle, trailer, tram, twoWheeledVehicle, trolley, van, vehicleWithoutCatalyticConverter, vehicleWithCaravan, vehicleWithTrailer, withEvenNumberedRegistrationPlates, withOddNumberedRegistrationPlates, other". I seguenti valori definiti da _VehicleTypeEnum_ e _VehicleTypeEnum2_, [DATEX 2 versione 2.3](http://d2docs.ndwcloud.nu/_static/umlmodel/v2.3/index.htm) ed estesi per altri usi  - `wardId`: ID del reparto dell'entità corrispondente a questa osservazione.  - `wardName`: Nome del reparto dell'entità corrispondente a questa osservazione.  - `zoneName`: Nome della zona dell'entità corrispondente a questa osservazione    
Proprietà richieste  
- `category`  - `id`  - `location`  - `type`  - `vehicleType`  ## Descrizione del modello di dati delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Vehicle:    
  description: 'This entity models a particular vehicle model, including all properties which are common to multiple vehicle instances belonging to such model.'    
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
    bearing:    
      description: "Gives the vehicle GPS angle measured in a clockwise direction from the True North. SameAs 'bearing' field from GTFS Realtime message-Position(https://developers.google.com/transit/gtfs-realtime/reference#message-position)"    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    cargoWeight:    
      description: 'Current weight of the vehicle''s cargo'    
      exclusiveMinimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Kilograms    
    category:    
      description: 'Vehicle category(ies) from an external point of view. This is different than the vehicle type (car, lorry, etc.) represented by the `vehicleType` property. Enum:''municipalServices, nonTracked, private, public, specialUsage, tracked''. Tracked vehicles are those vehicles which position is permanently tracked by a remote system. Or any other needed by an application They incorporate a GPS receiver together with a network connection to periodically update a reported position (location, speed, heading ...).'    
      items:    
        enum:    
          - municipalServices    
          - nonTracked    
          - private    
          - public    
          - specialUsage    
          - tracked    
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
    currentTripCount:    
      description: 'The current count of trips made by the vehicle corresponding to this observation on the given day of operation.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
    dateFirstUsed:    
      description: 'Timestamp which denotes when the vehicle was first used'    
      format: date    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime.    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateVehicleFirstRegistered:    
      description: 'The date of the first registration of the vehicle with the respective public authorities'    
      format: date    
      type: string    
      x-ngsi:    
        model: https://schema.org/dateVehicleFirstRegistered.    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    deviceBatteryStatus:    
      description: 'Gives the Battery charging status of the reporting device. Enum:''connected, disconnected''.'    
      enum:    
        - connected    
        - disconnected    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    deviceSimNumber:    
      description: 'Gives the SIM number of the device in the vehicle.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    emergencyVehicleType:    
      description: 'Type of emergency vehicle corresponding to this observation. Enum:''policeCar, policeMotorcycle, policeVan, policeSWAT, fireEngine, waterTender, airAmbulance, ambulance, motorcycleAmbulance, rescueVehicle, hazardousMaterialsApparatus, towTruck'    
      enum:    
        - policeCar    
        - policeMotorcycle    
        - policeVan    
        - policeSWAT    
        - fireEngine    
        - waterTender    
        - airAmbulance    
        - ambulance    
        - motorcycleAmbulance    
        - rescueVehicle    
        - hazardousMaterialsApparatus    
        - towTruck    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    feature:    
      description: 'Feature(s) incorporated by the vehicle. Enum:'' abs, airbag, alarm, backCamera, disabledRamp, gps, internetConnection, overspeed, proximitySensor, wifi''. Or any other needed by the application. In order to represent multiple instances of a feature it can be used the following syntax: `<feature>,<occurences>`. For example, a car with 4 airbags will be represented by `airbag,4`.'    
      items:    
        enum:    
          - abs    
          - airbag    
          - alarm    
          - backCamera    
          - disabledRamp    
          - gps    
          - internetConnection    
          - overspeed    
          - proximitySensor    
          - wifi    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    fleetVehicleId:    
      description: 'The identifier of the vehicle in the context of the fleet of vehicles to which it belongs'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text.    
        type: Property    
    fuelEfficiency:    
      description: 'The distance traveled per unit of fuel used, commonly in kilometers per liter (km/L).'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fuelFilled:    
      description: 'Amount of fuel filled in liters to the vehicle corresponding to this observation.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fuelType:    
      description: 'The type of fuel suitable for the engine or engines of the vehicle corresponding to this observation.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    heading:    
      description: 'Denotes the direction of travel of the vehicle and is specified in decimal degrees, where 0 <= `heading` < 360, counting clockwise relative to the true north. If the vehicle is stationary (i.e. the value of the `speed` attribute is `0`), then the value of the heading attribute must be equal to `-1`'    
      oneOf:    
        - maximum: 360    
          minimum: 0    
          type: number    
        - const: -1    
          type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Degree    
    id:    
      anyOf: &vehicle_-_properties_-_owner_-_items_-_anyof    
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
    ignitionStatus:    
      description: 'Gives the ignition status of the vehicle. True means ignited'    
      type: boolean    
      x-ngsi:    
        model: https://schema.org/Boolean    
        type: Property    
    image:    
      description: 'An image of the item'    
      format: uri    
      type: string    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Property    
    license_plate:    
      description: "Gives the License Plate number of the vehicle. SameAs: license_plate field from GTFS Realtime message-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)'"    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf: &vehicle_-_properties_-_previouslocation_-_oneof    
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
    mileageFromOdometer:    
      description: 'The total distance travelled by the particular vehicle since its initial production, as read from its odometer'    
      type: number    
      x-ngsi:    
        model: https://schema.org/mileageFromOdometer.    
        type: Property    
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
    observationDateTime:    
      description: 'Last reported time of observation'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *vehicle_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    previousLocation:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf: *vehicle_-_properties_-_previouslocation_-_oneof    
      x-ngsi:    
        type: Geoproperty    
    purchaseDate:    
      description: 'The date the item e.g. vehicle was purchased by the current owner'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/purchaseDate.    
        type: Property    
    refVehicleModel:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Reference to a VehicleModel'    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Relationship    
    reportId:    
      description: 'Unique Id assigned for the issue or report or feedback or transaction corresponding to this observation.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
    serviceOnDuty:    
      description: 'Nature of service provided by emergency vehicle corresponding to this observation. True indicates the emergency vehicle corresponding to this observation is attending to/ servicing to an emergency call of duty and is False otherwise.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Boolean    
        type: Property    
    serviceProvided:    
      description: 'Service(s) the vehicle is capable of providing or it is assigned to. Enum:''auxiliaryServices, cargoTransport, construction, fairground, garbageCollection, goodsSelling, maintenance, parksAndGardens, roadSignalling, specialTransport, streetCleaning, streetLighting, urbanTransit, wasteContainerCleaning''. Or any other value needed by an specific application.'    
      items:    
        enum:    
          - auxiliaryServices    
          - cargoTransport    
          - construction    
          - fairground    
          - garbageCollection    
          - goodsSelling    
          - maintenance    
          - parksAndGardens    
          - roadSignalling    
          - specialTransport    
          - streetCleaning    
          - streetLighting    
          - urbanTransit    
          - wasteContainerCleaning    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    serviceStatus:    
      description: 'Vehicle status (from the point of view of the service provided, so it could not apply to private vehicles). `parked` : Vehicle is parked and not providing any service at the moment. `onRoute` : Vehicle is performing a mission. A comma-separated modifier(s) can be added to indicate what mission is currently delivering the vehicle. For instance `onRoute,garbageCollection` can be used to denote that the vehicle is on route and in a garbage collection mission. ''broken'' : Vehicle is suffering a temporary breakdown. `outOfService` : Vehicle is on the road but not performing any mission, probably going to its parking area. Enum:''broken, onRoute, outOfService, parked'''    
      enum:    
        - broken    
        - onRoute    
        - outOfService    
        - parked    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    speed:    
      description: 'Denotes the magnitude of the horizontal component of the vehicle''s current velocity and is specified in Kilometers per Hour. If provided, the value of the speed attribute must be a non-negative real number. `-1` MAY be used if speed is transiently unknown for some reason'    
      oneOf:    
        - minimum: 0    
          type: number    
        - maximum: -1    
          minimum: -1    
          type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Km/h    
    tripNetWeightCollected:    
      description: 'The net weight collected by the vehicle corresponding to this observation at the end of the trip.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: 'NGSI Entity type. It has to be Vehicle'    
      enum:    
        - Vehicle    
      type: string    
      x-ngsi:    
        type: Property    
    vehicleAltitude:    
      description: 'Gives the current altitude of the vehicle using GPS'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    vehicleConfiguration:    
      description: 'A short text indicating the configuration of the vehicle, e.g. ''5dr hatchback ST 2.5 MT 225 hp'' or ''limited edition'''    
      type: string    
      x-ngsi:    
        model: https://schema.org/vehicleConfiguration.    
        type: Property    
    vehicleIdentificationNumber:    
      description: 'The Vehicle Identification Number (VIN) is a unique serial number used by the automotive industry to identify individual motor vehicles'    
      type: string    
      x-ngsi:    
        model: https://schema.org/vehicleIdentificationNumber.    
        type: Property    
    vehiclePlateIdentifier:    
      description: ' An identifier or code displayed on a vehicle registration plate attached to the vehicle used for official identification purposes. The registration identifier is numeric or alphanumeric and is unique within the issuing authority''s region. Normative References: DATEXII `vehicleRegistrationPlateIdentifier`'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    vehicleRunningStatus:    
      description: 'Gives the Battery charging status of the reporting device. Enum:''running, waiting, stopped''.'    
      enum:    
        - running    
        - stopped    
        - waiting    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    vehicleSpecialUsage:    
      description: 'Indicates whether the vehicle is been used for special purposes, like commercial rental, driving school, or as a taxi. The legislation in many countries requires this information to be revealed when offering a car for sale. Enum:''ambulance, fireBrigade, military, police, schoolTransportation, taxi, trashManagement'''    
      enum:    
        - ambulance    
        - fireBrigade    
        - military    
        - police    
        - schoolTransportation    
        - taxi    
        - trashManagement    
      type: string    
      x-ngsi:    
        model: https://schema.org/vehicleSpecialUsage    
        type: Property    
    vehicleTrackerDevice:    
      description: 'Installation status of the GPS device or the tracking device fitted to the vehicle corresponding to this observation.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    vehicleType:    
      description: 'Type of vehicle from the point of view of its structural characteristics. This is different than the vehicle category . Enum:''agriculturalVehicle, anyVehicle, articulatedVehicle, bicycle, binTrolley, bus, car, caravan, carOrLightVehicle, carWithCaravan, carWithTrailer, cleaningTrolley, constructionOrMaintenanceVehicle, fourWheelDrive, highSidedVehicle, lorry, minibus, moped, motorcycle, motorcycleWithSideCar, motorscooter, sweepingMachine, tanker, threeWheeledVehicle, trailer, tram, twoWheeledVehicle, trolley, van, vehicleWithoutCatalyticConverter, vehicleWithCaravan, vehicleWithTrailer, withEvenNumberedRegistrationPlates, withOddNumberedRegistrationPlates, other''. The following values defined by _VehicleTypeEnum_ and _VehicleTypeEnum2_, [DATEX 2 version 2.3](http://d2docs.ndwcloud.nu/_static/umlmodel/v2.3/index.htm) and extended for other uses'    
      enum:    
        - agriculturalVehicle    
        - ambulance    
        - anyVehicle    
        - articulatedVehicle    
        - autorickshaw    
        - bicycle    
        - binTrolley    
        - 'BRT mini bus·'    
        - 'BRT bus'    
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
    wardId:    
      description: 'Ward ID of the entity corresponding to this observation.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    wardName:    
      description: 'Ward name of the entity corresponding to this observation.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    zoneName:    
      description: 'Zone name of the entity corresponding to this observation'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
  required:    
    - id    
    - type    
    - vehicleType    
    - category    
    - location    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Transportation/blob/master/Vehicle/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Transportation/Vehicle/schema.json    
  x-model-tags: IUDX    
  x-version: 0.2.0    
```  
</details>    
## Esempio di payloads  
#### Veicolo NGSI-v2 valori chiave Esempio  
Ecco un esempio di un veicolo in formato JSON-LD come key-values. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "id": "vehicle:WasteManagement:1",  
  "type": "Vehicle",  
  "vehicleType": "lorry",  
  "category": [  
    "municipalServices"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -3.164485591715449,  
      40.62785133667262  
    ]  
  },  
  "name": "C Recogida 1",  
  "speed": 50,  
  "cargoWeight": 314,  
  "serviceStatus": "onRoute",  
  "serviceProvided": [  
    "garbageCollection",  
    "wasteContainerCleaning"  
  ],  
  "areaServed": "Centro",  
  "refVehicleModel": "vehiclemodel:econic",  
  "vehiclePlateIdentifier": "3456ABC",  
  "bearing": 43,  
  "fuelEfficiency": 13,  
  "fuelType": "Petrol",  
  "fuelFilled": 6,  
  "tripNetWeightCollected": 12,  
  "vehicleTrackerDevice": "Installed",  
  "wardId": "4",  
  "license_plate": "KA052134",  
  "currentTripCount": 1,  
  "reportId": "21645",  
  "zoneName": "South Zone",  
  "vehicleAltitude": 600,  
  "deviceSimNumber": "9942142573",  
  "wardName": "Kempegowda Ward",  
  "deviceBatteryStatus": "Connected",  
  "ignitionStatus": true,  
  "vehicleRunningStatus": "running",  
  "observationDateTime": "2021-03-11T15:51:02+05:30",  
  "serviceOnDuty": false,  
  "emergencyVehicleType": "ambulance",  
  "municipalityInfo": {  
    "district": "Bangalore Urban",  
    "ulbName": "BMC",  
    "cityId": "23",  
    "wardId": "23",  
    "stateName": "Karnataka",  
    "cityName": "Bangalore",  
    "zoneName": "South",  
    "wardName": "Bangalore Urban",  
    "zoneId": "2",  
    "wardNum": 4  
  }  
}  
```  
#### Veicolo NGSI-v2 normalizzato Esempio  
Ecco un esempio di un veicolo in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "id": "vehicle:WasteManagement:1",  
  "type": "Vehicle",  
  "category": {  
    "type": "array",  
    "value": [  
      "municipalServices"  
    ]  
  },  
  "vehicleType": {  
    "type": "Text",  
    "value": "lorry"  
  },  
  "name": {  
    "type": "Text",  
    "value": "C Recogida 1"  
  },  
  "vehiclePlateIdentifier": {  
    "type": "Text",  
    "value": "3456ABC"  
  },  
  "refVehicleModel": {  
    "type": "Relationship",  
    "value": "vehiclemodel:econic"  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -3.164485591715449,  
        40.62785133667262  
      ]  
    },  
    "metadata": {  
      "timestamp": {  
        "type": "DateTime",  
        "value": "2018-09-27T12:00:00"  
      }  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Centro"  
  },  
  "serviceStatus": {  
    "type": "Text",  
    "value": "onRoute"  
  },  
  "cargoWeight": {  
    "type": "Number",  
    "value": 314  
  },  
  "speed": {  
    "type": "Number",  
    "value": 50,  
    "metadata": {  
      "timestamp": {  
        "type": "DateTime",  
        "value": "2018-09-27T12:00:00"  
      }  
    }  
  },  
  "serviceProvided": {  
    "type": "array",  
    "value": [  
      "gargabeCollection",  
      "wasteContainerCleaning"  
    ]  
  },  
  "bearing": {  
    "type": "Number",  
    "value": 43  
  },  
  "fuelEfficiency": {  
    "type": "Number",  
    "value": 13  
  },  
  "fuelType": {  
    "type": "Text",  
    "value": "Petrol"  
  },  
  "fuelFilled": {  
    "type": "Number",  
    "value": 6  
  },  
  "tripNetWeightCollected": {  
    "type": "Number",  
    "value": 12  
  },  
  "vehicleTrackerDevice": {  
    "type": "Text",  
    "value": "Installed"  
  },  
  "wardId": {  
    "type": "Text",  
    "value": "4"  
  },  
  "license_plate": {  
    "type": "Text",  
    "value": "KA052134"  
  },  
  "currentTripCount": {  
    "type": "Number",  
    "value": 1  
  },  
  "reportId": {  
    "type": "Text",  
    "value": "21645"  
  },  
  "zoneName": {  
    "type": "Text",  
    "value": "South Zone"  
  },  
  "vehicleAltitude": {  
    "type": "Number",  
    "value": 600  
  },  
  "deviceSimNumber": {  
    "type": "Text",  
    "value": "9942142573"  
  },  
  "wardName": {  
    "type": "Text",  
    "value": "Kempegowda Ward"  
  },  
  "deviceBatteryStatus": {  
    "type": "Text",  
    "value": "Connected"  
  },  
  "ignitionStatus": {  
    "type": "Boolean",  
    "value": true  
  },  
  "vehicleRunningStatus": {  
    "type": "Text",  
    "value": "running"  
  },  
  "observationDateTime": {  
    "type": "DateTime",  
    "value": "2021-03-11T15:51:02+05:30"  
  },  
  "serviceOnDuty": {  
    "type": "Boolean",  
    "value": false  
  },  
  "emergencyVehicleType": {  
    "type": "Text",  
    "value": "ambulance"  
  },  
  "municipalityInfo": {  
    "type": "StructuredValue",  
    "value": {  
      "district": "Bangalore Urban",  
      "ulbName": "BMC",  
      "cityId": "23",  
      "wardId": "23",  
      "stateName": "Karnataka",  
      "cityName": "Bangalore",  
      "zoneName": "South",  
      "wardName": "Bangalore Urban",  
      "zoneId": "2",  
      "wardNum": 4  
    }  
  }  
}  
```  
#### Veicolo NGSI-LD valori-chiave Esempio  
Ecco un esempio di un veicolo in formato JSON-LD come key-values. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "id": "urn:ngsi-ld:Vehicle:vehicle:WasteManagement:1",  
  "type": "Vehicle",  
  "areaServed": "Centro",  
  "cargoWeight": 314,  
  "category": [  
    "municipalServices"  
  ],  
  "location": {  
    "coordinates": [  
      -3.164485591715449,  
      40.62785133667262  
    ],  
    "type": "Point"  
  },  
  "name": "C Recogida 1",  
  "refVehicleModel": "urn:ngsi-ld:VehicleModel:vehiclemodel:econic",  
  "serviceProvided": [  
    "gargabeCollection",  
    "wasteContainerCleaning"  
  ],  
  "serviceStatus": "onRoute",  
  "speed": 50,  
  "vehiclePlateIdentifier": "3456ABC",  
  "vehicleType": "lorry",  
  "bearing": 43,  
  "fuelEfficiency": 13,  
  "fuelType": "Petrol",  
  "fuelFilled": 6,  
  "tripNetWeightCollected": 12,  
  "vehicleTrackerDevice": "Installed",  
  "wardId": "4",  
  "license_plate": "KA052134",  
  "currentTripCount": 1,  
  "reportId": "21645",  
  "zoneName": "South Zone",  
  "vehicleAltitude": 600,  
  "deviceSimNumber": "9942142573",  
  "wardName": "Kempegowda Ward",  
  "deviceBatteryStatus": "Connected",  
  "ignitionStatus": true,  
  "vehicleRunningStatus": "running",  
  "observationDateTime": "2021-03-11T15:51:02+05:30",  
  "serviceOnDuty": false,  
  "emergencyVehicleType": "ambulance",  
  "municipalityInfo":{  
    "district":"Bangalore Urban",  
    "ulbName":"BMC",  
    "cityId":"23",  
    "wardId":"23",  
    "stateName":"Karnataka",  
    "cityName":"Bangalore",  
    "zoneName":"South",  
    "wardName":"Bangalore Urban",  
    "zoneId":"2",  
    "wardNum":4  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "iudx:EmergencyVehicle"  
  ]  
}  
```  
#### Veicolo NGSI-LD normalizzato Esempio  
Ecco un esempio di un veicolo in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "id": "urn:ngsi-ld:Vehicle:vehicle:WasteManagement:1",  
  "type": "Vehicle",  
  "category": {  
    "type": "Property",  
    "value": [  
      "municipalServices"  
    ]  
  },  
  "vehicleType": {  
    "type": "Property",  
    "value": "lorry"  
  },  
  "name": {  
    "type": "Property",  
    "value": "C Recogida 1"  
  },  
  "vehiclePlateIdentifier": {  
    "type": "Property",  
    "value": "3456ABC"  
  },  
  "refVehicleModel": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:VehicleModel:vehiclemodel:econic"  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -3.164485591715449,  
        40.62785133667262  
      ]  
    },  
    "observedAt": "2018-09-27T12:00:00Z"  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Centro"  
  },  
  "serviceStatus": {  
    "type": "Property",  
    "value": "onRoute"  
  },  
  "cargoWeight": {  
    "type": "Property",  
    "value": 314  
  },  
  "speed": {  
    "type": "Property",  
    "value": 50,  
    "observedAt": "2018-09-27T12:00:00Z"  
  },  
  "serviceProvided": {  
    "type": "Property",  
    "value": [  
      "gargabeCollection",  
      "wasteContainerCleaning"  
    ]  
  },  
  "bearing": {  
    "type": "Property",  
    "value": 43  
  },  
  "fuelEfficiency": {  
    "type": "Property",  
    "value": 13  
  },  
  "fuelType": {  
    "type": "Property",  
    "value": "Petrol"  
  },  
  "fuelFilled": {  
    "type": "Property",  
    "value": 6  
  },  
  "tripNetWeightCollected": {  
    "type": "Property",  
    "value": 12  
  },  
  "vehicleTrackerDevice": {  
    "type": "Property",  
    "value": "Installed"  
  },  
  "wardId": {  
    "type": "Property",  
    "value": "4"  
  },  
  "license_plate": {  
    "type": "Property",  
    "value": "KA052134"  
  },  
  "currentTripCount": {  
    "type": "Property",  
    "value": 1  
  },  
  "reportId": {  
    "type": "Property",  
    "value": "21645"  
  },  
  "zoneName": {  
    "type": "Property",  
    "value": "South Zone"  
  },  
  "vehicleAltitude": {  
    "type": "Property",  
    "value": 600  
  },  
  "deviceSimNumber": {  
    "type": "Property",  
    "value": "9942142573"  
  },  
  "wardName": {  
    "type": "Property",  
    "value": "Kempegowda Ward"  
  },  
  "deviceBatteryStatus": {  
    "type": "Property",  
    "value": "Connected"  
  },  
  "ignitionStatus": {  
    "type": "Property",  
    "value": true  
  },  
  "vehicleRunningStatus": {  
    "type": "Property",  
    "value": "running"  
  },  
  "observationDateTime": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2021-03-11T15:51:02+05:30"  
    }  
  },  
  "serviceOnDuty": {  
    "type": "Property",  
    "value": false  
  },  
  "emergencyVehicleType": {  
    "type": "Property",  
    "value": "ambulance"  
  },  
  "municipalityInfo": {  
    "type": "Property",  
    "value": {  
      "district": "Bangalore Urban",  
      "ulbName": "BMC",  
      "cityId": "23",  
      "wardId": "23",  
      "stateName": "Karnataka",  
      "cityName": "Bangalore",  
      "zoneName": "South",  
      "wardName": "Bangalore Urban",  
      "zoneId": "2",  
      "wardNum": 4  
    }  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "iudx:EmergencyVehicle"  
  ]  
}  
```  
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per avere una risposta su come trattare le unità di grandezza  
