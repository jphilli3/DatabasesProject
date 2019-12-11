import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { ApiService } from '../api.service';
import { Router } from '@angular/router';
import { Observable } from 'rxjs';
import { tap, catchError } from 'rxjs/operators';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  constructor(private svc: ApiService, private http: HttpClient, private router: Router){}
  
  username: String = '';
  response: any;

  user: any = [];
  
  ngOnInit() {
  }


  loginUser(event) {
    event.preventDefault();
    const target = event.target;
    const username = target.querySelector('#username').value;
    const password = target.querySelector('#password').value;
    const obs = this.http.get(this.svc.apiURL + 'users/' + username);
    obs.subscribe((response) => {
      console.log(response);
      this.user = response;
      if (this.user.password === password) {
        this.router.navigate(['/home']);
      }
    });
  } 
}
