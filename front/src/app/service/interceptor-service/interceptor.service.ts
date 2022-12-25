import { Injectable } from '@angular/core';
import { HttpRequest, HttpHandler, HttpEvent } from '@angular/common/http';
import { Observable } from 'rxjs';


@Injectable()
export class InterceptorService {

  constructor() { }

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

    return next.handle(request)

  }


}
