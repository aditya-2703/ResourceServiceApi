package com.ideabazaar.resource.resourceserviceapi.exception;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;

@ControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(ResourceNotFound.class)
    public ResponseEntity<String> handleUserNotFoundException(ResourceNotFound ex) {
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body("Project Not Found" + ex.getMessage());
    }
}
