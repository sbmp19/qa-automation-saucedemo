#!/usr/bin/env bash
# Ejecuta los tests y abre el reporte HTML automáticamente.
set -euo pipefail

REPORTE="reports/report.html"

echo "🔵 Ejecutando tests..."
.venv/bin/pytest

echo ""
echo "🔵 Abriendo reporte: $REPORTE"
open "$REPORTE"
