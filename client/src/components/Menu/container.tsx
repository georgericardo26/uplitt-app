import React, { Fragment, useCallback, useEffect, useState } from 'react'
import { useCookies } from 'react-cookie';

import { CreateRestaurantFields, IFoodCategoriesList, ObjFields } from '../../interfaces/defaults';
import { MenuComponent } from './component'
import { HeaderComponent, TopBarComponent, TopBarLogoComponent, TopBarProfileComponent, TopBarSearchAreaComponent } from '../Main/components/component';
import { RequestDelete, RequestGet, RequestPost } from '../../common/ApiClient/client';

import configData from '../../config'
import { MenuCategory, MenuImageSection, MenuListItems, OtherCategory } from '../Main/components/headerComponent';

export default function MenuContainer(){

    const [ foodItemCategories, setFoodItemCategories ] = useState<IFoodCategoriesList>({"results": []}); //Todo
    const [cookies, setCookie] = useCookies(['authentication', 'virtualshop']);


    const requestCallback = useCallback(() => {
        (async function() {

            if(cookies.authentication.seller.virtualshop !== null) {
                // Build URL
                console.log("cookie", cookies.authentication);
                let url = configData.UPLIT_API.URL;
                url += configData.UPLIT_API.RESOURCES.VIRTUALSHOP_LIST_CATEGORIES.replace("<id>", cookies.authentication.seller.virtualshop.id);
                
                const response = await RequestGet({
                    url: url,
                    header: {
                        headers: {
                            'Content-Type': 'application/json',
                            'Authorization': `Bearer ${cookies.authentication.access_token}`
                        }
                    }
                });

                if (response.status === 200){
                    setFoodItemCategories(response.data);
                    console.log("response", response.data);
                }
                else {
                    console.log("error");
                }

            }

        })();
    }, []);

    const requestDeleteFoodItem = useCallback((categoryId, foodId) => {

        (async function(categoryId, foodId) {

            let url = `${configData.UPLIT_API.URL}${configData.UPLIT_API.RESOURCES.FOOD_ITEMS}${foodId}`;
            // url += configData.UPLIT_API.RESOURCES.FOOD_ITEMS +"/"+ foodId;

            // let t = `${url}ksskls`;
                
            const response = await RequestDelete({
                url: url,
                header: {
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${cookies.authentication.access_token}`
                    }
                }
            });

            console.log(response.status);

            if (response.status === 204){
                let copyObject = foodItemCategories.results;
                let categoryItem: any | undefined, indexCategory: number | undefined, newFoodItemCategories: any | undefined;
                if(copyObject){
                
                    for (let i = 0; i < copyObject.length; i++){
                        if (copyObject[i]["id"] === categoryId){
                            categoryItem = copyObject[i];
                            indexCategory = i;
                            break;
                        }
                    }

                    if(categoryItem){
                        newFoodItemCategories = categoryItem.foodItems.filter((foodItem: any) => foodItem.id !== foodId); 
                        categoryItem.foodItems = newFoodItemCategories;
                    }

                    if(indexCategory !== undefined){
                        copyObject[indexCategory] = categoryItem;
                        setFoodItemCategories({"results": copyObject});
                    }
                    
                }
            }
            else {
                console.log("error");
            }

        })(categoryId, foodId);
        
    }, [foodItemCategories]);

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
            <MenuComponent 
                foodItemCategories={foodItemCategories.results}
                requestDeleteFoodItem={requestDeleteFoodItem}
             />
        </Fragment>
    )
}