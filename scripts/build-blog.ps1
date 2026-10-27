$ErrorActionPreference = 'Stop'
Write-Host "Running Python build script for full Markdown and UTF-8 support..."
python "$PSScriptRoot\build-blog.py"
