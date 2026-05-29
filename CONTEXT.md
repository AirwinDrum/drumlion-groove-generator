# Drumlion Groove Generator — Project Context

## Owner
Erwin Eitsen — Drumlion brand

## Working File
- **Edit here:** `/Users/erwineitsen/Desktop/Projekte/Drumlion/groove-generator/index.html`
- **Dev preview (immer synchron halten):** `/Users/erwineitsen/Downloads/drumlion_groove_generator_v6.html`
  - Nach jeder Änderung: `cp /Users/erwineitsen/Desktop/Projekte/Drumlion/groove-generator/index.html /Users/erwineitsen/Downloads/drumlion_groove_generator_v6.html`
- **GitHub:** AirwinDrum/drumlion-groove-generator (private)
- **Netlify:** Auto-deploys from GitHub (only deploy when user explicitly says "deploy" or "push")

## Tech Stack
- Single HTML file — all CSS, JS, SVG notation, base64 MP3s embedded
- No framework, no build step
- localStorage key: `drumlion_v4_course`
- 28 MP3 drum sounds embedded as base64

## Drum Sound Files
Located at: `/Users/erwineitsen/Desktop/Projekte/Drumlion/Drumlion Sounds/Drumlion Aiff Sounds/*.mp3`

## MuseScore Source Files
- `/Users/erwineitsen/Desktop/Projekte/Drumlion/Lifetime Course /Fills/Fill 1 - 10 (Quarter Fills).mscz`
- `/Users/erwineitsen/Desktop/Projekte/Drumlion/Lifetime Course /Fills/Fill 2 - 30 (Eigth Note Fills.mscz`
- Rudiments: not yet received

## Notation System
- SVG-based, custom renderer
- Line positions (1=top, 5=bottom of staff):
  - crash1: -1.5 (above staff), head: circledX
  - hh: -0.5 (above staff), head: x
  - tom1: 0.5, head: oval
  - tom2: 1.0, head: oval
  - snare: 1.5, head: oval
  - tom3: 2.5 (between lines 3-4), head: oval
  - kick: 3.5, head: oval
  - kick2: 4.0, head: oval
  - hhPedal: 5.5 (below staff), head: x
- 2-bar fill layout: GROOVE bar left + FILL bar right, continuous staff lines
- Labels only on fill notes (at/after fillStart index), never on groove bar
- Stickings rendered below fill notes

## Course System
- Categories: grooves (1-20), fillins (1-30), rudiments (1-40)
- EXERCISE IDs: grooves 1-20, fillins 21-50, rudiments (TBD)
- Rep counter = bpmStep (not play count)
- Mark as Completed: fade transition, no auto-start
- Distribution algorithm: boost sequence, G→F interleaved

## MVP Scope (pre-launch)
- 20 Grooves ✓
- 20 Fills (partially done — notation complete, stickings partially missing)
- 2 Rudiments (files not yet received)

## Open — Code/Generator
- [ ] Drumkey-Legende bauen (korrekte Notenköpfe + Bezeichnungen)
- [ ] Speed-Tabelle: exakt aus Numbers-Datei als JSON exportieren — NIEMALS interpolieren
- [ ] iFrame-Einbindung mit URL-Parametern für Hosting
- [ ] Eigene Drum-Samples ersetzen Platzhalter (bereits erledigt für 28 Sounds)
- [ ] Stickings für Fills 1-10 (Quarter Fills) — noch null
- [ ] Stickings für Fills 15-25, 27, 29-30 (Eighth Fills) — noch null
- [ ] Rudiments 1-40 notation (MuseScore-Dateien fehlen noch)
- [ ] Video-Integration: videoUrl-Feld + Player-UI
- [ ] "Un-complete" a lesson (state rollback)
- [ ] Song-Rotation (1 per 10h played)
- [ ] Theme-System (Kids, Medieval, Steampunk, Dark)

