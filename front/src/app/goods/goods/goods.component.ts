import { Component, OnInit } from '@angular/core';

import { GoodsSchema } from 'src/app/schemas/goods';
import { GetGoodsService } from 'src/app/service/goods-service/get-goods.service';

@Component({
  selector: 'app-goods',
  templateUrl: './goods.component.html',
  styleUrls: ['./goods.component.css']
})
export class GoodsComponent implements OnInit {

  goods: GoodsSchema[] = [];

  constructor(
    private service: GetGoodsService,
  ) { }

  ngOnInit(): void {
    this.getGoods()
  }

  getGoods(): void {
    this.service.getGoods("/get_all_products").subscribe(goods => this.goods = goods)
  }

}
