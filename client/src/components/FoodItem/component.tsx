import React, { Fragment, useEffect, useState } from 'react';
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

import { IAddRestaurant, ICategoryItem, IFoodItem, TypeFoodCategoryField, TypeTag } from '../../interfaces/defaults';
import { AlertComponent } from '../Main/components/alerts';
import { PageContentComponent, HeaderComponent } from '../Main/components/component';

const FoodItemComponent = function(props: any){ //Todo

    const [ active, setActive ] = useState<boolean>(false); 

    const { 
        handleSubmit, 
        inputFields, 
        errorDisplay, 
        successDisplay, 
        foodCategories, 
        getImage, 
        origemURL, 
        currentFoodItem,
        updateState,
        idCurrentFoodItem,
        listTags,
        handleTags,
        tags
    } = props
    
    return (
        <PageContentComponent>
            <div className="food-item-page">
                <div className="container">
                    <div className="form-content">
                        <div className="title-content">
                            <h1>{(typeof idCurrentFoodItem !== "undefined" && idCurrentFoodItem.length > 0)
                            ? "Edit Product" : "Add Product"
                            }</h1>
                        </div>
                        <form className="food-item-form " onSubmit={(event) => handleSubmit(event)}>
                            <div className="form-group">
                                <div className="form-section">
                                    <div className="input-file-container">
                                        <input className="input-file" id="input-file" type="file" accept="image/*" onChange={(event)=> getImage(event.target)}></input>
                                        <label className="input-file-trigger"></label>
                                    </div>
                                </div>
                                <div className="form-section">
                                    <label>Product Name</label>
                                    <input type="text" 
                                        className="form-control" 
                                        placeholder="Product Name"
                                        required 
                                        id="title" 
                                        name="title"
                                        value={currentFoodItem.title}
                                        onChange={(event)=>{updateState("title", event.target.value)}}
                                        ></input>
                                </div>
                                <div className="form-section">  
                                    <label>Category</label>
                                    <select 
                                        id="foodItemCategory" 
                                        name="foodItemCategory" 
                                        required={true}
                                        value={(currentFoodItem.foodItemCategory)? currentFoodItem.foodItemCategory.id : "default"}
                                        onChange={(event)=>{updateState("foodItemCategory", {id: event.target.value, title: event.target.textContent})}}
                                        >

                                        <option value="default" disabled>Select a category</option>
                                        {
                                            (foodCategories && foodCategories.length > 0) ?
                                            foodCategories.map((categoryItem: TypeFoodCategoryField) => (

                                                <option value={categoryItem.id}>
                                                {categoryItem.title}</option>

                                            )) : ""
                                        }

                                    </select>
                                   
                                </div>
                                <div className="form-section">
                                    <label>Product Description</label>
                                    <textarea 
                                        className="form-control text-description" 
                                        placeholder="About Product" 
                                        required 
                                        id="description" 
                                        name="description"
                                        value={currentFoodItem.description}
                                        onChange={(event)=>{updateState("description", event.target.value)}}
                                    ></textarea>
                                </div>

                                <div className="form-section">
                                    <label>Price</label>
                                    <input 
                                        type="text" 
                                        className="form-control" 
                                        placeholder="Price" 
                                        required 
                                        id="price" 
                                        name="price"
                                        value={currentFoodItem.price}
                                        onChange={(event)=>{updateState("price", event.target.value)}}
                                    ></input>
                                </div>
                                <hr></hr>
                                <div className="form-section">
                                    <label>Tags</label>
                                    <br></br>
                                    <div className="tags">
                                        <ul className="list-inline">
                                            {
                                                (listTags.results !== undefined) ? listTags.results.map((tag: TypeTag)=> (
                                                    <li className="list-inline-item">
                                                        <label className="food-item-container">{tag.name}
                                                            <input type="checkbox"
                                                                onClick={(event: any)=>{ 
                                                                    handleTags({
                                                                        target: {
                                                                            id: tag.id,
                                                                            value: event.target.checked
                                                                        }
                                                                    });
                                                                }}
                                                                checked={(Object.keys(tags.length > 0))? tags[`${tag.id}`]: false}
                                                            ></input>
                                                            <span className="checkmark"></span>
                                                        </label>
                                                    </li>
                                                )) : ""
                                            }
                                        </ul>
                                    </div>
                  
                                </div>
                                <hr></hr>

                                <div className="form-section">
                                    <label>Ingredients</label>
                                  <br></br>
                                    <div className="ingredients">
                                        <div className="menu-add-ingredients">
                                            <button><FontAwesomeIcon icon={['fas', 'plus-square']} size="lg" /></button>
                                        </div>
                                        <div className="fields-area">

                                        </div>
                                    </div>
                  
                                </div>

                            </div>

                            <div className="response-error">
                                <AlertComponent
                                        title="Error:" 
                                        message="Something is wrong when trying create food item, try again later." 
                                        type="danger"
                                        display={`${errorDisplay}`}
                                />
                                <AlertComponent
                                        title="Success:" 
                                        message="Food Item insert successfully." 
                                        type="sucess"
                                        display={`${successDisplay}`}
                                />
                            </div>

                            <div className="row">
                                <div className="col-md-6">
                                    <a href="/menu" className="btn get-back">Back</a>
                                </div>
                                <div className="col-md-6">
                                    <button className="btn food-item-button">
                                        {(typeof idCurrentFoodItem !== "undefined" && idCurrentFoodItem.length > 0) ?
                                        "Edit Product" : "Add Product"}
                                    </button>
                                </div>
                            </div>
                        </form>
                        
                    </div>
                </div>
            </div>
        </PageContentComponent>
    )
}

export { FoodItemComponent }