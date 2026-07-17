<#
.SYNOPSIS
    Validate the course's Python notebook samples by executing them against a live
    Microsoft Foundry / Azure OpenAI configuration.

.DESCRIPTION
    Discovers every course notebook (excluding .NET notebooks, the .venv,
    site-packages, .git, node_modules, translations, and skill template assets),
    executes each one headlessly with nbconvert, and reports a PASS/FAIL matrix
    plus the first error for any failure. Results are also written to results.json
    in the output directory.

    Requirements:
      - Python 3.12+ with the course requirements installed (pip install -r requirements.txt)
        plus nbconvert + ipykernel:  python -m pip install nbconvert ipykernel
      - A configured .env at the repo root (see .env.example) OR the equivalent
        environment variables already set.
      - `az login` completed (samples authenticate with AzureCliCredential / Entra ID).

.PARAMETER Python
    Python executable to use. Defaults to auto-detection (python, python3, py -3).

.PARAMETER Timeout
    Per-cell execution timeout in seconds. Default: 300.

.PARAMETER Filter
    Optional wildcard applied to the notebook's repo-relative path, e.g. '01-*' or '*agent-framework*'.

.PARAMETER IncludeDotnet
    Also attempt .NET notebooks (requires the .NET Interactive kernel). Off by default.

.PARAMETER List
    Only list the notebooks that would run; do not execute them.

.PARAMETER Retries
    Number of times to retry a notebook that fails with a *transient* error
    (shared-quota HTTP 429, Azure CLI token hiccup, or a timeout). Deterministic
    code errors (ImportError, TypeError, ...) are never retried. Default: 2.

.PARAMETER RetryDelaySeconds
    Backoff delay between transient retries, in seconds. Default: 20.

.PARAMETER OutputDir
    Where executed copies, per-notebook logs, and results.json are written.
    Default: $env:TEMP\aiab-nbval

.EXAMPLE
    pwsh scripts/validate-notebooks.ps1

.EXAMPLE
    pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

.EXAMPLE
    pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe" -List
#>
[CmdletBinding()]
param(
    [string]$Python,
    [int]$Timeout = 300,
    [string]$Filter,
    [string[]]$Only,
    [switch]$IncludeDotnet,
    [switch]$List,
    [int]$Retries = 2,
    [int]$RetryDelaySeconds = 20,
    [string]$OutputDir = (Join-Path $env:TEMP 'aiab-nbval')
)

$ErrorActionPreference = 'Stop'
$RepoRoot = Split-Path -Parent $PSScriptRoot

function Resolve-Python {
    param([string]$Preferred)
    $candidates = @()
    if ($Preferred) { $candidates += $Preferred }
    if ($env:AIAB_PYTHON) { $candidates += $env:AIAB_PYTHON }
    $candidates += @('python', 'python3', 'py')
    foreach ($c in $candidates) {
        try {
            $v = & $c --version 2>&1
            if ($LASTEXITCODE -eq 0 -and "$v" -match 'Python 3') { return $c }
        }
        catch { }
    }
    return $null
}

$py = Resolve-Python -Preferred $Python
if (-not $py) {
    Write-Error "No working Python found. Pass -Python <path> or set AIAB_PYTHON. Needs Python 3.12+ with nbconvert."
    exit 2
}
Write-Host "Python: $py ($(& $py --version 2>&1))"

# Verify nbconvert is available.
& $py -m nbconvert --version *> $null
if ($LASTEXITCODE -ne 0) {
    Write-Error "nbconvert is not installed for '$py'. Run: $py -m pip install nbconvert ipykernel"
    exit 2
}

# Warn if configuration looks missing.
$envFile = Join-Path $RepoRoot '.env'
if (-not (Test-Path $envFile) -and -not $env:AZURE_AI_PROJECT_ENDPOINT) {
    Write-Warning "No .env at repo root and AZURE_AI_PROJECT_ENDPOINT is not set. Notebooks that call Azure will fail. See .env.example."
}

# Paths to exclude from discovery (not course samples).
$excludePattern = '\\\.venv\\|[/\\]site-packages[/\\]|\\\.git\\|[/\\]node_modules[/\\]|\\\.agents\\|[/\\]translations[/\\]|[/\\]translated_images[/\\]'

