import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

const baseAPIURL = 'http://127.0.0.1:8000/';
const healthURL = baseAPIURL + 'health';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(private http: HttpClient) { }
  getHealth() {
    this.http.get(healthURL, {observe: 'response'}).subscribe( res => {
      console.log(res.body);
    });
  }
}
