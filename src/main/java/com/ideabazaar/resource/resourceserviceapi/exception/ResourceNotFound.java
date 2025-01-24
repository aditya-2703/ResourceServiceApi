package com.ideabazaar.resource.resourceserviceapi.exception;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.ResponseStatus;

@ResponseStatus(value = HttpStatus.INTERNAL_SERVER_ERROR)
public class ResourceNotFound extends Exception{

    public ResourceNotFound(Long id){
        super("Project is Not present in Database with id ="+id);
    }
}
