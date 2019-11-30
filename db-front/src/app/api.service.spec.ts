import { Health } from './health';
import { TestBed } from '@angular/core/testing';

import { ApiService } from './api.service';
import { HttpClientTestingModule } from '@angular/common/http/testing';

describe('ApiService', () => {
  beforeEach(() => TestBed.configureTestingModule({
    imports: [
      HttpClientTestingModule,
    ],
  }));

  it('should be created', () => {
    const service: ApiService = TestBed.get(ApiService);
    expect(service).toBeTruthy();
  });
  it(`should have status`, () => {
    const service: ApiService = TestBed.get(ApiService);
    console.log(service.getHealth());
    expect(service.getHealth());
  });
});
