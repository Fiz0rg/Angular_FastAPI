import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

import { UserService } from 'src/app/service/user-service/user.service';
import { UserId } from 'src/app/schemas/user';

@Component({
  selector: 'app-own-user',
  templateUrl: './own-user.component.html',
  styleUrls: ['./own-user.component.css']
})
export class OwnUserComponent implements OnInit {

  user?: UserId

  constructor(
    private userService: UserService,
    private router: Router,
  ) { }

  ngOnInit(): void {
    this.getUser()
  }

  getUser(): void {
    this.userService.getCurrentUser('/users/me').subscribe(data => this.user = data)
  }
  
  logout(): void {
    localStorage.clear();
    this.router.navigate(['/home_page'])
  }

}
