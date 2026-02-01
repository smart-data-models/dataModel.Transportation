<!-- 10-Header -->
  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

Entität: Vehicle  
===============
<!-- /10-Header -->
  
<!-- 15-License -->
  

[Offene Lizenz](https://github.com/smart-data-models//dataModel.Transportation/blob/master/Vehicle/LICENSE.md)  

[Dokument wurde automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->
  
<!-- 20-Description -->
  

Global description: **Diese Entität modelliert ein bestimmtes Fahrzeugmodell, einschließlich aller Eigenschaften, die mehreren Fahrzeuginstanzen angehören, die zu einem solchen Modell gehören.**  

version: 0.2.2  
<!-- /20-Description -->
  
<!-- 30-PropertiesList -->
  


## Liste der Eigenschaften  


<sup><sub>[*] Wenn es in einem Attribut keinen Typ gibt, liegt das daran, dass es mehrere Typen oder unterschiedliche Formate/Muster haben könnte</sub></sup>  
- `address[object]`: Die Postadresse  . Model: [https://schema.org/address](https://schema.org/address)  
	- `addressCountry[string]`: Das Land. Zum Beispiel Spanien  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: Die Ortschaft, in der sich die Straßenadresse befindet und die in der Region liegt  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: Die Region, in der die Ortschaft liegt und die im Land liegt  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Ein Bezirk ist eine Art von Verwaltungseinheit, die in einigen Ländern von der lokalen Regierung verwaltet wird  
	- `postOfficeBoxNumber[string]`: Die Postfachnummer für Postfachadressen. Zum Beispiel 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: Die Postleitzahl. Zum Beispiel 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: Die Straßenadresse  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
	- `streetNr[string]`: Nummer, die ein bestimmtes Grundstück auf einer öffentlichen Straße identifiziert  
- `alternateName[string]`: Ein alternativer Name für diesen Artikel  
- `annotations[array]`: Anmerkungen zum Artikel  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `areaServed[string]`: Das geografische Gebiet, in dem ein Service oder ein angebotenes Produkt bereitgestellt wird  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `battery[number]`: Der aktuelle Prozentsatz der verbleibenden Batteriekapazität im Falle eines Elektrofahrzeugs oder eines an das Fahrzeug angeschlossenen Geräts  
- `bearing[number]`: Gibt den GPS-Winkel des Fahrzeugs an, gemessen im Uhrzeigersinn vom wahren Norden. Entsprechend dem 'bearing'-Feld der GTFS-Echtzeitnachricht-Position (https://developers.google.com/transit/gtfs-realtime/reference#message-position)  . Model: [https://schema.org/Number](https://schema.org/Number)  
- `cargoWeight[number]`: Aktuelles Gewicht der Ladung des Fahrzeugs  . Model: [https://schema.org/Number](https://schema.org/Number)  
- `category[array]`: Fahrzeugkategorie(n) aus einer externen Perspektive. Dies ist anders als der Fahrzeugtyp (Auto, LKW usw.), der durch die `vehicleType`-Eigenschaft dargestellt wird. Enum: 'municipalServices, nonTracked, private, public, specialUsage, tracked'. Geführte Fahrzeuge sind solche, deren Position permanent von einem Fernsystem verfolgt wird. Oder alle anderen, die von einer Anwendung benötigt werden. Sie enthalten einen GPS-Empfänger zusammen mit einer Netzwerkverbindung, um regelmäßig eine gemeldete Position (Ort, Geschwindigkeit, Richtung ...) zu aktualisieren.  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `color[string]`: Die Farbe des Produkts  . Model: [https://schema.org/color](https://schema.org/color)  
- `currentTripCount[number]`: Die aktuelle Anzahl der Fahrten, die das Fahrzeug entsprechend dieser Beobachtung an dem gegebenen Betriebstag unternommen hat  . Model: [https://schema.org/Number](https://schema.org/Number)  
- `dataProvider[string]`: Eine Folge von Zeichen, die den Anbieter der harmonisierten Datenentität identifiziert  
- `dateCreated[date-time]`: Zeitstempel für die Erstellung der Entität. Dieser wird in der Regel von der Speicherplattform zugewiesen  
- `dateFirstUsed[date]`: Zeitstempel, der angibt, wann das Fahrzeug erstmals verwendet wurde  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)  
- `dateModified[date-time]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform zugewiesen  
- `dateVehicleFirstRegistered[date]`: Das Datum der ersten Registrierung des Fahrzeugs bei den zuständigen Behörden  . Model: [https://schema.org/dateVehicleFirstRegistered](https://schema.org/dateVehicleFirstRegistered)  
- `description[string]`: Eine Beschreibung dieses Artikels  
- `deviceBatteryStatus[string]`: Gibt den Ladezustand der Batterie des meldepflichtigen Geräts an. Enum: 'verbunden, getrennt'  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `deviceSimNumber[string]`: Gibt die SIM-Nummer des Geräts im Fahrzeug an  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `emergencyVehicleType[string]`: Art des Rettungsfahrzeugs, das dieser Beobachtung entspricht. Enum: 'Polizeiwagen, Polizeimotorrad, Polizeivan, Polizei-SWAT, Feuerwehrwagen, Tanklöschfahrzeug, Luftrettung, Rettungswagen, Motorradrettung, Rettungsfahrzeug, Fahrzeug für gefährliche Stoffe, Abschleppwagen'  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `feature[array]`: Funktion(en), die in das Fahrzeug integriert sind. Enum: 'abs, airbag, alarm, backCamera, disabledRamp, gps, internetConnection, overspeed, proximitySensor, wifi'. Oder alle anderen, die von der Anwendung benötigt werden. Um mehrere Instanzen einer Funktion darzustellen, kann die folgende Syntax verwendet werden: `<Funktion>,<Vorkommen>`. Zum Beispiel wird ein Auto mit 4 Airbags durch `airbag,4` dargestellt  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `fleetVehicleId[string]`: Die Identifikationsnummer des Fahrzeugs im Kontext der Fahrzeugflotte, der es angehört  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `fuelEfficiency[number]`: Die zurückgelegte Strecke pro verbrauchter Brennstoffeinheit, üblicherweise in Kilometern pro Liter (km/L)  . Model: [https://schema.org/Number](https://schema.org/Number)  
- `fuelFilled[number]`: Menge an in Litern aufgefülltem Kraftstoff für das Fahrzeug, das dieser Beobachtung entspricht  . Model: [https://schema.org/Number](https://schema.org/Number)  
- `fuelType[string]`: Die Art des Kraftstoffs, der für den Motor oder die Motoren des Fahrzeugs geeignet ist, das dieser Beobachtung entspricht  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `heading[*]`: Bennent die Fahrtrichtung des Fahrzeugs und wird in Dezimalgraden angegeben, wobei 0 <= `heading` < 360, im Uhrzeigersinn relativ zum wahren Norden gezählt. Wenn das Fahrzeug stationär ist (d. h. der Wert des `speed`-Attributs ist `0`), muss der Wert des `heading`-Attributs `-1` entsprechen  . Model: [https://schema.org/Number](https://schema.org/Number)  
- `id[*]`: Eindeutiger Identifikator der Entität  
- `ignitionStatus[boolean]`: Gibt den Zündungsstatus des Fahrzeugs an. True bedeutet entzündet  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)  
- `image[uri]`: Ein Bild des Artikels  . Model: [https://schema.org/URL](https://schema.org/URL)  
- `license_plate[string]`: Gibt die Nummer des Kennzeichens des Fahrzeugs an. SameAs: license_plate-Feld aus GTFS-Echtzeitnachricht-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `location[*]`: Geojson-Referenz zum Artikel. Es kann Punkt, Linienzug, Polygon, MultiPunkt, MultiLinienzug oder MultiPolygon sein  
- `mileageFromOdometer[number]`: Die gesamte vom jeweiligen Fahrzeug seit seiner ersten Produktion zurückgelegte Strecke, wie sie vom Tachometer abgelesen wird  . Model: [https://schema.org/mileageFromOdometer](https://schema.org/mileageFromOdometer)  
- `municipalityInfo[object]`: Gemeindeinformationen, die dieser Beobachtung entsprechen  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `cityId[string]`: Stadt-ID, die dieser Beobachtung entspricht  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `cityName[string]`: Stadtname, der dieser Beobachtung entspricht  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `district[string]`: Bezirksname entsprechend dieser Beobachtung  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `stateName[string]`: Name des Staates, der dieser Beobachtung entspricht  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `ulbName[string]`: Name des städtischen lokalen Verwaltungskörpers, der dieser Beobachtung entspricht  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `wardId[string]`: Ward-ID, die dieser Beobachtung entspricht  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `wardName[string]`: Name des Ward, der dieser Beobachtung entspricht  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `wardNum[number]`: Stationsnummer, die dieser Beobachtung entspricht  . Model: [https://schema.org/Number](https://schema.org/Number)    
	- `zoneId[string]`: Zonen-ID, die dieser Beobachtung entspricht  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `zoneName[string]`: Zonennamen, die dieser Beobachtung entsprechen  . Model: [https://schema.org/Text](https://schema.org/Text)    
- `name[string]`: Der Name dieses Artikels  
- `observationDateTime[date-time]`: Letzte gemeldete Beobachtungszeit  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)  
- `owner[array]`: Eine Liste, die eine JSON-kodierte Zeichenfolge enthält, die auf die eindeutigen IDs des/die Eigentümer(s) verweist  
- `previousLocation[*]`: Geojson-Referenz zum Artikel. Es kann Punkt, Linienzug, Polygon, MultiPunkt, MultiLinienzug oder MultiPolygon sein  
- `purchaseDate[date-time]`: Das Datum, an dem das Objekt, z. B. das Fahrzeug, vom aktuellen Eigentümer gekauft wurde  . Model: [https://schema.org/purchaseDate](https://schema.org/purchaseDate)  
- `refVehicleModel[*]`: Verweis auf ein Fahrzeugmodell  . Model: [https://schema.org/URL](https://schema.org/URL)  
- `reportId[string]`: Eindeutige ID, die für das Problem oder den Bericht oder das Feedback oder die Transaktion zugewiesen wird, die dieser Beobachtung entspricht  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `seeAlso[*]`: Liste von URIs, die auf zusätzliche Ressourcen über das Element verweisen  
- `serviceOnDuty[boolean]`: Art der von dem entsprechenden Rettungsfahrzeug erbrachten Dienstleistung. True bedeutet, dass das entsprechende Rettungsfahrzeug einem Notruf nachkommt bzw. eine Notrufdienstleistung erbringt und False ist ansonsten  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)  
- `serviceProvided[array]`: Dienst(e), den das Fahrzeug leisten kann oder dem es zugewiesen ist. Enum: 'auxiliaryServices, cargoTransport, construction, fairground, garbageCollection, goodsSelling, maintenance, parksAndGardens, roadSignalling, specialTransport, streetCleaning, streetLighting, urbanTransit, wasteContainerCleaning'. Oder jeder andere Wert, der von einer bestimmten Anwendung benötigt wird  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `serviceStatus[string]`: Fahrzeugstatus (aus der Sicht der bereitgestellten Dienstleistung, daher kann er nicht auf private Fahrzeuge anwendbar sein). `parked` : Das Fahrzeug ist geparkt und bietet derzeit keinen Dienst. `onRoute` : Das Fahrzeug führt eine Mission aus. Ein durch Komma getrennter Modifikator kann hinzugefügt werden, um anzugeben, welche Mission das Fahrzeug derzeit ausführt. Zum Beispiel kann `onRoute,Abfallentsorgung` verwendet werden, um anzugeben, dass das Fahrzeug unterwegs ist und eine Abfallentsorgungsmission ausführt. `defekt` : Das Fahrzeug erleidet einen vorübergehenden Ausfall. `außerBetrieb` : Das Fahrzeug ist auf der Straße, führt aber keine Mission aus, wahrscheinlich auf dem Weg zu seinem Parkplatz. Enum:'defekt, onRoute, außerBetrieb, geparkt'  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)  
- `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Es wird empfohlen, den vollqualifizierten Domänennamen des Quellanbieters oder die URL zum Quellobjekt zu verwenden.  
- `speed[*]`: Bennent die Größe der horizontalen Komponente der aktuellen Geschwindigkeit des Fahrzeugs und wird in Kilometern pro Stunde angegeben. Wenn vorhanden, muss der Wert des Speed-Attributs eine nicht-negative reelle Zahl sein. `-1` DARF verwendet werden, wenn die Geschwindigkeit aus einem bestimmten Grund vorübergehend unbekannt ist  . Model: [https://schema.org/Number](https://schema.org/Number)  
- `tripNetWeightCollected[number]`: Das Nettogewicht, das vom Fahrzeug, das dieser Beobachtung entspricht, am Ende der Fahrt gesammelt wurde  . Model: [https://schema.org/Number](https://schema.org/Number)  
- `type[string]`: NGSI-Entitätentyp. Es muss Fahrzeug sein  
- `vehicleAltitude[string]`: Gibt die aktuelle Höhe des Fahrzeugs unter Verwendung von GPS an  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `vehicleConfiguration[string]`: Ein kurzer Text, der die Konfiguration des Fahrzeugs angibt, z. B. '5-türer Schrägheck ST 2,5 MT 225 PS' oder 'Limitierte Auflage'  . Model: [https://schema.org/vehicleConfiguration](https://schema.org/vehicleConfiguration)  
- `vehicleIdentificationNumber[string]`: Die Fahrzeugidentifikationsnummer (FIN) ist eine eindeutige Seriennummer, die von der Automobilindustrie verwendet wird, um einzelne Kraftfahrzeuge zu identifizieren  . Model: [https://schema.org/vehicleIdentificationNumber](https://schema.org/vehicleIdentificationNumber)  
- `vehiclePlateIdentifier[string]`:  Ein Identifikator oder Code, der auf einer am Fahrzeug angebrachten Zulassungsplakette angezeigt wird und zu offiziellen Identifizierungszwecken verwendet wird. Der Registrierungsidentifikator ist numerisch oder alphanumerisch und innerhalb der Region der ausgebenden Behörde eindeutig. Normative Verweisungen: DATEXII `vehicleRegistrationPlateIdentifier`  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `vehicleRunningStatus[string]`: Gibt den Ladezustand der Batterie des meldepflichtigen Geräts an. Enum: 'laufend, wartend, gestoppt'  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `vehicleSpecialUsage[string]`: Gibt an, ob das Fahrzeug für besondere Zwecke wie gewerbliche Vermietung, Fahrschule oder als Taxi verwendet wurde. Die Gesetzgebung in vielen Ländern erfordert, dass diese Informationen offengelegt werden, wenn ein Auto zum Verkauf angeboten wird. Enum: 'Rettungswagen, Feuerwehr, Militär, Polizei, Schultransport, Taxi, Abfallwirtschaft'  . Model: [https://schema.org/vehicleSpecialUsage](https://schema.org/vehicleSpecialUsage)  
- `vehicleTrackerDevice[string]`: Installationsstatus des GPS-Geräts oder des zu diesem Fahrzeug gehörenden Ortungsgeräts, entsprechend dieser Beobachtung  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `vehicleType[string]`: Fahrzeugtyp aus Sicht seiner strukturellen Eigenschaften. Dies ist anders als die Fahrzeugkategorie. Enum: 'LandwirtschaftlichesFahrzeug, beliebigesFahrzeug, Gelenkfahrzeug, Fahrrad, Abfallwagen, Bus, Pkw, Wohnwagen, PkwOderLeichtesFahrzeug, PkwMitWohnwagen, PkwMitAnhänger, Reinigungswagen, Baufahrzeug, Allradfahrzeug, Hochseitenfahrzeug, Lkw, Minibus, Moped, Motorrad, MotorradMitBeiwagen, Motorroller, Kehrmaschine, Tankwagen, Dreiradfahrzeug, Anhänger, Straßenbahn, ZweiRäderFahrzeug, Wagen, FahrzeugOhneKatalysator, FahrzeugMitWohnwagen, FahrzeugMitAnhänger, mitGerademKennzeichen, mitUngerademKennzeichen, andere'. Die folgenden Werte sind definiert durch _VehicleTypeEnum_ und _VehicleTypeEnum2_, [DATEX 2 Version 2.3](http://d2docs.ndwcloud.nu/_static/umlmodel/v2.3/index.htm) und für andere Verwendungen erweitert.  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `wardId[string]`: Ward-ID der Entität, die dieser Beobachtung entspricht  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `wardName[string]`: Name des Ward der diesem Beobachtung entsprechenden Entität  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `zoneName[string]`: Zonennamen der Entität, die dieser Beobachtung entspricht  . Model: [https://schema.org/Text](https://schema.org/Text)  
<!-- /30-PropertiesList -->
  
<!-- 35-RequiredProperties -->
  

Erforderliche Eigenschaften  
- `Kategorie`  
- `id`  
- `Standort`  
- `Typ`  
- `Fahrzeugtyp`  
<!-- /35-RequiredProperties -->
  
<!-- 40-NotesYaml -->
  
<!-- /40-NotesYaml -->
  
<!-- 50-DataModelHeader -->
  

## Datenmodellbeschreibung von Eigenschaften  

Sortiert alphabetisch (Klicken für Details)  
<!-- /50-DataModelHeader -->
  
<!-- 60-ModelYaml -->
  
<details><summary><strong>full yaml details</strong></summary>    

```yaml  
Vehicle:    
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
    battery:    
      description: The current percentage of battery left in case of an electric vehicle, or a device connected to the vehicle    
      maximum: 1    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    bearing:    
      description: Gives the vehicle GPS angle measured in a clockwise direction from the True North. SameAs 'bearing' field from GTFS Realtime message-Position(https://developers.google.com/transit/gtfs-realtime/reference#message-position)    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    cargoWeight:    
      description: Current weight of the vehicle's cargo    
      exclusiveMinimum: 0    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Kilograms    
    category:    
      description: Vehicle category(ies) from an external point of view. This is different than the vehicle type (car, lorry, etc.) represented by the `vehicleType` property. Enum:'municipalServices, nonTracked, private, public, specialUsage, tracked'. Tracked vehicles are those vehicles which position is permanently tracked by a remote system. Or any other needed by an application They incorporate a GPS receiver together with a network connection to periodically update a reported position (location, speed, heading ...)    
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
      description: The color of the product    
      type: string    
      x-ngsi:    
        model: https://schema.org/color    
        type: Property    
    currentTripCount:    
      description: The current count of trips made by the vehicle corresponding to this observation on the given day of operation    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
    dateFirstUsed:    
      description: Timestamp which denotes when the vehicle was first used    
      format: date    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateVehicleFirstRegistered:    
      description: The date of the first registration of the vehicle with the respective public authorities    
      format: date    
      type: string    
      x-ngsi:    
        model: https://schema.org/dateVehicleFirstRegistered    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    deviceBatteryStatus:    
      description: Gives the Battery charging status of the reporting device. Enum:'connected, disconnected'    
      enum:    
        - connected    
        - disconnected    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    deviceSimNumber:    
      description: Gives the SIM number of the device in the vehicle    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    emergencyVehicleType:    
      description: Type of emergency vehicle corresponding to this observation. Enum:'policeCar, policeMotorcycle, policeVan, policeSWAT, fireEngine, waterTender, airAmbulance, ambulance, motorcycleAmbulance, rescueVehicle, hazardousMaterialsApparatus, towTruck    
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
      description: 'Feature(s) incorporated by the vehicle. Enum:'' abs, airbag, alarm, backCamera, disabledRamp, gps, internetConnection, overspeed, proximitySensor, wifi''. Or any other needed by the application. In order to represent multiple instances of a feature it can be used the following syntax: `<feature>,<occurences>`. For example, a car with 4 airbags will be represented by `airbag,4`'    
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
      description: The identifier of the vehicle in the context of the fleet of vehicles to which it belongs    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    fuelEfficiency:    
      description: The distance traveled per unit of fuel used, commonly in kilometers per liter (km/L)    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fuelFilled:    
      description: Amount of fuel filled in liters to the vehicle corresponding to this observation    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fuelType:    
      description: The type of fuel suitable for the engine or engines of the vehicle corresponding to this observation    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    heading:    
      description: Denotes the direction of travel of the vehicle and is specified in decimal degrees, where 0 <= `heading` < 360, counting clockwise relative to the true north. If the vehicle is stationary (i.e. the value of the `speed` attribute is `0`), then the value of the heading attribute must be equal to `-1`    
      oneOf:    
        - exclusiveMaximum: 360    
          maximum: 360    
          minimum: 0    
          type: number    
        - enum:    
            - -1    
          type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Degree    
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
    ignitionStatus:    
      description: Gives the ignition status of the vehicle. True means ignited    
      type: boolean    
      x-ngsi:    
        model: https://schema.org/Boolean    
        type: Property    
    image:    
      description: An image of the item    
      format: uri    
      type: string    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Property    
    license_plate:    
      description: 'Gives the License Plate number of the vehicle. SameAs: license_plate field from GTFS Realtime message-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)'''    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
    mileageFromOdometer:    
      description: The total distance travelled by the particular vehicle since its initial production, as read from its odometer    
      type: number    
      x-ngsi:    
        model: https://schema.org/mileageFromOdometer    
        type: Property    
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
    observationDateTime:    
      description: Last reported time of observation    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
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
    previousLocation:    
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
    purchaseDate:    
      description: The date the item e.g. vehicle was purchased by the current owner    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/purchaseDate    
        type: Property    
    refVehicleModel:    
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
      description: Reference to a VehicleModel    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Relationship    
    reportId:    
      description: Unique Id assigned for the issue or report or feedback or transaction corresponding to this observation    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
    serviceOnDuty:    
      description: Nature of service provided by emergency vehicle corresponding to this observation. True indicates the emergency vehicle corresponding to this observation is attending to/ servicing to an emergency call of duty and is False otherwise    
      type: boolean    
      x-ngsi:    
        model: https://schema.org/Boolean    
        type: Property    
    serviceProvided:    
      description: Service(s) the vehicle is capable of providing or it is assigned to. Enum:'auxiliaryServices, cargoTransport, construction, fairground, garbageCollection, goodsSelling, maintenance, parksAndGardens, roadSignalling, specialTransport, streetCleaning, streetLighting, urbanTransit, wasteContainerCleaning'. Or any other value needed by an specific application    
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
      description: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object    
      type: string    
      x-ngsi:    
        type: Property    
    speed:    
      description: Denotes the magnitude of the horizontal component of the vehicle's current velocity and is specified in Kilometers per Hour. If provided, the value of the speed attribute must be a non-negative real number. `-1` MAY be used if speed is transiently unknown for some reason    
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
      description: The net weight collected by the vehicle corresponding to this observation at the end of the trip    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be Vehicle    
      enum:    
        - Vehicle    
      type: string    
      x-ngsi:    
        type: Property    
    vehicleAltitude:    
      description: Gives the current altitude of the vehicle using GPS    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    vehicleConfiguration:    
      description: A short text indicating the configuration of the vehicle, e.g. '5dr hatchback ST 2.5 MT 225 hp' or 'limited edition'    
      type: string    
      x-ngsi:    
        model: https://schema.org/vehicleConfiguration    
        type: Property    
    vehicleIdentificationNumber:    
      description: The Vehicle Identification Number (VIN) is a unique serial number used by the automotive industry to identify individual motor vehicles    
      type: string    
      x-ngsi:    
        model: https://schema.org/vehicleIdentificationNumber    
        type: Property    
    vehiclePlateIdentifier:    
      description: ' An identifier or code displayed on a vehicle registration plate attached to the vehicle used for official identification purposes. The registration identifier is numeric or alphanumeric and is unique within the issuing authority''s region. Normative References: DATEXII `vehicleRegistrationPlateIdentifier`'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    vehicleRunningStatus:    
      description: Gives the Battery charging status of the reporting device. Enum:'running, waiting, stopped'    
      enum:    
        - running    
        - stopped    
        - waiting    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    vehicleSpecialUsage:    
      description: Indicates whether the vehicle is been used for special purposes, like commercial rental, driving school, or as a taxi. The legislation in many countries requires this information to be revealed when offering a car for sale. Enum:'ambulance, fireBrigade, military, police, schoolTransportation, taxi, trashManagement'    
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
      description: Installation status of the GPS device or the tracking device fitted to the vehicle corresponding to this observation    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    vehicleType:    
      description: Type of vehicle from the point of view of its structural characteristics. This is different than the vehicle category . Enum:'agriculturalVehicle, anyVehicle, articulatedVehicle, bicycle, binTrolley, bus, car, caravan, carOrLightVehicle, carWithCaravan, carWithTrailer, cleaningTrolley, constructionOrMaintenanceVehicle, fourWheelDrive, highSidedVehicle, lorry, minibus, moped, motorcycle, motorcycleWithSideCar, motorscooter, sweepingMachine, tanker, threeWheeledVehicle, trailer, tram, twoWheeledVehicle, trolley, van, vehicleWithoutCatalyticConverter, vehicleWithCaravan, vehicleWithTrailer, withEvenNumberedRegistrationPlates, withOddNumberedRegistrationPlates, other'. The following values defined by _VehicleTypeEnum_ and _VehicleTypeEnum2_, [DATEX 2 version 2.3](http://d2docs.ndwcloud.nu/_static/umlmodel/v2.3/index.htm) and extended for other uses    
      enum:    
        - agriculturalVehicle    
        - ambulance    
        - anyVehicle    
        - articulatedVehicle    
        - autorickshaw    
        - bicycle    
        - binTrolley    
        - BRT mini bus·    
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
        - e-bike    
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
        - pilotVessel    
        - passengerVessel    
        - cargoVessel    
        - tug    
        - militaryVessel    
        - sailingVessel    
        - vessel    
        - other    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    wardId:    
      description: Ward ID of the entity corresponding to this observation    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    wardName:    
      description: Ward name of the entity corresponding to this observation    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    zoneName:    
      description: Zone name of the entity corresponding to this observation    
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
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms...    
  x-license-url: https://github.com/smart-data-models/dataModel.Transportation/blob/master/Vehicle/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Transportation/Vehicle/schema.json    
  x-model-tags: IUDX, SEDIMARK    
  x-version: 0.2.2    
```  
</details>    
<!-- /60-ModelYaml -->
  
<!-- 70-MiddleNotes -->
  
<!-- /70-MiddleNotes -->
  
<!-- 80-Examples -->
  

## Beispielnutzlasten  

#### Fahrzeug NGSI-v2 Schlüssel-Wert-Beispiel  

Hier ist ein Beispiel für ein Fahrzeug im JSON-Format als Schlüssel-Werte. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und es die Kontextdaten einer einzelnen Entität zurückgibt.  
<details><summary><strong>show/hide example</strong></summary>    

```json  

{  
  "id": "vehicle:WasteManagement:1",  
  "type": "Vehicle",  
  "vehicleType": "lorry",  
  "battery": 0.81,  
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
  "vehicleAltitude": "600",  
  "deviceSimNumber": "9942142573",  
  "wardName": "Kempegowda Ward",  
  "deviceBatteryStatus": "connected",  
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
</details>  

#### Fahrzeug NGSI-v2 normalisiertes Beispiel  

Hier ist ein Beispiel für ein Fahrzeug im JSON-Format als normalisiert. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden und es die Kontextdaten einer einzelnen Entität zurückgibt.  
<details><summary><strong>show/hide example</strong></summary>    

```json  

{  
  "id": "vehicle:WasteManagement:1",  
  "type": "Vehicle",  
  "category": {  
    "type": "StructuredValue",  
    "value": [  
      "municipalServices"  
    ]  
  },  
  "vehicleType": {  
    "type": "Text",  
    "value": "lorry"  
  },  
  "battery": {  
    "type": "Number",  
    "value": 0.81  
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
    "type": "Text",  
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
    "type": "StructuredValue",  
    "value": [  
      "garbageCollection",  
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
    "type": "Boolean",  
    "value": true  
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
    "type": "Text",  
    "value": "600"  
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
    "value": "connected"  
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
</details>  

#### Fahrzeug-NGSI-LD-Schlüsselwert-Beispiel  

Hier ist ein Beispiel für ein Fahrzeug im JSON-LD-Format als Schlüssel-Werte. Dies ist kompatibel mit NGSI-LD, wenn `options=keyValues` verwendet wird und die Kontextdaten einer einzelnen Entität zurückgibt.  
<details><summary><strong>show/hide example</strong></summary>    

```json  

{  
  "id": "urn:ngsi-ld:Vehicle:vehicle:WasteManagement:1",  
  "type": "Vehicle",  
  "areaServed": "Centro",  
  "battery": 0.81,  
  "bearing": 43,  
  "cargoWeight": 314,  
  "category": [  
    "municipalServices"  
  ],  
  "currentTripCount": 1,  
  "deviceBatteryStatus": "connected",  
  "deviceSimNumber": "9942142573",  
  "emergencyVehicleType": "ambulance",  
  "fuelEfficiency": 13,  
  "fuelFilled": 6,  
  "fuelType": "Petrol",  
  "ignitionStatus": true,  
  "license_plate": "KA052134",  
  "location": {  
    "coordinates": [  
      -3.164485591715449,  
      40.62785133667262  
    ],  
    "type": "Point"  
  },  
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
  },  
  "name": "C Recogida 1",  
  "observationDateTime": "2021-03-11T15:51:02+05:30",  
  "refVehicleModel": "urn:ngsi-ld:VehicleModel:vehiclemodel:econic",  
  "reportId": "21645",  
  "serviceOnDuty": false,  
  "serviceProvided": [  
    "garbageCollection",  
    "wasteContainerCleaning"  
  ],  
  "serviceStatus": "onRoute",  
  "speed": 50,  
  "tripNetWeightCollected": 12,  
  "vehicleAltitude": "600",  
  "vehiclePlateIdentifier": "3456ABC",  
  "vehicleRunningStatus": "running",  
  "vehicleTrackerDevice": "Installed",  
  "vehicleType": "lorry",  
  "wardId": "4",  
  "wardName": "Kempegowda Ward",  
  "zoneName": "South Zone",  
  "@context": [  
    "https://smart-data-models.github.io/dataModel.Transportation/context.jsonld"  
  ]  
}  
```  
</details>  

#### Fahrzeug NGSI-LD normalisiertes Beispiel  

Hier ist ein Beispiel für ein Fahrzeug im JSON-LD-Format als normalisiert. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden und gibt die Kontextdaten einer einzelnen Entität zurück.  
<details><summary><strong>show/hide example</strong></summary>    

```json  

{  
  "id": "urn:ngsi-ld:Vehicle:vehicle:WasteManagement:1",  
  "type": "Vehicle",  
  "areaServed": {  
    "type": "Property",  
    "value": "Centro"  
  },  
  "battery": {  
    "type": "Property",  
    "value": 0.81,  
    "observedAt": "2021-03-11T15:51:02+05:30"  
  },  
  "bearing": {  
    "type": "Property",  
    "value": 43  
  },  
  "cargoWeight": {  
    "type": "Property",  
    "value": 314  
  },  
  "category": {  
    "type": "Property",  
    "value": [  
      "municipalServices"  
    ]  
  },  
  "currentTripCount": {  
    "type": "Property",  
    "value": 1  
  },  
  "deviceBatteryStatus": {  
    "type": "Property",  
    "value": "Connected"  
  },  
  "deviceSimNumber": {  
    "type": "Property",  
    "value": "9942142573"  
  },  
  "emergencyVehicleType": {  
    "type": "Property",  
    "value": "ambulance"  
  },  
  "fuelEfficiency": {  
    "type": "Property",  
    "value": 13  
  },  
  "fuelFilled": {  
    "type": "Property",  
    "value": 6  
  },  
  "fuelType": {  
    "type": "Property",  
    "value": "Petrol"  
  },  
  "ignitionStatus": {  
    "type": "Property",  
    "value": true  
  },  
  "license_plate": {  
    "type": "Property",  
    "value": "KA052134"  
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
  "name": {  
    "type": "Property",  
    "value": "C Recogida 1"  
  },  
  "observationDateTime": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2021-03-11T15:51:02+05:30"  
    }  
  },  
  "refVehicleModel": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:VehicleModel:vehiclemodel:econic"  
  },  
  "reportId": {  
    "type": "Property",  
    "value": "21645"  
  },  
  "serviceOnDuty": {  
    "type": "Property",  
    "value": false  
  },  
  "serviceProvided": {  
    "type": "Property",  
    "value": [  
      "garbageCollection",  
      "wasteContainerCleaning"  
    ]  
  },  
  "serviceStatus": {  
    "type": "Property",  
    "value": "onRoute"  
  },  
  "speed": {  
    "type": "Property",  
    "value": 50,  
    "observedAt": "2018-09-27T12:00:00Z"  
  },  
  "tripNetWeightCollected": {  
    "type": "Property",  
    "value": 12  
  },  
  "vehicleAltitude": {  
    "type": "Property",  
    "value": 600  
  },  
  "vehiclePlateIdentifier": {  
    "type": "Property",  
    "value": "3456ABC"  
  },  
  "vehicleRunningStatus": {  
    "type": "Property",  
    "value": "running"  
  },  
  "vehicleTrackerDevice": {  
    "type": "Property",  
    "value": "Installed"  
  },  
  "vehicleType": {  
    "type": "Property",  
    "value": "lorry"  
  },  
  "wardId": {  
    "type": "Property",  
    "value": "4"  
  },  
  "wardName": {  
    "type": "Property",  
    "value": "Kempegowda Ward"  
  },  
  "zoneName": {  
    "type": "Property",  
    "value": "South Zone"  
  },  
  "@context": [  
    "https://smart-data-models.github.io/dataModel.Transportation/context.jsonld"  
  ]  
}  
```  
</details><!-- /80-Examples -->
  
<!-- 90-FooterNotes -->
  
<!-- /90-FooterNotes -->
  
<!-- 95-Units -->
  

See [FAQ 10](https://smartdatamodels.org/index.php/faqs/) to get an answer on how to deal with magnitude units  
<!-- /95-Units -->
  
<!-- 97-LastFooter -->
  
---  

[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->
  
