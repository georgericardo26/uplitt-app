import React, { Fragment, useCallback, useEffect, useState } from 'react'
import { useCookies } from 'react-cookie';

import { CategoryFields, CreateRestaurantFields, IFoodCategoriesList, ObjFields } from '../../interfaces/defaults';
import { CategoryComponent } from './component'
import { HeaderComponent, TopBarComponent, TopBarLogoComponent, TopBarProfileComponent, TopBarSearchAreaComponent } from '../Main/components/component';
import { RequestGet, RequestPost } from '../../common/ApiClient/client';

import configData from '../../config'
import { MenuCategory, MenuImageSection, MenuListItems, OtherCategory } from '../Main/components/headerComponent';

export default function CategoryContainer(){

    const [ inputFields, setInputFields ] = useState<CategoryFields>({});
    const [ errorDisplay, setErrorDisplay ] = useState("none");
    const [ successDisplay, setSuccessDisplay ] = useState("none");
    const [cookies, setCookie] = useCookies(['authentication', 'virtualshop']);

    const handleSubmit = function(event: any) {
        event.preventDefault();
        
        let obj = {} as CategoryFields;

        // Get input fields inserting to OBJ
        for (const item of event.target){
            obj[item["name"] as keyof CategoryFields] = item["value"]
        }

        setInputFields(obj);
    }

    const clearInputs = function() {
        let field_name = document.getElementById("name") as HTMLInputElement;        
        let field_description = document.getElementById("description") as HTMLInputElement;

        field_name.value = "";
        field_description.value = "";
    }

    const requestCallback = useCallback(() => {
        (async function() {
            
            if(Object.keys(inputFields).length) {

                // Build URL
                let url = configData.UPLIT_API.URL;
                url += configData.UPLIT_API.RESOURCES.FOOD_ITEM_CATEGORY
                
                const response = await RequestPost({
                    url: url,
                    bodyData: {
                        title: inputFields.name,
                        description: inputFields.description,
                        virtualshop: cookies.virtualshop.id
                    },
                    header: {
                        headers: {
                            'Content-Type': 'application/json',
                            'Authorization': `Bearer ${cookies.authentication.access_token}`
                        }
                    }
                });

                //Empty fields object
                setInputFields({})

                if (response.status === 201) {
                    clearInputs();
                    console.log(response.data);
                    setErrorDisplay("none");
                    setSuccessDisplay("block");
                }
                else {
                    setErrorDisplay("block");
                    setSuccessDisplay("none");
                }

            }
        })();
    }, [inputFields]);

    useEffect(() => {
        requestCallback();
    }, [requestCallback])


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
            <CategoryComponent 
                handleSubmit={handleSubmit} 
                inputFields={inputFields} 
                errorDisplay={errorDisplay}
                successDisplay={successDisplay}
            />
            
        </Fragment>
    )
}