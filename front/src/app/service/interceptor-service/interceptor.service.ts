import { Injectable } from '@angular/core';
import { HttpRequest, HttpHandler, HttpEvent, HttpErrorResponse, HttpInterceptor, HttpClient, HttpHeaders } from '@angular/common/http';

import { Router } from '@angular/router';

import {Observable, tap, throwError } from 'rxjs';


@Injectable()
export class InterceptorService implements HttpInterceptor {

  constructor(
    private router: Router,
    private http: HttpClient,
  ) { }

  protected AuthErrorHandler(error: HttpErrorResponse): Observable<any> | undefined{
    if(error.status == 401) {
      this.router.navigate(['/login'])      
      return ;}
    
    if(error.status == 422) {      
      if(localStorage.getItem("refresh_token")){
        try{
          const a = this.http.post<string>("http://127.0.0.1:8000/user/refresh_token", localStorage.getItem("refresh_token")).subscribe()
        } catch(error) {
          console.log("Error");
          
          this.router.navigate(['/login'])
        }
        return throwError(error);
      }
    }
    else {
      console.log("No");
      
    }
    return;
  } 

  intercept(
    request: HttpRequest<any>,
    next: HttpHandler,
  ): Observable<HttpEvent<any>> {


    if(request.headers.has("Content-Type")) {
      request = request.clone({setHeaders: {
        "Content-Type": "application/json"
      }})
    }
    if(localStorage.getItem("access_token")) {
      request = request.clone({ setHeaders: {
        "Authorization": `Bearer ${localStorage.getItem("access_token")}`
      }})
    }

    return next.handle(request).pipe(
      tap({
        error: (error) => {
          if(error instanceof HttpErrorResponse) {
              this.AuthErrorHandler(error)
          }
        }
      })
    )
  }
}
