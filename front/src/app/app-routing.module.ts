import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';

import { UserComponent } from './user/user.component';
import { RegistrationComponent } from './user/registration/registration.component';
import { CategoryComponent } from './categories/category/category.component'
import { CreateCategoryComponent } from './categories/create-category/create-category.component';
import { CreateGoodsComponent } from './goods/create-goods/create-goods.component';
import { GoodsComponent } from './goods/goods/goods.component';
import { LoginUserComponent } from './user/login-user/login-user.component';
import { TestComponent } from './user/test/test.component';
import { OwnUserComponent } from './user/own-user/own-user.component';
import { SortedCategoryComponent } from './categories/sorted-category/sorted-category.component';
import { GoodsDetailComponent } from './goods/goods-detail/goods-detail.component';
import { UserBasketComponent } from './basket/user-basket/user-basket.component';
import { HomePageComponent } from './home-page/home-page.component';
import { AuthGuardService } from './service/auth-guard/auth-guard.service';
import { LogoutComponent } from './user/logout/logout.component';


const routes: Routes = [
  {path: 'users', component: UserComponent},
  {path: 'registration', component: RegistrationComponent},
  {path: 'categories', component: CategoryComponent},
  {path: 'create_category', component: CreateCategoryComponent},
  {path: 'create_product', component: CreateGoodsComponent},
  {path: 'products', component: GoodsComponent},
  {path: 'login', component: LoginUserComponent},
  {path: 'test', component: TestComponent},
  {path: 'own_user', component: OwnUserComponent},
  {path: 'category/:categoryName', component: SortedCategoryComponent},
  {path: 'products/:productName', component: GoodsDetailComponent},
  {path: 'user_basket', component: UserBasketComponent},
  {path: 'home_page', component: HomePageComponent},
  {path: 'logout', component: LogoutComponent}
]


@NgModule({
  declarations: [],
  imports: [RouterModule.forRoot(routes), CommonModule],
  exports: [RouterModule]
})
export class AppRoutingModule { }