$nbs = Get-ChildItem -Path $RepoRoot -Recurse -Filter *.ipynb |
    Where-Object { $_.FullName -notmatch $excludePattern } |
    Where-Object { $IncludeDotnet -or ($_.FullName -notmatch 'dotnet|dotNET') } |
    Sort-Object FullName

if ($Filter) {
    $nbs = $nbs | Where-Object { $_.FullName.Substring($RepoRoot.Length + 1) -like $Filter }
}
if ($Only) {
    $nbs = $nbs | Where-Object {
        $rel = $_.FullName.Substring($RepoRoot.Length + 1)
        @($Only | Where-Object { $rel -like "*$_*" }).Count -gt 0
    }
}

Write-Host "Discovered $($nbs.Count) notebook(s) under $RepoRoot"
if ($List) {
    $nbs | ForEach-Object { "  " + $_.FullName.Substring($RepoRoot.Length + 1) }
    exit 0
}

New-Item -ItemType Directory -Force -Path $OutputDir | Out-Null
Push-Location $RepoRoot
try {
    $rows = @()
    # Errors worth retrying: shared-quota 429s, Azure CLI token hiccups, and timeouts.
    # Deterministic code errors (ImportError, TypeError, ...) are NOT retried.
    $transient = 'HTTP/1.1 429|Too Many Requests|exceeded (call|token) rate limit|exceeded your current quota|CredentialUnavailable|Failed to invoke the Azure CLI|TimeoutError|timed out|Connection reset|ServiceResponseError'
    foreach ($nb in $nbs) {
        $rel = $nb.FullName.Substring($RepoRoot.Length + 1)
        $safe = ($rel -replace '[\\/:]', '_')
        $logf = Join-Path $OutputDir ("log_" + $safe + ".txt")
        $code = 1
        $attempt = 0
        while ($true) {
            $attempt++
            & $py -m nbconvert --to notebook --execute $nb.FullName `
                --output-dir $OutputDir --output ("exec_" + $safe) `
                --ExecutePreprocessor.timeout=$Timeout *> $logf
            $code = $LASTEXITCODE
            if ($code -eq 0) { break }
            $logText = (Get-Content $logf -Raw -ErrorAction SilentlyContinue)
            if ($attempt -le $Retries -and $logText -match $transient) {
                Write-Host ("  transient error, retry {0}/{1} in {2}s: {3}" -f $attempt, $Retries, $RetryDelaySeconds, $rel)
                Start-Sleep -Seconds $RetryDelaySeconds
                continue
            }
            break
        }
        $err = ''
        if ($code -ne 0) {
            $m = Select-String -Path $logf -Pattern '(\w*Error|\w*Exception|CellExecutionError|StdinNotImplementedError):' | Select-Object -Last 1
            if ($m) { $err = ($m.Line.Trim() -replace '\s+', ' ') }
            if ($err.Length -gt 200) { $err = $err.Substring(0, 200) }
        }
        $status = if ($code -eq 0) { 'PASS' } else { 'FAIL' }
        "{0}  {1}  {2}" -f $status, $rel, $err
        $rows += [pscustomobject]@{ Notebook = $rel; Status = $status; Exit = $code; Error = $err; Log = $logf; Attempts = $attempt }
    }
}
finally {
    Pop-Location
}

$rows | ConvertTo-Json -Depth 4 | Set-Content (Join-Path $OutputDir 'results.json')
$pass = @($rows | Where-Object { $_.Exit -eq 0 }).Count
$fail = @($rows | Where-Object { $_.Exit -ne 0 }).Count
Write-Host ""
Write-Host "===== SUMMARY =====" -ForegroundColor Cyan
Write-Host "PASS: $pass"
Write-Host "FAIL: $fail"
Write-Host "Results: $(Join-Path $OutputDir 'results.json')"
if ($fail -gt 0) {
    Write-Host "----- FAILURES -----" -ForegroundColor Yellow
    $rows | Where-Object { $_.Exit -ne 0 } | ForEach-Object { "FAIL  {0}  ::  {1}" -f $_.Notebook, $_.Error }
}
exit $fail
