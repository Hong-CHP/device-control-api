import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { EventModule } from './event/event.module';
import { SerialModule } from './serial/serial.module';

@Module({
  imports: [EventModule, SerialModule],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
