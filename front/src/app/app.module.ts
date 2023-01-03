import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule, HTTP_INTERCEPTORS } from "@angular/common/http";

import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import {
  MatButtonModule,
  MatMenuModule,
  MatToolbarModule,
  MatIconModule,
  MatCardModule,
  MatInputModule,
} from '@angular/material';

import { MatListModule } from '@angular/material/list'
import { MatSelectModule } from '@angular/material/select';

import { AppComponent } from './app.component';
import { UserComponent } from './user/user.component';
import { UserDetailComponent } from './user-detail/user-detail.component';
import { AppRoutingModule } from './app-routing.module';
import { RegistrationComponent } from './user/registration/registration.component';
import { CategoryComponent } from './categories/category/category.component';
import { CreateCategoryComponent } from './categories/create-category/create-category.component';
import { CreateGoodsComponent } from './goods/create-goods/create-goods.component';
import { GoodsComponent } from './goods/goods/goods.component';
import { LoginUserComponent } from './user/login-user/login-user.component';
import { TestComponent } from './user/test/test.component';
import { OwnUserComponent } from './user/own-user/own-user.component';
import { InterceptorService } from './service/interceptor-service/interceptor.service';
import { SortedCategoryComponent } from './categories/sorted-category/sorted-category.component';
import { GoodsDetailComponent } from './goods/goods-detail/goods-detail.component';
import { UserBasketComponent } from './basket/user-basket/user-basket.component';


@NgModule({
  declarations: [
    AppComponent,
    UserComponent,
    UserDetailComponent,
    RegistrationComponent,
    CategoryComponent,
    CreateCategoryComponent,
    CreateGoodsComponent,
    GoodsComponent,
    LoginUserComponent,
    TestComponent,
    OwnUserComponent,
    SortedCategoryComponent,
    GoodsDetailComponent,
    UserBasketComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    
    FormsModule,
    ReactiveFormsModule,

    MatButtonModule,
    MatMenuModule,
    MatToolbarModule,
    MatIconModule,
    MatCardModule,
    MatListModule,
    MatSelectModule,
    MatInputModule,

    BrowserAnimationsModule 
  ],
  providers: [
    {
      provide: HTTP_INTERCEPTORS,
      useClass: InterceptorService,
      multi: true,
  }],
  bootstrap: [AppComponent]
})
export class AppModule { }
