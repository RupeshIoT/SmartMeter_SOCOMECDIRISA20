
# SMART Meter SOCOMEC DIRIS A 20
# Phase 1 current Addr-1792
# To run:  /usr/bin/python3 /home/rupesh2019/Rupesh/IoT/CodePython/SOCOMEC1.py
import minimalmodbus
import time
import serial


delay=2
# port name, slave address (in decimal)
instrument = minimalmodbus.Instrument('/dev/ttyUSB0',10)
#sudo chmod 777 /dev/rfcomm0 
instrument.serial.baudrate = 9600


while True:
    # Register number, number of decimals, function code
    bl = instrument.read_register(512, 0, 3)
    print('Network Type (Phase ?): ' + str(bl) +'BL')
    time.sleep(delay)
    
    I1 = instrument.read_registers(768,2,3)
    print('Current (Phase 1): ' + str(I1[1]/1000) +'A')
    time.sleep(delay)

    I1max = instrument.read_registers(838, 2,3)
    
    print('Current (Phase 1max): ' + str(I1max[1]/1000) +'A')
    time.sleep(delay)
    
    Vp1 = instrument.read_registers(782, 2, 3)
    print('Phase to Neutarl Voltase (Phase 1): ' + str(Vp1[1]/100) +'V')
    time.sleep(delay)

    #fre = instrument.read_register(1802, 2, 3)
    fre = instrument.read_registers(788, 2, 3)
    print('Frequency: ' + str(fre[1]/100)+'Hz')
    time.sleep(delay)
    
    powerkw = instrument.read_registers(790, 2, 3)
    print('Power: ' + str(powerkw[1]/100) +'kW')
    time.sleep(delay)
    
    powerkvar = instrument.read_long(792, 3, True)
    print('Power: ' + str(powerkvar/100) +'kvar')
    time.sleep(delay)
    powerkva = instrument.read_registers(794, 2, 3)
    print('Power: ' + str(powerkva[1]/100) +'kVA')
    time.sleep(delay)
    
    work = instrument.read_registers(856, 2, 3)
    print('Energy: ' + str(work[1]) +'KWh')
    time.sleep(delay)