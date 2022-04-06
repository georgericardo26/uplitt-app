import React from 'react'
import { ISignUpSucess } from '../../interfaces/defaults'

const SignUpSucessComponent = function(props: ISignUpSucess){
    return (
        <div className="register-success-page">
            <div className="wrap">
                <div className="container">
                    <div className="register-sucess-content">
                        <div className="title-content">
                            <h1>Congratulations!</h1>
                            <h1>We're almost there</h1>
                        </div>

                        <div className="confirmation-message">
                                <p>A confirmation email was sent to<br></br><span>{props.account_creation}</span><br></br> check your inbox and see you soon.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export { SignUpSucessComponent }