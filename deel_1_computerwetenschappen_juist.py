def rooster_naar_coord(vak_grootte, rooster_pos):
    # vak_grootte en rooster_pos zijn de parameters gegeven aan de functie
    # vak grootte is de lengte van een vak in pixels
    # rooster_pos is een tuple/lijst met twee elementen
    # eerste element is het nummer van de kolom en de tweede is het nummer van de rij
    # de benedenste rij heeft index 0 en de meest linkse kolom heeft ook index 0


    # varabele x is de "realistische" positie -> d.w.z. dat voor gegeven rooster_pos(0,0), x=1 omdat het over eerste kolom van links gaat
    # dezelfde voor y

    x = rooster_pos[0] + 1
    y = rooster_pos[1] + 1


    # x_coord is de coordinaat van het middenpunt van de gegeven vak
    # die wordt berekend door vak_grootte te vermenigvuldigen met (x-1/2) (die -1/2 komt omdat je maar de helft van de laatste vak moet nemen om het middenpunt te krijgen)
    # dezelfde voor y

    x_coord = vak_grootte*(x-1/2)
    y_coord = vak_grootte*(y-1/2)

    return (x_coord, y_coord)

def coord_naar_rooster(vak_grootte, coord_pos):
    # vak_grootte en coord_pos zijn de parameters gegeven aan de functie
    # vak grootte is de lengte van een vak in pixels
    # coord_pos is een tuple/lijst met twee elementen
    # eerste element is de x coordinaat in pixels en de tweede is de y coordinaat in pixels
    # coordinaat helemaal benden links is (0,0)

    x_coord = coord_pos[0]
    y_coord = coord_pos[1]


    # x is de vak waarin gegeven x coordinaat behoort
    # x wordt berekent door x_coord te delen door de vak grootte en dan afronden naar beneden ( int() van een niet-geheel getal, rondt dat getal standaard naar beneden )
    # voor een vak grootte van 10 pixels, behoort coord 9.4 tot de nulde kolom, 10.2 tot de eerste, kolom 24.7 tot de tweede, etc
    # idem voor y

    x = int(x_coord/vak_grootte)
    y = int(y_coord/vak_grootte)

    return(x,y)

# dit zijn voorbeeldlijsten voor bodem en water

bodem = [1,1,4,1,2,5,1,1,2,1,3,1,2,1,2,1,1]
water = [0,0,0,3,2,0,2,2,1,2,0,0,0,1,0,0,0]


def aantal_meeren(W, B=None):
    # B=None wilt zeggen dat wanneer je functie aantal_meeren gebruukt, je tweede argument niet moet geven, omdat bodemlijst helemaal niet nodig is voor deze functie
    # als je dus tweede argument geeft, dan is B gelijk aan die tweede argument, en als je hem niet geeft (wat eigenlijk de bedoeling is), dan is B gewoon gelijk aan None
    # in principe, kan je die B=None gewoon weglaten, maar in de opdracht stond dat je bodem als parameter in aantal_meeren moest gebruiken, dus ik heb het erbij gezet

    # er wordt aangenomen dat 'gesloten' meeren niet mogelijk zijn (dus dat je water hebt dat van alle vier kanten omringd is door bodem)
    #
    #   bbbbbbbbbbbb
    #   bbb wwww bbb
    #   bbb wwww bbb
    #   bbbbbbbbbbbb - zoiets bedoel ik met 'gesloten' meer


    # size is de grootte van het spelbord, het kon even goed len()
    # pos is de startpositie en is gelijk aan nul omdat je start te tellen aan het linker kant van het bord
    # aantal is in het begin gelijk aan 0 en bij elke nieuwe meer wordt die met 1 verhoogd

    size = len(W)
    pos=0
    aantal = 0

    # we gaan deze loop uitvoeren totdat pos gelijk wordt aan size (op het einde van de elke uitvoering van de loop, wordt pos met 1 verhoogd)
    while pos < size:
        # als er op huidige positie geen water is, gebeurt er niets en we kijken gewoon de volgende positie
        if W[pos] == 0:
            pos +=1

        # indien er op huidige positie wel water is, wil dat zeggen dat we een nieuwe meer zijn tegengekomen en dus aantal meeren wordt verhoogd met 1
        else:
            aantal += 1
            # we gaan naar de volgende positie
            pos +=1
            # we blijven gaan naar de volgende positie zolang er op de huidige positie water anawezig is (want dat wil zeggen dat het nog steeds over zelfde meer gaat)
            while pos < size and is_meer(pos, W):
                pos +=1

    # op het einde, geeft de functie totaal aantal meeren
    return aantal


def is_meer (i, W, B=None):
    # voor een bepaalde positie i, gaat deze functie checken, of er een meer op die positie aanwezig is

    # als het waterniveau in kolom i, niet gelijk is aan nul, dan is er een meer in kolom i, anders niet
    if W[i] != 0:
        return True

    else:
        return False


