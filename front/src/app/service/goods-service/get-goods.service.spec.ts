import { TestBed } from '@angular/core/testing';

import { GetGoodsService } from './get-goods.service';

describe('GetGoodsService', () => {
  let service: GetGoodsService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(GetGoodsService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
