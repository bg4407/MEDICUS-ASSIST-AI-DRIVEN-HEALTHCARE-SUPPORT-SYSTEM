# Get the directory of the script
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition

# Path to the specific Python 3.11.9 executable
$PythonPath = "C:\Users\Borneil\AppData\Local\Programs\Python\Python311\python.exe"

# Check if Python 3.11.9 is installed
& $PythonPath --version
if ($LASTEXITCODE -ne 0) {
    Write-Host "Python 3.11.9 is not installed at $PythonPath. Please install Python 3.11.9 before running this script."
    exit 1
}

# Check the exact version of the installed Python
$PythonVersion = & $PythonPath -c "import sys; print('.'.join(map(str, sys.version_info[:3])))"
if ($PythonVersion -ne "3.11.9") {
    Write-Host "Python 3.11.9 is not installed at $PythonPath. Found version: $PythonVersion"
    exit 1
}

# Navigate to the script directory
cd $ScriptDir

# Remove existing virtual environment
if (Test-Path -Path "$ScriptDir\venv") {
    Remove-Item -Recurse -Force "$ScriptDir\venv"
}

# Create a new virtual environment with Python 3.11.9
& $PythonPath -m venv --upgrade-deps "$ScriptDir\venv"

# Activate the virtual environment
& "$ScriptDir\venv\Scripts\Activate"

# Install dependencies
pip install -r "$ScriptDir\requirements.txt"

Write-Host "Virtual environment setup complete. Starting the server..."

# Start the server
Start-Process -NoNewWindow -FilePath "$ScriptDir\venv\Scripts\python.exe" -ArgumentList "$ScriptDir\backend\src\app.py"

Write-Host "Server started. To activate the virtual environment manually, run '$ScriptDir\venv\Scripts\Activate'"
