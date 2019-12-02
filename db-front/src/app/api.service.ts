import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from "../environments/environment";


@Injectable({
  providedIn: 'root'
})
export class ApiService {
  apiURL = environment.apiURL
  constructor(private http: HttpClient) {}

  getUserDetails(username){
    return this.http.get(this.apiURL+"getUserDetails/{user}?username="+username)
    .subscribe((response)=>{
      console.log(response)
    })
  }

}

