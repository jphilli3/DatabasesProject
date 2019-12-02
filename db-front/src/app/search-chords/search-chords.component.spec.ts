import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SearchChordsComponent } from './search-chords.component';

describe('SearchChordsComponent', () => {
  let component: SearchChordsComponent;
  let fixture: ComponentFixture<SearchChordsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SearchChordsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SearchChordsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
