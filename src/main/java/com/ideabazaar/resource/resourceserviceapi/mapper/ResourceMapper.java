package com.ideabazaar.resource.resourceserviceapi.mapper;

import com.ideabazaar.resource.resourceserviceapi.dto.ResourceDTO;
import com.ideabazaar.resource.resourceserviceapi.model.Resource;
import org.mapstruct.Mapper;
import org.mapstruct.factory.Mappers;

@Mapper(componentModel = "spring")
public interface ResourceMapper {
    ResourceMapper INSTANCE = Mappers.getMapper(ResourceMapper.class);

    // Map fields from User -> UserDto
    ResourceDTO resourceToResourceDto(Resource user);

    // Map fields from UserDto -> User
    Resource resourceDtoToResource(ResourceDTO resourceDto);
}
