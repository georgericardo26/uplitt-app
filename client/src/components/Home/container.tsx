import React, { Fragment } from 'react'
import { useCookies } from 'react-cookie';

import { TopBarComponent, TopBarLogoComponent, TopBarSearchAreaComponent, TopBarProfileComponent, HeaderComponent } from '../Main/components/component';
import { MenuCategory, MenuImageSection, MenuListItems, OtherCategory } from '../Main/components/headerComponent';
import HomeComponent from './component';

export default function HomeContainer(){

    const [cookies] = useCookies(['authentication']);

    return (
        <Fragment>
            <TopBarComponent>
                <TopBarLogoComponent grid="col-md-3"/>
                <TopBarSearchAreaComponent grid="col-md-6" />
                <TopBarProfileComponent grid="col-md-3" profileName={cookies.authentication.seller.user.first_name} />
            </TopBarComponent>
            <HeaderComponent>
                <MenuListItems>
                    <MenuImageSection />
                    <MenuCategory />
                    <OtherCategory />
                </MenuListItems>
            </HeaderComponent>
            <HomeComponent />
        </Fragment>
    )
}