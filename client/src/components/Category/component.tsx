import React, { Fragment } from 'react';
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

import { IAddRestaurant, ICategoryItem, IFoodItem } from '../../interfaces/defaults';
import { AlertComponent } from '../Main/components/alerts';
import { PageContentComponent, HeaderComponent } from '../Main/components/component';

const CategoryComponent = function(props: any){ //Todo

    const { handleSubmit, inputFields, errorDisplay, successDisplay } = props

    return (
        <PageContentComponent>
            <div className="category-page">
                <div className="container">
                    <div className="form-content">
                        <div className="title-content">
                            <h1>Add Category</h1>
                        </div>
                        <form className="category-form" onSubmit={(event) => handleSubmit(event)}>

                            <div className="form-group">
                                <div className="form-section">
                                    <label>Category</label>
                                    <input type="text" className="form-control" placeholder="Category Name" id="name" required name="name"></input>
                                </div>
                                <div className="form-section">  
                                    <label>Description</label>
                                    <textarea className="form-control text-description" rows={5} placeholder="Description" id="description" required name="description"></textarea>
                                </div>
                            </div>

                            <div className="response-error">
                                <AlertComponent
                                        title="Error:" 
                                        message="Something is wrong when trying create food category, try again later." 
                                        type="danger"
                                        display={`${errorDisplay}`}
                                />
                                <AlertComponent
                                        title="Success:" 
                                        message="Food Item Category insert successfully." 
                                        type="sucess"
                                        display={`${successDisplay}`}
                                />
                            </div>

                            <div className="row">
                                <div className="col-md-6">
                                    <a href="/menu" className="btn get-back">Back</a>
                                </div>
                                <div className="col-md-6">
                                    <button className="btn category-button">Add Category</button>
                                </div>
                            </div>
                        </form>
                        
                    </div>
                </div>
            </div>
        </PageContentComponent>
    )
}

export { CategoryComponent }