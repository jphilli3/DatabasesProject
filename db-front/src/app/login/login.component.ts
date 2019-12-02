import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  
  username: String = "";
  response: any;
  constructor(private svc: ApiService ,private http: HttpClient) { 
  }
  
  ngOnInit() {
  }

  loginUser(event){
    event.preventDefault()
    console.log(event)
  }

  login() {
    this.http.get(this.svc.apiURL + "users/" + "{id}?user_id=1").subscribe((response)=>{
    this.response = response; 
    console.log(this.response);})
  }

}
