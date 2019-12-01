import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { FastApiService } from './fast-api.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {

  constructor(private svc: FastApiService, private http: HttpClient){
    svc.printToConsole("Got the service");
  }

  ngOnInit(){
   let obs = this.http.get("http://127.0.0.1:8000/")
   obs.subscribe((response)=>console.log(response))
  }
}
