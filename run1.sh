#!/usr/bin/env bash

###############################################################################
#
# Root Cause Analysis Agent
#
# Production Setup Script
#
###############################################################################

set -Eeuo pipefail

PROJECT_NAME="RootCauseAnalysisAgent"
VENV_NAME="rootcauseanalysisagent"
PYTHON_REQUIRED_MAJOR=3
PYTHON_REQUIRED_MINOR=11

###############################################################################
# Colors
###############################################################################

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

###############################################################################
# Logging Helpers
###############################################################################

info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

###############################################################################
# Error Handler
###############################################################################

trap 'error "Setup failed on line $LINENO"; exit 1' ERR

###############################################################################
# Check Python
###############################################################################

info "Checking Python installation..."

if command -v python3 >/dev/null 2>&1; then
    PYTHON=python3
elif command -v python >/dev/null 2>&1; then
    PYTHON=python
else
    error "Python not found."
    exit 1
fi

###############################################################################
# Check Version
###############################################################################

VERSION=$($PYTHON -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")

MAJOR=$(echo "$VERSION" | cut -d. -f1)
MINOR=$(echo "$VERSION" | cut -d. -f2)

if [[ "$MAJOR" -lt "$PYTHON_REQUIRED_MAJOR" ]] || \
   [[ "$MAJOR" -eq "$PYTHON_REQUIRED_MAJOR" && "$MINOR" -lt "$PYTHON_REQUIRED_MINOR" ]]; then

    error "Python 3.11 or newer is required."

    exit 1
fi

success "Python Version: $VERSION"

###############################################################################
# Create Virtual Environment
###############################################################################

if [[ ! -d "$VENV_NAME" ]]; then

    info "Creating virtual environment..."

    "$PYTHON" -m venv "$VENV_NAME"

    success "Virtual environment created."

else

    warning "Virtual environment already exists."

fi

###############################################################################
# Activate
###############################################################################

source "$VENV_NAME/bin/activate"

###############################################################################
# Upgrade Pip
###############################################################################

info "Upgrading pip..."

python -m pip install --upgrade pip setuptools wheel

###############################################################################
# Install Requirements
###############################################################################

info "Installing dependencies..."

pip install -r requirements.txt

###############################################################################
# Verify Imports
###############################################################################

info "Verifying installed packages..."

python <<EOF
import pandas
import yaml
import openai
import jinja2
import rich
import tqdm
import duckdb
import networkx
print("Dependency verification successful.")
EOF

###############################################################################
# Create Project Directories
###############################################################################

info "Creating project folders..."

mkdir -p input
mkdir -p output
mkdir -p workspace
mkdir -p logs
mkdir -p prompts
mkdir -p config
mkdir -p tests

###############################################################################
# Finished
###############################################################################

echo
echo "============================================================"
echo "Setup Completed Successfully"
echo "============================================================"
echo

echo "Virtual Environment"

echo "    $VENV_NAME"

echo

echo "Activate"

echo "    source $VENV_NAME/bin/activate"

echo

echo "Run"

echo "    python analyze.py --help"

echo

success "Ready to start development."
