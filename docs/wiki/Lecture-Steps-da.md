[English](Lecture-Steps) · **Dansk** · [Bahasa Melayu](Lecture-Steps-ms)

# Trin i lektionen

Dag 62-opgavens ni krav. Hvert trin har et skærmbillede og hvad vi lærte.

## Trin 1: Forsiden bruger `css/styles.css`

![Den stylede forside](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/062-coffee-and-wifi/raw/branch/main/docs/screenshots/01-home-page.png)

**Hvad vi lærte:** skabelonarv. `base.html` indlæser Bootstrap-Flasks CSS med `bootstrap.load_css()` og linker vores egen `styles.css` med `url_for('static', filename=...)`; alle sider, der udvider den, får samme udseende.

## Trin 2: `/cafes` viser en Bootstrap-tabel med CSV-data

![Tabellen over caféer](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/062-coffee-and-wifi/raw/branch/main/docs/screenshots/02-cafes-table.png)

**Hvad vi lærte:** at læse en CSV-fil med modulet `csv`, give rækkerne videre til en skabelon og løbe dem igennem med Jinja. Bootstrap-klasserne `table table-dark table-striped table-hover` giver tabellen sit udseende uden ekstra CSS.

## Trin 3: Placeringer bliver til "Maps Link"

![Kolonnen Maps Link](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/062-coffee-and-wifi/raw/branch/main/docs/screenshots/03-maps-links.png)

**Hvad vi lærte:** en lille regel (en værdi, der starter med `http`, er et link), som står ét sted, så skabelonen kun afgør, hvordan en celle vises, ikke hvad den betyder.

## Trin 4: "Show Me!" fører til café-siden

![Café-siden efter et klik på knappen](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/062-coffee-and-wifi/raw/branch/main/docs/screenshots/04-show-me-button.png)

**Hvad vi lærte:** `url_for('cafes')` bygger et link ud fra funktionens navn, så en rute kan skifte sti uden at ødelægge linkene.

## Trin 5: Den hemmelige `/add`-rute viser formularen

![Formularen til at tilføje en café](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/062-coffee-and-wifi/raw/branch/main/docs/screenshots/05-secret-add-form.png)

**Hvad vi lærte:** en rute, som intet linker til. En Flask-WTF `FlaskForm` erklærer felterne (tekstfelter og `SelectField` til vurderingerne), og Bootstrap-Flasks `render_form` tegner hele formularen i Bootstrap-stil.

## Trin 6: Placeringsfeltet validerer URL'en

![Valideringsfejl for URL](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/062-coffee-and-wifi/raw/branch/main/docs/screenshots/06-url-validation-error.png)

**Hvad vi lærte:** WTForms-validatorer (`DataRequired`, `URL`). Browserens validering er slået fra med `novalidate`, så det er serverens kontrol og dens besked, du ser. Formularen skal bruge en hemmelig nøgle til CSRF-beskyttelse; den læses fra miljøet og står aldrig i koden.

## Trin 7: En gyldig indsendelse tilføjer caféen

![Den nye café i tabellen](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/062-coffee-and-wifi/raw/branch/main/docs/screenshots/07-cafe-added.png)

**Hvad vi lærte:** `validate_on_submit()` og redirect efter POST: efter en vellykket gemning sendes browseren til `/cafes`, så en opdatering ikke indsender formularen to gange.

## Trin 8: Caféen tilføjes til `cafe-data.csv`

![Slutningen af CSV-filen](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/062-coffee-and-wifi/raw/branch/main/docs/screenshots/08-csv-appended.png)

**Hvad vi lærte:** at tilføje med tilstanden `"a"` og `csv.writer`, som sætter citationstegn om et navn med komma. Filhåndteringen ligger i en repository-klasse bag en grænseflade, så use casen kan testes uden en fil.

## Trin 9: Alle navigationslinks virker

![Tilføj-siden med sit link](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/062-coffee-and-wifi/raw/branch/main/docs/screenshots/09-navigation-links.png)

**Hvad vi lærte:** alle links bygges med `url_for`, og en end-to-end-test følger hvert `href` på siderne og kontrollerer, at det svarer 200, så et brudt link fanges af en test.
