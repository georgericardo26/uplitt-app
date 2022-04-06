import React, { Fragment } from 'react';
import { CookiesProvider, useCookies } from 'react-cookie';

import { SignUpSucessComponent } from './component'
import { TopBarComponent, TopBarLogoComponent } from '../Main/components/component';


export default function SignUpSucessContainer(){
    const [cookies] = useCookies(['account_creation']);

    return (
        <Fragment>
            <TopBarComponent>
                <TopBarLogoComponent grid="col-md-3" />
            </TopBarComponent>
            <SignUpSucessComponent account_creation={cookies.account_creation} />
        </Fragment>
    )
}