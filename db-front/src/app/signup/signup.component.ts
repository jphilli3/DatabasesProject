import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { ApiService } from '../api.service';
import { Router } from '@angular/router';
import { Observable } from 'rxjs';
import { tap, catchError } from 'rxjs/operators';

@Component({
    selector: 'app-signup',
    templateUrl: './signup.component.html',
    styleUrls: ['./signup.component.css']
  })
export class SignUpComponent implements OnInit {
    constructor(private svc: ApiService, private http: HttpClient, private router: Router) {}

    username: String = '';
    response: any;

    ngOnInit() {
    }

    createNewUser(event) {
        event.preventDefault();
        const target = event.target;
        const username = target.querySelector('#username').value;
        const first_name = target.querySelector('#first_name').value;
        const last_name = target.querySelector('#last_name').value;
        const password = target.querySelector('#password1').value;
        console.log('TEST');
        const httpOptions = {
          headers: new HttpHeaders({
            'Content-Type':  'application/json',
            'Accept': 'application/json'
          })
        };
        this.http.post(this.svc.apiURL + 'users/', {
          'username': username,
          'password': password,
          'first_name': first_name,
          'last_name': last_name,
          'level': 1
        }, httpOptions)
          .subscribe(data => {
            this.router.navigate(['/search-chords']);
           }, error => {
            console.log(error);
          });
      }
}
