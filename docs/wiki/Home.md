**English** · [Dansk](Home-da) · [Bahasa Melayu](Home-ms)

# Coffee and Wifi

Day 62 of Udemy's "100 Days of Code: The Complete Python Pro Bootcamp". A small Flask site lists London cafes from a CSV file, and a secret `/add` form appends a new cafe.

## What is in this wiki

- [Getting Started](Getting-Started): create a `.venv`, install, run.
- [Lecture Steps](Lecture-Steps): the nine steps of the assignment, each with a screenshot and what we gained.
- [Testing](Testing): how the tests are organised and how to run them.

## The idea in one minute

1. `/` is a home page with a "Show Me!" button.
2. `/cafes` shows every cafe in a Bootstrap table; the location is a "Maps Link".
3. `/add` is secret (nothing links to it). It validates the form, including that the location is a URL, and appends one line to `cafe-data.csv`.

The repository README has the same screenshots; the project documents (business case, plan, milestones and reviews) are in the `docs/` folder.
