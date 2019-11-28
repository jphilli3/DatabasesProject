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
  selector: 'app-search-bar',
  styleUrls: ['./app.component.css'],
  template: `
    <input class="search-bar" type="text">
    `
})
export class SearchBarComponent {
  value = '';
  input(event: any) {
    this.value = event.target.value;
  }
}

@Component({
  selector: 'app-chord-view',
  styleUrls: ['./app.component.css'],
  template: `
  <div class="chord-view">
    <div class="string">
      </div>
    <div class="string">
      </div>
    <div class="string">
      </div>
    <div class="string">
      </div>
    <div class="string">
      </div>
    <div class="string">
      </div>
  </div>
    `
})

export class ChordViewComponent {
  value = '';
  input(event: any) {
    this.value = event.target.value;
  }
}
// @Component({
//   selector: 'app-search-button',
//   templateUrl: './app.component.html',
//   template: `
//   <button (click)="search()">Search</button>
//   `
// })

// export class SearchButtonComponent {
 
// }
