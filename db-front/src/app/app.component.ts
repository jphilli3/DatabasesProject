import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})


export class AppComponent {
  title = 'Guitar Hero';

  apiURL = "http://127.0.0.1:8000/"
  constructor(private http: HttpClient){}

  ngOnInit(){
    let obs = this.http.get(this.apiURL)
    obs.subscribe((response)=> console.log(response))
  }
}