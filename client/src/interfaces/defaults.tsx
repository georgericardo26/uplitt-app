import { AxiosRequestConfig } from "axios";
import { types } from "util";

export interface IProps {
    children: React.ReactNode
}


export interface ITopBar {
    children: React.ReactNode
}

export interface ISignUP {
    handleSubmit: (event: any) => void,
    ErrorDisplay?: string
}

export interface IAddRestaurant {
    handleSubmit: (event: any) => void,
    handleRestaurantForm: (event: any) => void,
    ErrorDisplay?: string,
    showRestaurantForm: boolean,
    getImage: (event: any) => void,
    loadScript: (url: any, callback: any) => void,
    handleScriptLoad: (updateQuery: any, autoCompleteRef: any, setError: any) => void
}


export type ObjFields = {
    first_name?: string,
    last_name?: string,
    username?: string,
    email?: string,
    phone_number?: string,
    password?: string,
    re_password?: string
}

export type CategoryFields = {
    name?: string,
    description?: string
}

export type FoodItemFields = {
    title?: string,
    description?: string,
    foodItemCategory_pk?: number,
    price?: string,
    image?: number,
    tags?: any,
    ingredientItems?: any
}

export interface ITagsIds {
    [key: number]: any
}

export type TypeTag = {
   id?: number,
   updateAt?: string,
   createAt?: string,
   name?: string,
   description?: string,
   color?: string
}

export type ListCategoriesFields = {
    id?: number,
    name?: string,
    description?: string
}

export type TypeFoodCategoryField = {
    id?: number,
    title?: string,
    description?: string,
    virtualshop?: number
}

export type CreateRestaurantFields = {
    name?: string,
	phoneNumber?: string,
    AddressLine1?: string,
    AddressLine2?: string,
    city?: string,
    stateProvinceRegion?: string,
    country?: string,
    postalCode?: string,
}

export type GoogleAddressFields = {
    city?: string,
	state?: string,
    country?: string,
    postalCode?: string,
    lat?: number,
    lng?: number
}

export type MenuFields = {
    address_line1?: string,
    address_line2?: string,
    city?: string,
    state?: string,
    country?: string,
    zipcode?: string
}

export type ItemsType = {
    name: string
}

export type IGridOption = {
    grid: string
}

export type TypeProfileTopBar = {
    grid: string
    profileName?: string
}

export interface IRequestData {
    url: string,
    bodyData?: Object,
    header?: Object
}

export type IResponseData = {
    status?: number,
    data?: Object
}

export type ItypeAlert = {
    sucess: string,
    info: string,
    warning: string,
    danger: string,
    primary: string,
    secondary: string,
    dark: string,
    light: string
}

export type IAlertProps = {
    title: string,
    message: string, 
    type: string,
    display: string
}

export type ISignUpSucess = {
    account_creation: string
}

export interface IFoodCategoriesList {
    count?: number,
    next?: string | null,
    previous?: string | null,
    results?: Array<ICategoryItem>
}

export interface ICategoryItem {
    id: number,
    title: string,
    description: string | null,
    foodItems: Array<IFoodItem>
}

export interface IFoodItem {
    id: number,
    title: string,
    description: string | null,
    price: string | null,
    food_item_image: IImage
}

export interface IImage {
    id: number,
    name: string,
    url: string | null,
    image_path?: string
}

export interface TypeOBJCurrentFoodItemField {
    id?: number,
    title?: string,
    description?: string,
    price?: string,
    food_item_image?: Object,
    foodItemCategory?: Object,
    virtualshop?: Object,
    updateAt?: string,
    createAt?: string
}
/*
createAt: "2021-05-22T20:56:39.918100Z"
description: "Lorem Ipsum Test"
foodItemCategory: {id: 3, url: "http://localhost:8000/api/v1/food-items-categories/3/", title: "Wine"}
food_item_image: {id: 26, url: "http://localhost:8000/static/images/others/2021-05….827033Captura_de_Tela_2021-05-20_as_13.07.04.png"}
id: 5
price: "8.50"
title: "Wine 1"
updateAt: "2021-05-22T20:56:39.918056Z"
virtualshop: {id: 17, name: "Coco Bambu"}
*/
export interface IfoodItemImage {
    id?: number,
    url?: string
}
export interface IfoodItemCategory {
    id?: number,
    url?: string,
    title?: string
}
export interface Ivirtualshop {
    id?: number,
    name?: string
}
export interface TypeOBJFoodItemField {
    title?: string,
    description?: string,
    foodItemCategory_pk?: number,
    price?: string
}
/* 

{
  "id": 1,
  "title": "Salad Dish",
  "description": "Lorem Ipsum Test",
  "price": "22.00",
  "food_item_image": {
    "id": 10,
    "url": "http://0.0.0.0:8000/static/images/others/2021-05-22T160805.350725Captura_de_Tela_2021-05-20_as_13.07.04.png"
  },
  "foodItemCategory": {
    "id": 1,
    "url": "http://0.0.0.0:8000/api/v1/food-items-categories/1/",
    "title": "Salads"
  },
  "virtualshop": {
    "id": 10,
    "name": "Coco Bambu"
  },
  "updateAt": "2021-05-22T16:08:05.486831Z",
  "createAt": "2021-05-22T16:08:05.486870Z"
}
*/

// export interface ICategoryItem {
//     id: number,
//     name: string,
//     description: string | null,
// }