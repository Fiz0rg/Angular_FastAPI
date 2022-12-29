import { Component, OnInit } from '@angular/core';
import { UserBasket } from 'src/app/schemas/basket';

import { BasketService } from 'src/app/service/basket/basket.service';

@Component({
  selector: 'app-user-basket',
  templateUrl: './user-basket.component.html',
  styleUrls: ['./user-basket.component.css']
})
export class UserBasketComponent implements OnInit {

  goods: UserBasket[] = []

  constructor(
    private basketService: BasketService,
  ) { }

  ngOnInit(): void {
    this.getUserBasket()
  }

  getUserBasket(): void {
    this.basketService.getBasket("/get_my_basket").subscribe(goods => this.goods = goods)
  }

}
