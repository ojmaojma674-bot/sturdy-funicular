# Android APK Build Setup for VHOTIEX AI

## Prerequisites
- Android Studio
- JDK 17
- Android SDK with API 34

## Local build
```bash
./gradlew assembleDebug
./gradlew assembleRelease
```

## Output
- app/build/outputs/apk/debug/app-debug.apk
- app/build/outputs/apk/release/app-release-unsigned.apk

## Release signing
Use a keystore before releasing publicly.

## GitHub Actions
A workflow can build the APK automatically and upload it as an artifact.
