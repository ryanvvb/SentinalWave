import os
import time
import numpy as np
import argparse

# Setting up some constants
# Change these to your proper folders!
GENERIC = './../Data/GenericFsk'
HYUNDAI = './../Data/Hyundai'
TOYOTALC= './../Data/ToyotaLc'
GENERATE = '/None'  # Changed this to '/None' to create a 'None' directory

def generate_square_wave_signal(frequency, duration, sampling_rate, amplitude, output_directory, noise_amplitude):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Calculate the number of samples
    num_samples = int(sampling_rate * duration)

    prefix = "bad_keyfob_signal"  # Prefix for output file names
    timestamp = time.strftime("%Y%m%d%H%M%S")
    fname = os.path.join(output_directory, f"{prefix}{timestamp}.raw")

    # Create a time array
    t = np.linspace(0, duration, num_samples, endpoint=False)

    # Generate a square wave signal
    square_wave = amplitude * (1 + np.sign(np.sin(2 * np.pi * frequency * t)))

    # Add random noise to the signal
    noise = noise_amplitude * np.random.normal(0, 1, num_samples)
    square_wave_with_noise = square_wave + noise

    # Convert the signal to 16-bit PCM format
    square_wave_with_noise = (square_wave_with_noise * 32767).astype(np.int16)

    # Save the square wave signal with noise to a RAW file
    with open(fname, 'wb') as raw_file:
        square_wave_with_noise.tofile(raw_file)

    return fname

def main(iter, noise_amplitude):
    # Set the parameters
    frequency = 433.9e6  # Frequency of the square wave (in Hz)
    duration = 4   # Duration of the signal (in seconds)
    sampling_rate = 8e6  # Sampling rate (in samples per second)
    amplitude = 1  # Amplitude of the square wave
    output_directory = GENERIC + GENERATE  # Output directory

    for _ in range(iter):
        raw_fname = generate_square_wave_signal(frequency, duration, sampling_rate, amplitude, output_directory, noise_amplitude)
        print(f"Raw signal saved to {raw_fname}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate square wave signals.")
    parser.add_argument("--iter", type=int, default=15, help="Number of iterations to run")
    parser.add_argument("--noise", type=float, default=0.1, help="Amplitude for noise")
    args = parser.parse_args()
    main(args.iter, args.noise)
