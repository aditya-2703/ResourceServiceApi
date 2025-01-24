package com.ideabazaar.resource.resourceserviceapi.controller;


import com.ideabazaar.resource.resourceserviceapi.dto.ResourceDTO;
import com.ideabazaar.resource.resourceserviceapi.exception.ResourceNotFound;
import com.ideabazaar.resource.resourceserviceapi.model.Resource;
import com.ideabazaar.resource.resourceserviceapi.service.ResourceService;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping(value = "/api/",produces = MediaType.APPLICATION_JSON_VALUE)
public class ResourceController {

    ResourceService resourceService;
    ResourceController(ResourceService resourceService) {
        this.resourceService = resourceService;
    }

    // C - Project
    @PostMapping("/resource/create")
    public ResponseEntity<ResourceDTO> createResource(@RequestBody ResourceDTO resourceDTO) {
        ResourceDTO udpatedresourceDTO = this.resourceService.createResource(resourceDTO);
        return new ResponseEntity<>(udpatedresourceDTO, HttpStatus.CREATED);
    }

    // R - all
    @GetMapping("/resources")
    public ResponseEntity<List<ResourceDTO>> getAllResources() {
        List<ResourceDTO> resoucesdto = this.resourceService.getAllResources();
        return new ResponseEntity<>(resoucesdto, HttpStatus.OK);
    }
    // R - single
    @GetMapping("/resource/{id}")
    public ResponseEntity<ResourceDTO> getSingleResource(@PathVariable Long id) throws ResourceNotFound {
        ResourceDTO Projectdto = this.resourceService.getSingleResource(id);
        if(Projectdto == null) {
            throw new ResourceNotFound(id); // Throw the exception
        }
        return new ResponseEntity<>(Projectdto, HttpStatus.OK);
    }

    // U - update
    @PutMapping("/resource/")
    public ResponseEntity<ResourceDTO> updateResource(@RequestBody ResourceDTO resourceDTO) throws ResourceNotFound {
        ResourceDTO updatedProjectdto = this.resourceService.updateResource(resourceDTO);
        if(updatedProjectdto == null) {
            throw new ResourceNotFound(resourceDTO.getId());
        }
        return new ResponseEntity<>(updatedProjectdto, HttpStatus.OK);
    }

    // D - Delete
    @DeleteMapping("/resource/{id}")
    public ResponseEntity<String> deleteResource(@PathVariable Long id) throws ResourceNotFound {
        boolean isDeleted = this.resourceService.deleteResource(id);

        if (isDeleted) {
            return ResponseEntity.ok("Project  with ID " + id + " has been deleted."); // 200 OK with message
        } else {
            throw new ResourceNotFound(id);
        }
    }


    // Read all the project related to input userid
    @GetMapping("/customresources/{id}")
    public List<ResourceDTO> getAllResourceDTOByUserId(@PathVariable Long id) throws ResourceNotFound {
        List<ResourceDTO> allprojectData = this.resourceService.getResourcelistByProject(id);
//        return new ResponseEntity<>(allprojectData, HttpStatus.OK);
        return allprojectData;
    }
}

//  - **Resources**: `id`, `title`, `link`, `type (course/article)`

