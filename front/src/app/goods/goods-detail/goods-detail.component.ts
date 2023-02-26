import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { GoodsSchema } from 'src/app/schemas/goods';
import { GetGoodsService } from 'src/app/service/goods-service/get-goods.service';
import { UserService } from 'src/app/service/user-service/user.service';

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
    private userService: UserService,
    ) { }

  productName!: string
  productSchema!: GoodsSchema
  is_authorized!: boolean

  ngOnInit(): void {

    const routeParams = this.route.snapshot.paramMap 
    const categoryNameFromPath = String(routeParams.get("productName"))

    this.productName = categoryNameFromPath
    
    this.checkIfAuthorized()

    this.getOneProduct()
  } 

  checkIfAuthorized(): void {
    this.userService.getCurrentUser("/me").subscribe((res: any) => {
      if(res) {
        this.is_authorized = true
        console.log(this.is_authorized)
      }}
    )
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
