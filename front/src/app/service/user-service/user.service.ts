import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';

import { Observable } from 'rxjs';

import { CreateUser, User, UserId } from 'src/app/user';


@Injectable({
  providedIn: 'root'
})
export class UserService {

  private UsersLink = 'http://127.0.0.1:8000/user'

  httpOptions = {
    headers: new HttpHeaders({
      'accept': 'application/x-www-form-urlencoded',
    })
  };

  constructor(
    private http: HttpClient,
  ) { }

  getUsers(url: string): Observable<User[]> {
    return this.http.get<User[]>(this.UsersLink + url)
  }

  createUser(url: string, user: object): Observable<CreateUser> {
    return this.http.post<CreateUser>(this.UsersLink+url, user)
  }

  login(url: string, login: FormData): Observable<CreateUser> {
    return this.http.post<CreateUser>(this.UsersLink + url, login, this.httpOptions)
  }

  getCurrentUser(url: string): Observable<UserId> {

    // console.log(this.UsersLink + url)
    return this.http.get<UserId>(this.UsersLink + url)
  }

}
