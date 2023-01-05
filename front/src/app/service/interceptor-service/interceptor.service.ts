import { Injectable } from '@angular/core';
import { HttpRequest, HttpHandler, HttpEvent, HttpErrorResponse, HttpInterceptor } from '@angular/common/http';

import { Router } from '@angular/router';

import {Observable, tap } from 'rxjs';


@Injectable()
export class InterceptorService implements HttpInterceptor {

  constructor(
    private router: Router,
  ) { }

  intercept(
    request: HttpRequest<any>,
    next: HttpHandler,
  ): Observable<HttpEvent<any>> {
    if(!request.headers.has("Authorization")){
      request = request.clone({setHeaders: {
        'Accept': 'application/x-www-form-urlencoded',
          } }).clone({
        setHeaders: {
          Authorization: `Bearer ${localStorage.getItem('access_token')}`
        } 
      });
      if(!localStorage.getItem("access_token_create_time")){
        localStorage.setItem("access_token_create_time", String(Date.now()))
      }
    }
    
    const b = localStorage.getItem("access_token_create_time")
    const asd = Date.now()

    if(localStorage.getItem('access_token')){
      if(Date.now() - (Number(b!)) > 900000) {
        localStorage.clear()
      }
    }
  

    return next.handle(request).pipe(
      tap({
        error: (error) => {
          if(error instanceof HttpErrorResponse) {
            if(error.status === 401) {
              this.router.navigate(['/login'])
            }
          }
        }
      })
    )
  }
}
