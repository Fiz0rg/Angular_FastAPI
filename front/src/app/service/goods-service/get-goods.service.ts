import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

import { map, Observable } from 'rxjs';
import { GoodsSchema } from 'src/app/schemas/goods';

@Injectable({
  providedIn: 'root'
})
export class GetGoodsService {

  baseGoodsUrl = 'http://127.0.0.1:8000/product'

  constructor(
    private http: HttpClient
  ) { }

  getGoods(url: string): Observable<GoodsSchema[]> {
    return this.http.get<GoodsSchema[]>(this.baseGoodsUrl + url)
  }

  createGoods(url: string, object: object): Observable<GoodsSchema> {
    return this.http.post<GoodsSchema>(this.baseGoodsUrl + url, object)
  }

  addingProductInBasket(url: string, productName: string): Observable<string> {
    return this.http.post<string>(this.baseGoodsUrl + url, productName)
  }

}
