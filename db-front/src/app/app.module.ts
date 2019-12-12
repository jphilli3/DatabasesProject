import { SearchProgressionsComponent, SearchProgressionBarComponent, ProgressionViewComponent } from './search-progressions/search-progressions.component';
import { SearchSongsComponent, SearchSongBarComponent, SongViewComponent } from './search-songs/search-songs.component';

import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { RouterModule, Routes } from '@angular/router';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SearchBarComponent, ChordViewComponent, SearchChordsComponent } from './search-chords/search-chords.component';
import { HttpClientModule } from '@angular/common/http';
import { LoginComponent } from './login/login.component';
import { HomeComponent, UsernameComponent } from './home/home.component';
import { KnownChordComponent } from './home/home.component';
import { PageNotFoundComponent } from './page-not-found/page-not-found.component';
import { SignUpComponent } from './signup/signup.component';

@NgModule({
  declarations: [
    AppComponent,
    SearchBarComponent,
    ChordViewComponent,
    LoginComponent,
    HomeComponent,
    SearchChordsComponent,
    PageNotFoundComponent,
    SignUpComponent,
    KnownChordComponent,
    UsernameComponent,
    SearchSongsComponent,
    SearchSongBarComponent,
    SongViewComponent,
    SearchProgressionsComponent,
    SearchProgressionBarComponent,
    ProgressionViewComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule
    
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
