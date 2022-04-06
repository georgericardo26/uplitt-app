import React from 'react';
import { IAlertProps, ItypeAlert } from '../../../interfaces/defaults';


const AlertComponent = function(props: IAlertProps){

    const { title, message, type, display } = props
   
    const typeAlert = {
        sucess: "alert-success",
        info: "alert-info",
        warning: "alert-warning",
        danger: "alert-danger",
        primary: "alert-primary",
        secondary: "alert-secondary",
        dark: "alert-dark",
        light: "alert-light"
    };

    return (
        <div className={`"alert ${typeAlert[props.type as keyof ItypeAlert]} alert-dismissible alert-component"`} style={{display: `${display}`}}>
            <strong>{title}</strong> {props.message}
        </div>
    )
}

export { AlertComponent }