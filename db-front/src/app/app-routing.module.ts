import { NgModule } from '@angular/core';
import { Route, RouterModule } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { HomeComponent } from './home/home.component';
import { SearchChordsComponent } from './search-chords/search-chords.component';
import { PageNotFoundComponent } from './page-not-found/page-not-found.component';

const routes: Route[] = [
  {path: "", redirectTo: "/login", pathMatch: "full"},
  {path: "login", component: LoginComponent},
  {path: "home", component: HomeComponent},
  //to do child routes
  // {path: "home", component: HomeComponent, children: [{path: "childPage", component: childPageComponent}]}
  // if you utilize children in routes, you must add <router-outlet> </router-outlet> in the childPageComponent.html page 
  {path: "search-chords", component: SearchChordsComponent},
  {path: "**", component: PageNotFoundComponent},

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
