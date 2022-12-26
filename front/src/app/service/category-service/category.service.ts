import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Category } from 'src/app/schemas/categories';

@Injectable({
  providedIn: 'root'
})
export class CategoryService {

  private baseCategoryUrl = 'http://127.0.0.1:8000/category';

  constructor(
    private http: HttpClient,
  ) { }

  getAllCategories(url: string): Observable<Category[]> {
    return this.http.get<Category[]>(this.baseCategoryUrl + url)
  }

  createCategory(url: string, object: object): Observable<Category>{
    return this.http.post<Category>(this.baseCategoryUrl + url, object)
  }
}
