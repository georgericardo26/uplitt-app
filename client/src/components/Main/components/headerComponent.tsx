import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import React, { Fragment } from "react";

import MenuImage from "../../../assets/img/background-menu.jpeg"
import { IProps } from "../../../interfaces/defaults";

export function MenuListItems(props: IProps){
    return (
        <ul className="admin-menu">
            {props.children}
        </ul>
    )
}

export function MenuImageSection() {
    return (
        <Fragment>
            <div className="header-image">
                <img src={MenuImage} />
            </div>
        </Fragment>
    )
}

export function MenuCategory() {
    return (
        <Fragment>
            <li className="menu-heading">
                <h3>Menu</h3>
            </li>
            <li>
                <a href="/home">
                    <span><FontAwesomeIcon icon={['fas', 'home']} size="xs" /></span>
                    <span className="icon"></span><span> Home</span>
                </a>
            </li>
            <li>
                <a href="#0">
                    <span><FontAwesomeIcon icon={['fas', 'shopping-cart']} size="xs" /></span>
                    <span>Order</span>
                </a>
            </li>
            <li>
                <a href="/menu">
                    <span><FontAwesomeIcon icon={['fas', 'utensils']} size="xs" /></span>
                    <span>Menu</span>
                </a>
            </li>
            <li>
                
                <a href="#0">
                    <span><FontAwesomeIcon icon={['fas', 'comment']} size="xs" /></span>
                    <span>Review</span>
                </a>
            </li>
        </Fragment>
    );
}


export function OtherCategory() {
    return (
        <Fragment>
            <li className="menu-heading">
                <h3>Other</h3>
            </li>
            <li>
                <a href="#0">
                    <span><FontAwesomeIcon icon={['fas', 'cog']} size="xs" /></span>
                    <span>Settings</span>
                </a>
            </li>
            <li>
                <a href="#0">
                    <span><FontAwesomeIcon icon={['fas', 'credit-card']} size="xs" /></span>
                    <span>Payment</span>
                </a>
            </li>
            <li>
                <a href="#0">
                    <span><FontAwesomeIcon icon={['fas', 'user']} size="xs" /></span>
                    <span>Accounts</span>
                </a>
            </li>
        </Fragment>
    );
}
