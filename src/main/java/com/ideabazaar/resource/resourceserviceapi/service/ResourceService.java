package com.ideabazaar.resource.resourceserviceapi.service;

import com.ideabazaar.resource.resourceserviceapi.dto.ResourceDTO;
import com.ideabazaar.resource.resourceserviceapi.exception.ResourceNotFound;
import com.ideabazaar.resource.resourceserviceapi.mapper.ResourceMapper;
import com.ideabazaar.resource.resourceserviceapi.model.Resource;
import com.ideabazaar.resource.resourceserviceapi.repository.ResourceRepository;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

@Service
public class ResourceService {

    private ResourceRepository resourceRepository;

    public ResourceService(ResourceRepository resourceRepositoryabcd) {
        this.resourceRepository = resourceRepositoryabcd;
    }

    // C
    public ResourceDTO createResource(ResourceDTO resourceDTO) {
        // dto -> project
        Resource resource = ResourceMapper.INSTANCE.resourceDtoToResource(resourceDTO);
        // save to db
        Resource updatedproject = this.resourceRepository.save(resource);
        // project -> dto
        return ResourceMapper.INSTANCE.resourceToResourceDto(updatedproject);
    }

    // R
    public ResourceDTO getSingleResource(Long id) {
        Optional<Resource> project = this.resourceRepository.findById(id);
        // project -> dto
        return ResourceMapper.INSTANCE.resourceToResourceDto(project.get());
    }
    public List<ResourceDTO> getAllResources() {
        List<Resource> resources = this.resourceRepository.findAll();
        // project -> dto
        List<ResourceDTO> projectDTOs = new ArrayList<>();
        for (Resource resource: resources) {
            projectDTOs.add(ResourceMapper.INSTANCE.resourceToResourceDto(resource));
        }
        return projectDTOs;
    }

    // U
    public ResourceDTO updateResource(ResourceDTO projectDTO) {
        // dto -> user
        Resource user = ResourceMapper.INSTANCE.resourceDtoToResource(projectDTO);
        if(user!=null){
            Resource updateduser = this.resourceRepository.save(user);
            // user -> dto
            return ResourceMapper.INSTANCE.resourceToResourceDto(updateduser);
        }else{
            return null;
        }
    }


    // D
    public boolean deleteResource(Long id) throws ResourceNotFound {
        if (resourceRepository.existsById(id)) {
            resourceRepository.deleteById(id);
            return true;
        } else {
            throw new ResourceNotFound(id);
        }
    }

    // custom
    public List<ResourceDTO> getResourcelistByProject(Long id) {
        List<Resource> resourceslist = resourceRepository.findResourceByProjectId(id);
        List<ResourceDTO> resourceDTOs = new ArrayList<>();
        for(Resource resource : resourceslist){
            ResourceDTO resourceDTOobj = ResourceMapper.INSTANCE.resourceToResourceDto(resource);
            resourceDTOs.add(resourceDTOobj);
        }
        return resourceDTOs;
    }
}
