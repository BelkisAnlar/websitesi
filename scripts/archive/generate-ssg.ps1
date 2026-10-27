$ErrorActionPreference = 'Stop'

# Load JSON Data
$jsonData = Get-Content 'blog-data.json' -Raw -Encoding UTF8 | ConvertFrom-Json

# Helper to read base template from existing file (we'll steal header/footer from iletisim.html)
$baseHtml = Get-Content 'iletisim.html' -Raw -Encoding UTF8

# Extract Header
$headerRegex = '(?is)(<!DOCTYPE html>.*?</header>)'
$headerMatch = [regex]::Match($baseHtml, $headerRegex)
$headerHtml = $headerMatch.Groups[1].Value
$headerHtml = $headerHtml -replace '<title>.*?</title>', '<title>{{TITLE}}</title>'

# Extract Footer
$footerRegex = '(?is)(<div class="custom-shape-divider-top-footer">.*?</html>)'
$footerMatch = [regex]::Match($baseHtml, $footerRegex)
$footerHtml = $footerMatch.Groups[1].Value

# We need to add Blog to the nav and footer of the header/footer since iletisim.html had it?
# Wait, iletisim.html was deleted! Let's read from hakkimda.html instead!
