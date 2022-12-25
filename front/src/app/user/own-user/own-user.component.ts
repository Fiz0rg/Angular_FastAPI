import { Component, OnInit } from '@angular/core';

import { UserService } from 'src/app/service/user-service/user.service';
import { UserId } from 'src/app/user';

@Component({
  selector: 'app-own-user',
  templateUrl: './own-user.component.html',
  styleUrls: ['./own-user.component.css']
})
export class OwnUserComponent implements OnInit {

  user?: UserId

  constructor(
    private userService: UserService,
  ) { }

  ngOnInit(): void {
    this.getUser()

  }

  getUser(): void {
    this.userService.getCurrentUser('/users/me').subscribe(data => this.user = data)
  }

}
