import React, { Fragment, useCallback, useEffect, useState } from 'react'
import { useCookies } from 'react-cookie';

import { ObjFields } from '../../interfaces/defaults';
import { SignUpComponent } from './component'
import configData from '../../config'
import { TopBarComponent, TopBarLogoComponent } from '../Main/components/component';
import { RequestPost } from '../../common/ApiClient/client';

export default function SignUpContainer(){

    const [ inputFields, setInputFields ] = useState<ObjFields>({});
    const [ errorDisplay, setErrorDisplay ] = useState("none");

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
            if(Object.keys(inputFields).length){

                // Build URL
                let url = configData.UPLIT_API.URL;
                url += configData.UPLIT_API.RESOURCES.SELLER;

                const response = await RequestPost({url: url, bodyData: {
                    user: {
                        username: inputFields.username,
                        password: inputFields.password,
                        first_name: inputFields.first_name,
                        last_name: inputFields.last_name,
                        email: inputFields.email,
                        phoneNumber: inputFields.phone_number
                    }
                }});

                // Empty fields object
                setInputFields({})

                if (response.status === 201){
                    setErrorDisplay("none");
                    window.location.href = "/signup-success";
                }
                else {
                    setErrorDisplay("block");
                }
                
            }
        })()
    }, [inputFields])

    useEffect(() => {
        requestCallback();
    }, [requestCallback])


    return (
        <Fragment>
            <TopBarComponent>
                <TopBarLogoComponent grid="col-md-3"/>
            </TopBarComponent>
            <SignUpComponent handleSubmit={handleSubmit} ErrorDisplay={errorDisplay} />
        </Fragment>
    )
}