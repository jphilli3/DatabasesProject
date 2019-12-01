import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class FastApiService {

  printToConsole(arg){
    console.log(arg);
  }
}
