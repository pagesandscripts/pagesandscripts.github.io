# Index Page Generator
# This script generates the main index.html from story data
# Usage: .\tools\generate-index.ps1

param(
    [string]$DataFile = "stories-data.json",
    [string]$TemplateFile = "templates\index-template.html"
)

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoRoot = Resolve-Path (Join-Path $scriptDir "..")
$outputRoot = Join-Path $repoRoot "docs"

$dataPath = Join-Path $repoRoot $DataFile
$templatePath = Join-Path $repoRoot $TemplateFile
$outputPath = Join-Path $outputRoot "index.html"

# Load story data
if (-not (Test-Path $dataPath)) {
    Write-Error "Story data file not found: $dataPath"
    exit 1
}

Write-Host "Loading story data from $DataFile..." -ForegroundColor Cyan
$storyData = Get-Content $dataPath -Raw | ConvertFrom-Json

# Load template
if (-not (Test-Path $templatePath)) {
    Write-Error "Index template not found: $templatePath"
    exit 1
}

$template = Get-Content $templatePath -Raw

# Generate story lists
$enListItems = @()
$faListItems = @()

foreach ($story in $storyData.stories) {
    $enItem = @"
          <li>
            <a href="en/stories/$($story.slug)/index.html">
              <span>$($story.en.title)</span>
            </a>
          </li>
"@
    
    $faItem = @"
          <li>
            <a href="fa/stories/$($story.slug)/index.html">
              <span>$($story.fa.title)</span>
            </a>
          </li>
"@
    
    $enListItems += $enItem
    $faListItems += $faItem
}

$enList = $enListItems -join "`n"
$faList = $faListItems -join "`n"

# Replace placeholders in template
$indexContent = $template -replace '{{EN_STORY_LIST}}', $enList
$indexContent = $indexContent -replace '{{FA_STORY_LIST}}', $faList

# Write index.html
$utf8NoBom = New-Object System.Text.UTF8Encoding $false
[System.IO.File]::WriteAllText($outputPath, $indexContent, $utf8NoBom)

$count = $storyData.stories.Count
Write-Host "`nSuccessfully generated index.html with $count stories!" -ForegroundColor Green
