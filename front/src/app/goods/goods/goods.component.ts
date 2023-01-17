import { Component, OnInit } from '@angular/core';

import { GoodsSchema } from 'src/app/schemas/goods';
import { GetGoodsService } from 'src/app/service/goods-service/get-goods.service';
import { UserService } from 'src/app/service/user-service/user.service';

@Component({
  selector: 'app-goods',
  templateUrl: './goods.component.html',
  styleUrls: ['./goods.component.css']
})
export class GoodsComponent implements OnInit {

  goods: GoodsSchema[] = [];
  user: boolean = false; 

  constructor(
    private goodsService: GetGoodsService,
    private userService: UserService,
  ) { }

  ngOnInit(): void {
    this.getGoods()
    this.isAdminUser()    
  }

  getGoods(): void {
    this.goodsService.getGoods("/get_all_products").subscribe(goods => this.goods = goods)
  }

  isAdminUser(): void {
    if(localStorage.getItem("access_token")){
      this.userService.getCurrentUser("/me").subscribe(user => this.user = user.is_admin)
    }
  }

}
