import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { Observable } from 'rxjs';
import { UserBasket } from 'src/app/schemas/basket';

@Injectable({
  providedIn: 'root'
})
export class BasketService {

  private baseBasketUrl = 'http://127.0.0.1:8000/basket'

  constructor(
    private http: HttpClient,
  ) { }


  getBasket(url: string): Observable<UserBasket[]> {
    return this.http.get<UserBasket[]>(this.baseBasketUrl + url)
  }

}
