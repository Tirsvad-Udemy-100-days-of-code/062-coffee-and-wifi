**English** · [Dansk](Lecture-Steps-da) · [Bahasa Melayu](Lecture-Steps-ms)

# Lecture Steps

The nine requirements of the Day 62 assignment. Each step has a screenshot and what we gained from it.

## Step 1: The home page uses `css/styles.css`

![The styled home page](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/062-coffee-and-wifi/raw/branch/main/docs/screenshots/01-home-page.png)

**What we gained:** template inheritance. `base.html` loads Bootstrap-Flask's CSS with `bootstrap.load_css()` and links our own `styles.css` with `url_for('static', filename=...)`; every page that extends it gets the same look.

## Step 2: `/cafes` shows a Bootstrap table of the CSV

![The cafes table](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/062-coffee-and-wifi/raw/branch/main/docs/screenshots/02-cafes-table.png)

**What we gained:** reading a CSV file with the `csv` module, passing the rows to a template, and looping over them with Jinja. The Bootstrap classes `table table-dark table-striped table-hover` style the table without any extra CSS.

## Step 3: Locations become "Maps Link" anchors

![The Maps Link column](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/062-coffee-and-wifi/raw/branch/main/docs/screenshots/03-maps-links.png)

**What we gained:** a small rule (a value that starts with `http` is a link) kept in one place, so the template only decides how to show a cell, not what it means.

## Step 4: "Show Me!" goes to the cafes page

![The cafes page reached from the button](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/062-coffee-and-wifi/raw/branch/main/docs/screenshots/04-show-me-button.png)

**What we gained:** `url_for('cafes')` builds a link from the function's name, so a route can change its path without breaking the links.

## Step 5: The secret `/add` route shows the form

![The add form](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/062-coffee-and-wifi/raw/branch/main/docs/screenshots/05-secret-add-form.png)

**What we gained:** a route that nothing links to. A Flask-WTF `FlaskForm` declares the fields (text fields and `SelectField` for the ratings), and Bootstrap-Flask's `render_form` draws the whole form in Bootstrap style.

## Step 6: The location field validates the URL

![The URL validation error](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/062-coffee-and-wifi/raw/branch/main/docs/screenshots/06-url-validation-error.png)

**What we gained:** WTForms validators (`DataRequired`, `URL`). Browser validation is switched off with `novalidate`, so the server-side check and its message are the ones you see. The form needs a secret key for its CSRF protection; it is read from the environment, never hard-coded.

## Step 7: A valid submit adds the cafe

![The new cafe in the table](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/062-coffee-and-wifi/raw/branch/main/docs/screenshots/07-cafe-added.png)

**What we gained:** `validate_on_submit()` and redirect-after-POST: after a successful save the browser is sent to `/cafes`, so a refresh does not submit the form twice.

## Step 8: The cafe is appended to `cafe-data.csv`

![The end of the CSV file](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/062-coffee-and-wifi/raw/branch/main/docs/screenshots/08-csv-appended.png)

**What we gained:** appending with mode `"a"` and `csv.writer`, which quotes a name that contains a comma. The file handling lives in a repository class behind an interface, so the use case can be tested without a file.

## Step 9: All navigation links work

![The add page with its link](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/062-coffee-and-wifi/raw/branch/main/docs/screenshots/09-navigation-links.png)

**What we gained:** every link is built with `url_for`, and an end-to-end test follows every `href` on the pages and checks that it answers 200, so a broken link is caught by a test.
