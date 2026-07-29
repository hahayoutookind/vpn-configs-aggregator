# vpn-configs-aggregator

This repository collects text from a small set of public URLs, combines it into one file, and generates a Base64 version of the same content.

## What it does

On each run, the workflow:

1. Downloads text from the configured source URLs
2. Merges all text into a single file: "all-vpn.txt"
3. Encodes the merged text as Base64
4. Saves the encoded result to "all-vpn-base64.txt"

The files are overwritten each time the workflow runs, so they always contain the latest generated output.

## Automation

The workflow is set up to run:

- every hour
- on new commits to the repository
- manually, if needed

> [!IMPORTANT]
> This repository was entirely AI vibecoded and is made for personal use.
> It may be rough, minimal, or contain assumptions that fit my own setup rather than a general-purpose production workflow.

## Files

- ".github/workflows/update-vpn.yml" — GitHub Actions workflow
- "scripts/update_vpn.py" — Python script that downloads and processes the text
- "all-vpn.txt" — merged plain text output
- "all-vpn-base64.txt" — merged Base64 output
