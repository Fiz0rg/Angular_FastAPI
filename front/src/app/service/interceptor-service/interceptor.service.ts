import { Injectable } from '@angular/core';
import { HttpRequest, HttpHandler, HttpEvent, HttpErrorResponse, HttpInterceptor } from '@angular/common/http';

import { Router } from '@angular/router';

import { catchError, Observable, tap } from 'rxjs';


@Injectable()
export class InterceptorService implements HttpInterceptor {

  protected handleAuth

  constructor(
    private router: Router,
  ) { }

  intercept(
    request: HttpRequest<any>,
    next: HttpHandler,
  ): Observable<HttpEvent<any>> {
    request = request.clone({setHeaders: {
      'Accept': 'application/x-www-form-urlencoded',
        } }).clone({
      setHeaders: {
        Authorization: `Bearer ${localStorage.getItem('access_token')}`
      }
    });

    return next.handle(request).pipe(
      catchError((error: HttpErrorResponse) => )
    )
  }
}
