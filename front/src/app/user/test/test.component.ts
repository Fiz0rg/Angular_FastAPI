import { Component, OnInit } from '@angular/core';

import { UserService } from 'src/app/service/user-service/user.service';

@Component({
  selector: 'app-test',
  templateUrl: './test.component.html',
  styleUrls: ['./test.component.css']
})
export class TestComponent implements OnInit {

  constructor(
      private userService: UserService,
    ) {}

  ngOnInit(): void {
  }

  test(): void {
  };

}
