#!/usr/bin/env sh
##
# A simple upload script for the test app.
# Remove old files that usually cause problems
# Uploads the libs and the app to the board and starts it
# Starts the REPL
#
# You already should have micropython installed on the board.
#
# Jens Dede <jd@comnets.uni-bremen.de>
# 

echo "Usage:"
echo ""
echo "./upload.sh         Autodetect the port. Upload everything and start the REPL"
echo "./upload <comport>  Use the specific comport for the described actions"

if command -v uv >/dev/null 2>&1; then
    echo "uv installed. We can continue"
else
    echo "Error: This script uses uv. Check the project README for further details."
    echo "Aborting..."
    exit 1
fi

#echo "Performing a soft-reset"
#uv run mpremote connect $1 soft-reset

#echo "List files on the connected device"
#uv run mpremote connect $1 fs ls

echo "Removing lib, main.py and boot.py to ensure we have a clean system"
uv run mpremote connect $1 fs rm -rf lib libs
uv run mpremote connect $1 fs rm -rf main.py
uv run mpremote connect $1 fs rm -rf boot.py

echo "Now, we upload the current version of this code..."

uv run mpremote connect $1 cp main.py :main.py

uv run mpremote connect $1 fs mkdir lib
for f in $(ls lib/*.py); do
    l=$(basename $f)
    uv run mpremote connect $1 cp $f :lib/$l
done

echo "Showing prompt. Do not forget to restart the device using <CTRL>+d"

uv run mpremote connect $1 repl


