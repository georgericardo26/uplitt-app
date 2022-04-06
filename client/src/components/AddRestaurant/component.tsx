import React, { Fragment, useState, useRef, useEffect } from 'react';
import { IAddRestaurant } from '../../interfaces/defaults';
import { AlertComponent } from '../Main/components/alerts';
import { PageContentComponent, HeaderComponent } from '../Main/components/component';

const AddRestaurantComponent = function(props: IAddRestaurant){

    const { 
        handleSubmit, 
        handleRestaurantForm, 
        ErrorDisplay, 
        showRestaurantForm, 
        getImage, 
        loadScript,
        handleScriptLoad
     } = props

    const [query, setQuery] = useState("");
    const [error, setError] = useState(false)
    const autoCompleteRef = useRef(null);

    useEffect(() => {
        loadScript(
          `https://maps.googleapis.com/maps/api/js?key=${process.env.REACT_APP_GOOGLE_API_KEY}&libraries=places`,
          () => handleScriptLoad(setQuery, autoCompleteRef, setError)
        );
      }, [loadScript, handleScriptLoad]);

    return (
        <PageContentComponent>
            {
                (showRestaurantForm)?
                    <div className="add-restaurant-area">
                    <div className="container">
                        <div className="form-content">
                            <div className="title-content">
                                <h1>Restaurant Information</h1>
                            </div>
                            <form className="add-reataurant-form" onSubmit={(event) => handleSubmit(event)}>
                                <div className="form-group">
                                    <input type="text" className="form-control sign-up-input" placeholder="Restaurant Name" required name="name"></input>
                                    <input type="text" className="form-control sign-up-input" placeholder="Phone Number" name="phoneNumber"></input>
                                    
                                    <input
                                        className="form-control input-search"
                                        ref={autoCompleteRef}
                                        onChange={event => setQuery(event.target.value)}
                                        placeholder="Enter an address"
                                        value={query}
                                        name="AddressLine1"
                                    />
                                </div>

                                <div className="form-group">
                                    <input className="input-file" id="input-file" type="file" accept="image/*" onChange={(event)=> getImage(event.target)}></input>
                                    <label className="input-file-trigger"></label>
                                </div>

                                <div className="response-error">
                                    <AlertComponent
                                            title="Error:" 
                                            message="Something is wrong when trying create your account, try again later." 
                                            type="danger"
                                            display={`${ErrorDisplay}`}
                                    />
                                </div>

                                <button className="btn add-restaurant-button">Create Restaurant</button>
                            </form>
                            
                        </div>
                    </div>
                </div>
                : 
                <div>
                    <div className="welcome-uplit">
                        <div className="container">
                            <div className="message-welcome">
                                <h1>Welcome <br></br> to <span className="uptlit-font">Uplit</span></h1>
                            </div>
                            <div className="second-message">
                                <p>The best way to order<br></br> food without leaving</p>
                            </div>
                            <div className="add-restaurant">
                                <button className="btn add-restaurant-button" onClick={(event) => handleRestaurantForm(event)}>Add your restaurant</button>
                            </div>
                        </div>
                    </div>
                </div>
            }
        </PageContentComponent>
    )
}

export { AddRestaurantComponent }