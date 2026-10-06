# UK &amp; Ireland Racecourse Weather &amp; Going

A single-page site showing the daily **weather forecast** for all 86 UK &amp;
Ireland racecourses, plus the **official going** for every course with a
fixture in the next 7 days.

- **Weather** comes live from the free [Open-Meteo API](https://open-meteo.com)
  (no key needed) when you open the page.
- **Going** is the official ground condition from
  [Sporting Life](https://www.sportinglife.com/racing/going), refreshed every
  30 minutes by a GitHub Action and saved into `going_data.js`.

## Live site

Once GitHub Pages is enabled (see below), the site is at:

```
https://<your-username>.github.io/<repo-name>/
```

## How it works

| Piece | What it does |
|-------|--------------|
| `index.html` | The web page. Fetches weather in the browser and reads going from `going_data.js`. |
| `fetch_going.py` | Downloads the going from Sporting Life and writes `going.json` + `going_data.js`. |
| `racecourses.py` | Coordinates and country for all 86 racecourses. |
| `.github/workflows/update-going.yml` | Runs `fetch_going.py` every 30 minutes and commits the fresh going. |

The weather updates live every time the page loads. The going is a snapshot
that the GitHub Action keeps fresh, so the hosted site stays up to date
without anyone running anything.

## Enabling GitHub Pages

1. Push these files to a new GitHub repository.
2. In the repo, go to **Settings &rarr; Pages**.
3. Under **Build and deployment**, set **Source** to **Deploy from a branch**.
4. Choose branch **main** and folder **/ (root)**, then **Save**.
5. Wait a minute, then open the URL shown on that Pages screen.

## The going auto-refresh (GitHub Action)

The workflow in `.github/workflows/update-going.yml` runs every 30 minutes on
GitHub's servers, fetches the latest going, and commits it. No local machine
needs to be on.

- To refresh manually: open the **Actions** tab, pick **Update going**, and
  click **Run workflow**.
- The first scheduled run may take up to ~30 minutes to kick in after the repo
  is created.

## Running locally (optional)

You can also refresh the going on your own machine:

```bash
pip install -r requirements.txt
python fetch_going.py
```

Then open `index.html` in a browser.

## Credits

Weather by [Open-Meteo](https://open-meteo.com). Going by
[Sporting Life](https://www.sportinglife.com/racing/going).
