import json
from pathlib import Path

REPORT_PATH = Path("/app/report.json")


def load_report():
    assert REPORT_PATH.exists(), "expected /app/report.json to exist"
    try:
        return json.loads(REPORT_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise AssertionError("/app/report.json must contain valid JSON") from exc


def test_report_schema():
    """Success criterion 1: /app/report.json is a JSON object with exactly the required keys."""
    report = load_report()
    assert isinstance(report, dict), "report must be a JSON object"
    assert set(report) == {"total_requests", "unique_ips", "top_path"}


def test_total_requests():
    """Success criterion 2: total_requests equals the six non-empty log entries."""
    report = load_report()
    assert report["total_requests"] == 6


def test_unique_ips():
    """Success criterion 3: unique_ips equals the three distinct client IP addresses."""
    report = load_report()
    assert report["unique_ips"] == 3


def test_top_path():
    """Success criterion 4: top_path equals the most frequently requested path."""
    report = load_report()
    assert report["top_path"] == "/index.html"
