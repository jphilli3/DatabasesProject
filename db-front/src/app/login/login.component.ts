import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { ApiService } from '../api.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  
  username: String = "";
  response: any;
  
  ngOnInit() {
  }

  users: any[] = [];
  constructor(private svc: ApiService, private http: HttpClient, private router: Router){}


  loginUser(event){
    event.preventDefault()
    const target = event.target
    const username = target.querySelector('#username').value
    const password = target.querySelector('#password ').value
    
    const obs = this.http.get(this.svc.apiURL+"getUserDetails/{user}?username="+username)
    obs.subscribe((response)=>{
      this.users.push(response);

    });

    console.log(this.users)

    // if (this.users[0]["password"] == password) this.router.navigate(["/search-chords"])
}

  

}
