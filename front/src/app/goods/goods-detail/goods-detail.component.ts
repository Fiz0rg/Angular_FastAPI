import { HttpResponse } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { map, tap } from 'rxjs';
import { GoodsSchema } from 'src/app/schemas/goods';
import { BasketService } from 'src/app/service/basket/basket.service';
import { GetGoodsService } from 'src/app/service/goods-service/get-goods.service';

@Component({
  selector: 'app-goods-detail',
  templateUrl: './goods-detail.component.html',
  styleUrls: ['./goods-detail.component.css']
})
export class GoodsDetailComponent implements OnInit {

  constructor(
    private route: ActivatedRoute,
    private goodsService: GetGoodsService,
    ) { }

  goodsName!: string
  productSchema: GoodsSchema[] = []

  ngOnInit(): void {

    const routeParams = this.route.snapshot.paramMap 
    const categoryNameFromPath = String(routeParams.get("productName"))

    this.goodsName = categoryNameFromPath
    console.log(categoryNameFromPath);
    
    this.getOneProduct()
  } 

  getOneProduct(): void {
    this.goodsService.getGoods("/get_all_products").pipe(
      map(dataObject => dataObject.filter(
        data => data.name == this.goodsName
      ))
    ).subscribe(result => this.productSchema = result)
  }

  addingInBasket(productName: string): void {

    const url = `/add_product_in_basket?product_name=${productName}`
    console.log(url);
    this.goodsService.addingProductInBasket(url, productName).subscribe()
  }

}
