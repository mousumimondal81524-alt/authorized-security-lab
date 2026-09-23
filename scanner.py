import socket
import time


def check_tcp_port(host: str, port: int, timeout: float = 2.0) -> bool:
    """Check one TCP port. Use only against an authorized lab target."""
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except (socket.timeout, ConnectionRefusedError, OSError):
        return False


def scan_authorized_host(host: str, ports: list[int]) -> list[dict]:
    """Perform a small, rate-limited connectivity check."""
    results = []

    for port in ports:
        start = time.perf_counter()
        reachable = check_tcp_port(host, port)
        elapsed_ms = round((time.perf_counter() - start) * 1000, 2)

        results.append({
            "host": host,
            "port": port,
            "reachable": reachable,
            "response_time_ms": elapsed_ms,
        })

        time.sleep(0.2)

    return results
