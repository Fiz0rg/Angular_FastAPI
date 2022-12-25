import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { Router } from '@angular/router';

import { UserService } from 'src/app/service/user-service/user.service';

@Component({
  selector: 'app-login-user',
  templateUrl: './login-user.component.html',
  styleUrls: ['./login-user.component.css']
})
export class LoginUserComponent implements OnInit {

  form: FormGroup;

  constructor(
    private loginForm: FormBuilder,
    private userService: UserService,
    private router: Router,
  ) {
    this.form = this.loginForm.group({
      username: '',
      password: '',
    });
   }

  ngOnInit(): void {
  }

  login(): void {

    let formData = new FormData();
    let formValue = this.form.value;

    for (let key in formValue) {
      formData.append(key, formValue[key])
    };

    formData.append('scope', 'buyer')

    this.userService.login("/token", formData).subscribe((res: any) => {
      if(res.access_token){
        localStorage.setItem("access_token", res.access_token)
        console.log(localStorage.getItem("access_token"))
        this.router.navigate(['/own_user'])
      }
    });
  }


}
