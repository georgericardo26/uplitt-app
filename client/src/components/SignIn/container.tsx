import React, { Fragment, useCallback, useEffect, useState } from 'react'

import { ObjFields } from '../../interfaces/defaults';
import { MenuComponent } from './component'
import configData from '../../config'
import { TopBarComponent, TopBarLogoComponent } from '../Main/components/component';
import { RequestPost } from '../../common/ApiClient/client';
import { useCookies } from 'react-cookie';

export default function MenuContainer(){

    const [ inputFields, setInputFields ] = useState<ObjFields>({});
    const [ errorDisplay, setErrorDisplay ] = useState("none");
    const [cookies, setCookie] = useCookies(['account_creation']);

    const handleSubmit = function(event: any) {
        event.preventDefault();
        
        let obj = {} as ObjFields;

        // Get input fields inserting to OBJ
        for (const item of event.target){
            obj[item["name"] as keyof ObjFields] = item["value"]
        }
        setInputFields(obj)
    }

    const requestCallback = useCallback(() => {

        (async function() {
            if(Object.keys(inputFields).length) {

                // Build URL
                let url = configData.UPLIT_AUTHENTICATION.URL;
                url += configData.UPLIT_AUTHENTICATION.RESOURCES.TOKEN;

                const response = await RequestPost({url: url, bodyData: {
                    client_id: process.env.REACT_APP_UPLIT_API_CLIENT_ID,
                    client_secret: process.env.REACT_APP_UPLIT_API_CLIENT_SECRET,
                    grant_type: "password",
                    username: inputFields.username,
                    password: inputFields.password
                  }});

                // Empty fields object
                setInputFields({})

                if (response.status === 200) {
                    setErrorDisplay("none");
                    setCookie('authentication', response.data);

                    // {
                    //     expires: new Date(Date.now() + response.data.expires_in)
                    //   }

                    if (response.data.seller.has_virtualshop === true){
                        window.location.href = "/home";
                    }
                    else {
                        window.location.href = "/add-restaurant";
                    }
                }
                else {
                    setErrorDisplay("block");
                }
            }
        })()
    }, [inputFields]);

    useEffect(() => {
        requestCallback();
    }, [requestCallback])

    return (
        <Fragment>
            <TopBarComponent>
                <TopBarLogoComponent grid="col-md-3"/>
            </TopBarComponent>
            <MenuComponent handleSubmit={handleSubmit} ErrorDisplay={errorDisplay} />
        </Fragment>
    )
}