import React from 'react';
import { ISignUP } from '../../interfaces/defaults';
import logo from "../../assets/img/logo.jpeg"
import { AlertComponent } from '../Main/components/alerts';

const MenuComponent = function(props: ISignUP){

    const { handleSubmit, ErrorDisplay } = props

    return (
        <div className="sign-up-page">
            <div className="container">
                <div className="form-content">
                    <div className="title-content">
                        <h1>Sign In</h1>
                    </div>
                    <form className="sign-up-form" onSubmit={(event) => handleSubmit(event)}>
                        <div className="form-group">
                            <input type="text" className="form-control sign-up-input" placeholder="username" required name="username"></input>
                            <input type="password" className="form-control sign-up-input" placeholder="Password" required name="password"></input>
                        </div>

                        <div className="response-error">
                            <AlertComponent
                                    title="Error:" 
                                    message="Something is wrong when trying signing your account, try again later." 
                                    type="danger"
                                    display={`${ErrorDisplay}`}
                            />
                        </div>
                    
                        <button className="btn sign-up-button">LOGIN</button>

                    </form>
                    
                </div>
            </div>
        </div>
    )
}

export { MenuComponent }