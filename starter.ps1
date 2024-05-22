if (-Not (Test-Path "$env:USERPROFILE\scoop")) {
    Write-Output "Установка Scoop..."
    Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force
    Invoke-Expression (New-Object System.Net.WebClient).DownloadString('https://get.scoop.sh')
}

scoop update

if (-Not (Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Output "Установка Git..."
    scoop install git
}

if (-Not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Output "Установка Python..."
    scoop install python
    $env:Path += ";$((Get-Command python).Path)"
}

$repoUrl = "https://github.com/krbdtx/qa_hw_14.git"
$repoPath = "C:\path\to\clone\repository"

Write-Output "Клонирование репозитория..."
git clone $repoUrl $repoPath

Set-Location $repoPath

Write-Output "Создание виртуального окружения..."
python -m venv venv

Write-Output "Активация виртуального окружения..."
& .\venv\Scripts\Activate.ps1

Write-Output "Установка зависимостей..."
pip install --upgrade pip
pip install -r requirements.txt

Write-Output "Запуск тестов..."
pytest

Write-Output "Получение отчета..."
allure serve allure-results

