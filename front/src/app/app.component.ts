import { Component, OnInit } from '@angular/core';
import { UserService } from './service/user-service/user.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {

  currentUser: boolean = false

  constructor(
    private userService: UserService,
  ){}

  ngOnInit(): void {
    this.getUser()
    console.log(this.currentUser);
    
  }

  getUser(): void {
    this.userService.getCurrentUser("/me").subscribe(data => this.currentUser = data.is_admin)
  }

}
