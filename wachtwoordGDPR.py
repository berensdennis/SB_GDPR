from pcinput import getString
eerstekeer = getString("Is dit je eerste keer? ja/nee")
if eerstekeer == str("ja"):
    wachtwoordnieuw = getString("Geef een wachtwoord op")
    gebruikersnaam = getString("Geef uw gebruikersnaam op")
    wachtwoord = getString("geef uw wachtwoord op")
    if wachtwoord==wachtwoordnieuw and gebruikersnaam==str("Jolien"):
        print ("welkom Jolien")
    else:
        print("ik ken je niet")
else:
    wens = getString("Wens je het wachtwoord te wijzigen? ja/nee")
    if wens == str("ja"):
        wachtwoordnieuw = getString("Geef een wachtwoord op")
        gebruikersnaam = getString("Geef uw gebruikersnaam op")
        wachtwoord = getString("geef uw wachtwoord op")
        if wachtwoord==wachtwoordnieuw and gebruikersnaam==str("Jolien"):
                print ("welkom Jolien")
        else:
            print("ik ken je niet")
    else:
        gebruikersnaam = getString("Geef uw gebruikersnaam op")
        wachtwoord = getString("Wachtoord ingeven")
        if gebruikersnaam==str("Jolien") and wachtwoord==str("KnutselKnuts"):
                print("welkom Jolien")
        else:
                print("ik ken je niet.")
