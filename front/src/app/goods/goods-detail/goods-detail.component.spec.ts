import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GoodsDetailComponent } from './goods-detail.component';

describe('GoodsDetailComponent', () => {
  let component: GoodsDetailComponent;
  let fixture: ComponentFixture<GoodsDetailComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ GoodsDetailComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(GoodsDetailComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
