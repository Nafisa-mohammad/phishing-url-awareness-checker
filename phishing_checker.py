
import re
from urllib.parse import urlparse


def inspect_url(raw_url):
    """Check visible URL text for selected warning signs."""

    url = raw_url.strip()
    findings = []

    if not url:
        return ["No URL entered."]

    candidate = url if "://" in url else "http://" + url

    parsed = urlparse(candidate)
    host = (parsed.hostname or "").lower()

    if not host:
        return ["Could not identify a hostname."]

    # Check 1: @ symbol
    if "@" in candidate:
        findings.append(
            "Contains an @ symbol; inspect carefully."
        )

    # Check 2: URL length
    if len(url) > 100:
        findings.append(
            "Unusually long URL (over 100 characters)."
        )

    # Check 3: IP address
    if re.fullmatch(r"(?:\d{1,3}\.){3}\d{1,3}", host):
        findings.append(
            "Uses an IP address instead of a familiar domain."
        )

    # Check 4: Number of hostname segments
    labels = [part for part in host.split(".") if part]

    if len(labels) >= 5:
        findings.append(
            "Contains many hostname segments/subdomains."
        )

    # Check 5: Punycode marker
    if "xn--" in host:
        findings.append(
            "Contains a punycode-style hostname."
        )

    # Check 6: HTTP scheme
    if parsed.scheme.lower() == "http":
        findings.append(
            "Uses HTTP. HTTPS alone does not prove trust."
        )

    if not findings:
        findings.append(
            "No listed warning signs found. This does NOT prove safety."
        )

    return findings


def main():
    print("EWB Phishing URL Awareness Checker")
    print("Text checks only - this program does not open URLs.")

    # Improvement 1: Allow multiple URL checks
    while True:

        raw_url = input(
            "\nEnter a sample URL (or type q to quit): "
        )

        if raw_url.strip().lower() in ("q", "quit", "exit"):
            print("Goodbye! Stay alert online.")
            break

        print("\nResult:")

        findings = inspect_url(raw_url)

        for item in findings:
            print("- " + item)

        # Improvement 2: Count warning signs
        info_messages = (
            "No URL entered.",
            "Could not identify a hostname.",
            "No listed warning signs found."
        )

        warning_count = sum(
            1 for item in findings
            if not item.startswith(info_messages)
        )

        print(f"\nTotal warning signs found: {warning_count}")

        print("\nNever enter passwords from unexpected links.")


if __name__ == "__main__":
    main()
