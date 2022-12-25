import { ComponentFixture, TestBed } from '@angular/core/testing';

import { OwnUserComponent } from './own-user.component';

describe('OwnUserComponent', () => {
  let component: OwnUserComponent;
  let fixture: ComponentFixture<OwnUserComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ OwnUserComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(OwnUserComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
