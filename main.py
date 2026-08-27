import speedtest

def convert_speed(bps):
    mbps = bps / (1024*1024)  # Convert to megabits per second
    return mbps

def check_intenet_speed():
    try:
        servernames =[]     
        st = speedtest.Speedtest()
        st.get_servers(servernames) 
        st.get_best_server()
        st.download()
        st.upload()
        results = st.results.dict()

        download = results["download"]
        upload = results["upload"]  
        ping = results["ping"]    

        download_mbps = convert_speed(download)
        upload_mbps = convert_speed(upload)

        print(f"Download speed: {int(download_mbps)} Mbps")
        print(f"Upload speed: {int(upload_mbps)} Mbps")
        print(f"Ping: {int(ping)} ms") 

    except Exception as e:
        print(f"Error checking the internet speed: {e}")

if __name__=="__main__":
    check_intenet_speed()