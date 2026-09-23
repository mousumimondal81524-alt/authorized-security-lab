from datetime import datetime
from pathlib import Path


def create_report(results: list[dict], filename: str = "evidence/report.txt") -> None:
    Path(filename).parent.mkdir(parents=True, exist_ok=True)

    with open(filename, "w", encoding="utf-8") as file:
        file.write("AUTHORIZED SECURITY LAB REPORT\n")
        file.write("=" * 40 + "\n")
        file.write(f"Generated: {datetime.now().isoformat(timespec='seconds')}\n\n")

        for result in results:
            file.write(f"Host: {result['host']}\n")
            file.write(f"Port: {result['port']}\n")
            file.write(f"Reachable: {result['reachable']}\n")
            file.write(f"Response time: {result['response_time_ms']} ms\n")
            file.write("-" * 40 + "\n")
