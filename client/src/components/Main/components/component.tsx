import React from 'react';
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

import { IProps, ITopBar, IGridOption, TypeProfileTopBar } from '../../../interfaces/defaults'
import ProfileImage from "../../../assets/img/user.png"
import MenuImage from "../../../assets/img/background-menu.jpeg"


const TopBarComponent = function(props: ITopBar){

    return (
        <div className="top-bar">
            <div className="container">
                <div className="row">
                    {props.children}
                </div>
            </div>
        </div>
    )
}

const TopBarLogoComponent = function(props: IGridOption){
    return (
        <div className={props.grid}>
            <div className="logo">
                <a className="a-logo" href="/">Uplit</a>
            </div>
        </div>
    )
}

const TopBarSearchAreaComponent = function(props: IGridOption){
    return (
        <div className={props.grid}>
            <div className="search-area">
                <input type="text" className="input-search"></input>
            </div>
        </div>
    )
}


const TopBarSignInUPAreaComponent = function(props: IGridOption){
    return (
        <div className={props.grid}>
            <div className="singup-in-links">
                <a href="/signin" className="sign-in">Sign In</a>
                <a href="/signup" className="sign-up">Sign Up</a>
            </div>
        </div>
    )
}

const TopBarProfileComponent = function(props: TypeProfileTopBar){
    return (
        <div className={props.grid}>

            <div className="profile-menu">
                <div className="profile-img">
                    <img src={ProfileImage}></img>
                </div>
                <div className="profile-name">
                    <button type="button" className="profile-button" data-toggle="dropdown">
                        {props.profileName}
                    </button>
                    <div className="dropdown-menu">
                        <a className="dropdown-item" href="#">Link 1</a>
                        <a className="dropdown-item" href="#">Link 2</a>
                        <a className="dropdown-item" href="#">Link 3</a>
                    </div>
                </div>
            </div>
        </div>
    )
}

const HeaderComponent = function(props: IProps) {
    return (
        <header className="page-header">
                <nav>
                    {props.children}
                </nav>
        </header>
    );
}

const SectionComponent = function (props: IProps){
    return (
        <>{props.children}</>
    )
}

const PageContentComponent = function (props: IProps){
    return (
        <section className="page-content">
            {props.children}
        </section>
    )
}

export { 
    TopBarComponent,
    TopBarLogoComponent,
    TopBarSearchAreaComponent,
    TopBarProfileComponent,
    HeaderComponent, 
    SectionComponent,
    TopBarSignInUPAreaComponent,
    PageContentComponent
}
