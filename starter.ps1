if (-Not (Test-Path "$env:USERPROFILE\scoop")) {
    Write-Output "Installing Scoop..."
    Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force
    Invoke-Expression (New-Object System.Net.WebClient).DownloadString('https://get.scoop.sh')
}

scoop update

if (-Not (Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Output "Installing Git..."
    scoop install git
}

if (-Not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Output "Installing Python..."
    scoop install python
    $env:Path += ";$((Get-Command python).Path)"
}

$repoUrl = "https://github.com/krbdtx/qa_hw_14.git"
$repoPath = "C:\path\to\clone\repository"

git clone $repoUrl $repoPath

Set-Location $repoPath

python -m venv venv

& .\venv\Scripts\Activate.ps1

pip install --upgrade pip
pip install -r requirements.txt

pytest

allure serve allure-results --clean -o allure-report

