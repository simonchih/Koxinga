#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")"

PYTHON="${PYTHON:-python3}"
"$PYTHON" -c 'import platform, sys; assert sys.platform == "darwin" and platform.machine() == "arm64", "Build requires native arm64 Python on macOS"'
"$PYTHON" -m PyInstaller --clean --noconfirm koxinga.spec
/usr/bin/file dist/koxinga
test "$(/usr/bin/lipo -archs dist/koxinga)" = arm64
echo "Built standalone macOS arm64 executable: $(pwd)/dist/koxinga"
