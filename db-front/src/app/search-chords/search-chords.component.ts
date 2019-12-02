import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-search-chords',
  templateUrl: './search-chords.component.html',
  styleUrls: ['./search-chords.component.css']
})
export class SearchChordsComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }

}
@Component({
  selector: 'app-search-bar',
  styleUrls: ['./search-chords.component.css'],
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
  <td class="chord-view-cell">
  <svg class="chord-view">
      <rect class = "header" x="0" y= "0"/>
    <g id="frets">
      <rect class = "fret-shadow" x="0" y=20%"/>
      <rect class = "fret-shadow" x="0" y=40%/>
      <rect class = "fret-shadow" x="0" y=60%/>
      <rect class = "fret-shadow" x="0" y=80%/>
      <text x="10" y="14%" font-family="sans-serif" font-size="20px" fill="black"> 1 </text>
      <rect class = "fret" x="0" y= 20%/>
      <text x="10" y="34%" font-family="sans-serif" font-size="20px" fill="black"> 2 </text>
      <rect class = "fret" x="0" y= 40%/>
      <text x="10" y="54%" font-family="sans-serif" font-size="20px" fill="black"> 3 </text>
      <rect class = "fret" x="0" y= 60%/>
      <text x="10" y="74%" font-family="sans-serif" font-size="20px" fill="black"> 4 </text>
      <rect class = "fret" x="0" y= 80%/>
      
    </g>
    <g id="strings">
      <rect class = "string-shadow" x=10% y="0"/>
      <rect class = "string-shadow" x=25% y="0"/>
      <rect class = "string-shadow" x=40% y="0"/>
      <rect class = "string-shadow" x=55% y="0"/>
      <rect class = "string-shadow" x=70% y="0"/>
      <rect class = "string-shadow" x=85% y="0"/>
      <rect class = "string" x=10% y="0"/>
      <rect class = "string" x=25% y="0"/>
      <rect class = "string" x=40% y="0"/>
      <rect class = "string" x=55% y="0"/>
      <rect class = "string" x=70% y="0"/>
      <rect class = "string" x=85% y="0"/>
    </g>
    <g id="positions">
      <circle class="position" cx=12% cy=20% r="15" display="block"/>
      <circle class="position" cx=27% cy=20% r="15" display="block"/>
      <circle class="position" cx=42% cy=20% r="15" display="block"/>
      <circle class="position" cx=57% cy=20% r="15" display="block"/>
      <circle class="position" cx=72% cy=20% r="15" display="block"/>
      <circle class="position" cx=87% cy=20% r="15" display="block"/>
      
      <circle class="position" cx=12% cy=40% r="15" display="block"/>
      <circle class="position" cx=27% cy=40% r="15" display="block"/>
      <circle class="position" cx=42% cy=40% r="15" display="block"/>
      <circle class="position" cx=57% cy=40% r="15" display="block"/>
      <circle class="position" cx=72% cy=40% r="15" display="block"/>
      <circle class="position" cx=87% cy=40% r="15" display="block"/>

      <circle class="position" cx=12% cy=60% r="15" display="block"/>
      <circle class="position" cx=27% cy=60% r="15" display="block"/>
      <circle class="position" cx=42% cy=60% r="15" display="block"/>
      <circle class="position" cx=57% cy=60% r="15" display="block"/>
      <circle class="position" cx=72% cy=60% r="15" display="block"/>
      <circle class="position" cx=87% cy=60% r="15" display="block"/>

      <circle class="position" cx=12% cy=80% r="15" display="block"/>
      <circle class="position" cx=27% cy=80% r="15" display="block"/>
      <circle class="position" cx=42% cy=80% r="15" display="block"/>
      <circle class="position" cx=57% cy=80% r="15" display="block"/>
      <circle class="position" cx=72% cy=80% r="15" display="block"/>
      <circle class="position" cx=87% cy=80% r="15" display="block"/>
    </g>
    </svg>
    <label class="chord-name" for="chord-view-cell"> D </label>
    </td>
    `
})

export class ChordViewComponent {
  value = '';
  dChord: number[] = [0, 0, 0, 3, 2, 3];
  // Chords with positions numbered 0-23 (6*4)
} 
