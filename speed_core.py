from dataclasses import dataclass

import speedtest


BITS_PER_MEGABIT = 1_000_000


@dataclass(frozen=True)
class SpeedTestResult:
    download_mbps: int
    upload_mbps: int
    ping_ms: int


def convert_speed(bits_per_second):
    return bits_per_second / BITS_PER_MEGABIT


def run_speed_test():
    tester = speedtest.Speedtest()
    tester.get_best_server()
    download = tester.download()
    upload = tester.upload()
    ping = tester.results.ping

    return SpeedTestResult(
        download_mbps=round(convert_speed(download)),
        upload_mbps=round(convert_speed(upload)),
        ping_ms=round(ping),
    )
