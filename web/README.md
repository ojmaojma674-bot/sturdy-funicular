# Installable Web App (PWA)

This folder contains a simple installable web package for the VHOTIEX AI app.

## Features
- Installable as a PWA
- Offline caching via service worker
- Dark futuristic UI
- Works in modern browsers
- Can be deployed to GitHub Pages, Netlify, Vercel, or any static host

## Run locally

```bash
cd web
python3 -m http.server 8000
```

Then open:

```text
http://localhost:8000
```

## Install from browser
1. Open the app in Chrome/Edge
2. Click the install button in the address bar
3. Or use the in-app Install App button

## Deploy to GitHub Pages
If you want GitHub Pages to serve the app:
1. In GitHub repo settings, enable Pages
2. Set source to `Deploy from a branch`
3. Choose branch `main`
4. Set folder to `/web`

Then your app will be available at:

```text
https://<username>.github.io/<repo>/
```

## Notes
This is a PWA package, not a native APK. For Android APK, you would need a wrapper like Capacitor or a native Android project.
