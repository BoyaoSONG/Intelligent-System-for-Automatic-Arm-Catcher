import serial
import time

ser = serial.Serial('COM4',9600)
angle_init = [83, 73, 68, 36, 55, 83]
angle_move = [['QLD$74', 'HHD$70', 'HHD$7+',	'FGD$7)', 'FGDS7('],
              ['QLD$74', 'HID$70', 'HID$7+', 'FID$7)', 'FIDS7('],
              ['KLD$74', 'KKD$7/', 'IKD$7+',	'GKD$7)', 'GKDS7('],
              ['KLD$74', 'KLD$7/', 'ILD$7+', 'HLD$7)', 'HLDa7('],
              ['KLD$74', 'FND$70', 'FND$7,', 'FMD$7)', 'FMDa7('],
              ['QLD$74', 'HHD$70', 'NGD$7-', 'LGD$7+', 'LGDa7*'],
              ['QLD$74', 'HID$70', 'LID$7,', 'LID$7*', 'LIDa7*'],
              ['KLD$74', 'KKD$7/', 'KJD$7,', 'MJD$7*', 'MJDa7*'],
              ['KLD$74', 'KLD$7/', 'KLD$7,', 'MLD$7*', 'MLDa7*'],
              ['KLD$74', 'FND$70', 'MND$7-', 'KND$7+', 'KNDa7*'],
              ['QLD$74', 'HHD$70', 'NHD$7.', 'QGD$7-', 'QGDa7,'],
              ['QLD$74', 'HID$70', 'PID$7.',	'PID$7,', 'PIDa7,'],
              ['KLD$74', 'KKD$7/', 'QKD$7.', 'QKD$7-', 'QKDa7-'],
              ['KLD$74', 'KLD$7/', 'QMD$7.',	'RMD$7-', 'RMDa7-'],
              ['KLD$74', 'FND$70', 'PND$7.',	'PND$7,	', 'PNDa7,'],
              ['QLD$74', 'NFD$71', 'TGD$71',	'TGD$7/	', 'TGDa7-'],
              ['QLD$74', 'HID$70', 'TID$72',	'THD$7/	', 'UHDa7.'],
              ['KLD$74', 'KKD$7/', 'UKD$72',	'TKD$7/	', 'UKDa7.'],
              ['KLD$74', 'KLD$7/', 'SLD$73',	'ULD$70	', 'VLDa7/'],
              ['KLD$74', 'FND$70', 'SOD$71',	'UOD$7/	', 'UODa7.'],
              ]


def motor_init():
    to_send = 'SID$7S'
    ser.write(bytes(to_send, 'UTF-8'))


def motor_collect():
    to_send = 'SIDa7S'
    ser.write(bytes(to_send, 'UTF-8'))
    time.sleep(1)
    to_send = 'SwDa7S'
    ser.write(bytes(to_send, 'UTF-8'))
    time.sleep(1)
    to_send = 'SwDa7?'
    ser.write(bytes(to_send, 'UTF-8'))
    time.sleep(1)
    to_send = 'SwDa74'
    ser.write(bytes(to_send, 'UTF-8'))
    time.sleep(1)
    to_send = 'SwD$74'
    ser.write(bytes(to_send, 'UTF-8'))
    time.sleep(1)
    to_send = 'SwD$7S'
    ser.write(bytes(to_send, 'UTF-8'))
    motor_init()


def motor_move(num):
    num = num - 6
    print("11111111", num)
    for i in [0, 1, 2, 3, 4]:
        to_send = angle_move[num][i]
        ser.write(bytes(to_send, 'UTF-8'))
        time.sleep(1)
    motor_collect()

