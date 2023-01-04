import { Component, OnInit } from '@angular/core';
import { map } from 'rxjs';
import { GoodsSchema } from '../schemas/goods';
import { GetGoodsService } from '../service/goods-service/get-goods.service';

@Component({
  selector: 'app-home-page',
  templateUrl: './home-page.component.html',
  styleUrls: ['./home-page.component.css']
})
export class HomePageComponent implements OnInit{

  popularGoods: GoodsSchema[] = []

  constructor(
    private goodsService: GetGoodsService,
  ) {}

  ngOnInit(): void {
    this.getMostPopGoods()
  }

  getMostPopGoods(): void {
    this.goodsService.getGoods("/get_ten_goods").subscribe(product => this.popularGoods = product)
  }


}
