import { Health } from './health';
import { ApiService } from './api.service';
import { Component } from '@angular/core';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent {
  title = 'Guitar Hero';
}

@Component({
  selector: 'app-search',
  templateUrl: './app.component.html',
  template: `
    <input (keyup)="input($event)">
    <p>
    <button (click)="search()">Search Chord</button>
    </p>
    <p>{{value}}</p>`
})
export class SearchButtonComponent {
  value = '';
  b = true;
  search() {
    this.value = '';
  }
  input(event: any) {
    this.value = event.target.value;
  }
}
