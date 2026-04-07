import { Injectable, OnModuleInit } from '@nestjs/common';
import { SerialPort } from 'serialport';

@Injectable()
export class SerialService implements OnModuleInit {
    private port: SerialPort
    
    onModuleInit() {
        this.port = new SerialPort({
            path: '/dev/ttyACM0',
            baudRate: 9600
        })
    }

    send(data: string) {
        if (this.port && this.port.writable)
            this.port.write(data)
    }
}   
