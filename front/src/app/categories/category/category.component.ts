import { Component, OnInit } from '@angular/core';

import { CategoryService } from 'src/app/service/category-service/category.service';
import { Category } from 'src/app/schemas/categories';

@Component({
  selector: 'app-category',
  templateUrl: './category.component.html',
  styleUrls: ['./category.component.css']
})
export class CategoryComponent implements OnInit {

  categories: Category[] = [];

  constructor(
    private categoryService: CategoryService,
  ) { }

  ngOnInit(): void {
    this.getAllCategories()
  }

  getAllCategories(): void {
    this.categoryService.getAllCategories('/get_all').subscribe(data => this.categories = data)
  }

}
