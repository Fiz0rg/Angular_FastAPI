import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SortedCategoryComponent } from './sorted-category.component';

describe('SortedCategoryComponent', () => {
  let component: SortedCategoryComponent;
  let fixture: ComponentFixture<SortedCategoryComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SortedCategoryComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SortedCategoryComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
