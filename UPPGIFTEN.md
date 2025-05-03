# Exam_testverktyg
## Examination Testverktyg


Du ska lösa uppgiften självständigt. När du tar hjälp av AI, eller diskuterar med andra studerande, ska du se till att du förstår vad koden gör.

---

# Bakgrund
"Läslistan" är en webbsida där man kan välja ut sina favoriter från en 
katalog med böcker, eller lägga till nya. Beställaren är en organisation 
som vill öka barns och ungas läsande. Nuvarande version har begränsad 
funktionalitet. På sikt vill man utöka webbsidan med funktioner för:
- att dela sina listor, 
- skapa quiz 
- diskutera böcker med varandra. 

Därför är det viktigt att det finns tester för all grundläggande funktionalitet. 

Detta är din uppgift!

### Webbsidan som ska testas: 

- [Läslistan ](https://tap-ht24-testverktyg.github.io/exam-template/)


(För den som är intresserad av JavaScript och React finns källkoden i ett 
repo i kursens GitHub-organisation, alltså där alla kodexempel finns.)

Du ska ha en README.md fil i projektets rotmapp, där du berättar:
- vad du har testat,
- hur man startar projektet

Börja med att läsa igenom hela uppgiften.

# Detta ska du göra
- Skapa ett projekt med Python, pytest, Playwright och behave. 
- Gör ett motsvarande, publikt repo på GitHub. (Det är tillåtet att 
använda fler moduler.)
- Skapa filerna README.md och STORIES.md i projektets rotmapp. 
(Du får använda STORIES.txt om du hellre vill det.)
- Formulera user stories för den funktionalitet som finns på webbsidan idag.
Skriv ner dessa i STORIES.md.
- Ta fram feature-filer utifrån dina user stories.
- Bygg step-filer för alla features. Page-filer vid behov.
- Skriv ner 

    - Nu kan du lämna in! 
 
# Inlämning
  Skapa en textfil "exam1_mitt_namn.txt" som innehåller länk till ditt 
  projekt på GitHub. Ladda upp textfilen på LearnPoint. 
  
  Kom ihåg, det räcker inte med att ladda upp filen, du måste klicka 
  på knappen för att lämna in också!

----------------

# För G krävs
A) Det finns user stories som täcker all funktionalitet.

B) Alla user stories har minst en feature. Alla features har minst ett scenario.

C) Det går att starta ditt projekt, efter instruktionerna du har skrivit i README.md.

D) Alla test är gröna.

# För VG krävs
E) Högre kvalitet och kod som återanvänds.

F) Du använder designmönstret Page Object.

G) Du använder Scenario Outline.

H) Dina features försöker täcka alla meningsfulla möjligheter för 
motsvarande user story.


### Exempel på meningsfulla möjligheter: 
testa inte bara att det går att favoritmarkera, utan att det går att 
ta bort en favoritmarkering, och vad som händer om man klickar 
fler än två gånger.

-----

# Tips
- Flera element på sidan har ett testid som [du kan använda med Playwright](https://playwright.dev/docs/locators#locate-by-test-id).
- Använd headless när du kommit en bit och när du lämnar in uppgiften. 
  Det snabbar upp testandet rejält.
- Kom ihåg att testa att alla vyer gör det de ska, och att navigeringen fungerar.


-----

# Examinationsdatum
TAP HT24D
Testverktyg
Ordinarie inlämning: 2025-05-11
Komplettering 1: 2025-06-01
Komplettering 2: 2025-06-15
