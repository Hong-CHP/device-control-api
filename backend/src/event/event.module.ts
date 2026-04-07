import { Module } from '@nestjs/common';
import { EventController } from './event.controller';
import { EventService } from './event.service';
import { SerialModule } from 'src/serial/serial.module';

@Module({
    imports: [SerialModule],
    controllers: [EventController],
    providers: [EventService]
})
export class EventModule{}