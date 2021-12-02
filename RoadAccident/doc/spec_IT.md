Entità: RoadAccident  
====================  
[Licenza aperta](https://github.com/smart-data-models//dataModel.Transportation/blob/master/RoadAccident/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descrizione globale: **Descrizione di un incidente stradale con cause e conseguenze. Prima versione sviluppata nel progetto Synchronicity**  

## Elenco delle proprietà  

- `accidentDate`: Data dell'incidente  - `accidentDescription`: Descrizione di questo incidente stradale come una combinazione di situazioni codificate elencate. 0: Circostanza imprecisata; 1: Il conducente procedeva regolarmente senza svoltare; 2: Il conducente procedeva con una guida distratta o un percorso indeciso; 3: Il conducente procedeva senza mantenere la distanza di sicurezza; 4: Il conducente procedeva senza dare la precedenza al veicolo proveniente da destra; 5: Il conducente procedeva senza rispettare lo stop; 6: Il conducente procedeva senza rispettare il segnale di dare la precedenza; 7: Il conducente procedeva in senso contrario al traffico; 8: Il conducente procedeva senza rispettare i segnali del semaforo o dell'agente; 10: Il conducente procedeva senza rispettare i segnali di divieto di transito o di accesso; 11: Il conducente procedeva con eccesso di velocità; 12: Il conducente procedeva senza rispettare i limiti di velocità; 13: Il conducente procedeva con le luci abbaglianti incrociando altri veicoli; 14: Il conducente ha girato regolarmente a destra; 15: Ha girato irregolarmente a destra; 16: Il conducente ha girato regolarmente a sinistra; 17: Ha girato irregolarmente a sinistra; 18: Il conducente è passato all'incrocio; 20: Il conducente ha proceduto regolarmente; 21: Il conducente ha proceduto con una guida distratta o indecisa; 22: Il conducente ha proceduto senza mantenere la distanza di sicurezza; 23: Il conducente ha proceduto con eccesso di velocità; 24: Conducente procedeva senza rispettare i limiti di velocità; 25: Procedeva non in prossimità del margine destro della carreggiata; 26: Conducente procedeva in senso contrario al traffico; 27: Conducente procedeva senza rispettare i segnali di divieto di transito o di accesso; 28: Conducente procedeva con le luci abbaglianti incrociando altri veicoli; 29: Conducente passava regolarmente; 30: Passava irregolarmente a destra; 31: Conducente ha sorpassato in curva, in collina o con insufficiente visibilità; 32: Ha sorpassato un veicolo che ne stava sorpassando un altro; 33: Conducente è passato senza osservare l'apposito cartello di divieto; 34: Manovrato in retrocessione o conversione; 35: Conducente ha manovrato per immettersi nel flusso della circolazione; 36: Manovrato per svoltare a sinistra (passaggio privato, distributore); 37: Conducente ha manovrato regolarmente per fermarsi o fermarsi; 38: Conducente ha manovrato irregolarmente per fermarsi o fermarsi; 39: È stato affiancato da altri veicoli a due ruote irregolari; 40: Conducente ha proceduto regolarmente; 41: Conducente ha proceduto con eccesso di velocità; 42: Conducente ha proceduto senza rispettare i limiti di velocità; 43: Conducente ha proceduto contro il traffico; 44: Conducente ha superato il veicolo in marcia; 45: Manovrato; 46: Manovrava senza rispettare i segnali dei semafori o degli agenti; 47: Il conducente usciva dal passo carrabile senza precauzioni; 48: Il conducente usciva dalla corsia e colpiva il pedone; 49: Non dava la precedenza al pedone sulle strisce appropriate; 50: Superava un veicolo fermo per consentire l'attraversamento; 51: Il conducente colpiva il pedone con il carico; 52: Il conducente superava un tram in modo irregolare alla fermata; 60: Il conducente procedeva regolarmente; 61: Il conducente procedeva con una guida distratta o indecisa; 62: Il conducente procedeva senza mantenere la distanza di sicurezza; 63: Il conducente procedeva contro il traffico; 64: Il conducente procedeva con eccesso di velocità; 65: Il conducente procedeva senza rispettare i limiti di velocità; 66: Il conducente procedeva senza rispettare i segnali di divieto di transito o accesso; 67: Il conducente stava superando un altro veicolo in marcia; 68: Il conducente ha imprudentemente attraversato il passaggio a livello; 70: Sversamento con fuoriuscita per evitare l'impatto; 71: Lista con fuoriuscita per guida distratta; 72: Lista con fuoriuscita a velocità eccessiva; 73: Autista ha frenato improvvisamente con conseguenza al trasportato; 74: Caduta di persona da veicolo per: apertura porta; 75: Caduta di persona da veicolo per: discesa da veicolo in movimento; 76: Caduta di persona dal veicolo per: aggrappamento o posizionamento improprio; 80: Avaria o guasto ai freni; 81: Rottura o guasto allo sterzo; 82: Scoppio o eccessiva usura dei pneumatici; 83: Mancanza o insufficienza dei fari o delle luci di posizione; 84: Mancanza o insufficienza dei lampeggianti o dei segnali luminosi di arresto; 85: Rottura degli organi di aggancio del rimorchio; 86: Carenza di attrezzature per il trasporto di merci pericolose; 87: Carenza degli adattamenti prescritti ai veicoli dei portatori di handicap fisici; 88: Distacco delle ruote; 89: Mancanza o insufficienza di dispositivi visivi per cicli  - `accidentLocation`: Breve descrizione se l'incidente è avvenuto in un'area urbana o extraurbana. 0: Regionale all'interno dell'area urbana 1: Strada urbana nella città 2: Strada provinciale all'interno della città 3: Strada statale all'interno del paese 4: Strada extraurbana 5: Provinciale 6: Strada statale 7: Autostrada 8: Altra strada 9: Strada regionale  - `accidentStatisticalDate`: data approssimativa dell'incidente (spesso la fonte originale dei dati sugli incidenti riporta solo attributi statistici come stagione, giorno della settimana e ora approssimativa  - `accidentType`: Rapida classificazione questo incidente stradale. 1: Scontro frontale; 2: Scontro frontale-laterale; 3: Scontro laterale; 4: Collisione; 5: Investimento di pedoni; 6: Impatto con veicolo fermo o in sosta; 7: Impatto con veicolo parcheggiato; 8: Impatto con ostacolo; 9: Impatto con treno; 10: Fuoriuscita, scivolata; 11: Incidente dovuto a frenata improvvisa; 12: Incidente dovuto a caduta da un veicolo;.  - `address`: L'indirizzo postale  - `alternateName`: Un nome alternativo per questa voce  - `areaServed`: L'area geografica in cui viene fornito un servizio o un articolo offerto  - `dataProvider`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `dateCreated`: Timestamp di creazione dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `dateModified`: Timestamp dell'ultima modifica dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `description`: Una descrizione di questo articolo  - `id`: Identificatore unico dell'entità  - `localId`: Identificatore unico dal set di dati di origine  - `location`: Riferimento Geojson all'elemento. Può essere Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `name`: Il nome di questo articolo.  - `numPassengersDead`: Numero di passeggeri del veicolo morti a causa dell'incidente  - `numPassengersInjured`: Numero di passeggeri del veicolo feriti a causa dell'incidente  - `numPedestrianDead`: Numero di pedoni morti a causa dell'incidente  - `numPedestrianInjured`: Numero di pedoni feriti a causa dell'incidente  - `owner`: Una lista contenente una sequenza di caratteri codificata in JSON che si riferisce agli ID unici dei proprietari  - `pedestriansInvolved`: Booleano per determinare se i pedoni sono stati coinvolti negli incidenti  - `roadClass`:  La classificazione della strada dove è avvenuto questo incidente  - `roadIntersection`: Breve descrizione del pezzo di strada dove è avvenuto l'incidente.   1: Incrocio; 2: Rotatoria; 3: Intersezione segnalata; 4: Intersezione con semaforo; 5: Intersezione non segnalata; 6: Passaggio a livello; 7: Dritto; 8: Curva; 9: Dosso, strettoia; 10: Pendenza; 11: Galleria illuminata; 12: Galleria non illuminata;  - `roadPaving`: Pavimentazione stradale. 1: Strada asfaltata; 2: Strada asfaltata grezza; 3: Strada non asfaltata;  - `roadSign`: Breve descrizione del cartello stradale dove è avvenuto l'incidente. 1: Assente; 2: Verticale; 3: Orizzontale; 4: Verticale e orizzontale; 5: Temporaneo da cantiere;  - `roadSurface`: Breve descrizione delle condizioni della strada durante l'incidente. 1: asciutto; 2: bagnato; 3: scivoloso; 4: ghiacciato; 5: innevato;  - `roadTrunk`: Breve descrizione del tipo di tronco della strada dove è avvenuto l'incidente. 1: Ramo stradale; 2: Ramo secondario; 3: Ramo minore; 4: Ramo di svincolo; 5: Svincolo stradale; 6: Corsia sinistra autostradale; 7: Carreggiata destra autostradale; 8: Svincolo di ingresso autostradale; 9: Svincolo di uscita autostradale; 10: Tronco di svincolo autostradale; 11: Stazione autostradale; 12: Altri casi; 15: Strada extra urbana.  - `seeAlso`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source`: Una sequenza di caratteri che dà la fonte originale dei dati dell'entità come URL. Si raccomanda di essere il nome di dominio completamente qualificato del fornitore di origine, o l'URL dell'oggetto di origine.  - `status`: Stato dell'incidente stradale. Enum:'archiviato, in corso, risolto'.  - `totalDeadPeopleWithin24Hours`: Numero di persone morte direttamente a causa dell'incidente  - `totalDeadPeopleWithin30Days`: Numero di persone morte a causa delle conseguenze dell'incidente  - `totalInjured`: numero totale di persone ferite (non morte) a causa dell'incidente  - `type`: Tipo di entità NGSI. deve essere RoadAccident  - `vehiclesInvolved`: Lista dei veicoli (e pedoni) coinvolti a causa dell'incidente 0 : pedone 1 : bicicletta 2 : veicolo agricolo 3 : autobus 4 : minibus 5 : auto 6 : roulotte 7 : tram 8 : cisterna 9 : auto con roulotte 10 : auto con rimorchio 11 : camion 12 : ciclomotore 13 : cisterna 14 : motocicletta 15 : motociclettaConSideCar 16 : motorscooter 17 : rimorchio 18 : furgone 19 : roulotte 20 : veicolo di costruzione o manutenzione 21 : carrello 22 : carrello portarifiuti 23 : spazzatrice 24 : carrello di pulizia  - `weakestSubject`: veicolo che rappresenta il soggetto più debole coinvolto perché l'incidente (di solito pedone). 0 : pedone 1 : bicicletta 2 : veicolo agricolo 3 : autobus 4 : minibus 5 : auto 6 : roulotte 7 : tram 8 : autocisterna 9 : auto con roulotte 10 : auto con rimorchio 11 : camion 12 : motorino 13 : autocisterna 14 : moto 15 : moto con carrozzeria 16 : motocooter 17 : rimorchio 18 : furgone 19 : roulotte 20 : veicolo da costruzione o manutenzione 21 : carrello 22 : carrello portarifiuti 23 : macchina spazzatrice 24 : carrello di pulizia  - `weatherConditions`: Breve descrizione delle condizioni meteorologiche durante questo incidente stradale. 0 : serenoNotte 1 : soleggiatoGiorno 2 : poco nuvoloso 3 : parzialmente nuvoloso 4 : foschia 5 : nebbia 6 : nuvole alte 7 : nuvoloso 8 : molto nuvoloso 9 : nuvoloso 10 : pioggia leggera 11 : pioviggine 12 : pioggia leggera 13 : heavyRainShower 14 : heavyRain 15 : sleetShower 16 : sleet 17 : hailShower 18 : hail 19 : shower 20 : lightSnow 21 : snow 22 : heavySnowShower 23 : heavySnow 24 : thunderShower 25 : thunder    
Proprietà richieste  
- `id`  - `status`  - `type`    
Modello di dati proveniente dal progetto synchronicity  
## Descrizione del modello di dati delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
RoadAccident:    
  description: 'A road accident description with causes and aftermath. First version developed in Synchronicity project'    
  properties:    
    accidentDate:    
      description: 'Datetime of the accident'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    accidentDescription:    
      description: 'Description about this Road Accident as a combination of codified situation enlisted. 0: Unspecified circumstance; 1: Driver proceeded regularly without turning; 2: Driver proceeded with a distracted driving or undecided course; 3: Driver proceeded without maintaining a safe distance; 4: Driver proceeded without giving priority to the vehicle coming from the right; 5: Driver proceeded without respecting the stop; 6: Driver proceeded without respecting the signal to give precedence; 7: Driver proceeded against traffic; 8: Driver proceeded without respecting the traffic light or agent signals; 10: Driver proceeded without respecting the signs of prohibition of transit or access; 11: Driver proceeded with speeding; 12: Driver proceeded without respecting the speed limits; 13: Driver proceeded with the dazzling lights crossing other vehicles; 14: Driver turned right regularly; 15: It turned irregularly to the right; 16: Driver turned left regularly; 17: It turned irregularly to the left; 18: Driver passed at the intersection; 20: Driver proceeded regularly; 21: Driver proceeded with a distracted driving or undecided course; 22: Driver proceeded without maintaining a safe distance; 23: Driver proceeded with speeding; 24: Driver proceeded without respecting the speed limits; 25: It proceeded not near the right edge of the roadway; 26: Driver proceeded against traffic; 27: Driver proceeded without respecting the signs of prohibition of transit or access; 28: Driver proceeded with the dazzling lights crossing other vehicles; 29: Driver passed regularly; 30: It passed irregularly to the right; 31: Driver overtook on a curve, on a hill or with insufficient visibility; 32: It overtook a vehicle that was overtaking another; 33: Driver passed without observing the appropriate prohibition sign; 34: Maneuvered in relegation or conversion; 35: Driver maneuvered to get into the flow of circulation; 36: Maneuvering To turn left (private passage, distributor); 37: Driver maneuvered regularly to stop or stop; 38: Driver maneuvered irregularly to stop or stop; 39: It was joined by other irregular two-wheeled vehicles; 40: Driver proceeded regularly; 41: Driver proceeded with speeding; 42: Driver proceeded without respecting the speed limits; 43: Driver proceeded against traffic; 44: Driver passed the vehicle in gear; 45: Maneuvered; 46: Maneuvered without respecting traffic light or agent signals; 47: Driver came out of the driveway without precaution; 48: Driver stepped out of the lane and hit the pawn; 49: It did not give priority to the pedestrian on the appropriate crossings; 50: It overtook a vehicle stopped to allow the crossing; 51: Driver hit the pedestrian with the load; 52: Driver was passing a tram unevenly at the stop; 60: Driver proceeded regularly; 61: Driver proceeded with a distracted driving or undecided course; 62: Driver proceeded without maintaining a safe distance; 63: Driver proceeded against traffic; 64: Driver proceeded with speeding; 65: Driver proceeded without respecting the speed limits; 66: Driver proceeded without respecting the signs of prohibition of transit or access; 67: Driver was passing another vehicle in gear; 68: Driver imprudently crossed the level crossing; 70: Spill with spillage to avoid impact; 71: Listening with spillage for distracted driving; 72: List with over-speed spill; 73: Driver suddenly braked with consequence to the transported; 74: Fall of person from vehicle for: door opening; 75: Fall of person from vehicle for: descent from vehicle in motion; 76: Fall of person from vehicle due to: clinging or improperly placed; 80: Brake failure or failure; 81: Breakage or steering failure; 82: Tire burst or excessive wear; 83: Lack or insufficiency of headlights or position lights; 84: Lack or insufficiency of flashing lights or stopping light signals; 85: Breaking of trailer coupling parts; 86: Deficiency of dangerous goods transport equipment; 87: Deficiency of the adaptations prescribed to vehicles of physically handicapped people; 88: Wheel detachment; 89: Lack or insufficiency    
        of visual devices for cycles'    
      items:    
        enum:    
          - 0    
          - 1    
          - 2    
          - 3    
          - 4    
          - 5    
          - 6    
          - 7    
          - 8    
          - 9    
          - 10    
          - 11    
          - 12    
          - 13    
          - 14    
          - 15    
          - 16    
          - 17    
          - 18    
          - 19    
          - 20    
          - 21    
          - 22    
          - 23    
          - 24    
          - 25    
          - 26    
          - 27    
          - 28    
          - 29    
          - 30    
          - 31    
          - 32    
          - 33    
          - 34    
          - 35    
          - 36    
          - 37    
          - 38    
          - 39    
          - 40    
          - 41    
          - 42    
          - 43    
          - 44    
          - 45    
          - 46    
          - 47    
          - 48    
          - 49    
          - 50    
          - 51    
          - 52    
          - 53    
          - 54    
          - 55    
          - 56    
          - 57    
          - 58    
          - 59    
          - 60    
          - 61    
          - 62    
          - 63    
          - 64    
          - 65    
          - 66    
          - 67    
          - 68    
          - 69    
          - 70    
          - 71    
          - 72    
          - 73    
          - 74    
          - 75    
          - 76    
          - 77    
          - 78    
          - 79    
          - 80    
          - 81    
          - 82    
          - 83    
          - 84    
          - 85    
          - 86    
          - 87    
          - 88    
          - 89    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    accidentLocation:    
      description: 'Brief description if the accident took place in a urban or extra-urban area. 0: Regional within the urban area 1: Urban road in the town 2: Provincial road within the town 3: State road within the village 4: Extra-urban road 5: Provincial 6: State road 7: Highway 8: Another way 9: Regional road'    
      enum:    
        - 0    
        - 1    
        - 2    
        - 3    
        - 4    
        - 5    
        - 6    
        - 7    
        - 8    
        - 9    
      type: string    
      x-ngsi:    
        type: Property    
    accidentStatisticalDate:    
      description: 'approximate datetime of the accident (often original accident data source reports only statistical attributes such as season, weekday and approximate hour'    
      properties:    
        hour:    
          type: integer    
        quarter:    
          type: integer    
        weekday:    
          description: 'Week days'    
          enum:    
            - Monday    
            - Tuesday    
            - Wednesday    
            - Thursday    
            - Friday    
            - Saturday    
            - Sunday    
          type: string    
        year:    
          type: integer    
      type: object    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    accidentType:    
      description: 'Quick classification this Road Accident. 1: Frontal collision; 2: Frontal-lateral collision; 3: Side crash; 4: Collision; 5: Pedestrian investment; 6: Impact with vehicle stopped or stopped; 7: Impact with parked vehicle; 8: Impact with obstacle; 9: Impact with train; 10: Spill, slip; 11: Accident due to sudden braking; 12: Accident due to falling from a vehicle;. '    
      items:    
        enum:    
          - 1    
          - 2    
          - 3    
          - 4    
          - 5    
          - 6    
          - 7    
          - 8    
          - 9    
          - 10    
          - 11    
          - 12    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
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
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
    id:    
      anyOf: &roadaccident_-_properties_-_owner_-_items_-_anyof    
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
    localId:    
      description: 'Unique identifier from the source data set'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
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
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    numPassengersDead:    
      description: 'Number of vehicle''s passengers dead because the accident'    
      minimum: 0    
      type: integer    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    numPassengersInjured:    
      description: 'Number of vehicle''s passengers injured because the accident'    
      minimum: 0    
      type: integer    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    numPedestrianDead:    
      description: 'Number of pedestrians dead because the accident'    
      minimum: 0    
      type: integer    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    numPedestrianInjured:    
      description: 'Number of pedestrians injured because the accident'    
      minimum: 0    
      type: integer    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *roadaccident_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    pedestriansInvolved:    
      description: 'Boolean to determine if pedestrians were involved in the accidents'    
      type: boolean    
      x-ngsi:    
        type: Property    
    roadClass:    
      description: ' The classification of road where this accident took place'    
      type: string    
      x-ngsi:    
        model: https://wiki.openstreetmap.org/wiki/Key:highway    
        type: Property    
    roadIntersection:    
      description: 'Brief description of the piece of the road where the accident took place.   1: Crossroad; 2: Roundabout; 3: Reported intersection; 4: Intersection with traffic light; 5: Intersection not reported; 6: Rail crossing; 7: Straight; 8: Curve; 9: Bump, bottleneck; 10: Slope; 11: Illuminated gallery; 12: Unlit gallery;'    
      enum:    
        - 1    
        - 2    
        - 3    
        - 4    
        - 5    
        - 6    
        - 7    
        - 8    
        - 9    
        - 10    
        - 11    
        - 12    
      type: string    
      x-ngsi:    
        type: Property    
    roadPaving:    
      description: 'Road paving. 1: Paved road; 2: Rough paved road; 3: Unpaved road;'    
      enum:    
        - 1    
        - 2    
        - 3    
      type: string    
      x-ngsi:    
        type: Property    
    roadSign:    
      description: 'Brief description of the road sign where the accident took place. 1: Absent; 2: Vertical; 3: Horizontal; 4: Vertical and horizontal; 5: Temporary by construction site;'    
      enum:    
        - 1    
        - 2    
        - 3    
        - 4    
        - 5    
      type: string    
      x-ngsi:    
        type: Property    
    roadSurface:    
      description: 'Brief description of the condition of the road during the accident. 1: Dry; 2: Wet; 3: Slippery; 4: frozen; 5: Snowcapped;'    
      enum:    
        - 1    
        - 2    
        - 3    
        - 4    
        - 5    
      type: string    
      x-ngsi:    
        type: Property    
    roadTrunk:    
      description: 'Brief description of type of trunk of the road where the accident took place. 1: Road branch; 2: Secondary branch; 3: Minor branch; 4: Junction branch; 5: Road junction; 6: Motorway left lane; 7: Highway carriageway right; 8: Motorway junction entrance; 9: Highway exit junction; 10: Highway junction trunk; 11: Highway station; 12: Other cases; 15: Extra urban road.'    
      enum:    
        - 1    
        - 2    
        - 3    
        - 4    
        - 5    
        - 6    
        - 7    
        - 8    
        - 9    
        - 10    
        - 11    
        - 12    
        - 15    
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
    status:    
      description: 'Status of the Road Accident. Enum:''archived, onGoing, solved'''    
      enum:    
        - archived    
        - onGoing    
        - solved    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    totalDeadPeopleWithin24Hours:    
      description: 'Number of people dead directly because the accident'    
      minimum: 0    
      type: integer    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    totalDeadPeopleWithin30Days:    
      description: 'Number of people dead because the aftermath of the accident'    
      minimum: 0    
      type: integer    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    totalInjured:    
      description: 'total number of people injured (not dead) because the accident'    
      minimum: 0    
      type: integer    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: 'NGSI Entity type. it has to be RoadAccident'    
      enum:    
        - RoadAccident    
      type: string    
      x-ngsi:    
        type: Property    
    vehiclesInvolved:    
      description: 'List of the vehicles (and pedestrians) involved because the accident 0 : pedestrian 1 : bicycle 2 : agriculturalVehicle 3 : bus 4 : minibus 5 : car 6 : caravan 7 : tram 8 : tanker 9 : carWithCaravan 10 : carWithTrailer 11 : lorry 12 : moped 13 : tanker 14 : motorcycle 15 : motorcycleWithSideCar 16 : motorscooter 17 : trailer 18 : van 19 : caravan 20 : constructionOrMaintenanceVehicle 21 : trolley 22 : binTrolley 23 : sweepingMachine 24 : cleaningTrolley'    
      items:    
        enum:    
          - 0    
          - 1    
          - 2    
          - 3    
          - 4    
          - 5    
          - 6    
          - 7    
          - 8    
          - 9    
          - 10    
          - 11    
          - 12    
          - 13    
          - 14    
          - 15    
          - 16    
          - 17    
          - 18    
          - 19    
          - 20    
          - 21    
          - 22    
          - 23    
          - 24    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    weakestSubject:    
      description: 'vehicle that represent the weakest subject involved because the accident (usually pedestrian). 0 : pedestrian 1 : bicycle 2 : agriculturalVehicle 3 : bus 4 : minibus 5 : car 6 : caravan 7 : tram 8 : tanker 9 : carWithCaravan 10 : carWithTrailer 11 : lorry 12 : moped 13 : tanker 14 : motorcycle 15 : motorcycleWithSideCar 16 : motorscooter 17 : trailer 18 : van 19 : caravan 20 : constructionOrMaintenanceVehicle 21 : trolley 22 : binTrolley 23 : sweepingMachine 24 : cleaningTrolley'    
      enum:    
        - 0    
        - 1    
        - 2    
        - 3    
        - 4    
        - 5    
        - 6    
        - 7    
        - 8    
        - 9    
        - 10    
        - 11    
        - 12    
        - 13    
        - 14    
        - 15    
        - 16    
        - 17    
        - 18    
        - 19    
        - 20    
        - 21    
        - 22    
        - 23    
        - 24    
      type: string    
      x-ngsi:    
        type: Property    
    weatherConditions:    
      description: 'Brief description of weather conditions during this Road Accident. 0 : clearNight 1 : sunnyDay 2 : slightlyCloudy 3 : partlyCloudy 4 : mist 5 : fog 6 : highClouds 7 : cloudy 8 : veryCloudy 9 : overcast 10 : lightRainShower 11 : drizzle 12 : lightRain 13 : heavyRainShower 14 : heavyRain 15 : sleetShower 16 : sleet 17 : hailShower 18 : hail 19 : shower 20 : lightSnow 21 : snow 22 : heavySnowShower 23 : heavySnow 24 : thunderShower 25 : thunder'    
      items:    
        enum:    
          - 0    
          - 1    
          - 2    
          - 3    
          - 4    
          - 5    
          - 6    
          - 7    
          - 8    
          - 9    
          - 10    
          - 11    
          - 12    
          - 13    
          - 14    
          - 15    
          - 16    
          - 17    
          - 18    
          - 19    
          - 20    
          - 21    
          - 22    
          - 23    
          - 24    
          - 25    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - status    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Transportation/blob/master/RoadAccident/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Transportation/RoadAccident/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
## Esempio di payloads  
#### RoadAccident NGSI-v2 valori chiave Esempio  
Ecco un esempio di un RoadAccident in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "id": "urn:ngsi-ld:RoadAccident:id:ORHW:45620815",  
  "type": "RoadAccident",  
  "dateCreated": "2018-06-23T04:19:24Z",  
  "dateModified": "2020-10-29T08:36:40Z",  
  "source": "To be defined",  
  "name": "Name of the element of the accident.",  
  "alternateName": "Other name.",  
  "description": "Clash in the middle of a traffic light",  
  "dataProvider": "Municipality.",  
  "owner": [  
    "urn:ngsi-ld:RoadAccident:items:SUUU:18395806",  
    "urn:ngsi-ld:RoadAccident:items:GVOF:30958855"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:RoadAccident:items:ESLS:37894243",  
    "urn:ngsi-ld:RoadAccident:items:ZNUH:87936284"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -56.6404505,  
      168.370658  
    ]  
  },  
  "address": {  
    "streetAddress": "FranklinStrasse",  
    "addressLocality": "Berlin",  
    "addressRegion": "Berlin",  
    "addressCountry": "Germany",  
    "postalCode": "10387",  
    "postOfficeBoxNumber": "",  
    "areaServed": "worldwide."  
  },  
  "areaServed": "worldwide",  
  "localId": "20210312-A1.",  
  "status": "onGoing",  
  "accidentDate": "2021-03-12T13:59:36Z",  
  "accidentStatisticalDate": {  
    "year": 2021,  
    "quarter": 1,  
    "weekday": "Friday",  
    "hour": 4  
  },  
  "accidentType": [  
    "10",  
    "6"  
  ],  
  "accidentDescription": [  
    "23",  
    "46"  
  ],  
  "weatherConditions": [  
    "10",  
    "20"  
  ],  
  "roadSurface": "2",  
  "roadPaving": "2",  
  "accidentLocation": "5",  
  "roadClass": "Motorway.",  
  "roadIntersection": "8",  
  "roadTrunk": "12",  
  "roadSign": "5",  
  "pedestriansInvolved":  
    true  
  ,  
  "vehiclesInvolved": [  
    "21",  
    "6"  
  ],  
  "weakestSubject": "20",  
  "numPassengersInjured": 1,  
  "numPassengersDead": 1,  
  "numPedestrianInjured": 1,  
  "numPedestrianDead": 0,  
  "totalInjured": 2,  
  "totalDeadPeopleWithin30Days": 0,  
  "totalDeadPeopleWithin24Hours": 0  
}  
```  
#### RoadAccident NGSI-v2 normalizzato Esempio  
Ecco un esempio di un RoadAccident in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "id": "urn:ngsi-ld:RoadAccident:id:ORHW:45620815",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2018-06-23T04:19:24Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2020-10-29T08:36:40Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "To be defined"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Name of the element of the accident."  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Other name."  
  },  
  "description": {  
    "type": "Property",  
    "value": "Clash in the middle of a traffic light"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Municipality."  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:RoadAccident:items:SUUU:18395806",  
      "urn:ngsi-ld:RoadAccident:items:GVOF:30958855"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:RoadAccident:items:ESLS:37894243",  
      "urn:ngsi-ld:RoadAccident:items:ZNUH:87936284"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -56.6404505,  
        168.370658  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "FranklinStrasse",  
      "addressLocality": "Berlin",  
      "addressRegion": "Berlin",  
      "addressCountry": "Germany",  
      "postalCode": "10387",  
      "postOfficeBoxNumber": "",  
      "areaServed": "worldwide."  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "worldwide"  
  },  
  "type": "RoadAccident",  
  "localId": {  
    "type": "Property",  
    "value": "20210312-A1."  
  },  
  "status": {  
    "type": "Property",  
    "value": "onGoing"  
  },  
  "accidentDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2021-03-12T13:59:36Z"  
    }  
  },  
  "accidentStatisticalDate": {  
    "type": "Property",  
    "value": {  
      "year": 2021,  
      "quarter": 1,  
      "weekday": "Friday",  
      "hour": 4  
    }  
  },  
  "accidentType": {  
    "type": "Property",  
    "value": [  
      "10",  
      "6"  
    ]  
  },  
  "accidentDescription": {  
    "type": "Property",  
    "value": [  
      "23",  
      "46"  
    ]  
  },  
  "weatherConditions": {  
    "type": "Property",  
    "value": [  
      "10",  
      "20"  
    ]  
  },  
  "roadSurface": {  
    "type": "Property",  
    "value": "2"  
  },  
  "roadPaving": {  
    "type": "Property",  
    "value": "2"  
  },  
  "accidentLocation": {  
    "type": "Property",  
    "value": "5"  
  },  
  "roadClass": {  
    "type": "Property",  
    "value": "Motorway."  
  },  
  "roadIntersection": {  
    "type": "Property",  
    "value": "8"  
  },  
  "roadTrunk": {  
    "type": "Property",  
    "value": "12"  
  },  
  "roadSign": {  
    "type": "Property",  
    "value": "5"  
  },  
  "pedestriansInvolved": {  
    "type": "Property",  
    "value": [  
      "true"  
    ]  
  },  
  "vehiclesInvolved": {  
    "type": "Property",  
    "value": [  
      "21",  
      "6"  
    ]  
  },  
  "weakestSubject": {  
    "type": "Property",  
    "value": "20"  
  },  
  "numPassengersInjured": {  
    "type": "Property",  
    "value": 1  
  },  
  "numPassengersDead": {  
    "type": "Property",  
    "value": 1  
  },  
  "numPedestrianInjured": {  
    "type": "Property",  
    "value": 1  
  },  
  "numPedestrianDead": {  
    "type": "Property",  
    "value": 0  
  },  
  "totalInjured": {  
    "type": "Property",  
    "value": 2  
  },  
  "totalDeadPeopleWithin30Days": {  
    "type": "Property",  
    "value": 0  
  },  
  "totalDeadPeopleWithin24Hours": {  
    "type": "Property",  
    "value": 0  
  }  
}  
```  
#### RoadAccident Valori chiave NGSI-LD Esempio  
Ecco un esempio di un RoadAccident in formato JSON-LD come key-values. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "id": "urn:ngsi-ld:RoadAccident:id:ORHW:45620815",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2018-06-23T04:19:24Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2020-10-29T08:36:40Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "To be defined"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Name of the element of the accident."  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Other name."  
  },  
  "description": {  
    "type": "Property",  
    "value": "Clash in the middle of a traffic light"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Municipality."  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:RoadAccident:items:SUUU:18395806",  
      "urn:ngsi-ld:RoadAccident:items:GVOF:30958855"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:RoadAccident:items:ESLS:37894243",  
      "urn:ngsi-ld:RoadAccident:items:ZNUH:87936284"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -56.6404505,  
        168.370658  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "FranklinStrasse",  
      "addressLocality": "Berlin",  
      "addressRegion": "Berlin",  
      "addressCountry": "Germany",  
      "postalCode": "10387",  
      "postOfficeBoxNumber": "",  
      "areaServed": "worldwide."  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "worldwide"  
  },  
  "type": "RoadAccident",  
  "localId": {  
    "type": "Property",  
    "value": "20210312-A1."  
  },  
  "status": {  
    "type": "Property",  
    "value": "onGoing"  
  },  
  "accidentDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2021-03-12T13:59:36Z"  
    }  
  },  
  "accidentStatisticalDate": {  
    "type": "Property",  
    "value": {  
      "year": 2021,  
      "quarter": 1,  
      "weekday": "Friday",  
      "hour": 4  
    }  
  },  
  "accidentType": {  
    "type": "Property",  
    "value": [  
      "10",  
      "6"  
    ]  
  },  
  "accidentDescription": {  
    "type": "Property",  
    "value": [  
      "23",  
      "46"  
    ]  
  },  
  "weatherConditions": {  
    "type": "Property",  
    "value": [  
      "10",  
      "20"  
    ]  
  },  
  "roadSurface": {  
    "type": "Property",  
    "value": "2"  
  },  
  "roadPaving": {  
    "type": "Property",  
    "value": "2"  
  },  
  "accidentLocation": {  
    "type": "Property",  
    "value": "5"  
  },  
  "roadClass": {  
    "type": "Property",  
    "value": "Motorway."  
  },  
  "roadIntersection": {  
    "type": "Property",  
    "value": "8"  
  },  
  "roadTrunk": {  
    "type": "Property",  
    "value": "12"  
  },  
  "roadSign": {  
    "type": "Property",  
    "value": "5"  
  },  
  "pedestriansInvolved": {  
    "type": "Property",  
    "value": [  
      "true"  
    ]  
  },  
  "vehiclesInvolved": {  
    "type": "Property",  
    "value": [  
      "21",  
      "6"  
    ]  
  },  
  "weakestSubject": {  
    "type": "Property",  
    "value": "20"  
  },  
  "numPassengersInjured": {  
    "type": "Property",  
    "value": 1  
  },  
  "numPassengersDead": {  
    "type": "Property",  
    "value": 1  
  },  
  "numPedestrianInjured": {  
    "type": "Property",  
    "value": 1  
  },  
  "numPedestrianDead": {  
    "type": "Property",  
    "value": 0  
  },  
  "totalInjured": {  
    "type": "Property",  
    "value": 2  
  },  
  "totalDeadPeopleWithin30Days": {  
    "type": "Property",  
    "value": 0  
  },  
  "totalDeadPeopleWithin24Hours": {  
    "type": "Property",  
    "value": 0  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### RoadAccident NGSI-LD normalizzato Esempio  
Ecco un esempio di un RoadAccident in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "id": "urn:ngsi-ld:RoadAccident:id:ORHW:45620815",  
  "type": "RoadAccident",  
  "dateCreated": "2018-06-23T04:19:24Z",  
  "dateModified": "2020-10-29T08:36:40Z",  
  "source": "To be defined",  
  "name": "Name of the element of the accident.",  
  "alternateName": "Other name.",  
  "description": "Clash in the middle of a traffic light",  
  "dataProvider": "Municipality.",  
  "owner": [  
    "urn:ngsi-ld:RoadAccident:items:SUUU:18395806",  
    "urn:ngsi-ld:RoadAccident:items:GVOF:30958855"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:RoadAccident:items:ESLS:37894243",  
    "urn:ngsi-ld:RoadAccident:items:ZNUH:87936284"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -56.6404505,  
      168.370658  
    ]  
  },  
  "address": {  
    "streetAddress": "FranklinStrasse",  
    "addressLocality": "Berlin",  
    "addressRegion": "Berlin",  
    "addressCountry": "Germany",  
    "postalCode": "10387",  
    "postOfficeBoxNumber": "",  
    "areaServed": "worldwide."  
  },  
  "areaServed": "worldwide",  
  "localId": "20210312-A1.",  
  "status": "onGoing",  
  "accidentDate": "2021-03-12T13:59:36Z",  
  "accidentStatisticalDate": {  
    "year": 2021,  
    "quarter": 1,  
    "weekday": "Friday",  
    "hour": 4  
  },  
  "accidentType": [  
    "10",  
    "6"  
  ],  
  "accidentDescription": [  
    "23",  
    "46"  
  ],  
  "weatherConditions": [  
    "10",  
    "20"  
  ],  
  "roadSurface": "2",  
  "roadPaving": "2",  
  "accidentLocation": "5",  
  "roadClass": "Motorway.",  
  "roadIntersection": "8",  
  "roadTrunk": "12",  
  "roadSign": "5",  
  "pedestriansInvolved": [  
    "true"  
  ],  
  "vehiclesInvolved": [  
    "21",  
    "6"  
  ],  
  "weakestSubject": "20",  
  "numPassengersInjured": 1,  
  "numPassengersDead": 1,  
  "numPedestrianInjured": 1,  
  "numPedestrianDead": 0,  
  "totalInjured": 2,  
  "totalDeadPeopleWithin30Days": 0,  
  "totalDeadPeopleWithin24Hours": 0,  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per avere una risposta su come trattare le unità di grandezza