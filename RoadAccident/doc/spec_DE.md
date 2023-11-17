<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entität: RoadAccident    
=====================<!-- /10-Header -->    
<!-- 15-License -->    
[Offene Lizenz](https://github.com/smart-data-models//dataModel.Transportation/blob/master/RoadAccident/LICENSE.md)    
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Globale Beschreibung: **Eine Beschreibung eines Verkehrsunfalls mit Ursachen und Folgen. Die erste Version wurde im Rahmen des Projekts Synchronicity entwickelt**.    
Version: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Liste der Eigenschaften    
<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, kann es mehrere Typen oder verschiedene Formate/Muster haben</sub></sup>.    
- `accidentDate[date-time]`: Zeitpunkt des Unfalls  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `accidentDescription[array]`: Beschreibung dieses Verkehrsunfalls als eine Kombination von kodifizierten Situationen aufgelistet. 0: Nicht spezifizierter Umstand; 1: Der Fahrer ist regelmäßig gefahren, ohne zu wenden; 2: Der Fahrer ist abgelenkt oder unentschlossen gefahren; 3: Der Fahrer ist gefahren, ohne einen Sicherheitsabstand einzuhalten; 4: Der Fahrer ist gefahren, ohne dem von rechts kommenden Fahrzeug Vorrang einzuräumen; 5: Der Fahrer ist gefahren, ohne die Haltelinie zu beachten; 6: Der Fahrer ist gefahren, ohne das Vorfahrtsignal zu beachten; 7: Der Fahrer ist gegen den Verkehr gefahren; 8: Der Fahrer ist gefahren, ohne die Ampel- oder Agentensignale zu respektieren; 10: Der Fahrer ist gefahren, ohne die Zeichen des Durchfahrts- oder Zufahrtsverbots zu respektieren; 11: Der Fahrer ist mit überhöhter Geschwindigkeit gefahren; 12: Der Fahrer ist gefahren, ohne die Geschwindigkeitsbegrenzungen zu respektieren; 13: Der Fahrer ist mit den blendenden Lichtern gefahren, die andere Fahrzeuge kreuzen; 14: Der Fahrer ist regelmäßig nach rechts abgebogen; 15: Er ist unregelmäßig nach rechts abgebogen; 16: Der Fahrer ist regelmäßig nach links abgebogen; 17: Er ist unregelmäßig nach links abgebogen; 18: Der Fahrer ist an der Kreuzung vorbeigefahren; 20: Der Fahrer ist regelmäßig gefahren; 21: Der Fahrer ist abgelenkt oder unentschlossen gefahren; 22: Der Fahrer ist ohne Einhaltung eines Sicherheitsabstandes gefahren; 23: Der Fahrer ist mit überhöhter Geschwindigkeit gefahren; 24: Der Fahrer fuhr, ohne die Geschwindigkeitsbegrenzungen zu beachten; 25: Er fuhr nicht in der Nähe des rechten Fahrbahnrandes; 26: Der Fahrer fuhr gegen den Verkehr; 27: Der Fahrer fuhr, ohne die Zeichen des Durchfahrts- oder Zufahrtsverbots zu beachten; 28: Der Fahrer fuhr mit den blendenden Lichtern, die andere Fahrzeuge kreuzen; 29: Der Fahrer überholte regelmäßig; 30: Er überholte unregelmäßig nach rechts; 31: Der Fahrer überholte in einer Kurve, auf einer Anhöhe oder bei unzureichender Sicht; 32: Er überholte ein Fahrzeug, das ein anderes überholte; 33: Der Fahrer überholte, ohne das entsprechende Verbotsschild zu beachten; 34: Er manövrierte im Abstieg oder in der Umkehr; 35: Der Fahrer manövrierte, um in den Verkehrsfluss zu gelangen; 36: Er manövrierte, um nach links abzubiegen (Privatdurchfahrt, Verteiler); 37: Fahrer manövrierte regelmäßig, um anzuhalten oder umzukehren; 38: Fahrer manövrierte unregelmäßig, um anzuhalten oder umzukehren; 39: Es gesellten sich andere unregelmäßige Zweiräder dazu; 40: Fahrer fuhr regelmäßig; 41: Fahrer fuhr mit überhöhter Geschwindigkeit; 42: Fahrer fuhr, ohne die Geschwindigkeitsbegrenzungen zu beachten; 43: Fahrer fuhr gegen den Verkehr; 44: Fahrer überholte das Fahrzeug im Gang; 45: Manövrierte; 46: Manövriert, ohne die Ampel- oder Agentensignale zu beachten; 47: Fahrer kam aus der Einfahrt, ohne Vorsicht walten zu lassen; 48: Fahrer kam von der Fahrbahn ab und stieß mit dem Bauern zusammen; 49: Er räumte dem Fußgänger an den entsprechenden Übergängen keinen Vorrang ein; 50: Er überholte ein Fahrzeug, das angehalten hatte, um den Übergang zu ermöglichen; 51: Fahrer stieß mit der Ladung gegen den Fußgänger; 52: Fahrer überholte eine Straßenbahn ungleichmäßig an der Haltestelle; 60: Der Fahrer fuhr regelmäßig; 61: Der Fahrer fuhr abgelenkt oder unentschlossen; 62: Der Fahrer fuhr, ohne einen Sicherheitsabstand einzuhalten; 63: Der Fahrer fuhr gegen den Verkehr; 64: Der Fahrer fuhr mit überhöhter Geschwindigkeit; 65: Der Fahrer fuhr, ohne die Geschwindigkeitsbegrenzungen zu beachten; 66: Der Fahrer fuhr, ohne die Verbotsschilder für die Durchfahrt oder den Zugang zu beachten; 67: Fahrer überholte ein anderes Fahrzeug im Gang; 68: Fahrer überquerte unvorsichtig den Bahnübergang; 70: Verschütten mit Verschütten, um Aufprall zu vermeiden; 71: List mit Verschütten wegen abgelenkten Fahrens; 72: Listen mit Überschreitung der zulässigen Höchstgeschwindigkeit; 73: Fahrer bremste plötzlich mit Folge für den Transport; 74: Sturz einer Person aus dem Fahrzeug wegen: Öffnen der Tür; 75: Sturz einer Person aus dem Fahrzeug wegen: Absteigen aus dem fahrenden Fahrzeug; 76: Sturz von Personen aus dem Fahrzeug durch: Festhalten oder unsachgemäße Platzierung; 80: Versagen oder Ausfall der Bremse; 81: Bruch oder Ausfall der Lenkung; 82: Reifenplatzer oder übermäßige Abnutzung; 83: Fehlende oder unzureichende Scheinwerfer oder Positionslichter; 84: Fehlende oder unzureichende Blink- oder Bremslichtsignale; 85: Bruch von Teilen der Anhängerkupplung; 86: Mangelhafte Ausrüstung für die Beförderung gefährlicher Güter; 87: Mangel an den für Fahrzeuge von körperlich Behinderten vorgeschriebenen Anpassungen; 88: Ablösen der Räder; 89: Fehlen oder Mangel an Sichtvorrichtungen für Fahrräder  . Model: [https://schema.org/Text](https://schema.org/Text)- `accidentLocation[string]`: Kurze Beschreibung, ob sich der Unfall in einem städtischen oder außerstädtischen Gebiet ereignet hat. 0: Regional innerhalb des Stadtgebiets 1: Städtische Straße in der Stadt 2: Provinzstraße innerhalb der Stadt 3: Staatsstraße innerhalb des Dorfes 4: Außerstädtische Straße 5: Provinzstraße 6: Staatsstraße 7: Autobahn 8: Anderer Weg 9: Regionalstraße  - `accidentStatisticalDate[object]`: Ungefährer Zeitpunkt des Unfalls (häufig werden aus der ursprünglichen Unfalldatenquelle nur statistische Attribute wie Jahreszeit, Wochentag und ungefähre Uhrzeit gemeldet)  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)	- `hour`:       
	- `quarter`:       
	- `weekday[string]`: Wochentage      
- `accidentType[array]`: Schnelle Klassifizierung dieses Verkehrsunfalls. 1: Frontalaufprall; 2: Frontal-Seitenaufprall; 3: Seitenaufprall; 4: Kollision; 5: Fußgängeraufprall; 6: Aufprall auf ein stehendes oder angehaltenes Fahrzeug; 7: Aufprall auf ein geparktes Fahrzeug; 8: Aufprall auf ein Hindernis; 9: Aufprall auf einen Zug; 10: Auslaufen, Ausrutschen; 11: Unfall durch plötzliches Bremsen; 12: Unfall durch Sturz aus einem Fahrzeug;.  - `address[object]`: Die Postanschrift  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Das Land. Zum Beispiel, Spanien  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: Die Ortschaft, in der sich die Adresse befindet, und die in der Region liegt  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: Die Region, in der sich der Ort befindet, und die auf dem Land liegt  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Ein Bezirk ist eine Art von Verwaltungseinheit, die in einigen Ländern von der lokalen Regierung verwaltet wird.      
	- `postOfficeBoxNumber[string]`: Die Postfachnummer für Postfachadressen. Zum Beispiel, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: Die Postleitzahl. Zum Beispiel, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: Die Straßenanschrift  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit  - `dateCreated[date-time]`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen  - `dateModified[date-time]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben  - `description[string]`: Eine Beschreibung dieses Artikels  - `id[*]`: Eindeutiger Bezeichner der Entität  - `localId[string]`: Eindeutiger Bezeichner aus dem Quelldatensatz  . Model: [https://schema.org/Text](https://schema.org/Text)- `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `name[string]`: Der Name dieses Artikels  - `numPassengersDead[number]`: Anzahl der Fahrzeuginsassen, die bei dem Unfall ums Leben gekommen sind  . Model: [https://schema.org/Number](https://schema.org/Number)- `numPassengersInjured[number]`: Anzahl der durch den Unfall verletzten Fahrzeuginsassen  . Model: [https://schema.org/Number](https://schema.org/Number)- `numPedestrianDead[number]`: Anzahl der durch den Unfall getöteten Fußgänger  . Model: [https://schema.org/Number](https://schema.org/Number)- `numPedestrianInjured[number]`: Anzahl der durch den Unfall verletzten Fußgänger  . Model: [https://schema.org/Number](https://schema.org/Number)- `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `pedestriansInvolved[boolean]`: Boolescher Wert zur Bestimmung, ob Fußgänger an den Unfällen beteiligt waren  - `roadClass[string]`:  Die Klassifizierung der Straße, auf der sich der Unfall ereignete  . Model: [https://wiki.openstreetmap.org/wiki/Key:highway](https://wiki.openstreetmap.org/wiki/Key:highway)- `roadIntersection[string]`: Kurze Beschreibung des Straßenabschnitts, auf dem sich der Unfall ereignet hat.   1: Kreuzung; 2: Kreisverkehr; 3: Gemeldete Kreuzung; 4: Kreuzung mit Ampel; 5: Nicht gemeldete Kreuzung; 6: Bahnübergang; 7: Gerade; 8: Kurve; 9: Bodenwelle, Engstelle; 10: Steigung; 11: Beleuchtete Galerie; 12: Unbeleuchtete Galerie;  - `roadPaving[string]`: Straßenbelag. 1: Gepflasterte Straße; 2: Grob gepflasterte Straße; 3: Ungepflasterte Straße;  - `roadSign[string]`: Kurze Beschreibung des Verkehrszeichens, an dem sich der Unfall ereignet hat. 1: Abwesend; 2: Senkrecht; 3: Waagerecht; 4: Senkrecht und waagerecht; 5: Vorübergehend durch Baustelle;  - `roadSurface[string]`: Kurze Beschreibung des Zustands der Straße zum Zeitpunkt des Unfalls. 1: Trocken; 2: Nass; 3: Glatt; 4: Gefroren; 5: Schneebedeckt;  - `roadTrunk[string]`: Kurze Beschreibung der Art des Straßenabschnitts, auf dem sich der Unfall ereignet hat. 1: Straßenabzweig; 2: Nebenabzweig; 3: Nebenabzweig; 4: Kreuzungsabzweig; 5: Straßenkreuzung; 6: Autobahneinfahrt links; 7: Autobahnfahrbahn rechts; 8: Autobahneinfahrt; 9: Autobahnausfahrt; 10: Autobahnknotenpunkt; 11: Autobahnstation; 12: Sonstige Fälle; 15: Außerortsstraße  - `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `status[string]`: Status des Verkehrsunfalls. Enum:'archived, onGoing, solved'  . Model: [https://schema.org/Text](https://schema.org/Text)- `totalDeadPeopleWithin24Hours[number]`: Anzahl der unmittelbar durch den Unfall verstorbenen Personen  . Model: [https://schema.org/Number](https://schema.org/Number)- `totalDeadPeopleWithin30Days[number]`: Anzahl der Menschen, die an den Folgen des Unfalls gestorben sind  . Model: [https://schema.org/Number](https://schema.org/Number)- `totalInjured[number]`: Gesamtzahl der durch den Unfall verletzten (nicht toten) Personen  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: NGSI-Entitätstyp. es muss RoadAccident sein  - `vehiclesInvolved[array]`: Liste der am Unfall beteiligten Fahrzeuge (und Fußgänger) 0 : Fußgänger 1 : Fahrrad 2 : landwirtschaftliches Fahrzeug 3 : Bus 4 : Kleinbus 5 : Auto 6 : Wohnwagen 7 : Straßenbahn 8 : Tankwagen 9 : AutoMitWohnwagen 10 : AutoMitAnhänger 11 : Lastkraftwagen 12 : Moped 13 : Tankwagen 14 : Motorrad 15 : MotorradMitAuto 16 : Motorroller 17 : Anhänger 18 : Lieferwagen 19 : Wohnwagen 20 : Bau- oder Wartungsfahrzeug 21 : Wagen 22 : Müllwagen 23 : Kehrmaschine 24 : Reinigungswagen  - `weakestSubject[string]`: Fahrzeug, das das schwächste am Unfall beteiligte Subjekt darstellt (normalerweise Fußgänger). 0 : Fußgänger 1 : Fahrrad 2 : Landwirtschaftsfahrzeug 3 : Bus 4 : Kleinbus 5 : Auto 6 : Wohnwagen 7 : Straßenbahn 8 : Tankwagen 9 : AutoMitWohnwagen 10 : AutoMitAnhänger 11 : Lastwagen 12 : Moped 13 : Tankwagen 14 : Motorrad 15 : MotorradMitWohnwagen 16 : Motorroller 17 : Anhänger 18 : Lieferwagen 19 : Wohnwagen 20 : Bau-oderWartungsfahrzeug 21 : Wagen 22 : Müllwagen 23 : Kehrmaschine 24 : Reinigungswagen  - `weatherConditions[array]`: Kurze Beschreibung der Wetterbedingungen während dieses Verkehrsunfalls. 0 : klarNacht 1 : sonnigTag 2 : leichtbewölkt 3 : teilweisebewölkt 4 : Nebel 5 : Hochnebel 6 : hoheWolken 7 : bewölkt 8 : starkbewölkt 9 : bedeckt 10 : leichterRegenSchauer 11 : Nieselregen 12 : leichterRegen 13 : starkerRegenSchauer 14 : starkerRegen 15 : GraupelSchauer 16 : Graupel 17 : HagelSchauer 18 : Hagel 19 : Schauer 20 : leichterSchnee 21 : Schnee 22 : starkerSchneeSchauer 23 : starkerSchnee 24 : GewitterSchauer 25 : Gewitter  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Erforderliche Eigenschaften    
- `id`  - `status`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
Datenmodell aus dem Synchronizitätsprojekt    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Datenmodell Beschreibung der Eigenschaften    
Alphabetisch sortiert (für Details anklicken)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
RoadAccident:      
  description: A road accident description with causes and aftermath. First version developed in Synchronicity project      
  properties:      
    accidentDate:      
      description: Datetime of the accident      
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
          description: Week days      
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
    localId:      
      description: Unique identifier from the source data set      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
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
    numPassengersDead:      
      description: Number of vehicle's passengers dead because the accident      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    numPassengersInjured:      
      description: Number of vehicle's passengers injured because the accident      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    numPedestrianDead:      
      description: Number of pedestrians dead because the accident      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    numPedestrianInjured:      
      description: Number of pedestrians injured because the accident      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
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
    pedestriansInvolved:      
      description: Boolean to determine if pedestrians were involved in the accidents      
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
      description: 'Brief description of type of trunk of the road where the accident took place. 1: Road branch; 2: Secondary branch; 3: Minor branch; 4: Junction branch; 5: Road junction; 6: Motorway left lane; 7: Highway carriageway right; 8: Motorway junction entrance; 9: Highway exit junction; 10: Highway junction trunk; 11: Highway station; 12: Other cases; 15: Extra urban road'      
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
      description: Number of people dead directly because the accident      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    totalDeadPeopleWithin30Days:      
      description: Number of people dead because the aftermath of the accident      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    totalInjured:      
      description: total number of people injured (not dead) because the accident      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    type:      
      description: NGSI Entity type. it has to be RoadAccident      
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.Transportation/blob/master/RoadAccident/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.Transportation/RoadAccident/schema.json      
  x-model-tags: ""      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Beispiel-Nutzlasten    
#### RoadAccident NGSI-v2 key-values Beispiel    
Hier ist ein Beispiel für einen RoadAccident im JSON-LD-Format als Key-Values. Dies ist mit NGSI-v2 kompatibel, wenn `options=keyValues` verwendet wird, und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
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
  "pedestriansInvolved": true,  
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
</details>    
#### RoadAccident NGSI-v2 normalisiert Beispiel    
Hier ist ein Beispiel für einen RoadAccident im JSON-LD-Format in normalisierter Form. Dies ist mit NGSI-v2 kompatibel, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:RoadAccident:id:ORHW:45620815",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2018-06-23T04:19:24Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2020-10-29T08:36:40Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "To be defined"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Name of the element of the accident."  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Other name."  
  },  
  "description": {  
    "type": "Text",  
    "value": "Clash in the middle of a traffic light"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Municipality."  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:RoadAccident:items:SUUU:18395806",  
      "urn:ngsi-ld:RoadAccident:items:GVOF:30958855"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:RoadAccident:items:ESLS:37894243",  
      "urn:ngsi-ld:RoadAccident:items:ZNUH:87936284"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -56.6404505,  
        168.370658  
      ]  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
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
    "type": "Text",  
    "value": "worldwide"  
  },  
  "type": "RoadAccident",  
  "localId": {  
    "type": "Text",  
    "value": "20210312-A1."  
  },  
  "status": {  
    "type": "Text",  
    "value": "onGoing"  
  },  
  "accidentDate": {  
    "type": "DateTime",  
    "value": "2021-03-12T13:59:36Z"  
  },  
  "accidentStatisticalDate": {  
    "type": "StructuredValue",  
    "value": {  
      "year": 2021,  
      "quarter": 1,  
      "weekday": "Friday",  
      "hour": 4  
    }  
  },  
  "accidentType": {  
    "type": "StructuredValue",  
    "value": [  
      "10",  
      "6"  
    ]  
  },  
  "accidentDescription": {  
    "type": "StructuredValue",  
    "value": [  
      "23",  
      "46"  
    ]  
  },  
  "weatherConditions": {  
    "type": "StructuredValue",  
    "value": [  
      "10",  
      "20"  
    ]  
  },  
  "roadSurface": {  
    "type": "Text",  
    "value": "2"  
  },  
  "roadPaving": {  
    "type": "Text",  
    "value": "2"  
  },  
  "accidentLocation": {  
    "type": "Text",  
    "value": "5"  
  },  
  "roadClass": {  
    "type": "Text",  
    "value": "Motorway."  
  },  
  "roadIntersection": {  
    "type": "Text",  
    "value": "8"  
  },  
  "roadTrunk": {  
    "type": "Text",  
    "value": "12"  
  },  
  "roadSign": {  
    "type": "Text",  
    "value": "5"  
  },  
  "pedestriansInvolved": {  
    "type": "Boolean",  
    "value": true  
  },  
  "vehiclesInvolved": {  
    "type": "StructuredValue",  
    "value": [  
      "21",  
      "6"  
    ]  
  },  
  "weakestSubject": {  
    "type": "Text",  
    "value": "20"  
  },  
  "numPassengersInjured": {  
    "type": "Boolean",  
    "value": true  
  },  
  "numPassengersDead": {  
    "type": "Boolean",  
    "value": true  
  },  
  "numPedestrianInjured": {  
    "type": "Boolean",  
    "value": true  
  },  
  "numPedestrianDead": {  
    "type": "Boolean",  
    "value": false  
  },  
  "totalInjured": {  
    "type": "Number",  
    "value": 2  
  },  
  "totalDeadPeopleWithin30Days": {  
    "type": "Boolean",  
    "value": false  
  },  
  "totalDeadPeopleWithin24Hours": {  
    "type": "Boolean",  
    "value": false  
  }  
}  
```  
</details>    
#### RoadAccident NGSI-LD Schlüsselwerte Beispiel    
Hier ist ein Beispiel für einen RoadAccident im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:RoadAccident:id:ORHW:45620815",  
  "type": "RoadAccident",  
  "accidentDate": "2021-03-12T13:59:36Z",  
  "accidentDescription": [  
    "23",  
    "46"  
  ],  
  "accidentLocation": "5",  
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
  "address": {  
    "streetAddress": "FranklinStrasse",  
    "addressLocality": "Berlin",  
    "addressRegion": "Berlin",  
    "addressCountry": "Germany",  
    "postalCode": "10387",  
    "postOfficeBoxNumber": "",  
    "areaServed": "worldwide."  
  },  
  "alternateName": "Other name.",  
  "areaServed": "worldwide",  
  "dataProvider": "Municipality.",  
  "dateCreated": "2018-06-23T04:19:24Z",  
  "dateModified": "2020-10-29T08:36:40Z",  
  "description": "Clash in the middle of a traffic light",  
  "localId": "20210312-A1.",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -56.6404505,  
      168.370658  
    ]  
  },  
  "name": "Name of the element of the accident.",  
  "numPassengersDead": 1,  
  "numPassengersInjured": 1,  
  "numPedestrianDead": 0,  
  "numPedestrianInjured": 1,  
  "owner": [  
    "urn:ngsi-ld:RoadAccident:items:SUUU:18395806",  
    "urn:ngsi-ld:RoadAccident:items:GVOF:30958855"  
  ],  
  "pedestriansInvolved": true,  
  "roadClass": "Motorway.",  
  "roadIntersection": "8",  
  "roadPaving": "2",  
  "roadSign": "5",  
  "roadSurface": "2",  
  "roadTrunk": "12",  
  "seeAlso": [  
    "urn:ngsi-ld:RoadAccident:items:ESLS:37894243",  
    "urn:ngsi-ld:RoadAccident:items:ZNUH:87936284"  
  ],  
  "source": "To be defined",  
  "status": "onGoing",  
  "totalDeadPeopleWithin24Hours": 0,  
  "totalDeadPeopleWithin30Days": 0,  
  "totalInjured": 2,  
  "vehiclesInvolved": [  
    "21",  
    "6"  
  ],  
  "weakestSubject": "20",  
  "weatherConditions": [  
    "10",  
    "20"  
  ],  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Transportation/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### RoadAccident NGSI-LD normalisiert Beispiel    
Hier ist ein Beispiel für einen RoadAccident im JSON-LD-Format in normalisierter Form. Dies ist mit NGSI-LD kompatibel, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:RoadAccident:id:ORHW:45620815",  
  "type": "RoadAccident",  
  "accidentDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2021-03-12T13:59:36Z"  
    }  
  },  
  "accidentDescription": {  
    "type": "Property",  
    "value": [  
      "23",  
      "46"  
    ]  
  },  
  "accidentLocation": {  
    "type": "Property",  
    "value": "5"  
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
  "alternateName": {  
    "type": "Property",  
    "value": "Other name."  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "worldwide"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Municipality."  
  },  
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
  "description": {  
    "type": "Property",  
    "value": "Clash in the middle of a traffic light"  
  },  
  "localId": {  
    "type": "Property",  
    "value": "20210312-A1."  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -56.6404505,  
        88.370658  
      ]  
    }  
  },  
  "name": {  
    "type": "Property",  
    "value": "Name of the element of the accident."  
  },  
  "numPassengersDead": {  
    "type": "Property",  
    "value": 1  
  },  
  "numPassengersInjured": {  
    "type": "Property",  
    "value": 1  
  },  
  "numPedestrianDead": {  
    "type": "Property",  
    "value": 0  
  },  
  "numPedestrianInjured": {  
    "type": "Property",  
    "value": 1  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:RoadAccident:items:SUUU:18395806",  
      "urn:ngsi-ld:RoadAccident:items:GVOF:30958855"  
    ]  
  },  
  "pedestriansInvolved": {  
    "type": "Property",  
    "value": true  
  },  
  "roadClass": {  
    "type": "Property",  
    "value": "Motorway."  
  },  
  "roadIntersection": {  
    "type": "Property",  
    "value": "8"  
  },  
  "roadPaving": {  
    "type": "Property",  
    "value": "2"  
  },  
  "roadSign": {  
    "type": "Property",  
    "value": "5"  
  },  
  "roadSurface": {  
    "type": "Property",  
    "value": "2"  
  },  
  "roadTrunk": {  
    "type": "Property",  
    "value": "12"  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:RoadAccident:items:ESLS:37894243",  
      "urn:ngsi-ld:RoadAccident:items:ZNUH:87936284"  
    ]  
  },  
  "source": {  
    "type": "Property",  
    "value": "To be defined"  
  },  
  "status": {  
    "type": "Property",  
    "value": "onGoing"  
  },  
  "totalDeadPeopleWithin24Hours": {  
    "type": "Property",  
    "value": 0  
  },  
  "totalDeadPeopleWithin30Days": {  
    "type": "Property",  
    "value": 0  
  },  
  "totalInjured": {  
    "type": "Property",  
    "value": 2  
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
  "weatherConditions": {  
    "type": "Property",  
    "value": [  
      "10",  
      "20"  
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
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
