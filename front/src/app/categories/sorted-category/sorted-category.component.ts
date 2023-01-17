import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import { GetGoodsService } from 'src/app/service/goods-service/get-goods.service';
import { GoodsSchema } from 'src/app/schemas/goods';
import { map } from 'rxjs';

@Component({
  selector: 'app-sorted-category',
  templateUrl: './sorted-category.component.html',
  styleUrls: ['./sorted-category.component.css']
})
export class SortedCategoryComponent implements OnInit {

  constructor(
    private route: ActivatedRoute,
    private goodsService: GetGoodsService,
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
    
    this.goodsService.getGoods("/get_all_products").pipe(
      map(dataArray => dataArray.filter(
        dataObject => dataObject.category.name == this.categoryName
      ))
    ).subscribe(data => this.goodsByNameCategory = data)
  }

}
