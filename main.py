from speed_core import run_speed_test


def check_internet_speed():
    try:
        result = run_speed_test()
        print(f"Download speed: {result.download_mbps} Mbps")
        print(f"Upload speed: {result.upload_mbps} Mbps")
        print(f"Ping: {result.ping_ms} ms")
    except Exception as e:
        print(f"Error checking the internet speed: {e}")


if __name__ == "__main__":
    check_internet_speed()
