# fabrykaTestowDS
Fabryka Testów - kurs Python + Selenium (TAPS 2.0)

* moduł 5: Selenium - wstęp
* moduł 6: Selenium - rozwinięcie
* moduł 7: Selenium - testy kontrolek, prosta strona internetowa (https://simpletestsite.fabrykatestow.pl/)
* moduł 8: Selenium - testy, sklep internetowy (https://tapsshop.pl/)
  * Page Object Pattern
  * testy zakładki "Koszyk":
    * dodawanie/usuwanie produktów z koszyka
    * cofnięcie usuwania produktów z koszyka
    * zmiana ilości produktów w koszyku
    * sprawdzenie poprawności cen w koszyku
  * testy zakładki "Moje Konto":
    * logowanie/rejestracja użytkownika
    * wysyłanie przypomnienia hasła
    * sprawdzenie niepoprawnych linków - polityka prywatności
  * testy zakładki "Sklep":
    * sortowanie produktów po cenie rosnąco/malejąco
    * wyszukiwanie produktów po nazwie
  * testy E2E:
    * przejście całego procesu zakupowego
    * sprawdzenie cen i informacji w podsumowaniu zamówienia
* moduł 9: Selenium Grid - konfiguracja hub'a i node'a za pomocą plików konfiguracyjnych *.json, *.toml
  * hub:
    * java -jar selenium-server-4.17.0.jar hub --config hubConfig.json
    * java -jar selenium-server-4.17.0.jar hub --config hubConfig.toml
  * node:
    * java -jar selenium-server-4.17.0.jar node --config nodeConfig.json
    * java -jar selenium-server-4.17.0.jar node --config nodeConfig.toml
