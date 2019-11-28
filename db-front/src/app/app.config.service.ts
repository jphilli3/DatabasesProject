import { Health } from './health';
import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpResponse} from '@angular/common/http';
import {Observable} from 'rxjs/Observable';

const httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};
@Injectable({
  providedIn: 'root'
})
export class ConfigService {

    constructor(private http: HttpClient) { }

    baseAPIURL = 'http://127.0.0.1:8000/health';

    getHealth(): Observable<HttpResponse<any>> {
        return this.http.get<any>(this.baseAPIURL, httpOptions);
    }
}