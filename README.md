# dataframe.uk

Website for Dataframe Limited. Plain HTML, CSS and JavaScript with no build step, hosted on GitHub Pages from the `docs/` folder.

## What's where

| Path | Contents |
|------|----------|
| `content/website-copy.md` | Approved website copy (the source for all page text) |
| `docs/` | The published site: everything in here goes live |
| `docs/index.html` | Home page (all sections) |
| `docs/privacy.html` | Privacy Policy |
| `docs/404.html` | "Page not found" page |
| `docs/assets/css/styles.css` | All styles. Colours, fonts and spacing are tokens at the top of the file |
| `docs/assets/js/main.js` | Mobile menu, clickable table rows, "Copy address" button |
| `docs/assets/fonts/` | Self-hosted fonts (SIL Open Font Licence, licence files included) |
| `docs/CNAME` | Custom domain for GitHub Pages (`dataframe.uk`) |
| `design/` | Sources for the social share image and app icon |

## Preview locally

```bash
python3 -m http.server 8000 --directory docs
```

Then open http://localhost:8000.

## Before launch

The site has no forms and collects no information. Visitors contact you by emailing `inquiries@dataframe.uk`.

1. **Email.** Check that `inquiries@dataframe.uk` exists in Microsoft 365 (the domain's mail is hosted there) and receives mail.
2. **LinkedIn.** Uncomment the LinkedIn row in the contact card in `index.html` and add the URL.
3. **Privacy Policy.** Check it against how you actually handle email, in particular the 24-month retention period.
4. **Claims to confirm:** "Vendor-neutral" / "Independent advice", the five ways to work with you, the "within one working day" reply promise, and the FAQ answer on who owns the work.

Company details (number 13975651, England and Wales, registered office) come from the [Companies House record](https://find-and-update.company-information.service.gov.uk/company/13975651). They appear in the footer of every page, the contact card and the Privacy Policy. If the registered office moves, search for `Great Portland` and update each one.

## Publish on GitHub Pages

1. Push `main` to `github.com/DataframeUK/dataframe_uk`.
2. In the repository, go to **Settings → Pages**. Under **Build and deployment**, choose **Deploy from a branch**, then branch `main` and folder `/docs`. Save.
3. **Custom domain** should show `dataframe.uk` (it is read from `docs/CNAME`). If it doesn't, enter it and save.
4. Once DNS is working (next section) and GitHub has issued the certificate, tick **Enforce HTTPS**.

GitHub Pages on a private repository needs a paid GitHub plan. On the free plan the repository must be public.

### Verify the domain (recommended)

Verifying the domain stops anyone else from pointing a GitHub Pages site at it.

1. Go to the **DataframeUK** organisation's **Settings → Pages → Add a domain**, and enter `dataframe.uk`.
2. GitHub shows a TXT record (name starting `_github-pages-challenge-`). Add it in GoDaddy as below, then click **Verify**.

## Point dataframe.uk at GitHub (GoDaddy)

In GoDaddy, open **My Products → dataframe.uk → DNS**.

1. Delete the existing **A** record for `@` (usually GoDaddy's "Parked" address), and turn off any **Forwarding** on the domain.
2. Add four **A** records, name `@`:
   - `185.199.108.153`
   - `185.199.109.153`
   - `185.199.110.153`
   - `185.199.111.153`
3. Optional, for IPv6: add four **AAAA** records, name `@`:
   - `2606:50c0:8000::153`
   - `2606:50c0:8001::153`
   - `2606:50c0:8002::153`
   - `2606:50c0:8003::153`
4. Edit the **CNAME** record named `www` so it points to `dataframeuk.github.io`.
5. Leave **MX** and other email records alone. Your email runs on Microsoft 365 (`dataframe-uk.mail.protection.outlook.com`), and changing these would stop it.

Changes usually take effect within an hour, but can take up to 48 hours. To check:

```bash
dig dataframe.uk +noall +answer
```

When both records are in place, GitHub sends `www.dataframe.uk` to `dataframe.uk` automatically.

## Updating the share image and icon

`docs/assets/img/og-image.png` (1200 × 630, used when the link is shared on LinkedIn, Slack and so on) and `docs/assets/img/apple-touch-icon.png` (180 × 180) are rendered from `design/og-image.html` and `design/icon.html`. Serve the repository root (`python3 -m http.server 8000`), open each file at its stated size, and take a screenshot (Chrome DevTools → device toolbar → "Capture screenshot"). Scale the icon down to 180 × 180.
