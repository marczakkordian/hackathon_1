# hackathon_1
13.03.2021

1. Opis problemu

Stworzenie programu, który podczas uruchomienia będzie miał wsad inicjalny i będzie umożliwiał wyświetlenie
danych adresowych (Imię, nawzisko, nr telefonu) a także pozwalał na podstawowe modyfikacje danych: 
dodanie nowych wierszy, update, usunięcie.

2. Koncepcja rozwiązania

I. definicja tablicy dwuwymiarowej z danymi inicjalnymi.
   
II. definicja funkcji w progaramie:
- display all contacts: join gdy lista nie jest pusta, Info warning gdy lista jest pusta + dodanie wartości +1 w indexie aby nie był od zera i czytelniejszy dla usera
- add new contact : append
- update contact : wyszukanie wiersza do update'u, user_index -1 aby usuwało się to co potrzeba, instrukcja z wyborem która kolumna ma być zmieniona
- remove contact : list.pop
- remove all data : clear
- command list : wyświetlenie dla usera opcji na życzenia
- quit : brak
- (być może przydałby się też search)

III. definicja warunków w main part programu za pomocą pętli while i ciągu intrukcji if/elif

3. Opcjonalnie: opis obsługi programu, jeśli będziecie wykorzystywać dodatkowe biblioteki etc

Podczas pracy nad programem znalazłem informacje, że python ma dedykowaną bibliotekę do budowy UI (tkinter) ale
nie zdecydowałem się jej użyć z zerowym wcześniejszym doświadczeniem na jej temat.   

- dodałem funkcje update'u, usunięcia wszystkich danych
- dodałem printy w funkcjach w stylu log.info aby lepiej widzieć co się dzieje w programie (przykład: ---> Update contact is closed <----)