## Open — Vor Launch
- [ ] Systeme.io Kursstruktur entfernen — Groove Generator als iFrame einbetten (Login-Schutz bleibt über Systeme.io)
- [x] USt-IdNr eintragen: Impressum, Stripe, PayPal (DE410250170)
  - [x] Systeme.io ✓ (Sales invoice footer)
  - [x] Impressum HTML ✓
- [ ] Cookiebot-Abschnitt in Privacy Policy ergänzen
- [ ] Launch-Emails senden (3 Newsletter-Emails vorbereitet, noch nicht gesendet)
- [ ] Launch-Datum festlegen
- [ ] Adressänderung ab 01.08.2026 beachten: BOP/BZSt, Finanzamt, Impressum, Stripe, PayPal, Systeme.io, **Accountable**

## Langfristiges Ziel: 50.000€/Monat
- Drumlion Abo (1.000-1.500 Member) → ~15-20k/mo
- YouTube AdSense (500k+ Views/mo) → ~2-5k/mo
- YouTube Sponsorings → ~3-10k/mo
- Merch → ~2-5k/mo
- Premium Drumpad (200€/Stück, 25-50/mo) → ~5-10k/mo
- Affiliate/Kooperationen → ~2-5k/mo
→ **Nach Launch: Langfristige Strategie ausarbeiten**

## Roadmap 2026
- **Launch 01.06.** — Groove Generator als iFrame in Systeme.io, Login über Systeme.io Membership
- **Ende 2026** — Eigene App-Lösung: Login, serverseitiger Fortschritt (geräteübergreifend), kein Systeme.io mehr

## Open — Steuer / Finanzen
- [x] USt-IdNr: **DE410250170**
- [x] OSS-Verfahren angemeldet (28.05.2026)
  - Transferticket: **ep1480yomq02ot2kgh4s8hbg1hskd0qd**
  - Registrierungsbeginn: **01.06.2026**
  - Steuernummer: 08/036/53123 (Finanzamt Bingen-Alzey)
- [ ] OSS-Verfahren anmelden (BZSt) — für digitale Produkte an EU-Privatkunden
- [ ] Geschäftskonto einrichten — Kontist (Konto + auto. Steuerrücklage) oder Qonto
- [ ] Accountable einrichten (Buchhaltung + Steuer, integriert mit Kontist)
- [ ] Ab ~60-80k Gewinn: UG/GmbH prüfen (Steueroptimierung Gehalt vs. Gewinn)
- [ ] Steuerberater als Kontrolleur einschalten (Spezialisierung: Online-Business / digital)

## Open — Nach Launch
- [ ] DSGVO-Audit komplett (#3)
- [ ] Sicherheit: Rate limiting, Input-Validierung, HTTPS-Only, Auth-Absicherung
- [ ] Backups: Automatische DB-Snapshots, Disaster-Recovery
- [ ] Churn-Rate-Strategie (#5)
- [ ] Lead-Strategie + Content-Pillars (#7)
- [ ] drumXperiments Series (#9)
- [ ] Affiliate-Programm evaluieren (#16)
- [ ] A/B-Testing aufsetzen (#17)
- [ ] Kunden-Settings-Bereich optimieren (#18)
- [ ] "Find your Drumlion Level" Einstufungstest (#20)
- [ ] User Accounts / Auth (post-launch)

## Rules
- NEVER deploy to Netlify unless user explicitly says "deploy" or "push"
- NEVER interpolate the Speed-Tabelle — always export exact values from Numbers file
- Always develop locally first, test in browser, then deploy on request
- UI text always white, fonts large enough to read
- Tom 3 = old Tom 4 (MIDI 43/41), Tom 3 removed entirely
- Counts: 1-bar = 8 eighth-note positions; 2-bar fills = groove bar + fill bar

## Rudiment Distribution (NOT YET IMPLEMENTED)
- Rudiments join the NORMAL intro rotation (lessons-based like grooves/fills)
- But only start being introduced at Level 3 (= 200h)
- BPM range of each rudiment is calibrated so all rudiment lessons END around Level 100
- The 40 rudiments are spread evenly through the intro queue from Level 3 onward
- Implementation: filter rudiments out of _introQueue until player reaches Level 3 (200h)
