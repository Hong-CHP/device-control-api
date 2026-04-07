import { Controller, Post, Body } from "@nestjs/common";
import { EventService } from "./event.service";

@Controller('event')
export class EventController {
    constructor (private readonly eventService: EventService) {}

    @Post()
    handleEvent(@Body() body: any) {
        return this.eventService.handleEvent(body)
    }
}