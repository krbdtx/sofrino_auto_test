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

$repoUrl = "https://github.com/krbdtx/sofrino_auto_test.git"
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
Write-Output "Выберете желаемый уровень тестов для запуска:"
Write-Output "1. Web"
Write-Output "2. API"
#Write-Output "3. Mobile"
$testType = Read-Host "Введите номер уровня"

switch ($testType) {
    1 {
        Write-Output "Запуск UI тестов в Web..."
        pytest tests/web
    }
    2 {
        Write-Output "Запуск API тестов..."
        pytest tests/api
    }
    3 {
        Write-Output "Запуск тестов на мобильном устройстве..."
        pytest tests/mobile
    }
    default {
        Write-Output "Ошибка не верный ввод."
        exit 1
    }
}

Write-Output "Получение отчета..."
allure serve allure-results

