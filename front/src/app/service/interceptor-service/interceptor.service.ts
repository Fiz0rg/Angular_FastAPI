import { Injectable } from '@angular/core';
import { HttpRequest, HttpHandler, HttpEvent, HttpErrorResponse, HttpInterceptor } from '@angular/common/http';

import { Router } from '@angular/router';

import {Observable, tap, throwError } from 'rxjs';


@Injectable()
export class InterceptorService implements HttpInterceptor {

  constructor(
    private router: Router,
  ) { }

  protected AuthErrorHandler(error: HttpErrorResponse): Observable<any> | undefined{
    if(error.status == 401) {
      if(localStorage.getItem("refresh_token")){
        console.log(localStorage.getItem("refresh_token"));
        return throwError(error);
      }
    }
    return;
  }

  intercept(
    request: HttpRequest<any>,
    next: HttpHandler,
  ): Observable<HttpEvent<any>> {
    // request = request.clone({setHeaders: {
    //   "Accept": "application/x-www-form-urlencoded",
    //   "Content-Type": "application/x-www-form-urlencoded"
    // }})


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
            if(error.status === 401) {
              this.AuthErrorHandler(error)
              this.router.navigate(['/login'])
            }
          }
        }
      })
    )
  }
}
