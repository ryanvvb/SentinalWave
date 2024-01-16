# Basic imports
import os
import time
import subprocess
import signal

# Setting up some constants
# Change these to your proper folders!
HYUNDAI = './../Data/Hyundai'
GENERIC = './../Data/GenericFsk'
TOYOTALC= './../Data/ToyotaLc'
LOCK = '/Lock/'
UNLOCK = '/Unlock/'
BAD = '/None/'

def record_signal(output, samp_rate, freq, dur, prefix):
    
    # Init the SDR
    # Specific to the hackrf for now (will make a generic one for the regular SDR next)
    scantime = dur
    start = time.time()
    timestamp = time.strftime("%Y%m%d%H%M%S")
    fname = output+prefix+timestamp+'.raw'
    lgain = 16
    bgain = 16

    # Create the output folder if it doesn't exist
    if not os.path.exists(output):
        os.makedirs(output)

    print(f"Preparing to scan to {prefix+timestamp}...")
    # Running as a subprocess (can make into a threaded proc as well
    p = subprocess.Popen(["hackrf_transfer","-r",str(fname),"-f",str(freq), "-s",str(samp_rate)])    
    time.sleep(dur)
    p.send_signal(signal.SIGINT)
    print(f"File saved...")


if __name__ == '__main__':
    # Configure your parameters
    output = HYUNDAI+UNLOCK  # Folder to save the recorded signals
    samp_rate = 8e6  # Sample rate (2Msps in this example)
    freq = 433.9e6  # Center frequency (433.92 MHz in this example for subaru and hyundai 4Runner I think was 315Mhz)
    dur = 4  # Recording duration in seconds
    prefix = "keyfob_signal"  # Prefix for output file names

    try:
        while True:
            record_signal(output, samp_rate, freq, dur, prefix)
            print(f"Recording completed {output}, f:{freq}, s:{samp_rate}.\nWaiting for the next capture in 2 seconds...")
            time.sleep(2)  # Wait for X seconds before the next capture
    except KeyboardInterrupt:
        print("Exiting...")