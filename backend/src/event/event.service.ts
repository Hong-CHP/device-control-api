import { Injectable } from "@nestjs/common";
import { SerialService } from "src/serial/serial.service";

@Injectable()
export class EventService {
    constructor(private readonly serialPort: SerialService) {}

    handleEvent(body: any){
        if (body.type === 'face_detected')
            this.serialPort.send('1')
        else
            this.serialPort.send('0')
        return {ok : true}
    }
}