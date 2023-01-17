import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { GoodsSchema } from 'src/app/schemas/goods';
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
    private router: Router,
    ) { }

  productName!: string
  productSchema!: GoodsSchema

  ngOnInit(): void {

    const routeParams = this.route.snapshot.paramMap 
    const categoryNameFromPath = String(routeParams.get("productName"))

    this.productName = categoryNameFromPath
    
    this.getOneProduct()
  } 

  getOneProduct(): void {
    let url = `/${this.productName}`
    this.goodsService.getOneProduct(url).subscribe(result => this.productSchema = result)
  }


  addingInBasket(productName: string): void {
    const url = `/add_product_in_basket?product_name=${productName}`
    this.goodsService.addingProductInBasket(url, productName).subscribe( (res:any) => {
      if(res.status_response == 200) {
        this.router.navigate(['/products'])
      }
    })
  }

}
