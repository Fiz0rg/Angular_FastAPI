import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import { GoodsSchema } from 'src/app/schemas/goods';
import { CategoryService } from 'src/app/service/category-service/category.service';

@Component({
  selector: 'app-sorted-category',
  templateUrl: './sorted-category.component.html',
  styleUrls: ['./sorted-category.component.css']
})
export class SortedCategoryComponent implements OnInit {

  constructor(
    private route: ActivatedRoute,
    private categoryService: CategoryService,
    ) { }

  categoryName!: string;

  goodsByNameCategory: GoodsSchema[] = []

  ngOnInit(): void {
    const routeParams = this.route.snapshot.paramMap 
    const categoryNameFromPath = String(routeParams.get("categoryName"))

    this.categoryName = categoryNameFromPath

    this.getGoodsByCategoryName()
  }


  getGoodsByCategoryName(): void {
    
    this.categoryService.getGoodsByCategoryName(`/${this.categoryName}`).subscribe(data => this.goodsByNameCategory = data)
  }

}