def start_eind_meer(i, W, B=None):

    # als gegeven kolom i, helemaal geen deel uitmaakt van een meer, returnt deze functie gewoon False
    if not is_meer(i, W):
        return False

    else:
        size=len(W)

        # we gaan telkens een stap meer naar links kijken of er een meer is en opslaan de laatste positie waar een meer is in variabele begin
        d = 1
        while i-d >=0 and is_meer(i-d, W):
            d += 1

        begin = i-d+1

        # er wordt dezelfde gedaan als hierboven, maar dan naar rechts
        d=1
        while i+d < size and is_meer(i+d, W):
            d +=1

        end= i+d-1

        return (begin,end)


def verdamp(i, W, B=None):

    # als er op gegeven positie i, geen water is, kan er niets verdampen, dus returnt deze functie gewoon False
    if not is_meer(i, W):
        return False

    else:
        # we berekenen de lengte van meer op positie i en slaan die lengte op in variabele len
        begin, end = start_eind_meer(i, W)
        len=end-begin

        # we verwangen stuk van de waterlijst waar meer was, door len keer 0 (dus alle elementen in die lijst waar meer was, zullen nu 0 worden)
        W[begin:end+1]=[0]*(len+1)
#
# print(rooster_naar_coord(20, (5, 2)))
# print(coord_naar_rooster(20, (85.7, 34.10)))
# print(aantal_meeren(water, bodem))
# print(is_meer(8, water, bodem))
# print(is_meer(11, water, bodem))
# print(start_eind_meer(8, water, bodem))
# verdamp(6, water, bodem)
# print(water)
# print(bodem)
# print("\n \n \n")
########################

#nieuwe bodem en water voorbeeldlijsten
bodem = [1,1,1,1,1,1,4,1,2,5,1,1,1]
water = [0,0,0,0,2,2,2,2,2,2,0,0,0]


def hoogteverschil(i,j, W, B):

    size = len(W)

    # hoogte op positie i is het aantal bodemblokjes in die kolom + het aantal waterblokjes
    # hoogte verschil is dan gewoon de hoogte op positie i - de hoogte op positie j
    if i>=0 and j>=0 and i<size and j<size:
        h= (B[i] + W[i]) - (B[j] + W[j])

        return h

    else:
        return False


def drukverschil_links(i, W, B):

    # we moeten een speciaal geval definieren waar we drukverschil checken voor de eerste (nulde) kolom
    # in dat geval is drukverschil van links gelijk aan -1 als er een water blokje is in de eerste kolom en 0 indien er geen water is in de eerste kolom
    if i == 0:
        if W[0] != 0:
            return -1
        else:
            return 0

    # voor alle andere gevallen is het drukverschil van links gelijk aan het aantal water blokjes op de positie i vermenigvuldigd met het hoogteverschil tussen positie i en i-1 (eerste van links dus)
    dvl = W[i]*hoogteverschil(i-1, i, W, B)
    return dvl

def drukverschil_rechts(i, W, B):

    # analoog aan drukverschil_links

    if i == len(W)-1:
        if W[len(W)-1] != 0:
            return -1
        else:
            return 0

    dvr = W[i]*hoogteverschil(i+1, i, W, B)
    return dvr


def nivellering_links_mogelijk(W,B):
    size=len(W)

    # er wordt voor alle kolommen gecheckt of het drukverschil naar links kleiner is dan 0 (want dat wil zeggen dat er in die kolom, nivellering naar links mogelijk is)
    for i in range(size):
        if drukverschil_links(i, W, B) < 0:
            return True

    return False

def nivellering_rechts_mogelijk(W,B):
    size=len(W)

    # analoog aan nivellering_links
    for i in range(size):
        if drukverschil_rechts(i, W, B) < 0:
            return True

    return False

def niveller(W, B):
    size=len(W)
    #Wtotal is totaal hoeveelheid water op het bord voor dat de nivellering wordt uitgevoerd
    Wtotal = sum(W)

    # de loop wordt uigevoerd zolang er een kolom is die naar links kan genivelleerd worden
    while nivellering_links_mogelijk(W, B):

        for i in range(size):
            # voor elke kolom waar er een negatieve drukvershil naar links is (d.w.z. water kan afstromen naar links)
            # wordt waterniveau in die kolom met 1 verlaagt en het niveau in de kolom naar links 1 groter
            # indien het over de meest linkse kolom gaat, wordt alleen het niveau in die kolom 1 lager
            if drukverschil_links(i, W, B) < 0:
                W[i] -= 1
                if i != 0:
                    W[i-1] += 1

    # analoog aan de loop hierboven voor nivellering_links_mogelijk
    while nivellering_rechts_mogelijk(W, B):

        for i in range(size):
            if drukverschil_rechts(i, W, B) < 0:
                W[i] -= 1
                if i < size-1:
                    W[i+1] += 1

    # Wcurrent is de hoevelheid water op het bord na dat de nivellering is uigevoerd
    Wcurrent = sum(W)

    # de functie return verschil in het water op het bord voor en na de uitvoering van de functie > dat is hoevelheid water dat is afgestroomd
    return (Wtotal - Wcurrent)


# print(hoogteverschil(7,8, water, bodem))
# print(drukverschil_links(8, water, bodem))
# print(hoogteverschil(9,8, water, bodem))
# print(drukverschil_rechts(8, water, bodem))
# print(nivellering_links_mogelijk(water, bodem))
# print(niveller(water,bodem))
# print(water)
