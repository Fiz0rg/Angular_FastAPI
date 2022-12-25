import { Component, OnInit, Input } from '@angular/core';
import { User } from "../user"
import { UserService } from 'src/app/service/user-service/user.service';


@Component({
  selector: 'app-user-detail',
  templateUrl: './user-detail.component.html',
  styleUrls: ['./user-detail.component.css']
})
export class UserDetailComponent implements OnInit {

  @Input() user?: User;

  constructor(private userService: UserService) { }

  ngOnInit(): void {
  }



}
