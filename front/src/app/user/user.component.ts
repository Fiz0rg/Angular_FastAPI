import { Component, OnInit } from '@angular/core';

import { FormGroup, FormBuilder, FormControl } from '@angular/forms';

import { UserService } from 'src/app/service/user-service/user.service';

import { UsernamePasswordUserSchema, User } from '../schemas/user';

@Component({
  selector: 'app-user',
  templateUrl: './user.component.html',
  styleUrls: ['./user.component.css']
})
export class UserComponent implements OnInit {

  users: User[] = [];
  currentUser?: User;

  constructor(private userService: UserService,
              private form: FormBuilder,          
    ) { }

  ngOnInit(): void {
    this.getUsers() 
    console.log(this.users);
    
  }

  userForm = this.form.group<UsernamePasswordUserSchema>({
    username: "",
    password: "",
  })

  selectUser(user: User): void {
    this.currentUser = user;
  }

  getUsers(): void {
    this.userService.getUsers('/get_all').subscribe(users => this.users = users)
  };

}
