import { Component, OnInit } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { Router } from '@angular/router';

import { GetGoodsService } from 'src/app/service/goods-service/get-goods.service';

@Component({
  selector: 'app-create-goods',
  templateUrl: './create-goods.component.html',
  styleUrls: ['./create-goods.component.css']
})
export class CreateGoodsComponent implements OnInit {

  goodsForm = this.form.group({
    name: '',
    price: '',
    category: '',
  })

  constructor(
    private form: FormBuilder,
    private service: GetGoodsService,
    private router: Router,
  ) { }

  ngOnInit(): void {
  }

  createGoods(): void {
    
    this.service.createGoods("/create_product", this.goodsForm.value).subscribe( (res: any) => {
      if(res) {
        this.router.navigate(['/products'])
      }
    })
  }

}
