import React, { Fragment, useCallback, useEffect, useState } from 'react'
import { useCookies } from 'react-cookie';

import { CreateRestaurantFields, GoogleAddressFields, ObjFields } from '../../interfaces/defaults';
import { AddRestaurantComponent } from './component'
import { HeaderComponent, TopBarComponent, TopBarLogoComponent, TopBarProfileComponent, TopBarSearchAreaComponent } from '../Main/components/component';
import { RequestPost } from '../../common/ApiClient/client';

import configData from '../../config'
import { MenuListItems, OtherCategory } from '../Main/components/headerComponent';

export default function AddRestaurantContainer(){

    const [ inputFields, setInputFields ] = useState<CreateRestaurantFields>({});
    const [ errorDisplay, setErrorDisplay ] = useState("none");
    const [ showRestaurantForm, setShowRestaurantForm ] = useState(false)
    const [cookies, setCookie, removeCookie] = useCookies(['authentication', 'virtualshop']);
    const [ imageOBJ, setImageOBJ ] = useState(null);
    const [ getAddress, setAddress ] = useState<GoogleAddressFields>({});

    /* Google autocomplete */
    let autoComplete:any;

    const loadScript = (url: any, callback: any) => {
        let script:any = document.createElement("script");
        script.type = "text/javascript";

        if (script.readyState) {
            script.onreadystatechange = function() {
                if (script.readyState === "loaded" || script.readyState === "complete") {
                    script.onreadystatechange = null;
                    callback();
                }
            };
        } else {
            script.onload = () => callback();
        }

        script.src = url;
        document.getElementsByTagName("head")[0].appendChild(script);
    };

    function handleScriptLoad(updateQuery: any, autoCompleteRef: any, setError: any) {
        autoComplete = new window.google.maps.places.Autocomplete(
          autoCompleteRef.current
        );
        // autoComplete.setFields(["address_components", "formatted_address", "types"]);
        autoComplete.addListener("place_changed", () =>
            handlePlaceSelect(updateQuery, setError)
        );
    }

    async function handlePlaceSelect(updateQuery:any, setError:any) {
        const addressObject = autoComplete.getPlace();
        let IsCompleteAddress = false;
        let city;
        let state;
        let country;
        let postalCode;

        addressObject.address_components.forEach(function(item:any) {
            if(item.types.includes("administrative_area_level_2")){
                city = item.long_name;
            }
            if(item.types.includes("administrative_area_level_1")) {
                state = item.short_name;
            }
            if(item.types.includes("country")) {
                country = item.long_name;
            }
            if(item.types.includes("postal_code")){
                postalCode = item.long_name;
            }
        });
        setAddress({
            city: city,
            state: state,
            country: country,
            postalCode: postalCode,
            lat: addressObject.geometry.location.lat(),
            lng: addressObject.geometry.location.lng()
        });

      }

    
    /* !-----Google autocomplete */  

    const handleRestaurantForm = function(event: any){
        event.preventDefault();
        setShowRestaurantForm(true)
    }

    const handleSubmit = function(event: any) {
        event.preventDefault();
        
        let obj = {} as CreateRestaurantFields;

        // Get input fields inserting to OBJ
        for (const item of event.target){
            obj[item["name"] as keyof CreateRestaurantFields] = item["value"]
        }
        setInputFields(obj)
    }

    const getImage = function(event: any) {
        console.log(event.files[0]);
        setImageOBJ(event.files[0]);
    }

    const requestAddImageAndRestaurant = useCallback(() => {
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
                await RequestPost({
                    url: url,
                    bodyData: bodyFormData,
                    header: {
                        headers: {
                            'Content-Type': 'multipart/form-data',
                            'Authorization': `Bearer ${cookies.authentication.access_token}`
                        }
                    }
                }).then(async (response) => {

                    if (response.status == 201) {

                        // Build URL to Add Restaurant
                        let url = configData.UPLIT_API.URL;
                        url += configData.UPLIT_API.RESOURCES.VIRTUALSHOP;
                        
                        // Make add restaurant
                        await RequestPost({
                            url: url, 
                            bodyData: {
                                name: inputFields.name,
                                phoneNumber: inputFields.phoneNumber,
                                address: {
                                    AddressLine1: inputFields.AddressLine1,
                                    city: getAddress.city,
                                    stateProvinceRegion: getAddress.state,
                                    country: getAddress.country,
                                    postalCode: getAddress.postalCode,
                                    lat: getAddress.lat,
                                    long: getAddress.lng
                                },
                                image: response.data.id
                            },
                            header: {
                                headers: {
                                    'Content-Type': 'application/json',
                                    'Authorization': `Bearer ${cookies.authentication.access_token}`
                                }
                            }
                        }).then((response) => {
                            console.log("Add restaurant", response.data);

                            // Empty object fields 
                            setInputFields({});

                            // Empty Image OBJ
                            setImageOBJ(null);

                            if (response.status == 201) {

                                console.log("Add restaurant", response.data);
                                
                                // Update current cookie
                                // let currentCookie = cookies.authentication;
                                // currentCookie["has_virtualshop"] = true;
                                // currentCookie["virtualshop"] = {
                                //     id: response.data.id,
                                //     url: response.data.url,
                                //     name: response.data.name
                                // }

                                // removeCookie("authentication");
                                setCookie("virtualshop", response.data);


                                // Set Errors none and success block
                                setErrorDisplay("none");
                                window.location.href = "/home";

                            } else {
                                setErrorDisplay("block");
                            }

                        }).catch((error) => {
                            // Empty object fields 
                            setInputFields({});

                             // Set Errors none and success block
                             setErrorDisplay("block");
                        });
                    }
                }).catch((error) => {
                    console.log(error);
                    setErrorDisplay("block");
                });

            }

        })();
    }, [inputFields]);

    useEffect(() => {
        requestAddImageAndRestaurant();
    }, [requestAddImageAndRestaurant])


    return (
        <Fragment>
            <TopBarComponent>
                <TopBarLogoComponent grid="col-md-3"/>
                <TopBarSearchAreaComponent grid="col-md-6" />
                <TopBarProfileComponent grid="col-md-3" profileName={(cookies.authentication) ? cookies.authentication.seller.user.first_name : "Unknown"} />
            </TopBarComponent>
            <HeaderComponent>
                <MenuListItems>
                    <OtherCategory />
                </MenuListItems>
            </HeaderComponent>
            <AddRestaurantComponent
                handleSubmit={handleSubmit}
                handleRestaurantForm={handleRestaurantForm}
                ErrorDisplay={errorDisplay}
                showRestaurantForm={showRestaurantForm}
                getImage={getImage}
                loadScript={loadScript} 
                handleScriptLoad={handleScriptLoad} 
            />
        </Fragment>
    )
}