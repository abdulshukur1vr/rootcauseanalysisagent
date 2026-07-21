#!/usr/bin/env bash

###############################################################################
#
# Root Cause Analysis Agent
#
# Local Development Setup
#
###############################################################################

set -Eeuo pipefail


PROJECT_ENV="rootcauseanalysisagent"
PYTHON_MIN_MAJOR=3
PYTHON_MIN_MINOR=11


RED="\033[0;31m"
GREEN="\033[0;32m"
YELLOW="\033[1;33m"
BLUE="\033[0;34m"
RESET="\033[0m"


log()
{
    echo -e "${BLUE}[INFO]${RESET} $1"
}


success()
{
    echo -e "${GREEN}[SUCCESS]${RESET} $1"
}


warn()
{
    echo -e "${YELLOW}[WARNING]${RESET} $1"
}


fail()
{
    echo -e "${RED}[ERROR]${RESET} $1"
    exit 1
}


trap 'fail "Setup failed at line $LINENO"' ERR


###############################################################################
# Python Check
###############################################################################

log "Checking Python installation"


if command -v python3 >/dev/null 2>&1
then
    PYTHON=python3
else
    fail "python3 not found"
fi


VERSION=$(
$PYTHON -c \
"import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')"
)


MAJOR=$(echo "$VERSION" | cut -d. -f1)
MINOR=$(echo "$VERSION" | cut -d. -f2)


if [[ "$MAJOR" -lt "$PYTHON_MIN_MAJOR" ]] ||
   [[ "$MAJOR" -eq "$PYTHON_MIN_MAJOR" &&
      "$MINOR" -lt "$PYTHON_MIN_MINOR" ]]
then
    fail "Python 3.11+ required. Found $VERSION"
fi


success "Python version $VERSION"


###############################################################################
# Virtual Environment
###############################################################################

if [[ ! -d "$PROJECT_ENV" ]]
then

    log "Creating virtual environment"

    $PYTHON -m venv "$PROJECT_ENV"

else

    warn "Virtual environment already exists"

fi


source "$PROJECT_ENV/bin/activate"


###############################################################################
# Dependencies
###############################################################################

log "Updating pip"

python -m pip install --upgrade pip setuptools wheel


log "Installing dependencies"

pip install -r requirements.txt


###############################################################################
# Directory Setup
###############################################################################

log "Creating runtime directories"


mkdir -p \
input \
workspace \
output \
logs \
config


###############################################################################
# Dependency Validation
###############################################################################

log "Validating dependencies"


python <<EOF

import yaml
import pandas
import openai
import rich

print("Dependency validation successful")

EOF


success "Environment ready"


echo

echo "Activate environment:"
echo

echo "source ${PROJECT_ENV}/bin/activate"

echo

echo "Run:"
echo

echo "python analyze.py --help"

