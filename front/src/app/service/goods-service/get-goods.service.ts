import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

import { Observable } from 'rxjs';
import { Goods } from 'src/app/schemas/goods';

@Injectable({
  providedIn: 'root'
})
export class GetGoodsService {

  baseGoodsUrl = 'http://127.0.0.1:8000/product'

  constructor(
    private http: HttpClient
  ) { }

  getGoods(url: string): Observable<Goods[]> {
    return this.http.get<Goods[]>(this.baseGoodsUrl + url)
  }

  createGoods(url: string, object: object): Observable<Goods> {
    return this.http.post<Goods>(this.baseGoodsUrl + url, object)
  }

}
