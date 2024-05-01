#This code can receive hex string from PC through Serial. 
#You can send hex string using python code beloww. 

import struct
import time 
import serial 

ser = serial.Serial('COM3', 115200)

# Sample integer values
integer_values = [123, 100, 10, 16]

while True:
    # Format string for packing four integers (little-endian)
    format_string = "bbbb"  # '<' for little-endian, '>' for big-endian

    # Pack integers into a byte array
    packed_bytes = struct.pack(format_string, *integer_values)
    ser.write(packed_bytes)

    # Unpack the byte array into integers
    unpacked_values = struct.unpack(format_string, packed_bytes)

    # Print the results
    print("Original integers:", integer_values)
    print("Packed bytes:", packed_bytes)  # This will be a bytes object
    print("Unpacked integers:", unpacked_values)

    time.sleep(1)
