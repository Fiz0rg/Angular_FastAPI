import { Component, OnInit } from '@angular/core';
import { FormBuilder } from '@angular/forms'
import { Router } from '@angular/router'

import { CreateUser } from 'src/app/user';
import { UserService } from 'src/app/service/user-service/user.service';

@Component({
  selector: 'app-registration',
  templateUrl: './registration.component.html',
  styleUrls: ['./registration.component.css']
})
export class RegistrationComponent implements OnInit {

  constructor(private userService: UserService,
              private formBuilder: FormBuilder,
              private router: Router,          
    ) { }

  url = "/registration"

  userForm = this.formBuilder.group<CreateUser>({
    username: '',
    password: '',
  })

  ngOnInit(): void {
  }

  createUser(): void {
    this.userService.createUser(this.url, this.userForm.value).subscribe( (res:any) =>
      this.router.navigate(['/login'])
    )
  }

}
