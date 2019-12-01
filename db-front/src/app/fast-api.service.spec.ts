import { TestBed } from '@angular/core/testing';

import { FastApiService } from './fast-api.service';

describe('FastApiService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: FastApiService = TestBed.get(FastApiService);
    expect(service).toBeTruthy();
  });
});
