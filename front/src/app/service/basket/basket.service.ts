import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Router } from '@angular/router';

import { catchError, Observable, throwError } from 'rxjs';
import { UserBasket } from 'src/app/schemas/basket';

@Injectable({
  providedIn: 'root'
})
export class BasketService {

  private baseBasketUrl = 'http://127.0.0.1:8000/basket'

  private handleError(error: HttpErrorResponse) {
    if (error.status === 0) {
      // A client-side or network error occurred. Handle it accordingly.
      console.error('An error occurred:', error.error);
    } else {
      // The backend returned an unsuccessful response code.
      // The response body may contain clues as to what went wrong.
      console.error(
        `Backend returned code ${error.status}, body was: `, error.error);
    }
    // Return an observable with a user-facing error message.
    return throwError(() => new Error('Something bad happened; please try again later.'));
  }

  constructor(
    private http: HttpClient,
    private router: Router
  ) { }


  getBasket(url: string): Observable<UserBasket[]> {
    return this.http.get<UserBasket[]>(this.baseBasketUrl + url).pipe(
      catchError(this.handleError)
    )
  }

}
