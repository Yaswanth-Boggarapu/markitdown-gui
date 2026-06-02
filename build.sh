#!/bin/bash
# ─────────────────────────────────────────────────────────────────────────────
# build.sh — Build MarkItDown.app and package it into a .dmg
# Run this on your Mac:  chmod +x build.sh && ./build.sh
# ─────────────────────────────────────────────────────────────────────────────

set -e

echo ""
echo "╔════════════════════════════════════════╗"
echo "║     MarkItDown GUI — macOS Builder     ║"
echo "╚════════════════════════════════════════╝"
echo ""

# ── 0. Check we're on macOS ───────────────────────────────────────────────────
if [[ "$(uname)" != "Darwin" ]]; then
  echo "❌  This script must be run on macOS."
  exit 1
fi

# ── 1. Check Python ───────────────────────────────────────────────────────────
echo "▸ Checking Python..."
python3 --version || { echo "❌  python3 not found. Install from python.org"; exit 1; }

# ── 2. Install dependencies ───────────────────────────────────────────────────
echo ""
echo "▸ Installing Python dependencies..."
pip3 install --break-system-packages --upgrade \
  "markitdown[all]" \
  pyinstaller \
  dmgbuild

# ── 3. Clean previous build ───────────────────────────────────────────────────
echo ""
echo "▸ Cleaning previous build artifacts..."
rm -rf build dist MarkItDown.dmg

# ── 4. Build .app with PyInstaller ───────────────────────────────────────────
echo ""
echo "▸ Building MarkItDown.app with PyInstaller..."
pyinstaller markitdown.spec --noconfirm

APP_PATH="dist/MarkItDown.app"

if [ ! -d "$APP_PATH" ]; then
  echo "❌  Build failed — MarkItDown.app not found in dist/"
  exit 1
fi

echo "✅  MarkItDown.app built successfully"

# ── 5. Create DMG ────────────────────────────────────────────────────────────
echo ""
echo "▸ Creating MarkItDown.dmg..."

cat > /tmp/dmg_settings.py << 'DMGEOF'
import os

application = defines.get('app', 'dist/MarkItDown.app')
appname = os.path.basename(application)

files = [application]
symlinks = {'Applications': '/Applications'}

badge_icon = application
background = 'builtin-arrow'

icon_locations = {
    appname:        (140, 120),
    'Applications': (500, 120),
}

window_rect = ((100, 100), (660, 280))
icon_size = 100
text_size = 14
DMGEOF

dmgbuild \
  -s /tmp/dmg_settings.py \
  -D app="$APP_PATH" \
  "MarkItDown" \
  "MarkItDown.dmg"

echo ""
echo "╔════════════════════════════════════════╗"
echo "║  ✅  Done!  →  MarkItDown.dmg ready   ║"
echo "╚════════════════════════════════════════╝"
echo ""
echo "  Double-click MarkItDown.dmg to install."
echo "  Drag MarkItDown.app into Applications."
echo ""
