# Authorized Security Lab — Rules of Engagement

## Written authorization
- Lab owner: ____________________
- Assessor: Mousumi Mondal
- Approved assets: See `authorized-lab-assets.csv`
- Approval date: ____________________

Never test a system that is absent from the asset inventory.

## Permitted techniques
- Asset verification
- Limited reconnaissance
- Controlled TCP connectivity validation
- Non-destructive evidence collection
- Finding documentation and reporting

## Explicit exclusions
No denial of service, destructive payloads, persistence, credential reuse,
third-party targets, or uncontrolled data extraction.

## Testing window and stop conditions
- Start: ____________________
- End: ____________________
- Emergency contact: ____________________
- Rate limit: maximum one connection attempt per selected port with a short delay
- Stop immediately if an unauthorized asset is encountered, an external system is affected,
  the approved window ends, or a safety condition occurs.

## Evidence handling
Store the minimum evidence, redact secrets and personal data, and define deletion timing.
Do not commit credentials, tokens, private keys, or unnecessary personal data.

## Reporting
For each finding record:
- asset
- severity rationale
- reproduction steps
- impact
- evidence
- remediation
