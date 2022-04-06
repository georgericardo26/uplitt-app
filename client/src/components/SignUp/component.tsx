import React from 'react';
import { ISignUP } from '../../interfaces/defaults';
import { AlertComponent } from '../Main/components/alerts';

const SignUpComponent = function(props: ISignUP){

    const { handleSubmit, ErrorDisplay } = props

    return (
        <div className="sign-up-page">
            <div className="container">
                <div className="form-content">
                    <div className="title-content">
                        <h1>Sign Up</h1>
                    </div>
                    <form className="sign-up-form" onSubmit={(event) => handleSubmit(event)}>
                        <div className="form-group">
                            <label>Your Profile</label>
                            <input type="text" className="form-control sign-up-input" placeholder="First Name" required name="first_name"></input>
                            <input type="text" className="form-control sign-up-input" placeholder="Last Name" name="last_name"></input>
                            <input type="text" className="form-control sign-up-input" placeholder="Username" name="username"></input>
                            <input type="email" className="form-control sign-up-input" placeholder="Email" required name="email"></input>
                            <input type="text" className="form-control sign-up-input" placeholder="Phone Number" required name="phone_number"></input>
                            <input type="password" className="form-control sign-up-input" placeholder="Password" required name="password"></input>
                            <input type="password" className="form-control sign-up-input" placeholder="Re-Type Password" required name="re_password"></input>
                        </div>

                        <div className="response-error">
                            <AlertComponent
                                    title="Error:" 
                                    message="Something is wrong when trying create your account, try again later." 
                                    type="danger"
                                    display={`${ErrorDisplay}`}
                            />
                        </div>

                        <button className="btn sign-up-button">REGISTER</button>
                    </form>
                    
                </div>
            </div>
        </div>
    )
}

export { SignUpComponent }