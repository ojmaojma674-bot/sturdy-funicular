#!/usr/bin/env bash
set -euxo pipefail

export DEBIAN_FRONTEND=noninteractive

sudo apt-get update
sudo apt-get install -y --no-install-recommends \
  unzip \
  wget \
  libc6-i386 \
  lib32stdc++6 \
  zlib1g:i386 \
  libncurses5

ANDROID_SDK_ROOT="/opt/android-sdk"
mkdir -p "$ANDROID_SDK_ROOT/cmdline-tools"

if [ ! -d "$ANDROID_SDK_ROOT/cmdline-tools/latest" ]; then
  cd /tmp
  wget -q "https://dl.google.com/android/repository/commandlinetools-linux-11076708_latest.zip" -O cmdline-tools.zip
  rm -rf /tmp/android-sdk-tools
  mkdir -p /tmp/android-sdk-tools
  unzip -q cmdline-tools.zip -d /tmp/android-sdk-tools
  rm -rf "$ANDROID_SDK_ROOT/cmdline-tools/latest"
  mv /tmp/android-sdk-tools/cmdline-tools "$ANDROID_SDK_ROOT/cmdline-tools/latest"
fi

yes | "$ANDROID_SDK_ROOT/cmdline-tools/latest/bin/sdkmanager" --sdk_root="$ANDROID_SDK_ROOT" --licenses
"$ANDROID_SDK_ROOT/cmdline-tools/latest/bin/sdkmanager" --sdk_root="$ANDROID_SDK_ROOT" \
  "platform-tools" \
  "platforms;android-34" \
  "build-tools;34.0.0"

sudo tee /etc/profile.d/android-sdk.sh >/dev/null <<EOF
export ANDROID_HOME=/opt/android-sdk
export ANDROID_SDK_ROOT=/opt/android-sdk
export PATH="\$PATH:\$ANDROID_SDK_ROOT/cmdline-tools/latest/bin:\$ANDROID_SDK_ROOT/platform-tools:\$ANDROID_SDK_ROOT/build-tools/34.0.0"
EOF

sudo chown -R vscode:vscode "$ANDROID_SDK_ROOT" || true

printf '\nAndroid SDK setup complete.\n'
printf 'Run: ./gradlew assembleDebug\n'
