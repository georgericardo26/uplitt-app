import React, { Fragment } from 'react';
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import Accordion from 'react-bootstrap/Accordion';
import Card from 'react-bootstrap/Card';
import Button from 'react-bootstrap/Button';

import { IAddRestaurant, ICategoryItem, IFoodItem } from '../../interfaces/defaults';
import { PageContentComponent, HeaderComponent } from '../Main/components/component';

const MenuComponent = function(props: any){ //Todo

    const { foodItemCategories, requestDeleteFoodItem } = props

    return (
        <PageContentComponent>
           <div className="menu-area">
                <div className="container">
                    <div className="title-area">
                        <h1>Menu</h1>
                    </div>
                    <div className="button-area">
                        <div className="row">
                            <div className="col-md-6 button-column">
                                <a href="/food-item/add">Add Item</a>
                            </div>
                            <div className="col-md-6 button-column">
                                <a href="/food-category/add">Add Category</a>
                            </div>
                        </div>
                    </div>
                    <div className="categories-area">
                        <div className="categories-section">
                            <table className="food-item-table">
                                <thead>
                                    {
                                        (foodItemCategories) ? 
                                            <Fragment>

                                                <tr>
                                                    <th>Image</th>
                                                    <th>Name</th>
                                                    <th>Description</th>
                                                    <th>Category</th>
                                                    <th>Price</th>
                                                    <th></th>
                                                </tr>

                                            </Fragment>
                                         : ""
                                    }
                                </thead>
                                <tbody>
                                    {
                                        (foodItemCategories) ? foodItemCategories.map((category: ICategoryItem) =>
                                        (
                                            <Fragment>
                                                
                                                <div className="category-name">
                                                    <h3>{category.title}</h3>
                                                </div>
                                                <br></br>
                                                <br></br>
                                
                                                {   (category.foodItems && category.foodItems.length > 0) ?
                                                    category.foodItems.map((foodItem: IFoodItem)=>(
                                                        <tr>
                                                            <td>
                                                                { <img src={foodItem.food_item_image.image_path}></img> }
                                                            </td>
                                                            <td>{foodItem.title}</td>
                                                            <td>{foodItem.description}</td>
                                                            <td>{category.title}</td>
                                                            <td>{foodItem.price}</td>
                                                            <td>
                                                                <ul>
                                                                    <li><a href={`/food-item/${foodItem.id}/edit`}><FontAwesomeIcon icon={['fas', 'edit']} size="xs" /></a></li>
                                                                    <li><a key={foodItem.id} href="javascript:void(0)" onClick={()=> (requestDeleteFoodItem(category.id, foodItem.id))}><FontAwesomeIcon icon={['fas', 'trash-alt']} size="xs" /></a></li>
                                                                </ul>
                                                            </td>
                                                        </tr>
                                                    )) : 
                                                    <tr>
                                                        empty
                                                    </tr>
                                                }
                                            </Fragment>
                                        )): ""
                                    }

                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div> 
        </PageContentComponent>
    )
}

export { MenuComponent }