import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { ApiService } from '../api.service';
import { Router } from '@angular/router';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  
  username: String = '';
  response: any;
  
  ngOnInit() {
  }

  user: any = [];
  constructor(private svc: ApiService, private http: HttpClient, private router: Router){}


  loginUser(event) {
    event.preventDefault();
    const target = event.target;
    const username = target.querySelector('#username').value;
    const password = target.querySelector('#password ').value;
    const obs = this.http.get(this.svc.apiURL + 'getUserDetails/{user}?username=' + username);
    obs.subscribe((response) => {
      this.user = response;
      if (this.user.password === password) {
        this.router.navigate(['/home']);
      }
    });
  } 

  createNewUser(event) {
    event.preventDefault();
    const target = event.target;
    const username = target.querySelector('#username').value;
    const password = target.querySelector('#password ').value;
    const newUser = {'username': username, 'password': password, 'firstname': 'New', 'lastname': 'User', 'player_level': '2'};
  
    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type':  'application/json'
      })
    };
    return this.http.post(this.svc.apiURL + 'users/' + newUser.username, newUser, httpOptions)
    .subscribe(user => {
      console.log(user);
      this.router.navigate(['/search-chords']);
    });
  }
}
