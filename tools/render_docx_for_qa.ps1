param(
  [Parameter(Mandatory=$true)]
  [string]$InputDocx,

  [string]$OutputDir = "",

  [switch]$EmitPdf
)

$ErrorActionPreference = "Stop"

$repoRoot = Resolve-Path -LiteralPath (Join-Path $PSScriptRoot "..")
$python = "C:\Users\User\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
$pdftoppm = "C:\Users\User\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe"
$libreOfficeProgram = "C:\Program Files\LibreOffice\program"

if (-not (Test-Path -LiteralPath $python)) {
  throw "Bundled Codex Python not found: $python"
}
if (-not (Test-Path -LiteralPath $pdftoppm)) {
  throw "Bundled Poppler pdftoppm not found: $pdftoppm"
}
if (-not (Test-Path -LiteralPath (Join-Path $libreOfficeProgram "soffice.exe"))) {
  throw "LibreOffice soffice.exe not found. Install with: winget install --id TheDocumentFoundation.LibreOffice --source winget"
}

if ([string]::IsNullOrWhiteSpace($OutputDir)) {
  $stem = [System.IO.Path]::GetFileNameWithoutExtension($InputDocx)
  $OutputDir = Join-Path $repoRoot "tmp\render_$stem"
}

$env:Path = "$libreOfficeProgram;$env:Path"

$resolvedInput = Resolve-Path -LiteralPath $InputDocx
$resolvedOutput = New-Item -ItemType Directory -Force -Path $OutputDir
$stem = [System.IO.Path]::GetFileNameWithoutExtension($resolvedInput.Path)

& soffice --headless --convert-to pdf --outdir $resolvedOutput.FullName $resolvedInput.Path
$pdfPath = Join-Path $resolvedOutput.FullName "$stem.pdf"

if (-not (Test-Path -LiteralPath $pdfPath)) {
  throw "LibreOffice did not create expected PDF: $pdfPath"
}

$prefix = Join-Path $resolvedOutput.FullName "page"
& $pdftoppm -png $pdfPath $prefix

Get-ChildItem -LiteralPath $resolvedOutput.FullName -Filter "page-*.png" | Sort-Object Name | ForEach-Object {
  Write-Output $_.FullName
}

if (-not $EmitPdf) {
  Remove-Item -LiteralPath $pdfPath -Force
}
Write-Output "Rendered QA pages: $OutputDir"
