import React from 'react'
import { Switch, Route, Redirect } from 'react-router-dom';

import HomeContainer from '../Home/container'
import SignInContainer from '../SignIn/container';
import SignUpContainer from '../SignUp/container'
import SignUpSucessContainer from '../SignUpSucess/container';
import WelcomeContainer from '../Welcome/container'
import AddRestaurantContainer from '../AddRestaurant/container';
import MenuContainer from '../Menu/container';
import CategoryContainer from '../Category/container';
import FoodItemContainer from '../FoodItem/container';


export default function Routers(){
    return(
        <Switch>
            <Route exact path="/" component={WelcomeContainer}></Route>
            <Route exact path="/home" component={HomeContainer}></Route>
            <Route exact path="/signup" component={SignUpContainer}></Route>
            <Route exact path="/signup-success" component={SignUpSucessContainer}></Route>
            <Route exact path="/signin" component={SignInContainer}></Route>
            <Route exact path="/add-restaurant" component={AddRestaurantContainer}></Route>
            <Route exact path="/menu" component={MenuContainer}></Route>
            <Route exact path="/food-category/add" component={CategoryContainer}></Route>
            <Route exact path="/food-item/add" component={FoodItemContainer}></Route>
            <Route exact path="/food-item/:id/edit" component={FoodItemContainer}></Route>
            <Redirect from="*" to="/"></Redirect>
        </Switch>
    )
}
