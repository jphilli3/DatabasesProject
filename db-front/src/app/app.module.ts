import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent, SearchButtonComponent } from './app.component';

@NgModule({
  declarations: [
    AppComponent,
    SearchButtonComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent, SearchButtonComponent]
})
export class AppModule { }
