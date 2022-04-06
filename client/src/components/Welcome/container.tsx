import React, { Fragment } from 'react'

import WelcomeComponent from './component'
import { SectionComponent, TopBarComponent, TopBarLogoComponent, TopBarSignInUPAreaComponent} from '../Main/components/component'

export default function WelcomeContainer(){
    return (
        <Fragment>
            <TopBarComponent>
                <TopBarLogoComponent grid="col-md-3"/>
                <TopBarSignInUPAreaComponent grid="col-md-9"/>
            </TopBarComponent>
            <SectionComponent>
                <WelcomeComponent />
            </SectionComponent>
        </Fragment>
    )
}