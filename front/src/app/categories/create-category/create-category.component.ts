import { Component, OnInit } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { Router } from '@angular/router';

import { CategoryService } from 'src/app/service/category-service/category.service';

@Component({
  selector: 'app-create-category',
  templateUrl: './create-category.component.html',
  styleUrls: ['./create-category.component.css']
})
export class CreateCategoryComponent implements OnInit {

  category = this.form.group({
    category_name: ''
  })

  constructor(
    private form: FormBuilder,
    private categoryService: CategoryService,
    private router: Router,
  ) { }

  ngOnInit(): void {
  }

  newCategory(): void {    
    this.categoryService.createCategory("/create_category", this.category.value).subscribe(res => 
      this.router.navigate(['categories']))
  }


}
