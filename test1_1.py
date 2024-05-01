import struct
import time 
import serial 

ser = serial.Serial('COM5', 115200)

# 샘플 정수 값
integer_values = [0,]

while True:
    integer_values = [5, 26, 16, 16]
    # 정수 값을 16진수 문자열로 변환
    hex_string = ''.join(format(i, '02X') for i in integer_values)
    
    # 문자열을 바이트로 변환
    hex_bytes = bytes.fromhex(hex_string)
    
    # 바이트 보내기
    ser.write(hex_bytes)
    
    # 전송된 바이트 출력
    print("보낸 바이트:", hex_bytes)
    
    # 바이트 받기
    received_bytes = ser.read(len(hex_bytes))
    
    # 받은 바이트 출력
    print("받은 바이트:", received_bytes)
    
    # 받은 바이트를 16진수 문자열로 변환
    received_hex_string = received_bytes.hex()

    # 16진수 문자열을 정수로 변환
    received_integers = [int(received_hex_string[i:i+2], 16) for i in range(0, len(received_hex_string), 2)]

    print("받은 정수 값:", received_integers)
    
    time.sleep(1)
