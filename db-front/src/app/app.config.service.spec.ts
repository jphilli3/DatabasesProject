
import { Health } from './health';
import { TestBed } from '@angular/core/testing';

import { ConfigService } from './app.config.service'
import { HttpClientTestingModule } from '@angular/common/http/testing';

describe('Config Service', () => {
  beforeEach(() => TestBed.configureTestingModule({
    imports: [
      HttpClientTestingModule,
    ],
  }));


});
