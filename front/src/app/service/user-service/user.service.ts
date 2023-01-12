import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';

import { Observable } from 'rxjs';
import { UserSchema } from 'src/app/schemas/user';

import { UsernamePasswordUserSchema, User } from 'src/app/schemas/user';


@Injectable({
  providedIn: 'root'
})
export class UserService {

  private UsersLink = 'http://127.0.0.1:8000/user'

  httpOptions = {
    headers: new HttpHeaders({
      'Accept': 'application/x-www-form-urlencoded',
    })
  };

  constructor(
    private http: HttpClient,
  ) { }

  getUsers(url: string): Observable<User[]> {
    return this.http.get<User[]>(this.UsersLink + url)
  }

  createUser(url: string, user: object): Observable<UsernamePasswordUserSchema> {
    return this.http.post<UsernamePasswordUserSchema>(this.UsersLink+url, user)
  }

  login(url: string, login: object): Observable<UsernamePasswordUserSchema> {    
    return this.http.post<UsernamePasswordUserSchema>(this.UsersLink + url, login)
  }

  getCurrentUser(url: string): Observable<UserSchema> {
    return this.http.get<UserSchema>(this.UsersLink + url)
  }

}
