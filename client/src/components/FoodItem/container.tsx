import React, { Fragment, useCallback, useEffect, useState } from 'react'
import { useCookies } from 'react-cookie';
import { useParams } from 'react-router-dom';

import { CategoryFields, CreateRestaurantFields, FoodItemFields, IFoodCategoriesList, ITagsIds, ListCategoriesFields, ObjFields, TypeOBJCurrentFoodItemField, TypeOBJFoodItemField } from '../../interfaces/defaults';
import { FoodItemComponent } from './component'
import { HeaderComponent, TopBarComponent, TopBarLogoComponent, TopBarProfileComponent, TopBarSearchAreaComponent } from '../Main/components/component';
import { RequestGet, RequestPatch, RequestPost } from '../../common/ApiClient/client';

import configData from '../../config'
import { MenuCategory, MenuImageSection, MenuListItems, OtherCategory } from '../Main/components/headerComponent';

export default function FoodItemContainer(){

    const [cookies, setCookie] = useCookies(['authentication', 'virtualshop']);

    const [ inputFields, setInputFields ] = useState<FoodItemFields>({});
    const [ errorDisplay, setErrorDisplay ] = useState("none");
    const [ successDisplay, setSuccessDisplay ] = useState("none");
    const [ foodCategories, setFoodCategories ] = useState<ListCategoriesFields[]>([]);
    const [ imageOBJ, setImageOBJ ] = useState(null);
    const [ imageResponseData, SetImageResponseData ] = useState<any>({});
    const [ origemURL, setOrigemURL ] = useState<string>("");
    const [ currentFoodItemId, setCurrentFoodItemId ] = useState<string>(""); 
    const [ currentFoodItem, setCurrentFoodItem ] = useState<any>({});
    const [ listTags, setListTags ] = useState<any>({});
    const [ tags, setTags ] = useState<ITagsIds>({}); 

    
    const [test, setTest] = useState<any>("");
    
    let { id } = useParams<any>();

    const handleSubmit = function(event: any) {
        console.log("testing handle submit");
        event.preventDefault();
        
        let obj = {} as FoodItemFields;

        // Get input fields inserting to OBJ
        for (const item of event.target){

            if (!item.type.includes("image")){
                obj[item["name"] as keyof FoodItemFields] = item["value"]
            }
        }

        // Get the checked tags
        if(Object.keys(tags).length > 0) {
            let IdTags = [];
            IdTags = Object.keys(tags).filter((key, value) => {
                return tags[key as unknown as keyof ITagsIds] === true
            });
            obj["tags"] = IdTags;
        }
        obj["ingredientItems"] = [];

        setInputFields(obj);
    }

    const handleTags = function(event: any){
        let currentList;
        setTags((prevState: any) => (
            {
                ...prevState,
                [event.target.id]: event.target.value,
            }
        ));
    }

    const updateState = function(field: string, value: any){
        setCurrentFoodItem((prevState: any)=> {
            return {
                ...prevState,
                [field]: value
            }
        })
    }

    const checkOrigemURL = function() {
        if (typeof id !== "undefined" && id.length > 0) {
            //setCurrentFoodItemId(id);
            requestRetrieveFoodItem();
        }
        
    }

    const getImage = function(event: any) {
        console.log(event.files[0]);
        setImageOBJ(event.files[0]);
    }

    const clearInputs = function() {
        let field_title = document.getElementById("title") as HTMLInputElement;        
        let field_description = document.getElementById("description") as HTMLInputElement;
        let field_price = document.getElementById("price") as HTMLInputElement;
        let field_foodItemCategory_pk = document.getElementById("foodItemCategory") as HTMLInputElement;
        let field_file = document.getElementById("input-file") as HTMLInputElement;      

        field_title.value = "";
        field_description.value = "";
        field_price.value = "";
        field_foodItemCategory_pk.value = "";
    }

    const fillImageForm = function() {
        //const dT = new ClipboardEvent('').clipboardData || // Firefox < 62 workaround exploiting https://bugzilla.mozilla.org/show_bug.cgi?id=1422655
        const dT = new DataTransfer(); // specs compliant (as of March 2018 only Chrome)
        dT.items.add(new File(['foo'], 'programmatically_created.txt'));

        //inp.files = dT.files;
    };

    const requestRetrieveFoodItem = useCallback(() => {
        (async function() {

            if (typeof id !== "undefined" && id.length > 0) {

                console.log("opa chegou aqui");
                
                let url = configData.UPLIT_API.URL;
                url += configData.UPLIT_API.RESOURCES.FOOD_ITEMS + id;

                const response = await RequestGet({
                    url: url,
                    header: {
                        headers: {
                            'Content-Type': 'application/json',
                            'Authorization': `Bearer ${cookies.authentication.access_token}`
                        }
                    }
                });

                if (response.status === 200) {
                    setCurrentFoodItem(response.data);

                    if(response.data.tags.length > 0){
                        let objTags = {} as ITagsIds;
                        response.data.tags.forEach((item: number) => {
                            objTags[item as keyof ITagsIds] = true
                        });
                        setTags(objTags);
                    }
                    
                    console.log("current food: ", response.data);
                }
                else {
                    setCurrentFoodItem({})
                }

            }

        })();
    }, []);

    const requestListTags = useCallback(() => {
        (async function() {
            let url = configData.UPLIT_API.URL;
            url += configData.UPLIT_API.RESOURCES.TAGS;

            const response = await RequestGet({
                url: url,
                header: {
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${cookies.authentication.access_token}`
                    }
                }
            });

            if (response.status === 200) {
                console.log("Tags: ", response.data);
                setListTags(response.data);
            }
            else {
                setListTags([]);
            }

        })();
    }, []);

    const requestListFoodCategories = useCallback(() => {
        (async function() {
            let url = configData.UPLIT_API.URL;
            url += configData.UPLIT_API.RESOURCES.FOOD_ITEM_CATEGORY;

            const response = await RequestGet({
                url: url,
                header: {
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${cookies.authentication.access_token}`
                    }
                }
            });

            if (response.status === 200) {
                console.log("Food Item Categories: ", response.data);
                setFoodCategories(response.data);
            }
            else {
                setFoodCategories([]);
            }

        })();
    }, []);

    const requestAddImageAndFood = useCallback(() => {
        (async function() {

            console.log("ta aqui.");
            if (Object.keys(inputFields).length) {
                console.log("bateu aqui");
                 // Add image
                let url = configData.UPLIT_API.URL;
                url += "images/";

                // Create formdata to request
                let bodyFormData = new FormData() as any;
                bodyFormData.append("upload", imageOBJ);

                // Make Add Image request
                const imageResponse = await RequestPost({
                    url: url,
                    bodyData: bodyFormData,
                    header: {
                        headers: {
                            'Content-Type': 'multipart/form-data',
                            'Authorization': `Bearer ${cookies.authentication.access_token}`
                        }
                    }
                });

                 // save in state the add image response
                 SetImageResponseData(imageResponse.data);
                
                 //requestBaseFood(imageResponse.status, imageResponse);

                 // Build URL Add Food Item
                 url = configData.UPLIT_API.URL;
                 url += "food-items/"

                 //currentFoodItem
                 let objRequest = {} as any;

                 for (const item of Object.keys(inputFields)){ 
                     objRequest[item] = inputFields[item as keyof FoodItemFields]
                 }

                 console.log("OBJ Request: ", objRequest);

                 if(typeof id !== "undefined" && id.length > 0){

                     if(imageOBJ){
                         objRequest["image"] = imageResponse.data.id
                     }
                     else {
                         objRequest["image"] = (currentFoodItem.food_item_image) ? currentFoodItem.food_item_image.id : null
                     }
                     
                     url += `${currentFoodItem.id}/`
                     requestEditFoodItem(url, objRequest);
                 }
                 else {
                     objRequest["image"] = imageResponse.data.id
                     requestAddFoodItem(url, objRequest);
                 }

            }

        })();
    }, [inputFields]);

    const requestEditFoodItem = useCallback((url, objRequest) => {
        (async function(url, objRequest){
            await RequestPatch({
                url: url,
                bodyData: objRequest,
                header: {
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${cookies.authentication.access_token}`
                    }
                }
            }).then((response) => {

                // Empty object fields 
                setInputFields({});

                // Empty Image OBJ
                setImageOBJ(null);

                if (response.status == 200) {
                    console.log("no if");
                    clearInputs();

                    // Set Errors none and success block
                    setErrorDisplay("none");
                    setSuccessDisplay("block");

                } else {
                    console.log("no else");
                    setErrorDisplay("block");
                    setSuccessDisplay("none");
                }

            }).catch((error) => {
                console.log("aciu bem aqui", error);
                // Empty object fields 
                setInputFields({});

                 // Set Errors none and success block
                 setErrorDisplay("block");
                 setSuccessDisplay("none");
            });
        })(url, objRequest);
    }, []);


    const requestAddFoodItem = useCallback((url, objRequest)=> {
        (async function(url, objRequest){
            console.log("obj request", objRequest);
            await RequestPost({
                url: url,
                bodyData: objRequest,
                header: {
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${cookies.authentication.access_token}`
                    }
                }
            }).then((response) => {

                // Empty object fields 
                setInputFields({});
                
                // Empty Image OBJ
                setImageOBJ(null);

                console.log("status code", response.status);

                if (response.status == 201) {

                    console.log("Food Item Added!");
                    clearInputs();
                    console.log("display none!");
                    setErrorDisplay("none");
                    setSuccessDisplay("block");

                } else {
                    console.log("Caiu Else");
                    console.log("display block!");
                    setErrorDisplay("block");
                    setSuccessDisplay("none");
                }
            }).catch((error) => {
                // Empty object fields 
                setInputFields({});

                 // Set Errors none and success block
                 console.log(error);
                 console.log("display block!");
                 setErrorDisplay("block");
                 setSuccessDisplay("none");
            });
        })(url, objRequest);
    }, []);

    useEffect(() => {
        checkOrigemURL();
        //requestRetrieveFoodItem();
        requestListTags();
        requestListFoodCategories();
        requestAddImageAndFood(); 
    }, [requestAddImageAndFood])


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
            <FoodItemComponent 
                handleSubmit={handleSubmit} 
                inputFields={inputFields} 
                errorDisplay={errorDisplay}
                successDisplay={successDisplay}
                foodCategories={foodCategories}
                getImage={getImage}
                origemURL={origemURL}
                currentFoodItem={currentFoodItem}
                updateState={updateState}
                idCurrentFoodItem={id}
                listTags={listTags}
                handleTags={handleTags}
                tags={tags}
            />
        </Fragment>
    )
}