import { Component, OnInit, ViewChild } from '@angular/core';

import { CategoryService } from 'src/app/service/category-service/category.service';
import { Category } from 'src/app/schemas/categories';
import { UserService } from 'src/app/service/user-service/user.service';

@Component({
  selector: 'app-category',
  templateUrl: './category.component.html',
  styleUrls: ['./category.component.css']
})
export class CategoryComponent implements OnInit {

  categories: Category[] = [];

  is_admin: boolean = false;

  constructor(
    private categoryService: CategoryService,
    private userService: UserService,
  ) { }

  ngOnInit(): void {
    this.getAllCategories()
    this.getCurrentUser()
  }

  getAllCategories(): void {
    this.categoryService.getAllCategories('/get_all').subscribe(data => this.categories = data)
  }

  getCurrentUser(): void {
    if(localStorage.getItem("access_token")){
      this.userService.getCurrentUser('/me').subscribe(user => this.is_admin = user.is_admin)
    }
  }

}
