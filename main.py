from scanner import scan_authorized_host
from reporter import create_report


def main() -> None:
    print("AUTHORIZED SECURITY LAB")
    print("=" * 30)
    print("Target: LAB-01")
    print("Environment: Isolated localhost")
    print("Scope: 127.0.0.1 only")

    # These are deliberately limited to local training ports.
    host = "127.0.0.1"
    ports = [80, 443, 8080]

    results = scan_authorized_host(host, ports)

    for result in results:
        status = "REACHABLE" if result["reachable"] else "NOT REACHABLE"
        print(
            f"{result['host']}:{result['port']} -> "
            f"{status} ({result['response_time_ms']} ms)"
        )

    create_report(results)
    print("Report written to evidence/report.txt")


if __name__ == "__main__":
    main()
