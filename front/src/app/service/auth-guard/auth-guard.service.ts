import { Injectable } from '@angular/core';
import { Router, ActivatedRouteSnapshot, RouterStateSnapshot } from '@angular/router';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthGuardService {

  constructor(
    private router: Router
  ) { }


  canActivate(next: ActivatedRouteSnapshot, state: RouterStateSnapshot): Observable<boolean> | Promise<boolean> | boolean {
    if(localStorage.getItem("access_token")) {
      console.log(localStorage.getItem("access_token"));
      console.log("dasdasdddddddddddddddddddddddddddddddddddddddd");
      
      
      return true;
    }

    this.router.navigate(['/login']);

    return false;
  }
}
