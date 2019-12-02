import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from "../environments/environment";


@Injectable({
  providedIn: 'root'
})
export class ApiService {
  apiURL = environment.apiURL
  constructor(private http: HttpClient) {}

  

  }


